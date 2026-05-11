import pandas as pd
import re
import string
import nltk
import matplotlib.pyplot as plt
import seaborn as sns

from nltk.corpus import stopwords
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

# Download stopwords
nltk.download('stopwords')

# ---------------------------
# Load Dataset
# ---------------------------
df = pd.read_csv("NLP/sms-spam-detector/spam.csv", encoding="latin-1")

# Keep only useful columns
df = df[['v1', 'v2']]
df.columns = ['label', 'message']

print(df.head())
print(df.info())

# ---------------------------
# Data Visualization
# ---------------------------
plt.figure(figsize=(6, 4))
sns.countplot(x='label', data=df)
plt.title("Spam vs Ham Distribution")
plt.show()

# ---------------------------
# Text Cleaning
# ---------------------------
stop_words = set(stopwords.words('english'))


def clean_text(text):
    text = text.lower()
    text = re.sub(r'\d+', '', text)
    text = text.translate(str.maketrans('', '', string.punctuation))
    words = text.split()
    words = [word for word in words if word not in stop_words]
    return " ".join(words)


df['clean_message'] = df['message'].apply(clean_text)

# ---------------------------
# Label Encoding
# ---------------------------
df['label'] = df['label'].map({
    'ham': 0,
    'spam': 1
})

# ---------------------------
# Features + Target
# ---------------------------
X = df['clean_message']
y = df['label']

# ---------------------------
# TF-IDF
# ---------------------------
vectorizer = TfidfVectorizer(max_features=3000)
X_tfidf = vectorizer.fit_transform(X)

# ---------------------------
# Train Test Split
# ---------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X_tfidf,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# ---------------------------
# Model
# ---------------------------
model = MultinomialNB()
model.fit(X_train, y_train)

# ---------------------------
# Predictions
# ---------------------------
y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# ---------------------------
# Confusion Matrix
# ---------------------------
cm = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(6, 4))
sns.heatmap(cm, annot=True, fmt='d')
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()

# ---------------------------
# Custom Prediction
# ---------------------------
messages = [
    "Congratulations! You won ₹10000",
    "Hey where are you?"
]

cleaned = [clean_text(msg) for msg in messages]
vectorized = vectorizer.transform(cleaned)

preds = model.predict(vectorized)

for msg, pred in zip(messages, preds):
    result = "Spam" if pred == 1 else "Ham"
    print(msg, "->", result)
