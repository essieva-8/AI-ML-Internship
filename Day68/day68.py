#Task 2

from sentence_transformers import SentenceTransformer

# Load the pre-trained model
model = SentenceTransformer("all-MiniLM-L6-v2")
print("Model loaded successfully!")


#Task 3

# Define sentences
sentences = [
    "Artificial Intelligence",
    "Machine Learning",
    "Deep Learning",
    "Python Programming"
]

# Generate embeddings
embeddings = model.encode(sentences)

# Display embeddings
for sentence, embedding in zip(sentences, embeddings):
    print("\nSentence:", sentence)
    print("Embedding:")
    print(embedding)


#Task 4

print("Comparison of Popular Embedding Models")
print("=" * 100)

print(f"{'Model':<25} {'Main Feature':<30} {'Speed':<12} {'Quality':<15} {'Suitable For'}")
print("-" * 100)

print(f"{'all-MiniLM-L6-v2':<25} {'Lightweight, general purpose':<30} {'Fast':<12} {'Good':<15} {'Semantic Search'}")
print(f"{'all-mpnet-base-v2':<25} {'High-quality embeddings':<30} {'Slower':<12} {'Very Good':<15} {'Semantic Similarity'}")
print(f"{'multi-qa-MiniLM':<25} {'Question-answer retrieval':<30} {'Fast':<12} {'Good':<15} {'RAG / Retrieval'}")


#Task 5 

print("Embedding Generation Workflow")
print("--------------------------------")
print("Sentence")
print("   ↓")
print("Sentence Transformer")
print("   ↓")
print("Embedding Vector")
print("   ↓")
print("Vector Database")
print("   ↓")
print("Similarity Search")
print("   ↓")
print("Retrieve Best Match")