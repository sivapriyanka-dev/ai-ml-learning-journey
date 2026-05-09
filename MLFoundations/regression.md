# Day 32 Regression

Regression is a type of supervised learning where the goal is to predict a continuous value based on input features. It is used when the output variable is a real number, such as price, temperature, or salary.

Predict continuous values:

House Price → ₹45,00,000
Salary → ₹12,50,000
Temperature → 32.5°C

Output is a number.

# Regression Metrics

To evaluate the performance of a regression model, we use various metrics:

1. Mean Absolute Error (MAE): The average absolute difference between the predicted and actual values.
2. Mean Squared Error (MSE): The average squared difference between the predicted and actual values.
3. R² Score: The proportion of the variance in the dependent variable that is predictable from the independent variables.
   R² Score = 1 - (SS_res / SS_tot)
   Where:
   SS_res = Σ(y_true - y_pred)²
   SS_tot = Σ(y_true - y_mean)²
   R² Score ranges from 0 to 1, where 1 indicates perfect prediction and 0 indicates that the model does not explain any of the variance in the target variable.

# Linear Regression

Linear Regression is a simple algorithm that models the relationship between a dependent variable and one or more independent variables by fitting a linear equation to observed data.
The equation of a linear regression model is:
y = β₀ + β₁x₁ + β₂x₂ + ... + βₙxₙ + ε
Where:
y = dependent variable (target)
x₁, x₂, ..., xₙ = independent variables (features)
β₀ = intercept
β₁, β₂, ..., βₙ = coefficients
ε = error term
The goal of linear regression is to find the best-fitting line that minimizes the sum of the squared differences between the observed and predicted values. This is typically done using the Ordinary Least Squares (OLS) method.

# MAE — Mean Absolute Error

Average prediction error.

Example:
Actual = 500000
Predicted = 450000
Error = 50000

Interpretation: “On average, model misses by ₹50,000”

# MSE — Mean Squared Error

Squares errors before averaging. Punishes big mistakes harder.
RMSE — Root Mean Squared Error - Same units as target. Easy to explain.
Example: Model is off by ₹65,000 on average

# R² Score

How much variance model explains.

Range:
1.0 → perfect
0.8 → very good
0.5 → okay
0 → useless

# Example:

Actual house prices: [5.0, 3.0, 8.0]
Meaning: $500k, $300k, $800k

Your model predicted: [4.5, 2.0, 7.0]
Meaning: $450k, $200k, $700k

Errors:
5.0 - 4.5 = 0.5
3.0 - 2.0 = 1.0
8.0 - 7.0 = 1.0

So mistakes are: [0.5, 1.0, 1.0]

1. MAE (Mean Absolute Error) : Average mistake
   On average, how much is my model wrong?
   Take Errors [0.5, 1.0, 1.0]
   then Average: (0.5 + 1 + 1) / 3 = 0.83
   so MAE = 0.83
   means On average, prediction is off by $83,000

2. MSE (Mean Squared Error) - Huge mistake gets punished hard.
   Take Errors [0.5, 1.0, 1.0]
   square them
   0.5² = 0.25
   1² = 1
   1² = 1
   now result is [0.25, 1, 1]
   then Average: (0.25 + 1 + 1)/3 = 0.75
   so MSE = 0.75
   Why square? Because big mistakes should hurt more.
   Huge mistake gets punished hard.

3. RMSE (Root Mean Squared Error) - Much easier to understand.
   Problem with MSE, Units become weird. for Eg price unit = dollars then dollars² which is Not intuitive.
   So take square root:
   if MSE = 0.75 then sqrt(0.75) = 0.866
   RMSE = 0.866 means Typical prediction error ≈ $86,600

4. R² Score
   This asks How much of the price variation did my model explain?
   R² = 1.0 Perfect. Predictions exactly match actual values.
   R² = 0.8 Very good. Model explains 80% of variation.
   R² = 0.5 Decent. Half the behavior understood.
   R² = 0 Model useless. No better than random average guessing.

✅ MAE → business explanation
✅ RMSE → technical comparison
✅ R² → model quality summary
