#Task 1

import os
import pandas as pd

from dotenv import load_dotenv

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_ollama import ChatOllama

# LOAD OLLAMA CLOUD API KEY
load_dotenv()

OLLAMA_API_KEY = os.getenv("OLLAMA_API_KEY")

if not OLLAMA_API_KEY:
    raise ValueError(
        "OLLAMA_API_KEY not found. "
        "Please set your Ollama Cloud API key."
    )

print("Ollama Cloud API key loaded successfully.")

# PATH TO YOuR DOCUMENTS
folder_path = r"D:\AI&ML Intern\AI-ML-Internship\Day79\Documents"

# FIND ALL PDF DOCUMENTS
pdf_files = [
    os.path.join(folder_path, file)
    for file in os.listdir(folder_path)
    if file.lower().endswith(".pdf")
]

print("\nDocuments found:")

for file in pdf_files:
    print("-", os.path.basename(file))

# LOAD ALL PDF DOCUMENTS
documents = []

for pdf_file in pdf_files:

    loader = PyPDFLoader(pdf_file)

    pdf_documents = loader.load()

    # Add source filename to metadata
    for doc in pdf_documents:
        doc.metadata["source_file"] = os.path.basename(pdf_file)

    documents.extend(pdf_documents)


print("\nTotal pages loaded:", len(documents))

# SPLIT DOCUMENTS INTO CHUNKS
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks = text_splitter.split_documents(documents)

print("Total chunks created:", len(chunks))

# CREATE EMBEDDINGS
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

print("Embedding model loaded.")

# CREATE CHROMA VECTOR STORE
vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    collection_name="day79_rag_collection"
)

print("Chroma vector store created.")

# CREATE RETRIEVER
retriever = vectorstore.as_retriever(
    search_kwargs={"k": 3}
)

print("Retriever created.")

# CONNECT TO OLLAMA CLOUD
llm = ChatOllama(
    model="gpt-oss:20b-cloud",
    base_url="https://ollama.com", 
    headers={ 
        "Authorization": f"Bearer {OLLAMA_API_KEY}" 
    }, 
    temperature=0 
) 
 
print("Ollama Cloud LLM configured.") 
 
# RAG FUNCTION 
def ask_rag(question): 
 
    # Retrieve relevant chunks 
    retrieved_docs = retriever.invoke(question) 
 
    # Combine retrieved context 
    context = "\n\n".join( 
        [ 
            f"Source: {doc.metadata.get('source_file', 'Unknown')}\n" 
            f"Page: {doc.metadata.get('page', 'Unknown')}\n" 
            f"{doc.page_content}" 
            for doc in retrieved_docs 
        ] 
    ) 
 
    # RAG prompt 
    prompt = f""" 
You are a helpful document-based question answering assistant. 
 
Answer the question ONLY using the provided context. 
 
If the answer cannot be found in the context, 
say: 
 
"I could not find the answer in the provided documents." 
 
Do not invent or add information that is not supported 
by the retrieved documents. 
 
Always mention the source document when possible. 
 
CONTEXT: 
{context} 
 
QUESTION: 
{question} 
 
ANSWER: 
""" 
 
    # Generate answer 
    response = llm.invoke(prompt) 
 
    return response.content, retrieved_docs 
 
# TEN QUESTIONS FOR RAG EVALUATION 
questions = [ 
    "What is the internship duration?", 
    "What are the office timings?", 
    "How many casual leaves are allowed?", 
    "What are the company policies?", 
    "What are the rules mentioned in the handbook?", 
    "Who is the designated HR contact?", 
    "Is there a dress code?", 
    "What is the policy for sick leave?", 
    "Are interns eligible for holiday pay?", 
    "What are the standard working hours?" 
] 
 
# STORE EVALUATION RESULTS 
results = [] 
 
# TEST ALL 10 QUESTIONS 
for i, question in enumerate(questions, start=1): 
 
    print("\n" + "=" * 80) 
    print(f"QUESTION {i}") 
    print("=" * 80) 
 
    print(question) 
 
    # Ask the RAG chatbot 
    answer, retrieved_docs = ask_rag(question) 
  
    # Display retrieved documents 
    print("\nRETRIEVED DOCUMENTS") 
    print("-" * 80) 
 
    for j, doc in enumerate(retrieved_docs, start=1): 
 
        source = doc.metadata.get( 
            "source_file", 
            "Unknown" 
        ) 
 
        page = doc.metadata.get( 
            "page", 
            "Unknown" 
        ) 
 
        print( 
            f"{j}. Source: {source} | Page: {page}" 
        ) 
 
    # Display final answer 
    print("\nFINAL ANSWER") 
    print("-" * 80) 
 
    print(answer) 
 
     
    # Manual evaluation
    relevant = input( 
        "\nAre the retrieved documents relevant " 
        "to the question? (Yes/No): " 
    ) 
 
    correct = input( 
        "Is the answer correct? (Yes/No): " 
    ) 
 
    hallucination = input( 
        "Does the answer contain hallucinated " 
        "information? (Yes/No): " 
    ) 
 
    faithful = input( 
        "Is the answer faithful to the retrieved " 
        "documents? (Yes/No): " 
    ) 
  
    # Store results 
    results.append({ 
 
        "Question": question, 
 
        "Retrieved Documents": len(retrieved_docs), 

        "Relevant Documents?": relevant,
 
        "Correct Answer?": correct, 
 
        "Hallucination?": hallucination, 
 
        "Faithful?": faithful 
    }) 
 

