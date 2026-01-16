import re
import faiss
import numpy as np
from typing import TypedDict, Optional

from sentence_transformers import SentenceTransformer
from langchain_ollama import ChatOllama
from langgraph.graph import StateGraph, END


# =========================
# 1. RAG
# =========================

def smart_chunk(text, max_length=120):
    sentences = re.split(r'(?<=[.!?]) +', text)
    chunks, current = [], ""
    for s in sentences:
        if len(current) + len(s) <= max_length:
            current += s + " "
        else:
            chunks.append(current.strip())
            current = s + " "
    if current:
        chunks.append(current.strip())
    return chunks


docs_raw = [
    "Apache Kafka is a distributed event streaming platform used for building real-time data pipelines.",
    "AWS Lambda is a serverless compute service that runs code in response to events.",
    "Amazon S3 is an object storage service with high durability and availability.",
    "CloudFront is a content delivery network that caches content globally."
]

docs = []
for d in docs_raw:
    docs.extend(smart_chunk(d))

embedder = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
embeddings = embedder.encode(docs)

index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(np.array(embeddings))


def retrieve(query: str, k=2) -> str:
    q_emb = embedder.encode([query])
    _, ids = index.search(np.array(q_emb), k)
    return "\n".join(docs[i] for i in ids[0])


# =========================
# 2. Estado
# =========================

class Estado(TypedDict):
    pergunta: str
    contexto: Optional[str]
    resposta: Optional[str]
    critica: Optional[str]
    tentativas: int
    precisa_contexto: bool
    resposta_boa: bool


# =========================
# 3. Modelos (agentes)
# =========================

decisor_llm = ChatOllama(model="mistral", temperature=0)
gerador_llm = ChatOllama(model="mistral", temperature=0)
critico_llm = ChatOllama(model="mistral", temperature=0)


# =========================
# 4. Nós
# =========================

def decidir_contexto(state: Estado) -> dict:
    prompt = f"""
Você é um orquestrador.
Pergunta: {state['pergunta']}
Responda apenas "sim" ou "não":
Essa pergunta precisa de contexto externo para ser respondida corretamente?
"""
    resp = decisor_llm.invoke(prompt).content.lower()
    return {"precisa_contexto": "sim" in resp}


def buscar_contexto(state: Estado) -> dict:
    return {"contexto": retrieve(state["pergunta"])}


def gerar_resposta(state: Estado) -> dict:
    prompt = f"""
Você é um especialista técnico.
Use o contexto se existir.

Contexto:
{state.get("contexto")}

Pergunta:
{state['pergunta']}

Resposta:
"""
    resposta = gerador_llm.invoke(prompt).content
    return {"resposta": resposta, "tentativas": state["tentativas"] + 1}


def criticar_resposta(state: Estado) -> dict:
    prompt = f"""
Você é um revisor técnico rigoroso.
Pergunta: {state['pergunta']}
Resposta: {state['resposta']}

Avalie se a resposta é correta, objetiva e útil.
Responda no formato:
OK: sim ou não
Crítica: <texto curto>
"""
    out = critico_llm.invoke(prompt).content.lower()

    ok = "ok: sim" in out
    critica = out.split("crítica:")[-1].strip() if "crítica:" in out else out

    return {"resposta_boa": ok, "critica": critica}


def melhorar_resposta(state: Estado) -> dict:
    prompt = f"""
Você é um especialista melhorando sua própria resposta.
Pergunta: {state['pergunta']}
Resposta anterior: {state['resposta']}
Crítica: {state['critica']}

Escreva uma versão melhorada e objetiva:
"""
    resposta = gerador_llm.invoke(prompt).content
    return {"resposta": resposta}


# =========================
# 5. Grafo
# =========================

graph = StateGraph(Estado)

graph.add_node("decidir", decidir_contexto)
graph.add_node("buscar", buscar_contexto)
graph.add_node("gerar", gerar_resposta)
graph.add_node("criticar", criticar_resposta)
graph.add_node("melhorar", melhorar_resposta)

graph.set_entry_point("decidir")

graph.add_conditional_edges(
    "decidir",
    lambda s: "buscar" if s["precisa_contexto"] else "gerar"
)

graph.add_edge("buscar", "gerar")
graph.add_edge("gerar", "criticar")

graph.add_conditional_edges(
    "criticar",
    lambda s: END if s["resposta_boa"] or s["tentativas"] >= 3 else "melhorar"
)

graph.add_edge("melhorar", "criticar")

app = graph.compile()


# =========================
# 6. Execução
# =========================

if __name__ == "__main__":
    estado_inicial: Estado = {
        "pergunta": "Explique o que é Kafka em uma frase.",
        "contexto": None,
        "resposta": None,
        "critica": None,
        "tentativas": 0,
        "precisa_contexto": False,
        "resposta_boa": False
    }

    resultado = app.invoke(estado_inicial)

    print("\nResposta final:")
    print(resultado["resposta"])
    print("\nCrítica final:")
    print(resultado["critica"])
    print("\nTentativas:", resultado["tentativas"])
