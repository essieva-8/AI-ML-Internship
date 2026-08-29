#Task 2

# Load all PDF documents from a folder
import os
from langchain_community.document_loaders import PyPDFLoader

folder = r"D:\AI&ML Intern\AI-ML-Internship\Day76\Documents"

documents = []

for file in os.listdir(folder):

    if file.endswith(".pdf"):

        file_path = os.path.join(folder, file)

        loader = PyPDFLoader(file_path)

        loaded_pages = loader.load()

        documents.extend(loaded_pages)

        print(f"Loaded: {file}")
        print(f"Pages: {len(loaded_pages)}")
        print("-" * 40)

print(f"Total pages loaded: {len(documents)}")


#Task 3

# Split documents and generate embeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings

# Text splitter
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)

# Split all loaded documents
chunks = splitter.split_documents(documents)

print("Total documents/pages:", len(documents))
print("Total chunks:", len(chunks))

# Create embeddings
embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

print("Embedding model loaded successfully.")

# Generate an embedding for the first chunk
vector = embedding.embed_query(chunks[0].page_content)

print("Embedding dimension:", len(vector))


#Task 4

# Store chunks in ChromaDB and create a retriever
from langchain_chroma import Chroma

# Create ChromaDB
vector_db = Chroma.from_documents(
    documents=chunks,
    embedding=embedding,
    persist_directory="./chroma_db"
)

print("Documents stored in ChromaDB successfully.")

# Create retriever
retriever = vector_db.as_retriever(
    search_kwargs={"k": 4}
)

print("Retriever created successfully.")


#Task 5

# Query multiple PDFs and display the sources
questions = [
    "What is the internship duration?",
    "What are the office timings?",
    "How many casual leaves are allowed?",
    "What are the company policies?",
    "What are the rules mentioned in the handbook?"
]

for question in questions:

    print("\n" + "=" * 70)
    print("QUESTION:", question)
    print("=" * 70)

    results = retriever.invoke(question)

    for i, doc in enumerate(results, start=1):

        print(f"\nResult {i}")
        print("Source:", doc.metadata.get("source"))
        print("Page:", doc.metadata.get("page", "Unknown"))
        print("Content:")
        print(doc.page_content[:500])