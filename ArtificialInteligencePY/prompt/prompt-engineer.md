# Prompt Engineering — Guia Profundo

## 1. O que é Prompt Engineering

Prompt Engineering é a disciplina de **projetar instruções eficazes para modelos de linguagem (LLMs)** para obter respostas mais **precisas, controladas e úteis**.

Um prompt não é apenas uma pergunta. Ele representa **todo o contexto fornecido ao modelo**.

Um prompt pode conter:

* **Role (papel do modelo)**
* **Instruções**
* **Contexto**
* **Exemplos**
* **Formato de saída**
* **Restrições**

Estrutura comum:

```
[ROLE]
[INSTRUCTION]
[CONTEXT]
[EXAMPLES]
[OUTPUT FORMAT]
[CONSTRAINTS]
```

Exemplo:

```
You are a senior backend engineer.

Explain what distributed transactions are.

Use simple language and give one real-world example.
```

---

# 2. Como LLMs interpretam prompts

Modelos de linguagem funcionam prevendo **a próxima palavra mais provável**.

Matematicamente:

```
P(next_token | context)
```

Ou seja, o modelo calcula a probabilidade da próxima palavra com base no contexto.

Prompt Engineering funciona porque **moldamos o espaço de probabilidade** do modelo.

Quanto mais:

* contexto
* estrutura
* restrições

mais previsível será a resposta.

---

# 3. Técnicas fundamentais de Prompt Engineering

## 3.1 Role Prompting

Definir o papel do modelo.

Exemplo:

```
You are a staff software engineer at a large tech company.
```

ou

```
You are a professor of distributed systems.
```

Isso influencia:

* vocabulário
* profundidade
* estilo de resposta

---

## 3.2 Instruction Prompting

Instruções claras reduzem ambiguidade.

Prompt ruim:

```
Explain Kafka.
```

Prompt melhor:

```
Explain Apache Kafka focusing on:

- partitions
- brokers
- leader election
- replication

Target audience: senior backend engineers.
```

---

## 3.3 Output Formatting

Controlar a estrutura da resposta.

Exemplo:

```
Return the answer using the following format:

Problem:
Solution:
Example:
```

Isso ajuda quando o output será usado por software.

---

## 3.4 Few-Shot Prompting

Ensinar o modelo com exemplos.

```
Classify the sentiment.

Text: I love this product
Sentiment: Positive

Text: This is terrible
Sentiment: Negative

Text: The delivery was slow
Sentiment:
```

Isso melhora tarefas de classificação.

---

## 3.5 Zero-Shot Prompting

Sem exemplos.

```
Translate to Portuguese:

I love software engineering.
```

---

## 3.6 Chain-of-Thought Prompting

Força o modelo a raciocinar passo a passo.

```
Solve the problem step by step.
```

ou

```
Let's think step by step.
```

Muito útil para:

* matemática
* lógica
* planejamento

---

## 3.7 Self-Consistency Prompting

Executar múltiplos raciocínios e escolher o mais consistente.

```
Generate 5 different reasoning paths and select the most consistent answer.
```

Usado em:

* modelos de reasoning
* sistemas de agentes

---

## 3.8 Tree of Thought (ToT)

Expansão do chain-of-thought.

O modelo explora múltiplos caminhos de raciocínio.

```
Step 1: generate possible solutions
Step 2: evaluate them
Step 3: choose the best
```

---

# 4. Prompt Templates

Sistemas profissionais usam **templates reutilizáveis**.

Exemplo:

```
SYSTEM:
You are a senior backend engineer.

USER:

Context:
{context}

Question:
{question}

Constraints:
- be concise
- use bullet points
```

Ferramentas comuns:

* LangChain
* LlamaIndex
* Semantic Kernel

---

# 5. Prompt Chaining

Dividir problemas complexos em múltiplos prompts.

Pipeline:

```
Prompt 1 → Extract information
Prompt 2 → Analyze information
Prompt 3 → Generate report
```

Exemplo de arquitetura:

