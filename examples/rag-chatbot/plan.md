# Plan: RAG Chatbot API

> Captured chat output from the `/plan` skill. A real run stays in chat or is published as tracker tickets when requested.

Source design: [RAG chatbot design at the revision used for this example](https://github.com/owainlewis/blueprint/blob/9ec6081beeaff327a96fe60ef555ae52a504aa21/examples/rag-chatbot/design.md)

## Milestone 1: Run the service locally

### Task 1: Start the API and check its health

#### What are we building?

Create the smallest version of the API that starts locally, connects to PostgreSQL, and reports whether the database is available.

#### Why?

Developers need a repeatable starting point before they can add document upload or question answering.

#### Done when

- Docker Compose starts the API and PostgreSQL with pgvector.
- `GET /health` returns `200` when PostgreSQL is available and `503` when it is not. (`AC-2`)
- The health check does not call OpenAI. (`AC-2`)
- The app refuses to start when required settings are missing. (`AC-17`)
- The README explains local startup and that document text will be sent to OpenAI.
- The baseline test suite passes. (`AC-20`)

#### How to check

```bash
docker compose up -d
curl http://localhost:8000/health
uv sync --frozen
uv run pytest
```

Also make PostgreSQL unavailable and verify the documented `503` response. Make the OpenAI test adapter fail and verify that `/health` still returns `200` while PostgreSQL is available.

#### Agent notes

- Depends on: None.
- Source: [RAG chatbot design at the revision used for this example](https://github.com/owainlewis/blueprint/blob/9ec6081beeaff327a96fe60ef555ae52a504aa21/examples/rag-chatbot/design.md).
- Use FastAPI, PostgreSQL with pgvector, Docker Compose, and `uv`.
- Require `DATABASE_URL` and `OPENAI_API_KEY`.
- Return errors as `{error: {code, message}}`.
- Keep the health check limited to PostgreSQL.

#### Out of scope

- Document upload, search, chat, authentication, and cloud deployment.

## Milestone 2: Store uploaded documents

### Task 2: Upload PDFs and make them searchable

#### What are we building?

Add an endpoint that accepts a PDF, extracts its text, and stores a document record with all extracted searchable sections in PostgreSQL.

#### Why?

The service cannot answer questions until it has safely stored material to search.

#### Done when

- `POST /api/v1/documents` accepts a PDF up to 25 MiB and returns its ID, filename, upload time, and section count. (`AC-1`)
- Two files with the same name are stored as separate documents.
- Invalid, empty, and oversized files return the documented errors and create no records. (`AC-3`; `INV-3`)
- Each document and all its searchable sections are committed together or not at all. (`AC-15`; `INV-3`)
- OpenAI and database failures return the documented errors without leaving partial data. (`AC-15`; `AC-21`; `INV-3`; `INV-4`)
- Graceful shutdown lets short uploads finish, rejects new uploads, and rolls back work that exceeds the deadline. (`AC-18`)
- Startup accepts shutdown deadlines from `1` through `60` seconds and rejects zero, negative, larger, and non-integer values. (`AC-23`)

#### How to check

```bash
uv run pytest
curl -F "file=@tests/fixtures/test.pdf" http://localhost:8000/api/v1/documents
```

Use focused tests to force extraction, OpenAI, persistence, and shutdown failures. Query PostgreSQL after each failure to prove that no partial document remains.

#### Agent notes

- Depends on: Task 1.
- Source: [RAG chatbot design at the revision used for this example](https://github.com/owainlewis/blueprint/blob/9ec6081beeaff327a96fe60ef555ae52a504aa21/examples/rag-chatbot/design.md).
- Accept PDF files only. Reject files over 25 MiB before extraction.
- Use opaque UUIDs for document identity. The filename is display data only.
- Divide text into sections of about 500 tokens with about 50 tokens of overlap.
- Store sections and OpenAI embeddings in PostgreSQL with pgvector.
- Identify each section by its document UUID and stable zero-based position.
- Delete sections through a cascading foreign key when their document is deleted. (`INV-2`)
- Read the shutdown deadline from `SERVER_GRACEFUL_SHUTDOWN_SECONDS`. Default to `10`; accept integers from `1` through `60`.
- Mock OpenAI in tests.

#### Out of scope

- Listing, deletion, search, chat, and non-PDF formats.

### Task 3: List and delete documents

#### What are we building?

Add endpoints to show stored documents and remove a selected document with all of its searchable text.

#### Why?

Users need to know what the service can search and remove information they no longer want included in answers.

#### Done when

- `GET /api/v1/documents` returns each document's ID, filename, upload time, and section count. (`AC-4`)
- `DELETE /api/v1/documents/{id}` removes the document and its searchable sections. (`AC-5`; `INV-2`)
- Deleting an unknown ID returns the documented `404` response. (`AC-14`)
- Database failures return the documented error and leave existing data unchanged. (`AC-16`)
- Deleted text can no longer be found by later searches. (`AC-5`; `INV-2`)

#### How to check

```bash
uv run pytest
```

Upload the PDF fixture, list documents, delete its returned ID, and verify that the ID and its sections are gone. Force listing and deletion failures and verify their responses and stored data.

#### Agent notes

- Depends on: Task 2.
- Source: [RAG chatbot design at the revision used for this example](https://github.com/owainlewis/blueprint/blob/9ec6081beeaff327a96fe60ef555ae52a504aa21/examples/rag-chatbot/design.md).
- Use the document UUID in API paths. Never use the filename as identity.
- Keep HTTP formatting in FastAPI routes and PostgreSQL access in a repository.
- Rely on the database foreign-key cascade to remove stored sections.
- Return errors as `{error: {code, message}}`.

#### Out of scope

- Search, chat, permissions, and soft deletion.

## Milestone 3: Answer questions from documents

### Task 4: Answer questions using uploaded PDFs

#### What are we building?

Add an endpoint that finds relevant text in uploaded PDFs and uses that text to answer a question. Return the source text with the answer, or say clearly when the documents do not contain enough information.

#### Why?

This is the useful result of the application: people can ask questions without searching every uploaded PDF by hand.

#### Done when

- `POST /api/v1/chat` accepts `{"message":"..."}` and returns an answer with its sources. Missing and empty questions return the documented validation error. (`AC-6`; `AC-13`)
- The answer generator receives exactly the source sections returned to the caller, with at most five sections. (`AC-7`; `INV-1`)
- Equal scores are ordered by document ID and section position. (`AC-9`) A score exactly on the relevance threshold qualifies and a lower score does not. (`AC-8`) Threshold settings accept numeric values from `0` through `1` and reject invalid values before startup. (`AC-10`)
- When no useful text exists, the endpoint returns the fixed no-information answer with no sources. (`AC-11`) Failed uploads and deleted documents cannot affect later answers. (`AC-12`; `INV-2`; `INV-3`)
- OpenAI and database failures return the documented errors. (`AC-22`; `AC-24`; `INV-4`)
- The full test suite passes against PostgreSQL with pgvector while OpenAI calls are mocked. (`AC-19`)

#### How to check

```bash
uv run pytest
```

Upload `tests/fixtures/test.pdf`, ask `What database is used for embeddings?`, and verify that the answer mentions PostgreSQL with pgvector and includes a source. Test empty questions, threshold boundaries, stable ordering, deleted documents, and forced OpenAI and database failures.

#### Agent notes

- Depends on: Tasks 2 and 3.
- Source: [RAG chatbot design at the revision used for this example](https://github.com/owainlewis/blueprint/blob/9ec6081beeaff327a96fe60ef555ae52a504aa21/examples/rag-chatbot/design.md).
- Search PostgreSQL with pgvector cosine similarity and return at most five sections.
- Read the inclusive threshold from `RAG_RELEVANCE_THRESHOLD`. Default to `0.75`; accept numeric values from `0` through `1`.
- Order equal scores by document ID and section position.
- Send only returned source sections to OpenAI.
- Return source document ID, filename, section position, and content.
- Mock OpenAI in tests.

#### Out of scope

- Conversation history, streaming, reranking, and retrieval tuning beyond the V1 defaults.
