# 🚀 Day 29 — Feature Engineering + Pipelines

## Feature Engineering

Feature engineering means transforming raw data into a format ML models can learn from better. For Example
| Age | Salary | City | Bought Product |
| --- | ------ | --------- | -------------- |
| 25 | 50000 | Hyderabad | Yes |
| 40 | 120000 | Chennai | No |

Features here: Age, Salary, City
Target: Bought Product

But ML models cannot directly understand text like "Hyderabad". And models can behave badly if numbers are on very different scales. So we preprocess the data.

# Why Preprocessing Matters

Real-world data is messy.

- Problems include:
  missing values
  text categories
  different scales
  irrelevant columns
  inconsistent formatting

- Without preprocessing:
  models become inaccurate
  training becomes unstable
  results become misleading

Part 1 — Handling Categorical Data
Models understand numbers, not text. We must convert text → numbers.

Difference Between Encoding Methods:
| Method | Use Case |
| ---------------- | -------------------- |
| Label Encoding | Ordered categories |
| One Hot Encoding | Unordered categories |

- **Label Encoding**: Used when categories have order. Like
  Small = 0
  Medium = 1
  Large = 2

Code: from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
df["Gender"] = le.fit_transform(df["Gender"])

- **One-Hot Encoding**: Used for categorical columns without order. Creates binary columns for each category. This avoids giving fake numerical meaning.
  | City_Hyd | City_Chennai | City_Delhi |
  | -------- | ------------ | ---------- |
  | 1 | 0 | 0 |
  | 0 | 1 | 0 |

Code: from sklearn.preprocessing import OneHotEncoder
encoder = OneHotEncoder()
encoded = encoder.fit_transform(data[['City']])

Part 2 — Scaling Numerical Features
Features like Age and Salary may be on different scales. This can cause some models to perform poorly.
| Age | Salary |
| --- | ------ |
| 25 | 50000 |
| 40 | 120000 |
Salary dominates because values are much larger. Some models become biased toward larger-scale features.

- **Standardization**: Centers data to mean=0 and scales to std=1.
  | before Age| | Age_scaled |
  | --- | | ---------- |
  | 20 | | -1.22 |
  | 30 | | 0 |
  | 40 | | 1.22 |

  from sklearn.preprocessing import StandardScaler
  scaler = StandardScaler()
  scaled = scaler.fit_transform(data[['Age', 'Salary']])

- **ColumnTransformer**: This is industry-level preprocessing.
  It allows:
  scaling numerical columns
  encoding categorical columns
  all in one place

  Part 3 — The BIG Problem Without Pipelines. Very easy to make mistakes.

- Imagine this workflow
  scale training data
  encode training data
  train model
- Now for test data:
  scale test data
  encode test data

Common bugs:
❌ forgetting scaling
❌ different transformations
❌ data leakage
❌ messy code
❌ impossible deployment

# What Is a Pipeline?

A pipeline automates preprocessing + model training.
Raw Data
↓
Preprocessing
↓
Feature Engineering
↓
Model Training
↓
Prediction

- Benefits:
  - Consistency: Same steps for train/test
  - Reproducibility: Easy to rerun
  - Clean Code: Organized workflow
  - Easy Deployment: One object to deploy

Instead of: clean manually, scale manually, encode manually, train manually
We do: pipeline.fit(X_train, y_train)
Now scaling automatically happens before prediction.

Part 4 — Different Processing for Different Columns
Real datasets have:
numerical columns
categorical columns

We process them differently. example
| Age | Salary | City |
| --------- | --------- | ----------- |
| numerical | numerical | categorical |
we need to
scaling for numbers
encoding for text

This is where ColumnTransformer becomes powerful.

# ColumnTransformer

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler

preprocessor = ColumnTransformer([
('num', StandardScaler(), ['Age', 'Salary']),
('cat', OneHotEncoder(), ['City'])
])

this does
scale Age + Salary
encode City

# Why Pipelines Are Extremely Important

1. Prevent Data Leakage
   scaler.fit(X_test)
   This leaks information from test data. Pipelines avoid this automatically.

2. Cleaner Code
   Instead of 20 preprocessing lines: we do pipeline.fit()

3. Easier Deployment
   In production: new_data → same preprocessing → prediction
   Pipeline guarantees consistency.

4. Easier Experimentation
   Swap models easily without rewriting preprocessing.

# fit vs transform vs fit_transform

- fit: learns parameters from data (e.g., mean/std for scaling)
- transform: applies learned parameters to data
- fit_transform: does both in one step (fit + transform)

# Example Pipeline Code

from sklearn.pipeline import Pipeline
pipeline = Pipeline([
('preprocessor', preprocessor),
('model', LogisticRegression())
])
pipeline.fit(X_train, y_train)
Now we can do:
predictions = pipeline.predict(X_test)
This ensures all preprocessing happens correctly before prediction.

# 🚀 Day 30

We should understand:

✅ Accuracy
✅ Precision
✅ Recall
✅ F1 Score
✅ Confusion Matrix
✅ ROC-AUC

| Metric    | Best When                  |
| --------- | -------------------------- |
| Accuracy  | Balanced data              |
| Precision | False positives costly     |
| Recall    | False negatives costly     |
| F1 Score  | Need balance               |
| ROC-AUC   | Overall classifier quality |

