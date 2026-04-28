# It is Classification Model (predicting categories/classes) - Predicts Categories

import numpy as np
from sklearn.linear_model import LogisticRegression

X = np.array([[2], [4], [6], [8]])
y = np.array([0, 0, 1, 1])

model = LogisticRegression()

model.fit(X, y)

print(model.predict([[5]]))  # output is - [1] Meaning: Pass.

# Probabilities
print(model.predict_proba([[5]]))  # [[0.49999572 0.50000428]]

# Meaning:
# 40% fail
# 60% pass
# Prediction chooses higher probability.
