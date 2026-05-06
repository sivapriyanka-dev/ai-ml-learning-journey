import pandas as pd
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_score, recall_score

# Step 1 Read Dataset
df = pd.read_excel("CustomerChurnPrediction/Telco_customer_churn.xlsx")

# Step 2 Define X and y
# print(df.head())
# from df.columns we Define X and y
X = df.drop("Churn Value", axis=1)  # X = everything other than churn (inputs)
y = df["Churn Value"]  # y = only churn value (output)

# Step 3 Clean and Prepare Data
# Drop columns we don't need and convert text to numbers. Because Churn Reason caused High Cardinality Problem which is Data Leakage
# 1. Not all columns are useful
# 2. Some columns leak future info
# 3. Too many categories → explosion in features
# also Total Charges is treated as TEXT(object) which is wrong. It should be numeric (float)

X = X.drop(columns=[
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

# Convert text to numbers
X["Total Charges"] = pd.to_numeric(X["Total Charges"], errors="coerce")
X = X.fillna(0)
X = pd.get_dummies(X)
# print(X.head())
# print(X.shape) # (7043, 41) → we have 41 features after one-hot encoding

# Step 4 Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

# Step 5 Train First Model (Logistic Regression)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Step 6 Predict
y_pred = model.predict(X_test)

# Step 7 Evaluate
print(accuracy_score(y_test, y_pred))  # 0.7991483321504613

# Till now we did - Data → Cleaning → Encoding → Split → Model → Evaluation

# Step 8 Confusion Matrix
print(confusion_matrix(y_test, y_pred))
# [[914  95] [[TN FP]
#  [188 212]]  [FN TP]]
# 188 FN - customers actually left
# Model said they would stay 😬

# Step 9  Precision & Recall
# 0.6905537459283387 When model says "This customer will churn" It is correct about 68% of the time
print("Precision:", precision_score(y_test, y_pred))
# Of all customers who actually churned, model only caught 53% That means: 47% churn customers were missed
print("Recall:", recall_score(y_test, y_pred))  # 0.53

# Step 10 Hyperparameter Tuning with GridSearchCV
param_grid = {
    "n_estimators": [50, 100],
    "max_depth": [5, 10, None],
    "min_samples_split": [2, 5]
}
grid = GridSearchCV(RandomForestClassifier(random_state=42),
                    param_grid, cv=5, scoring="recall")
grid.fit(X_train, y_train)
# {'max_depth': 10, 'min_samples_split': 2, 'n_estimators': 100}
print("Best parameters:", grid.best_params_)
print("Best score:", grid.best_score_)  # 0.5167026537577488

# Step 11 Train model with best parameters
best_model = grid.best_estimator_

best_pred = best_model.predict(X_test)

print("Tuned Accuracy:", accuracy_score(
    y_test, best_pred))  # 0.8076650106458482
print("Tuned Precision:", precision_score(
    y_test, best_pred))  # 0.6984615384615385
print("Tuned Recall:", recall_score(y_test, best_pred))  # 0.5675
print(confusion_matrix(y_test, best_pred))
# [[911  98]
#  [173 227]]
