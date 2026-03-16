# 📚 Tipos de Modelos em NLP e IA Generativa

---

## 1. Modelos Seq2Seq (Sequence-to-Sequence)

### O que são?
Modelos que recebem uma sequência de entrada e geram outra sequência como saída.

### Exemplos:
- **T5** (Text-to-Text Transfer Transformer)
- **BART**
- **RNN/LSTM seq2seq** (antes do Transformer)

### Aplicações:
- Tradução automática
- Resumo automático
- Pergunta e resposta (Q&A)
- Geração de texto condicional

---

## 2. Modelos Autoregressivos

### O que são?
Modelos que geram texto prevendo o próximo token com base nos tokens anteriores.

### Exemplos:
- **GPT (Generative Pre-trained Transformer)**
- **GPT-2, GPT-3, GPT-4**
- **GPT-Neo, GPT-J**

### Aplicações:
- Geração livre de texto (chatbots, assistentes)
- Completar frases e códigos
- Criar histórias, diálogos

---

## 3. Modelos Encoder-Only (Representação)

### O que são?
Modelos focados em criar representações (embeddings) para textos, não para geração.

### Exemplos:
- **BERT**
- **RoBERTa**
- **DistilBERT**

### Aplicações:
- Classificação de texto
- Detecção de sentimentos
- Similaridade textual
- Busca semântica

---

## 4. Modelos Encoder-Decoder (Transformer Seq2Seq)

### O que são?
Modelos com duas partes: encoder lê o texto, decoder gera texto. Muito usados para tradução, resumo, etc.

### Exemplos:
- **T5**
- **BART**

### Aplicações:
- Tradução
- Resumo
- Pergunta e resposta

---

## 5. Modelos Masked Language Models (MLM)

### O que são?
Modelos treinados para prever palavras faltando em uma frase.

### Exemplos:
- **BERT**
- **RoBERTa**

### Aplicações:
- Pré-treinamento
- Análise de sentimentos
- Extração de entidades

---

## 6. Modelos de Difusão (Diffusion Models)

### O que são?
Modelos probabilísticos para gerar dados complexos, muito usados em imagens, mas também em texto.

### Exemplos:
- **Imagen (Google)**
- **Stable Diffusion**

### Aplicações:
- Geração de imagens
- Multimodal (texto + imagem)

---

## 7. Modelos Multimodais

### O que são?
Modelos que entendem e geram dados em mais de um formato (texto, imagem, áudio).

### Exemplos:
- **CLIP (texto + imagem)**
- **DALL·E**
- **Flamingo (DeepMind)**

### Aplicações:
- Geração de imagens a partir de texto
- Busca multimodal
- Assistentes multimodais

---

## 8. Modelos Reinforcement Learning with Human Feedback (RLHF)

### O que são?
Modelos que aprendem a melhorar respostas com feedback humano, usados em sistemas de chat avançados.

### Exemplos:
- **ChatGPT**
- **InstructGPT**

### Aplicações:
- Chatbots com respostas mais naturais e seguras
- Assistentes virtuais avançados

---

# 📌 Resumo

| Tipo                   | Foco                | Exemplos          | Uso principal                  |
|------------------------|---------------------|-------------------|-------------------------------|
| Seq2Seq                | Entrada → Saída seq. | T5, BART          | Tradução, resumo, Q&A          |
| Autoregressivo         | Geração token a token| GPT-3, GPT-4      | Geração de texto livre         |
| Encoder-only           | Representação       | BERT, RoBERTa     | Classificação, busca           |
| Diffusion              | Modelagem probabilística | Stable Diffusion | Imagem, multimodal             |
| Multimodal             | Texto + outros dados | CLIP, DALL·E      | Geração multimodal             |
| RLHF                   | Aprendizado com feedback | ChatGPT          | Chatbots avançados             |

---