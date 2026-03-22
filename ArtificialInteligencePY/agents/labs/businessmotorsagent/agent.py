import json
import re
from typing import TypedDict, Optional
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, END
from langfuse.langchain import CallbackHandler


handler = CallbackHandler()
llm = ChatOpenAI(
    model="openai/gpt-4o-mini",
    temperature=0.3,
    base_url="https://openrouter.ai/api/v1",
    api_key="",
    callbacks=[handler]
)

# ---------------- STATE ----------------

class State(TypedDict):
    ask: str
    enhance_prompt: Optional[str]
    perception: Optional[str]
    plan: Optional[str]
    executor: Optional[str]
    result: Optional[str]
    valid: Optional[bool]
    attempts: int


# --------------------- Nodes -----------------

def should_execute(state: State):
    prompt = f"""
        You're a motors agent, and should decide if the user prompt is clear or not to execute directly.
        - Rules:
         - If the user prompt is about motors (cars, motorcycles, etc.) and it's clear to execute, valid should be true.
         - If the user prompt is outside the motors domain or unclear, valid should be false.
         - Reply with JSON only using this schema: {{"valid": boolean, "reason": string}}.
         - reason should explain why the request was rejected when valid is false.
         - reason can be an empty string when valid is true.
        User prompt: {state['ask']}
    """

    r = llm.invoke(prompt).content
    try:
        parsed = json.loads(r)
        is_valid = bool(parsed.get("valid", False))
        reason = str(parsed.get("reason", "")).strip()
    except (json.JSONDecodeError, TypeError, ValueError):
        normalized = r.strip().lower()
        is_valid = normalized == "true"
        reason = "I can only answer questions about motors such as cars or motorcycles." if not is_valid else ""

    return {"valid": is_valid, "result": None if is_valid else reason}

def enhance_prompt(state: State):
    prompt = f"""
        You should enhrance the user prompt below
        
        User prompt: {state['ask']}
    """
    
    r = llm.invoke(prompt).content
    return {"enhance_prompt": r}

def perception(state: State):
    prompt = f"""
        You should percept the user intention
        
        User prompt: {state['enhance_prompt']}
    """
    
    r = llm.invoke(prompt).content
    return {"perception": r} 

def plan(state: State):
    prompt = f"""
        You should create a actionable plan to solve the perception
        
        User prompt: {state['enhance_prompt']}
        Perception: {state['perception']}
    """   
    r = llm.invoke(prompt).content
    return {"plan": r}

def executor(state: State):
    prompt = f"""
        Return a response for this plan below with the tools that you have
        
        User prompt: {state['enhance_prompt']}
        Perception: {state['perception']}
        Plan: {state['plan']}
    """
    
    r = llm.invoke(prompt).content
    return {
        "result": r,
        "attempts": state["attempts"] + 1
    }

def validator(state: State):
    prompt = f"""
        Valid if the result is valid or not
        RULES:
        - The response should be just a boolean true or false
        
        INFO:
        User prompt: {state['enhance_prompt']}
        Perception: {state['perception']}
        Plan: {state['plan']}
        Result: {state['result']}
    """
    r = llm.invoke(prompt).content
    return {"valid": "true" in r}

def should_continue(state: State):
    if state["valid"]:
        return "end"
    if state["attempts"] > 2:
        return "end"
    return "retry"

def execution_is_valid(state: State):
    if state["valid"]:
        return "continue"
    return "end"

# ----------------------  GRAPH ---------------------

graph = StateGraph(State)

graph.add_node("should_execute", should_execute)
graph.add_node("enhance_prompt", enhance_prompt)
graph.add_node("perception", perception)
graph.add_node("plan", plan)
graph.add_node("executor", executor)
graph.add_node("validator", validator)

graph.set_entry_point("should_execute")

graph.add_edge("enhance_prompt","perception")
graph.add_edge("perception", "plan")
graph.add_edge("plan", "executor")
graph.add_edge("executor", "validator")

graph.add_conditional_edges(
    "should_execute",
    execution_is_valid,
    {
        "continue": "enhance_prompt",
        "end": END,
    }
)
graph.add_conditional_edges(
    "validator", 
    should_continue, 
    {
        "retry": "enhance_prompt",
        "end": END
    }
)

agent = graph.compile()

# ------------------- Runner --------------------


if __name__ == "__main__":
    result = agent.invoke(
        {
            "ask": "Wich car is better in terms of performance, BMW 320i or BMW X1?",
            "attempts": 0
        },
        config={"callbacks": [handler]}
    )

    print("\nFINAL RESULT\n")
    print(result["result"])