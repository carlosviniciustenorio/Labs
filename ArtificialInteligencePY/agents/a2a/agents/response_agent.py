from infra.message_bus import subscribe


def run():

    for msg in subscribe("response"):

        if msg["type"] == "analysis_result":

            print("\nFINAL RESPONSE\n")
            print(msg["payload"]["insight"])