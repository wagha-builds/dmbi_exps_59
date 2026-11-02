# Data Mining & Business Intelligence (DMBI) — Lab Experiments

**Student Name:** Atharva Waghmode  
**Roll Number:** 59  
**Division:** D15A  
**Course:** Data Mining and Business Intelligence (DMBI)  
**Academic Year:** 2026 – 2027  
**GitHub Repository:** [https://github.com/wagha-builds/dmbi_exps_59](https://github.com/wagha-builds/dmbi_exps_59)

---

## 📑 Repository Structure & Lab Guidelines Compliance

In accordance with lab submission instructions:
1. **Separate GitHub Folder for Each Experiment:** Each experiment is organized inside its own directory (`Experiment_1` to `Experiment_9`).
2. **Document (DOC / PDF) with GitHub Link:** Every experiment folder contains the complete experiment report (`.docx` soft copy and `.pdf` hard-copy-ready copy) with the individual GitHub link prominently featured at the end.
3. **Dataset Used:** The exact raw and processed datasets are maintained in each experiment's `datasets/` folder.
4. **Program Code:** Executable Python code (`.py`), interactive Jupyter Notebooks (`.ipynb`), SQL DDL scripts (`.sql`), and RapidMiner process workflows (`.rmp`) are provided in each experiment's `code/` folder.
5. **Excel Sheet Directory:** The master experiment tracker and link directory is available as both [`Excel_Sheet_1_All_Experiments.xlsx`](./Excel_Sheet_1_All_Experiments.xlsx) and [`Excel_Sheet_1_All_Experiments.csv`](./Excel_Sheet_1_All_Experiments.csv).

---

## 📂 Experiments Directory & Individual GitHub Links

| Exp No. | Experiment Title | Domain / Topic | Software / Tools | Dataset(s) Used | Individual GitHub Link |
|:---:|:---|:---|:---|:---|:---|
| **01** | **Design of Star Schema and Snowflake Schema** | Data Warehousing & Dimensional Modeling | SQL (DDL/DML), SQLite, Python | Relational Dimensions & Facts (`Result_Fact`, `Issue_Fact`) | [Experiment 1 Link](https://github.com/wagha-builds/dmbi_exps_59/tree/main/Experiment_1) |
| **02** | **Data Preprocessing Using Python** | Data Cleaning & Transformation | Python 3, Pandas, NumPy, Scikit-Learn | `student_result_raw.csv`, `student_result_preprocessed.csv` | [Experiment 2 Link](https://github.com/wagha-builds/dmbi_exps_59/tree/main/Experiment_2) |
| **03** | **Exploratory Data Analysis and Visualization** | EDA & Descriptive Statistics | Python 3, Pandas, Matplotlib, Seaborn | `student_result_raw.csv` (512 records, 9 attributes) | [Experiment 3 Link](https://github.com/wagha-builds/dmbi_exps_59/tree/main/Experiment_3) |
| **04** | **Classification using RapidMiner (Decision Tree & Naïve Bayes)** | Supervised Learning (GUI Workflow) | RapidMiner Studio / Altair AI Studio 10.x | `student_result_classification.csv` (500 records) | [Experiment 4 Link](https://github.com/wagha-builds/dmbi_exps_59/tree/main/Experiment_4) |
| **05** | **Classification using Python (Decision Tree & Naïve Bayes)** | Inbuilt vs. User-Defined Functions | Python 3, Scikit-Learn, Pandas, NumPy | `student_result_classification.csv` (500 records) | [Experiment 5 Link](https://github.com/wagha-builds/dmbi_exps_59/tree/main/Experiment_5) |
| **06** | **Clustering using Python (K-Means Clustering)** | Unsupervised Learning & Segmentation | Python 3, Scikit-Learn, Matplotlib, Seaborn | `jiohotstar_viewing_behavior.csv` (10,000 records) | [Experiment 6 Link](https://github.com/wagha-builds/dmbi_exps_59/tree/main/Experiment_6) |
| **07** | **Clustering using RapidMiner / Altair AI Studio** | K-Means Pipeline & Normalization | RapidMiner Studio / Altair AI Studio 10.x | `jiohotstar_rapidminer_cluster.csv` (10,000 records) | [Experiment 7 Link](https://github.com/wagha-builds/dmbi_exps_59/tree/main/Experiment_7) |
| **08** | **Association Mining Algorithm (Apriori) using Python** | Association Rule Mining & Market Basket | Python 3, Mlxtend, Pandas, Matplotlib | `jiohotstar_behavioral_transactions.csv`, `groceries_dataset.csv` | [Experiment 8 Link](https://github.com/wagha-builds/dmbi_exps_59/tree/main/Experiment_8) |
| **09** | **Association Mining Algorithm (FP-Growth) using RapidMiner** | Frequent Pattern Mining & Rules | RapidMiner Studio / Altair AI Studio 10.x | `jiohotstar_association_data.csv`, `groceries_dataset.csv` | [Experiment 9 Link](https://github.com/wagha-builds/dmbi_exps_59/tree/main/Experiment_9) |

---

## 🚀 Quick Execution Guide

To reproduce or run any experiment locally:

```bash
# 1. Clone the repository
git clone https://github.com/wagha-builds/dmbi_exps_59.git
cd dmbi_exps_59

# 2. Install required Python packages
pip install pandas numpy scikit-learn matplotlib seaborn mlxtend openpyxl python-docx

# 3. Run individual experiment code
# Experiment 1 (Star & Snowflake Schema DW)
python Experiment_1/code/star_snowflake_dw.py

# Experiment 2 (Data Preprocessing)
python Experiment_2/code/data_preprocessing.py

# Experiment 3 (Exploratory Data Analysis)
python Experiment_3/code/eda_visualization.py

# Experiment 4 (RapidMiner Classification Simulation)
python Experiment_4/code/rapidminer_classification_simulation.py

# Experiment 5 (Python Classification: Inbuilt vs User-Defined)
python Experiment_5/code/classification_python.py

# Experiment 6 (K-Means Clustering)
python Experiment_6/code/kmeans_clustering.py

# Experiment 7 (RapidMiner Clustering Simulation)
python Experiment_7/code/rapidminer_clustering_simulation.py

# Experiment 8 (Apriori Association Rule Mining)
python Experiment_8/code/apriori_association_mining.py

# Experiment 9 (FP-Growth Association Rule Mining)
python Experiment_9/code/rapidminer_fpgrowth_simulation.py
```

---

## 📜 Submission Details

- **Soft Copy Submission:** Both `.docx` and `.pdf` files are provided in each experiment folder, complete with embedded diagrams, screenshots, performance tables, and the individual GitHub links.
- **Hard Copy Submission:** Ready-to-print PDF documents formatted with cover headings and GitHub verification footers are included inside every experiment folder.
