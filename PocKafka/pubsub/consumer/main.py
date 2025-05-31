from confluent_kafka import Consumer

conf = {
  'bootstrap.servers': 'localhost:9092',
  'group.id': 'meu-grupo',
  'auto.offset.reset': 'earliest',
}


consumer = Consumer(conf)
consumer.subscribe(['meu-topico'])

print("Aguardando mensagens... (Ctrl+C para sair)")
try:
    while True:
        msg = consumer.poll(timeout=1.0)
        if msg is None:
            continue
        if msg.error():
            print(f"Erro: {msg.error()}")
        else:
            print(f"Recebido: {msg.value().decode('utf-8')} [partição {msg.partition()}]")
except KeyboardInterrupt:
    pass
finally:
    consumer.close()
