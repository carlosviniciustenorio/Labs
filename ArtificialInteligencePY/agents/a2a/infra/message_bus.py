import redis
import json

redis_client = redis.Redis(
    host="localhost",
    port=6379,
    decode_responses=True
)


def publish(channel, message):
    redis_client.publish(channel, json.dumps(message))


def subscribe(channel):

    pubsub = redis_client.pubsub()
    pubsub.subscribe(channel)

    for message in pubsub.listen():

        if message["type"] == "message":
            yield json.loads(message["data"])