# data_preprocessing.py
# Experiment 2: Data Preprocessing Using Python
# Author: Atharva Waghmode (Roll No: 59, Div: D15A)
# GitHub: https://github.com/wagha-builds/dmbi_exps_59/tree/main/Experiment_2

import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler
import os

# 1. Load Dataset
data_path = os.path.join(os.path.dirname(__file__), "..", "datasets", "student_result_raw.csv")
df = pd.read_csv(data_path)
print(f"[Step 1] Dataset Loaded: Shape = {df.shape}")
print(df.head())

# 2. Check Duplicates and Missing Values
duplicates = df.duplicated().sum()
print(f"\n[Step 2] Duplicate Rows Found: {duplicates}")
print("Missing Values per Column:")
print(df.isnull().sum())

# 3. Remove Duplicate Records
df_clean = df.drop_duplicates().copy()
print(f"\n[Step 3] Shape after removing duplicates: {df_clean.shape}")

# 4. Handle Missing Values (Mean for numerical, Mode for categorical)
for num_col in ['age', 'study_hours_per_week', 'attendance_pct']:
    mean_val = df_clean[num_col].mean()
    df_clean[num_col].fillna(mean_val, inplace=True)

mode_city = df_clean['city'].mode()[0]
df_clean['city'].fillna(mode_city, inplace=True)
print(f"\n[Step 4] Missing values handled. Remaining nulls: {df_clean.isnull().sum().sum()}")

# Standardize class column casing
df_clean['class'] = df_clean['class'].str.upper().replace({'9TH': '9th', '10TH': '10th', '11TH': '11th', '12TH': '12th'})

# 5. Encoding Categorical Data
cat_cols = ['class', 'section', 'subject', 'city']
label_encoders = {}
for col in cat_cols:
    le = LabelEncoder()
    df_clean[col] = le.fit_transform(df_clean[col].astype(str))
    label_encoders[col] = le
print(f"\n[Step 5] Categorical features encoded: {cat_cols}")

# 6. Feature Scaling (StandardScaler)
scaler = StandardScaler()
scale_cols = ['age', 'study_hours_per_week', 'attendance_pct', 'marks_obtained']
df_clean[scale_cols] = scaler.fit_transform(df_clean[scale_cols])
print(f"\n[Step 6] Numerical features standardized using StandardScaler:")
print(df_clean[scale_cols].describe().round(3))

# 7. Final Info & Head
print(f"\n[Step 7] Final preprocessed dataset shape: {df_clean.shape}")
print(df_clean.head())

# Save preprocessed dataset
out_path = os.path.join(os.path.dirname(__file__), "..", "datasets", "student_result_preprocessed.csv")
df_clean.to_csv(out_path, index=False)
print(f"[+] Cleaned dataset saved to: {out_path}")
