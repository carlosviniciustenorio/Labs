
# 🧠 Explicação do Código de Inferência com Modelo Fine-Tuned com LoRA

Este código carrega um modelo base (ex: `flan-t5-small`), aplica os ajustes LoRA a partir de um diretório `checkpoint`, e gera uma resposta para um prompt textual.

---

## 📦 1. Imports

```python
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from peft import PeftModel, PeftConfig
import torch
```

| Módulo | Função |
|--------|--------|
| `AutoTokenizer` | Converte texto em tokens e vice-versa |
| `AutoModelForSeq2SeqLM` | Carrega o modelo base para tarefas de sequência para sequência |
| `PeftConfig`, `PeftModel` | Utilizados para aplicar LoRA (Low-Rank Adaptation) |
| `torch` | Biblioteca de deep learning (PyTorch) |

---

## 📁 2. Caminho para o checkpoint

```python
checkpoint_path = "./output/checkpoint-9"
```

Define o caminho onde estão os arquivos gerados durante o fine-tuning com LoRA:
- `adapter_model.safetensors`
- `adapter_config.json`

---

## ⚙️ 3. Carregando a configuração LoRA

```python
peft_config = PeftConfig.from_pretrained(checkpoint_path)
```

- Lê o `adapter_config.json`
- Obtém:
  - Nome do modelo base (`base_model_name_or_path`)
  - Hiperparâmetros LoRA (`r`, `alpha`, `dropout`, etc.)

---

## 🧠 4. Carregando o modelo base

```python
base_model = AutoModelForSeq2SeqLM.from_pretrained(peft_config.base_model_name_or_path)
```

Carrega o modelo base original (como `google/flan-t5-small`) **sem os ajustes LoRA ainda**.

---

## 🧬 5. Aplicando os pesos LoRA ao modelo base

```python
model = PeftModel.from_pretrained(base_model, checkpoint_path)
```

Aplica os pesos LoRA ao modelo base, usando:
- `adapter_model.safetensors`
- `adapter_config.json`

O resultado é um modelo leve e personalizado.

---

## ✅ 6. Colocando o modelo em modo de inferência

```python
model.eval()
```

- Desativa dropout, batchnorm, etc.
- Recomendado antes de fazer previsões (`inference`)

---

## 🧾 7. Carregando o tokenizer

```python
tokenizer = AutoTokenizer.from_pretrained(checkpoint_path)
```

Carrega o tokenizer do checkpoint (ou do modelo base, se preferir), necessário para:
- Codificar texto → tokens
- Decodificar tokens → texto

---

## 💬 8. Definindo o prompt e tokenizando

```python
prompt = "Who is the only God?"
inputs = tokenizer(prompt, return_tensors="pt")
```

- Define o prompt a ser respondido
- Converte para tensores PyTorch com `input_ids` e `attention_mask`

---

## 🚀 9. Gerando a resposta com o modelo

```python
with torch.no_grad():
    outputs = model.generate(
        input_ids=inputs["input_ids"],
        attention_mask=inputs["attention_mask"],
        max_new_tokens=50,
        do_sample=True,
        top_p=0.9,
        temperature=0.8
    )
```

| Parâmetro        | Função |
|------------------|--------|
| `torch.no_grad()` | Desativa o cálculo de gradientes (mais leve e rápido) |
| `max_new_tokens` | Limita a resposta a até 50 tokens novos |
| `do_sample`      | Ativa geração amostrada (em vez de determinística) |
| `top_p`          | Usa nucleus sampling para escolher tokens |
| `temperature`    | Controla a aleatoriedade (menor = mais conservador) |

---

## 📤 10. Decodificando e exibindo a resposta

```python
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```

- Converte os tokens gerados de volta para texto
- Remove tokens especiais (`<pad>`, `<eos>`, etc.)

---