And know when to use each.
Why Accuracy Can Be Dangerous. Suppose:
100 customers
90 did NOT churn
10 churned
Model predicts: Everyone will NOT churn
Accuracy: 90/100 = 90%
Looks amazing. But model found ZERO churn customers.

1️⃣ Accuracy: Correct Predictions / Total Predictions
from sklearn.metrics import accuracy_score
accuracy_score(y_test, y_pred)

2️⃣ Confusion Matrix: Foundation of classification metrics.
Predicted
No Yes
Actual No TN FP
Actual Yes FN TP
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
print(cm)

3️⃣ Precision: TP / (TP + FP)
Of predicted positives, how many were actually correct?
Eg: TP = 20 and FP = 5
Precision = 20 / (20 + 5) = 80%
High precision = fewer false alarms.
from sklearn.metrics import precision_score
precision_score(y_test, y_pred)

4️⃣ Recall: TP / (TP + FN)
Of actual positives, how many did we find?
Eg: TP = 20 and FN = 10
Recall = 20 / (20 + 10) = 66.7%
High recall = fewer missed cases.
from sklearn.metrics import recall_score
recall_score(y_test, y_pred)

5️⃣ F1 Score: Harmonic mean of precision and recall.
Balance between Precision + Recall.
F1 = 2 _ (Precision _ Recall) / (Precision + Recall)
from sklearn.metrics import f1_score
f1_score(y_test, y_pred)

6️⃣ Classification Report
Best shortcut. Gives:
Precision
Recall
F1
Support
from sklearn.metrics import classification_report
print(classification_report(y_test, y_pred))

7️⃣ ROC-AUC Score
ROC curve plots TPR vs FPR at different thresholds.
AUC = Area Under the ROC Curve
AUC = 1 means perfect model

ROC-AUC evaluates model performance across all classification thresholds, so it needs probability scores, not fixed binary predictions.

from sklearn.metrics import roc_auc_score
roc_auc_score(y_test, y_pred_proba)

# When to Use Each Metric

- Accuracy: When classes are balanced and all errors are equally bad.
- Precision: When false positives are costly (e.g., spam detection).
- Recall: When false negatives are costly (e.g., disease diagnosis).
- F1 Score: When you want a balance between precision and recall.
- Confusion Matrix: To understand types of errors.
- ROC-AUC: To evaluate model performance across thresholds.

# Conclusion

- Always choose metrics based on the problem context.
- Don't rely solely on accuracy.
- Use pipelines to ensure consistent preprocessing and avoid data leakage.

# 🚀 Day 31 Cross Validation + Industry ML Workflow

Problem with train_test_split()
Suppose:
80% training
20% testing
You get: Accuracy = 89%

What if this split was just lucky?
Different random split: Accuracy = 78%
Different split again: Accuracy = 84%
Now which one is true?

That’s why we use Cross Validation.
Cross Validation gives a more reliable estimate of model performance by averaging results across multiple splits.
1️⃣ Cross Validation
Instead of testing once We test multiple times on different splits of the data.
Model trains multiple times. Then averages performance. Much more reliable.
from sklearn.model_selection import cross_val_score
scores = cross_val_score(model, X, y, cv=5)

2️⃣ K-Fold Cross Validation
Data is split into K equal parts (folds). Most common type.
For K=5: (cv=5)
Means: split data into 5 folds. train 5 times. each fold becomes test once
Fold 1: Train on Folds 2-5, Test on Fold 1
Fold 2: Train on Folds 1, 3-5, Test on Fold 2
Fold 3: Train on Folds 1-2, 4-5, Test on Fold 3
Fold 4: Train on Folds 1-3, 5, Test on Fold 4
Fold 5: Train on Folds 1-4, Test on Fold 5
Ex: [0.82, 0.84, 0.79, 0.86, 0.83]
Average: 0.828 That’s your true performance estimate.
from sklearn.model_selection import cross_val_score
scores = cross_val_score(model, X, y, cv=5)
print("Cross Validation Scores:", scores)

3️⃣ cross_val_score()
This is the main function for cross validation in scikit-learn. It takes:

- model
- data (X, y)
- cv (number of folds)
  It returns an array of scores for each fold. You can then average them.
  from sklearn.model_selection import cross_val_score
  scores = cross_val_score(model, X, y, cv=5)
  print("Cross Validation Scores:", scores)
  print("Average CV Score:", scores.mean())

4️⃣ Important Scoring Options
By default, cross_val_score() uses accuracy for classification. But you can specify other metrics:
from sklearn.model_selection import cross_val_score
scores = cross_val_score(model, X, y, cv=5, scoring='precision')
print("Precision Scores:", scores)
scores = cross_val_score(model, X, y, cv=5, scoring='recall')
print("Recall Scores:", scores)
scores = cross_val_score(model, X, y, cv=5, scoring='f1')
print("F1 Scores:", scores)
scores = cross_val_score(model, X, y, cv=5, scoring='roc_auc')
print("ROC-AUC Scores:", scores)

5️⃣ Why Pipeline + CV Together Matter
Pipelines ensure that all preprocessing steps are correctly applied during each fold of cross validation. This prevents data leakage and gives a true estimate of model performance.
BAD: if scale full dataset first then CV. This leaks information called Data Leakage. Model secretly sees test info which is Bad evaluation.
GOOD: Pipeline handles preprocessing inside each fold. Then CV happens safely.
Pipeline([
preprocessing,
model
])
