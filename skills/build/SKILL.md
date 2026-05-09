---
name: build
description: "Deprecated compatibility alias for implement. Use implement for new workflows."
user-invocable: true
argument-hint: "<task reference or description>"
---

# Build

`build` is deprecated. Use `implement` for new workflows.

For compatibility with existing prompts and automation, treat this invocation as `implement`:

- Execute one scoped change using the `implement` workflow.
- Do not confuse this skill with project build commands such as `npm build`, `cargo build`, or CI build steps.
- Mention in the final report that `build` has been renamed to `implement`.
