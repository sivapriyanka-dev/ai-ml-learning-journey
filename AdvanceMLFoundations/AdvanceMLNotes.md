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

- **One-Hot Encoding**: Creates binary columns for each category. This avoids giving fake numerical meaning.
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
