# Project Notes

Build a Python RAG chatbot API. Users upload PDF documents, the system chunks and embeds them, then users can ask questions and get answers grounded in their documents.

Stack: FastAPI, PostgreSQL with pgvector for embeddings, OpenAI API for embeddings and chat completion. Use UV for package management.

Endpoints:

- POST /api/v1/documents - upload a PDF, chunk it, embed it, store it
- POST /api/v1/chat - send a message, retrieve relevant chunks, return an AI-generated answer with source references
- GET /api/v1/documents - list uploaded documents
- DELETE /api/v1/documents/{id} - remove a document and its embeddings

Keep it simple. Single user, no auth for now. The chunking strategy does not need to be fancy. Fixed-size chunks with overlap are fine.

Should be deployable with Docker Compose (API + Postgres).

Expected behavior:

- Non-PDF uploads fail clearly.
- Missing document deletion returns a not-found error.
- Upstream OpenAI failures return an upstream error.
- When no document chunk is relevant, the chat endpoint returns a fixed "no relevant information" answer instead of making something up.

Testing:

- Use pytest.
- Mock OpenAI calls in tests.
- Use a small PDF fixture with known text so chat and source references can be verified.
