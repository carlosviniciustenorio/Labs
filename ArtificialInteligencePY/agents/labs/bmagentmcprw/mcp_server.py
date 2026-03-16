import json
import uuid
import time
import os
import requests
from fastapi import FastAPI, Header, HTTPException, Request
from fastapi.responses import StreamingResponse

app = FastAPI(title="MCP Server - Streamable JSON-RPC")

API_KEY = "super-secret-key"
SESSIONS = {}

EXTERNAL_ANUNCIOS_URL = os.getenv(
    "ANUNCIOS_API_URL",
    "http://localhost:8000/api/anuncios"
)

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


# ---------------- CORE ----------------

def validate_api_key(x_api_key: str):
    if x_api_key != API_KEY:
        raise HTTPException(401, "Invalid API Key")


def validate_session(session_id: str):
    if session_id not in SESSIONS:
        raise HTTPException(401, "Invalid session")


def rpc_initialize(params):
    session_id = str(uuid.uuid4())
    SESSIONS[session_id] = {"created_at": time.time()}
    return {"sessionId": session_id, "tools": TOOLS}


def rpc_list_tools(params):
    return TOOLS


def rpc_call_tool(params):
    name = params["name"]
    args = params.get("arguments", {})

    if name == "get_ads":
        resp = requests.get(
            EXTERNAL_ANUNCIOS_URL,
            params={"take": args.get("take", 5)},
            timeout=10,
        )
        resp.raise_for_status()
        return resp.json()

    if name == "rag_search":
        time.sleep(2)
        return {"query": args.get("query"), "docs": ["doc1", "doc2"]}

    raise Exception("Tool not found")


# ---------------- STREAMABLE RPC ----------------

@app.post("/rpc")
async def rpc_endpoint(
    request: Request,
    x_api_key: str = Header(..., alias="x-api-key"),
    session_id: str | None = Header(None, alias="session-id"),
):
    validate_api_key(x_api_key)

    payload = await request.json()

    method = payload["method"]
    params = payload.get("params", {})
    rpc_id = payload["id"]

    if method != "initialize":
        if not session_id:
            raise HTTPException(401, "Missing session-id")
        validate_session(session_id)

    def stream():
        try:
            yield json.dumps({"type": "start", "id": rpc_id}) + "\n"

            if method == "initialize":
                result = rpc_initialize(params)

            elif method == "tools/list":
                result = rpc_list_tools(params)

            elif method == "tools/call":
                yield json.dumps({"type": "tool_start", "tool": params["name"]}) + "\n"

                for i in range(3):
                    time.sleep(0.5)
                    yield json.dumps({"type": "progress", "step": i}) + "\n"

                result = rpc_call_tool(params)

            else:
                raise Exception("Unknown method")

            yield json.dumps({
                "jsonrpc": "2.0",
                "id": rpc_id,
                "result": result,
            }) + "\n"

        except Exception as e:
            yield json.dumps({
                "jsonrpc": "2.0",
                "id": rpc_id,
                "error": {"message": str(e)},
            }) + "\n"

    return StreamingResponse(stream(), media_type="application/json")