from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import ToolMessage
from langsmith import traceable
from mcp.http.mcp_tool_http import add_numbers


llm = ChatOllama(
    model="mistral",
    temperature=0
)

tools = [add_numbers]
llm_with_tools = llm.bind_tools(tools)

prompt = ChatPromptTemplate.from_messages([
    ("system", "Você é o MathAgent. Sempre use ferramentas quando houver cálculo."),
    ("human", "{input}")
])

@traceable(name="run_agent")
def run_agent(user_input: str):
    chain = prompt | llm_with_tools
    response = chain.invoke({"input": user_input})

    print("\n🔹 Model response:")
    print(response)

    if response.tool_calls:
        tool_messages = []

        for call in response.tool_calls:
            name = call["name"]
            args = call["args"]

            print(f"\n🛠 Executando tool: {name}({args})")

            if name == "add_numbers":
                result = add_numbers.invoke(args)

                tool_messages.append(
                    ToolMessage(
                        tool_call_id=call["id"],
                        content=str(result),
                    )
                )

        final_response = llm_with_tools.invoke(
            [response, *tool_messages]
        )

        return final_response.content

    return response.content


if __name__ == "__main__":
    result = run_agent("Use a tool to sum 12 and 30 and tell me the result.")
    print("\n✅ Final Answer:")
    print(result)
