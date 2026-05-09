import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
import matplotlib.pyplot as plt
import joblib

# Load dataset
housing = fetch_california_housing(as_frame=True)

# Convert to dataframe
df = housing.frame

print(df.head())
print(df.shape)
print(df.columns)

# Features and target
X = df.drop("MedHouseVal", axis=1)
y = df["MedHouseVal"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Build pipeline
pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("model", RandomForestRegressor(
        n_estimators=100,
        random_state=42
    ))
])

# Train pipeline
pipeline.fit(X_train, y_train)

# Predict
y_pred = pipeline.predict(X_test)

print("Pipeline trained successfully")

# Evaluate model
mae = mean_absolute_error(y_test, y_pred)  # Average absolute mistake
mse = mean_squared_error(y_test, y_pred)  # Squares errors
rmse = mse ** 0.5  # Square root of MSE
r2 = r2_score(y_test, y_pred)  # How well model explains house price variation.

print("MAE:", mae)
print("MSE:", mse)
print("RMSE:", rmse)
print("R2 Score:", r2)

# Feature importance
feature_importance = pipeline.named_steps["model"].feature_importances_

feature_names = X.columns

importance_df = pd.DataFrame({
    "Feature": feature_names,
    "Importance": feature_importance
})

importance_df = importance_df.sort_values(
    by="Importance",
    ascending=False
)

print(importance_df)

# Actual vs Predicted plot
plt.figure(figsize=(8, 6))

plt.scatter(y_test, y_pred, alpha=0.5)

plt.xlabel("Actual House Prices")
plt.ylabel("Predicted House Prices")
plt.title("Actual vs Predicted House Prices")

plt.tight_layout()
plt.show()

# Save trained model
joblib.dump(pipeline, "house_price_model.pkl")

print("Model saved successfully")
