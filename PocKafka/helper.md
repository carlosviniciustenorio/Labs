docker exec kafka kafka-topics --create --topic meu-topico --partitions 1 --replication-factor 1 --bootstrap-server localhost:9092
docker exec kafka1 kafka-topics --create --topic meu-topico --partitions 3 --replication-factor 3 --bootstrap-server localhost:9092
docker exec kafka1 kafka-topics --alter --topic meu-topico --partitions 3 --bootstrap-server kafka:9092
docker exec kafka1 kafka-topics --delete --topic meu-topico --bootstrap-server kafka:9092
docker exec kafka1 kafka-topics --describe --topic meu-topico --bootstrap-server localhost:9092

chmod +x gerar-certificados.sh
./gerar-certificados.sh

---

### Kafka vs RabbitMQ: Diferenças principais

| Aspecto                 | Apache Kafka                                                                         | RabbitMQ                                                                                  |
| ----------------------- | ------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------- |
| **Modelo**              | Pub/Sub + Log distribuído                                                            | Fila de mensagens tradicional (MQ) + Pub/Sub                                              |
| **Arquitetura**         | Sistema distribuído, baseado em logs imutáveis (partições com offset)                | Broker tradicional, roteia mensagens para filas, suporte a vários protocolos (AMQP, MQTT) |
| **Mensagens**           | Armazenadas por tempo/configuração, mensagens persistem e podem ser relidas (replay) | Consumidas e removidas da fila, foco em entrega única                                     |
| **Escalabilidade**      | Altamente escalável horizontalmente, cluster com vários brokers                      | Escalável, mas geralmente mais complexo para clusters muito grandes                       |
| **Garantia de entrega** | Pelo menos uma vez, exatamente uma vez (com configuração complexa)                   | Suporta pelo menos uma vez, pode ser configurado para exatamente uma vez                  |
| **Ordem das mensagens** | Garantida por partição (ordem sequencial dentro da partição)                         | Ordem não garantida entre filas e consumidores, mas pode ser configurada dentro da fila   |
| **Casos de uso**        | Processamento de streams, ingestão de dados, event sourcing, análise em tempo real   | Processamento de tarefas, sistemas tradicionais de mensageria, integração entre sistemas  |
| **Performance**         | Alta taxa de transferência para grandes volumes de dados                             | Mais flexível, porém com overhead maior em cenários de alto throughput                    |
| **Protocolos**          | Proprietário (Kafka protocol)                                                        | AMQP, MQTT, STOMP, HTTP e outros                                                          |
| **Complexidade**        | Requer configuração mais elaborada, curva de aprendizado maior                       | Mais fácil de começar, mais maduro para casos de filas tradicionais                       |

---

### Resumo rápido:

* **Kafka** é ótimo para **streams de dados em alta escala, persistência de eventos e processamento em tempo real**. A mensagem fica armazenada e pode ser lida várias vezes, permitindo replays.

* **RabbitMQ** é mais indicado para **filas tradicionais, roteamento flexível e integração de sistemas** com garantias imediatas de entrega, menos foco em armazenamento de longo prazo.


--------------------------------------------

---

### 1. **Limite de tamanho de mensagem no Kafka**

* **Tamanho padrão máximo**: 1 MB por mensagem (configuração padrão: `message.max.bytes` no broker e `max.request.size` no cliente).
* **Pode ser aumentado**: até cerca de 10 MB ou mais, ajustando essas configurações, mas aumentar demais impacta a performance e o uso de memória.
* **Prática comum**: mensagens muito grandes (ex: arquivos, vídeos) **não são recomendadas** no Kafka. Para esses casos, o ideal é enviar apenas o caminho/URL para o dado, armazenado em um sistema de arquivos distribuído (S3, HDFS, etc).

---

### 2. **Quando usar Kafka**

* Para **processamento de eventos em alta escala e streaming de dados em tempo real**.
* Quando precisa de **persistência das mensagens** para múltiplos consumidores lerem em momentos diferentes (replay).
* Para casos de **event sourcing, logs distribuídos, ingestão massiva de dados**.
* Quando deseja **alta taxa de transferência, alta durabilidade e ordenação garantida por partição**.

---

### 3. **Quando usar AWS SNS**

* Para **pub/sub simples e escalável na nuvem**, especialmente quando você quer **notificar múltiplos sistemas/serviços** (ex: Lambda, HTTP endpoints, emails, SMS).
* SNS não armazena mensagens, é focado em **entrega imediata** para assinantes (fan-out).
* Útil quando deseja **integração fácil com outros serviços AWS**.
* Ideal para notificações, alertas, disparo de eventos simples, e quando não precisa de armazenamento ou processamento complexo.

---

### Resumo simples:

| Kafka                                     | AWS SNS                                 |
| ----------------------------------------- | --------------------------------------- |
| Mensagens grandes (>1MB) não recomendadas | Tamanho máximo \~256 KB (limite do SNS) |
| Persistência + replay                     | Entrega imediata, sem armazenamento     |
| Altíssima taxa de dados/streams           | Pub/Sub para notificações simples       |
| Controla consumo por offset               | Push para assinantes (push-based)       |
| Complexidade e manutenção maior           | Simples, gerenciado pela AWS            |

---

Se você precisa de **streaming, replay e alta taxa**, Kafka.
Se precisa de **notificações rápidas, fan-out fácil e integração com AWS**, SNS.