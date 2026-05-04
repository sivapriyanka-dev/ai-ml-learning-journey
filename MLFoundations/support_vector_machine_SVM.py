# ✅ Day 26 — Support Vector Machine (SVM)
import numpy as np
from sklearn.svm import SVC

X = np.array([[1], [2], [3], [7], [8], [9]])
y = np.array([0, 1, 0, 1, 0, 1])  # non-linear pattern

# Linear SVM
model = SVC(kernel="linear")
model.fit(X, y)
print("Linear:", model.predict([[5]]))  # [1]

# RBF SVM
model = SVC(kernel="rbf", gamma=1)
model.fit(X, y)
print("RBF:", model.predict([[5]]))  # [0]
