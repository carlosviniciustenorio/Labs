# Lambda Sink Connector – Comportamento Profundo e Operacional

### 1. **Envio de mensagens (Batching)**

* O **Kafka Connect Sink Connector** (incluindo o Lambda Sink Connector) geralmente trabalha com **batching**:

  * Ele consome mensagens do Kafka em lotes para otimizar throughput e reduzir overhead de chamadas.
  * O tamanho do lote (batch size) e o tempo máximo de espera (linger.ms ou flush.interval.ms) são configuráveis no Kafka Connect.
  * Isso significa que o conector envia **um lote de mensagens** de uma só vez para a AWS Lambda, não mensagem a mensagem individualmente.

* No caso do Lambda Sink Connector oficial:

  * O conector envia um array JSON com as mensagens para a Lambda, que deve ser capaz de processar essa lista.
  * Isso melhora a eficiência, mas a Lambda precisa estar preparada para lidar com múltiplas mensagens por invocação.

---

### 2. **Tamanho máximo da mensagem/lote**

* A Lambda tem limite de tamanho de payload por invocação, que é **6 MB (payload total de evento)**.
* Logo, o tamanho do batch enviado pelo connector deve estar abaixo disso para evitar erros.
* Também há limites no Kafka Connect para tamanho máximo de lote, que devem ser configurados para garantir que o payload fique dentro do permitido.
* Caso o lote ultrapasse o limite, o conector falha e pode tentar reenvio (depende da configuração).

---

### 3. **Tratamento de erros e retry**

* Se a entrega do lote para a Lambda **falhar na chamada de invoke** (ex: erro de rede, Lambda indisponível), o conector geralmente:

  * **Faz retry automático** com backoff configurável (retry.backoff.ms, etc).
  * Bloqueia o commit do offset no Kafka até que a entrega seja bem-sucedida (garantindo pelo menos uma entrega).
  * Isso evita perda de mensagens, mas pode travar o consumo se o problema persistir.

* Se a Lambda processar o evento, mas **a execução da função falhar** (erro no código, timeout, exceção não tratada):

  * O Lambda responde com erro ao conector.
  * O conector entende que a entrega falhou e também fará retry do lote, bloqueando offset.
  * **Isso pode gerar reprocessamento de mensagens (mensagens duplicadas) até que Lambda processe corretamente**.

---

### 4. **Dead Letter Queue (DLQ) e estratégias de retry**

* O **Lambda Sink Connector oficial não tem DLQ nativo** para mensagens que falham repetidamente.

* Portanto, a prática comum é:

  * Criar um **tópico Kafka de retry ou dead-letter** (DLQ) separado.
  * Implementar um mecanismo externo (ex: outra Lambda, consumidor, ou job) que consuma o tópico de retry e trate as mensagens manualmente ou com lógica customizada (ex: alertas, limpeza, correção).
  * Isso evita travar o pipeline principal.

* Alternativamente, pode-se configurar o AWS Lambda com **DLQ nativo do Lambda** (SQS ou SNS) para mensagens que falham após retries do Lambda, mas isso é separado do Kafka Connect.

---

### 5. **Garantias de entrega e idempotência**

* O Kafka Connect com Lambda Sink Connector geralmente oferece **"at least once"**:

  * Ou seja, mensagens podem ser processadas mais de uma vez, pois a confirmação (offset commit) só ocorre após sucesso da Lambda.
  * Idempotência deve ser garantida na função Lambda para evitar efeitos colaterais ao reprocessar mensagens duplicadas.

---

### 6. **Configurações importantes para controlar comportamento**

* `tasks.max` — número máximo de tarefas paralelas do conector (afeta paralelismo).
* `batch.size` e `batch.flush.timeout.ms` — tamanho e frequência do envio de lotes.
* `retry.backoff.ms` — intervalo entre tentativas de retry.
* `max.retries` — número máximo de tentativas antes de falhar.
* Configurações específicas para controle de falhas e logs.

---

# Resumo prático para entrevista

| Tópico                           | Explicação                                                                                      |
| -------------------------------- | ----------------------------------------------------------------------------------------------- |
| **Batching**                     | Envia mensagens em lotes para Lambda, que recebe array JSON com múltiplas mensagens.            |
| **Limite de tamanho**            | Tamanho total do lote < 6MB (limite payload Lambda). Configurar batch size para respeitar isso. |
| **Erros na entrega**             | Kafka Connect faz retry da invocação Lambda, bloqueia commit do offset até sucesso.             |
| **Erro no processamento Lambda** | Lambda retorna erro, Connect reenvia o lote, pode ter duplicação (at least once).               |
| **DLQ**                          | Não há DLQ nativo no Lambda Sink Connector; usar tópico Kafka separado para retry ou DLQ.       |
| **Idempotência**                 | Deve ser garantida na Lambda para evitar efeitos adversos no reprocessamento.                   |

---