# ✅ Day 18 — Underfitting vs Overfitting

1️⃣ Underfitting - High Variance

Model is too simple. It misses the real pattern.
Example: Trying to fit a straight line to complicated curved data.

Analogy: Studying only chapter titles for an exam 😅
Result:
Bad on training data
Bad on test data

Signs of Underfitting :
-> Low training accuracy
-> Low test accuracy

Note: Too simple. (only straight line for complex data)

Why it happens?

- Model too simple
- Not enough training
- Poor features

2️⃣ Overfitting - High Bias

Model memorizes training data. Looks amazing during training, but fails on new data.

Analogy: Memorizing exact answers instead of understanding concepts.
Result:
Very high training performance
Poor test performance

Note: Crazy curve trying to hit every point. (too much noise learned)

Why it happens?

- Model too complex
- Too little data
- Learns noise

# What actually happens in flow.

Your data:
X y
2 40
4 60
6 80
8 100
10 120
12 140

Relationship is: y=10x+20 Perfectly linear.

1. Training

   After split:
   X_train = [[12],[6],[10],[8]]
   y_train = [140,80,120,100]
   then model.fit(X_train, y_train)

   What training means - The model looks at those points and learns:
   slope m = 10
   intercept b = 20

   So it learns: y=10x+20 - This is training performance.

   If we tested it on those same training points:
   x=6 → predicts 80 ✔
   x=8 → predicts 100 ✔

   Training score = perfect.

2. Testing

   Held-out unseen data:
   X_test = [[2],[4]]
   y_test = [40,60]

   Now: model.predict(X_test)
   Predicts: [40,60]
   Compare to actual: [40,60]

   Perfect again. Test score = perfect.

# Good fit (ideal)

Line matches trend.
Suppose:
Train accuracy = 95%
Test accuracy = 93%

Close together and high.
✅ Learned real pattern.

# Overfitting - High Variance

Curve wiggles through every point.
Suppose model memorizes training data.
Train = 99%
Test = 55%

Looks amazing during training. fails on new data.
❌ Overfit. Like memorizing practice questions.

# Underfitting - High Bias

Line too simple misses trend.
Model too simple / not learning enough.
Train = 60%
Test = 58%

Bad on both.
❌ Underfit. Like barely studying.
