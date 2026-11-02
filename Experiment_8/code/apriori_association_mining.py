# apriori_association_mining.py
# Experiment 8: Apriori Association Rule Mining using Python
# Author: Atharva Waghmode (Roll No: 59, Div: D15A)
# GitHub: https://github.com/wagha-builds/dmbi_exps_59/tree/main/Experiment_8

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mlxtend.frequent_patterns import apriori, association_rules
import os

# 1. Load Behavioral Transaction Dataset
data_path = os.path.join(os.path.dirname(__file__), "..", "datasets", "jiohotstar_behavioral_transactions.csv")
df = pd.read_csv(data_path)
print(f"[Step 1] JioHotstar Behavioral Transaction Matrix Loaded: {df.shape[0]} transactions, {df.shape[1]} items")
print(df.head())

# 2. Item Support Frequencies
print("\n[Step 2] Individual Item Frequencies and Support:")
item_support = df.mean().sort_values(ascending=False)
for item, supp in item_support.items():
    print(f"  {item:25s}: Support = {supp:.4f} ({supp*100:.1f}%)")

# 3. Apply Apriori Algorithm (min_support = 0.05)
print("\n[Step 3] Running Apriori Algorithm (min_support = 0.05)...")
frequent_itemsets = apriori(df.astype(bool), min_support=0.05, use_colnames=True)
frequent_itemsets['length'] = frequent_itemsets['itemsets'].apply(lambda x: len(x))
frequent_itemsets = frequent_itemsets.sort_values(by='support', ascending=False)
print(f"Total Frequent Itemsets Discovered: {len(frequent_itemsets)}")
print(frequent_itemsets.head(10))

# 4. Generate Association Rules (metric = 'confidence', min_threshold = 0.5)
print("\n[Step 4] Generating Association Rules (min confidence = 0.5, lift > 1.0)...")
rules = association_rules(frequent_itemsets, metric='confidence', min_threshold=0.5)
rules = rules[rules['lift'] > 1.0].sort_values(by='lift', ascending=False)
print(f"Total Association Rules Generated: {len(rules)}")

# Format antecedent and consequent for clean display
rules['rule'] = rules['antecedents'].apply(lambda x: ', '.join(list(x))) + ' => ' + rules['consequents'].apply(lambda x: ', '.join(list(x)))
display_cols = ['rule', 'support', 'confidence', 'lift']
print("\nTop 10 Association Rules by Lift:")
print(rules[display_cols].head(10).to_string(index=False))

# 5. Scatter Plot: Support vs Confidence colored by Lift
plt.figure(figsize=(8, 5))
scatter = plt.scatter(rules['support'], rules['confidence'], c=rules['lift'], cmap='viridis', s=60, alpha=0.8)
plt.colorbar(scatter, label='Lift')
plt.title("Association Rules: Support vs Confidence (Colored by Lift)")
plt.xlabel("Support")
plt.ylabel("Confidence")
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig("association_rules_scatter.png")
plt.close()
print("\n[Step 5] Visualization plot saved as 'association_rules_scatter.png'.")

# 6. Conclusion summary
top_rule = rules.iloc[0]
print("\n" + "="*50)
print(f"Strongest Rule Discovered: {top_rule['rule']}")
print(f"  Support: {top_rule['support']:.4f} | Confidence: {top_rule['confidence']:.4f} | Lift: {top_rule['lift']:.4f}")
print("="*50)
