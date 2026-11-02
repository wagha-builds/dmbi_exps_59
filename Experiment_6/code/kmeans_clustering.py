# kmeans_clustering.py
# Experiment 6: K-Means Clustering on JioHotstar Viewer Engagement Dataset using Python
# Author: Atharva Waghmode (Roll No: 59, Div: D15A)
# GitHub: https://github.com/wagha-builds/dmbi_exps_59/tree/main/Experiment_6

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score, davies_bouldin_score
import os

# 1. Load Dataset
data_path = os.path.join(os.path.dirname(__file__), "..", "datasets", "jiohotstar_viewing_behavior.csv")
df = pd.read_csv(data_path)
print(f"[Step 1] JioHotstar Dataset Loaded: {df.shape[0]} records, {df.shape[1]} attributes")
print(df.head())

# 2. Select Features for Clustering (excluding drop-off target columns)
features = [
    'average_watch_percentage', 'episode_duration', 'hook_strength', 
    'pacing_score', 'pause_count', 'rewind_count', 'cognitive_load'
]
X = df[features].copy()
print(f"\n[Step 2] Selected Features for Clustering: {features}")

# 3. Standardize Features using StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
print("\n[Step 3] Features standardized (mean ~ 0, std ~ 1).")

# 4. Elbow Method to find optimal K
print("\n[Step 4] Running Elbow Method for K=1 to 8...")
inertia_list = []
k_range = range(1, 9)
for k in k_range:
    km = KMeans(n_clusters=k, random_state=42, n_init=10)
    km.fit(X_scaled)
    inertia_list.append(km.inertia_)

plt.figure(figsize=(7, 4))
plt.plot(k_range, inertia_list, marker='o', linestyle='--', color='darkblue')
plt.title("Elbow Method for Optimal Number of Clusters (K)")
plt.xlabel("Number of Clusters (K)")
plt.ylabel("Inertia (Sum of Squared Distances)")
plt.grid(True)
plt.tight_layout()
plt.savefig("elbow_method.png")
plt.close()
print("Elbow plot saved as 'elbow_method.png'. Optimal K = 4 selected.")

# 5. Apply K-Means with K = 4
kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
df['Cluster'] = kmeans.fit_predict(X_scaled)
print("\n[Step 5] K-Means clustering completed with 4 clusters.")
cluster_counts = df['Cluster'].value_counts().sort_index()
print("Cluster Membership Counts:")
for c_id, count in cluster_counts.items():
    print(f"  Cluster {c_id}: {count:,} records ({count/len(df)*100:.1f}%)")

# 6. Evaluation Measures
sil_score = silhouette_score(X_scaled[:2000], df['Cluster'][:2000]) # sampled for speed
db_score = davies_bouldin_score(X_scaled, df['Cluster'])
print(f"\n[Step 6] Clustering Evaluation Measures:")
print(f"  Inertia: {kmeans.inertia_:.2f}")
print(f"  Silhouette Score: {sil_score:.3f}")
print(f"  Davies-Bouldin Index: {db_score:.3f}")

# 7. Visualization: Watch Percentage vs Cognitive Load
plt.figure(figsize=(8, 5))
palette = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']
sns.scatterplot(
    x='average_watch_percentage', 
    y='cognitive_load', 
    hue='Cluster', 
    data=df, 
    palette=palette, 
    alpha=0.6, 
    s=25
)
plt.title("K-Means Clustering: Average Watch % vs Cognitive Load (K=4)")
plt.xlabel("Average Watch Percentage (%)")
plt.ylabel("Cognitive Load Score")
plt.legend(title="Cluster")
plt.tight_layout()
plt.savefig("kmeans_clusters_scatter.png")
plt.close()
print("Scatter plot saved as 'kmeans_clusters_scatter.png'.")

# 8. Cluster-wise Feature Profiling
print("\n[Step 7] Cluster-wise Mean Feature Profiles:")
profile = df.groupby('Cluster')[features].mean().round(2)
print(profile)
