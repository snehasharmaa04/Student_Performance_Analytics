import pandas as pd
import numpy as np
from functions import calculate_metrics, process_student_records, get_subject_analysis

def main():
    print("=" * 65)
    print("       STUDENT PERFORMANCE ANALYTICS SYSTEM")
    print("=" * 65)

    # 1. Dataset Read karna (Step 2)
    try:
        df = pd.read_csv('students.csv')
        print(f"[✓] Dataset successfully load hua: {len(df)} records mile.\n")
    except FileNotFoundError:
        print("[!] Error: students.csv file nahi mili!")
        return

    # 2. Data Processing (functions.py ka use karke)
    df = calculate_metrics(df)
    df = process_student_records(df)

    # Processed table display karna
    display_cols = ['StudentID', 'Name', 'Department', 'Total_Marks', 'Average_Marks', 'Grade', 'Status']
    print("--- Processed Student Records ---")
    print(df[display_cols].to_string(index=False))
    print("\n" + "=" * 65)

    # 3. Overall Class Performance (NumPy operations)
    overall_avg = np.round(np.mean(df['Average_Marks'].to_numpy()), 2)
    highest_score = np.max(df['Average_Marks'].to_numpy())
    lowest_score = np.min(df['Average_Marks'].to_numpy())

    total_students = len(df)
    passed_count = int(np.sum(df['Status'].to_numpy() == 'Pass'))
    failed_count = int(np.sum(df['Status'].to_numpy() == 'Fail'))
    pass_pct = np.round((passed_count / total_students) * 100, 2)

    print("--- Class Performance Summary ---")
    print(f"Total Students      : {total_students}")
    print(f"Overall Class Mean  : {overall_avg}%")
    print(f"Highest Average     : {highest_score}%")
    print(f"Lowest Average      : {lowest_score}%")
    print(f"Passed Students     : {passed_count} ({pass_pct}%)")
    print(f"Failed Students     : {failed_count} ({np.round(100 - pass_pct, 2)}%)")
    print("\n" + "=" * 65)

    # 4. Subject-Wise Analysis
    print("--- Subject-Wise Performance Analysis ---")
    subject_df = get_subject_analysis(df)
    print(subject_df.to_string(index=False))
    print("\n" + "=" * 65)

    # 5. Top Performers (Top 3 Students)
    top_performers = df.sort_values(by='Average_Marks', ascending=False).head(3)
    print("--- Top 3 Students ---")
    for rank, (_, row) in enumerate(top_performers.iterrows(), start=1):
        print(f"Rank {rank}: {row['Name']} ({row['Department']}) - Avg: {row['Average_Marks']}% | Grade: {row['Grade']}")
    print("=" * 65)

if _name_ == '_main_':
    main()
