# HTML PRD and design document skill

> **Status:** Proposed for review

## 1. Executive summary

Add an `/html-doc` skill that turns an existing Markdown product requirements document (PRD) or technical design into a clear, static HTML document. The Markdown file remains the source of truth. The HTML adds navigation, stronger visual hierarchy, useful callouts, readable diagrams, responsive layout, and print styles without changing the document's meaning.

The skill is a presentation step, not another product or technical design workflow. This avoids competing with `/design` and prevents requirements from changing during rendering. The main downside is a second file that can drift from its source. The generated page records the source path and content hash, and the skill regenerates rather than edits HTML by hand.

## 2. Context and scope

Markdown is good for writing and source review. Long PRDs and design documents are harder to scan in raw form because summaries, decisions, requirements, risks, diagrams, and open questions have similar visual weight.

The new skill accepts a Markdown file or exact Markdown supplied in the request. It creates one sibling HTML file for people to read in a browser, print, or attach to a review. It preserves all source content and order while changing its presentation.

This design covers PRDs and proposed technical designs. It does not decide product requirements, settle technical choices, host documents, or replace the Markdown source.

## 3. System context

```mermaid
flowchart LR
    Brief([Idea or problem]) --> Author["PRD authoring or /design"]
    Author --> Source["Canonical Markdown"]
    Source --> Skill["/html-doc"]
    Skill --> Page["Generated HTML"]
    Page --> Review([Human review])
    Review -->|content changes| Source
```

The authoring step owns meaning. `/html-doc` owns presentation. Review comments that change behavior, scope, requirements, or decisions go back into the Markdown source before the page is regenerated.

## 4. Proposed design

### How it works

A user invokes `/html-doc` with a Markdown path and states whether it is a PRD or design document. The kind may be omitted only when the source basename is exactly `prd.md` or `design.md`. The skill does not infer the kind from headings or prose.

The skill copies the bundled HTML template to a sibling output such as `docs/payments/prd.html`. It maps the source into semantic HTML in the same order. It adds a document header, status and source metadata, a linked table of contents, and presentation treatments based on section meaning. Unknown sections remain normal sections and are never dropped.

The page uses semantic HTML, inline CSS, and no runtime JavaScript. During generation, the exact dependency tree recorded in the skill lockfile renders Mermaid blocks with `@mermaid-js/mermaid-cli@11.16.0` and Puppeteer `25.5.0`. The generator rejects resource-bearing Mermaid source before rendering, runs Chromium with network resolution and proxy access denied, validates each SVG against an allowlist, embeds it as a base64 data image, and keeps the exact Mermaid source in a disclosure below the image. The result works as a local file without a server or network connection.

The skill opens the result in a real browser. It checks desktop and mobile widths, keyboard navigation, diagrams, long tables, code blocks, links, and print preview. It compares the rendered content with the source. It fixes presentation defects in the generated file or template, but sends content defects back to the source.

### Page structure

```text
+------------------------------------------------------------------+
| Document kind  Status                          Source and revision |
| Title                                                            |
| Existing summary from the source                                 |
+-------------------+----------------------------------------------+
| Contents          | Main document                                |
| 1. Problem        |                                              |
| 2. Goals          | Clear section rhythm                         |
| 3. Requirements   | Decision, risk, and question callouts        |
| ...               | Readable tables, code, and diagrams          |
|                   |                                              |
+-------------------+----------------------------------------------+
| Source path and generator version                                |
+------------------------------------------------------------------+
```

On narrow screens, the contents move above the document and the page becomes one column. Print hides navigation and source-control details that do not help the paper reader. Visual callouts use a label, border, icon or shape, and text so color is never the only signal.

### Components and responsibilities

