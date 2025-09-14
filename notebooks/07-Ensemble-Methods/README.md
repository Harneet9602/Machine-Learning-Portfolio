# Project 07: Ensemble Learning Techniques for Classification

## Objective

This project explores a variety of powerful ensemble learning methods designed to improve predictive performance and model robustness over single estimators. We apply these techniques to a classification task (liver disease prediction) to demonstrate their versatility and effectiveness.

## Key Concepts Demonstrated

* **Baseline Model Comparison**: Established baseline performance using `LogisticRegression` and `DecisionTreeClassifier` to provide a benchmark for evaluating ensemble methods.
* **Bagging and Pasting**: Implemented `BaggingClassifier` to demonstrate how training models on random subsets of data (with and without replacement) can reduce variance.
* **Random Forests**: Used `RandomForestClassifier` to show how an ensemble of decorrelated decision trees can lead to highly accurate predictions. Also demonstrated how to extract and visualize **feature importances** from the trained model.
* **Voting Classifiers**: Implemented both **Hard Voting** (majority vote) and **Soft Voting** (averaging probabilities) to combine the predictions of different types of models on a synthetic dataset for a clear demonstration.
* **Performance Visualizations**: Included bar plots to visually compare the accuracies of various classification ensembles against baseline models.

## Datasets Used

* **Liver Patient Data**: The `liver_patient.csv` dataset is used for the primary classification tasks.
* **Synthetic Data**: A synthetic dataset was generated to clearly demonstrate the mechanics of Voting Classifiers.

## Key Findings

* **Classification (Liver Patient Dataset)**: The ensemble methods showed varied performance, with **Bagging Classifier** and **Random Forest Classifier** both achieving an accuracy of **63.79%**, a slight improvement over the baseline `DecisionTreeClassifier` (64.66%) in some cases, but not outperforming the baseline `LogisticRegression` model on this particular dataset.
* **Feature Importance**: For the liver patient dataset, `Alkaline_Phosphotase` and `Alamine_Aminotransferase` were identified by the Random Forest as the most important features for making predictions.
* **Voting Classifiers**: On the synthetic dataset, **Soft Voting (95.00% accuracy)** slightly outperformed **Hard Voting (94.00% accuracy)**, demonstrating that averaging prediction probabilities can often capture more nuance than a simple majority vote.
