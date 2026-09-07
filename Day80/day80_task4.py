# ============================================================
# DAY 80 - PRACTICAL TASK 4
# RAG Chatbot with Logging
# ============================================================

import os
import time
import logging

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

LOG_FILE = os.path.join(
    BASE_DIR,
    "chatbot.log"
)

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(CHROMA_DIR, exist_ok=True)
os.makedirs(STATIC_DIR, exist_ok=True)


# ============================================================
# CONFIGURE APPLICATION LOGGING
# ============================================================

logger = logging.getLogger("day80_task4")
logger.setLevel(logging.INFO)

# Prevent messages from going to the root logger
logger.propagate = False

# Create file handler
file_handler = logging.FileHandler(
    LOG_FILE,
    encoding="utf-8"
)

file_handler.setLevel(logging.INFO)

# Log format
formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s"
)

file_handler.setFormatter(formatter)

# Add handler only once
if not logger.handlers:
    logger.addHandler(file_handler)
logger.info("DAY 80 TASK 4 LOGGER STARTED")

# Silence noisy third-party HTTP logs
logging.getLogger("httpx").setLevel(logging.WARNING)
logging.getLogger("httpcore").setLevel(logging.WARNING)
logging.getLogger("huggingface_hub").setLevel(logging.WARNING)


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
    title="Day 80 RAG Chatbot with Logging",
    description="RAG chatbot with PDF upload, source tracking and logging",
    version="1.0"
)


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
    collection_name="day80_task4_rag",
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

    start_time = time.time()

    try:

        logger.info(
            f"PDF upload started | File: {file.filename}"
        )

        # Check PDF
        if not file.filename.lower().endswith(".pdf"):

            response_time = time.time() - start_time

            logger.error(
                f"Upload failed | File: {file.filename} | "
                f"Response Time: {response_time:.2f}s | "
                f"Status: Failure | Reason: Not a PDF"
            )

            return {
                "status": "failed",
                "message": "Only PDF files are allowed.",
                "response_time": round(
                    response_time,
                    2
                )
            }

        # Save PDF
        file_path = os.path.join(
            UPLOAD_DIR,
            file.filename
        )

        content = await file.read()

        with open(file_path, "wb") as f:
            f.write(content)

        # Load PDF
        loader = PyPDFLoader(
            file_path
        )

        documents = loader.load()

        # Split document
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=50
        )

        chunks = splitter.split_documents(
            documents
        )

        # Store embeddings
        vectorstore.add_documents(
            chunks
        )

        response_time = time.time() - start_time

        # Log successful upload
        logger.info(
            f"PDF upload successful | "
            f"File: {file.filename} | "
            f"Pages: {len(documents)} | "
            f"Chunks: {len(chunks)} | "
            f"Response Time: {response_time:.2f}s | "
            f"Status: Success"
        )

        return {
            "status": "success",
            "filename": file.filename,
            "pages": len(documents),
            "chunks": len(chunks),
            "response_time": round(response_time, 2),
            "message": "PDF uploaded successfully."
        }

    except Exception as e:

        response_time = time.time() - start_time

        logger.exception(
            f"PDF upload failed | "
            f"File: {file.filename} | "
            f"Response Time: {response_time:.2f}s | "
            f"Status: Failure | "
            f"Error: {str(e)}"
        )

        return {
            "status": "failed",
            "error": str(e),
            "response_time": round(
                response_time,
                2
            )
        }


# ============================================================
# ASK QUESTION ENDPOINT
# ============================================================

@app.post("/ask")
async def ask_question(
    question: str
):

    start_time = time.time()

    # Log user question
    logger.info(
        f"User Question: {question}"
    )

    try:

        # Retrieve top 3 chunks
        docs = vectorstore.similarity_search(
            question,
            k=3
        )

        if not docs:

            response_time = time.time() - start_time

            logger.warning(
                f"Question failed | "
                f"Response Time: {response_time:.2f}s | "
                f"Status: Failure | "
                f"Reason: No documents found"
            )

            return {
                "answer": "I don't know.",
                "sources": [],
                "response_time": round(response_time, 2),
                "status": "failure"
            }

        # Combine context
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

        # Generate response using Ollama Cloud
        response = client.chat(
            model="gpt-oss:120b",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        answer = response[
            "message"
        ][
            "content"
        ]

        # Extract source names
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

        # Calculate response time
        response_time = time.time() - start_time

        # Log success
        logger.info(
            f"Question completed | "
            f"Response Time: {response_time:.2f}s | "
            f"Status: Success"
        )

        return {
            "answer": answer,
            "sources": sources,
            "response_time": round(
                response_time,
                2
            ),
            "status": "success"
        }

    except Exception as e:

        response_time = time.time() - start_time

        # Log failure
        logger.exception(
            f"Question failed | "
            f"Response Time: {response_time:.2f}s | "
            f"Status: Failure | "
            f"Error: {str(e)}"
        )

        return {
            "answer": "An error occurred.",
            "sources": [],
            "response_time": round(
                response_time,
                2
            ),
            "status": "failure",
            "error": str(e)
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
        "message":
        "Day 80 RAG Chatbot with Logging is running.",
        "frontend":
        "http://127.0.0.1:8000/static/index.html"
    }