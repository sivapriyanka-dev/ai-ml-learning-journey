# ✅ Day 15 — What is Machine Learning?

Rules + Data → Output
Instead of hardcoding rules, the system learns patterns.

Example:
You manually code: If marks > 50 → pass
Machine Learning: Data + Outputs → Model learns Rules

Example - Dataset:

| Hours Studied | Marks |
| ------------- | ----- |
| 2             | 40    |
| 4             | 60    |
| 6             | 80    |

Model learns: More study hours → higher marks
Then predicts for 5 hours. That prediction is ML.

# Machine Learning = Teaching computers to learn patterns from data and make predictions.

---

# Types of ML

1. Supervised Learning
   Has inputs + correct answers (labels)

   Example:
   House size → price
   Study hours → marks

   We know target answer.

2. Unsupervised Learning
   No labels. Model finds patterns itself.

   Example:
   Group similar customers

3. Reinforcement Learning
   Learn by rewards/penalties.

   Example:
   Chess AI
   Self-driving decisions

---

Scikit-learn (written as sklearn in Python) is one of the most popular Machine Learning libraries in Python.

Think of it as a toolbox full of ready-made ML algorithms.

=> pip install scikit-learn

1. Train Machine Learning Models -> from sklearn.linear_model import LinearRegression
2. Split Data into Train/Test -> from sklearn.model_selection import train_test_split -> X_train, X_test, y_train, y_test = train_test_split(X, y)
3. Evaluate Models -> from sklearn.metrics import accuracy_score
4. Data Preprocessing -> from sklearn.preprocessing import StandardScaler

---

# First Model - Linear Regression

Used when predicting numbers.

Examples:
Salary prediction
House prices
Marks prediction

# Core Idea: y = mx + b

Where:
x = input
y = prediction
m = slope
b = intercept

Example
If model learns: marks=10(hours)+20
Study 5 hours: 10(5)+20=70
Predicted marks = 70

Creating Linear Regression Model in linear_regression_model.py
using
=> import sklearn
=> from sklearn.linear_model import LinearRegression

# ✅ Day 23 — Feature Engineering + Model Improvement

👉 Feature = input variable. for example in this
| Hours | Attendance | Marks |
| ----- | ---------- | ----- |
| 5 | 80 | 70 |

Hours → feature
Attendance → feature
Marks → target

Feature Engineering - Creating better input features to improve model

Example
Original: hours = [2,4,6]
New feature: hours_squared = [4,16,36]
👉 This helps model learn non-linear patterns

Why? - Sometimes model can't learn pattern with raw data. Better features → better predictions.

Feature Importance (Random Forest) - model.feature_importances - Shows which feature matters most.

- Scaling - Different features have different ranges:

| Feature | Range           |
| ------- | --------------- |
| Hours   | 1–10            |
| Salary  | 10,000–1,00,000 |

Big numbers dominate model 😬
Solution: Scaling - Makes values comparable

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

small example where X alone fails But X² makes model succeed
| X | y |
| -2 | 1 |
| -1 | 0 |
| 1 | 0 |
| 2 | 1 |
👉 Pattern:
Ends → 1
Middle → 0
This is a curve pattern, not a straight line.

Try with ONLY X
😬 What happens:
Model tries to draw a straight line
But your data is shaped like a U
👉 Result: Poor accuracy (often ~0.5)

Add X² feature
now data looks like
| X | X² | y |
| -2 | 4 | 1 |
| -1 | 1 | 0 |
| 1 | 1 | 0 |
| 2 | 4 | 1 |
MAGIC Pattern:
Now the pattern depends on X²
Small X² → 0
Large X² → 1
👉 Result: Accuracy becomes 1.0

Note: Instead of Feeding raw data blindly You Transform data into something the model can understand
| Situation | Model |
| ---------------- | ----------------------------------------- |
| Straight pattern | Any model works |
| Curved pattern | Need feature engineering OR complex model |
