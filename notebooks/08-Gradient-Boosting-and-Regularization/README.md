# Project 08: Gradient Boosting and Regularization

## Objective

This project provides a deep dive into advanced machine learning techniques, separated into three focused notebooks. It explores **Gradient Boosting**, a powerful sequential ensemble method, for both regression and classification tasks. Additionally, it demonstrates the use of **Regularized Linear Models** (Ridge and Lasso) to prevent overfitting and perform feature selection.

## Key Concepts Demonstrated

* **Gradient Boosting**: Implemented and tuned `GradientBoostingRegressor` and `GradientBoostingClassifier`, showcasing the model's sequential, error-correcting approach.
* **Hyperparameter Tuning**: Used `GridSearchCV` to systematically find the optimal combination of hyperparameters (`n_estimators`, `learning_rate`, `max_depth`) for the Gradient Boosting models.
* **Ridge Regression (L2 Regularization)**: Used `RidgeCV` to apply L2 regularization, which shrinks model coefficients to handle multicollinearity and reduce model complexity.
* **Lasso Regression (L1 Regularization)**: Used `LassoCV` to apply L1 regularization, demonstrating its ability to perform automatic feature selection by shrinking some coefficients to zero.
* **Performance Visualization**: Created a suite of visualizations to analyze model performance, including **Actual vs. Predicted** plots, **Residual Plots**, **Feature Importance** charts, **ROC Curves**, and **Coefficient Comparison** plots.

## Datasets Used

* **Housing Data**: The `Book1.csv` dataset is used for all regression tasks.
* **Liver Patient Data**: The `liver_patient.csv` dataset is used for the classification task.

## Key Findings

### Gradient Boosting Regressor (`08a-Gradient-Boosting-Regressor.ipynb`)
* After hyperparameter tuning, the Gradient Boosting Regressor performed exceptionally well, achieving a very low **Mean Squared Error (MSE) of 0.0132** on the housing price test set.
* The feature importance plot revealed that `area` is by far the most significant predictor of price, followed by `bathrooms` and `stories`.
* The residuals plot confirmed a well-fitted model, with errors randomly scattered around the zero line.

### Gradient Boosting Classifier (`08b-Gradient-Boosting-Classifier.ipynb`)
* The tuned Gradient Boosting Classifier achieved a strong **accuracy of 73.50%** on the liver patient dataset, significantly outperforming the baseline Decision Tree model (64.66%).
* The model's ability to distinguish between classes was excellent, as shown by a high **AUC score of 0.81** from the ROC curve.

### Regularized Regression (`08c-Regularized-Regression.ipynb`)
* **Ridge Regression** was the top-performing regularized model with a final **MSE of 0.0133** and an optimal alpha of **0.3199**.
* **Lasso Regression** produced a slightly higher **MSE of 0.0139**. While it is known for feature selection, in this instance, it shrank the `bedrooms` coefficient to a very small value (0.005) but did not completely eliminate it.
* The coefficient comparison plot clearly illustrated how both Ridge and Lasso effectively reduce coefficient magnitudes compared to a standard linear model.
