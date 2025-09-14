# Project 06: Model Evaluation Metrics for Classification

## Objective

This notebook provides a practical demonstration of key evaluation metrics for classification models. Using the liver patient dataset, 
we train **Logistic Regression** and **Decision Tree** models and then dive deep into various metrics to understand their performance beyond simple accuracy. This project emphasizes why a single metric like accuracy can be misleading, especially for imbalanced datasets, and showcases a more holistic approach to model evaluation.

## Key Concepts Demonstrated

* **Handling Class Imbalance**: The project directly addresses the common problem of class imbalance in the training data by applying the `class_weight='balanced'` parameter in the Logistic Regression model.
* **Accuracy Score**: Used as a baseline metric to get a general sense of model performance.
* **Cross-Validation**: Both **K-Fold** and **Stratified K-Fold** cross-validation are implemented to provide a more robust and reliable measure of the model's performance by training and testing on multiple subsets of the data.
* **Confusion Matrix**: A detailed visualization is created to show the counts of true positives, true negatives, false positives, and false negatives, giving a clear picture of the model's predictive behavior.
* **Precision, Recall, and F1-Score**: The `classification_report` is generated to analyze these crucial metrics, which are especially important for medical datasets where the cost of false negatives and false positives is high.
* **ROC Curve and AUC Score**: A Receiver Operating Characteristic (ROC) curve is plotted to visualize the trade-off between the true positive rate and false positive rate. The Area Under the Curve (AUC) provides a single score to summarize the model's ability to distinguish between classes.

## Dataset Used

* **Liver Patient Data**: The `liver_patient.csv` dataset is used for all classification and evaluation tasks.

## Key Findings

* The training data was found to be **imbalanced**, with the "Disease" class (label 1) having 341 samples compared to only 122 samples for the "No Disease" class (label 0).
* By using the `class_weight='balanced'` parameter, the **Logistic Regression** model's performance improved significantly, achieving a balanced accuracy of **73.28%** on the test set. This outperformed the baseline Decision Tree's accuracy of **64.66%**.
* The balanced model showed a strong **recall of 0.86** for the "No Disease" class, meaning it correctly identified 86% of the healthy patients in the test set.
* The **ROC curve** for the Logistic Regression model resulted in an **AUC of 0.80**, indicating a good capability to distinguish between patients with and without liver disease.
* Cross-validation provided a more conservative but robust performance estimate, with the Stratified K-Fold approach yielding a mean accuracy of **61.75%**, highlighting its importance for a realistic performance expectation.
