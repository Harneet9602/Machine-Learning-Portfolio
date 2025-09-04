# Housing Price Prediction: Exploratory Data Analysis (EDA) and Preprocessing
## Objective
This project covers the essential first steps of any data science workflow. The goal is to take a raw housing dataset, understand its structure, clean it, handle categorical data, and prepare it for future machine learning tasks through visualization and feature scaling.

## Key Concepts Demonstrated
**Data Loading & Inspection:** Using pandas to load a CSV file and inspect its basic properties (.head(), .info(), .shape).

**Data Cleaning:** Identifying and handling different data types.

**Feature Transformation:** Manually converting categorical text features (like 'yes'/'no') into numerical format (1/0) that a model can understand.

**Data Visualization:** Using Matplotlib and Seaborn to create scatter plots and histograms to explore relationships and distributions within the data.

**Feature Scaling:** Applying Min-Max scaling to normalize all features into a common range, a crucial step for many machine learning algorithms.

## Dataset
The project uses the Housing Prices Dataset, which contains various features describing residential homes in an Indian city. It contains information on 545 house listings with 13 distinct features.
* **Shape:** 545 rows, 13 columns
* **Data Quality:** There are no missing values, which simplifies the cleaning process.
* **Features:**
    * **Numerical:** `price`, `area`, `bedrooms`, `bathrooms`, `stories`, `parking`
    * **Categorical:** `mainroad`, `guestroom`, `basement`, `hotwaterheating`, `airconditioning`, `prefarea`, `furnishingstatus`

## 📊 Exploratory Data Analysis (EDA) & Key Insights
The primary goal of the EDA was to uncover relationships between different features and the target variable, price.

### Key Insight: Price vs. Area by Furnishing Status
The relationship between a house's price and its area was visualized, with furnishing status as a key differentiator.
From this visualization, we can derive several important insights:
* **Positive Correlation:** There is a clear positive correlation between `area` and `price`. As the square footage of a house increases, its price generally tends to increase as well.

* **Impact of Furnishing:** `furnishingstatus` is a significant factor in determining the price.
    * **Furnished houses** (dark blue) consistently command higher prices for any given area.
    * **Unfurnished houses** (light green) are generally the most affordable.
    * **Semi-furnished houses** (teal) fall in the middle price range.

* **Variance:** While the trend is positive, there is considerable variance in price for houses of similar sizes, indicating that other features (like `airconditioning`, `prefarea`, etc.) also play a crucial role.

## ⚙️ Data Preprocessing
To prepare the dataset for machine learning, the following steps were performed:

#### Categorical to Numerical Conversion:
All categorical columns with binary values (e.g., 'yes'/'no') were mapped to numerical format (1/0). The furnishingstatus column, which has three categories, was also converted to a numerical representation (e.g., furnished: 1.0, semi-furnished: 0.5, unfurnished: 0.0).

#### Feature Scaling:
All numerical features, including the newly converted categorical ones, were scaled to a range between 0 and 1 using Min-Max Scaling. This step is crucial for many machine learning algorithms (like Linear Regression and Support Vector Machines) as it ensures that all features contribute equally to the model's training, preventing features with larger scales from dominating.
The preprocessed data was then saved to CSV Files/processed_housing_data.csv for use in the next stage.

## ✅ Conclusion & Next Steps
This initial analysis successfully explored the housing dataset and prepared it for model building. The key takeaway is that a house's area and furnishing status are strong predictors of its price.
The cleaned and scaled dataset is now ready for the next logical step: training a regression model to predict housing prices based on these features. Excellent work on this first part of the project!
