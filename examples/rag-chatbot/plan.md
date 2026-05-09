# Plan: RAG Chatbot API

Source input: `examples/input.md`

Source spec: `docs/rag-chatbot/spec.md`

## Shared Context

Build a greenfield FastAPI service for uploading PDFs, storing chunks and embeddings in PostgreSQL with pgvector, and answering questions with OpenAI using retrieved document context. Keep V1 single-user, PDF-only, and deployable locally with Docker Compose.

Shared decisions:

- Use FastAPI, PostgreSQL with pgvector, UV, Docker Compose, and OpenAI.
- Use fixed-size chunks with overlap.
- Mock OpenAI in tests.
- Keep errors shaped as `{error: {code, message}}`.

## Task 1: Project Foundation

**Goal**

Create the application scaffold, local services, configuration, database connection, and health endpoint.

**Context**

This task establishes the project structure and local runtime that every later task depends on. It should not implement document ingestion or chat behavior.

**Relevant files or references**

- `pyproject.toml`
- `docker-compose.yml`
- `app/main.py`
- `app/core/config.py`
- `app/db/session.py`
- `tests/`

**Proposed approach**

Set up a UV-managed FastAPI project. Add Docker Compose with an API service and PostgreSQL image that supports pgvector. Add environment-backed settings, database session setup, and a health endpoint that checks API startup and database connectivity.

**Acceptance criteria**

- The API and database start with Docker Compose.
- The app can connect to PostgreSQL.
- A health endpoint returns a successful JSON response.
- Configuration comes from environment variables.

**Source reference**

`docs/rag-chatbot/spec.md`: Context, Requirements, Design.

**Verify**

Run `docker compose up -d` and call the health endpoint. Run the project test command.

**Out of scope**

PDF upload, chunking, embeddings, retrieval, chat, and document listing.

## Task 2: Document Upload And Ingestion

**Goal**

Accept PDF uploads, extract text, chunk it, embed chunks, and store documents and chunks for retrieval.

**Context**

This is the first task that touches file handling, schema design, OpenAI embeddings, and failure behavior. It should leave enough stored data for later list, delete, and chat tasks.

**Relevant files or references**

- `app/api/documents.py`
- `app/models.py`
- `app/services/pdf.py`
- `app/services/chunking.py`
- `app/services/openai.py`
- `tests/fixtures/test.pdf`

**Proposed approach**

Add document and chunk tables. Implement PDF validation and text extraction. Add fixed-size chunking with overlap. Add an OpenAI embedding adapter. Implement `POST /api/v1/documents` and store document metadata, chunk content, chunk order, and embeddings.

**Acceptance criteria**

- `POST /api/v1/documents` accepts a PDF and returns `{id, filename, chunk_count}`.
- Uploaded PDFs are extracted, chunked, embedded, and stored.
- Non-PDF uploads return `400` with `bad_request`.
- OpenAI embedding failures return `502` with `upstream_error`.
- A deterministic PDF fixture exists for tests.

**Source reference**

`docs/rag-chatbot/spec.md`: Requirements, Design, Error Behavior, Testing Strategy.

**Verify**

Run the upload endpoint test and a manual `curl -F "file=@tests/fixtures/test.pdf" http://localhost:8000/api/v1/documents`.

**Out of scope**

Listing, deletion, vector retrieval, chat responses, auth, and non-PDF formats.

## Task 3: Document Listing And Deletion

**Goal**

List uploaded documents and delete a document with all related chunks.

**Context**

Task 2 creates stored documents and chunks. This task adds read and delete behavior while preserving the deletion invariant.

**Relevant files or references**

- `app/api/documents.py`
- `app/models.py`
- Document and chunk database tests

**Proposed approach**

Implement `GET /api/v1/documents` and `DELETE /api/v1/documents/{id}`. Use database cascade behavior or explicit deletion so chunks cannot survive their document. Return consistent JSON for success and errors.

**Acceptance criteria**

- `GET /api/v1/documents` returns document metadata and chunk counts.
- `DELETE /api/v1/documents/{id}` deletes the document and related chunks.
- Deleting a missing document returns `404` with `not_found`.
- Deleted chunks cannot be retrieved through later queries.

**Source reference**

`docs/rag-chatbot/spec.md`: Requirements, Invariants, Error Behavior.

**Verify**

Upload the PDF fixture, list documents, delete the returned ID, list again, and assert the document and chunks are gone.

**Out of scope**

Search, chat, soft delete, permissions, and retention policy.

## Task 4: Retrieval-Backed Chat

**Goal**

Answer user questions using retrieved document chunks and return source references.

**Context**

The document and chunk data exists after Tasks 2 and 3. This task connects message embedding, vector retrieval, prompt construction, chat completion, and source formatting.

**Relevant files or references**

- `app/api/chat.py`
- `app/services/openai.py`
- `app/models.py`
- Chat endpoint tests

**Proposed approach**

Implement `POST /api/v1/chat`. Embed the incoming message, retrieve the top 5 chunks by vector similarity, build a grounded prompt from the chunks, call OpenAI chat completion, and return `{answer, sources}`. If retrieval finds no relevant chunks, return the fixed no-information response.

**Acceptance criteria**

- `POST /api/v1/chat` accepts a message and returns `{answer, sources}`.
- Sources include chunk content and document ID.
- A question answerable from the PDF fixture returns an answer grounded in the fixture and at least one source.
- No relevant chunks returns the fixed no-information response and no sources.
- OpenAI chat failures return `502` with `upstream_error`.

**Source reference**

`docs/rag-chatbot/spec.md`: Requirements, Design, Decisions, Error Behavior.

**Verify**

Upload the PDF fixture, ask `What database is used for embeddings?`, and assert the answer mentions PostgreSQL with pgvector and includes a source.

**Out of scope**

Conversation history, streaming, reranking, multi-document filtering, and retrieval tuning beyond V1 defaults.

## Task 5: End-To-End Verification

**Goal**

Prove the main API flows and expected error paths with deterministic tests.

**Context**

The core API should exist after Tasks 1-4. This task closes coverage gaps and makes the workflow reviewable without depending on live OpenAI calls.

**Relevant files or references**

- `tests/`
- `tests/fixtures/test.pdf`
- Docker Compose test database setup

**Proposed approach**

Add endpoint and integration tests with `pytest` and `httpx`. Run database-backed tests against PostgreSQL with pgvector. Mock OpenAI embeddings and chat completions. Cover successful flows and required error responses.

**Acceptance criteria**

- Tests cover upload, list, delete, chat with relevant chunks, chat with no relevant chunks, non-PDF upload, missing document deletion, and OpenAI failure paths.
- OpenAI calls are mocked with deterministic responses.
- Tests verify the deletion invariant and error response shape.
- The documented verification commands pass.

**Source reference**

`docs/rag-chatbot/spec.md`: Testing Strategy, Invariants, Error Behavior.

**Verify**

Run `pytest` and any project lint/type checks introduced by the scaffold.

**Out of scope**

Changing API behavior, adding new endpoints, testing third-party internals, and live OpenAI integration tests.
