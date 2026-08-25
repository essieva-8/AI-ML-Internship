#Task 2

from langchain_community.document_loaders import PyPDFLoader

# Load the PDF
loader = PyPDFLoader("C:\\Users\\lenovo\\Downloads\\Categorical_Variables_Analysis_Report.pdf")

# Load all pages
documents = loader.load()

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

# Display number of chunks
print("Number of chunks:", len(chunks))


#Task 4

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

# Create embeddings
embedding = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

print("Embeddings created successfully.")

# Store in ChromaDB
vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embedding
)

print("Chunks stored in ChromaDB.")

# Create retriever
retriever = vectorstore.as_retriever(
    search_kwargs={"k": 3}
)

print("Retriever created successfully.")


#Task 5

questions = [
    "What percentage of applicants have completed the deposit process and what percentage have not?",
    "What does the cross-tabulation of Deposit Status and I-20 Status reveal about applicant progression?",
    "What are the major demographic and academic characteristics of the SEVIS student population?",
    "What does the gender distribution indicate about the SEVIS student population?",
    "Which countries of citizenship and academic majors are most represented in the SEVIS dataset?"
]

# Retrieve top 3 chunks
for i, question in enumerate(questions, start=1):

    print("\n" + "=" * 60)
    print("Question", i, ":", question)
    print("=" * 60)

    docs = retriever.invoke(question)

    for j, doc in enumerate(docs, start=1):

        print("\nTop Chunk", j)
        print("-" * 40)
        print(doc.page_content)