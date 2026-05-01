# ✅ Day 19 — Classification

Regression vs Classification

- Regression - Predicts numbers

Examples:
House price
Salary
Marks

- Classification - Predicts labels/categories/classes

Examples:
Pass / Fail
Spam / Not Spam
Disease / No Disease

Example Dataset for Classification
Hours Studied Pass
2 0
4 0
6 1
8 1

Where:
0 = Fail
1 = Pass

# First Classification Model: Logistic Regression

(Despite name "regression", it's for classification 😄)
example:
X Class(y)
2 0
4 0
6 1
8 1
Training - model.fit(X,y)
The model learns:
Lower X values → likely class 0
Higher X values → likely class 1

=> It tries to find a boundary separating classes. Probably around: x≈5

Why not use a straight line? If we used linear regression: y=mx+b predictions might be:
1.3
-0.2

But classes should only be:
0
1

So logistic regression converts outputs into probabilities.

It uses a sigmoid function - P(y=1)=1/1+e−(mx+b)

This squashes values into:
between 0 and 1
interpreted as probability
example: For model.predict([[5]])
Model may think: Probability of class 1 = 0.52
Since above 0.5 threshold: [1]

- Logistic regression: S-shaped curve:

Linear Regression: Predicts: 75.3
Logistic Regression: Predicts probability: P(class=1)=0.82 then converts to: 1 (class)

- predict_proba() is where logistic regression becomes intuitive.
  print(model.predict([[5]])) => [1] That only tells final class.
  print(model.predict_proba([[5]])) => [[0.48 0.52]] returns probabilities for each class.
  This means:
  48% chance class 0
  52% chance class 1

Since 52% is bigger predict() -> 1

📌 Real Uses
Fraud detection
Spam filters
Disease prediction
Customer churn

# ✅ Day 20 — Classification Evaluation

1️⃣ Accuracy
Accuracy = Total Predictions / Correct Predictions
​
Example:
10 predictions
8 correct
Accuracy = 80%

from sklearn.metrics import accuracy_score
y_true = [1,0,1,1]
y_pred = [1,0,0,1]

print(accuracy_score(y_true,y_pred)) => 0.75 (75%)

2️⃣ Confusion Matrix
Shows what model got right/wrong.

from sklearn.metrics import confusion_matrix
print(confusion_matrix(y_true,y_pred))

          Predicted
         0      1

Actual 0 TN FP
Actual 1 FN TP

- Meaning
  TP = True Positive - Correct positive prediction
  TN = True Negative - Correct negative prediction
  FP = False Positive - Predicted positive wrongly
  FN = False Negative - Missed a positive

Example: Spam filter:
Email actually important, but predicted spam?
That’s False Positive. which is Bad 😬

3️⃣ Precision - “When I say yes, how often am I right?”
Of predicted positives, how many were correct?

Precision = TP/TP+FP

Important when false alarms are costly.

4️⃣ Recall - “How many real yes cases did I find?”
Of actual positives, how many did we catch?

Recall=TP/TP+FN

Important in medical diagnosis. Missing disease is dangerous.

# code

from sklearn.metrics import precision_score, recall_score

print(precision_score(y_true,y_pred))
print(recall_score(y_true,y_pred))

# Easy memory trick for TP TN FP FN

True = prediction was correct
False = prediction was wrong
Positive/Negative = what model predicted

| Actual \ Predicted | Positive | Negative |
| ------------------ | -------- | -------- |
| Positive           | TP       | FN       |
| Negative           | FP       | TN       |

1. True Positive (TP) ✅ Model says positive, and reality is positive.
   Correct positive prediction.
   Predicted: Disease
   Actual: Disease
   Example: Doctor test says you have disease, and you really do.

2. True Negative (TN) ✅ Model says negative, and reality is negative.
   Correct negative prediction.
   Predicted: No disease
   Actual: No disease

3. False Positive (FP) ❌ Model says positive wrongly. predicted positive wrongly
   False alarm. Sometimes called Type I Error.
   Predicted: Disease
   Actual: No disease
   Example: Test says you have disease, but you don’t.

4. False Negative (FN) ❌ Model misses a real positive. predicted negative wrongly
   Dangerous miss. Also called Type II Error.
   Predicted: No disease
   Actual: Disease
   Example: Test says you're healthy, but you actually have disease.

# ✅ Day 21 — Decision Trees - Rule-based categories

# Second Classification Model: Decision Trees

This model makes predictions using if-else style questions. Very human-like.
Instead of fitting equations, it asks questions:

Is hours studied > 5?
Yes → Pass
No → Fail
That’s a tiny decision tree.

           Hours > 5?
            /     \
          No      Yes
         Fail   Attendance >80?
                   /    \
                 No     Yes
               Fail    Pass

🎯 Used For Classification:

- Spam detection
- Loan approval
- Disease diagnosis
  Can also do regression too.

⚠️ But... Decision trees can overfit.
If tree becomes too complex:
memorizes data
poor generalization

# ✅ Day 22 — Random Forest 🌲🌲🌲 - ensemble model (many models together)

Instead of relying on one decision tree (which can overfit), we use many trees and combine their results.
🌳 Why "Forest"?
One tree → may make mistakes
Many trees → more reliable

Think like voting:
Tree 1 → Pass  
Tree 2 → Pass  
Tree 3 → Fail  
Final → Pass (majority vote)

Why Random Forest is Powerful.
Because:
Different trees learn different patterns
Errors cancel out

| Decision Tree   | Random Forest    |
| --------------- | ---------------- |
| Single tree     | Many trees       |
| Overfits easily | Less overfitting |
| Simple          | More accurate    |

NOTE:
Decision Tree → one opinion
Random Forest → group decision
👉 Group usually smarter
