# ✅ Day 27 — Naive Bayes

import numpy as np
from sklearn.naive_bayes import GaussianNB

X = np.array([[2], [4], [6], [8]])
y = np.array([0, 0, 1, 1])

model = GaussianNB()

model.fit(X, y)

print(model.predict([[5]]))  # [0]
print(model.predict([[3]]))  # [0]
print(model.predict([[7]]))  # [1]
