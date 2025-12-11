# 🧠 Roteiro de Estudos — IA Generativa com Python (8 Semanas)

> **Objetivo:** dominar o uso de LLMs, RAG e agentes inteligentes em Python, com foco prático em IA Generativa.  
> **Resultado final:** você será capaz de criar, personalizar e publicar aplicações inteligentes (chatbots, copilotos e agentes).

---

## 🗓️ Semana 1 — Fundamentos e Ferramentas Base

🎯 **Objetivo:** montar o ambiente e entender como LLMs funcionam.

### Estude
- Conceitos: *tokens*, *embeddings*, *attention*, *transformers*, *fine-tuning*, *RAG*
- Diferença entre GPT, LLaMA, Mistral, Claude
- Rodar modelos locais com **Ollama**

### Ferramentas
- [Ollama](https://ollama.ai)
- [OpenAI API](https://platform.openai.com/docs)
- [Hugging Face Transformers](https://huggingface.co/docs/transformers/index)

### Prática
- Instalar **Python 3.10+**, **VSCode**, **Jupyter**
- Rodar `ollama run mistral`
- Fazer chamadas à API do OpenAI com `openai` SDK

### 🧩 Mini-projeto
Criar um script Python que faz perguntas ao GPT e salva as respostas em um arquivo `.txt`.

---

## 🧠 Semana 2 — Prompt Engineering

🎯 **Objetivo:** aprender a se comunicar de forma estruturada com LLMs.

### Estude
- Tipos de prompts: *system*, *user*, *few-shot*, *chain-of-thought*
- Técnicas: *role prompting*, *persona*, *zero-shot vs few-shot*

### Ferramentas
- [OpenAI API Playground](https://platform.openai.com/playground)
- [LangChain Prompt Templates](https://python.langchain.com/docs/modules/model_io/prompts/)

### 🧩 Mini-projeto
Criar um **gerador de e-mails** com diferentes estilos (formal, criativo, técnico).

---

## 🔍 Semana 3 — Embeddings e Busca Semântica

🎯 **Objetivo:** entender como representar texto em vetores e fazer busca semântica.

### Estude
- O que é *embedding*
- Similaridade vetorial (cosine similarity)
- Introdução a bancos vetoriais (FAISS, Chroma)

### Ferramentas
- [Sentence Transformers](https://www.sbert.net/)
- [FAISS](https://github.com/facebookresearch/faiss)
- [Chroma](https://docs.trychroma.com/)

### 🧩 Mini-projeto
Criar uma **busca semântica local** que lê um texto ou PDF e retorna trechos similares à pergunta.

---

## 📚 Semana 4 — RAG (Retrieval-Augmented Generation)

🎯 **Objetivo:** conectar um LLM aos seus próprios dados.

### Estude
- Conceito e arquitetura de RAG
- Pipelines com **LangChain** e **LlamaIndex**
- Estratégias de chunking e indexação

### Ferramentas
- [LangChain](https://python.langchain.com/)
- [LlamaIndex](https://docs.llamaindex.ai/)
- [Chroma](https://docs.trychroma.com/)

### 🧩 Mini-projeto
Criar um **chat com base em documentos locais (PDF/MD)** usando LangChain + Chroma + GPT/Ollama.

---

## ⚙️ Semana 5 — Fine-tuning e Personalização

🎯 **Objetivo:** adaptar modelos para domínios específicos.

### Estude
- *Fine-tuning*, *LoRA*, *QLoRA*, *PEFT*
- Diferença entre fine-tuning completo e leve

### Ferramentas
- [Transformers](https://huggingface.co/docs/transformers/training)
- [PEFT](https://huggingface.co/docs/peft)
- [BitsAndBytes](https://github.com/TimDettmers/bitsandbytes)

### 🧩 Mini-projeto
Treinar um modelo pequeno (ex: `distilGPT2`) com exemplos próprios e avaliar resultados.

---

## 🤖 Semana 6 — Agentes e Cadeias de Raciocínio

🎯 **Objetivo:** criar fluxos inteligentes e agentes autônomos.

### Estude
- Conceito de *agents*, *tools* e *chains*
- LangChain Agents, CrewAI e Autogen
- Memória de contexto e ferramentas externas

### Ferramentas
- [LangChain Agents](https://python.langchain.com/docs/modules/agents/)
- [CrewAI](https://github.com/joaomdmoura/crewAI)
- [Autogen (Microsoft)](https://github.com/microsoft/autogen)

### 🧩 Mini-projeto
Criar um **agente que responde perguntas e usa APIs externas** (ex: busca no Google, previsão do tempo).

---

## 💻 Semana 7 — Deploy e Integração

🎯 **Objetivo:** disponibilizar sua IA como serviço.

### Estude
- Criação de APIs com **FastAPI**
- Contêineres com **Docker**
- Deploy em **Hugging Face Spaces**

### Ferramentas
- [FastAPI](https://fastapi.tiangolo.com/)
- [Docker](https://docs.docker.com/)
- [Hugging Face Spaces](https://huggingface.co/spaces)

### 🧩 Mini-projeto
Deployar seu chatbot RAG ou agente em **Hugging Face Spaces** com API pública.

---

## 🧩 Semana 8 — Ética, Segurança e Guardrails

🎯 **Objetivo:** garantir segurança e confiabilidade no uso de LLMs.

### Estude
- *Prompt injection*, *data leakage*, *bias*, *hallucination*
- Guardrails e moderação de conteúdo

### Ferramentas
- [Guardrails AI](https://github.com/guardrails-ai/guardrails)
- [OpenAI Moderation API](https://platform.openai.com/docs/guides/moderation)
- [NVIDIA NeMo Guardrails](https://github.com/NVIDIA/NeMo-Guardrails)

### 🧩 Mini-projeto
Adicionar validações ao chatbot: filtros de conteúdo e respostas seguras.

---

## ✅ Resultado Final

Ao fim das 8 semanas, você será capaz de:

- Rodar e integrar LLMs (open-source e APIs)
- Criar pipelines RAG com dados próprios
- Fine-tunar modelos de linguagem
- Construir e publicar agentes inteligentes
- Aplicar boas práticas de segurança e ética em IA

---

## 📘 Recursos Recomendados

- 📗 [Hugging Face Course (gratuito)](https://huggingface.co/learn)
- 📘 [LangChain Tutorials](https://python.langchain.com/docs/tutorials/)
- 🎥 [FreeCodeCamp – LLMs e LangChain](https://www.youtube.com/watch?v=zIZ0hWvF6nA)
- 📚 [OpenAI Cookbook](https://github.com/openai/openai-cookbook)
- 💬 [Awesome LLM Apps](https://github.com/Hannibal046/Awesome-LLM)

---

## 🧾 Checklist de Progresso

| Semana | Tema | Status |
|--------|------|--------|
| 1 | Fundamentos e Ferramentas | ☐ |
| 2 | Prompt Engineering | ☐ |
| 3 | Embeddings e Busca Semântica | ☐ |
| 4 | RAG | ☐ |
| 5 | Fine-tuning | ☐ |
| 6 | Agentes | ☐ |
| 7 | Deploy | ☐ |
| 8 | Ética e Segurança | ☐ |