# Task 2 

# CREATE FINAL EVALUATION TABLE 
evaluation_table = pd.DataFrame(results) 

evaluation_table = evaluation_table[
    [
        "Question",
        "Retrieved Documents",
        "Correct Answer?",
        "Hallucination?",
        "Faithful?"
    ]
]
 
# DISPLAY FINAL EVALUATION TABLE 
print("\n\n" + "=" * 110) 
print("RAG EVALUATION TABLE") 
print("=" * 110) 
 
print( 
    evaluation_table.to_string(index=False) 
) 
 

#Task 3

print("\n\n" + "=" * 80)
print("TASK 3 - HALLUCINATION TEST")
print("=" * 80)

# Intentionally ask a question that is not in the documents
test_question = "What is the company's policy on international business class travel?"

# Ask the RAG chatbot
answer, retrieved_docs = ask_rag(test_question)

# Display question
print("\nTEST QUESTION")
print("-" * 80)
print(test_question)

# Display retrieved documents
print("\nRETRIEVED DOCUMENTS")
print("-" * 80)

for i, doc in enumerate(retrieved_docs, start=1):

    source = doc.metadata.get(
        "source_file",
        "Unknown"
    )

    page = doc.metadata.get(
        "page",
        "Unknown"
    )

    print(
        f"{i}. Source: {source} | Page: {page}"
    )

# Display chatbot response
print("\nCHATBOT RESPONSE")
print("-" * 80)

print(answer)

# Observe whether the chatbot knows or hallucinates
print("\nOBSERVATION")
print("-" * 80)

if (
    "I could not find the answer in the provided documents."
    in answer
):
    print("Result: The chatbot correctly said it does not know.")
else:
    print("Result: The chatbot may have hallucinated an answer.")


#Task 4

# COMPARE TOP-1, TOP-3 AND TOP-5 RETRIEVAL
print("\n\n" + "=" * 80)
print("TASK 4 - RETRIEVAL COMPARISON")
print("=" * 80)

# Test question
test_question = "What are the standard working hours?"

def test_retrieval(k):

    # Retrieve top-k documents
    docs = vectorstore.similarity_search(
        test_question,
        k=k
    )

    # Create context
    context = "\n\n".join(
        [
            f"Source: {doc.metadata.get('source_file', 'Unknown')}\n"
            f"Page: {doc.metadata.get('page', 'Unknown')}\n"
            f"{doc.page_content}"
            for doc in docs
        ]
    )

    # Prompt
    prompt = f"""
You are a document-based question answering assistant.

Answer the question ONLY using the provided context.

If the answer cannot be found in the context, say:

"I could not find the answer in the provided documents."

Do not invent information.

CONTEXT:
{context}

QUESTION:
{test_question}

ANSWER:
"""

    # Generate answer
    response = llm.invoke(prompt)

    return docs, response.content

# ============================================================
# TOP-1 RETRIEVAL
# ============================================================

docs_1, answer_1 = test_retrieval(1)

print("\n" + "=" * 80)
print("TOP-1 RESULT")
print("=" * 80)

print("\nRetrieved Documents:", len(docs_1))
print("\nAnswer:")
print(answer_1)

# ============================================================
# TOP-3 RETRIEVAL
# ============================================================

docs_3, answer_3 = test_retrieval(3)

print("\n" + "=" * 80)
print("TOP-3 RESULTS")
print("=" * 80)

print("\nRetrieved Documents:", len(docs_3))
print("\nAnswer:")
print(answer_3)

# ============================================================
# TOP-5 RETRIEVAL
# ============================================================

docs_5, answer_5 = test_retrieval(5)

print("\n" + "=" * 80)
print("TOP-5 RESULTS")
print("=" * 80)

print("\nRetrieved Documents:", len(docs_5))
print("\nAnswer:")
print(answer_5)

# OBSERVATIONS
print("\n\n" + "=" * 80)
print("OBSERVATIONS")
print("=" * 80)

print("""
Top-1:
Retrieves only the most relevant document chunk.
The answer may be concise, but important information may be missed.

Top-3:
Retrieves three relevant chunks and provides more context.
This generally improves answer completeness and reliability.

Top-5:
Retrieves five chunks and provides the largest amount of context.
It may improve completeness, but irrelevant information can sometimes
be included and may make the context less focused.

Overall:
Top-1 is focused but may miss information.
Top-3 usually provides a good balance between relevance and context.
Top-5 provides more context but may introduce unnecessary information.
""")


#Task 5

print("""Ragas is a framework designed for evaluating RAG pipelines.

Features
Evaluates RAG system performance.
Supports evaluation of retrieval quality.
Can evaluate generated answers.
Provides metrics for assessing different components of a RAG pipeline.
Helps identify weaknesses in retrieval and generation.

Advantages
Helps automate RAG evaluation.
Reduces the amount of manual evaluation required.
Helps identify retrieval problems.
Helps detect problems with generated answers.
Supports systematic comparison of RAG systems.
Use Cases

Ragas can be used for:

Evaluating RAG chatbots.
Testing document retrieval.
Comparing different retrieval configurations.
Evaluating generated answers.
Monitoring improvements to RAG pipelines.""")