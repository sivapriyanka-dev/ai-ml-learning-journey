# Day 36 NLP Fundamentals

import pandas as pd
import nltk
import string
import re

from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

# Download NLTK data
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')
nltk.download('wordnet')

# Sample text
text = "I LOVE learning Python for NLP!!! It is amazing, 100% useful."

print("Original Text:")
print(text)

# ---------------------------
# 1. Lowercase
# ---------------------------
text = text.lower()
print("\nLowercase:")
print(text)

# ---------------------------
# 2. Remove numbers
# ---------------------------
text = re.sub(r'\d+', '', text)
print("\nRemove Numbers:")
print(text)

# ---------------------------
# 3. Remove punctuation
# ---------------------------
text = text.translate(str.maketrans('', '', string.punctuation))
print("\nRemove Punctuation:")
print(text)

# ---------------------------
# 4. Tokenization
# ---------------------------
tokens = nltk.word_tokenize(text)
print("\nTokens:")
print(tokens)

# ---------------------------
# 5. Stopword Removal
# ---------------------------
stop_words = set(stopwords.words('english'))
filtered_tokens = [word for word in tokens if word not in stop_words]

print("\nAfter Stopword Removal:")
print(filtered_tokens)

# ---------------------------
# 6. Stemming
# ---------------------------
stemmer = PorterStemmer()
stemmed = [stemmer.stem(word) for word in filtered_tokens]

print("\nStemmed Words:")
print(stemmed)

# ---------------------------
# 7. Lemmatization
# ---------------------------
lemmatizer = WordNetLemmatizer()
lemmatized = [lemmatizer.lemmatize(word) for word in filtered_tokens]

print("\nLemmatized Words:")
print(lemmatized)

# ---------------------------
# 8. Bag of Words
# ---------------------------
documents = [
    "I love NLP",
    "I love Python",
    "Python is great for machine learning"
]

vectorizer = CountVectorizer()
X_bow = vectorizer.fit_transform(documents)

print("\nBag of Words Feature Names:")
print(vectorizer.get_feature_names_out())

print("\nBag of Words Matrix:")
print(X_bow.toarray())

# ---------------------------
# 9. TF-IDF
# ---------------------------
tfidf = TfidfVectorizer()
X_tfidf = tfidf.fit_transform(documents)

print("\nTF-IDF Feature Names:")
print(tfidf.get_feature_names_out())

print("\nTF-IDF Matrix:")
print(X_tfidf.toarray())
