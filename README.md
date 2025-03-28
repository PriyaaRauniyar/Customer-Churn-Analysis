# Customer Churn Analysis – Business Analytics Portfolio Project

## 📌 Table of Contents
- [Project Overview](#project-overview)
- [Business Objective](#business-objective)
- [Tools and Technologies](#tools-and-technologies)
- [Step-by-Step Process](#step-by-step-process)
- [Exploratory Data Visualizations](#exploratory-data-visualizations)
- [Key Insights](#key-insights)
- [Business Value](#business-value)
- [What I Learned](#what-i-learned)
- [Conclusion](#conclusion)
- [Dataset Source](#dataset-source)
- [License](#license)

---

## Project Overview
This project presents a complete end-to-end customer churn analysis using a real-world telecom dataset. It demonstrates key business analytics skills including data cleaning, exploratory data analysis (EDA), predictive modeling, and dashboard development. The objective is to identify key drivers of churn, provide actionable insights for customer retention strategies, and present the results in a visually compelling format.

The final deliverables include Python scripts for preprocessing and modeling, EDA charts, a cleaned dataset, a logistic regression model evaluation, and a professional Power BI dashboard for executive-level insights.

---

## Business Objective
Telecom companies often struggle with customer retention. High churn rates can severely impact revenue and long-term growth. This project analyzes telecom customer data to:

- Understand patterns and factors contributing to churn
- Predict which customers are likely to churn
- Help the business implement targeted retention strategies
- Visualize insights in a dynamic, decision-ready dashboard

---

## Tools and Technologies

**Languages & Libraries:**
- Python: pandas, numpy, seaborn, matplotlib, scikit-learn

**Data Visualization:**
- Power BI: Slicers, KPIs, DAX measures, interactive visuals

**Others:**
- Git & GitHub for version control and sharing

---

## Step-by-Step Process

### 1. Data Cleaning (Python)
- Handled missing values
- Converted TotalCharges to numeric
- Removed blank entries and rows with zero tenure
- One-hot encoded categorical variables for modeling

### 2. Exploratory Data Analysis (Python)
- Visualized churn distribution
- Analyzed churn across contract types, monthly charges, and tenure
- Generated clear, well-labeled plots using seaborn and matplotlib

### 3. Predictive Modeling (Python)
- Used logistic regression to classify churn
- Evaluated model using accuracy, precision, recall, F1-score
- Generated confusion matrix and classification report

### 4. Dashboard Development (Power BI)
- Built interactive dashboard with:
  - KPIs: Total Customers, Churn Rate, Avg Monthly Charges
  - Bar charts: Churn by Contract Type, Churn Distribution
  - Slicer: Internet Service Type
  - DAX measure for Churn Rate (%)
- Designed for business users and decision-makers

---

## Exploratory Data Visualizations
Below are key visuals used during EDA to analyze churn behavior and identify business insights.

### 📊 Churn Distribution

![Churn Distribution](churn_distribution.png)

The dataset shows a noticeable imbalance between retained and churned customers. This imbalance can influence modeling performance and highlights the need to focus on customer retention.

### 📊 Churn by Contract Type

![Churn by Contract Type](churn_by_contract.png)

Customers on month-to-month contracts churn significantly more than those with one- or two-year contracts. A key business recommendation is to incentivize long-term contracts through loyalty rewards or pricing benefits.

### 📊 Monthly Charges by Churn

![Monthly Charges by Churn](monthly_charges_by_churn.png)

Churned customers tend to have higher monthly charges. This could indicate dissatisfaction with pricing. Business teams can evaluate pricing tiers or offer cost-reduction bundles for high-value customers at risk of churning.

### 📊 Tenure by Churn

![Tenure by Churn](tenure_by_churn.png)

Customers who churned tend to have much lower tenure. This suggests early-stage disengagement and supports strategies such as onboarding journeys, early follow-ups, or welcome offers to improve retention.

---

## 📊 Power BI Dashboard Screenshot

![Churn Analysis Dashboard](dashboard_screenshot.png)

---

## Key Insights
- Month-to-month contract customers are significantly more likely to churn
- Fiber optic internet users show a higher churn rate compared to DSL
- Customers with lower tenure and higher monthly charges tend to leave more

These insights can guide retention strategies such as:
- Loyalty discounts for month-to-month customers
- Enhanced support or bundled offers for high-risk segments
- Personalized welcome journeys and early engagement campaigns
- Tiered pricing models to reduce dissatisfaction among high-paying customers
- Proactive outreach or rewards for customers with low tenure

---

## Business Value
This project mimics the responsibilities of a business analyst in a real organization:
- Data wrangling and validation
- Investigating churn causes through data
- Applying basic machine learning to forecast churn likelihood
- Creating an interactive executive dashboard

---

## What I Learned
- Applied real business analytics techniques from start to finish
- Strengthened data visualization and communication skills
- Improved proficiency in Python, Power BI, and model evaluation
- Gained hands-on experience in building projects aligned with business outcomes

---

## Conclusion
This project demonstrates how structured analytics, combined with stakeholder-oriented thinking, can transform raw customer data into powerful business decisions. Through clear visual storytelling, data modeling, and dashboard insights, we can recommend practical actions to reduce churn and retain customers effectively.

### Suggested Retention Strategies
- Offer exclusive loyalty perks to customers on month-to-month plans
- Create tailored welcome journeys for new customers in their first 3 months
- Provide proactive customer care to high-risk users (low tenure, high charges)
- Introduce personalized pricing plans based on usage patterns
- Run targeted outreach campaigns to fiber optic internet users at risk

---

## Dataset Source
- Raw Dataset: [IBM Sample Telecom Dataset on Kaggle](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)

---

## License
This project is intended for educational and portfolio use.









