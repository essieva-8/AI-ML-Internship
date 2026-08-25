#Task 1

from langchain_chroma import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

# Sample documents
documents = [
    "Python is a popular programming language.",
    "Machine Learning allows computers to learn from data.",
    "Deep Learning uses neural networks.",
    "Natural Language Processing deals with human language.",
    "RAG combines retrieval with language generation."
]

# Create embedding model
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Create ChromaDB vector store
vectorstore = Chroma.from_texts(
    texts=documents,
    embedding=embeddings,
    collection_name="day73_collection"
)

# Convert vector store into a retriever
retriever = vectorstore.as_retriever(
    search_kwargs={"k": 3}
)


#Task 2

# Five user questions
questions = [
    "What is machine learning?",
    "How long is the internship?",
    "What does a retriever do?",
    "What is BM25?",
    "What is hybrid search?"
]

# Retrieve top 3 documents
for question in questions:

    print("\n" + "=" * 60)
    print("Question:", question)
    print("=" * 60)

    results = retriever.invoke(question)

    for i, doc in enumerate(results, start=1):
        print(f"{i}. {doc.page_content}")


#Task 3

# -----------------------------
# Keyword Search
# -----------------------------

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

print("\n" + "=" * 60)
print("KEYWORD SEARCH - TF-IDF")
print("=" * 60)

# Create TF-IDF vectorizer
vectorizer = TfidfVectorizer()

# Convert documents into TF-IDF vectors
tfidf_matrix = vectorizer.fit_transform(documents)

for question in questions:

    print("\nQuestion:", question)
    print("-" * 60)

    # Convert question into TF-IDF vector
    question_vector = vectorizer.transform([question])

    # Calculate cosine similarity
    scores = cosine_similarity(
        question_vector,
        tfidf_matrix
    )[0]

    # Display results
    for index in scores.argsort()[::-1]:
        print(
            f"Score: {scores[index]:.4f} | "
            f"{documents[index]}"
        )

# -----------------------------
# Dense Retrieval
# -----------------------------

from sentence_transformers import SentenceTransformer

print("\n" + "=" * 60)
print("DENSE RETRIEVAL")
print("=" * 60)

# Load Sentence Transformer model ONCE
model = SentenceTransformer("all-MiniLM-L6-v2")

# Create embeddings for documents ONCE
document_embeddings = model.encode(documents)

for question in questions:

    print("\nQuestion:", question)
    print("-" * 60)

    # Create embedding for question
    query_embedding = model.encode([question])

    # Calculate cosine similarity
    dense_scores = cosine_similarity(
        query_embedding,
        document_embeddings
    )[0]

    # Display results
    for index in dense_scores.argsort()[::-1]:
        print(
            f"Score: {dense_scores[index]:.4f} | "
            f"{documents[index]}"
        )

# Dense retrieval is better suited to this example because it uses embeddings to capture semantic similarity rather than relying only on exact keyword overlap.


#Task 4

print("BM25 (Best Matching 25) is an advanced keyword-based information-retrieval algorithm.")
print("It ranks documents based on factors such as keyword frequency, document length, and word importance.")

print("\nTwo real-world applications")

print("1. Elasticsearch — uses BM25 as its default similarity algorithm for relevance scoring in text search.")
print("2. Apache Lucene — provides BM25-based relevance scoring and is widely used as the underlying search technology in many applications.")


#Task 5

import pandas as pd

data = {
    "Retrieval Method": [
        "Sparse Retrieval",
        "Dense Retrieval",
        "BM25",
        "Hybrid Search"
    ],
    "How it Works": [
        "Matches exact keywords",
        "Uses embeddings to compare semantic meaning",
        "Ranks documents using keyword frequency, document length and relevance",
        "Combines sparse/BM25 and dense retrieval"
    ],
    "Advantages": [
        "Fast, simple, easy to implement",
        "Understands meaning, high accuracy",
        "Strong keyword ranking, efficient",
        "Very high retrieval quality, combines both strengths"
    ],
    "Disadvantages": [
        "Poor with synonyms and semantic meaning",
        "Requires embedding models and more computation",
        "Does not fully understand semantic meaning",
        "More resources and complexity"
    ],
    "Use Cases": [
        "Keyword search, document search",
        "AI chatbots, RAG systems, semantic search",
        "Search engines, document retrieval",
        "Enterprise RAG, advanced search systems"
    ]
}

df = pd.DataFrame(data)

print(df.to_string(index=False))