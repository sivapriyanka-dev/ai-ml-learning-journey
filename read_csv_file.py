import pandas as pd

# ✅ Day 11: Reading CSV Files
# CSV = Comma Separated Values

df = pd.read_csv("data.csv")
print(df)  # prints all data
print(df.head())  # first 5 rows
print(df.tail())  # last rows
print(df.columns)  # columns
print(df.shape)  # shape (rows, columns) eg - (100, 3) → 100 rows, 3 columns


# Select Data

print(df["marks"])  # select marks column
print(df[df["marks"] > 80])  # filter
print(df["marks"].mean())
print(df[df["city"] == "Pune"])  # Students from Pune

# Add Pass Column
df["pass"] = df["marks"] >= 50
print(df)
print(df[df["marks"] == df["marks"].max()])  # topper student

print('--------------------------------------------------------')


# ✅ Day 12: Data Analysis with Pandas
# NOTE: EDA (Exploratory Data Analysis)
# In ML workflow: Dataset → Analysis → Cleaning → Model

# 1. Basic Analysis
print(df["marks"].mean())   # average
print(df["marks"].max())    # highest
print(df["marks"].min())    # lowest

# 2. Describe
print(df.describe())  # Gives: mean, min, max, count, std (spread)

# 3. Filtering Data
print(df[df["marks"] > 80])  # Students with marks > 80
print(df[df["marks"] < 50])  # Failed students

# 4. Group By - Analyze by category (city)
print(df.groupby("city")["marks"].mean())  # Avg marks per city

# 5. Count by Category
print(df["city"].value_counts())  # How many students per city
print(df.groupby("city").size())  # Same as above

# 6. Add New Column (Derived Data)
# df["marks"] → takes the marks column
# .apply(...) → applies a function to each value in marks
# lambda x: → a short function where x is each student's marks
df["grade"] = df["marks"].apply(
    lambda x: "A" if x >= 90 else "B" if x >= 75 else "C" if x >= 50 else "Fail"
)
print(df)

# 7. Count how many passed vs failed
df["pass"] = df["marks"].apply(lambda x: "Pass" if x >= 50 else "Fail")
print(df["pass"].value_counts())
