import pandas as pd
import numpy as np

# Subject columns definimg
SUBJECT_COLUMNS = ['Maths', 'Physics', 'Computer_Science']

def calculate_metrics(df):
    marks_matrix = df[SUBJECT_COLUMNS].to_numpy()

    # NumPy array operations (row-wise calculation)
    df['Total_Marks'] = np.sum(marks_matrix, axis=1)
    df['Average_Marks'] = np.round(np.mean(marks_matrix, axis=1), 2)
    return df

def assign_grade(average):
    if average >= 90:
        return 'A+'
    elif average >= 80:
        return 'A'
    elif average >= 70:
        return 'B'
    elif average >= 60:
        return 'C'
    elif average >= 50:
        return 'D'
    else:
        return 'F'

def determine_status(row):
    subject_pass = all(row[sub] >= 40 for sub in SUBJECT_COLUMNS)
    attendance_pass = row['Attendance'] >= 75
    return 'Pass' if (subject_pass and attendance_pass) else 'Fail'

def process_student_records(df):
    grades = []
    statuses = []

    for _, row in df.iterrows():
        grades.append(assign_grade(row['Average_Marks']))
        statuses.append(determine_status(row))

    df['Grade'] = grades
    df['Status'] = statuses
    return df

def get_subject_analysis(df):
    analysis = []
    for sub in SUBJECT_COLUMNS:
        scores = df[sub].to_numpy()
        analysis.append({
            'Subject': sub,
            'Average': np.round(np.mean(scores), 2),
            'Highest': np.max(scores),
            'Lowest': np.min(scores),
            'Standard_Dev': np.round(np.std(scores), 2)
        })
    return pd.DataFrame(analysis)
