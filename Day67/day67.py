#Task 2

from PyPDF2 import PdfReader

# PDF file path
pdf_path = "C:\\Users\\lenovo\\Downloads\\fileViewer.pdf"

# Create PDF reader
reader = PdfReader(pdf_path)

# Store extracted text
text = ""

# Extract text from every page
for page in reader.pages:
    page_text = page.extract_text()

    if page_text:
        text += page_text + "\n"

# Print extracted text
print(text)


#Task 3

document = """
Artificial Intelligence is transforming many industries.
Machine Learning allows computers to learn patterns from data.
Natural Language Processing helps computers understand human language.
Retrieval-Augmented Generation combines document retrieval with language models.
Vector databases help store and retrieve document embeddings efficiently.
"""

# Manually divide the document into 5 chunks
chunks = [
    "Chunk 1: Artificial Intelligence is transforming many industries.",
    
    "Chunk 2: Machine Learning allows computers to learn patterns from data.",
    
    "Chunk 3: Natural Language Processing helps computers understand human language.",
    
    "Chunk 4: Retrieval-Augmented Generation combines document retrieval with language models.",
    
    "Chunk 5: Vector databases help store and retrieve document embeddings efficiently."
]

# Print the chunks
for chunk in chunks:
    print(chunk)


#Task 4

print("RAG PIPELINE")
print("    |")
print("    v")
print("Upload PDF")
print("    |")
print("    v")
print("Extract Text")
print("    |")
print("    v")
print("Split into Chunks")
print("    |")
print("    v")
print("Create Embeddings")
print("    |")
print("    v")
print("Vector Database")
print("    |")
print("    v")
print("User Question")
print("    |")
print("    v")
print("Convert Question to Embedding")
print("    |")
print("    v")
print("Similarity Search")
print("    |")
print("    v")
print("Retrieve Relevant Chunks")
print("    |")
print("    v")
print("   LLM")
print("    |")
print("    v")
print("Generate Answer")


#Task 5

print("FAISS vs ChromaDB vs Pinecone")
print("=" * 80)

print(f"{'Feature':<20} {'FAISS':<20} {'ChromaDB':<20} {'Pinecone':<20}")
print("-" * 80)

print(f"{'Type':<20} {'Vector Library':<20} {'Vector Database':<20} {'Managed Vector DB':<20}")
print(f"{'Deployment':<20} {'Local':<20} {'Local/Self-hosted':<20} {'Cloud-based':<20}")
print(f"{'Python Support':<20} {'Yes':<20} {'Yes':<20} {'Yes':<20}")
print(f"{'Ease of Use':<20} {'Moderate':<20} {'Easy':<20} {'Easy':<20}")
print(f"{'Best For':<20} {'Fast Search':<20} {'RAG Applications':<20} {'Scalable Search':<20}")
print(f"{'Internet Required':<20} {'No':<20} {'No':<20} {'Generally Yes':<20}")
print(f"{'Scalability':<20} {'Depends':<20} {'Good':<20} {'High':<20}")