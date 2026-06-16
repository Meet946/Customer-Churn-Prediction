# Customer Churn Prediction Project Journal

## Day 1 - Project Setup and Environment Configuration

### Objective

To establish a professional project structure and development environment for building an end-to-end Customer Churn Prediction system.

### Tasks Completed

#### 1. Project Planning

* Finalized Customer Churn Prediction as the first placement-focused Data Science project.
* Defined the project goal as predicting whether a customer is likely to leave a telecom service provider.

#### 2. Environment Setup

* Created a Python virtual environment using venv.
* Activated the virtual environment.
* Installed required libraries:

  * Pandas
  * NumPy
  * Matplotlib
  * Seaborn
  * Scikit-Learn
  * Jupyter Notebook
  * Streamlit

#### 3. Project Structure Creation

Created the following directory structure:

Customer-Churn-Prediction/

* data/
* notebooks/
* src/
* models/
* app/
* reports/
* README.md
* requirements.txt

#### 4. Source Code Organization

Created initial source files:

* data_preprocessing.py
* train_model.py
* predict.py

These files will later contain data preprocessing, model training, and prediction logic.

#### 5. Git and GitHub Setup

* Initialized a local Git repository.
* Created a .gitignore file.
* Added project files to version control.
* Created the first Git commit.
* Connected the local repository to GitHub.
* Successfully pushed the project to GitHub.

### Key Learnings

* Learned how to create and manage a Python virtual environment.
* Learned the importance of version control using Git.
* Learned how professional Machine Learning projects are structured.
* Understood the importance of maintaining a clean and organized repository.

### Challenges Faced

* Understanding the purpose of the .gitignore file.
* Verifying that the virtual environment files were excluded from Git tracking.

### Resolution

* Configured .gitignore correctly to prevent unnecessary files from being pushed to GitHub.

### Next Steps

* Download and inspect the Telco Customer Churn dataset.
* Perform dataset auditing and data understanding.
* Identify feature types, target variable distribution, and data quality issues.

### Project Status

✅ Environment Setup Completed

✅ GitHub Repository Created

✅ Development Workflow Established

🚧 Dataset Understanding Phase Pending


# Day 2 - Dataset Understanding and Initial Data Cleaning

## Objective

To understand the Customer Churn dataset, inspect its structure, identify data quality issues, and perform initial data cleaning.

## Dataset Overview

### Dataset Information

* Total Records: 7043
* Total Features: 21
* Target Variable: Churn

### Dataset Shape

```python
(7043, 21)
```

The dataset contains information about telecom customers, including demographics, services subscribed, billing details, and churn status.

---

## Target Variable Analysis

### Churn Distribution

```text
No     5174
Yes    1869
```

### Observations

* Customers who stayed: 5174
* Customers who churned: 1869
* Approximately 73.5% of customers remained with the company.
* Approximately 26.5% of customers churned.

### Conclusion

The dataset is moderately imbalanced but still suitable for classification modeling.

---

## Data Quality Assessment

### Duplicate Records Check

```python
df.duplicated().sum()
```

Output:

```python
0
```

### Observation

No duplicate records were found in the dataset.

---

## Investigation of TotalCharges Column

### Initial Observation

Using:

```python
df.info()
```

It was observed that:

```text
TotalCharges -> str (object)
```

This was unexpected because TotalCharges represents billing amounts and should be numerical.

---

### Root Cause Analysis

Using:

```python
(df["TotalCharges"] == " ").sum()
```

Output:

```python
11
```

### Observation

There were 11 records containing blank spaces instead of numerical values.

Because of these blank entries, Pandas treated the entire TotalCharges column as a string datatype.

---

## Data Cleaning Performed

### Step 1: Convert TotalCharges to Numeric

```python
df["TotalCharges"] = pd.to_numeric(
    df["TotalCharges"],
    errors="coerce"
)
```

### Result

The blank values were converted into NaN values.

---

### Step 2: Verify Missing Values

```python
df["TotalCharges"].isnull().sum()
```

Output:

```python
11
```

### Observation

All hidden missing values were successfully identified.

---

### Step 3: Business Investigation

The rows with missing TotalCharges values were examined.

Observation:

* All affected customers had tenure = 0 months.
* These customers were newly joined customers.
* They had not completed any billing cycle.

---

### Step 4: Missing Value Treatment

