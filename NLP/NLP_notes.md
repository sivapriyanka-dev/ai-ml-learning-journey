# ✅ Day 36 — NLP Fundamentals - Natural Language Processing

1. NLP = teaching computers to understand human language.
   Examples:
   Spam detection
   Sentiment analysis
   Chatbots
   Translation
   Auto-correct
   Voice assistants

Eg: "I love this movie"
Machine sees - text → numbers → prediction

2. NLP Pipeline
   Text
   ↓
   Cleaning
   ↓
   Tokenization
   ↓
   Stopword removal
   ↓
   Stemming/Lemmatization
   ↓
   Vectorization
   ↓
   Model training

3. Text Cleaning
   Raw text: "I LOVE Python!!! 100%"
   After cleaning: "love python"
   Cleaning includes:
   Lowercase
   Remove punctuation
   Remove numbers
   Remove special characters

4. Tokenization
   Split sentence into words.
   Eg: "I love NLP" -> ["I", "love", "NLP"]

5. Stopwords
   Common words with little meaning.
   Eg: the, is, am, are, in, on
   in Sentence: "I am learning NLP" -> ["learning", "NLP"]

6. Stemming
   Cuts words to root form. Fast but crude.
   Eg:
   playing → play
   studies → studi
   running → run

7. Lemmatization
   Smarter root conversion. Better than stemming.
   Eg:
   studies → study
   better → good
   running → run

8. Bag of Words
   Convert text into numbers.
   Sentences:
   "I love NLP"
   "I love Python"
   Vocabulary: ["I", "love", "NLP", "Python"]
   Vectors:
   [1,1,1,0]
   [1,1,0,1]

9. TF-IDF
   TF = How common in THIS document (Term Frequency)
   IDF = How rare in ALL documents (Inverse Document Frequency)
   Improved Bag of Words. Important words get higher weight.
   Example:
   "the" appears everywhere → low importance
   "python" appears rarely → high importance
   Formula: important word = common here + rare everywhere else

For Code
pip install nltk scikit-learn pandas
NLTK (Natural Language Toolkit)

# MultinomialNB = Multinomial Naive Bayes

It’s a machine learning algorithm mainly used for text classification. Based on probability (Bayes theorem).
Multinomial Naive Bayes is a probabilistic classification algorithm commonly used for NLP tasks. It works well with text features like word counts or TF-IDF and predicts classes based on probability

Examples:
Spam detection
Sentiment analysis
News classification
Document categorization

TF-IDF gives words → MultinomialNB classifies them
