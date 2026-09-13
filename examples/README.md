# Blueprint examples

These examples show the current design format: requirements, user experience, technical design and choices, acceptance and proof, and open questions.

- [RAG chatbot design](rag-chatbot/design.md) develops the [project notes](input.md) into a local API proposal. The [paired plan](rag-chatbot/plan.md) divides it into two useful delivery tasks.
- [Dispatch design](dispatch-control-plane/design.md) shows a local agent control plane with task execution, history, and recovery.

Both describe whole systems, so their technical sections need more detail than a routine feature. Keep smaller designs shorter. Commands and test scenarios describe the applications to be built; those applications are not implemented in this repository.

The examples are curated teaching material. Judge a generated design by its decisions, user experience, scope, and proof. Different wording or a different valid implementation can satisfy the same brief.

Run `./examples/regenerate.sh` from the repository root to print prompts for making a new RAG design and plan. Review the results before replacing an example. When changing a design's scope or acceptance criteria, update its paired plan too. Published implementation tickets should link to an immutable reviewed design revision.
