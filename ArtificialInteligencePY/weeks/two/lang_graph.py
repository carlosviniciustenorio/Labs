import faiss
import numpy as np
import re
from typing import TypedDict, Optional
from langgraph.graph import StateGraph, END
from langchain_ollama import ChatOllama
from sentence_transformers import SentenceTransformer

def smart_chunk(text, max_length=100):
    sentences = re.split(r'(?<=[.!?]) +', text)
    chunks = []
    current = ""

    for sentence in sentences:
        if len(current) + len(sentence) <= max_length:
            current += sentence + " "
        else:
            chunks.append(current.strip())
            current = sentence + " "

    if current:
        chunks.append(current.strip())

    return chunks


docs_raw = [
    "AWS Lambda is a serverless compute service that runs your code in response to events. It scales automatically.",
    "ECS Fargate is a serverless compute engine for containers from AWS. It allows you to run containers without managing servers.",
    "S3 is an object storage service for storing files. It is durable and highly available.",
    "CloudFront is a CDN service that delivers content with low latency. It caches content globally.",
    "Apache Kafka is a streaming events plataform."
]

docs = []
for d in docs_raw:
    docs.extend(smart_chunk(d))

embedder = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
embeddings = embedder.encode(docs)

print(f'EMBEDDINGS: {np.array(embeddings)}')

dim = embeddings.shape[1]  # 384
index = faiss.IndexFlatL2(dim)
index.add(np.array(embeddings))

print("Index criado com sucesso!")
print(f"Total de chunks indexados: {len(docs)}")


def search(query, k=2):
    q_emb = embedder.encode([query])
    _, ids = index.search(np.array(q_emb), k)
    return [docs[i] for i in ids[0]]

class Estado(TypedDict):
    pergunta: str
    contexto: Optional[str]
    resposta: Optional[str]
    tentativas: int
    ok: bool
    precisa_contexto: bool


llm = ChatOllama(model="mistral", temperature=0)


def decidir_contexto(state: Estado) -> dict:
    precisa = "?" in state["pergunta"] or "o que é" in state["pergunta"].lower()
    return {"precisa_contexto": precisa}


def buscar_contexto(state: Estado) -> dict:
    context = search(state["pergunta"], 2)[0]
    return {"contexto": context}


def gerar_resposta(state: Estado) -> dict:
    prompt = f"""
Você é um engenheiro de software sênior.
Contexto: {state.get("contexto")}
Pergunta: {state["pergunta"]}
Responda de forma objetiva.
"""
    resposta = llm.invoke(prompt).content
    return {
        "resposta": resposta,
        "tentativas": state["tentativas"] + 1
    }


def avaliar_resposta(state: Estado) -> dict:
    ok = state["resposta"] is not None and len(state["resposta"]) < 200
    return {"ok": ok}


graph = StateGraph(Estado)

graph.add_node("decidir", decidir_contexto)
graph.add_node("buscar", buscar_contexto)
graph.add_node("gerar", gerar_resposta)
graph.add_node("avaliar", avaliar_resposta)

graph.set_entry_point("decidir")

graph.add_conditional_edges(
    "decidir",
    lambda s: "buscar" if s["precisa_contexto"] else "gerar"
)

graph.add_edge("buscar", "gerar")
graph.add_edge("gerar", "avaliar")

graph.add_conditional_edges(
    "avaliar",
    lambda s: END if s["ok"] or s["tentativas"] >= 3 else "gerar"
)

app = graph.compile()

if __name__ == "__main__":
    estado_inicial: Estado = {
        "pergunta": "Explique o que é Kafka em uma frase.",
        "contexto": None,
        "resposta": None,
        "tentativas": 0,
        "ok": False,
        "precisa_contexto": False
    }

    resultado = app.invoke(estado_inicial)

    print("\nResposta final:")
    print(resultado["resposta"])
    print("\nTentativas:", resultado["tentativas"])