#Task 1

import chromadb

# Create ChromaDB client
client = chromadb.Client()

# Create collection
collection = client.create_collection(name="internship_documents")

# Sample documents
documents = [
    "The AI internship duration is 3 months.",
    "The internship fee is completely free.",
    "Placement assistance is available for eligible candidates.",
    "The internship starts on August 1.",
    "A certificate is provided after successful completion.",
    "Students learn Artificial Intelligence and Machine Learning.",
    "Python programming is an important part of the internship.",
    "Students work on practical AI and ML projects.",
    "The internship includes hands-on training.",
    "Students learn about Retrieval Augmented Generation and RAG."
]

# Unique IDs
ids = [f"doc_{i}" for i in range(1, 11)]

# Add documents to ChromaDB
collection.add(
    documents=documents,
    ids=ids
)

print("10 documents successfully added to ChromaDB.")

# Display stored documents
results = collection.get()

print("\nStored Documents:")
for doc_id, document in zip(results["ids"], results["documents"]):
    print(doc_id, ":", document)


#Task 2

# Questions
questions = [
    "What is the internship fee?",
    "How long is the internship?",
    "Is placement assistance available?"
]

# Perform similarity search
for question in questions:

    print("\n" + "=" * 60)
    print("Question:", question)
    print("=" * 60)

    results = collection.query(
        query_texts=[question],
        n_results=3
    )

    print("\nRetrieved Results:")

    for i, document in enumerate(results["documents"][0], start=1):
        print(f"{i}. {document}")


#Task 3 

# Compare different values of n_results
for question in questions:
    print("\n" + "=" * 60)
    print("Question:", question)
    print("=" * 60)

    for n in [1, 3, 5]:
        results = collection.query(
            query_texts=[question],
            n_results=n
        )

        print(f"\nTop {n} Retrieved Results:")
        for i, document in enumerate(results["documents"][0], start=1):
            print(f"{i}. {document}")


#Task 4

# Comparison of Similarity Metrics

comparison = {
    "Metric": [
        "Cosine Similarity",
        "Euclidean Distance",
        "Dot Product"
    ],
    "Description": [
        "Measures the angle between two vectors",
        "Measures the straight-line distance between vectors",
        "Compares vectors by multiplying corresponding values"
    ],
    "Advantages": [
        "Focuses on vector direction and works well for semantic similarity",
        "Simple and intuitive distance measurement",
        "Efficient and works well with normalized vectors"
    ],
    "Common Use Cases": [
        "Text embeddings, document retrieval, RAG",
        "Clustering and vector similarity",
        "Embedding search and vector databases"
    ]
}

# Print comparison table
print("Comparison of Similarity Metrics")
print("-" * 200)

print(f"{'Metric':<25}{'Description':<55}{'Advantages':<70}{'Common Use Cases'}")
print("-" * 200)

for i in range(3):
    print(
        f"{comparison['Metric'][i]:<25}"
        f"{comparison['Description'][i]:<55}"
        f"{comparison['Advantages'][i]:<70}"
        f"{comparison['Common Use Cases'][i]}"
    )


#Task 5

# Accept user query
query = input("Enter your question: ")

# Perform similarity search
results = collection.query(
    query_texts=[query],
    n_results=3
)

# Display results
print("\nTop 3 Most Similar Document Chunks:")
print("-" * 50)

for i, document in enumerate(results["documents"][0], start=1):
    print(f"{i}. {document}")


