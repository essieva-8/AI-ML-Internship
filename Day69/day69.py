#Task 1

import chromadb

# Create ChromaDB client
client = chromadb.Client()

# Create collection
collection = client.create_collection(
    name="college_data"
)

print("Collection created successfully!")
print("Collection name:", collection.name)


#Task 2

collection.add(
    documents=[
        "The AI/ML internship fee is ₹5000.",
        "The internship duration is 3 months.",
        "Students with a background in Computer Science, Data Science, Mathematics, or related fields are eligible.",
        "Hostel accommodation is available for selected students.",
        "Students receive placement assistance after completing the internship."
    ],
    ids=[
        "1",
        "2",
        "3",
        "4",
        "5"
    ]
)

print("Five documents inserted successfully!")


#Task 3

results = collection.query(
    query_texts=[
        "How long is the internship?"
    ],
    n_results=1
)

print("Retrieved result:")
print(results["documents"][0][0])


#Task 4

import faiss
print("FAISS imported successfully!")


#Task 5

print(f"{'Feature':<20} {'ChromaDB':<40} {'FAISS':<45} {'Pinecone':<45}")
print("-" * 140)

print(f"{'Open Source':<20} {'Yes':<40} {'Yes':<45} {'No':<45}")
print(f"{'Cloud Support':<20} {'Can be self-hosted; cloud options exist':<40} {'Primarily a library/self-managed':<45} {'Yes':<45}")
print(f"{'Ease of Use':<20} {'Easy / beginner-friendly':<40} {'More advanced':<45} {'Easy managed service':<45}")
print(f"{'Best Use Cases':<20} {'RAG, semantic search, AI applications':<40} {'High-speed similarity search, large vector collections':<45} {'Cloud-based, scalable AI applications':<45}")
