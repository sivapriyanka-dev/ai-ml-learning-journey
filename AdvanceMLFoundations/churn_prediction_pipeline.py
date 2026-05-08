import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    precision_score,
    recall_score,
    classification_report
)
import joblib

# STEP 1 — LOAD DATASET
# ======================================================
df = pd.read_excel("AdvanceMLFoundations/Telco_customer_churn.xlsx")
print("Dataset Loaded Successfully\n")

# STEP 2 — DROP LEAKAGE / UNNECESSARY COLUMNS
# ======================================================
df = df.drop(columns=[
    "Churn Reason",
    "Churn Label",
    "Churn Score",
    "CLTV",
    "CustomerID",
    "Count",
    "Country",
    "State",
    "City",
    "Zip Code",
    "Lat Long",
    "Latitude",
    "Longitude"
])

# STEP 3 — FIX DATA TYPES
# ======================================================
# Convert Total Charges to numeric
df["Total Charges"] = pd.to_numeric(
    df["Total Charges"],
    errors="coerce"
)

# STEP 4 — DEFINE FEATURES + TARGET
# ======================================================
X = df.drop("Churn Value", axis=1)
y = df["Churn Value"]

# STEP 5 — IDENTIFY COLUMN TYPES
# ======================================================
numeric_features = [
    "Tenure Months",
    "Monthly Charges",
    "Total Charges"
]

categorical_features = X.select_dtypes(
    include=["object"]
).columns.tolist()

print("Numerical Features:")
print(numeric_features)

print("\nCategorical Features:")
print(categorical_features)

# STEP 6 — NUMERICAL PIPELINE
# ======================================================
numeric_transformer = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler())
])

# STEP 7 — CATEGORICAL PIPELINE
# ======================================================
categorical_transformer = Pipeline([
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("encoder", OneHotEncoder(handle_unknown="ignore"))
])

# STEP 8 — COMBINE PREPROCESSING
# ======================================================
preprocessor = ColumnTransformer([
    ("num", numeric_transformer, numeric_features),
    ("cat", categorical_transformer, categorical_features)
])

# STEP 9 — CREATE FULL PIPELINE
# ======================================================
pipeline = Pipeline([
    ("preprocessor", preprocessor),
    ("model", LogisticRegression(max_iter=1000))
])

# STEP 10 — TRAIN TEST SPLIT
# ======================================================
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# STEP 11 — TRAIN MODEL
# ======================================================
pipeline.fit(X_train, y_train)
print("\nModel Training Completed")

# STEP 12 — PREDICTIONS
# ======================================================
y_pred = pipeline.predict(X_test)

# STEP 13 — EVALUATION
# ======================================================
print("\n================ MODEL EVALUATION ================\n")

print("Accuracy:")
print(accuracy_score(y_test, y_pred))

print("\nPrecision:")
print(precision_score(y_test, y_pred))

print("\nRecall:")
print(recall_score(y_test, y_pred))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# STEP 14 — HYPERPARAMETER TUNING
# ======================================================
param_grid = {
    "model__C": [0.01, 0.1, 1, 10, 100]
}

grid = GridSearchCV(
    pipeline,
    param_grid,
    cv=3,
    scoring="recall"
)
grid.fit(X_train, y_train)
print("\n================ GRID SEARCH RESULTS ================\n")

print("Best Parameters:")
print(grid.best_params_)

print("\nBest Cross Validation Recall:")
print(grid.best_score_)

# STEP 15 — BEST MODEL EVALUATION
# ======================================================
best_model = grid.best_estimator_
best_predictions = best_model.predict(X_test)
print("\n================ BEST MODEL RESULTS ================\n")

print("Accuracy:")
print(accuracy_score(y_test, best_predictions))

print("\nPrecision:")
print(precision_score(y_test, best_predictions))

print("\nRecall:")
print(recall_score(y_test, best_predictions))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, best_predictions))

# STEP 16 — SAVE FULL PIPELINE
# ======================================================
joblib.dump(best_model, "churn_pipeline.pkl")
print("\nPipeline Saved Successfully")

# STEP 17 — TEST WITH NEW CUSTOMER
# ======================================================
new_customer = pd.DataFrame({
    "Gender": ["Female"],
    "Senior Citizen": [0],
    "Partner": ["Yes"],
    "Dependents": ["No"],
    "Tenure Months": [12],
    "Phone Service": ["Yes"],
    "Multiple Lines": ["No"],
    "Internet Service": ["Fiber optic"],
    "Online Security": ["No"],
    "Online Backup": ["Yes"],
    "Device Protection": ["No"],
    "Tech Support": ["No"],
    "Streaming TV": ["Yes"],
    "Streaming Movies": ["Yes"],
    "Contract": ["Month-to-month"],
    "Paperless Billing": ["Yes"],
    "Payment Method": ["Electronic check"],
    "Monthly Charges": [85.5],
    "Total Charges": [1025.0]
})

prediction = best_model.predict(new_customer)
print("\n================ NEW CUSTOMER PREDICTION ================\n")

if prediction[0] == 1:
    print("Customer Will Churn")
else:
    print("Customer Will Stay")
