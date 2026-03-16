from transformers import (
    AutoTokenizer,
    AutoModelForSeq2SeqLM,
    Seq2SeqTrainingArguments,
    Seq2SeqTrainer,
    DataCollatorForSeq2Seq
)
from datasets import load_dataset
from peft import get_peft_model, LoraConfig, TaskType
import torch

model_name = "google/flan-t5-small"

tokenizer = AutoTokenizer.from_pretrained(model_name)

model = AutoModelForSeq2SeqLM.from_pretrained(
    model_name,
    torch_dtype=torch.float32
)

peft_config = LoraConfig(
    task_type=TaskType.SEQ_2_SEQ_LM,
    r=4,
    lora_alpha=8,
    lora_dropout=0.1,
    bias="none"
)
model = get_peft_model(model, peft_config)

data = load_dataset("json", data_files="dataset.json")

def tokenize(example):
    input_text = f"Pergunta: {example['prompt']}"
    target_text = example["response"]
    return tokenizer(input_text, text_target=target_text, truncation=True, padding="max_length", max_length=128)

tokenized_data = data["train"].map(tokenize)

training_args = Seq2SeqTrainingArguments(
    output_dir="./output",
    per_device_train_batch_size=1,
    num_train_epochs=3,
    fp16=False, 
    logging_steps=1,
    save_steps=10,
    save_total_limit=1,
    save_strategy="epoch",
    report_to="none"
)

trainer = Seq2SeqTrainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_data,
    tokenizer=tokenizer,
    data_collator=DataCollatorForSeq2Seq(tokenizer, model=model)
)

trainer.train()