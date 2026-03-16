from infra.message_bus import subscribe, publish


def run():

    for msg in subscribe("planner"):

        if msg["type"] == "user_request":

            topic = msg["payload"]["topic"]

            publish("research", {
                "from": "planner",
                "to": "research",
                "type": "research_request",
                "payload": {
                    "topic": topic
                }
            })