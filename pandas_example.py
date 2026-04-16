import pandas as pd

print("This is my learning from day 8-14 (Week 2)")
print("This is Pandas Learning 🐼🐼🐼")

# 👉 Pandas = tool to work with datasets (tables)

# 🫡 do => pip install pandas

# ✅ Day 10: Pandas basics

data = {
    "name": ["A", "B", "C"],
    "marks": [80, 90, 70]
}

df = pd.DataFrame(data)
# print(df)
print(df["marks"])
print(df.iloc[0])
print(df.iloc[2])
print(df.head())   # first rows
print(df.columns)  # column names
print(df.shape)    # (rows, columns)
print(df["marks"].mean())
print(df["marks"].max())
print(df["marks"].min())
print(df[df["marks"] > 70])  # Filter students with marks > 70

# Add new column
df["grade"] = ["C", "B", "A"]
print(df)

# Practice
# data2 = {
#     "name": ["A", "B", "C"],
#     "marks": [60, 75, 90]
# }

# df2 = pd.DataFrame(data2)
# print(df2.iloc[0])
