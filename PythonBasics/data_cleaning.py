# ✅ Day 13: Data Cleaning (Pandas)
# Handle missing values
# Clean incorrect data
# Prepare data for ML


# Why Cleaning?
# Real datasets are never perfect:
# Missing values
# Wrong entries
# Duplicates
# 👉 If not cleaned → ML model gives wrong results

# First I analyze the dataset, then handle missing values appropriately, remove duplicates if present, clean text fields, and ensure correct data types


import pandas as pd
df = pd.read_csv("PythonBasics/CSVFiles/data2.csv")

# # ✅ Step 1: Check Missing Values
# print(df.isnull())  # Shows True/False for missing values
# print(df.isnull().sum())  # Count missing values
# print(df.info())  # Overview of data including null counts

# # ❌ Step 2: Drop Missing Values
# df = df.dropna()  # Drops rows with any missing value

# # ➕ Step 3: Fill Missing Values
# # Fill missing marks with average
# df["marks"].fillna(df["marks"].mean(), inplace=True)

# # 🔁 Step 4: Remove Duplicates
# df = df.drop_duplicates()

# # 🧹 Step 5: Clean Text Data
# df["city"] = df["city"].str.strip()  # Remove extra spaces

# # 🔄 Step 6: Fix Data Types
# df["marks"] = df["marks"].astype(int)

# # Replace wrong values:
# df["city"] = df["city"].replace("Hyd", "Hyderabad")


################################################################
# Best real-world workflow
# 1. Checking missing values (ALWAYS DO ✔️)
# 2 & 3. Drop vs Fill (choose ONE, not both ❗)
# 4. Remove duplicates (DO IF NEEDED ✔️)
# 5. Clean text (GOOD PRACTICE ✔️)
# 6. Fix data types (IMPORTANT ✔️)
# Replace values (USE WHEN REQUIRED ✔️)


df = pd.read_csv("PythonBasics/CSVFiles/data2.csv")

# 1. Understand data
print(df.info())
print(df.isnull().sum())

# 2. Handle missing values
df["marks"] = df["marks"].fillna(df["marks"].mean())

# 3. Clean text
df["city"] = df["city"].str.strip().str.title()

# 3.1 Standardize values (ADD HERE)
df["city"] = df["city"].replace("Hyd", "Hyderabad")

# 4. Remove duplicates
df = df.drop_duplicates()

# 5. Fix data types
df["marks"] = df["marks"].astype(int)

# 6. Save to new file for safe side
df.to_csv("PythonBasics/CSVFiles/cleaned_data.csv", index=False)

print("CSV updated successfully!")
