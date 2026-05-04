# ✅ Day 24 — K-Nearest Neighbors (KNN)

# 👉 SIMPLE EXAMPLE WITH SCALING
# from sklearn.preprocessing import StandardScaler
# from sklearn.neighbors import KNeighborsClassifier
# import numpy as np

# X = np.array([[2], [4], [6], [8]])
# y = np.array([0, 0, 1, 1])

# # Scale data
# scaler = StandardScaler()
# X_scaled = scaler.fit_transform(X)

# model = KNeighborsClassifier(n_neighbors=3, weights='distance')
# model.fit(X_scaled, y)

# # Predict
# test = scaler.transform([[5]])
# print(model.predict(test)) # [0]

# ------------------------------------------------------------------------------------

# 👉 SIMPLE EXAMPLE WITHOUT SCALING
# import numpy as np
# from sklearn.neighbors import KNeighborsClassifier

# X = np.array([[2], [4], [6], [8]])
# y = np.array([0, 0, 1, 1])

# model = KNeighborsClassifier(n_neighbors=3)
# model.fit(X, y)
# print(model.predict([[5]]))  # [0]

# ------------------------------------------------------------------------------------

# 👉 Final Example with and without scaling
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

# ---------------- DATA ----------------
# Features: [Age, Salary]
X = np.array([
    [20, 100000],  # class 0
    [21, 110000],  # class 0
    [22, 120000],  # class 0
    [40, 20000],    # class 1
    [41, 22000],    # class 1
    [42, 24000]     # class 1
])

y = np.array([0, 0, 0, 1, 1, 1])

# Test point (carefully chosen)
test = np.array([[30, 90000]])

# ---------------- WITHOUT SCALING ----------------
model = KNeighborsClassifier(n_neighbors=5)
model.fit(X, y)

pred_without = model.predict(test)
print("Without scaling:", pred_without)

# ---------------- WITH SCALING ----------------
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
test_scaled = scaler.transform(test)

model.fit(X_scaled, y)
pred_with = model.predict(test_scaled)

print("With scaling:", pred_with)
