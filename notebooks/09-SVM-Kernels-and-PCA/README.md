# Project 09: SVM Kernels and Dimensionality Reduction with PCA

## Objective
This project is broken into two notebooks to explore two important machine learning concepts. The first notebook provides a visual demonstration of different Support Vector Machine (SVM) kernels. The second notebook showcases a practical application of the PCA + SVM workflow for classification on a real-world dataset.

---

### Notebook 1: `SVM-Kernels.ipynb` - Visualizing SVM Kernels
This notebook focuses on building an intuitive understanding of how SVMs create decision boundaries. By using a simple, 2D synthetic dataset, we can clearly visualize the impact of different kernel choices.

* **Key Concepts Demonstrated**:
    * **SVM Kernels**: Visually compared the decision boundaries of **Linear**, **Polynomial**, and **Radial Basis Function (RBF)** kernels.
    * **Decision Boundary Visualization**: Plotted the classification regions for each kernel to show their different approaches to separating data.
    * **Hyperparameter Effects**: Demonstrated how changing the `gamma` parameter affects the flexibility and shape of the RBF kernel's boundary.

---

### Notebook 2: `pca-with-svm.ipynb` - Classification with Dimensionality Reduction
This notebook demonstrates a complete machine learning pipeline for a real-world classification problem using the liver patient dataset.

* **Key Concepts Demonstrated**:
    * **Principal Component Analysis (PCA)**: Used PCA for dimensionality reduction, transforming the dataset from 9 features down to 2 principal components.
    * **Data Standardization**: Applied `StandardScaler` as a critical preprocessing step for PCA.
    * **PCA + SVM Workflow**: Showcased the end-to-end process of scaling data, reducing its dimensions with PCA, and then training an SVM classifier on the new, simplified feature space.

---

## Overall Key Findings
* The SVM kernel visualizations clearly showed that the **Linear kernel** creates a straight-line separator, the **Polynomial kernel** creates a curved boundary, and the **RBF kernel** creates a more complex, localized boundary suitable for intricate data distributions.
* Applying PCA to the liver patient data successfully reduced the 9 original features to just **2 principal components**. These two components were able to explain **38.92%** of the total variance in the original data.
* The SVM classifier, trained on the two principal components, achieved an accuracy of **70.94%** on the test set. This is a solid performance, especially considering the model was trained on a much simpler version of the original data.
