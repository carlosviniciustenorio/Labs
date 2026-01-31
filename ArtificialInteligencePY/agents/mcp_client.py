import requests


class MCPClient:
    def __init__(self, base_url="http://localhost:9001", api_key="super-secret-key"):
        self.base_url = base_url
        self.api_key = api_key
        self.session_id = None

    def handshake(self):
        r = requests.post(
            f"{self.base_url}/handshake",
            headers={"x-api-key": self.api_key},
            timeout=10,
        )
        r.raise_for_status()
        self.session_id = r.json()["session_id"]

    def _headers(self):
        if not self.session_id:
            self.handshake()

        return {
            "x-api-key": self.api_key,
            "session_id": self.session_id,
        }

    def list_tools(self):
        r = requests.get(
            f"{self.base_url}/tools",
            headers=self._headers(),
            timeout=10,
        )
        r.raise_for_status()
        return r.json()

    def call(self, tool_name: str, args: dict):
        if tool_name == "rag_search":
            r = requests.post(
                f"{self.base_url}/rag/query",
                json=args,
                headers=self._headers(),
                timeout=10,
            )
            r.raise_for_status()
            return r.json()

        if tool_name == "get_ads":
            r = requests.get(
                f"{self.base_url}/api/anuncios",
                params=args,
                headers=self._headers(),
                timeout=10,
            )
            r.raise_for_status()
            return r.json()

        raise ValueError(f"Tool not found: {tool_name}")