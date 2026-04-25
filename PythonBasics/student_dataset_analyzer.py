# ✅ Day 14: Mini Project: Student Dataset Analyzer
# Use Pandas to analyze a real dataset end-to-end:
# Load data
# Analyze
# Clean
# Extract insights

# Step 1: Load Dataset
import pandas as pd

df = pd.read_csv("PythonBasics/CSVFiles/students.csv")
print(df.head())

# Step 2: Basic Analysis
print("Average Marks:", df["marks"].mean())
print("Highest Marks:", df["marks"].max())
print("Lowest Marks:", df["marks"].min())

# Step 3: Find Topper
print(df[df["marks"] == df["marks"].max()])

# Step 4: Failed Students
print(df[df["marks"] < 50])

# Step 5: Average Marks by City
print(df.groupby("city")["marks"].mean())

# Step 6: Add Grades
df["grade"] = df["marks"].apply(
    lambda x: "A" if x >= 90 else
    "B" if x >= 75 else
    "C" if x >= 50 else
    "Fail"
)
print(df)
# Save updated DataFrame for Grades to CSV
# df.to_csv("PythonBasics/CSVFiles/students_updated.csv", index=False)

# Step 7: Pass/Fail Count
df["pass"] = df["marks"] >= 50
print(df["pass"].value_counts())

# Find topper city
topper_city = df[df["marks"] == df["marks"].max()]["city"].values[0]
print("Topper City:", topper_city)

# Find city with highest average marks
highest_avg_city = df.groupby("city")["marks"].mean().idxmax()
print("City with Highest Average Marks:", highest_avg_city)

# Filter only grade A students
grade_a_students = df[df["grade"] == "A"]
print("Grade A Students:", grade_a_students)
