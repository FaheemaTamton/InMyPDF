#  InMyPDF – Agentic Multimodal RAG System

InMyPDF is an AI-powered Agentic Retrieval-Augmented Generation (RAG) system designed to intelligently understand and query PDF documents using multimodal ingestion pipelines, vector search, and LLM-powered reasoning.

The platform processes text, tables, and image-based content from PDFs, converts them into vector embeddings, and enables users to ask natural language questions through an intelligent AI agent interface.

Built using FastAPI, LangChain, FAISS, Sentence Transformers, OpenAI models, and multimodal document ingestion pipelines.

---
#  Features

##  Multimodal PDF Understanding
- Extracts:
  - Plain text
  - Tables
  - Image-based text
- Supports intelligent document parsing
- Handles complex PDF structures



##  Agentic RAG Pipeline
- Retrieval-Augmented Generation workflow
- Intelligent reasoning agent using LangChain
- Context-aware question answering
- Dynamic retrieval orchestration

##  Vector Search System
- Semantic document chunking
- Embedding generation using Sentence Transformers
- Fast similarity search using FAISS
- Context retrieval optimization

##  OCR + Image Extraction
- Image text extraction using Tesseract OCR
- PDF image region processing
- Hybrid multimodal ingestion pipeline

##  Interactive Web Interface
- Upload PDFs directly through browser
- Ask natural language questions
- Real-time AI-generated responses
- Simple and clean frontend UI

---

#  System Workflow

```text
PDF Upload
     ↓
Multimodal Ingestion Pipeline
     ↓
Text Extraction
Table Extraction
Image OCR Extraction
     ↓
Combined Document Context
     ↓
Text Chunking
     ↓
Vector Embedding Generation
     ↓
FAISS Vector Storage
     ↓
Agentic Retrieval Pipeline
     ↓
LLM Reasoning & Response Generation
```

---

#  AI Architecture

InMyPDF combines multiple AI and NLP components into a unified Agentic RAG pipeline.

The system:
1. Extracts multimodal document content
2. Splits documents into semantic chunks
3. Converts chunks into vector embeddings
4. Stores vectors in FAISS
5. Uses retrieval tools with LangChain agents
6. Generates grounded answers using LLMs

This architecture enables:
- Context-aware querying
- Intelligent document understanding
- Semantic retrieval
- AI-assisted reasoning

---

#  Tech Stack

## Frontend
- HTML
- CSS
- JavaScript
- Bootstrap

## Backend
- FastAPI
- Python

## AI / ML
- LangChain
- OpenAI
- Sentence Transformers
- FAISS
- Agentic RAG
- OCR (Tesseract)

## Document Processing
- PyPDF
- PDFPlumber

---

#  Project Structure

```bash
InMyPDF/
│
├── agent/
│   ├── agent.py
│   └── tools.py
│
├── api/
│   └── main.py
│
├── ingestion/
│   ├── text_ingest.py
│   ├── table_ingest.py
│   └── image_ingest.py
│
├── rag/
│   ├── pipeline.py
│   ├── vector_store.py
│   ├── text_splitter.py
│   └── llm.py
│
├── static/
│   └── js/
│
├── templates/
│   └── index.html
│
├── requirements.txt
└── docker-compose.yml
```

---

#  Core Functionalities

## 📌 PDF Ingestion
- Upload PDF files
- Automatic multimodal extraction
- Text + image + table understanding

## 📌 Semantic Retrieval
- Vector similarity search
- Relevant chunk retrieval
- Context-aware querying

## 📌 Agentic Reasoning
- AI agent orchestration
- Retrieval tool integration
- LLM-powered grounded responses

## 📌 Interactive Querying
- Ask questions in natural language
- Real-time response generation
- Browser-based interaction

---

#  Retrieval-Augmented Generation (RAG)

The system uses a RAG pipeline to:
- Reduce hallucinations
- Improve factual grounding
- Retrieve only relevant document context
- Generate context-aware answers

Unlike traditional chatbots, InMyPDF answers questions based on uploaded documents instead of general internet knowledge.


---


#  Project Goals

InMyPDF aims to simplify document understanding through Agentic AI systems and Retrieval-Augmented Generation architectures.

The project focuses on:
- Intelligent document querying
- Multimodal AI systems
- Agentic workflows
- Semantic retrieval systems
- Human-AI interaction


---

#  Developer

**Faheema Tamton**

AI & ML Engineer
Focused on AI systems, RAG architectures, multimodal AI, and intelligent healthcare technologies.

🔗 Portfolio


---

#  License

This project is developed for educational  purposes.
