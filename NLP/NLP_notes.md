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

# Day 46 → Sequence Models (RNN / LSTM)

Sequence models = understand order of words
RNN (Recurrent Neural Network) = remembers previous words
LSTM (Long Short-Term Memory) = better at remembering long-term dependencies
Example:
"I love NLP because it’s amazing"
RNN processes:
"I" → "love" → "NLP" → "because" → "it’s" → "amazing"
LSTM can remember "I love NLP" even after processing "because it’s amazing"

Classic NLP (done)
↓
RNN
↓
LSTM
↓
Attention
↓
Transformers
↓
BERT/GPT
↓
LLMs
↓
RAG / AI apps

Real problem
Classic NLP treats text like: unordered bag of words
But language is: ordered sequence
RNN says: Instead of seeing words independently: read one word at a time remember previous context
Think like: Human reading:
You don't read all words independently.
You remember previous words.
That’s RNN.

RNN formula (conceptually)
new hidden state = current input + previous hidden state
like:
Current memory: I
Current memory: I love
Current memory: I love deep
Current memory: I love deep learning

# RNNs are powerful but have limitations:

Vanishing gradients: struggle to learn long-term dependencies
LSTMs solve this with special gates:
Forget gate: decides what to forget
Input gate: decides what new information to add
Output gate: decides what to output

# Example code for RNN/LSTM using Keras

```python
import numpy as np
from keras.models import Sequential
from keras.layers import Embedding, LSTM, Dense
# Sample data
sentences = ["I love NLP", "NLP is amazing", "I enjoy deep learning"]
labels = [1, 1, 1]  # Dummy labels for binary classification
# Tokenization and padding (simplified)
tokenizer = Tokenizer(num_words=10000)
tokenizer.fit_on_texts(sentences)
sequences = tokenizer.texts_to_sequences(sentences)
from keras.preprocessing.sequence import pad_sequences
X = pad_sequences(sequences, maxlen=5)
y = np.array(labels)

# Build RNN/LSTM model
model = Sequential()
model.add(Embedding(input_dim=10000, output_dim=64, input_length=5))
model.add(LSTM(64))
model.add(Dense(1, activation='sigmoid'))
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.fit(X, y, epochs=10)
```

This code demonstrates a simple LSTM model for text classification. It includes tokenization, padding, and model building using Keras. The model is trained on dummy data for demonstration purposes.

# GRU

GRU (Gated Recurrent Unit) = simpler than LSTM, fewer parameters, faster to train
GRU has two gates:
Update gate: decides how much of the past information to keep
Reset gate: decides how much of the past information to forget
Example:
"I love NLP because it’s amazing"
GRU processes:
"I" → "love" → "NLP" → "because" → "it’s" → "amazing"
GRU can remember "I love NLP" even after processing "because it’s amazing" but with fewer parameters than LSTM.

# Example code for GRU using Keras

```python
import numpy as np
from keras.models import Sequential
from keras.layers import Embedding, GRU, Dense
# Sample data
sentences = ["I love NLP", "NLP is amazing", "I enjoy deep learning"]
labels = [1, 1, 1]  # Dummy labels for binary classification
# Tokenization and padding (simplified)
tokenizer = Tokenizer(num_words=10000)
tokenizer.fit_on_texts(sentences)
sequences = tokenizer.texts_to_sequences(sentences)
from keras.preprocessing.sequence import pad_sequences
X = pad_sequences(sequences, maxlen=5)
y = np.array(labels)
# Build GRU model
model = Sequential()
model.add(Embedding(input_dim=10000, output_dim=64, input_length=5))
model.add(GRU(64))
model.add(Dense(1, activation='sigmoid'))
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.fit(X, y, epochs=10)
```

This code demonstrates a simple GRU model for text classification. It includes tokenization, padding, and model building using Keras. The model is trained on dummy data for demonstration purposes.
