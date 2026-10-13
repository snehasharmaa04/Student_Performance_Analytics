# Student_Performance_Analytics
A modular Python based analytics system utilizing Numpy and Pandas to automate student grading, attendance validation, and cohort-level performance reporting.

# Student Performance Analytics System

## 1. Project Title & Details
- *Project Title:* Student Performance Analytics System
- *Technologies:* Python, NumPy, Pandas
- *Submission Date:* October 2026

## 2. Objective
This project automates student performance evaluation in educational settings. It reads raw student examination and attendance records, computes cumulative metrics, enforces academic grading logic, monitors attendance requirements, and generates subject-level and batch-level performance summaries.

## 3. Technologies Used
- *Python 3.x:* Core programming language
- *NumPy:* Vectorized calculations (array-based sum, mean, min, max, standard deviation)
- *Pandas:* Structured tabular manipulation, CSV ingestion, data filtering, and aggregations

## 4. Dataset Description
- *File:* students.csv (20 records)
- *Columns:*
  - StudentID: Unique identifier
  - Name: Full name of student
  - Department: Academic branch
  - Maths, Physics, Computer_Science: Subject scores (out of 100)
  - Attendance: Percentage of class attendance

## 5. Implementation
1. *Data Ingestion:* Reads the CSV using pd.read_csv().
2. *Matrix Calculations:* Converts subject columns into NumPy arrays to evaluate row-wise total and average marks.
3. *Logic Application:* Iterates through records using custom functions to assign letter grades and verify passing criteria (Marks >= 40 across all subjects and Attendance >= 75%).
4. *Subject Analysis:* Uses NumPy array methods to calculate average, minimum, maximum, and standard deviation per subject.
5. *Class Overview:* Ranks students to identify top performers and summarize pass/fail percentages.

## 6. Key Features
- Modular code architecture (main.py and functions.py)
- Vectorized array operations with NumPy
- Conditional rule engine for attendance and individual subject thresholds
- Subject-level statistical distribution breakdown
- Automatic ranking of top academic performers

## 7. Output Summary
The system produces:
- Processed student roster with Total, Average, Grade, and Status
- Cohort statistics (Overall mean, highest/lowest scores, pass percentage)
- Subject-wise breakdown table
- Top 3 student rank table

## 8. Final Outcome
The system successfully processes student performance data without requiring manual effort, providing clean, reproducible academic records.

## 9. Challenges & Learning
- *Vectorization vs Iteration:* Implementing NumPy array operations alongside iterative logic for compound rules.
- *Data Filtering:* Correctly verifying multiple conditions (attendance and individual subject cutoff scores).

## 10. Repository
Complete codebase containing main.py, functions.py, students.csv, and documentation.
