# 02: Regression Models - Predicting Continuous Values

## Objective
This project explores three fundamental regression algorithms to predict continuous values across two different datasets. The primary goals are:
1.  To predict **house prices** using both single and multiple features from a pre-processed housing dataset.
2.  To model the non-linear relationship between a person's **height and weight**, demonstrating the limitations of a simple linear model and the advantages of a polynomial one.

## Key Concepts Demonstrated
* **Simple Linear Regression**: Building a baseline model to predict a target variable (height) using a single input feature (weight).
* **Multiple Linear Regression**: Implementing a linear model that uses multiple input features (e.g., area, bedrooms) to predict a single continuous target (price).
* **Polynomial Regression**: Building a model capable of capturing non-linear relationships in data by creating polynomial features from an input feature. This was used to model the curved relationship between height and weight.

## Datasets Used
1.  **Housing Price Dataset** (`processed_housing_data.csv`)
    * This dataset is the pre-processed output from the `01-EDA-and-Preprocessing` project.
    * It contains 13 features, including `area`, `bedrooms`, `bathrooms`, and `parking`, which are used to predict the target variable, `price`.
    * All categorical variables have been encoded, and all features are scaled between 0 and 1.

2.  **Height-Weight Dataset** (`Training_set_heights200.csv`)
    * A simple dataset containing two columns: `Height` and `Weight`.
    * This dataset is used to demonstrate and compare the performance of linear vs. polynomial models on data with a clear non-linear trend.

## Project Structure
This project is divided into three Jupyter Notebooks, each focusing on a specific model:
* `Linear-Regression-model.ipynb`: A detailed implementation of Simple Linear Regression on **scaled** height-weight data.
* `Multiple-regression.ipynb`: Implementation of Multiple Linear Regression on the housing price dataset.
* `polynomial-regression.ipynb`: A comparison of Simple Linear vs. Polynomial Regression on **unscaled** height-weight data to visually emphasize the model fits.

## Model Summaries and Results

### 1. Simple Linear Regression (Height from Weight)
* **Objective**: To establish a baseline model predicting height based solely on weight using scaled data.
* **Result**: The model achieved a **Mean Squared Error (MSE) of 0.0189**.
* **Conclusion**: The model provides a solid linear approximation of the relationship, confirmed by a low MSE and a well-behaved residual plot.

### 2. Multiple Linear Regression (House Price Prediction)
* **Objective**: To predict house prices using a combination of 12 different features.
* **Result**: The model achieved an **MSE of 0.0133** on the test set.
* **Conclusion**: The model demonstrates high accuracy. By analyzing the coefficients, key price drivers were identified, with **`area` and `bathrooms`** having the most significant positive impact. The residual plot showed a random scatter of errors, indicating a good model fit.

### 3. Polynomial Regression (Height from Weight)
* **Objective**: To improve upon the simple linear model by capturing the non-linear trend in the height-weight data.
* **Results**:
    * Simple Linear Regression MSE: **121.20**
    * Polynomial Regression (Degree 3) MSE: **120.56**
* **Conclusion**: The Polynomial Regression model achieved a lower MSE, indicating a better numerical fit. The visualization clearly shows its curved line following the data's natural trend more closely than the straight line of the simple linear model.

## How to Run
1.  **Clone the repository.**
2.  **Ensure you have the necessary libraries installed**:
    ```bash
    pip install pandas numpy scikit-learn matplotlib seaborn jupyter
    ```
3.  **File Structure**: The notebooks assume that the datasets are located in a `CSV Files/` directory and the helper functions are in a `utils/` directory at the root of the portfolio.
4.  **Execute the Notebooks**: Run the cells in each of the three Jupyter Notebooks to see the analysis and results.
