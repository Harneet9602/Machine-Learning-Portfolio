# Project 10: End-to-End Classification Pipeline

## Objective
This capstone project implements a comprehensive, end-to-end machine learning pipeline to solve a classification problem. It demonstrates the entire workflow from data preprocessing and hyperparameter tuning to model evaluation and comparison, culminating in the selection of the best-performing model.

## Key Concepts Demonstrated
* **Data Preprocessing Pipeline**: Loading data with `pandas`, performing a train-test split, and standardizing features with `StandardScaler`.
* **Hyperparameter Tuning**: Systematically optimizing multiple models using `GridSearchCV` to find the best parameters for each classifier.
* **Comparative Model Evaluation**: Training, tuning, and comparing the performance of a wide range of classification algorithms on the same dataset.
* **Ensemble Learning**: Utilizing several ensemble techniques, including a `VotingClassifier`, to improve predictive accuracy and robustness.

## Models Compared
* Logistic Regression (including Softmax)
* Decision Tree Classifier
* Random Forest Classifier
* AdaBoost Classifier
* Gradient Boosting Classifier
* Support Vector Classifier (SVC)
* Soft Voting Classifier (Ensemble)

## Key Findings
* The hyperparameter tuning process was crucial for optimizing each model's performance. For example, the `LogisticRegression` model's best performance was found with a `C` value of **0.1**.
* The **Logistic Regression** and **Softmax Regression** models were the top performers among individual classifiers, both achieving an accuracy of **88.37%** after tuning. This suggests the underlying data has strong linear separability.
* The **Voting Classifier**, which combined the strengths of the Logistic Regression, Random Forest, and SVM models, also achieved a top-tier accuracy of **88.37%**, highlighting the power of ensembling different well-tuned models.
* Ensemble methods like **AdaBoost (86.05%)** and **Gradient Boosting (86.05%)** also performed very strongly, significantly outperforming the baseline Decision Tree model (76.74%).
