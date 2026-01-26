import os
import re
import faiss
import numpy as np
from typing import TypedDict, Optional
from langsmith import traceable
from langchain_ollama import ChatOllama
from langgraph.graph import StateGraph, END
from sentence_transformers import SentenceTransformer


perceptor_llm = ChatOllama(model="mistral", temperature=3)
context_llm = ChatOllama(model="mistral", temperature=3)
planner_llm = ChatOllama(model="mistral", temperature=3)
tool_llm = ChatOllama(model="mistral", temperature=3)
executor_llm = ChatOllama(model="mistral", temperature=3)
validator_llm = ChatOllama(model="mistral", temperature=3)
retry_llm = ChatOllama(model="mistral", temperature=3)

class State(TypedDict):
    ask: str
    perception: Optional[str]
    context: bool
    planner: Optional[str]
    tool_discovery: Optional[str]
    executor: Optional[str]
    validator: Optional[str]
    retry: Optional[str]
    attemps: Optional[int]
    
@traceable
def perception(state: State) -> dict:
    prompt = f"""You're a perceptor.
        Ask:{state['ask']}
        You need to know wheter you will need get tools to solve the question or just keep to the next step"""
    response = perceptor_llm.invoke(prompt).content
    return {"perception": response}
    
    
@traceable
def context(state: State) -> dict:
    return ""
    
@traceable
def planner(state: State) -> dict:
    prompt = f"""You need to plan your next steps based on state
        perception: {state['perception']}
        context: {state['context']}
    """
    response = planner_llm.invoke(prompt).content
    return {"planner": response}

@traceable
def tool_discovery(state: State) -> dict:
    return ""

@traceable
def executor(state: State) -> dict:
    prompt = f"""You should execute the plan that was planned by plan step. Don't change nothing.
        Plan: {state['plan']}
    """
    response = executor_llm.invoke(prompt)
    return {"executor": response, "attemps": state['attemps'] + 1}

@traceable
def validator(state: State) -> dict:
    prompt = f"""You need to validator the response that will be returned to the user wheter it does make sense
    Response: {state['executor']}
    """
    response = validator_llm.invoke(prompt).content
    return {"validator": response}

if __name__ == "__main__":
    