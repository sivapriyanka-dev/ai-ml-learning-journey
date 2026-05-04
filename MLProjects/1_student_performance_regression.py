# 🚀 Day 24 — End-to-End ML Project
# Project: Student Performance Predictor with Linear Regression
# We’ll do full pipeline: Load → Clean → Features → Train → Evaluate → Predict

# Step 1: Load Data
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pandas as pd

df = pd.read_csv("MLProjects/students.csv")
print(df.head())

# Step 2: Prepare Data - Features (X) and Target (y)
X = df[["hours", "attendance"]]
y = df["marks"]

# Step 3: Train/Test Split - 80% train, 20% test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Step 4: Train Model
# model learns something like: marks = a * hours + b * attendance + c
model = LinearRegression()
model.fit(X_train, y_train)

# Step 5: Evaluate Model - R² score
print(model.score(X_test, y_test))  # 0.7038091847632597

# Step 6: Make Prediction
# Predict marks for: 6 hours study and 80% attendance
print(model.predict([[6, 80]]))  # [69.90566038]

# Step 7: Add Feature Engineering
df["hours_squared"] = df["hours"] ** 2
X = df[["hours", "attendance", "hours_squared"]]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
model = LinearRegression()
model.fit(X_train, y_train)

print(model.score(X_test, y_test))  # 0.689651008332339
# What happens if we add more features?
# It may improve performance if the relationship is non-linear, but with small data it can cause overfitting and reduce generalization. from 70% to 68% in this case. Always evaluate!

# FYI for resolving warnings in console we need to do this: instead of plain - print(model.predict([[6, 80]]))
# new_data = pd.DataFrame([[6, 80]], columns=["hours", "attendance"])
# print(model.predict(new_data))
