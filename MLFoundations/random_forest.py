import numpy as np
from sklearn.ensemble import RandomForestClassifier

X = np.array([[2], [4], [6], [8]])
y = np.array([0, 0, 1, 1])

# n_estimators=10 means 10 trees
model = RandomForestClassifier(n_estimators=10)

model.fit(X, y)

print(model.predict([[5]]))  # [0]

# Feature Importance: Tells which input matters most
print(model.feature_importances_)  # [1.]
