# rapidminer_classification_simulation.py
# Simulating RapidMiner Decision Tree and Naive Bayes Classification Pipeline
# Author: Atharva Waghmode (Roll No: 59, Div: D15A)
# GitHub: https://github.com/wagha-builds/dmbi_exps_59/tree/main/Experiment_4

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import os

# Step 1: Import Dataset
data_path = os.path.join(os.path.dirname(__file__), "..", "datasets", "student_result_classification.csv")
df = pd.read_csv(data_path)
print(f"[Step 1] Retrieved ExampleSet: {df.shape[0]} examples, {df.shape[1]} attributes")

# Step 2: Select Attributes (drop student_id) & Set Role
X = df.drop(columns=['student_id', 'Result_Category'])
y = df['Result_Category']

# Encode categorical variables
le = LabelEncoder()
for col in ['class', 'section', 'subject', 'city']:
    X[col] = le.fit_transform(X[col])

# Step 3: Split Data (80% / 20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
print(f"[Step 3] Partitioned data: Train={len(X_train)} instances, Test={len(X_test)} instances")

# Step 4: Train Decision Tree Model
dt = DecisionTreeClassifier(max_depth=5, criterion="gini", random_state=42)
dt.fit(X_train, y_train)
y_pred_dt = dt.predict(X_test)

print("\n" + "="*50)
print("--- Decision Tree Results (RapidMiner Replicated) ---")
print(f"Accuracy: {accuracy_score(y_test, y_pred_dt)*100:.2f}%")
print("Confusion Matrix:")
cm_dt = confusion_matrix(y_test, y_pred_dt, labels=['Pass', 'Fail'])
print(pd.DataFrame(cm_dt, index=['Actual Pass', 'Actual Fail'], columns=['Pred Pass', 'Pred Fail']))
print("\nClassification Report:")
print(classification_report(y_test, y_pred_dt))

# Step 5: Train Naive Bayes Model
nb = GaussianNB()
nb.fit(X_train, y_train)
y_pred_nb = nb.predict(X_test)

print("="*50)
print("--- Naive Bayes Results (RapidMiner Replicated) ---")
print(f"Accuracy: {accuracy_score(y_test, y_pred_nb)*100:.2f}%")
print("Confusion Matrix:")
cm_nb = confusion_matrix(y_test, y_pred_nb, labels=['Pass', 'Fail'])
print(pd.DataFrame(cm_nb, index=['Actual Pass', 'Actual Fail'], columns=['Pred Pass', 'Pred Fail']))
print("\nClassification Report:")
print(classification_report(y_test, y_pred_nb))