| Component | Owns | Depends on | Does not own |
| --- | --- | --- | --- |
| `SKILL.md` | Input rules, generation workflow, parity checks, browser proof, and stop condition | Repository policy and supplied source | Product or technical decisions |
| HTML template | Page structure, design tokens, responsive layout, print rules, and accessibility defaults | Browser standards | Document content |
| Render script | Markdown conversion, diagram rendering, sanitization, metadata, and structural checks | Pandoc, Node.js, and pinned Mermaid CLI and Puppeteer packages | Content decisions or browser proof |
| Generated HTML | One reviewable view of one source revision | Markdown source and template | Canonical content or later edits |
| Markdown source | All claims, requirements, decisions, and document order | Its authoring workflow | Browser presentation |

### Decisions

**Keep Markdown canonical.** A paired Markdown and HTML document makes writing, diffing, and agent review simple while giving humans a better reading surface. Making HTML canonical would improve direct presentation but make content changes harder to inspect and merge.

**Make the skill presentation-only.** `/design` already owns technical design in this repository. Letting `/html-doc` also settle requirements or architecture would create two conflicting workflows. A user with only a rough idea must first supply or create the source document.

**Generate a static, offline page.** The output uses inline CSS and sanitized, base64-embedded SVG images with no fonts, scripts, images, or style sheets fetched at runtime. This makes a file easy to share and avoids broken pages behind network or content-security restrictions. It costs more generation work than loading a web framework.

**Lock the Mermaid renderer.** Generation uses `@mermaid-js/mermaid-cli@11.16.0` with Puppeteer `25.5.0`, Node.js 22.12 or newer, and Pandoc 3 or newer. The complete Node dependency tree is checked into the skill as `package-lock.json` and installed with `npm ci`. Mermaid CLI provides broad Mermaid compatibility and renders locally. Its Chromium dependency makes the first render slower and larger than a hand-written SVG path, but it does not become part of the output file.

**Deny renderer network access.** Before invoking Mermaid CLI, the generator rejects Mermaid source containing remote or local resource syntax, Mermaid initialization directives, icon-pack syntax, CSS `url()` or `@import`, HTML image or link elements, protocol-relative URLs, and `http:`, `https:`, `file:`, or `data:` URLs. Chromium keeps its sandbox enabled and starts with a deny-all proxy plus host resolution rules that map every host to failure. Remote configuration and icon packs are not loaded. After rendering, a parser-based SVG allowlist either accepts the whole diagram or rejects it. It never edits an unsafe diagram into a different one.

**Fail the whole candidate when a diagram fails.** A missing renderer, Mermaid parse error, sanitizer rejection, or browser failure is a generation failure. The skill reports the failing diagram and keeps the previous valid HTML byte-for-byte unchanged. Publishing a code-block fallback was rejected because readers could mistake a degraded page for a verified result.

**Use one restrained visual system for both document kinds.** Both layouts share typography, spacing, navigation, metadata, tables, code, and print behavior. PRDs emphasize users, goals, requirements, and measures. Designs emphasize system context, decisions, invariants, interfaces, failures, and risks. Separate templates would drift and add little value.

**Preserve source order and wording.** Presentation treatments may group a heading with its own content, but may not summarize, rewrite, rank, or omit source claims. This keeps the HTML trustworthy. A separate executive overview may appear only when that overview exists in the source.

**Define parity over canonical content.** Parity compares the Markdown abstract syntax tree with the canonical document-content subtree inside `main`. It excludes navigation, machine metadata, visible source metadata, and derived accessibility text because those repeat or describe source content. Each top-level Markdown block maps to one signed content node in source order, with its nested content kept inside that node. A Mermaid block maps to one `figure`; its exact source appears once in a disclosure and its rendered image has a useful alternative derived from diagram labels.

**Finalize atomically.** Generation creates a uniquely named candidate beside the output and takes an exclusive lock for that output. Only one render may target an output at a time. After structural and browser checks pass, one atomic replace operation installs the candidate without deleting the old output first. Normal failures and cancellation clean up the candidate and lock. A forced process kill may leave stale state, which the next run reports and requires the user to discard explicitly.

## 5. Invariants and requirements

### Invariants

