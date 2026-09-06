# RAG chatbot API

> **Status:** Proposed for review
>
> **Source:** [Project notes](../input.md)

## 1. Requirements: what and why

A person with a collection of PDFs wants answers without searching each document by hand. Build a local API that lets them upload, list, and delete documents, then ask questions with source text attached to each answer. When the collection contains no relevant information, say so.

V1 serves one trusted user through Docker Compose. Support text PDFs up to 25 MiB. Authentication, multiple users, OCR, conversation history, streaming, and background ingestion are out of scope.

## 2. User experience

1. Upload a PDF. A successful response contains its ID, filename, upload time, and chunk count. Chunks are searchable sections of the document. Processing finishes before the response; a failed upload creates no document.
2. List uploaded documents or delete one by ID. Deletion removes its searchable content. Uploading the same filename twice creates separate documents.
3. Submit a question. Receive an answer plus source entries containing document ID, filename, chunk position, and text. Sources are ordered by relevance.
4. If nothing relevant is found, receive `{"answer":"No relevant information found in uploaded documents.","sources":[]}`.

Invalid files and empty questions return a clear request error. Oversized files, missing documents, provider failures, and database failures have distinct error responses. Failures never appear as successful answers. The health endpoint reports database availability.

## 3. Technical design and choices

### Stack and processing

Use Python with FastAPI and `uv`, as requested in the brief. FastAPI provides the HTTP boundary; application services own ingestion and retrieval; a provider adapter keeps OpenAI calls replaceable in tests.

Use PostgreSQL with pgvector for both document data and embeddings, the numeric representations used for search. One store gives upload and deletion atomic behavior. It also couples search capacity to the database, which is acceptable for this local version.

Extract text and divide it into approximately 500-token chunks with 50-token overlap. Fixed chunks are easy to test; they can split ideas across boundaries. Generate embeddings before committing the document and every chunk in one transaction. Synchronous ingestion avoids a queue but makes upload latency grow with document size.

Use one configured embedding model for both uploads and questions. Changing that model requires re-embedding existing documents. Give documents opaque UUIDs; filenames are display data. Each chunk stores its document ID, zero-based position, text, and embedding. Deletion cascades to chunks.

For chat, calculate pgvector cosine similarity as `1 - (embedding <=> query_embedding)`. Select at most five chunks scoring at least `RAG_RELEVANCE_THRESHOLD`, default `0.75`. Order equal scores by document ID and chunk position. Send only those chunks to the answer generator and return the same source text. The threshold reduces weak-context answers but needs tuning for different content.

### Interfaces and failures

| Request | Successful response |
|---|---|
| `GET /health` | `{status: "ok"}` |
| `POST /api/v1/documents`, multipart `file` | `{id, filename, uploaded_at, chunk_count}` |
| `GET /api/v1/documents` | Array of document objects |
| `DELETE /api/v1/documents/{id}` | `{deleted: true}` |
| `POST /api/v1/chat`, `{message}` | `{answer, sources: [{document_id, filename, chunk_index, content}]}` |

Errors use `{error: {code, message}}`: invalid or textless PDFs and empty questions return `400/bad_request`; oversized PDFs `413/payload_too_large`; missing deletion `404/not_found`; OpenAI failures `502/upstream_error`; database operations `500/internal_error`. Health returns `503/service_unavailable` when PostgreSQL is unavailable and does not call OpenAI. No qualifying chunks is a successful chat response, not a provider error.

Require `DATABASE_URL` and `OPENAI_API_KEY` before startup. Reject a nonnumeric relevance threshold or a value outside `[0, 1]`. Roll back failed uploads. Docker Compose owns persistent database storage. This service has no authentication and stays local. Document text is sent to OpenAI; disclose that in the README.

## 4. Acceptance and proof

Use `pytest` and `httpx` against PostgreSQL with pgvector. Mock OpenAI with deterministic embeddings and answers. Run `uv sync --frozen` and `uv run pytest` in the application built from this design.

| ID | Done when | How to check |
|---|---|---|
| AC-1 | The application starts locally and health reflects database availability. | Run `docker compose up -d`; check health with PostgreSQL available and unavailable. Test missing required configuration and invalid threshold values. |
| AC-2 | PDF upload is atomic and returns the documented fields. | Upload a known PDF and two files sharing a name. Reject invalid, textless, and oversized files; force persistence failure and assert no partial rows. |
| AC-3 | Listing and deletion reflect stored documents. | List, delete by ID, verify chunks are gone, and repeat deletion to check `404`. |
| AC-4 | Answers use exactly the returned sources, with at most five matches in the defined order. | Use known PDF text and deterministic scores above, below, and equal to the threshold. Check ties and inspect generator input. |
| AC-5 | Empty questions fail clearly; absent or deleted evidence produces the fixed no-information response. | Exercise empty messages, no matches, and a question after deleting its only supporting document. |
| AC-6 | Provider and database failures return the documented errors without partial uploads or success-shaped answers. | Inject failures during upload, list, delete, retrieval, and generation. Check response codes and stored rows. |

## 5. Open questions

None block this local version. Authentication and asynchronous ingestion need a separate design if the deployment scope grows.
