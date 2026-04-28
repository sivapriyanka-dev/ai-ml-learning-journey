# ✅ Day 20 — Classification Evaluation

import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.metrics import precision_score, recall_score

X = np.array([[2], [4], [6], [8]])
y = np.array([0, 0, 1, 1])

model = LogisticRegression()
model.fit(X, y)

y_pred = model.predict(X)   # predictions on known data

print(y_pred)  # [0 0 1 1]

print(accuracy_score(y, y_pred))  # 1.0
print(confusion_matrix(y, y_pred))  # [[2 0][0 2]]
print(precision_score(y, y_pred))  # 1.0
print(recall_score(y, y_pred))  # 1.0