- `INV-1`: Every top-level Markdown abstract-syntax-tree block maps to one signed canonical content node in the HTML and remains in source order, with nested content kept inside its parent and the documented Mermaid figure mapping as the only compound presentation.
- `INV-2`: The HTML introduces no new requirement, decision, claim, priority, or status.
- `INV-3`: Content changes happen in Markdown, followed by regeneration. Generated HTML is not hand-edited.
- `INV-4`: The generated page needs no network connection at read time.
- `INV-5`: Navigation, reading order, and meaning remain usable without color, a mouse, or a wide screen.
- `INV-6`: The page identifies the exact source content revision from which it was generated.
- `INV-7`: A failed diagram, structural check, browser check, or final replacement never changes the previous valid output.
- `INV-8`: Only one active render may target an output, and every normal failure or cancellation removes its candidate and lock.

### Requirements

- Accept a repository-relative or absolute Markdown path. Also accept exact inline Markdown when the user explicitly provides the full document.
- Support `prd` and `design` document kinds. Require an explicit kind except when the source basename is exactly `prd.md` or `design.md`.
- Write `<source-basename>.html` beside the source by default. Accept an explicit output path.
- Leave the Markdown source unchanged.
- Show title, document kind, status when supplied, source path, and a SHA-256 source hash in the page header.
- Add a linked table of contents for second-level and third-level headings.
- Give stable, readable anchor IDs to headings and deduplicate repeated headings with numeric suffixes.
- Ensure every emitted DOM ID is unique. Repeated desktop and mobile navigation must not duplicate IDs.
- Render Markdown paragraphs, emphasis, links, lists, tasks, tables, blockquotes, code, and fenced diagrams without data loss.
- Use specific treatments for summary, goals, non-goals, requirements, acceptance criteria, decisions, invariants, failures, risks, and open questions when those sections exist.
- Include responsive styles for a 390-pixel viewport and a print stylesheet for A4 and US Letter.
- Use no external runtime assets and no runtime JavaScript.
- Verify the result in a real browser before reporting completion.

## 6. Interfaces and data

The skill accepts these request shapes:

```text
/html-doc docs/billing/prd.md
/html-doc docs/billing/design.md as design
/html-doc docs/billing/design.md --out artifacts/billing-design.html
```

The syntax describes intent rather than a shell command. The skill resolves paths from the repository root, unless the user gives an absolute path.

The generated page includes machine-readable metadata:

```html
<meta name="document-kind" content="design">
<meta name="source-path" content="docs/billing/design.md">
<meta name="source-sha256" content="...">
<meta name="generator" content="blueprint/html-doc@1">
```

The visible header repeats the document kind, source path, and source status. V1 recognizes status only from an exact leading blockquote in the form `> **Status:** <value>`. When that field is absent, the visible status is omitted. It does not show a generation time because timestamps create noisy diffs without proving content identity.

The `document-kind` metadata value is always the canonical lowercase value `prd` or `design`. The visible header may show the human labels `PRD` or `Technical design`.

Heading IDs use a lowercase ASCII slug made from visible heading text. Runs of other characters become one hyphen. Leading and trailing hyphens are removed. An empty result becomes `section`. Repeated IDs receive `-2`, `-3`, and so on in source order. Explicit source IDs are not supported in V1 because they are not part of the selected GitHub-Flavored Markdown input contract.

### Naming and identity

The source file path identifies the document. Its SHA-256 hash identifies the rendered revision. Renaming the source changes the default output path but not its content identity. If the source is missing or unreadable, the skill creates no output. Inline Markdown has no durable source path, so the skill requires an explicit output path and records `inline-input` as the source.

## 7. Failure behavior and lifecycle

