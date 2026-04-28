# ✅ Day 21 — Decision Trees - Predicts Rule-based categories

import numpy as np
from sklearn.tree import DecisionTreeClassifier

# Dataset: Let's use: X as Study hour and y as Pass/Fail
X = np.array([[2], [4], [6], [8]])
y = np.array([0, 0, 1, 1])

# Train Model
model = DecisionTreeClassifier()

model.fit(X, y)

# Predict
# Natural split is midpoint: (4+6)/2=5 And many tree algorithms choose such thresholds.
print(model.predict([[5]]))  # [0] Because 5 falls into <= 5 threshold
print(model.predict([[5.1]]))  # [1] now it crosses threshold
print(model.predict([[3]]))  # [0]
print(model.predict([[7]]))  # [1]

# model = DecisionTreeClassifier(max_depth=2) Limits complexity.
