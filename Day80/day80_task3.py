# ============================================================
# DAY 80 - PRACTICAL TASK 3
# RAG Chatbot with HTML Frontend
# ============================================================

import os

from dotenv import load_dotenv

from fastapi import FastAPI, UploadFile, File
from fastapi.staticfiles import StaticFiles

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

from ollama import Client


# ============================================================
# LOAD ENVIRONMENT VARIABLES
# ============================================================

load_dotenv()

OLLAMA_API_KEY = os.getenv(
    "OLLAMA_API_KEY"
)


# ============================================================
# OLLAMA CLOUD CLIENT
# ============================================================

client = Client(
    host="https://ollama.com",
    headers={
        "Authorization": f"Bearer {OLLAMA_API_KEY}"
    }
)


# ============================================================
# FASTAPI APPLICATION
# ============================================================

app = FastAPI(
    title="Day 80 RAG Chatbot",
    description="RAG chatbot with PDF upload and HTML frontend",
    version="1.0"
)


# ============================================================
# DIRECTORIES
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

STATIC_DIR = os.path.join(
    BASE_DIR,
    "static"
)

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(CHROMA_DIR, exist_ok=True)
os.makedirs(STATIC_DIR, exist_ok=True)


# ============================================================
# EMBEDDINGS
# ============================================================

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


# ============================================================
# CHROMADB
# ============================================================

vectorstore = Chroma(
    collection_name="day80_task3_rag",
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

    if not file.filename.lower().endswith(".pdf"):

        return {
            "status": "failed",
            "message": "Please upload a PDF file."
        }

    file_path = os.path.join(
        UPLOAD_DIR,
        file.filename
    )

    content = await file.read()

    with open(file_path, "wb") as f:
        f.write(content)

    # Load PDF
    loader = PyPDFLoader(file_path)

    documents = loader.load()

    # Split text
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    chunks = splitter.split_documents(
        documents
    )

    # Store chunks and embeddings
    vectorstore.add_documents(
        chunks
    )

    return {
        "status": "success",
        "filename": file.filename,
        "pages": len(documents),
        "chunks": len(chunks),
        "message": "PDF uploaded successfully."
    }


# ============================================================
# ASK QUESTION ENDPOINT
# ============================================================

@app.post("/ask")
async def ask_question(
    question: str
):

    # Retrieve top 3 relevant chunks
    docs = vectorstore.similarity_search(
        question,
        k=3
    )

    if not docs:

        return {
            "answer": "I don't know.",
            "sources": []
        }

    # Combine retrieved context
    context = "\n\n".join(
        doc.page_content
        for doc in docs
    )

    # RAG prompt
    prompt = f"""
You are a helpful RAG chatbot.

Answer the question using ONLY the context
provided below.

If the answer cannot be found in the context,
say exactly:

"I don't know."

Context:
{context}

Question:
{question}

Answer:
"""

    # Generate answer using Ollama Cloud
    response = client.chat(
        model="gpt-oss:120b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    answer = response["message"]["content"]

    # Extract source document names
    sources = list(
        set(
            os.path.basename(
                doc.metadata.get(
                    "source",
                    "Unknown"
                )
            )
            for doc in docs
        )
    )

    return {
        "answer": answer,
        "sources": sources
    }


# ============================================================
# STATIC FRONTEND
# ============================================================

app.mount(
    "/static",
    StaticFiles(
        directory=STATIC_DIR
    ),
    name="static"
)


# ============================================================
# ROOT ENDPOINT
# ============================================================

@app.get("/")
def home():

    return {
        "message": "Day 80 RAG Chatbot is running.",
        "frontend": "http://127.0.0.1:8000/static/index.html"
    }