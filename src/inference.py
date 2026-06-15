
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from peft import PeftModel

BASE_MODEL = "Qwen/Qwen2.5-0.5B-Instruct"
LORA_MODEL = "outputs/airwise-lora-final"

def build_prompt(question):
    return f"""### Instruction:
{question}

### Response:
"""

def generate_answer(model, tokenizer, question):
    prompt = build_prompt(question)
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=220,
            temperature=0.7,
            top_p=0.9,
            do_sample=True,
            pad_token_id=tokenizer.eos_token_id
        )

    text = tokenizer.decode(outputs[0], skip_special_tokens=True)

    if "### Response:" in text:
        return text.split("### Response:")[-1].strip()
    return text.strip()

def main():
    print("Loading tokenizer...")
    tokenizer = AutoTokenizer.from_pretrained(BASE_MODEL, trust_remote_code=True)

    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    print("Loading base model...")
    base_model = AutoModelForCausalLM.from_pretrained(
        BASE_MODEL,
        torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
        device_map="auto",
        trust_remote_code=True
    )

    print("Loading fine-tuned LoRA model...")
    finetuned_model = PeftModel.from_pretrained(base_model, LORA_MODEL)

    questions = [
        "Explain the difference between ambient air pollution and personal exposure.",
        "How would you handle missing data in high-frequency air pollution sensor data?",
        "What is outdoor-generated personal exposure?",
        "Why is temporal alignment important when combining GPS, accelerometer and pollutant data?"
    ]

    for q in questions:
        print("=" * 100)
        print("Question:", q)
        print("-" * 100)
        print("Fine-tuned model answer:")
        print(generate_answer(finetuned_model, tokenizer, q))
        print()

if __name__ == "__main__":
    main()
