# ✅ Day 17 — Train/Test Split + Evaluation

# Dataset -> Train model -> Test model -> Evaluate

# A model that works on training data alone is not enough. We must test whether it works on new unseen data.

# Why Split Data?
# If you train and test on same data:

# Model may just memorize 😬
# Looks good falsely

# So we split:
# Training Data → Learn pattern
# Test Data → Check performance
# Training Data (80%)
# Testing Data (20%)

# Evaluation -> Difference between prediction and truth.
# If actual: 100
# Predicted: 98
# Error = 2 -> Small error = good.

# Step 1 Imports
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Step 2 Dataset
X = np.array([[2], [4], [6], [8], [10], [12]])
y = np.array([40, 60, 80, 100, 120, 140])

# Step 3 Split Data -> test_size=0.2 → 20% for testing and random_state=42 → same split every run
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,  # test_size=1.0 is not allowed. 100% data goes to test model has nothing to learn from
    random_state=42  # This Seed can be any integer. It only controls repeatable randomness
)

# Step 4 Train
model = LinearRegression()
model.fit(X_train, y_train)

# Step 5 Test Predictions -> Compare predicted vs actual.
predictions = model.predict(X_test)

print(predictions)  # predicted values (sometimes predicted [99.5, 139.8])
print(y_test)  # actual values (sometimes actual [100, 140])

# Use Score (Easy Version)
# score() is an additional evaluation step not any replacement
print(model.score(X_test, y_test))
# This is R² score.
# Close to 1 → very good
# 0.95 → very good
# Close to 0 → poor
# negative → really bad

# See how data split works.
print(X_train)
print(X_test)

# Check model score:
print(model.score(X_test, y_test))

# predict
print(model.predict([[7]]))
