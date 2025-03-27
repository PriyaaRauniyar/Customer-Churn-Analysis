# ============================================================
# Project: Customer Churn Prediction – Data Cleaning Script
# Author: Priya Rauniyar
# Dataset: WA_Fn-UseC_-Telco-Customer-Churn.csv
# Description: This script performs data cleaning on the Telco
#              Customer Churn dataset in preparation for modeling.
# ============================================================

# Import necessary libraries
import pandas as pd

# Step 1: Load the dataset
file_path = "WA_Fn-UseC_-Telco-Customer-Churn.csv"  # Ensure this file is in the same directory
telco_df = pd.read_csv(file_path)

# Step 2: Explore the dataset
print("First 5 rows of the dataset:")
print(telco_df.head())

print("\nDataset shape:", telco_df.shape)

print("\nColumn data types:")
print(telco_df.dtypes)

print("\nMissing values in each column:")
print(telco_df.isnull().sum())

# Step 3: Convert 'TotalCharges' to float (handle errors)
telco_df['TotalCharges'] = pd.to_numeric(telco_df['TotalCharges'], errors='coerce')

# Check how many rows became NaN after conversion
missing_total_charges = telco_df['TotalCharges'].isnull().sum()
print("\nMissing values in 'TotalCharges' after conversion:", missing_total_charges)

# Display rows with missing TotalCharges
null_rows = telco_df[telco_df['TotalCharges'].isnull()]
print("\nRows with missing TotalCharges:")
print(null_rows[['customerID', 'tenure', 'MonthlyCharges', 'TotalCharges']])

# Step 4: Drop rows where TotalCharges is missing
telco_df = telco_df[telco_df['TotalCharges'].notnull()]
print("\nDataset shape after dropping rows with missing TotalCharges:", telco_df.shape)

# Step 5: Drop 'customerID' (not useful for modeling)
telco_df.drop('customerID', axis=1, inplace=True)

# Step 6: Convert 'Churn' column to binary (Yes = 1, No = 0)
telco_df['Churn'] = telco_df['Churn'].map({'Yes': 1, 'No': 0})

# Step 7: Encode all other binary Yes/No columns
yes_no_columns = ['Partner', 'Dependents', 'PhoneService', 'PaperlessBilling',
                  'OnlineSecurity', 'OnlineBackup', 'DeviceProtection',
                  'TechSupport', 'StreamingTV', 'StreamingMovies']

for col in yes_no_columns:
    telco_df[col] = telco_df[col].map({'Yes': 1, 'No': 0})

# Step 8: Encode 'gender' column (Female = 1, Male = 0)
telco_df['gender'] = telco_df['gender'].map({'Female': 1, 'Male': 0})

# Step 9: One-hot encode multi-category columns
telco_df = pd.get_dummies(telco_df, columns=['InternetService', 'Contract', 'PaymentMethod'])

# Step 10: Final shape and check
print("\nFinal dataset shape after encoding:", telco_df.shape)
print("\nData types after encoding:\n", telco_df.dtypes.head(15))

# Step 11: Encode 'MultipleLines' column
telco_df['MultipleLines'] = telco_df['MultipleLines'].replace({
    'No phone service': 0,
    'No': 0,
    'Yes': 1
})
print("\nData type of 'MultipleLines':", telco_df['MultipleLines'].dtype)

# Step 12: Export the cleaned dataset
telco_df.to_csv("cleaned_telco_churn.csv", index=False)
print("\nCleaned dataset saved as 'cleaned_telco_churn.csv'")
