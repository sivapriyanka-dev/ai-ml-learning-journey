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

# another example ofloc and iloc

df = pd.DataFrame({
    "name": ["A", "B", "C", "D"],
    "marks": [80, 90, 70, 60],
    "city": ["Hyd", "Chennai", "Hyd", "Mumbai"]
})

# loc (Label-based)
df.loc[1]  # 1. Get one row
df.loc[[0, 2]]  # 2. Get multiple rows
df.loc[:, ["name", "marks"]]  # 3. Get specific columns
df.loc[df["marks"] > 75]  # 4. Filter rows
df.loc[df["marks"] > 75, ["name", "marks"]]  # 5. Filter + select columns
df.loc[df["marks"] < 70, "grade"] = "Fail"  # 6. Update values
df.loc[0:2]  # 7. Slice rows

# .iloc (index-location-based or Position-based)
df.iloc[1]  # 1. Get one row
df.iloc[[0, 2]]  # 2. Get multiple rows
df.iloc[:, [0, 1]]  # 3. Get specific columns
df.iloc[1, 0]  # 4. Row + column
df.iloc[0:2]  # 5. Slice rows

# for df.index = ["a", "b", "c", "d"]
# df.loc["a"]    # ✅ works
# df.iloc[0]     # ✅ works
# df.loc[0]      # ❌ error
# df.iloc["a"]   # ❌ error
