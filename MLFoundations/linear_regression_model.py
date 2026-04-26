import numpy as np
from sklearn.linear_model import LinearRegression

X = np.array([[2], [4], [6], [8]])
y = np.array([40, 60, 80, 100])

model = LinearRegression()

model.fit(X, y)

print(model.predict([[3]]))

# How we did?
# Step 1: Inputs (Features)
# X = np.array([[2],[4],[6],[8]])
# Why double brackets? Because scikit-learn expects rows like: [[feature1],[feature2]]

# Step 2: Outputs (Target)
# y = np.array([40,60,80,100])

# Step 3: Create Model
# model = LinearRegression()

# Step 4: Train Model
# model.fit(X,y) -> This is where learning happens.

# Step 5: Predict
# prediction = model.predict([[5]])
# print(prediction)

# Model learned a line roughly, Then used it for prediction: y = 10x + 20 (y = mx + b)

print(model.coef_)  # gives the slope (m) - or - slope => [10.]
print(model.intercept_)  # gives the intercept (b) - or - starting point => 20.0
