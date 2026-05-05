# ✅ Day 28 — Model Tuning & Performance Improvement

# Model Tuning

Model tuning = finding the best combination of parameters + data processing to maximize performance

Every model has settings (hyperparameters)
Example:
KNN → k
Random Forest → number of trees
SVM → kernel
👉 Choosing best values = tuning

1. Hyperparameter Tuning
   Parameters you set manually:
   max_depth (tree depth)
   n_estimators (number of trees)
   learning_rate
   C, gamma (SVM)

2. Performance Improvement Techniques
   Feature scaling
   Feature selection
   Cross-validation
   Handling overfitting / underfitting

- Example: KNN Tuning
  model = KNeighborsClassifier(n_neighbors=3)
  with these changes Accuracy changes
  n_neighbors = 1
  n_neighbors = 3
  n_neighbors = 5
- Example: Random Forest
  model = RandomForestClassifier(n_estimators=10)
  with these changes More trees → usually better (but slower)
  n_estimators=10
  n_estimators=50
  n_estimators=100

There is no perfect model, Only best model + best parameters for your data

- Tuning is about finding the best fit for your data

# Grid Search (Automatic Tuning)

Instead of guessing manually we use so it Finds best parameter automatically
from sklearn.model_selection import GridSearchCV

# Performance of model

80% ML performance comes from:
Data
Feature engineering
Tuning
NOT just model choice.

# workflow is Train → Evaluate → Tune → Evaluate → Improve

| Model               | Most Important Parameter |
| ------------------- | ------------------------ |
| Linear Regression   | alpha                    |
| Logistic Regression | C                        |
| Decision Tree       | max_depth                |
| Random Forest       | n_estimators             |
| SVM                 | C, gamma                 |
| KNN                 | n_neighbors              |
| Naive Bayes         | almost none              |
