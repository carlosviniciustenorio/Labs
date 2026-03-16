# 🤖 Fine-Tuning com LoRA – Resumo Completo

---

## 📌 O que é Fine-Tuning?

Fine-tuning é o processo de pegar um modelo pré-treinado (como `flan-t5`, `bert`, `llama`) e ajustá-lo em um conjunto de dados específico, para uma tarefa personalizada.

- **Vantagem**: Aproveita o "conhecimento geral" do modelo e adapta para um domínio específico com menos dados.
- **Problema**: Fine-tuning completo é **custoso**, pois envolve atualizar todos os parâmetros do modelo.

---

## 🧩 O que é LoRA (Low-Rank Adaptation)?

**LoRA** é uma técnica que reduz o custo e o tempo do fine-tuning.

### ✨ Como funciona:
- Em vez de atualizar todos os parâmetros do modelo base, LoRA **insere camadas extras leves (low-rank)** dentro do modelo e **só essas camadas são treinadas**.
- O modelo base **permanece congelado**.

### 📦 Vantagens:
- Muito mais leve (poucos MBs vs vários GBs)
- Permite treinar em notebooks ou GPUs baratas
- Os adaptadores LoRA podem ser facilmente carregados e aplicados em tempo de execução

---

## 📁 Estrutura típica dos arquivos após fine-tuning com LoRA

Após o treinamento, o Hugging Face Trainer + PEFT gera um diretório como `output/checkpoint-X/`.

### Arquivos principais:

| Arquivo                     | Descrição                                                                 |
|----------------------------|---------------------------------------------------------------------------|
| `adapter_model.safetensors` | ✅ **Pesos LoRA treinados** (os "deltas" adaptados sobre o modelo base)   |
| `adapter_config.json`      | ✅ Configuração da LoRA (parâmetros como `r`, `alpha`, dropout, task type) |
| `tokenizer.json`           | ✅ Tokenizer serializado em JSON (pode ser usado no deploy)                |
| `tokenizer_config.json`    | ✅ Metadados do tokenizer (ex: se ele usa padding lateral, truncamento)    |
| `special_tokens_map.json`  | ✅ Mapeia tokens especiais como `[PAD]`, `[EOS]`, etc.                      |

---

### Arquivos auxiliares (checkpoint de treinamento):

| Arquivo                 | Utilidade                                                |
|------------------------|----------------------------------------------------------|
| `optimizer.pt`         | Estado do otimizador (usado para retomar treinamento)    |
| `scheduler.pt`         | Estado do scheduler de LR                                |
| `trainer_state.json`   | Progresso do treino, logs e métrica                      |
| `training_args.bin`    | Hiperparâmetros usados no treino                         |
| `rng_state.pth`        | Estado aleatório (para reprodutibilidade)                |
| `README.md`            | Texto padrão gerado pelo Hugging Face Trainer            |

**🔒 Observação**: Esses arquivos auxiliares **não são necessários para inferência**, apenas para continuar o treinamento.

---

## 🚀 Como reutilizar os arquivos em produção

Para fazer inferência com o modelo LoRA:

1. **Carregue o modelo base** (ex: `google/flan-t5-small`)
2. **Aplique os pesos LoRA** usando os arquivos:
   - `adapter_model.safetensors`
   - `adapter_config.json`

### Código exemplo:
```python
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from peft import PeftModel

base_model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-small")
model = PeftModel.from_pretrained(base_model, "./checkpoint-9/")
tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-small")

```

📦 Compactando para Deploy
Recomenda-se zipar:

```pgsql
adapter_model.safetensors
adapter_config.json
(optional) tokenizer_config.json

```

E subir para S3 ou embutir no seu container/Docker para uso com:
- Lambda
- ECS Fargate
- SageMaker
- EC2/API REST