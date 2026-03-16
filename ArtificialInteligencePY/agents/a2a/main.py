import multiprocessing
import time

from agents import planner_agent
from agents import research_agent
from agents import analysis_agent
from agents import response_agent

from infra.message_bus import publish


def start_agents():

    multiprocessing.Process(target=planner_agent.run).start()
    multiprocessing.Process(target=research_agent.run).start()
    multiprocessing.Process(target=analysis_agent.run).start()
    multiprocessing.Process(target=response_agent.run).start()


def send_request():

    publish("planner", {
        "from": "user",
        "to": "planner",
        "type": "user_request",
        "payload": {
            "topic": "AI Agents market"
        }
    })


if __name__ == "__main__":

    start_agents()

    time.sleep(2)

    send_request()