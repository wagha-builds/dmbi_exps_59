# rapidminer_clustering_simulation.py
# Simulating RapidMiner / Altair AI Studio K-Means Clustering Workflow
# Author: Atharva Waghmode (Roll No: 59, Div: D15A)
# GitHub: https://github.com/wagha-builds/dmbi_exps_59/tree/main/Experiment_7

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import os

# Step 1: Retrieve Dataset (10,000 records due to free tier limit)
data_path = os.path.join(os.path.dirname(__file__), "..", "datasets", "jiohotstar_rapidminer_cluster.csv")
df = pd.read_csv(data_path)
print(f"[Step 1] Retrieved ExampleSet: {len(df)} examples loaded into Altair AI Studio")

# Step 2: Select Attributes
features = ['average_watch_percentage', 'cognitive_load', 'episode_duration', 'hook_strength', 'pacing_score', 'pause_count', 'rewind_count']
X = df[features].copy()

# Step 3: Replace Missing Values (mean imputation)
X = X.fillna(X.mean())

# Step 4: Normalize (Z-transformation)
scaler = StandardScaler()
X_norm = scaler.fit_transform(X)

# Step 5: Clustering (K-Means with k=4)
kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
df['cluster'] = kmeans.fit_predict(X_norm)

print("\n" + "="*50)
print("--- Altair AI Studio Cluster Model Results ---")
counts = df['cluster'].value_counts().sort_index()
for c_id, count in counts.items():
    print(f"  Cluster {c_id}: {count:,} items")
print(f"Total Number of Processed Records: {len(df):,}")
print("="*50)
print("\nStatistics View (Normalized Features):")
norm_df = pd.DataFrame(X_norm, columns=features)
print(norm_df.describe().round(3))
