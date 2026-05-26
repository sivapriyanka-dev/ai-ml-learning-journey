# RAG (Retrieval Augmented Generation)

RAG = LLM + Retrieval
LLM = language model that generates text
Retrieval = search system that finds relevant info
RAG combines:

1. LLM generates text based on input
2. Retrieval finds relevant info from external source
3. LLM uses retrieved info to produce better output
   Example:
   User:
   "What is the capital of France?"
   RAG process:
4. LLM generates initial response: "The capital of France is Paris."
5. Retrieval finds relevant info: "The capital of France is Paris."
6. LLM confirms and produces final response: "The capital of France is Paris."
   Benefits of RAG:
   ✅ more accurate responses
   ✅ up-to-date information
   ✅ handles complex queries
   RAG is used in:

- question answering systems
- chatbots
- research assistants
- any AI application that benefits from combining generation with retrieval.

- Without RAG:
  LLM only knows training knowledge.
  Example:
  Ask: What is Priyanka's leave balance?
  GPT says: I don't know
  because private company data isn't in training.

- With RAG:
  System:
  - Step 1 Retrieve relevant docs
    Search:
    leave policy docs
    employee DB
    internal FAQ
    using embeddings.
  - Step 2 Send retrieved docs to LLM
    Prompt:
    Answer using this context:
    <retrieved docs here>
  - Step 3 Generate answer
    Now model answers correctly.

# Architecture:

User question
↓
Convert to embedding
↓
Vector DB similarity search
↓
Retrieve relevant chunks
↓
Send chunks + question to LLM
↓
Answer

# Real production flow:

PDFs / Docs / Company KB
↓
Chunk documents
↓
Create embeddings
↓
Store in vector DB
↓
User asks question
↓
Convert question to embedding
↓
Similarity search
↓
Retrieve top chunks
↓
Send chunks + question to GPT
↓
Natural answer

# Code

prompt = "Explain machine learning in simple words:"
result = generator(
prompt,
max_new_tokens=80,
do_sample=True,
temperature=0.7,
top_k=50,
top_p=0.95,
repetition_penalty=1.2
)
print(result[0]["generated_text"])

What these do:

- do_sample=True
  allows randomness instead of repeating same highest-probability token
- temperature=0.7
  balanced creativity
- top_k=50
  pick from top 50 probable next words
- top_p=0.95
  nucleus sampling
- repetition_penalty=1.2
  punishes repeating same words
- max_new_tokens
  cleaner than max_length
