import numpy as np

print("This is my learning from day 8-14 (Week 2)")
print("This is NumPy Learning ➕➖➗✖️")


# 🫡 do => pip install numpy

# GOAL: Learn to use NumPy and Pandas for data manipulation and analysis
# Work with arrays (NumPy)
# Handle datasets (Pandas)
# Do basic data analysis

# ✅ Day 8: Numpy basics 1D array

# marks = np.array([80, 90, 70, 60])
# print(marks)
# print(marks*2)
# print(marks)

# print(np.mean(marks))
# print(np.max(marks))
# print(np.min(marks))
# print(np.sum(marks))

# ✅ Day 9: Numpy basics 2D array
# 2D array (matrix)

arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(arr.shape)  # 2 rows 3 columns => (2,3)

# indexing
print(arr[0, 0])  # 1
print(arr[1, 2])  # 6
print(arr[0])     # first row
print(arr[:, 1])  # second column
print(arr[0, :])  # first row

# Operations
print(arr * 2)
print(np.sum(arr))
print(np.mean(arr))

# Find row-wise and column-wise sum
print(np.sum(arr, axis=1))  # sum along rows [ 6 15]
print(np.sum(arr, axis=0))  # sum along columns [5 7 9]

# practice Create:[[10, 20], [30, 40]]

arr2 = np.array([[10, 20], [30, 40]])
print(arr2.shape)
print(arr2[:, 1])
print(np.sum(arr2))
print(arr2 * 3)
