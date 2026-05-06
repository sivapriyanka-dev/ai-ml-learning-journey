import pandas as pd
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_score, recall_score
from sklearn.preprocessing import StandardScaler

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

# scaling is not necessary for tree-based models like Random Forest, but it is important for Logistic Regression. So we will scale the features before training the Logistic Regression model.
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Step 4 Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y,
    test_size=0.2,
    random_state=42
)

# Step 5 Train First Model (Logistic Regression)
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Step 6 Predict
y_pred = model.predict(X_test)

# Step 7 Evaluate
print(accuracy_score(y_test, y_pred))  # 0.8035714285714286

# Till now we did - Data → Cleaning → Encoding → Split → Model → Evaluation

# Step 8 Confusion Matrix
print(confusion_matrix(y_test, y_pred))
# [[900 109] [[TN FP]
#  [169 231]]  [FN TP]]
# 169 FN - customers actually left
# Model said they would stay 😬

# Step 9  Precision & Recall
# 0.6794117647058824 When model says "This customer will churn" It is correct about 68% of the time
print("Precision:", precision_score(y_test, y_pred))
# Of all customers who actually churned, model only caught 57% That means: 43% churn customers were missed
print("Recall:", recall_score(y_test, y_pred))  # 0.5775

# Step 10 Hyperparameter Tuning with GridSearchCV
param_grid = {
    "C": [0.01, 0.1, 1, 10, 100]
}
grid = GridSearchCV(LogisticRegression(max_iter=1000),
                    param_grid, cv=3, scoring="recall")
grid.fit(X_train, y_train)
print("Best C:", grid.best_params_)  # {'C': 100}
print("Best score:", grid.best_score_)  # 0.5752

# Step 11 Train model with best parameters
best_model = LogisticRegression(C=0.01, max_iter=1000)
best_model.fit(X_train, y_train)
y_pred_best = best_model.predict(X_test)
print("Best model accuracy:", accuracy_score(
    y_test, y_pred_best))  # 0.8005677785663591
print("Best model precision:", precision_score(
    y_test, y_pred_best))  # 0.6808510638297872
print("Best model recall:", recall_score(y_test, y_pred_best))  # 0.56
print("Best model confusion matrix:")
print(confusion_matrix(y_test, y_pred_best))
# [[904 105] [[TN FP]
#  [176 224]]  [FN TP]]

# Feature Importance / Coefficients
coefficients = pd.DataFrame({
    "Feature": X.columns,
    "Coefficient": best_model.coef_[0]
})

print(
    coefficients
    .sort_values(by="Coefficient", ascending=False)
    .head(10)
)
