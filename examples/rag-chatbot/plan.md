# Plan: RAG Chatbot API

## Overview
A Python API for uploading PDFs and asking questions answered from the document content. FastAPI + PostgreSQL/pgvector + OpenAI.
Spec: `docs/rag-chatbot/spec.md`

---

## Phase 1: Foundation
**Goal:** The app starts, connects to the database, and responds to a health check.

### Task 1: Project skeleton and database connection
**Context:** A Python RAG chatbot API using FastAPI and PostgreSQL with pgvector. Uses UV for package management. This task sets up the foundation — a running app with an async database connection and the pgvector extension enabled.
**Acceptance Criteria:**
1. Initialize the project with UV and add dependencies (fastapi, uvicorn, sqlalchemy async, asyncpg, pgvector, pydantic-settings)
2. Create the FastAPI app with a health check endpoint
3. Set up SQLAlchemy async engine configured via environment variables
4. Create Docker Compose with the API + PostgreSQL (pgvector enabled)
**Verify:** `docker compose up`, then `curl http://localhost:8000/health` returns `{"status": "ok"}`

---

## Phase 2: Document Management
**Goal:** PDFs can be uploaded, chunked, embedded, stored, listed, and deleted.

### Task 2: Document models and ingestion endpoint
**Context:** A RAG chatbot API that stores PDFs as text chunks with vector embeddings. Uses SQLAlchemy async with PostgreSQL and pgvector. OpenAI text-embedding-3-small (1536 dimensions). Chunks ~500 tokens with ~50 overlap.
**Acceptance Criteria:**
1. Create Document model (id, filename, uploaded_at, chunk_count) and Chunk model (id, document_id, content, embedding vector(1536), chunk_index)
2. Create POST `/api/v1/documents` that accepts a PDF, extracts text, chunks, embeds, and stores
3. Create GET `/api/v1/documents` and DELETE `/api/v1/documents/{id}`
**Verify:** `curl -F "file=@test.pdf" http://localhost:8000/api/v1/documents` returns document ID and chunk count. `curl http://localhost:8000/api/v1/documents` lists it. Delete returns 200, then list shows it gone.

---

## Phase 3: Chat
**Goal:** Users can ask questions and get answers grounded in their documents.

### Task 3: Chat endpoint with retrieval
**Context:** A RAG chatbot API with documents stored as embedded chunks in pgvector. The chat endpoint takes a question, finds relevant chunks via vector similarity, and generates an answer using OpenAI chat completion. Answers include source references. No relevant chunks = "no information" response.
**Acceptance Criteria:**
1. Create a retrieval service that embeds the query and searches pgvector for top-5 similar chunks
2. Create a chat service that builds a prompt from chunks and calls OpenAI chat completion
3. Create POST `/api/v1/chat` that wires retrieval → chat → response with sources
**Verify:** Upload a document, then `curl -X POST http://localhost:8000/api/v1/chat -H "Content-Type: application/json" -d '{"message": "..."}'` returns an answer with sources. Unrelated query returns "no information."

---

## Phase 4: Polish
**Goal:** Consistent error handling and test coverage.

### Task 4: Error handling and tests
**Context:** A RAG chatbot API with document upload, listing, deletion, and chat endpoints. All responses need consistent JSON structure and proper error handling.
**Acceptance Criteria:**
1. Define Pydantic response schemas for all endpoints
2. Add error handling: non-PDF uploads (400), missing documents (404), OpenAI failures (502)
3. Write integration tests using pytest with httpx AsyncClient and mocked OpenAI calls
**Verify:** `pytest` — all tests pass. `curl -F "file=@test.txt" http://localhost:8000/api/v1/documents` returns 400.
