from confluent_kafka import SerializingProducer
from confluent_kafka.serialization import StringSerializer
from confluent_kafka.schema_registry import SchemaRegistryClient
from confluent_kafka.schema_registry.avro import AvroSerializer
import uuid

schema_registry_conf = {'url': 'http://localhost:8081'}
schema_registry_client = SchemaRegistryClient(schema_registry_conf)

value_schema_str = """
{
  "type": "record",
  "name": "User",
  "fields": [
    {"name": "id", "type": "string"},
    {"name": "email", "type": "string"}
  ]
}
"""

value_serializer = AvroSerializer(schema_registry_client, value_schema_str, lambda obj, ctx: obj)

producer_conf = {
    'bootstrap.servers': 'localhost:9092',
    'key.serializer': StringSerializer('utf_8'),
    'value.serializer': value_serializer
}

producer = SerializingProducer(producer_conf)
topic = "meu-topico"

def delivery_report(err, msg):
    if err is not None:
        print(f"Falha na entrega: {err}")
    else:
        print(f"Mensagem entregue para {msg.topic()} [{msg.partition()}] no offset {msg.offset()}")

for i in range(10000):
    key = f"key-{uuid.uuid4()}"
    value = {"id": f"user{i}", "email": f"user{i}@exemplo.com"}
    producer.produce(topic=topic, key=key, value=value, on_delivery=delivery_report)

producer.flush()