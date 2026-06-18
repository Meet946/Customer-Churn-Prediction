# 📊 Customer Churn Prediction System

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red)
![Status](https://img.shields.io/badge/Status-Completed-success)

An end-to-end Machine Learning project that predicts whether a telecom customer is likely to churn based on demographic information, subscribed services, and billing details.

The project follows the complete Data Science lifecycle, including data understanding, exploratory data analysis, preprocessing, model development, hyperparameter tuning, threshold optimization, and deployment using Streamlit.

---

## 🚀 Features

* End-to-end Machine Learning pipeline
* Data preprocessing and feature engineering
* Exploratory Data Analysis (EDA)
* Multiple model comparison
* Hyperparameter tuning using GridSearchCV
* Threshold optimization for business objectives
* Interactive Streamlit dashboard
* Dynamic business recommendations
* Customer risk factor analysis
* Downloadable prediction report
* Model persistence using Joblib

---

## 📂 Dataset Information

**Dataset:** Telco Customer Churn Dataset

**Total Records:** 7043

**Total Features:** 21

**Target Variable:** Churn (Yes / No)

The dataset contains information related to:

* Customer demographics
* Services subscribed
* Contract details
* Payment methods
* Billing information
* Customer churn status

---

## 📁 Project Structure

```text
Customer-Churn-Prediction/
│
├── app.py
│   └── Streamlit dashboard
│
├── requirements.txt
│   └── Project dependencies
│
├── README.md
│   └── Project documentation
│
├── data/
│   └── Telco-Customer-Churn.csv
│
├── models/
│   ├── churn_model.pkl
│   └── preprocessor.pkl
│
├── notebooks/
│   ├── 01_data_understanding.ipynb
│   ├── 02_eda.ipynb
│   └── 03_preprocessing_and_modeling.ipynb
│
├── screenshots/
│   └── Application screenshots
│
└── src/
    └── predict.py
        └── Prediction pipeline
```

---

## 🛠️ Tech Stack

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* Streamlit
* Joblib
* XGBoost

---

## 🤖 Machine Learning Workflow

1. Dataset Understanding
2. Exploratory Data Analysis (EDA)
3. Data Cleaning
4. Train-Test Split
5. Feature Encoding and Scaling
6. Model Training and Comparison
7. Hyperparameter Tuning
8. Threshold Optimization
9. Feature Importance Analysis
10. Model Persistence
11. Streamlit Application Development

---

## 📈 Model Performance

**Final Algorithm:** Logistic Regression

* Test Accuracy: 80.70%
* Cross Validation Accuracy: 80.44%
* Optimized Decision Threshold: 0.55
* Mean Cross Validation F1 Score: 73.44%

---

## 💡 Key Business Insights

Customers are more likely to churn when they:

* Use Fiber Optic internet services
* Have Month-to-Month contracts
* Use Electronic Check payment methods
* Have shorter tenure periods
* Have higher monthly charges

Customers are less likely to churn when they:

* Have long-term contracts
* Have higher tenure
* Subscribe to Online Security services
* Subscribe to Tech Support services

---

## 🎯 Business Value

The system helps telecom companies:

* Identify high-risk customers proactively
* Reduce customer attrition
* Improve customer retention strategies
* Design targeted promotional campaigns
* Support data-driven business decisions

---

## 🖼️ Application Screenshots

### Dashboard Home

Add screenshot here.

### Low Churn Prediction

Add screenshot here.

### Medium Churn Prediction

Add screenshot here.

### High Churn Prediction

Add screenshot here.

---

## ▶️ Run Locally

Clone the repository:

```bash
git clone <repository-url>
cd Customer-Churn-Prediction
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

---

## 👨‍💻 Author

**Meet Modi**

B.Tech Computer Engineering Student
Data Science Enthusiast

GitHub: https://github.com/Meet946

Developed with ❤️ by Meet Modi
