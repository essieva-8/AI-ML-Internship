# ============================================================
# DAY 80 - PRACTICAL TASK 1
# FastAPI endpoint for asking questions
# ============================================================

from fastapi import FastAPI
from pydantic import BaseModel
from langchain_ollama import OllamaLLM


# ============================================================
# CREATE FASTAPI APPLICATION
# ============================================================

app = FastAPI(
    title="RAG Chatbot API",
    description="FastAPI endpoint for asking questions",
    version="1.0"
)


# ============================================================
# INITIALIZE LLM
# ============================================================

llm = OllamaLLM(
    model="llama3.2"
)


# ============================================================
# REQUEST MODEL
# ============================================================

class QuestionRequest(BaseModel):
    question: str


# ============================================================
# ASK ENDPOINT
# ============================================================

@app.post("/ask")
def ask_question(request: QuestionRequest):

    question = request.question

    # Generate AI answer
    answer = llm.invoke(question)

    return {
        "question": question,
        "answer": answer
    }


# ============================================================
# ROOT ENDPOINT
# ============================================================

@app.get("/")
def home():

    return {
        "message": "RAG Chatbot API is running"
    }

