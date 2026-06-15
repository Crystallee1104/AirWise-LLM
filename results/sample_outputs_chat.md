# Sample Outputs: Base Model vs LoRA Fine-Tuned Model

This file compares responses from the base Qwen2.5-0.5B-Instruct model and a LoRA fine-tuned version for environmental health question answering.

The fine-tuned model was trained on a small curated instruction-response dataset covering air pollution exposure, sensor data quality control, exposure modelling, and environmental health concepts.

This is an exploratory domain-adaptation prototype, not a validated medical or regulatory tool.


## Example 1

**Question:** Why is personal exposure not always the same as outdoor concentration?


### Base model answer

Personal exposure to environmental pollutants can vary significantly from their outdoor concentrations due to several factors:

1. **Individual Differences**: People have different sensitivities to various pollutants. Some individuals may be more sensitive to certain types of air pollution or other environmental hazards.

2. **Occupational Exposure**: Workers in industries that produce or use hazardous substances might experience higher levels of exposure compared to those who work in less toxic environments.

3. **Environmental Factors**: Weather conditions such as temperature, humidity, wind speed, and precipitation can affect how pollutants are distributed throughout a region. For example, high winds can carry pollutants over long distances.

4. **Geographical Location**: The proximity to sources of pollution can also influence exposure levels. Areas with heavy industrial activity or transportation routes near major sources might see higher concentrations than areas without these impacts.

5. **Time of Day**: Pollutants can accumulate faster during peak hours when people


### LoRA fine-tuned model answer

Personal exposure depends not only on outdoor concentration, but also on time spent near sources of pollution, where people park their cars, during transportation, in buildings, at home, and for other activities. Outdoor concentrations can be reduced by actions such as planting trees, improving waste management, and limiting vehicle emissions, so it may still feel polluted to someone who spends more time indoors or has nearby sources even if outdoor concentration stays constant.


### Observation

Compare whether the fine-tuned model provides more domain-specific wording, better exposure-science terminology, and clearer discussion of sensor data or modelling assumptions.


## Example 2

**Question:** How can missing GPS data affect exposure analysis?


### Base model answer

Missing GPS data in exposure analysis can have several significant impacts:

1. **Inaccurate Exposure Estimates**: GPS data is typically used to track the movement of individuals over time. If a person's GPS signal is lost or unreliable, it can lead to inaccurate estimates of their daily movements, which may not reflect their actual exposure levels.

2. **Lack of Context**: GPS data often provides context about where people are located at different times. Missing this information can make it difficult to understand how exposures might be distributed across different locations.

3. **Temporal Uncertainty**: GPS data is based on real-time updates. If someone moves away from a location for a short period (e.g., during a trip), they will appear as if they moved there only temporarily. This temporal uncertainty can complicate analyses that rely on past GPS data.

4. **Geographical Discrepancies**: In some cases,


### LoRA fine-tuned model answer

Missing GPS data can make it difficult to identify the participant's location. If GPS data is used to estimate location-based exposure metrics such as PM2.5 or CO, missing values may bias these estimates. It is important to check quality controls, confirm location assumptions, and report any assumptions about missingness when interpreting exposure patterns.


### Observation

Compare whether the fine-tuned model provides more domain-specific wording, better exposure-science terminology, and clearer discussion of sensor data or modelling assumptions.


## Example 3

**Question:** Why is timestamp consistency important in multimodal sensor datasets?


### Base model answer

Timestamp consistency is crucial in multimodal sensor datasets for several reasons:

1. **Data Integrity**: Timestamps help ensure that the same information is recorded at the same time across different sensors or devices. This is essential for maintaining a consistent timeline of events.

2. **Temporal Consistency**: In many applications, such as tracking movements over time (e.g., GPS), timestamps must be synchronized to avoid discrepancies between consecutive measurements. Without consistent timestamps, this can lead to incorrect interpretations of movement patterns.

3. **Accuracy and Traceability**: Timed recordings allow for precise measurement and traceability of activities. For example, in healthcare monitoring systems, timestamps ensure that patient records are accurately dated and linked to specific events.

4. **Data Integration**: In federated learning or other collaborative machine learning setups, timestamps facilitate seamless integration of data from various sources. They help in understanding the temporal context of interactions among multiple entities


### LoRA fine-tuned model answer

Timestamp consistency is important because multimodal sensor datasets combine measurements from different sources. Different devices, sensors, protocols, and clock settings can lead to inconsistent timestamps. Consistent timestamps allow downstream models to interpret measurements correctly and reduce bias.


### Observation

Compare whether the fine-tuned model provides more domain-specific wording, better exposure-science terminology, and clearer discussion of sensor data or modelling assumptions.


## Example 4

**Question:** Explain why a model-derived exposure metric should include uncertainty discussion.


### Base model answer

A model-derived exposure metric is crucial for understanding the reliability of its predictions in real-world applications. Uncertainty discussions within such metrics are essential because:

1. **Real-World Sensitivity**: Exposure metrics often involve complex interactions between various factors (e.g., age, gender, location). Uncertainties in these interactions can significantly impact the overall exposure assessment.

2. **Model Calibration**: The accuracy of the model used to derive the exposure metric depends on how well it accounts for uncertainties in the input parameters. Uncertainty discussions help ensure that the model's calibration process is robust and reliable.

3. **Risk Assessment**: Exposure metrics play a critical role in risk management. Uncertain exposures can lead to misinterpretation or overestimation of potential risks, which could have serious consequences if not addressed promptly.

4. **Public Health Policy**: In public health contexts, exposure metrics are used to inform policy decisions


### LoRA fine-tuned model answer

