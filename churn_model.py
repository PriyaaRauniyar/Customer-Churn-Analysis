# ============================================================
# Project: Customer Churn Prediction – Logistic Regression Model
# Author: Priya Rauniyar
# ============================================================

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Step 1: Load the cleaned dataset
df = pd.read_csv("cleaned_telco_churn.csv")

# Drop rows with any missing values (just to be safe)
df.dropna(inplace=True)


# Step 2: Drop irrelevant columns (e.g., customerID if still there)
if 'customerID' in df.columns:
    df.drop('customerID', axis=1, inplace=True)

# Step 3: Define features and target
X = df.drop('Churn', axis=1)
y = df['Churn']

# Step 4: Split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 5: Train logistic regression model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Step 6: Make predictions
y_pred = model.predict(X_test)

# Step 7: Evaluate model
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
report = classification_report(y_test, y_pred)

# Step 8: Print results
print("Logistic Regression Model Evaluation\n")
print("Accuracy:", round(accuracy * 100, 2), "%")
print("\nConfusion Matrix:\n", conf_matrix)
print("\nClassification Report:\n", report)

# Step 9: Save results to a text file
with open("churn_model_results.txt", "w") as f:
    f.write("Logistic Regression Model Evaluation\n")
    f.write(f"Accuracy: {round(accuracy * 100, 2)} %\n\n")
    f.write("Confusion Matrix:\n")
    f.write(str(conf_matrix))
    f.write("\n\nClassification Report:\n")
    f.write(report)
