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
# 1. Basic Analysis
print(df["marks"].mean())   # average
print(df["marks"].max())    # highest
print(df["marks"].min())    # lowest

# 2. Describe
print(df.describe())  # Gives: mean, min, max, count, std (spread)
