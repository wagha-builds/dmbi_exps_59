# rapidminer_fpgrowth_simulation.py
# Simulating RapidMiner FP-Growth and Association Rule Mining Workflow
# Author: Atharva Waghmode (Roll No: 59, Div: D15A)
# GitHub: https://github.com/wagha-builds/dmbi_exps_59/tree/main/Experiment_9

import pandas as pd
from mlxtend.frequent_patterns import fpgrowth, association_rules
import os

# Step 1: Retrieve Dataset
data_path = os.path.join(os.path.dirname(__file__), "..", "datasets", "jiohotstar_association_data.csv")
df = pd.read_csv(data_path)
print(f"[Step 1] Retrieved Dataset: {df.shape[0]} records loaded into RapidMiner")

# Step 2: Numerical to Binominal (converting 0/1 integers to boolean)
df_binominal = df.astype(bool)
print("[Step 2] Converted numeric columns to binominal (true/false) attributes.")

# Step 3: FP-Growth Operator (min_support = 0.05)
print("\n[Step 3] Running FP-Growth operator (min_support = 0.05)...")
frequent_sets = fpgrowth(df_binominal, min_support=0.05, use_colnames=True)
print(f"Discovered {len(frequent_sets)} frequent itemsets.")

# Step 4: Create Association Rules Operator (min_confidence = 0.5)
rules = association_rules(frequent_sets, metric="confidence", min_threshold=0.5)
rules = rules[rules['lift'] > 1.0].sort_values(by="confidence", ascending=False)

rules['rule_display'] = (
    rules['antecedents'].apply(lambda x: ', '.join(list(x))) + 
    ' --> ' + 
    rules['consequents'].apply(lambda x: ', '.join(list(x)))
)

print("\n" + "="*50)
print("--- RapidMiner Association Rules Output ---")
print(rules[['rule_display', 'support', 'confidence', 'lift']].head(10).to_string(index=False))
print("="*50)
print("\n[+] Association rules generated successfully!")
