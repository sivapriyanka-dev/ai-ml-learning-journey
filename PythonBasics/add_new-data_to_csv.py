# In this we are adding new data to an existing CSV file using pandas. We read the existing CSV file into a DataFrame, create a new row of data as a dictionary, append it to the DataFrame, and then save the updated DataFrame back to the CSV file without the index.

# This is Day 12 workflow, where we are doing data analysis with pandas. We perform basic analysis like filtering data, group by category, count by category, and add a new column based on conditions.

import pandas as pd

df = pd.read_csv("PythonBasics/CSVFiles/data2.csv")

# ✅ 1. Add a new row (most common)
# step 1 - new row
new_data = {"name": "Y", "marks": 85, "age": 22, "city": "pune"}

# step 2 - append row
df.loc[len(df)] = new_data

# step 3 - save back to CSV
df.to_csv("PythonBasics/CSVFiles/data2.csv", index=False)

# ✅ 2. Add multiple rows
new_rows = pd.DataFrame([
    {"name": "E", "marks": 60, "age": 20, "city": "Delhi"},
    {"name": "F", "marks": 95, "age": 23, "city": "Kerala"}
])
df = pd.concat([df, new_rows], ignore_index=True)
df.to_csv("PythonBasics/CSVFiles/data2.csv", index=False)

# ✅ 3. Add a new column
df["grade"] = df["marks"].apply(
    lambda x: "A" if x >= 90 else "B" if x >= 75 else "C" if x >= 50 else "Fail"
)
df.to_csv("PythonBasics/CSVFiles/data2.csv", index=False)


# ⚠️ Important thing to remember
# to_csv() overwrites the file by default
# If you want to append without deleting old data, use:
df.to_csv("PythonBasics/CSVFiles/data2.csv",
          mode="a", header=False, index=False)
# mode="a" → append mode
# header=False → don't write column names again
