# LLMs (Large Language Models)

LLMs are advanced language models trained on vast amounts of text data. They can generate human-like text, understand context, and perform various NLP tasks.
Examples:
GPT-3
BERT
T5
LLMs are the foundation of many AI applications, including chatbots, virtual assistants, and content generation tools. They have revolutionized the field of NLP and continue to evolve rapidly.

- BERT:
  understands text
  classification

BERT is Encoder model. Good for:
sentiment analysis
classification
search
question answering

Example: "This review is positive"

- GPT:
  generates text
  chatting
  coding
  reasoning

GPT is Decoder model. Good for:
text generation
conversations
coding
writing

Example: "Write python code for login API"

# LLM basics

LLMs are trained on huge datasets using self-supervised learning. They learn to predict the next word in a sentence, which helps them understand language patterns and context.
LLMs use attention mechanisms to focus on relevant parts of the input when generating output. This allows them to produce coherent and contextually appropriate responses.

1. Tokens
   LLMs don’t read words. They read tokens.
   Example: "I love machine learning"
   may become: ["I", "love", "machine", "learning"]
   Sometimes: "unbelievable"
   becomes: ["un", "believ", "able"]
   Why? Smaller chunks easier to learn.
2. Context Window
   How much model remembers at once.
   Example: Small model: 4000 tokens
   Big model: 128k tokens
   Meaning: How much conversation/document fits in memory.
   Analogy: working memory
3. Temperature
   Controls creativity.
   Low: temperature=0.1
   Output: predictable / factual
   Example: 2 + 2 = 4
   High: temperature=1.2
   Output: creative / varied
   Used for:
   stories
   brainstorming
4. Top-k / Top-p
   How next word is chosen.
   Model predicts probabilities:
   cat = 40%
   dog = 30%
   car = 5%
   pizza = 1%
   Top-k: pick from top few words.
   Top-p: pick until cumulative probability threshold.
   Controls randomness.
5. Embeddings
   Instead of classification: convert text into vectors.
   Example:
   "dog" → [0.21, -0.8, 0.55 ...]
   "puppy" → [0.20, -0.79, 0.53 ...]
   Close vectors = similar meaning.
   This powers:
   semantic search
   recommendations
   RAG

# RAG (Retrieval-Augmented Generation)

RAG combines LLMs with external knowledge sources. It retrieves relevant information from a database or search engine and uses it to generate more accurate and informed responses.
Example: "What is the capital of France?"
RAG retrieves: "The capital of France is Paris"
RAG is useful for tasks that require up-to-date information or specific knowledge that may not be present in the training data of the LLM. It enhances the capabilities of LLMs by providing access to external information sources.

# !pip install sentence-transformers

ready-made embedding models

Used everywhere in AI apps:
ChatGPT memory systems
semantic search
recommendations
RAG
document search

# What are embeddings?

Normal text: "I love dogs" Machine cannot understand meaning.
Embeddings convert text → numbers with meaning.
Example:
"I love dogs" → [0.12, -0.88, 0.43, ...]
Another:
"I like puppies" → [0.10, -0.85, 0.40, ...]

These vectors will be close because meanings are similar.
But: "I hate traffic"
vector far away.

This is called: semantic meaning

Analogy:
Imagine map coordinates.
Hyderabad: (17.38, 78.48)
Bangalore: (12.97, 77.59)
Nearby cities = closer points.
Same idea: Similar sentences = closer vectors.
