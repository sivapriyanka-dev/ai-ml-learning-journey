print("Hello, World! I am learning AI - ML")

print("This is my learning from day 1-7 (Week 1)")
print("Starting with basics of Python, I have learned about variables, data types, input/output, loops, conditions, functions, dictionaries, file handling and a mini project on student marks analysis.")

# ✅ Day 1: Python Basics
# Variables → store values
# Data types → int, float, str, bool
# Input → input()
# Output → print()
# Basic operations → + - * /

name = "Priyanka"
age = 25
print("My name is", name)
print("Age:", age)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Sum is:", a + b)

# ✅ Day 2: Lists & Loops
# Lists, for loop, while loop

nums = [1, 2, 3, 4, 5]
for n in nums:
    print(n * n)
marks = [80, 90, 75, 60, 85]

# ✅ Day 3: Conditions
# if, elif, else
# Logical operators (and, or, not)

num = 10
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# ✅ Day 4: Functions

# eg 1


def square(x):
    return x * x


print(square(5))

# eg 2


def add(a, b):
    return a + b


result = add(2, 3)
print(result)

# ✅ Day 5: Dictionaries & Strings
# These are basically object key value pair. We can store data in key value pair and we can access the data using key.

person = {"name": "Priya", "age": 25}
print(person["name"])

# Looping through dictionary
for key, value in person.items():
    print(key, value)

# ✅ Day 6: File Handling

# write
# with open("file.txt", "w") as f:
#     f.write("Hello AI")

# read
# with open("test.txt", "r") as f:
#     data = f.read()
# print(data)

# Read Line by Line
# with open("test.txt", "r") as f:
#     for line in f:
#         print(line.strip())


# ✅ Day 7: Mini Project - Student Marks Analysis

# average
def get_average(marks):
    return sum(marks) / len(marks)

# highest


def get_max(marks):
    max_val = marks[0]
    for m in marks:
        if m > max_val:
            max_val = m
            return max_val


print(max(marks))

print("Average marks:", get_average(marks))
print("Highest marks:", get_max(marks))
