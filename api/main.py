from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import os

from rag.pipeline import process_pdf, answer_query

app = FastAPI(title="Agentic RAG API")

# -------- FIX PATHS PROPERLY -------- #

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

STATIC_DIR = os.path.join(BASE_DIR, "static")
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")

# ------------------------------------ #

# Allow frontend / testing tools
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)




@app.post("/api/upload")
async def ingest_pdf(file: UploadFile = File(...)):
    global VECTOR_STORE

    if not file.filename.endswith(".pdf"):
        return {"success": False, "message": "Only PDF files are supported"}

    VECTOR_STORE = process_pdf(file.file)

    if VECTOR_STORE is None:
        return {"success": False, "message": "Failed to process PDF"}

    return {"success": True, "message": "PDF ingested successfully"}


@app.post("/api/ask")
async def query_rag(question: str = File(...)):
    if VECTOR_STORE is None:
        return {"answer": "No document ingested yet"}

    answer = answer_query(VECTOR_STORE, question)
    return {"answer": answer}