- A missing, unreadable, or non-Markdown source stops generation and names the failed path.
- A source whose basename is not exactly `prd.md` or `design.md` and has no explicit kind stops generation and asks for `prd` or `design`.
- Invalid Markdown is preserved as visible text where safe. The skill reports the affected source location instead of silently dropping it.
- A missing Mermaid renderer, Mermaid parse error, or rejected SVG stops generation and names the failing diagram. No candidate becomes the final output.
- Unsafe raw HTML is escaped by default. If the user explicitly permits trusted raw HTML, it is sanitized before inclusion.
- An existing output file is overwritten only when its generator metadata points to the same source path, or when the user explicitly chose that output. Otherwise the skill stops to avoid replacing unrelated work.
- Generation takes an exclusive lock for the exact output and writes a uniquely named sibling candidate. If a live lock already exists, it stops instead of running concurrently.
- A failed generation, structural check, browser check, or final replacement does not replace a previously valid output. After all checks pass, generation calls one atomic replacement operation. It never deletes the old output first.
- Normal failures and cancellation remove the candidate and lock. A forced process kill may leave a stale candidate and lock. A later run reports their exact paths and requires an explicit discard action before trying again.
- Regeneration replaces the entire generated page. It never attempts to merge hand edits.
- The skill stops after the HTML passes parity and browser checks. It does not publish or host the file.

## 8. Security, privacy, and operations

Markdown is untrusted input. Text and attributes are HTML-escaped. Links allow `http`, `https`, `mailto`, relative paths, and fragment targets. Other URL schemes are rendered as text. External links use `rel="noopener noreferrer"`.

Mermaid CLI runs locally at generation time with a locked version and a fixed strict configuration. Before rendering, the generator rejects resource-bearing source syntax, initialization directives, icon packs, CSS imports and URLs, HTML resource elements, and remote, local-file, or data URLs. Chromium keeps its sandbox enabled and starts with a deny-all proxy plus host-resolution rules that fail every host. The generator then parses the SVG and accepts only documented elements, attributes, and fragment references. Any disallowed construct rejects the whole diagram. The browser loads accepted SVG only through an `img` data URL, which isolates it from the document DOM. The page uses no runtime JavaScript. A restrictive content security policy blocks scripts, objects, frames, and network connections.

Generation requires Node.js 22.12 or newer, Pandoc 3 or newer, and npm. The skill installs the exact checked-in dependency tree with `npm ci`. Puppeteer may download its locked Chromium build during installation, before document content is read. The skill checks these dependencies before creating a candidate and never sends source content to a service.

The skill reads one source file and writes one output file. A default maximum source size of 2 MiB prevents accidental rendering of generated data or logs. The skill stops with a clear error at that limit. It never sends document content to an external service.

## 9. Acceptance criteria

- `AC-1`: Given representative PRD and design Markdown fixtures, the skill creates sibling HTML pages and leaves both sources byte-for-byte unchanged.
- `AC-2`: Every top-level Markdown abstract-syntax-tree block maps to one signed node in the canonical content subtree and remains in source order, with nested content kept in its parent. Navigation, metadata, and derived accessibility text are excluded from parity. Each Mermaid block maps to one figure whose exact source appears once in a disclosure.
- `AC-3`: The page header contains the correct visible kind, source path, status, and SHA-256 hash, while `document-kind` metadata contains canonical `prd` or `design`.
- `AC-4`: Repeated, Unicode-only, and punctuation-only headings receive unique working anchors according to the naming rules, and every emitted DOM ID is unique.
- `AC-5`: The table of contents links to every second-level and third-level heading.
- `AC-6`: A generated page opens from disk with network access disabled and has no failed runtime resource requests.
- `AC-7`: At 390, 768, and 1440 CSS pixels, text does not overlap, navigation remains usable, code scrolls within its container, and tables remain readable without widening the page.
- `AC-8`: Keyboard-only navigation can reach the skip link, table of contents, document links, and section targets in a clear order with a visible focus indicator.
- `AC-9`: Screen-reader inspection finds one page title, one `main` landmark, ordered headings without skipped levels introduced by the template, useful link names, and text alternatives for diagrams.
- `AC-10`: Print preview on A4 and US Letter hides navigation, preserves headings with their first content block where practical, repeats table headers, and does not clip code or diagrams.
- `AC-11`: Script tags, event attributes, unsafe URL schemes, embedded HTML, external CSS imports, and remote SVG resources in a hostile fixture do not execute or enter the generated DOM.
- `AC-12`: Resource-bearing Mermaid is rejected before renderer launch. A denied renderer request, Mermaid parse failure, SVG allowlist rejection, browser check failure, final replacement failure, or interrupted generation leaves the previous verified output byte-for-byte unchanged.
- `AC-13`: An unrelated existing HTML file is not overwritten without explicit user direction.
- `AC-14`: In a clean environment, `npm ci` installs the exact locked Mermaid CLI and Puppeteer versions and renders the representative Mermaid fixture.
- `AC-15`: Concurrent renders for one output cannot both proceed. Normal failures remove their candidate and lock, while stale state from a forced kill is reported and can be discarded explicitly.

