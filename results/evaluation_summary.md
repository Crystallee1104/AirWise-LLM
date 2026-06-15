# Evaluation Summary

## Overview

This project explores parameter-efficient fine-tuning of a small instruction-tuned language model for environmental health question answering. The model was adapted using LoRA on a curated instruction-response dataset covering air pollution exposure, multimodal sensor data, exposure modelling, and uncertainty communication.

## What Worked Well

The fine-tuned model showed improved domain orientation for several environmental exposure questions. Compared with the base model, it more frequently used concepts relevant to exposure science and sensor data analysis, including:

- personal exposure
- indoor and outdoor environments
- ventilation
- indoor sources
- timestamp consistency
- sensor data quality
- missing data
- uncertainty in model-derived exposure metrics

For questions about timestamp consistency and model-derived exposure uncertainty, the fine-tuned model produced more concise and domain-relevant answers than the base model.

## Error Analysis

The first training attempt used a custom instruction-response prompt format. This led to prompt leakage and unstable generation, where the model sometimes continued generating new instructions or unrelated question-answer structures.

To address this, the workflow was updated to use the Qwen chat template for both training and inference. This reduced prompt leakage and improved response stability.

A second issue was that the fine-tuned model sometimes became more concise but not always more complete than the base model. This suggests that small curated datasets can influence response style and domain terminology, but may not be sufficient to consistently improve factual completeness.

The model also showed limitations when asked about LoRA itself. Although the fine-tuned model improved over the base model, it still produced partially imprecise explanations. This highlights the need for careful evaluation, especially when adapting small models with limited training data.

## Limitations

- The project used a small manually curated dataset.
- Evaluation was qualitative and exploratory.
- The base model was relatively small, which limits reasoning and factual robustness.
- Fine-tuning improved domain wording but did not consistently outperform the base model across all questions.
- The model is not intended for medical advice, regulatory decisions, or expert replacement.

## Future Improvements

Future work could improve the project by:

- Expanding the dataset with more high-quality paraphrased examples.
- Testing a larger model such as Qwen2.5-1.5B-Instruct or 3B-Instruct.
- Adding rubric-based scoring for domain accuracy, specificity, clarity, and uncertainty handling.
- Including automatic checks for key environmental exposure concepts.
- Evaluating hallucination and factual consistency more systematically.

## Key Takeaway

This project demonstrates an end-to-end LoRA fine-tuning workflow using Hugging Face Transformers, PEFT, TRL and PyTorch. It also demonstrates practical model evaluation and error analysis, showing that successful applied generative AI work requires not only training a model, but also diagnosing failure modes, improving prompt formats, and interpreting results carefully.
