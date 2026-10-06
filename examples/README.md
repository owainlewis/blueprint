# Blueprint examples

These examples use the earlier combined design format. They remain valid input to `/plan` and delivery, but they are not templates for the new document boundaries. New system work uses `REQUIREMENTS.md` and `ARCHITECTURE.md`; a feature uses `spec.md`.

- [RAG chatbot design](rag-chatbot/design.md) develops the [project notes](input.md) into a local API proposal. The [paired plan](rag-chatbot/plan.md) divides it into two useful delivery tasks.
- [Dispatch design](dispatch-control-plane/design.md) shows a local agent control plane with task execution, history, and recovery.

Both describe whole systems, so their technical sections need more detail than a routine feature. Keep smaller designs shorter. Commands and test scenarios describe the applications to be built; those applications are not implemented in this repository.

The examples are curated teaching material. Judge a generated design by its decisions, user experience, scope, and proof. Different wording or a different valid implementation can satisfy the same brief.

Run `./examples/regenerate.sh` from the repository root to print prompts for making system documents, a feature spec, and a plan. Review the results before replacing an example. When changing a design's scope or acceptance criteria, update its paired plan too. Published implementation tickets should link to an immutable reviewed design revision.
