---
name: explain-visually
description: "Create a beautiful HTML explanation of a repo, spec, PR, architecture, or concept so a smart beginner can understand and retell it."
user-invocable: true
argument-hint: "<repo, spec, PR, architecture, concept, or source material>"
---

# Explain Visually

Create a human-facing HTML artifact that explains an idea visually. Beauty serves clarity. The reader should understand the idea well enough to retell it.

## Workflow

### 1. Understand

Read the source material. Identify the audience, core idea, moving parts, decisions, tradeoffs, and what the human should remember.

Ground the explanation in facts from the source. Prefer concrete names, paths, commands, interfaces, examples, and observed behavior over positioning language.

Default to explaining for a smart beginner. Define jargon before using it. If a term needs domain context, replace it with plain language or explain it visually.

### 2. Outline

Write the teaching path before building:

- what the reader should understand
- the order to explain it
- which ideas need diagrams
- what can be omitted
- which source facts support the explanation

Default teaching path:

- the simple version
- the problem
- the idea
- how it works
- a concrete example
- why it matters

### 3. Build

Create a responsive HTML explainer. Use Tailwind CSS via CDN for layout and responsive behavior. Use custom CSS only for fonts, theme tokens, diagrams, and small refinements.

Default format: slide-like sections on desktop, readable stacked sections on mobile. Do not preserve a fixed 16:9 frame on mobile.

Use:

- simple concrete titles
- short explanatory copy
- source-grounded statements, not slogans
- SVG diagrams that teach the idea
- strong typography, spacing, and visual hierarchy
- one clear idea per section

### 4. Verify

Run `browser-verify` before finishing. Check desktop and mobile viewports. Fix overflow, overlap, clipped text, unreadable scale, cramped spacing, and broken responsive layout.

## Style

- Fonts: Bricolage Grotesque for body and UI, Instrument Serif for display.
- Palette: warm paper background, dark ink, muted rust accent, restrained teal secondary.
- Think in grids, line height, margins, and visual hierarchy.
- Keep hero titles restrained. Prefer `md:text-7xl`; avoid `lg:text-9xl` unless the title is very short.
- Split the artifact before cramming content.
- On mobile, use natural-height sections, single-column grids, compact display type, readable text, and diagrams that fit without dominating the section.
- A mobile hero should feel readable, not like a cropped desktop slide.
- In SVG diagrams, align text inside shapes deliberately. Use `text-anchor`, `dominant-baseline`, explicit font sizes, and enough padding so labels do not drift, clip, or touch borders.

## Rules

- Explain, do not decorate.
- Teach before summarizing.
- Simple words beat abstract titles.
- Define loaded terms before relying on them.
- Make factual claims the source material supports.
- Use concrete names, paths, commands, and examples when they help the reader trust the explanation.
- Diagrams should make the idea easier to understand.
- Diagram text must be centered, aligned, and contained inside its shapes.
- Do not use `overflow: hidden` on content containers to hide layout problems.
- The artifact fails if the reader cannot explain the idea back.
- The artifact fails if text overlaps, clips, or overflows.