Based on business understanding, missing values were replaced with 0.

```python
df["TotalCharges"] = df["TotalCharges"].fillna(0)
```

### Justification

Since customers with tenure = 0 had not yet accumulated any charges, replacing missing values with 0 accurately represented the business scenario.

---

## Final Outcome

### Data Cleaning Status

✅ TotalCharges converted from string to numeric

✅ Hidden missing values identified

✅ Missing values handled using business logic

✅ No duplicate records present

✅ Dataset ready for Exploratory Data Analysis (EDA)

---

## Key Learnings

* Missing values may not always appear as NaN.
* Blank spaces can cause incorrect datatype detection.
* Business understanding is essential before choosing a missing value treatment strategy.
* Data cleaning decisions should be justified using domain knowledge rather than blindly applying statistical methods.

---

## Next Steps

* Perform Exploratory Data Analysis (EDA).
* Analyze churn patterns across different customer groups.
* Study the relationship between churn and:

  * Contract Type
  * Tenure
  * Monthly Charges
  * Internet Services
  * Payment Methods
* Generate business insights from the dataset.


# Day 2 - Initial Exploratory Data Analysis (EDA)

## Objective

To identify patterns and factors associated with customer churn through exploratory data analysis and generate actionable business insights.

---

## EDA 1: Churn Distribution Analysis

### Observation

Customer Churn Distribution:

```text
No     5174
Yes    1869
```

### Interpretation

* Approximately 73.5% of customers remained with the company.
* Approximately 26.5% of customers churned.
* The dataset is moderately imbalanced but suitable for classification modeling.

### Business Insight

A significant number of customers are leaving the company, making churn prediction an important business problem with direct revenue implications.

---

## EDA 2: Gender vs Churn

### Crosstab Result

```text
Female    2549   939
Male      2625   930
```

### Interpretation

The churn rates for male and female customers are nearly identical.

### Business Insight

Gender does not appear to be a significant factor influencing customer churn. Retention strategies should focus on behavioral and service-related factors rather than gender demographics.

---

## EDA 3: Senior Citizen vs Churn

### Crosstab Result

```text
SeniorCitizen    No    Yes
0               4508  1393
1                666   476
```

### Interpretation

Although the number of senior citizens is lower, their churn rate is significantly higher compared to non-senior customers.

Approximate Churn Rates:

* Non-Senior Customers: 23.6%
* Senior Citizens: 41.7%

### Business Insight

Senior citizens are substantially more likely to leave the service. This customer segment may require targeted retention strategies, improved customer support, or customized service plans.

---

## EDA 4: Contract Type vs Churn

### Crosstab Result

```text
Month-to-month   2220  1655
One year         1307   166
Two year         1647    48
```

### Interpretation

Approximate Churn Rates:

* Month-to-Month Contract: 42.7%
* One-Year Contract: 11.3%
* Two-Year Contract: 2.8%

### Business Insight

Contract type is one of the strongest indicators of churn. Customers with month-to-month contracts are significantly more likely to leave compared to customers with long-term contracts.

### Recommendation

The company should encourage customers to transition from month-to-month plans to longer-term contracts through discounts, loyalty benefits, or promotional offers.

---

## EDA 5: Tenure vs Churn

### Observation

The boxplot analysis revealed:

* Customers who churned generally had lower tenure.
* Customers who remained with the company had substantially higher tenure.

Approximate Median Tenure:

* Churned Customers: ~10 months
* Retained Customers: ~38 months

### Business Insight

Customer churn occurs predominantly during the early stages of the customer lifecycle. Long-term customers tend to remain loyal to the company.

### Recommendation

Customer retention efforts should focus on the first year of the customer journey, where the risk of churn is highest.

---

## Key Findings from Initial EDA

1. Gender has minimal impact on customer churn.
2. Senior citizens exhibit significantly higher churn rates.
3. Month-to-month contracts are strongly associated with customer churn.
4. Customers with lower tenure are more likely to leave the company.
5. Contract type and tenure appear to be strong candidate features for churn prediction.

---

## Next Steps

* Analyze MonthlyCharges vs Churn
* Analyze TotalCharges vs Churn
* Analyze InternetService vs Churn
* Analyze PaymentMethod vs Churn
* Identify additional churn drivers
* Generate business recommendations based on EDA findings
