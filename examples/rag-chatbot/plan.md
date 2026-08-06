# Plan: RAG Chatbot API

> Captured chat output from the `/plan` skill. A real run stays in chat or is published as tracker tickets when requested.

## Overview

A FastAPI service for uploading PDFs and answering questions from their contents. It uses retrieval-augmented generation (RAG): the service finds relevant text in PostgreSQL with pgvector, then gives that text to OpenAI to answer the question.

Source design: [RAG chatbot design](design.md)

## Shared decisions

- Use FastAPI, PostgreSQL with pgvector, Docker Compose, and OpenAI.
- Use `uv` for Python package and environment management.
- Use fixed-size chunks with overlap for V1.
- Limit PDF uploads to 25 MiB.
- Store a document and all of its chunks atomically.
- Mock OpenAI in tests.
- Add focused tests with each task and run them against PostgreSQL with pgvector.
- Keep API errors shaped as `{error: {code, message}}`, including `payload_too_large` for a PDF over 25 MiB.
- Return a fixed no-information answer instead of inventing an answer when the search finds no relevant text.
- Require `DATABASE_URL` and `OPENAI_API_KEY`.

---

## Milestone 1: Run the service locally

Goal: the app starts, connects to the database, and exposes a healthy API shell.

### Task 1: Start and check the API locally

#### Summary

Developers cannot build later features until they can start the API and its database in a repeatable way. This task adds local startup, required configuration, and a health check so a developer can tell whether the base service is ready.

#### User stories

- As a developer, I want to start the API and database locally and check their health so that I can build and test features on a known working service.

#### Outcome

The API and database can be started locally, configured from the environment, and checked with a health endpoint.

#### Context

This task creates the base service shape for every later endpoint. It should establish local startup, settings, database connectivity, and the test runner without adding document or chat behavior.

#### Constraints

- Build the API with FastAPI and use PostgreSQL with pgvector.
- Use `uv` for Python package management.
- Use Docker Compose for the API and PostgreSQL with pgvector.
- Keep configuration in environment variables.
- Require `DATABASE_URL` and `OPENAI_API_KEY`.
- Return API errors as `{error: {code, message}}`.

#### Acceptance criteria

- The API and database start with Docker Compose.
- `GET /health` returns `200` with `{"status":"ok"}` when the API can reach the database and `503` with `service_unavailable` when it cannot.
- The app fails before serving traffic when `DATABASE_URL` or `OPENAI_API_KEY` is missing.
- The README states that V1 is for one trusted user and sends document text to OpenAI.
- A baseline `uv run pytest` succeeds for later tasks.

#### Design reference

The [RAG chatbot design](design.md) covers the stack, Docker Compose surface, environment configuration, and JSON response expectations.

#### Checks

```bash
docker compose up -d
curl http://localhost:8000/health
uv sync --frozen
uv run pytest
```

Also make PostgreSQL unavailable and verify that `/health` returns the documented `503`. Cover each missing required setting.

#### Out of scope

Document upload, embeddings, retrieval, chat, auth, and deployment beyond local Docker Compose.

---

## Milestone 2: Store uploaded documents

Goal: PDFs can be uploaded, processed, and stored for later retrieval.

### Task 2: Upload and store PDFs

#### Summary

Users cannot ask questions about their documents until the service can turn an uploaded PDF into searchable text. This task validates each upload and stores its text for later searching without leaving partial data after a failure.

#### User stories

- As a user, I want to upload a PDF so that the service can use its contents when answering my questions.

#### Outcome

Users can upload a PDF and receive a stored document record with the number of text sections created from it.

#### Context

This task depends on Task 1, which creates the local API and database. It proves the path from upload to stored search data. It validates the file, extracts its text, and divides that text into small sections called chunks. It turns each chunk into a numeric representation called an embedding, which the service uses to find text with similar meaning. It then stores the document and its chunks for later document and chat tasks.

#### Constraints

