from typing import TypedDict
from langgraph.graph import StateGraph, END
from langchain_community.chat_models import ChatOllama

class Estado(TypedDict):
    pergunta: str
    resposta: str

llm = ChatOllama(model="mistral", temperature=0)

def responder(state: Estado) -> Estado:
    pergunta = state["pergunta"]
    resposta = llm.invoke(pergunta).content
    return {"resposta": resposta}

graph = StateGraph(Estado)
graph.add_node("responder", responder)
graph.set_entry_point("responder")
graph.add_edge("responder", END)

app = graph.compile()

resultado = app.invoke({"pergunta": "Explique Kafka em uma frase."})
print(resultado["resposta"])
