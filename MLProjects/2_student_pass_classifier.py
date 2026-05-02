# Project: Student pass/fail Predictor with Random Forest Classifier

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Load data
df = pd.read_csv("MLProjects/students.csv")

# Create target (pass/fail)
df["pass"] = df["marks"] >= 50

# Features & target
X = df[["hours", "attendance"]]
y = df["pass"]

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Evaluate
print("Accuracy:", model.score(X_test, y_test))  # Accuracy: 0.5

# Predictions
print(model.predict([[6, 80]]))  # Prediction (6,80): [ True]
print(model.predict([[4, 60]]))  # Prediction (4,60): [False]
print(model.predict([[9, 90]]))  # Prediction (9,90): [ True]