```
User question
      ↓
Retriever (RAG)
      ↓
Context builder
      ↓
LLM
      ↓
Answer
```

---

# 6. Retrieval Augmented Generation (RAG)

RAG adiciona conhecimento externo ao prompt.

Arquitetura:

```
User question
     ↓
Vector search
     ↓
Relevant documents
     ↓
Prompt + context
     ↓
LLM
```

Prompt típico:

```
Answer using ONLY the context below.

Context:
{documents}

Question:
{question}
```

Benefício principal:

* reduz hallucinations.

---

# 7. Prompt Guardrails

Controlar comportamento do modelo.

Exemplo:

```
If you don't know the answer, say "I don't know".
Do not fabricate information.
```

Outro exemplo:

```
Only answer using the provided context.
```

---

# 8. Structured Prompting

Usado em sistemas com ferramentas.

Exemplo:

```
You are an AI agent.

Available tools:

- search_web
- calculate
- get_weather

When needed, call a tool.
Return the final answer after using tools.
```

Isso é usado em:

* AI agents
* tool calling
* MCP servers

---

# 9. ReAct Prompting (Reason + Act)

Técnica popular em agentes.

Estrutura:

```
Thought:
Action:
Observation:
Thought:
Final Answer:
```

Exemplo:

```
Question: What is the capital of the country where the Amazon river starts?

Thought: I need to find where the Amazon river starts.
Action: search("Amazon river source")
Observation: Peru

Thought: Now find the capital of Peru.
Action: search("capital of Peru")
Observation: Lima

Final Answer: Lima
```

---

# 10. Técnicas avançadas

## System Prompting

Prompt interno que define comportamento global do modelo.

```
You are ChatGPT, a helpful AI assistant.
```

---

## Instruction Hierarchy

Prioridade de instruções:

```
System > Developer > User
```

---

## Prompt Compression

Reduz tokens mantendo informação essencial.

Importante para:

* long context
* RAG pipelines

---

## Automatic Prompt Optimization

Ferramentas que otimizam prompts automaticamente.

Exemplos:

* DSPy
* AutoPrompt
* Prompt tuning

---

# 11. Prompt Engineering para Agentes

Nos agentes de IA, o prompt define:

* ferramentas disponíveis
* regras
* comportamento
* limites

Exemplo:

```
You are a coding agent.

Available tools:

- search_docs
- run_code
- read_file

Always plan before acting.
```

---

# 12. Prompt Engineering vs Spec-Driven AI

O campo está evoluindo para **Spec-Driven AI Systems**.

Onde definimos explicitamente:

* ferramentas
* schemas
* comportamento
* políticas

Exemplo:

```
Tool: create_user

Input schema:
{
  name: string
  email: string
}
```

Isso funciona como **contrato entre agentes e sistemas**.

---

# 13. Principais habilidades de um Prompt Engineer

1. Model mental models (entender como LLMs pensam)
2. Instruction design
3. Context engineering
4. Evaluation frameworks
5. Debugging de LLMs

---

# 14. O futuro: Context Engineering

Prompt Engineering está evoluindo para **Context Engineering**.

Ou seja, projetar todo o ambiente de decisão do modelo:

* memória
* retrieval
* ferramentas
* políticas
* especificações

Não se trata apenas de prompts, mas de **sistemas completos de IA**.

---

# 15. Exemplo profissional

Prompt usado em sistemas de suporte técnico:

```
You are a senior cloud support engineer.

Use the context below to answer the user's question.

If the answer is not in the context, say "I don't know".

Context:
{retrieved_docs}

User question:
{question}

Answer using:

- step-by-step explanation
- commands if necessary
```

---

# Conclusão

Prompt Engineering controla:

| Camada       | Função             |
| ------------ | ------------------ |
| Instructions | comportamento      |
| Context      | conhecimento       |
| Examples     | padrão de resposta |
| Format       | estrutura          |
| Tools        | capacidades        |

Insight principal:

**Os melhores engenheiros de IA não escrevem prompts — eles projetam sistemas de raciocínio para modelos.**

---
