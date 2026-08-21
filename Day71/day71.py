#Task 2

from langchain_community.document_loaders import PyPDFLoader

# Load the PDF
loader = PyPDFLoader(r"C:\Users\lenovo\Downloads\Categorical_Variables_Analysis_Report.pdf")

# Extract the pages
documents = loader.load()

print("PDF loaded successfully!")
print("Number of pages:", len(documents))


#Task 3

from langchain_text_splitters import RecursiveCharacterTextSplitter

# Create text splitter
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

# Split documents into chunks
chunks = splitter.split_documents(documents)
print("Number of chunks:", len(chunks))


#Task 4

# Create embeddings
from langchain_community.embeddings import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(
model_name="all-MiniLM-L6-v2"
)

# Store embeddings in ChromaDB
from langchain_community.vectorstores import Chroma

db = Chroma.from_documents(
    documents=chunks,
    embedding=embedding
)
print("Documents stored in ChromaDB successfully!")

# Similarity Search

questions = [
    "What percentage of applicants have completed the deposit process and what percentage have not?",
    "What does the cross-tabulation of Deposit Status and I-20 Status reveal about applicant progression?",
    "What are the major demographic and academic characteristics of the SEVIS student population?"
]

for question in questions:

    print("\n===================================")
    print("Question:", question)
    print("===================================")

    docs = db.similarity_search(
        question,
        k=3
    )

    print("\nRelevant information:")

    for i, doc in enumerate(docs):
        print(f"\n--- Result {i + 1} ---")
        print(doc.page_content)


#Task 5

print("""
========================================================
       PDF QUESTION ANSWERING CHATBOT ARCHITECTURE
========================================================

                   
              +-------------------+
              |    Upload PDF     |
              +-------------------+
                        |
                        v
              +-------------------+
              |     Load PDF      |
              |   PyPDFLoader     |
              +-------------------+
                        |
                        v
              +-------------------+
              |   Text Chunking   |
              |  Chunk Size: 500  |
              |  Overlap: 50      |
              +-------------------+
                        |
                        v
              +-------------------+
              |    Embeddings     |
              | Sentence          |
              | Transformer       |
              +-------------------+
                        |
                        v
              +-------------------+
              |     ChromaDB      |
              |  Vector Database  |
              +-------------------+
                        |
                        |
                        |
              +-------------------+
              |   User Question   |
              +-------------------+
                        |
                        v
              +-------------------+
              | Question          |
              | Embedding         |
              +-------------------+
                        |
                        v
              +-------------------+
              | Similarity Search |
              +-------------------+
                        |
                        v
              +-------------------+
              | Retrieve Best     |
              | Chunks            |
              +-------------------+
                        |
                        v
              +-------------------+
              |    OpenAI / LLM   |
              |    Response       |
              +-------------------+
                        |
                        v
              +-------------------+
              |    Final Answer   |
              +-------------------+

========================================================
""")
