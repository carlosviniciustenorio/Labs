from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from peft import PeftModel, PeftConfig
import torch

checkpoint_path = "./output/checkpoint-9"
peft_config = PeftConfig.from_pretrained(checkpoint_path)
base_model = AutoModelForSeq2SeqLM.from_pretrained(peft_config.base_model_name_or_path)
model = PeftModel.from_pretrained(base_model, checkpoint_path)
model.eval()
tokenizer = AutoTokenizer.from_pretrained(checkpoint_path)
prompt = "Who is the only God?"
inputs = tokenizer(prompt, return_tensors="pt")

with torch.no_grad():
    outputs = model.generate(
        input_ids=inputs["input_ids"],
        attention_mask=inputs["attention_mask"],
        max_new_tokens=50,
        do_sample=True,
        top_p=0.9,
        temperature=0.8
    )

print(tokenizer.decode(outputs[0], skip_special_tokens=True))
