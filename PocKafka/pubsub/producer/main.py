from confluent_kafka import Producer

conf = {
    'bootstrap.servers': 'localhost:9092',
    'client.id': 'meu-produtor',
    'security.protocol': 'PLAINTEXT'  # padrão, sem SSL
}

producer = Producer(conf)

def delivery_report(err, msg):
    """Callback chamado para reportar sucesso ou erro no envio."""
    if err is not None:
        print(f'Erro ao enviar mensagem: {err}')
    else:
        print(f'Mensagem entregue no tópico {msg.topic()} partição {msg.partition()} offset {msg.offset()}')

topic = 'meu-topico'

for i in range(300):
    value = f'mensagem {i}'
    producer.produce(topic, value.encode('utf-8'), callback=delivery_report)
    # Dá uma chance para o delivery_report rodar e para o produtor enviar
    producer.poll(0)

producer.flush()  # Espera todas mensagens serem entregues antes de sair
