# Plan: RAG Chatbot API

## Overview

A Python API for uploading PDFs and answering questions from their contents using FastAPI, PostgreSQL with pgvector, and OpenAI.

Source spec: `docs/rag-chatbot/spec.md`

## Shared Decisions

- Use FastAPI, PostgreSQL with pgvector, Docker Compose, and OpenAI.
- Use fixed-size chunks with overlap for V1.
- Mock OpenAI in tests.
- Keep API errors shaped as `{error: {code, message}}`.

---

## Phase 1: Foundation

Goal: the app starts, connects to the database, and exposes a healthy API shell.

### Task 1: Project setup and health check

**Goal**

Create the service scaffold, database container, configuration, and health endpoint.

**Context**

This task creates the foundation for ingestion and chat. Later tasks should not need to revisit project structure or local startup.

**Proposed Approach**

Set up FastAPI, Docker Compose with PostgreSQL and pgvector, environment-based settings, and a health endpoint that checks database connectivity.

**Acceptance Criteria**

- The API and database start with Docker Compose.
- A health endpoint confirms the app can reach the database.
- Configuration comes from environment variables.

**Spec**

short. The shared spec has the stack decisions; this task only needs the concrete health endpoint and config names.

**Verify**

`docker compose up -d && curl http://localhost:8000/health` returns `{"status":"ok"}`.

**Out of Scope**

Document upload, embeddings, retrieval, and chat.

---

## Phase 2: Document Ingestion

Goal: PDFs can be uploaded, processed, and stored for later retrieval.

### Task 2: PDF upload and ingestion

**Goal**

Accept a PDF upload, extract text, chunk it, embed chunks, and store everything needed for retrieval.

**Context**

This is the first task that touches file handling, chunking, embeddings, schema design, and external API failure behavior.

**Proposed Approach**

Add document and chunk tables, a PDF text extraction path, fixed-size chunking, an OpenAI embedding adapter, and `POST /api/v1/documents`.

**Acceptance Criteria**

- `POST /api/v1/documents` accepts a PDF, extracts text, chunks it, embeds it, and stores the result.
- Non-PDF uploads return `400`.
- The response includes document ID, filename, and chunk count.
- A fixture exists at `tests/fixtures/test.pdf` containing `Blueprint uses PostgreSQL with pgvector for embeddings.`

**Spec**

full. This task owns schema, chunking, embedding, upload validation, and upstream error behavior.

**Verify**

`curl -F "file=@tests/fixtures/test.pdf" http://localhost:8000/api/v1/documents` returns `{id, filename, chunk_count}`.

**Out of Scope**

Document listing, deletion, retrieval, chat, auth, and non-PDF formats.

### Task 3: Document listing and deletion

**Goal**

Let users list uploaded documents and delete a document with its chunks.

**Context**

Documents and chunks exist after Task 2. This task adds read and delete behavior without changing ingestion.

**Proposed Approach**

Add `GET /api/v1/documents` and `DELETE /api/v1/documents/{id}`. Use database constraints or explicit deletion so chunks cannot survive after their document is removed.

**Acceptance Criteria**

- `GET /api/v1/documents` returns stored documents with metadata.
- `DELETE /api/v1/documents/{id}` removes the document and its related chunks.
- Deleting a missing document returns `404`.

**Spec**

short. The main invariant is cascade deletion; the API shapes are already in the project spec.

**Verify**

Upload `tests/fixtures/test.pdf`, list documents, delete the returned ID, then confirm the ID no longer appears in `GET /api/v1/documents`.

**Out of Scope**

Search, chat, cross-user permissions, and soft delete.

---

## Phase 3: Chat

Goal: users can ask questions and get grounded answers from uploaded documents.

### Task 4: Retrieval-backed chat endpoint

**Goal**

Answer user questions using retrieved document chunks and return source references.

**Context**

This task combines vector retrieval, prompt construction, OpenAI chat completion, source formatting, and no-result behavior.

**Proposed Approach**

Add `POST /api/v1/chat`, embed the incoming message, retrieve the top 5 chunks by vector similarity, call the chat model with retrieved context, and return `{answer, sources}`.

**Acceptance Criteria**

- `POST /api/v1/chat` accepts a message and returns `{answer, sources}`.
- Sources include chunk content and document ID.
- If nothing relevant is found, the response says there is no information and returns no sources.
- OpenAI failures return `502`.

**Spec**

full. This task owns retrieval threshold behavior, source shape, prompt construction, and upstream failure behavior.

**Verify**

Upload `tests/fixtures/test.pdf`, then ask `What database is used for embeddings?`; the response mentions PostgreSQL with pgvector and includes at least one source.

**Out of Scope**

Conversation history, streaming responses, reranking, and retrieval tuning beyond the V1 defaults.

---

## Phase 4: Test Coverage

Goal: the main API flows are covered by reliable integration tests.

### Task 5: Integration tests for the API

**Goal**

Prove the main API flows and expected error paths with deterministic tests.

**Context**

The core behavior exists after Tasks 1-4. This task raises confidence without changing product behavior.

**Proposed Approach**

Use `pytest` and `httpx` against a real PostgreSQL with pgvector test database. Mock OpenAI embedding and chat calls with deterministic responses.

**Acceptance Criteria**

- Tests cover upload, list, delete, chat with relevant chunks, chat with no relevant chunks, and `400`, `404`, and `502` paths.
- OpenAI calls are mocked with deterministic responses.
- Tests run against a real PostgreSQL with pgvector database.

**Spec**

none. The behavior is already defined by the project spec and previous tasks.

**Verify**

`pytest`

**Out of Scope**

Changing API behavior, adding new endpoints, and testing third-party library internals.
