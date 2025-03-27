# ============================================================
# Project: Customer Churn Prediction – Exploratory Data Analysis
# Author: Priya Rauniyar
# Dataset: WA_Fn-UseC_-Telco-Customer-Churn.csv (raw)
# Description: This script performs EDA to visualize churn trends.
# ============================================================

# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set style
sns.set(style="whitegrid")

# Step 1: Load original dataset
df = pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")

# Step 2: Clean TotalCharges column and drop missing
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
df = df[df['TotalCharges'].notnull()]

# Step 3: Check Churn column (no need to convert here; it's already Yes/No)
print("Unique Churn values:", df['Churn'].unique())

# Step 4: Plot churn distribution
plt.figure(figsize=(6, 4))
sns.countplot(x='Churn', data=df)
plt.title("Churn Distribution")
plt.xlabel("Churn (Yes = Left, No = Stayed)")
plt.ylabel("Number of Customers")
plt.savefig("churn_distribution.png", dpi=300, bbox_inches='tight')
plt.show()

# Step 5: Plot churn by contract type
plt.figure(figsize=(8, 5))
sns.countplot(data=df, x='Contract', hue='Churn')
plt.title("Churn by Contract Type")
plt.xlabel("Contract Type")
plt.ylabel("Number of Customers")
plt.legend(title="Churn")
plt.savefig("churn_by_contract.png", dpi=300, bbox_inches='tight')
plt.show()
# Plot: Monthly Charges vs Churn
plt.figure(figsize=(8, 5))
sns.boxplot(x='Churn', y='MonthlyCharges', data=df, palette="Set2")
plt.title("Monthly Charges by Churn")
plt.xlabel("Churn")
plt.ylabel("Monthly Charges")
plt.savefig("monthly_charges_by_churn.png", dpi=300, bbox_inches='tight')
plt.show()

# Plot: Tenure vs Churn
plt.figure(figsize=(8, 5))
sns.boxplot(x='Churn', y='tenure', data=df, palette="Set1")
plt.title("Tenure by Churn")
plt.xlabel("Churn")
plt.ylabel("Customer Tenure (Months)")
plt.savefig("tenure_by_churn.png", dpi=300, bbox_inches='tight')
plt.show()