A model-derived exposure metric only reflects measurements or estimates. It should also include measurement error, sampling bias, missing data, parameter misspecification, assumption violations, and uncertainty windows. This allows users to understand how the metric may vary, compare it with other sources, and interpret exposure estimates accurately.


### Observation

Compare whether the fine-tuned model provides more domain-specific wording, better exposure-science terminology, and clearer discussion of sensor data or modelling assumptions.


## Example 5

**Question:** What does LoRA fine-tuning demonstrate in this project?


### Base model answer

LoRA (Learning Rate Oscillation) is a technique used to optimize the learning rate during training of neural networks. In the context of a project involving LoRA fine-tuning, it demonstrates how:

1. **Adaptive Learning Rate**: The network learns to adjust its learning rate dynamically based on the performance of the model. This allows the network to adapt better to different types of problems or datasets.

2. **Regularization**: By oscillating the learning rate, LoRA helps prevent overfitting by ensuring that the network's complexity remains manageable while still improving its generalization ability.

3. **Efficiency**: Fine-tuning LoRA can be computationally efficient because it only involves updating the learning rate once per epoch, rather than retraining the entire network every time.

4. **Performance Improvement**: When applied correctly, LoRA can lead to significant improvements in model performance, especially when dealing with


### LoRA fine-tuned model answer

LoRA fine-tuning demonstrates a model adaptation technique by training small additional adapter modules instead of copying the entire model. In this project, you might use LoRA to adapt a language model for a specific task such as personalisation or question answering by adjusting parameter weights and learning rates rather than completely rewriting the model code.


### Observation

Compare whether the fine-tuned model provides more domain-specific wording, better exposure-science terminology, and clearer discussion of sensor data or modelling assumptions.


## Example 6

**Question:** How would you handle missing values in high-frequency air pollution sensor data?


### Base model answer

Handling missing values in high-frequency air pollution sensor data involves several strategies to ensure the reliability of your analysis:

1. **Imputation Methods**:
   - **Mean Imputation**: Replace missing values with the mean or median value of the available data.
   - **Median Imputation**: Replace missing values with the median value of the available data.
   - **Mode Imputation**: Replace missing values with the mode (most frequent) value of the available data.

2. **Prediction Models**:
   - Use machine learning models that can predict missing values based on historical data. For example, regression models like linear regression can be used to predict future values from past observations.
   - Ensemble methods such as Random Forests or Gradient Boosting Machines can also help in handling missing values by using multiple models trained on different subsets of the data.

3. **Data Augmentation**:
   - Generate synthetic data


### LoRA fine-tuned model answer

Missing values should first be assessed by duration, frequency, and likely cause. Short gaps may sometimes be interpolated or smoothed, while longer periods should usually be considered unreliable unless supported by other data patterns. All missing values should be flagged to identify which rows represent real measurements versus flags. Professional judgement is needed as missed data can affect time-activity classification and exposure estimates.


### Observation

Compare whether the fine-tuned model provides more domain-specific wording, better exposure-science terminology, and clearer discussion of sensor data or modelling assumptions.


## Example 7

**Question:** What is outdoor-generated personal exposure?


### Base model answer

Outdoor-generated personal exposure refers to the amount of air pollution or other pollutants that people inhale while engaging in physical activities outdoors. This can include particulate matter (PM), nitrogen dioxide (NO2), sulfur dioxide (SO2), ozone (O3), carbon monoxide (CO), and other harmful substances found in polluted air.

Outdoor exposure can be significant for several reasons:

1. **Health Impacts**: Exposure to these pollutants can lead to respiratory issues such as asthma attacks, bronchitis, and lung cancer.
2. **Environmental Health**: It contributes to climate change by releasing greenhouse gases like CO2 into the atmosphere.
3. **Economic Costs**: Increased healthcare costs due to illness and treatment related to air pollution.
4. **Social Impact**: Can affect public health and quality of life, particularly among vulnerable populations.

To mitigate this issue, it's important to reduce outdoor activity during peak


### LoRA fine-tuned model answer

Outdoor-generated personal exposure refers to the portion of a person's exposure that comes from sources outside indoor environments. Examples include traffic-related pollution, cooking, heating, smoking, yard waste disposal, and outdoor recreation activities. It is important for monitoring because it can differ significantly between indoors and outdoors.


### Observation

Compare whether the fine-tuned model provides more domain-specific wording, better exposure-science terminology, and clearer discussion of sensor data or modelling assumptions.


## Example 8

**Question:** Why is ventilation important for indoor air pollution modelling?


### Base model answer

Ventilation is crucial for indoor air pollution modeling because it helps to remove pollutants from the air before they can accumulate in the living spaces of people who live or work there. Here are some key reasons why proper ventilation is essential:

1. **Pollution Reduction**: When air is not well-ventilated, pollutants like dust, pollen, smoke, and other airborne particles can build up over time. This accumulation can lead to respiratory issues, allergies, and other health problems.

2. **Air Quality Improvement**: Proper ventilation ensures that the air quality inside a building remains clean and healthy. It prevents the buildup of harmful substances that could cause illness or even death if inhaled.

3. **Energy Efficiency**: Efficient ventilation systems help maintain comfortable indoor temperatures and humidity levels, which are critical for human comfort and energy efficiency.

4. **Health Benefits**: Regularly ventilated buildings have been shown to reduce the risk


### LoRA fine-tuned model answer

Ventilation controls what part of the environment air enters a building. It affects how quickly pollutants move between indoors and outdoors. For example, indoor sources may release pollutants faster if ventilation is poor, which can alter concentration profiles and contribute to exposure.


### Observation

Compare whether the fine-tuned model provides more domain-specific wording, better exposure-science terminology, and clearer discussion of sensor data or modelling assumptions.
