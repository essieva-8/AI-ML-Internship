#Task 1

from langchain_core.documents import Document

# Creating five sample documents

documents = [

    Document(
        page_content="Employees are entitled to 20 days of annual leave.",
        metadata={
            "filename": "HR_Policy.pdf",
            "page": 5,
            "department": "HR"
        }
    ),

    Document(
        page_content="Employees must submit leave requests through the HR portal.",
        metadata={
            "filename": "Employee_Handbook.pdf",
            "page": 12,
            "department": "HR"
        }
    ),

    Document(
        page_content="The company prepares its financial reports at the end of every quarter.",
        metadata={
            "filename": "Finance_Guide.pdf",
            "page": 8,
            "department": "Finance"
        }
    ),

    Document(
        page_content="All employees must follow workplace safety guidelines.",
        metadata={
            "filename": "Safety_Manual.pdf",
            "page": 15,
            "department": "Medical"
        }
    ),

    Document(
        page_content="All company contracts must be reviewed before approval.",
        metadata={
            "filename": "Legal_Policy.pdf",
            "page": 20,
            "department": "Legal"
        }
    )
]

print("Number of documents:", len(documents))


#Task 2

from langchain_chroma import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

# Create embedding model

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Create ChromaDB vector store

vector_db = Chroma.from_documents(
    documents=documents,
    embedding=embeddings,
    collection_name="day77_metadata_rag"
)

print("Documents successfully stored in ChromaDB.")


#Task 3

query = "What is the leave policy?"

results = vector_db.similarity_search(
    query,
    k=5,
    filter={
        "department": "HR"
    }
)

print("HR Documents Retrieved:")
print("-" * 50)

for i, doc in enumerate(results, start=1):

    print(f"\nResult {i}")
    print("Content:", doc.page_content)
    print("Filename:", doc.metadata["filename"])
    print("Page:", doc.metadata["page"])
    print("Department:", doc.metadata["department"])


#Task 4

# Retrieve relevant document

results = vector_db.similarity_search(
    query,
    k=1,
    filter={
        "department": "HR"
    }
)

if results:

    doc = results[0]

    print("Answer:")
    print(doc.page_content)

    print("\nSource:")
    print("File:", doc.metadata["filename"])
    print("Page:", doc.metadata["page"])

else:

    print("No relevant information found.")


#Task 5

#Retrieval Without Metadata Filtering
query = "What is the leave policy?"

results_without_filter = vector_db.similarity_search(
    query,
    k=5
)

print("Retrieval WITHOUT Metadata Filtering")
print("=" * 50)

for i, doc in enumerate(results_without_filter, start=1):

    print(f"\nResult {i}")
    print("Content:", doc.page_content)
    print("Filename:", doc.metadata["filename"])
    print("Department:", doc.metadata["department"])
    print("Page:", doc.metadata["page"])

#Retrieval With Metadata Filtering
query = "What is the leave policy?"

results_with_filter = vector_db.similarity_search(
    query,
    k=5,
    filter={
        "department": "HR"
    }
)

print("Retrieval WITH Metadata Filtering")
print("=" * 50)

for i, doc in enumerate(results_with_filter, start=1):

    print(f"\nResult {i}")
    print("Content:", doc.page_content)
    print("Filename:", doc.metadata["filename"])
    print("Department:", doc.metadata["department"])
    print("Page:", doc.metadata["page"])


print("Without metadata filtering, the vector database searches across all available documents. This can result in irrelevant documents being considered.")
print("With metadata filtering, the search is restricted to documents whose metadata matches the specified condition.")
