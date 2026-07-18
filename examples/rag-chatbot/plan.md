# Plan: RAG Chatbot API

> Captured chat output from the `plan` skill. A real run stays in chat or is published as tracker tickets when requested.

## Overview

A FastAPI service for uploading PDFs and answering questions from their contents using PostgreSQL with pgvector and OpenAI.

Source design: `docs/rag-chatbot/design.md`

## Shared Decisions

- Use FastAPI, PostgreSQL with pgvector, Docker Compose, and OpenAI.
- Use fixed-size chunks with overlap for V1.
- Mock OpenAI in tests.
- Add focused tests with each task and run them against PostgreSQL with pgvector.
- Keep API errors shaped as `{error: {code, message}}`.
- Return a fixed no-information answer instead of hallucinating when retrieval has no relevant chunks.

---

## Phase 1: Foundation

Goal: the app starts, connects to the database, and exposes a healthy API shell.

### Task 1: Local API foundation

**Outcome**

The API and database can be started locally, configured from the environment, and checked with a health endpoint.

**Context**

This task creates the base service shape for every later endpoint. It should establish local startup, settings, database connectivity, and the test runner without adding document or chat behavior.

**Constraints**

- Use `uv` for Python package management.
- Use Docker Compose for the API and PostgreSQL with pgvector.
- Keep configuration in environment variables.

**Acceptance Criteria**

- The API and database start with Docker Compose.
- `GET /health` returns `{"status":"ok"}` when the API can reach the database.
- The app fails clearly when required database configuration is missing.
- A baseline `pytest` run is available for later tasks.

**Design Reference**

`docs/rag-chatbot/design.md` covers the stack, Docker Compose surface, environment configuration, and JSON response expectations.

**Checks**

```bash
docker compose up -d
curl http://localhost:8000/health
pytest
```

**Out of Scope**

Document upload, embeddings, retrieval, chat, auth, and deployment beyond local Docker Compose.

---

## Phase 2: Document Ingestion

Goal: PDFs can be uploaded, processed, and stored for later retrieval.

### Task 2: PDF upload and ingestion

**Outcome**

Users can upload a PDF and receive a stored document record with chunk count.

**Context**

This task proves the ingestion path: validation, text extraction, chunking, embeddings, and persistence. Later document and chat tasks depend on the stored document and chunk data.

**Constraints**

- Accept PDFs only.
- Use fixed-size chunks of about 500 tokens with about 50 tokens of overlap.
- Mock OpenAI calls in tests.

**Acceptance Criteria**

- `POST /api/v1/documents` accepts a PDF and returns `{id, filename, uploaded_at, chunk_count}`.
- Uploaded PDFs are stored with chunks and embeddings that can be queried later.
- Non-PDF uploads return `400` with `{error: {code, message}}`.
- OpenAI embedding failures return `502` with `{error: {code, message}}`.
- A PDF fixture exists with known text for later retrieval tests.

**Design Reference**

`docs/rag-chatbot/design.md` covers document storage, chunking defaults, embedding behavior, upload validation, and upstream OpenAI error behavior.

**Checks**

```bash
pytest
curl -F "file=@tests/fixtures/test.pdf" http://localhost:8000/api/v1/documents
```

**Out of Scope**

Document listing, deletion, retrieval, chat, auth, and non-PDF formats.

### Task 3: Document listing and deletion

**Outcome**

Users can list uploaded documents and delete a document with all of its chunks and embeddings.

**Context**

Documents and chunks exist after Task 2. This task adds the document management behavior needed before chat can rely on the stored corpus.

**Constraints**

- Do not change upload behavior from Task 2.
- Deleted chunks must not remain retrievable.

**Acceptance Criteria**

- `GET /api/v1/documents` returns documents with `id`, `filename`, `uploaded_at`, and `chunk_count`.
- `DELETE /api/v1/documents/{id}` removes the document and its related chunks.
- Deleting a missing document returns `404` with `{error: {code, message}}`.
- After deletion, the document no longer appears in the list and its chunks are gone.

**Design Reference**

`docs/rag-chatbot/design.md` defines the document listing/deletion API shapes and the invariant that deleting a document also removes its chunks and embeddings.

**Checks**

```bash
pytest
```

Manual smoke check: upload `tests/fixtures/test.pdf`, list documents, delete the returned ID, then confirm the ID no longer appears in `GET /api/v1/documents`.

**Out of Scope**

Search, chat, cross-user permissions, and soft delete.

---

## Phase 3: Chat

Goal: users can ask questions and get grounded answers from uploaded documents.

### Task 4: Retrieval-backed chat endpoint

**Outcome**

Users can ask a question and receive a grounded answer with source references from uploaded PDFs.

**Context**

This task combines vector retrieval, prompt construction, OpenAI chat completion, source formatting, and no-result behavior.

**Constraints**

- Retrieve at most 5 chunks for each question.
- Return sources ordered by relevance.
- Do not add conversation history or streaming.

**Acceptance Criteria**

- `POST /api/v1/chat` accepts a message and returns `{answer, sources}`.
- Sources include `document_id`, `filename`, `chunk_index`, and `content`.
- A question answerable from the fixture returns an answer grounded in that fixture and at least one source.
- If no relevant chunks are found, the endpoint returns `{"answer":"No relevant information found in uploaded documents.","sources":[]}`.
- OpenAI embedding or chat failures return `502` with `{error: {code, message}}`.

**Design Reference**

`docs/rag-chatbot/design.md` covers retrieval defaults, chat response shape, source references, no-information behavior, and upstream OpenAI failure handling.

**Checks**

```bash
pytest
```

Manual smoke check: upload `tests/fixtures/test.pdf`, ask `What database is used for embeddings?`, and confirm the response mentions PostgreSQL with pgvector and includes at least one source.

**Out of Scope**

Conversation history, streaming responses, reranking, and retrieval tuning beyond the V1 defaults.
