import requests
from fastapi import FastAPI, Header, HTTPException, Query
from pydantic import BaseModel
from rag import retrieve
import uuid
import time
import os

app = FastAPI(title="MCP Server")

API_KEY = "super-secret-key"
SESSIONS = {}

EXTERNAL_ANUNCIOS_URL = os.getenv(
    "ANUNCIOS_API_URL",
    "http://localhost:8000/api/anuncios"
)
TIMEOUT = 10


# ---------------- AUTH ----------------

def validate_api_key(x_api_key: str):
    if x_api_key != API_KEY:
        raise HTTPException(401, "Invalid API Key")


def validate_session(session_id: str):
    if session_id not in SESSIONS:
        raise HTTPException(401, "Invalid session")


# ---------------- HANDSHAKE ----------------

@app.post("/handshake")
def handshake(x_api_key: str = Header(..., alias="x-api-key")):
    validate_api_key(x_api_key)

    session_id = str(uuid.uuid4())
    SESSIONS[session_id] = {"created_at": time.time()}
    return {"session_id": session_id}


# ---------------- MODELS ----------------

class RagRequest(BaseModel):
    query: str
    k: int = 2


# ---------------- TOOLS ----------------

TOOLS = {
    "rag_search": {
        "description": "Search knowledge base using RAG",
        "args": {"query": "string", "k": "int"},
    },
    "get_ads": {
        "description": "Fetch car ads from external REST API",
        "args": {"take": "int"},
    },
}


# ---------------- ENDPOINTS ----------------

@app.get("/tools")
def list_tools(
    session_id: str = Header(..., alias="session_id"),
    x_api_key: str = Header(..., alias="x-api-key"),
):
    validate_api_key(x_api_key)
    validate_session(session_id)
    return TOOLS


@app.post("/rag/query")
def rag_query(
    req: RagRequest,
    session_id: str = Header(..., alias="session_id"),
    x_api_key: str = Header(..., alias="x-api-key"),
):
    validate_api_key(x_api_key)
    validate_session(session_id)

    result = retrieve(req.query, req.k)
    return {"result": result}


@app.get("/api/anuncios")
def anuncios(
    take: int = Query(10),
    session_id: str = Header(..., alias="session_id"),
    x_api_key: str = Header(..., alias="x-api-key"),
):
    validate_api_key(x_api_key)
    validate_session(session_id)

    try:
        resp = requests.get(
            EXTERNAL_ANUNCIOS_URL,
            params={"take": take},
            timeout=TIMEOUT,
        )
        resp.raise_for_status()
    except requests.RequestException as e:
        raise HTTPException(502, f"External API error: {str(e)}")

    return resp.json()
