from confluent_kafka import DeserializingConsumer
from confluent_kafka.serialization import StringDeserializer
from confluent_kafka.schema_registry import SchemaRegistryClient
from confluent_kafka.schema_registry.avro import AvroDeserializer

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

value_deserializer = AvroDeserializer(schema_registry_client, value_schema_str, lambda obj, ctx: obj)

consumer_conf = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'meu-grupo',
    'auto.offset.reset': 'earliest',
    'key.deserializer': StringDeserializer('utf_8'),  # chave string simples
    'value.deserializer': value_deserializer
}

consumer = DeserializingConsumer(consumer_conf)
topic = "meu-topico"
consumer.subscribe([topic])

try:
    while True:
        msg = consumer.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            print(f"Erro: {msg.error()}")
            continue
        print(f"Chave: {msg.key()}, Valor: {msg.value()}")

except KeyboardInterrupt:
    pass
finally:
    consumer.close()