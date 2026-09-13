# Plan: RAG chatbot API

> Example of `/plan` output. Real plans stay in chat or become tracker tickets when requested.

Source: [Paired RAG design](design.md). These two examples describe the same scope. When publishing real tickets, link to the reviewed design revision.

## 1. Upload and manage a local PDF collection

### What are we building?

Let a person upload, list, and delete PDFs through a locally running API. Accepted documents become searchable text; failed uploads leave no partial records.

### Why?

Users need a reliable collection before the service can answer questions from it. This task delivers usable document management on its own.

### Done when

- Docker Compose starts the service and database; health reports database availability and startup validates required configuration (`AC-1`).
- Upload returns the documented metadata, preserves distinct IDs for duplicate filenames, and rejects invalid, textless, and oversized PDFs (`AC-2`).
- Listing shows stored documents. Deletion removes their chunks and returns the missing-document error when repeated (`AC-3`).
- Upload, list, and delete follow the shared provider/database failure contract, with no partial upload rows (`AC-6`, document operations).
- README explains local startup, supported files, API usage, and that document text is sent to OpenAI.

### How to check

```sh
docker compose up -d
uv sync --frozen
uv run pytest
```

Use a small PDF with known text. Test duplicate filenames, extraction failure, size limits, provider failure, and database rollback. Check stored rows after failures. Make PostgreSQL unavailable and verify health changes without calling OpenAI.

### Agent notes

- Depends on: None.
- Source: [Design](design.md), sections 1 through 4.
- Own the shared FastAPI, PostgreSQL/pgvector, OpenAI adapter, environment configuration, and error-response contracts.
- Ingest synchronously, using approximately 500-token chunks with 50-token overlap and one configured embedding model. Commit document and chunks together after embedding succeeds.
- Use document UUIDs, zero-based chunk positions, and cascading deletion. Keep HTTP handling, use-case behavior, persistence, and provider translation separate.
- Lock dependencies with `uv`; use pytest/httpx with a real PostgreSQL test database and mocked OpenAI. Validate the shared relevance-threshold configuration now; retrieval uses it in task 2.

### Out of scope

- Question answering, authentication, OCR, background ingestion, and cloud deployment.

## 2. Answer questions with matching source text

### What are we building?

Let a person ask a question about the uploaded collection and receive an answer with its supporting text. Return the fixed no-information response when the collection has no relevant evidence.

### Why?

This turns stored documents into a useful question-answering tool and lets users inspect where an answer came from.

### Done when

- Chat accepts a nonempty question and returns the documented answer/source shape, using exactly the source chunks given to the generator (`AC-4`).
- Retrieval applies the inclusive threshold, five-chunk limit, and deterministic ordering from the design (`AC-4`).
- Empty questions fail clearly; absent or deleted evidence returns the fixed no-information response (`AC-5`).
- Retrieval and generation failures use the shared error contract and never appear as successful answers (`AC-6`, chat operations).
- The full collection-to-answer flow works with the known PDF fixture, and README includes question and response examples.

### How to check

```sh
uv run pytest
```

Use deterministic embeddings to test scores below, equal to, and above the threshold, ties, and more than five matches. Inspect the mocked generator input and returned sources. Ask about the fixture before and after deleting its document. Force retrieval and provider failures and assert exact error codes.

### Agent notes

- Depends on: Upload and manage a local PDF collection.
- Source: [Design](design.md), sections 2 through 4.
- Reuse task 1's provider adapter, database schema, configuration, and error mapping.
- Use the same embedding model as ingestion. Search with pgvector cosine similarity; order equal scores by document ID and chunk position.
- Pass only selected source text to generation. Return the fixed no-information response without generation when no chunks qualify.
- Keep OpenAI mocked in automated tests; verify retrieval against PostgreSQL with pgvector.

### Out of scope

- Conversation history, streaming, reranking, model switching, and retrieval tuning beyond the specified defaults.
