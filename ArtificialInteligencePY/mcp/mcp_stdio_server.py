import sys
import json
import uuid


def send(message: dict):
    sys.stdout.write(json.dumps(message) + "\n")
    sys.stdout.flush()


def handle_initialize(msg):
    send({
        "id": msg["id"],
        "type": "result",
        "server": "Simple MCP Server",
        "version": "1.0"
    })


def handle_list_tools(msg):
    tools = [
        {
            "name": "add",
            "description": "Soma dois números",
            "input_schema": {
                "type": "object",
                "properties": {
                    "a": {"type": "number"},
                    "b": {"type": "number"}
                },
                "required": ["a", "b"]
            },
            "output_schema": {
                "type": "object",
                "properties": {
                    "result": {"type": "number"}
                }
            }
        }
    ]

    send({
        "id": msg["id"],
        "type": "result",
        "tools": tools
    })


def handle_call_tool(msg):
    tool = msg["tool"]
    args = msg["arguments"]

    if tool == "add":
        result = args["a"] + args["b"]
        send({
            "id": msg["id"],
            "type": "result",
            "content": {"result": result}
        })
    else:
        send({
            "id": msg["id"],
            "type": "error",
            "message": f"Tool '{tool}' not found"
        })


HANDLERS = {
    "initialize": handle_initialize,
    "list_tools": handle_list_tools,
    "call_tool": handle_call_tool,
}


def main():
    for line in sys.stdin:
        try:
            msg = json.loads(line.strip())
            handler = HANDLERS.get(msg["type"])

            if not handler:
                send({
                    "id": msg.get("id"),
                    "type": "error",
                    "message": "Unknown message type"
                })
                continue

            handler(msg)

        except Exception as e:
            send({
                "id": None,
                "type": "error",
                "message": str(e)
            })


if __name__ == "__main__":
    main()
