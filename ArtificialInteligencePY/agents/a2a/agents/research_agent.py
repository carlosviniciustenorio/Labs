from infra.message_bus import subscribe, publish


def run():

    for msg in subscribe("research"):

        if msg["type"] == "research_request":

            topic = msg["payload"]["topic"]

            data = [
                "AI agents adoption is increasing",
                "Enterprises investing in automation",
                "Multi-agent systems becoming popular"
            ]

            publish("analysis", {
                "from": "research",
                "to": "analysis",
                "type": "research_result",
                "payload": {
                    "topic": topic,
                    "data": data
                }
            })