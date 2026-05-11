# Day 37 NLP Project — Spam Classifier

import pandas as pd
import re
import string
import nltk

from nltk.corpus import stopwords
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Download resources
nltk.download('stopwords')

# -----------------------------
# Sample Dataset
# -----------------------------
data = {
    "message": [
        "Congratulations! You won a free iPhone",
        "Claim your ₹5000 reward now",
        "Win cash prize click here",
        "Limited time offer claim now",
        "Free entry in lottery",
        "Urgent! Your account won prize",

        "Hey how are you?",
        "Let's meet tomorrow",
        "Can you call me back?",
        "Dinner at 8?",
        "Where are you now?",
        "Happy birthday have a great day"
    ],
    "label": [
        "spam", "spam", "spam", "spam", "spam", "spam",
        "ham", "ham", "ham", "ham", "ham", "ham"
    ]
}

df = pd.DataFrame(data)

print("Dataset:")
print(df)

# -----------------------------
# Text Cleaning Function
# -----------------------------
stop_words = set(stopwords.words('english'))


def clean_text(text):
    text = text.lower()
    text = re.sub(r'\d+', '', text)
    text = text.translate(str.maketrans('', '', string.punctuation))
    words = text.split()
    words = [word for word in words if word not in stop_words]
    return " ".join(words)


df["clean_message"] = df["message"].apply(clean_text)

print("\nCleaned Data:")
print(df)

# -----------------------------
# Features + Labels
# -----------------------------
X = df["clean_message"]
y = df["label"]

# -----------------------------
# TF-IDF
# -----------------------------
vectorizer = TfidfVectorizer()
X_tfidf = vectorizer.fit_transform(X)

print("\nFeature Names:")
print(vectorizer.get_feature_names_out())

# -----------------------------
# Train/Test Split
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X_tfidf, y, test_size=0.3, random_state=42, stratify=y
)

# -----------------------------
# Model Training
# -----------------------------
model = MultinomialNB()
model.fit(X_train, y_train)

# -----------------------------
# Prediction
# -----------------------------
y_pred = model.predict(X_test)

print("\nAccuracy:", accuracy_score(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# -----------------------------
# Custom Prediction
# -----------------------------
new_messages = [
    "You won a cash prize click now",
    "Hey can we talk tonight?"
]

new_clean = [clean_text(msg) for msg in new_messages]
new_vector = vectorizer.transform(new_clean)

predictions = model.predict(new_vector)

print("\nCustom Predictions:")
for msg, pred in zip(new_messages, predictions):
    print(f"{msg} --> {pred}")
