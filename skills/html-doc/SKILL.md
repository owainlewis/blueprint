---
name: html-doc
description: Generates a polished, static HTML reading view from an existing Markdown PRD or technical design. Use when a user asks to render, present, visualize, or make a PRD or design document easier for humans to read in a browser.
---

# HTML document

Turn one complete Markdown PRD or technical design into one verified static HTML page. Keep Markdown canonical. Change presentation, not meaning.

## Boundaries

- Accept an existing Markdown file or exact inline Markdown.
- Support only `prd` and `design` document kinds.
- Infer the kind only from the exact basename `prd.md` or `design.md`. Otherwise require the user or request to name it.
- Do not write requirements, settle design choices, summarize missing content, or edit the source.
- If the source is only a rough brief, use the appropriate authoring skill first.
- Do not hand-edit generated HTML. Change the template or renderer, then regenerate.
- Do not publish or host the result unless the user separately asks.

## Requirements

Generation requires Python 3.11 or newer, Pandoc 3 or newer, Node.js 22.12 or newer, and npm. The skill directory contains a locked Mermaid dependency tree.

Before the first Mermaid render, run:

```bash
npm ci --prefix <skill-directory>
```

Use `scripts/html_doc.py` from this skill directory for all generation and lifecycle operations.

## Workflow

### 1. Read and classify the source

Read the complete source. Confirm it is no larger than 2 MiB. Determine the document kind from the request or the exact basename rule.

Treat content problems separately from presentation problems. If the Markdown contradicts itself, omits a required decision, or contains an invalid diagram, report that source problem. Do not silently repair its meaning.

### 2. Create a candidate

For a file source:

```bash
python3 <skill-directory>/scripts/html_doc.py render <source.md> --kind <prd-or-design> --out <output.html>
```

`--kind` may be omitted only for exact `prd.md` and `design.md` basenames. `--out` may be omitted to create a sibling HTML file.

For exact inline Markdown, pipe it through standard input and provide both kind and output:

```bash
python3 <skill-directory>/scripts/html_doc.py render --inline --kind <prd-or-design> --out <output.html>
```

The command returns JSON containing `candidate`, `output`, and `token`. It does not replace the final output. Keep those exact values for verification and finalization.

If an output lock already exists, do not delete it automatically. It may represent another pending render. Report its path. Use `discard --force-stale` only when the state is known to be abandoned.

### 3. Verify the candidate in a real browser

Open the candidate as a local file. Do not treat source inspection as browser proof.

Check all of these:

- desktop at 1440 CSS pixels;
- tablet at 768 CSS pixels;
- mobile at 390 CSS pixels;
- A4 and US Letter print preview;
- table-of-contents links and section targets;
- keyboard order from skip link through navigation and document links;
- visible focus indicators;
- one `main` landmark and a sensible heading outline;
- unique DOM IDs;
- horizontal overflow, clipped text, code, tables, and diagrams;
- useful diagram alternatives and accessible disclosure controls;
- console errors and failed resource requests;
- operation with browser network access disabled.

Compare the canonical content inside `main` with the Markdown abstract syntax tree. Navigation, source metadata, and derived accessibility text are not canonical content. Each top-level source block must map to one ordered `data-source-block` node with its SHA-256 identity and nested content intact. A Mermaid block maps to one figure whose exact source appears once in its disclosure.

If a presentation defect comes from the shared renderer or styles, fix that source and regenerate. If it is a content defect, leave the source and candidate unchanged and report it.

### 4. Finalize or discard

Only after every check passes, atomically install the candidate:

```bash
python3 <skill-directory>/scripts/html_doc.py finalize --out <output.html> --token <token>
```

If any check fails, remove only this pending candidate:

```bash
python3 <skill-directory>/scripts/html_doc.py discard --out <output.html> --token <token>
```

Finalization performs one same-directory atomic replacement. It never deletes the previous output first. A failed render, check, or replacement must leave the previous verified output byte-for-byte unchanged.

## Output standard

The final page must:

- preserve source wording and order;
- use canonical `prd` or `design` machine metadata;
- record the source path and SHA-256 hash;
- use semantic HTML, inline CSS, and no runtime JavaScript;
- contain no external runtime assets;
- use a restrained blue-grey visual system;
- remain readable without color, a mouse, a wide screen, or network access;
- include responsive and print styles;
- embed validated Mermaid SVG as a base64 image and retain the exact source in a disclosure.

Stop when the verified candidate is finalized. Report the output path, source hash, and browser checks performed.
