# ✅ Day 28 — Model Tuning & Performance Improvement

# 1. Linear Regression (Improve with Regularization)
# Problem: Overfitting when features are many
# Solution: Use Ridge / Lasso
import numpy as np
from sklearn.linear_model import Ridge
from sklearn.model_selection import GridSearchCV, train_test_split

# Step 1: Create data
X = np.array([[2], [4], [6], [8], [10], [12], [14], [16], [18], [20]])
y = np.array([40, 60, 80, 100, 120, 140, 160, 180, 200, 220])

# Step 2: Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Step 3: Define param grid
param_grid = {
    "alpha": [0.01, 0.1, 1, 10, 100]
}

# Step 4: Apply GridSearch
grid = GridSearchCV(Ridge(), param_grid, cv=3)
grid.fit(X_train, y_train)

print("Best alpha:", grid.best_params_)  # {'alpha': 0.01}
