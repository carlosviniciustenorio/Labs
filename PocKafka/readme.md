### Apache Kafka — Componentes e como funcionam

* **Cluster**
  Conjunto de brokers que juntos formam o Kafka. Garante alta disponibilidade e escalabilidade.

* **Broker**
  Servidor Kafka individual dentro do cluster. Armazena dados e atende requisições (produtores e consumidores).

* **Tópico (Topic)**
  Categoria ou feed onde as mensagens são publicadas. É a “fila lógica” no Kafka.

* **Partição (Partition)**
  Cada tópico é dividido em partições, que são segmentos ordenados e independentes dos dados.

  * Permite paralelismo (cada partição pode ser tratada por brokers e consumidores diferentes).
  * Cada mensagem dentro da partição tem um offset (posição única).

* **Produtor (Producer)**
  Envia mensagens para um tópico. Pode especificar para qual partição quer enviar a mensagem.

* **Consumidor (Consumer)**
  Lê mensagens dos tópicos (e partições). Pode ler de várias partições em paralelo.

* **Grupo de consumidores (Consumer Group)**
  Conjunto de consumidores que dividem o trabalho de consumir um tópico, cada partição é consumida por apenas um consumidor do grupo.

* **Offset**
  Posição sequencial da mensagem dentro da partição. Usado para rastrear o que já foi consumido.

* **Zookeeper (ou KRaft no Kafka moderno)**
  Serviço que gerencia a configuração e coordena o cluster (quem é líder, onde ficam as partições, etc). No Kafka mais novo, está sendo substituído pelo próprio Kafka (KRaft mode).

---

**Como funciona o fluxo básico:**
Produtores enviam mensagens para tópicos → tópicos armazenam as mensagens em partições distribuídas nos brokers → consumidores leem as mensagens das partições → offsets ajudam a controlar o progresso da leitura.