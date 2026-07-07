# 🚀 Enterprise Multi-Document RAG AI Assistant

> A production-ready Retrieval-Augmented Generation (RAG) AI Assistant capable of answering questions from multiple uploaded PDF documents using Google's Gemini, ChromaDB, FastAPI, and Streamlit.

---

## 📌 Overview

Enterprise Multi-Document RAG AI Assistant is an end-to-end AI application that enables users to upload multiple PDF documents and ask natural language questions based on their contents.

The application retrieves the most relevant document chunks using semantic search, builds contextual prompts, and generates accurate answers using Google Gemini.

The project follows a production-ready architecture with a separate frontend and backend, Docker support, modular components, analytics, and enterprise-grade organization.

---

# ✨ Features

### 📄 Document Management
- Upload multiple PDF documents
- Automatic text extraction
- Intelligent document chunking
- Metadata generation
- Duplicate document detection

### 🧠 Retrieval-Augmented Generation (RAG)
- Semantic search using ChromaDB
- Gemini Embeddings
- Context Builder
- Confidence Scoring
- Source Citations

### 💬 AI Chat
- Natural language conversation
- Multi-document question answering
- Context-aware responses
- Chat history
- Conversation memory

### ⚙ Backend
- FastAPI REST APIs
- Swagger Documentation
- Health Check API
- Document APIs
- Chat API
- Upload API

### 📊 Analytics
- Document Statistics
- Query Logger
- Feedback System
- Query Cache
- Chat Export

### 🐳 DevOps
- Docker Support
- Docker Compose
- Environment Configuration
- Modular Project Structure

---

# 🏗 System Architecture

```
                    Browser
                       │
        ┌──────────────┴──────────────┐
        │                             │
        ▼                             ▼
 Streamlit Frontend            Swagger UI
        │
        ▼
      API Client
        │
 REST API (HTTP)
        ▼
     FastAPI Backend
        │
        ▼
      RAG Pipeline
        │
 ┌──────┴─────────┐
 │                │
 ▼                ▼
Retriever     Context Builder
 │                │
 ▼                ▼
ChromaDB      Gemini LLM
 │
 ▼
Embeddings
```

---

# 🛠 Tech Stack

## Programming Language

- Python 3.12

## Frontend

- Streamlit

## Backend

- FastAPI
- Uvicorn

## AI

- Google Gemini
- Gemini Embeddings

## Vector Database

- ChromaDB

## Document Processing

- PyPDF
- LangChain Text Splitters

## Data

- Pandas
- NumPy

## Logging

- Loguru

## Deployment

- Docker
- Docker Compose

---

# 📂 Project Structure

```
Enterprise Multi-Document-RAG-AI-Assistant

├── api/
├── analytics/
├── backend/
│   ├── routers/
│   ├── schemas/
│   └── main.py
│
├── cache/
├── chroma_db/
├── config/
├── data/
├── document/
├── embeddings/
├── evaluation/
├── export/
├── feedback/
├── ingestion/
├── llm/
├── memory/
├── prompts/
├── retriever/
├── services/
├── tests/
├── ui/
├── utils/
├── vectorstore/
│
├── app.py
├── requirements.txt
├── Dockerfile.backend
├── Dockerfile.frontend
├── docker-compose.yml
└── README.md
```

---

# ⚙ Installation

## Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/Enterprise-Multi-Document-RAG-AI-Assistant.git

cd Enterprise-Multi-Document-RAG-AI-Assistant
```

---

## Create Virtual Environment

```bash
python -m venv .venv
```

Activate

### macOS/Linux

```bash
source .venv/bin/activate
```

### Windows

```bash
.venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Environment

Create a `.env` file.

```
GOOGLE_API_KEY=YOUR_API_KEY

GENERATION_MODEL=gemini-2.5-flash

EMBEDDING_MODEL=gemini-embedding-001

CHROMA_DB=chroma_db

DATA_FOLDER=data

TOP_K=5
```

---

# ▶ Run Locally

## Backend

```bash
uvicorn backend.main:app --reload
```

Backend

```
http://127.0.0.1:8000
```

Swagger

```
http://127.0.0.1:8000/docs
```

---

## Frontend

```bash
streamlit run app.py
```

```
http://localhost:8501
```

---

# 🐳 Docker

Build

```bash
docker compose build --no-cache
```

Run

```bash
docker compose up
```

Frontend

```
http://localhost:8501
```

Backend

```
http://localhost:8000/docs
```

---

# 📡 REST APIs

## Health

```
GET /health/
```

---

## Upload

```
POST /upload/
```

---

## Chat

```
POST /chat/
```

---

## Documents

```
GET /documents/
```

---

## Statistics

```
GET /documents/stats
```

---

# 📸 Screenshots

## Streamlit Dashboard

> *(Add screenshot here)*

---

## Chat Interface

> *(Add screenshot here)*

---

## Swagger Documentation

> *(Add screenshot here)*

---

# 🚀 Future Enhancements

- Hybrid Search (Vector + BM25)
- Cross Encoder Re-ranking
- OCR Support
- DOCX Support
- Excel Support
- Multi-modal Documents
- JWT Authentication
- User Login
- Role-based Access
- AWS Deployment
- CI/CD Pipeline
- Monitoring Dashboard
- RAG Evaluation (RAGAS)

---

# 👨‍💻 Author

**Chandni Pradhan**

AI Engineer | Machine Learning Engineer | Generative AI Developer

GitHub:
https://github.com/mlexpnew

LinkedIn:
https://www.linkedin.com/in/chandni-pradhan-67aa91324/

---

# 📄 License

This project is licensed under the MIT License.

---

# ⭐ If you like this project

Please consider giving it a ⭐ on GitHub.