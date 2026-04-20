# Plan: RAG Chatbot API

## Overview

A Python API for uploading PDFs and answering questions from their contents using FastAPI, PostgreSQL with pgvector, and OpenAI.
Spec: `docs/rag-chatbot/spec.md`

---

## Phase 1: Foundation
**Goal:** The app starts, connects to the database, and exposes a healthy API shell.

### Task 1: Project setup and health check

**Context:**
Set up the FastAPI service, PostgreSQL with pgvector, Docker Compose, and environment-based configuration. This creates a working foundation for later ingestion and chat features.

**Acceptance Criteria:**
- The API and database start with Docker Compose
- A health endpoint confirms the app can reach the database
- Configuration comes from environment variables

**Verify:**
`docker compose up -d && curl http://localhost:8000/health` returns `{"status":"ok"}`

---

## Phase 2: Document Ingestion
**Goal:** PDFs can be uploaded, processed, and stored for later retrieval.

### Task 2: PDF upload and ingestion

**Context:**
Build the ingestion path from uploaded PDF to stored chunks and embeddings. This task should leave the system able to accept a document and persist everything needed for later search.

**Acceptance Criteria:**
- `POST /api/v1/documents` accepts a PDF, extracts text, chunks it, embeds it, and stores the result
- Non-PDF uploads return `400`
- The response includes the document ID, filename, and chunk count

**Verify:**
`curl -F "file=@test.pdf" http://localhost:8000/api/v1/documents` returns `{id, filename, chunk_count}`

### Task 3: Document listing and deletion

**Context:**
Once documents exist, users need to inspect what has been uploaded and remove documents they no longer want. Deletion must clean up the related chunks and embeddings.

**Acceptance Criteria:**
- `GET /api/v1/documents` returns stored documents with metadata
- `DELETE /api/v1/documents/{id}` removes the document and its related chunks
- Deleting a missing document returns `404`

**Verify:**
Upload a document, run `curl http://localhost:8000/api/v1/documents`, then delete it with `curl -X DELETE http://localhost:8000/api/v1/documents/{id}`

---

## Phase 3: Chat
**Goal:** Users can ask questions and get grounded answers from uploaded documents.

### Task 4: Retrieval-backed chat endpoint

**Context:**
Build the question-answering flow on top of stored chunks and embeddings. The endpoint should retrieve relevant chunks, generate an answer, and return the supporting sources.

**Acceptance Criteria:**
- `POST /api/v1/chat` accepts a message and returns `{answer, sources}`
- Sources include the chunk content and document ID
- If nothing relevant is found, the response clearly says there is no information instead of hallucinating

**Verify:**
`curl -X POST http://localhost:8000/api/v1/chat -H "Content-Type: application/json" -d '{"message":"What does the document say about X?"}'`

---

## Phase 4: Test Coverage
**Goal:** The main API flows are covered by reliable integration tests.

### Task 5: Integration tests for the API

**Context:**
Once upload, listing, deletion, and chat all work, add integration tests that prove the main flows and error cases. Use a real PostgreSQL + pgvector instance and mock OpenAI calls for repeatability.

**Acceptance Criteria:**
- Tests cover upload, list, delete, chat with relevant chunks, chat with no relevant chunks, and the expected `400`, `404`, and `502` paths
- OpenAI calls are mocked with deterministic responses
- Tests run against a real PostgreSQL + pgvector database

**Verify:**
`pytest`
