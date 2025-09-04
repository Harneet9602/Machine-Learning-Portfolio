# Using Preprocessed Housing Data: Regression Models

### Objective
This project builds upon the preprocessed data from the first assignment to train and evaluate two fundamental types of regression models. The primary goal is to predict continuous values: first, house prices using multiple features,
and second, a person's height based on their weight, exploring both linear and non-linear relationships.

### Key Concepts Demonstrated
* **Multiple Linear Regression:** Implementing a linear model that uses multiple input features (e.g., `area`, `bedrooms`, `bathrooms`) to predict a single continuous target (`price`).
* **Polynomial Regression:** Building a model capable of capturing non-linear relationships in data by creating polynomial features from a single input feature. This was used to model the curved relationship between height and weight.
* **Model Training:** Using the `.fit()` method to train the regression models on the prepared training data.
* **Model Evaluation:** Using **Mean Squared Error (MSE)** as the primary metric to quantify the performance and prediction error of the regression models.
* **Data Visualization:** Plotting the results of the Polynomial Regression to visually confirm how well the model's curve fits the underlying data points.

### Datasets Used
1.  **Processed Housing Data:** This project directly uses the cleaned and scaled `processed_housing_data.csv` file generated in Assignment 01.
2.  **Height & Weight Data:** A simple two-column dataset used to demonstrate Polynomial Regression.

### Conclusion & Key Findings
- The **Multiple Linear Regression** model established a solid baseline for predicting house prices, providing a clear MSE score that can be used for comparison with more advanced models in later projects.
- The **Polynomial Regression** model was highly effective at capturing the non-linear trend in the height-weight data, and the visualization clearly showed its superiority over a simple straight-line fit for that specific dataset.
- This highlights the importance of choosing the right model for the data's underlying structure.
