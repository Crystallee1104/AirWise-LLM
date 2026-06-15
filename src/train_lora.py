
from datasets import load_dataset
from transformers import AutoTokenizer, AutoModelForCausalLM, TrainingArguments
from peft import LoraConfig
from trl import SFTTrainer
import torch

MODEL_NAME = "Qwen/Qwen2.5-0.5B-Instruct"

SYSTEM_PROMPT = (
    "You are an environmental health and sensor data assistant. "
    "Give accurate, concise, domain-specific explanations. "
    "Focus on personal exposure, microenvironments, ventilation, infiltration, "
    "sensor data quality, modelling assumptions, and uncertainty where relevant. "
    "Do not provide medical advice."
)

def main():
    print("Loading dataset...")
    dataset = load_dataset(
        "json",
        data_files={
            "train": "data/train.jsonl",
            "eval": "data/eval.jsonl"
        }
    )

    print(dataset)

    print("Loading tokenizer...")
    tokenizer = AutoTokenizer.from_pretrained(
        MODEL_NAME,
        trust_remote_code=True
    )

    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    def format_example(example):
        messages = [
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": example["instruction"]
            },
            {
                "role": "assistant",
                "content": example["response"]
            }
        ]

        return tokenizer.apply_chat_template(
            messages,
            tokenize=False,
            add_generation_prompt=False
        )

    print("Loading model...")
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_NAME,
        dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
        device_map="auto",
        trust_remote_code=True
    )

    print("Setting LoRA config...")
    lora_config = LoraConfig(
        r=16,
        lora_alpha=32,
        lora_dropout=0.05,
        bias="none",
        task_type="CAUSAL_LM",
        target_modules=[
            "q_proj", "k_proj", "v_proj", "o_proj",
            "gate_proj", "up_proj", "down_proj"
        ]
    )

    training_args = TrainingArguments(
        output_dir="outputs/airwise-lora-chat",
        num_train_epochs=10,
        per_device_train_batch_size=1,
        per_device_eval_batch_size=1,
        gradient_accumulation_steps=4,
        learning_rate=8e-5,
        logging_steps=5,
        eval_strategy="epoch",
        save_strategy="epoch",
        fp16=torch.cuda.is_available(),
        report_to="none",
        save_total_limit=2
    )

    print("Starting training...")
    trainer = SFTTrainer(
        model=model,
        args=training_args,
        train_dataset=dataset["train"],
        eval_dataset=dataset["eval"],
        peft_config=lora_config,
        formatting_func=format_example,
    )

    trainer.train()

    print("Saving final LoRA model...")
    trainer.save_model("outputs/airwise-lora-chat-final")
    tokenizer.save_pretrained("outputs/airwise-lora-chat-final")

    print("Training finished!")

if __name__ == "__main__":
    main()
