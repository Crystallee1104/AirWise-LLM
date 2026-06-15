
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from peft import PeftModel

BASE_MODEL = "Qwen/Qwen2.5-0.5B-Instruct"
LORA_MODEL = "outputs/airwise-lora-chat-final"
OUTPUT_FILE = "results/sample_outputs_chat.md"

QUESTIONS = [
    "Why is personal exposure not always the same as outdoor concentration?",
    "How can missing GPS data affect exposure analysis?",
    "Why is timestamp consistency important in multimodal sensor datasets?",
    "Explain why a model-derived exposure metric should include uncertainty discussion.",
    "What does LoRA fine-tuning demonstrate in this project?",
    "How would you handle missing values in high-frequency air pollution sensor data?",
    "What is outdoor-generated personal exposure?",
    "Why is ventilation important for indoor air pollution modelling?"
]

SYSTEM_PROMPT = "You are an environmental health and sensor data assistant. Give accurate, concise, domain-specific explanations. Do not provide medical advice."

def build_inputs(tokenizer, question, device):
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": question}
    ]

    text = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True
    )

    return tokenizer(text, return_tensors="pt").to(device)

def generate_answer(model, tokenizer, question):
    inputs = build_inputs(tokenizer, question, model.device)

    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=180,
            do_sample=False,
            pad_token_id=tokenizer.eos_token_id,
            eos_token_id=tokenizer.eos_token_id
        )

    generated_tokens = outputs[0][inputs["input_ids"].shape[-1]:]
    answer = tokenizer.decode(generated_tokens, skip_special_tokens=True)
    return answer.strip()

def main():
    print("Loading tokenizer...")
    tokenizer = AutoTokenizer.from_pretrained(BASE_MODEL, trust_remote_code=True)

    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    print("Loading base model...")
    base_model = AutoModelForCausalLM.from_pretrained(
        BASE_MODEL,
        dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
        device_map="auto",
        trust_remote_code=True
    )

    print("Generating base model answers...")
    base_answers = {}
    for q in QUESTIONS:
        base_answers[q] = generate_answer(base_model, tokenizer, q)

    del base_model
    torch.cuda.empty_cache()

    print("Loading model again for LoRA adapter...")
    tuned_base = AutoModelForCausalLM.from_pretrained(
        BASE_MODEL,
        dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
        device_map="auto",
        trust_remote_code=True
    )

    finetuned_model = PeftModel.from_pretrained(tuned_base, LORA_MODEL)

    print("Generating fine-tuned model answers...")
    tuned_answers = {}
    for q in QUESTIONS:
        tuned_answers[q] = generate_answer(finetuned_model, tokenizer, q)

    lines = []
    lines.append("# Sample Outputs: Base Model vs LoRA Fine-Tuned Model\n")
    lines.append("This file compares responses from the base Qwen2.5-0.5B-Instruct model and a LoRA fine-tuned version for environmental health question answering.\n")
    lines.append("The fine-tuned model was trained on a small curated instruction-response dataset covering air pollution exposure, sensor data quality control, exposure modelling, and environmental health concepts.\n")
    lines.append("This is an exploratory domain-adaptation prototype, not a validated medical or regulatory tool.\n")

    for i, question in enumerate(QUESTIONS, start=1):
        lines.append(f"\n## Example {i}\n")
        lines.append(f"**Question:** {question}\n")
        lines.append("\n### Base model answer\n")
        lines.append(base_answers[question] + "\n")
        lines.append("\n### LoRA fine-tuned model answer\n")
        lines.append(tuned_answers[question] + "\n")
        lines.append("\n### Observation\n")
        lines.append("Compare whether the fine-tuned model provides more domain-specific wording, better exposure-science terminology, and clearer discussion of sensor data or modelling assumptions.\n")

    with open(OUTPUT_FILE, "w") as f:
        f.write("\n".join(lines))

    print(f"Saved comparison outputs to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
