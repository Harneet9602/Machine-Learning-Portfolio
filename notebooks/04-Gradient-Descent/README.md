# Gradient Descent Algorithms for Linear Regression from Scratch

### 📈 Project Overview
This project provides a hands-on implementation and comparison of the three primary Gradient Descent optimization algorithms: **Batch**, **Stochastic**, and **Mini-Batch**. 
The algorithms are built from scratch using Python to solve a simple linear regression problem, demonstrating a core understanding of their mechanics and the trade-offs between accuracy and computational cost.

### 🤖 Key Concepts Covered
* **Linear Regression**: Implementing a simple model of the form $y = mx + b$ to predict height based on weight.
* **Gradient Descent**: An iterative optimization algorithm used to find the minimum of a cost function.
    * **Batch GD**: Calculates the gradient using the *entire* dataset. Most accurate but computationally slow.
    * **Stochastic GD (SGD)**: Calculates the gradient using a *single random sample*. Fast but has a noisy convergence.
    * **Mini-Batch GD**: A hybrid approach using a *small batch of samples*. Balances accuracy and speed.
* **Cost Function (MSE)**: The model's error is measured using Mean Squared Error, which the algorithms aim to minimize.
    $$MSE = \frac{1}{N} \sum_{i=1}^{N} (y_i - \hat{y}_i)^2$$


### 🏆 Results and Conclusion
The performance of the three methods was evaluated on the test set, yielding the following MSE scores:

| Algorithm | Mean Squared Error (MSE) |
| :--- | :---: |
| **Batch Gradient Descent** | 0.0189 |
| **Mini-Batch Gradient Descent** | **0.0183** |
| **Stochastic Gradient Descent** | 0.0231 |

**Conclusion**: While **Batch Gradient Descent** provided a stable and accurate fit, **Mini-Batch Gradient Descent** achieved a slightly lower MSE. It offers the best compromise between the stability of Batch GD and the speed of SGD, which is why it's the most common implementation in modern machine learning. **Stochastic GD**, while fast, was noticeably less accurate due to its noisy, single-sample updates.


### 🚀 How to Run

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/](https://github.com/)<your-username>/<your-repo-name>.git
    ```
2.  **Install the required libraries:**
    ```bash
    pip install pandas numpy matplotlib
    ```
3.  **Run the Jupyter Notebook:**
    ```bash
    jupyter notebook gradient-descent.ipynb
    ```
