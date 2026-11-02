# eda_visualization.py
# Experiment 3: Exploratory Data Analysis and Visualization
# Author: Atharva Waghmode (Roll No: 59, Div: D15A)
# GitHub: https://github.com/wagha-builds/dmbi_exps_59/tree/main/Experiment_3

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# 1. Load Dataset
data_path = os.path.join(os.path.dirname(__file__), "..", "datasets", "student_result_raw.csv")
df = pd.read_csv(data_path)
print(f"[Step 1] Loaded Dataset: Shape = {df.shape}")
print("Missing values:")
print(df.isnull().sum())

# 2. Central Tendency
print("\n--- Task 1: Measures of Central Tendency ---")
num_cols = ['age', 'study_hours_per_week', 'attendance_pct', 'marks_obtained']
for col in num_cols:
    print(f"{col:22s} | Mean: {df[col].mean():.2f} | Median: {df[col].median():.2f}")
print("\nCategorical Modes:")
for col in ['class', 'section', 'subject', 'city']:
    print(f"{col:10s} Mode: {df[col].mode()[0]}")

# 3. Measures of Dispersion
print("\n--- Task 2: Measures of Dispersion ---")
for col in num_cols:
    std = df[col].std()
    var = df[col].var()
    rng = df[col].max() - df[col].min()
    iqr = df[col].quantile(0.75) - df[col].quantile(0.25)
    print(f"{col:22s} | Std: {std:.2f} | Var: {var:.2f} | Range: {rng:.2f} | IQR: {iqr:.2f}")

# 4. Correlation Matrix
print("\n--- Task 3: Correlation Matrix ---")
corr = df[num_cols].corr()
print(corr.round(4))

# 5. Visualizations
plt.figure(figsize=(8, 4))
sns.histplot(df['study_hours_per_week'].dropna(), kde=True, bins=30, color='royalblue')
plt.title("Histogram of Study Hours per Week (Right-Skewed with Outliers)")
plt.xlabel("Study Hours per Week")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("hist_study_hours.png")
plt.close()

# Boxplot before cleanup
plt.figure(figsize=(10, 4))
sns.boxplot(x='class', y='marks_obtained', data=df)
plt.title("Boxplot of Marks Obtained by Class (Before Cleanup - 16 Variants)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("boxplot_before_cleanup.png")
plt.close()

# Boxplot after cleanup
df_clean_class = df.copy()
df_clean_class['class'] = df_clean_class['class'].str.upper().replace({'9TH': '9th', '10TH': '10th', '11TH': '11th', '12TH': '12th'})
plt.figure(figsize=(7, 4))
sns.boxplot(x='class', y='marks_obtained', data=df_clean_class, palette='Set2')
plt.title("Boxplot of Marks Obtained by Class (After Cleanup - 4 Classes)")
plt.tight_layout()
plt.savefig("boxplot_after_cleanup.png")
plt.close()

# Heatmap
plt.figure(figsize=(6, 5))
sns.heatmap(corr, annot=True, cmap='Blues', fmt=".3f", cbar=True)
plt.title("Feature Correlation Heatmap")
plt.tight_layout()
plt.savefig("correlation_heatmap.png")
plt.close()

# Scatter plot
plt.figure(figsize=(8, 5))
sns.scatterplot(x='attendance_pct', y='marks_obtained', hue='subject', data=df, alpha=0.8)
plt.title("Scatter Plot: Attendance % vs Marks Obtained")
plt.tight_layout()
plt.savefig("scatter_attendance_vs_marks.png")
plt.close()

print("[+] All EDA metrics calculated and visualization plots saved successfully!")
