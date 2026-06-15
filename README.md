# AirWise-LLM: LoRA Fine-Tuning for Environmental Health Question Answering

## Overview

AirWise-LLM is a small applied generative AI project exploring parameter-efficient fine-tuning of an instruction-tuned language model for environmental health question answering.

The project uses LoRA fine-tuning to adapt a small language model to answer questions related to air pollution exposure, multimodal sensor data, personal exposure modelling, data quality control, and uncertainty communication.

This project was designed as a lightweight but complete demonstration of an end-to-end LLM adaptation workflow, including dataset curation, supervised fine-tuning, inference comparison, qualitative evaluation, and error analysis.

## Motivation

Large language models are increasingly used to support scientific workflows, but general-purpose models may not always provide sufficiently domain-specific explanations for specialised research topics.

Environmental health and personal exposure research involve concepts such as indoor infiltration, ventilation, microenvironments, time-activity patterns, sensor data quality, and model-derived uncertainty. This project explores whether a small language model can be adapted to provide more relevant explanations for these topics using a parameter-efficient fine-tuning approach.

## Project Goals

- Build a small domain-specific instruction-response dataset for environmental health question answering.
- Fine-tune a small instruction-tuned language model using LoRA.
- Compare responses from the base model and the fine-tuned model.
- Evaluate whether fine-tuning improves domain-specific terminology and explanation quality.
- Identify limitations and failure modes through qualitative error analysis.

## Model and Methods

### Base Model

The project uses `Qwen/Qwen2.5-0.5B-Instruct` as the base instruction-tuned language model.

### Fine-Tuning Method

The model is fine-tuned using LoRA, a parameter-efficient fine-tuning method. Instead of updating all model parameters, LoRA trains small adapter modules while keeping most of the original model weights frozen.

This makes it suitable for small-scale applied AI experiments where compute resources are limited.

### Tools

- Python
- PyTorch
- Hugging Face Transformers
- Hugging Face Datasets
- PEFT
- TRL
- Google Colab with GPU acceleration

## Dataset

A small curated instruction-response dataset was created for this project. The dataset covers:

- Personal exposure vs ambient outdoor concentration
- Indoor-generated and outdoor-generated exposure
- Indoor infiltration, ventilation, deposition, and filtration
- GPS and accelerometer data in exposure studies
- Timestamp alignment in multimodal sensor datasets
- Missing data handling in high-frequency sensor streams
- Sensor data quality control
- Model-derived exposure metrics and uncertainty
- LoRA fine-tuning and domain adaptation

The dataset is intentionally small and manually curated, as the aim of this project is to demonstrate the workflow rather than build a production-ready domain expert model.

## Repository Structure

```text
AirWise-LLM/
├── README.md
├── requirements.txt
├── data/
│   ├── train.jsonl
│   └── eval.jsonl
├── src/
│   ├── train_lora.py
│   ├── inference.py
│   ├── compare_outputs.py
│   └── evaluate.py
├── results/
│   ├── sample_outputs_chat.md
│   └── evaluation_summary.md
├── notebooks/
└── outputs/
```

## Training Workflow

1. Prepare curated instruction-response data in JSONL format.
2. Load the base instruction-tuned model and tokenizer.
3. Format examples using the model's chat template.
4. Apply LoRA configuration through PEFT.
5. Train the model using supervised fine-tuning.
6. Save the LoRA adapter.
7. Compare base model and fine-tuned model outputs on held-out questions.

## Example Questions

- Why is personal exposure not always the same as outdoor concentration?
- How can missing GPS data affect exposure analysis?
- Why is timestamp consistency important in multimodal sensor datasets?
- Explain why a model-derived exposure metric should include uncertainty discussion.
- How would you handle missing values in high-frequency air pollution sensor data?

## Results

The fine-tuned model showed improved domain orientation for several environmental exposure questions. Compared with the base model, it more frequently used concepts relevant to exposure science and sensor data analysis, such as personal exposure, indoor and outdoor environments, ventilation, indoor sources, timestamp consistency, missing data, and uncertainty in model-derived exposure metrics.

For questions about timestamp consistency and model-derived exposure uncertainty, the fine-tuned model produced more concise and domain-relevant responses than the base model.

However, the fine-tuned model did not consistently outperform the base model across all questions. In some cases, the base model produced more complete general explanations, while the fine-tuned model produced shorter but more domain-oriented responses.

## Error Analysis

The first training attempt used a custom instruction-response format. This led to prompt leakage, where the model sometimes continued generating additional instructions or question-answer structures.

To address this, the workflow was updated to use the Qwen chat template for both training and inference. This reduced prompt leakage and improved generation stability.

A further limitation was observed when asking the model about LoRA itself. Although the fine-tuned model improved over the base model, it still produced partially imprecise explanations. This highlights the importance of careful evaluation, especially when working with small models and small datasets.

## Limitations

- The dataset is small and manually curated.
- Evaluation is qualitative rather than fully automated.
- The base model is relatively small, limiting factual robustness.
- Fine-tuning improved domain wording but did not consistently improve factual completeness.
- The model is not intended for medical advice, regulatory use, or expert replacement.

## Future Improvements

- Expand the dataset with more high-quality domain examples.
- Test a larger model such as Qwen2.5-1.5B-Instruct or Qwen2.5-3B-Instruct.
- Add rubric-based scoring for domain accuracy, specificity, clarity, and uncertainty handling.
- Evaluate hallucination and factual consistency more systematically.
- Create a small interactive demo for environmental health question answering.

## Key Takeaway

This project demonstrates an end-to-end LoRA fine-tuning workflow using Hugging Face Transformers, PEFT, TRL and PyTorch. It also demonstrates practical model evaluation and error analysis, showing that successful applied generative AI work requires not only training a model, but also diagnosing failure modes, improving prompt formats, and interpreting results carefully.

## Disclaimer

This project is for educational and portfolio purposes only. It is not a validated medical, regulatory, or environmental decision-making tool.