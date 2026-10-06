#!/bin/bash
# Print prompts for the system and feature workflow.
set -e

cat <<'PROMPTS'
Use /requirements for the RAG chatbot described in examples/input.md.
Use /architecture to design that system from REQUIREMENTS.md.
Use /architecture-review on ARCHITECTURE.md against REQUIREMENTS.md.
After the decisions are settled, use /spec for document ingestion and retrieval.
Use /architecture-review on docs/document-ingestion/spec.md.
After review, use /plan if the spec needs several delivery tasks.

Expected outputs:
  REQUIREMENTS.md
  ARCHITECTURE.md
  docs/document-ingestion/spec.md
  review verdicts and optional tasks in chat

Review generated documents before adding them as examples. Preserve references
between requirements, architecture, spec, and tasks. Applications described by
the examples are not implemented in this repository.
PROMPTS
