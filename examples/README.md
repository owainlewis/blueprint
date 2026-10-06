# One project, one feature

[Task list](task-list/REQUIREMENTS.md) is a small local CLI for keeping tasks.
Read its documents in this order:

1. [Requirements](task-list/REQUIREMENTS.md): the product and its key features.
2. [Architecture](task-list/ARCHITECTURE.md): the intended system and data model.
3. [Add and list tasks spec](task-list/docs/add-and-list/spec.md): one change, its technical design, and acceptance checks.

Requirements and architecture stay with the project. Each feature gets one
spec. This first spec implements adding and listing; completing tasks is a later
feature. The spec can go straight to `/task-to-pr` or `/factory` without a plan.

The task-list application is not implemented in Blueprint. These documents are
teaching examples, not evidence that its commands or tests pass. In its own repo,
`REQUIREMENTS.md` and `ARCHITECTURE.md` would live at the root.

## Try the workflow

For a new project, ask `/requirements` to define a local task-list CLI, then ask
`/architecture` to design it from those requirements. Ask `/spec` for adding and
listing tasks. Compare the outputs with these examples for decisions, scope,
and proof, rather than exact wording.

To deliver a real application, give its spec to `/task-to-pr` for a passing open
PR, or explicitly invoke `/factory` for gated merging. Do this in the
application's repo, not in Blueprint. Review consequential choices first and use
`/plan` only when the spec needs several delivery tasks.