- Add the endpoint to the existing FastAPI service.
- Accept PDFs only.
- Reject uploads over 25 MiB before text extraction.
- Use fixed-size chunks of about 500 tokens with about 50 tokens of overlap.
- Store documents, chunks, and embeddings in PostgreSQL with pgvector.
- Generate an opaque UUID for each uploaded document. Treat the original filename as display metadata, never identity.
- Identify each chunk by its document UUID and zero-based position. Keep that position stable for the lifetime of the document.
- Commit the document and all chunks in one database transaction.
- Use the existing `DATABASE_URL` and `OPENAI_API_KEY` settings.
- Return API errors as `{error: {code, message}}`.
- Mock OpenAI calls in tests.
- Read the shutdown deadline from `SERVER_GRACEFUL_SHUTDOWN_SECONDS`, defaulting to `10`, and fail startup unless it is an integer from `1` through `60`.

#### Acceptance criteria

- `POST /api/v1/documents` accepts a PDF and returns `{id, filename, uploaded_at, chunk_count}`.
- Uploading two documents with the same filename returns two distinct valid UUIDs and stores both documents.
- Uploaded PDFs are stored with chunks and embeddings that can be queried later.
- Stored chunks have unique positions from `0` through `chunk_count - 1` within their document.
- Non-PDF and empty-text PDF uploads return `400` with `bad_request`.
- Uploads over 25 MiB return `413` with `payload_too_large` and create no rows.
- OpenAI embedding failures return `502` with `upstream_error`.
- A persistence failure returns `500` with `internal_error`.
- Embedding and persistence failures leave no document or chunk rows behind.
- A slow upload that finishes before the graceful shutdown deadline commits normally.
- Cancelling a deliberately slow upload at the graceful shutdown deadline leaves no document or chunk rows behind.
- Startup accepts shutdown values from `1` through `60` and rejects zero, negative, greater values, and non-integers.
- A PDF fixture contains the sentence "PostgreSQL with pgvector stores the embeddings." for later retrieval tests.

#### Design reference

The [RAG chatbot design](design.md) covers document storage, chunking defaults, embedding behavior, upload validation, and upstream OpenAI error behavior.

#### Checks

```bash
uv run pytest
curl -F "file=@tests/fixtures/test.pdf" http://localhost:8000/api/v1/documents
```

Also run focused tests for a non-PDF, an empty-text PDF, and an oversized upload. Test embedding failure and a forced database failure that returns `500` with `internal_error`. Cover shutdown completion and cancellation during slow uploads. Test each shutdown setting boundary.

Upload the same fixture twice with the same filename. Prove that the returned IDs are distinct UUIDs and query each document's chunks to confirm unique zero-based positions.

For every failed upload, query PostgreSQL in the test fixture and prove that document and chunk row counts did not change.

#### Out of scope

Document listing, deletion, retrieval, chat, auth, and non-PDF formats.

### Task 3: List and delete uploaded documents

#### Summary

After uploading documents, users need to see what the service holds and remove material they no longer want searched. This task adds listing and deletion while ensuring removed text cannot appear in later answers.

#### User stories

- As a user, I want to list and delete uploaded documents so that I can control which material the service searches.

#### Outcome

Users can list uploaded documents and delete a document with all searchable data created from it.

#### Context

This task depends on Task 2. Task 2 stores each uploaded document as small text sections, called chunks, with numeric embeddings used to find text with similar meaning. Those documents form the collection that chat will search. This task lets users manage that collection before chat relies on it.

#### Constraints

- Add the endpoints to the existing FastAPI service and use the PostgreSQL document and chunk records created by Task 2.
- Use the opaque document UUID as API identity. Treat the filename as display metadata only.
- Do not change upload behavior from Task 2.
- Deleted chunks must not remain retrievable.
- Return API errors as `{error: {code, message}}`.

#### Acceptance criteria

- `GET /api/v1/documents` returns documents with `id`, `filename`, `uploaded_at`, and `chunk_count`.
- `DELETE /api/v1/documents/{id}` removes the document and its related chunks.
- Deleting a missing document returns `404` with `not_found`.
- Database failures during listing or deletion return `500` with `internal_error`; a failed deletion leaves the document and chunks intact.
- After deletion, the document no longer appears in the list and its chunks are gone.

#### Design reference

The [RAG chatbot design](design.md) defines the document listing/deletion API shapes and the invariant that deleting a document also removes its chunks and embeddings.

#### Checks

```bash
uv run pytest
```

