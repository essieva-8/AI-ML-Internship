# ============================================================
# DAY 80 - PRACTICAL TASK 2
# Upload PDF and store embeddings in ChromaDB
# ============================================================

import os

from fastapi import FastAPI, UploadFile, File

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma


# ============================================================
# CREATE FASTAPI APPLICATION
# ============================================================

app = FastAPI(
    title="RAG Document Upload API",
    description="Upload PDF documents and store embeddings in ChromaDB",
    version="1.0"
)


# ============================================================
# CREATE DIRECTORIES
# ============================================================

BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

UPLOAD_DIR = os.path.join(
    BASE_DIR,
    "uploaded_pdfs"
)

CHROMA_DIR = os.path.join(
    BASE_DIR,
    "chroma_db"
)

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(CHROMA_DIR, exist_ok=True)


# ============================================================
# CREATE EMBEDDING MODEL
# ============================================================

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


# ============================================================
# CREATE CHROMADB VECTOR STORE
# ============================================================

vectorstore = Chroma(
    collection_name="day80_documents",
    embedding_function=embeddings,
    persist_directory=CHROMA_DIR
)


# ============================================================
# PDF UPLOAD ENDPOINT
# ============================================================

@app.post("/upload")
async def upload_pdf(
    file: UploadFile = File(...)
):

    # Check file extension
    if not file.filename.lower().endswith(".pdf"):

        return {
            "status": "failed",
            "message": "Only PDF files are allowed."
        }

    # Create file path
    file_path = os.path.join(
        UPLOAD_DIR,
        file.filename
    )

    # Read uploaded file
    content = await file.read()

    # Save PDF
    with open(file_path, "wb") as f:
        f.write(content)

    # ========================================================
    # LOAD PDF
    # ========================================================

    loader = PyPDFLoader(file_path)

    documents = loader.load()

    # ========================================================
    # SPLIT DOCUMENT INTO CHUNKS
    # ========================================================

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    chunks = text_splitter.split_documents(
        documents
    )

    # ========================================================
    # STORE CHUNKS AND EMBEDDINGS
    # ========================================================

    vectorstore.add_documents(
        chunks
    )

    # ========================================================
    # RETURN RESPONSE
    # ========================================================

    return {
        "status": "success",
        "filename": file.filename,
        "pages": len(documents),
        "chunks": len(chunks),
        "message": "PDF uploaded and embeddings stored successfully."
    }


# ============================================================
# ROOT ENDPOINT
# ============================================================

@app.get("/")
def home():

    return {
        "message": "PDF RAG API is running"
    }