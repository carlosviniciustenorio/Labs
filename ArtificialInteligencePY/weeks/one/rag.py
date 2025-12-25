import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
import requests
import json
import re


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
    "CloudFront is a CDN service that delivers content with low latency. It caches content globally."
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


def ollama_generate(prompt):
    res = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": "mistral", "prompt": prompt},
        stream=True,
    )

    output = ""
    for line in res.iter_lines():
        if line:
            part = json.loads(line.decode())
            print(f'output part stream: {part}')
            output += part.get("response", "")
    return output

def rag_answer(question):
    results = search(question, k=2)
    context = "\n".join(results)

    final_prompt = f"""
Você é um assistente especializado.
Use APENAS o contexto abaixo para responder a pergunta.

Contexto:
{context}

Pergunta:
{question}

Resposta:
"""

    return ollama_generate(final_prompt)


if __name__ == "__main__":
    question = "What is the difference between ECS Fargate and AWS Lambda?"
    answer = rag_answer(question)
    print("\n=== RESPONSE ===\n")
    print(answer)