Focused tests force database failures during listing and deletion and assert `500` with `internal_error`. After a failed deletion, query PostgreSQL and prove the document and chunks remain.

Manual smoke check: upload `tests/fixtures/test.pdf`, list documents, delete the returned ID, then confirm the ID no longer appears in `GET /api/v1/documents`.

#### Out of scope

Search, chat, cross-user permissions, and soft delete.

---

## Milestone 3: Answer questions from documents

Goal: users can ask questions and get answers based on uploaded documents.

### Task 4: Answer questions from uploaded PDFs

#### Summary

Stored PDFs are not useful until users can ask questions and receive answers based on their contents. This task finds the most relevant stored text, gives it to OpenAI, cites the source passages, and says clearly when the documents do not contain an answer.

#### User stories

- As a user, I want answers based on my uploaded PDFs so that I can use the documents without searching them by hand.

#### Outcome

Users can ask a question and receive an answer based on uploaded PDFs, with references to the source text.

#### Context

This task depends on Tasks 2 and 3. Task 2 stores each PDF as small text sections, called chunks, and creates a numeric embedding for each chunk. Task 3 adds the deletion endpoint used to prove that removed documents no longer affect answers. This task creates the same kind of embedding for a question and compares the numbers to find text with similar meaning. It gives the matching text to OpenAI, formats the answer and source references, and handles questions that have no useful match.

#### Constraints

- Add the endpoint to the existing FastAPI service and query PostgreSQL with pgvector.
- Return each source's opaque document UUID and stable zero-based chunk position as `document_id` and `chunk_index`.
- Use the existing `DATABASE_URL` and `OPENAI_API_KEY` settings.
- Return API errors as `{error: {code, message}}`.
- Mock OpenAI calls in tests.
- Retrieve at most 5 chunks for each question.
- Calculate cosine similarity as `1 - (embedding <=> query_embedding)`.
- Read the inclusive threshold from `RAG_RELEVANCE_THRESHOLD`, defaulting to `0.75`, accept `0` and `1`, and fail startup unless it is numeric and satisfies `0 <= value <= 1`.
- Return sources by descending similarity, then document ID and chunk index for stable ties.
- Do not add conversation history or streaming.

#### Acceptance criteria

- `POST /api/v1/chat` accepts a message and returns `{answer, sources}`.
- A missing or empty message returns `400` with `bad_request`.
- Sources include `document_id`, `filename`, `chunk_index`, and `content`.
- A question answerable from the fixture returns an answer based on that fixture and at least one source.
- With more than five qualifying chunks, retrieval returns five and the mocked generator receives exactly the same ordered content returned in `sources`.
- A chunk scoring exactly `RAG_RELEVANCE_THRESHOLD` qualifies, while a lower score does not.
- Chunks with equal similarity are ordered by document ID and then chunk index.
- Threshold configuration accepts `0` and `1` and rejects non-numeric values, values below `0`, and values above `1` before startup.
- If no relevant chunks are found, the endpoint returns `{"answer":"No relevant information found in uploaded documents.","sources":[]}`.
- After a failed fixture upload or deletion of an uploaded fixture, asking about its known text returns the fixed no-information response with no sources.
- OpenAI embedding or chat failures return `502` with `upstream_error`.
- A database failure during retrieval returns `500` with `internal_error`.

#### Design reference

The [RAG chatbot design](design.md) covers retrieval defaults, chat response shape, source references, no-information behavior, and upstream OpenAI failure handling.

#### Checks

```bash
uv run pytest
```

Run focused tests for a missing or empty message and for a database failure during retrieval. Use fixed vectors with scores equal to, just below, and just above the threshold.

Create more than five matching chunks. Check that the mocked answer generator receives the same first five chunks returned in the sources.

Force a fixture upload to fail, then ask about its known text. Check the fixed no-information response. Upload and delete the fixture, ask the same question, and check the same response.

Test threshold settings at `0`, `1`, below `0`, above `1`, and with a non-numeric value.

Manual smoke check: upload `tests/fixtures/test.pdf`, ask `What database is used for embeddings?`, and confirm the response mentions PostgreSQL with pgvector and includes at least one source.

#### Out of scope

Conversation history, streaming responses, reranking, and retrieval tuning beyond the V1 defaults.
