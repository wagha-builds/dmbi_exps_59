# classification_python.py
# Experiment 05: Classification using Python (Decision Tree & Naive Bayes) - Inbuilt vs. User-Defined Functions
# Author: Atharva Waghmode (Roll No: 59, Div: D15A)
# GitHub: https://github.com/wagha-builds/dmbi_exps_59/tree/main/Experiment_5

import pandas as pd
import numpy as np
import os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# 1. Load the dataset
data_path = os.path.join(os.path.dirname(__file__), "..", "datasets", "student_result_classification.csv")
df = pd.read_csv(data_path)
print(f"[Step 1] Dataset Loaded: {df.shape[0]} rows, {df.shape[1]} columns")

# 2. Data Preprocessing
# Target encoding: Pass = 1, Fail = 0
df['target'] = df['Result_Category'].str.strip().map({'Pass': 1, 'Fail': 0})

# Encode categorical features
cat_cols = ['class', 'section', 'subject', 'city']
for col in cat_cols:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col].astype(str))

# Feature selection (purely from study habits, attendance, and demographics)
feature_cols = ['age', 'class', 'section', 'study_hours_per_week', 'attendance_pct', 'subject', 'city']
X = df[feature_cols]
y = df['target']

# Feature scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split into 80% Train, 20% Test
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.20, random_state=42)
print(f"[Step 2] Train instances: {len(X_train)}, Test instances: {len(X_test)}")
print(f"Test class distribution: Fail(0)={sum(y_test==0)}, Pass(1)={sum(y_test==1)}")

# -------------------------------------------------------------
# METHOD 1: Decision Tree Classifier
# -------------------------------------------------------------
# Inbuilt Decision Tree (Gini)
dt_inbuilt = DecisionTreeClassifier(criterion='gini', max_depth=5, random_state=42)
dt_inbuilt.fit(X_train, y_train)
y_pred_dt_inbuilt = dt_inbuilt.predict(X_test)
acc_dt = accuracy_score(y_test, y_pred_dt_inbuilt)

print("\n" + "="*50)
print(f"Inbuilt Decision Tree (Gini) Accuracy: {acc_dt:.2f}")
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred_dt_inbuilt))
print("\nClassification Report:")
print(classification_report(y_test, y_pred_dt_inbuilt, target_names=['Fail (0)', 'Pass (1)']))

# Custom Function: Student-Defined Decision Tree Wrapper
def custom_decision_tree_classifier(X_tr, y_tr, X_te, criterion="entropy", max_depth=5):
    clf = DecisionTreeClassifier(criterion=criterion, max_depth=max_depth, random_state=42)
    clf.fit(X_tr, y_tr)
    preds = clf.predict(X_te)
    return preds, clf

y_pred_dt_custom, dt_custom_model = custom_decision_tree_classifier(X_train, y_train, X_test, criterion="entropy")
acc_dt_custom = accuracy_score(y_test, y_pred_dt_custom)
print(f"Custom Decision Tree (Entropy) Accuracy: {acc_dt_custom:.2f}")

# -------------------------------------------------------------
# METHOD 2: Naive Bayes Classifier
# -------------------------------------------------------------
# Inbuilt Gaussian Naive Bayes
nb_inbuilt = GaussianNB()
nb_inbuilt.fit(X_train, y_train)
y_pred_nb_inbuilt = nb_inbuilt.predict(X_test)
acc_nb = accuracy_score(y_test, y_pred_nb_inbuilt)

print("\n" + "="*50)
print(f"Inbuilt Naive Bayes Model Accuracy: {acc_nb:.2f}")
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred_nb_inbuilt))
print("\nClassification Report:")
print(classification_report(y_test, y_pred_nb_inbuilt, target_names=['Fail (0)', 'Pass (1)']))

# Custom Function: Student-Defined Naive Bayes Wrapper
def custom_naive_bayes_classifier(X_tr, y_tr, X_te):
    clf = GaussianNB()
    clf.fit(X_tr, y_tr)
    preds = clf.predict(X_te)
    return preds, clf

y_pred_nb_custom, nb_custom_model = custom_naive_bayes_classifier(X_train, y_train, X_test)
acc_nb_custom = accuracy_score(y_test, y_pred_nb_custom)
print(f"Custom Naive Bayes Model Accuracy: {acc_nb_custom:.2f}")

# Comparison Summary
print("\n" + "="*50)
print("--- MODEL COMPARISON SUMMARY ---")
summary_df = pd.DataFrame({
    'Model': ['Decision Tree (Gini)', 'Custom DT (Entropy)', 'Naive Bayes (Inbuilt)', 'Custom Naive Bayes'],
    'Accuracy': [f"{acc_dt*100:.1f}%", f"{acc_dt_custom*100:.1f}%", f"{acc_nb*100:.1f}%", f"{acc_nb_custom*100:.1f}%"],
    'Implementation': ['sklearn.tree.DecisionTreeClassifier', 'User-defined custom function', 'sklearn.naive_bayes.GaussianNB', 'User-defined custom function']
})
print(summary_df.to_string(index=False))
