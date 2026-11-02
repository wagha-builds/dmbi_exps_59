# star_snowflake_dw.py
# Implementation & verification of Star and Snowflake Schemas in SQLite
# Author: Atharva Waghmode (Roll No: 59, Div: D15A)
# GitHub: https://github.com/wagha-builds/dmbi_exps_59/tree/main/Experiment_1

import sqlite3
import pandas as pd
import os

DB_FILE = "college_dw.db"
if os.path.exists(DB_FILE):
    os.remove(DB_FILE)

conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()

# Load and execute SQL schema
schema_file = os.path.join(os.path.dirname(__file__), "schema_design.sql")
with open(schema_file, "r", encoding="utf-8") as f:
    sql_script = f.read()

cursor.executescript(sql_script)
print("[+] Star Schema and Snowflake Schema created successfully in SQLite DW!")

# Load sample data into tables
data_dir = os.path.join(os.path.dirname(__file__), "..", "datasets")
tables = [
    ("Date_Dimension", "Date_Dimension.csv"),
    ("Student_Dimension", "Student_Dimension_Star.csv"),
    ("Subject_Dimension", "Subject_Dimension_Star.csv"),
    ("Exam_Dimension", "Exam_Dimension.csv"),
    ("Result_Fact", "Result_Fact.csv"),
    ("Staff_Dimension", "Staff_Dimension.csv"),
    ("Book_Dimension", "Book_Dimension.csv"),
    ("Issue_Fact", "Issue_Fact.csv"),
    ("Department_SubDimension", "Department_Dimension.csv"),
    ("Course_SubDimension", "Course_Dimension.csv"),
    ("Student_Dimension_Snowflake", "Student_Dimension_Snowflake.csv"),
    ("Subject_Dimension_Snowflake", "Subject_Dimension_Snowflake.csv")
]

for table_name, csv_file in tables:
    csv_path = os.path.join(data_dir, csv_file)
    if os.path.exists(csv_path):
        df = pd.read_csv(csv_path)
        df.to_sql(table_name, conn, if_exists="append", index=False)
        print(f" Loaded {len(df)} rows into {table_name}")

print("\n--- Verification Query: Aggregated Student Performance by Subject ---")
query = """
SELECT 
    sub.Subject_Name,
    COUNT(rf.Result_ID) AS Total_Exams_Recorded,
    ROUND(AVG(rf.Marks_Obtained), 2) AS Average_Marks,
    MIN(rf.Marks_Obtained) AS Min_Marks,
    MAX(rf.Marks_Obtained) AS Max_Marks
FROM Result_Fact rf
JOIN Subject_Dimension sub ON rf.Subject_ID = sub.Subject_ID
GROUP BY sub.Subject_Name;
"""
result_df = pd.read_sql_query(query, conn)
print(result_df)

conn.close()
