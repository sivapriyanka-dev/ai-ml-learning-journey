import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt

from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import (
    train_test_split,
    cross_val_score
)
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.ensemble import (
    RandomForestRegressor,
    GradientBoostingRegressor
)
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

# ======================================================
# STEP 1 — LOAD DATA
# ======================================================
housing = fetch_california_housing(as_frame=True)
df = housing.frame

print("Dataset Loaded Successfully")
print(df.shape)

# ======================================================
# STEP 2 — FEATURE ENGINEERING
# ======================================================

# Outlier handling
df["AveRooms"] = df["AveRooms"].clip(upper=20)
df["AveOccup"] = df["AveOccup"].clip(upper=20)
df["Population"] = df["Population"].clip(upper=10000)

# Log transforms
df["MedInc_log"] = np.log1p(df["MedInc"])
df["Population_log"] = np.log1p(df["Population"])
df["AveRooms_log"] = np.log1p(df["AveRooms"])
df["AveOccup_log"] = np.log1p(df["AveOccup"])

# Ratio features
df["RoomsPerBedroom"] = df["AveRooms"] / df["AveBedrms"]
df["PopulationPerOccup"] = df["Population"] / df["AveOccup"]

print("Feature Engineering Completed")

# ======================================================
# STEP 3 — FEATURES & TARGET
# ======================================================
X = df.drop("MedHouseVal", axis=1)
y = df["MedHouseVal"]

# ======================================================
# STEP 4 — TRAIN TEST SPLIT
# ======================================================
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# ======================================================
# STEP 5 — RANDOM FOREST PIPELINE
# ======================================================
rf_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("model", RandomForestRegressor(
        n_estimators=200,
        random_state=42,
        n_jobs=-1
    ))
])

# Cross validation
rf_cv_scores = cross_val_score(
    rf_pipeline,
    X_train,
    y_train,
    cv=5,
    scoring="r2"
)

print("\n================ RANDOM FOREST CV RESULTS ================\n")
print("R2 Scores:", rf_cv_scores)
print("Average R2:", rf_cv_scores.mean())

# Train
rf_pipeline.fit(X_train, y_train)

# Predict
rf_pred = rf_pipeline.predict(X_test)

# Evaluate
rf_mae = mean_absolute_error(y_test, rf_pred)
rf_mse = mean_squared_error(y_test, rf_pred)
rf_rmse = np.sqrt(rf_mse)
rf_r2 = r2_score(y_test, rf_pred)

print("\n================ RANDOM FOREST RESULTS ================\n")
print("MAE:", rf_mae)
print("RMSE:", rf_rmse)
print("R2 Score:", rf_r2)

# ======================================================
# STEP 6 — GRADIENT BOOSTING PIPELINE
# ======================================================
gb_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("model", GradientBoostingRegressor(
        n_estimators=200,
        learning_rate=0.05,
        max_depth=4,
        random_state=42
    ))
])

# Cross validation
gb_cv_scores = cross_val_score(
    gb_pipeline,
    X_train,
    y_train,
    cv=5,
    scoring="r2"
)

print("\n================ GRADIENT BOOSTING CV RESULTS ================\n")
print("R2 Scores:", gb_cv_scores)
print("Average R2:", gb_cv_scores.mean())

# Train
gb_pipeline.fit(X_train, y_train)

# Predict
gb_pred = gb_pipeline.predict(X_test)

# Evaluate
gb_mae = mean_absolute_error(y_test, gb_pred)
gb_mse = mean_squared_error(y_test, gb_pred)
gb_rmse = np.sqrt(gb_mse)
gb_r2 = r2_score(y_test, gb_pred)

print("\n================ GRADIENT BOOSTING RESULTS ================\n")
print("MAE:", gb_mae)
print("RMSE:", gb_rmse)
print("R2 Score:", gb_r2)

# ======================================================
# STEP 7 — FEATURE IMPORTANCE (BEST MODEL)
# ======================================================
best_model = gb_pipeline

feature_importance = best_model.named_steps["model"].feature_importances_

importance_df = pd.DataFrame({
    "Feature": X.columns,
    "Importance": feature_importance
}).sort_values(by="Importance", ascending=False)

print("\n================ FEATURE IMPORTANCE ================\n")
print(importance_df)

# ======================================================
# STEP 8 — VISUALIZATION
# ======================================================
plt.figure(figsize=(8, 6))
plt.scatter(y_test, gb_pred, alpha=0.4)

plt.xlabel("Actual House Prices")
plt.ylabel("Predicted House Prices")
plt.title("Gradient Boosting: Actual vs Predicted")

plt.tight_layout()
plt.show()

# ======================================================
# STEP 9 — SAVE BEST MODEL
# ======================================================
joblib.dump(best_model, "house_price_model_v2.pkl")

print("\nBest Model Saved Successfully")

# ======================================================
# STEP 10 — SAMPLE PREDICTION
# ======================================================
sample_house = pd.DataFrame({
    "MedInc": [5.0],
    "HouseAge": [20],
    "AveRooms": [6.0],
    "AveBedrms": [1.2],
    "Population": [1500],
    "AveOccup": [3.0],
    "Latitude": [34.05],
    "Longitude": [-118.25],
    "MedInc_log": [np.log1p(5.0)],
    "Population_log": [np.log1p(1500)],
    "AveRooms_log": [np.log1p(6.0)],
    "AveOccup_log": [np.log1p(3.0)],
    "RoomsPerBedroom": [6.0 / 1.2],
    "PopulationPerOccup": [1500 / 3.0]
})

prediction = best_model.predict(sample_house)

print("\nSample House Predicted Price:", prediction[0])