## 10. Test approach

- Prove `INV-1`, `INV-2`, `AC-1`, and `AC-2` with compact PRD and design fixtures containing every supported Markdown block and semantic section. Compare signed top-level abstract-syntax-tree blocks, rendered text, and canonical content-node order, apply the documented Mermaid figure mapping, and assert that the sources are unchanged.
- Prove `INV-6` and `AC-3` by checking visible metadata, canonical machine metadata, and the SHA-256 source hash.
- Prove `INV-5`, `AC-4`, `AC-5`, `AC-7`, `AC-8`, and `AC-9` with repeated, Unicode-only, and punctuation-only headings plus real-browser checks at 390, 768, and 1440 CSS pixels. Inspect overflow, keyboard focus, landmarks, headings, anchors, diagram alternatives, console errors, and unique DOM IDs.
- Prove `INV-4` and `AC-6` by serving nothing, disabling browser networking, and opening the output through a local file URL when browser policy permits. Otherwise use a local static server and separately assert that no runtime URL can leave the file.
- Prove `AC-10` by opening print preview for A4 and US Letter and inspecting each page for clipping and isolated headings.
- Prove `INV-7`, `INV-8`, `AC-11`, `AC-12`, `AC-13`, and `AC-15` with hostile Markdown and SVG fixtures, invalid Mermaid, a controlled endpoint that records attempted requests, a forced browser failure, a simulated final replacement failure, normal interruption, concurrent renders, stale-state recovery, and an unrelated existing output. Confirm that unsafe Mermaid is rejected before renderer launch, renderer network requests cannot reach the endpoint, each failure is reported, normal cleanup occurs, and an earlier valid output remains byte-for-byte unchanged.
- Prove `INV-3` by regenerating a fixture and confirming that the generator replaces the whole candidate instead of merging hand edits.
- Prove `AC-14` from an environment without `node_modules`: run `npm ci`, assert the installed package versions match the lockfile, and render the representative Mermaid fixture.
- Run the repository's skill review against the new instruction, renderer, script, and template. Check that `/html-doc` stays a presentation outcome and does not duplicate PRD or design decisions.

## 11. Risks and tradeoffs

| Risk | Consequence | Mitigation |
| --- | --- | --- |
| Markdown and HTML drift | Reviewers read stale requirements | Record the source hash, regenerate whole files, and forbid hand edits |
| Visual treatment changes meaning | A callout can imply priority or status not present in source | Map only known section roles and preserve wording and order |
| Generated HTML creates noisy diffs | Pull requests become harder to review | Keep output deterministic and omit timestamps or random IDs |
| Complex Markdown exceeds the template | Content is clipped or dropped | Preserve unknown blocks plainly and prove parity with adversarial fixtures |
| Mermaid CLI and Chromium add a large generation dependency | First use is slower and may fail on constrained machines | Pin both packages, check dependencies before writing, and fail without replacing the previous output |

## 12. Open questions

- Should generated HTML be committed beside Markdown by default, or treated as a local review artifact? The recommended default is a local review artifact unless repository policy says generated files are committed. This does not block implementation.
- V1 supports GitHub-Flavored Markdown as parsed by Pandoc. Other Markdown extensions are out of scope and must be enabled by a later design. This does not block implementation.

## 13. Out of scope

- Deciding PRD content, product priorities, or technical architecture
- Editing the Markdown source during presentation work
- A browser-based editor or review-comment system
- Hosting, publishing, access control, or analytics
- PDF generation
- Slide decks or marketing pages
- Live synchronization between Markdown and an open browser
