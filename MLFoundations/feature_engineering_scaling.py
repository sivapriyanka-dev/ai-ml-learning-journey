# 🧪 Mini Example

# Step 0: Original Data
from sklearn.ensemble import RandomForestClassifier
import numpy as np

X = np.array([[2], [4], [6], [8]])
y = np.array([0, 0, 1, 1])

# Step 1: Add New Feature
# Adds a second column = square of X. X_new = [[2, 4],[4,16],[6,36],[8,64]]
# Now model has 2 features instead of 1
X_new = np.c_[X, X**2]

# Step 2: Train-Test Split
# Training data : X_train = [[2,4], [4,16], [6,36]] and y_train = [0, 0, 1]
# Testing data : X_test = [[8,64]] and y_test = [1] Only 1 test sample (very small dataset ⚠️)
X_train, X_test = X_new[:3], X_new[3:]
y_train, y_test = y[:3], y[3:]

# Step 3: Train Model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Step 4: Test Model
# What happens: Test input = [8, 64] and True label = 1 so Accuracy = 1/1 = 1.0
print(model.score(X_test, y_test))

# Bonus: Check Feature Importance
# Meaning: X → 60% important and X² → 40% important
print(model.feature_importances_)  # [0.6, 0.4]
