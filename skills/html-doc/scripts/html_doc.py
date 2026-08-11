#!/usr/bin/env python3
"""Generate and atomically install static HTML views of Markdown documents."""

from __future__ import annotations

import argparse
import base64
import hashlib
import html
from html.parser import HTMLParser
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import unicodedata
import uuid
import xml.etree.ElementTree as ET


GENERATOR = "blueprint/html-doc@1"
MAX_SOURCE_BYTES = 2 * 1024 * 1024
SKILL_DIR = Path(__file__).resolve().parents[1]
ASSETS_DIR = SKILL_DIR / "assets"

RESOURCE_SOURCE_PATTERNS = (
    re.compile(r"%%\{"),
    re.compile(r"(?:https?|file|data):", re.IGNORECASE),
    re.compile(r"(?<!:)//"),
    re.compile(r"@import\b", re.IGNORECASE),
    re.compile(r"\burl\s*\(", re.IGNORECASE),
    re.compile(r"<\s*(?:img|link)\b", re.IGNORECASE),
    re.compile(r"\b(?:icon|image):", re.IGNORECASE),
)

ALLOWED_SVG_ELEMENTS = {
    "svg", "g", "path", "rect", "circle", "ellipse", "line", "polyline",
    "polygon", "text", "tspan", "defs", "marker", "style", "title", "desc",
    "clipPath", "linearGradient", "radialGradient", "stop", "filter", "feDropShadow",
}
ALLOWED_SVG_ATTRIBUTES = {
    "id", "class", "style", "viewBox", "version", "baseProfile", "xmlns",
    "role", "tabindex", "aria-label", "aria-labelledby", "aria-describedby",
    "aria-roledescription", "width", "height", "x", "y", "x1", "y1", "x2",
    "y2", "cx", "cy", "r", "rx", "ry", "d", "points", "transform", "fill",
    "stroke", "stroke-width", "stroke-dasharray", "stroke-dashoffset",
    "stroke-linecap", "stroke-linejoin", "stroke-miterlimit", "fill-opacity",
    "stroke-opacity", "opacity", "marker-start", "marker-mid", "marker-end",
    "orient", "refX", "refY", "markerWidth", "markerHeight", "markerUnits",
    "preserveAspectRatio", "dominant-baseline", "alignment-baseline", "text-anchor",
    "font-family", "font-size", "font-weight", "font-style", "letter-spacing", "dy",
    "dx", "offset", "stop-color", "stop-opacity", "clip-path", "overflow", "color",
    "shape-rendering", "vector-effect", "paint-order", "href", "filter", "flood-color",
    "flood-opacity", "stdDeviation", "gradientUnits", "data-edge", "data-et", "data-id",
    "data-look", "data-points",
}
UNSAFE_SVG_TEXT = re.compile(
    r"(?:https?|file|data|javascript|vbscript):|@import\b|(?<!:)//", re.IGNORECASE
)
URL_FUNCTION = re.compile(r"url\s*\(([^)]*)\)", re.IGNORECASE)


class GenerationError(RuntimeError):
    pass


def run(command: list[str], *, stdin: str | None = None) -> str:
    result = subprocess.run(
        command,
        input=stdin,
        text=True,
        capture_output=True,
        check=False,
    )
    if result.returncode:
        detail = (result.stderr or result.stdout).strip()
        raise GenerationError(f"Command failed ({command[0]}): {detail}")
    return result.stdout


def version_tuple(value: str) -> tuple[int, ...]:
    match = re.search(r"(\d+(?:\.\d+)+)", value)
    if not match:
        raise GenerationError(f"Could not parse version from {value!r}")
    return tuple(int(part) for part in match.group(1).split("."))


def check_dependencies(require_mermaid: bool) -> None:
    if version_tuple(run(["pandoc", "--version"]).splitlines()[0]) < (3, 0):
        raise GenerationError("Pandoc 3 or newer is required")
    if version_tuple(run(["node", "--version"])) < (22, 12):
        raise GenerationError("Node.js 22.12 or newer is required")
    if not require_mermaid:
        return
    mmdc = SKILL_DIR / "node_modules" / ".bin" / "mmdc"
    if not mmdc.exists():
        raise GenerationError(f"Mermaid dependencies are missing. Run `npm ci` in {SKILL_DIR}")
    for package, expected in (("@mermaid-js/mermaid-cli", "11.16.0"), ("puppeteer", "25.5.0")):
        package_file = SKILL_DIR / "node_modules" / package / "package.json"
        try:
            actual = json.loads(package_file.read_text())["version"]
        except (FileNotFoundError, KeyError, json.JSONDecodeError) as error:
            raise GenerationError(f"Cannot verify installed {package}: {error}") from error
        if actual != expected:
            raise GenerationError(f"Installed {package} is {actual}; expected {expected}. Run `npm ci`")


def reject_resource_bearing_mermaid(source: str) -> None:
    for pattern in RESOURCE_SOURCE_PATTERNS:
        match = pattern.search(source)
        if match:
            raise GenerationError(
                f"Mermaid source contains forbidden resource syntax near {match.group(0)!r}"
            )


def local_name(value: str) -> str:
    return value.rsplit("}", 1)[-1]


def validate_svg(svg: bytes) -> bytes:
    decoded = svg.decode("utf-8")
    if "<!DOCTYPE" in decoded.upper() or "<!ENTITY" in decoded.upper():
        raise GenerationError("Rendered SVG contains a document type or entity")
    try:
        root = ET.fromstring(decoded)
    except ET.ParseError as error:
        raise GenerationError(f"Rendered SVG is invalid XML: {error}") from error
    if local_name(root.tag) != "svg":
        raise GenerationError("Rendered diagram root is not SVG")
    for element in root.iter():
        tag = local_name(element.tag)
        if tag not in ALLOWED_SVG_ELEMENTS:
            raise GenerationError(f"Rendered SVG contains forbidden element <{tag}>")
        if element.text:
            if tag == "style" and "\\" in element.text:
                raise GenerationError("Rendered SVG style contains a CSS escape")
            if UNSAFE_SVG_TEXT.search(element.text):
                raise GenerationError(f"Rendered SVG <{tag}> contains a forbidden resource reference")
            for url_value in URL_FUNCTION.findall(element.text):
                if not url_value.strip(" \t\"'").startswith("#"):
                    raise GenerationError("Rendered SVG style contains a non-fragment CSS URL")
        for raw_name, value in element.attrib.items():
            name = local_name(raw_name)
            if name.lower().startswith("on") or name not in ALLOWED_SVG_ATTRIBUTES:
                raise GenerationError(f"Rendered SVG contains forbidden attribute {name!r}")
            if UNSAFE_SVG_TEXT.search(value):
                raise GenerationError(f"Rendered SVG attribute {name!r} contains a resource URL")
            if name in {
                "style", "fill", "stroke", "filter", "clip-path", "marker-start",
                "marker-mid", "marker-end", "href",
            } and "\\" in value:
                raise GenerationError(f"Rendered SVG attribute {name!r} contains a CSS escape")
            if name == "href" and value and not value.startswith("#"):
                raise GenerationError("Rendered SVG contains a non-fragment href")
            for url_value in URL_FUNCTION.findall(value):
                if not url_value.strip(" \t\"'").startswith("#"):
                    raise GenerationError("Rendered SVG contains a non-fragment CSS URL")
    return svg


def render_mermaid(source: str, diagram_number: int) -> str:
    reject_resource_bearing_mermaid(source)
    mmdc = SKILL_DIR / "node_modules" / ".bin" / "mmdc"
    with tempfile.TemporaryDirectory(prefix="blueprint-html-doc-") as temp_dir:
        temp = Path(temp_dir)
        source_path = temp / "diagram.mmd"
        svg_path = temp / "diagram.svg"
        source_path.write_text(source, encoding="utf-8")
        run([
            str(mmdc), "--quiet", "--input", str(source_path), "--output", str(svg_path),
            "--configFile", str(ASSETS_DIR / "mermaid.json"),
            "--puppeteerConfigFile", str(ASSETS_DIR / "puppeteer.json"),
            "--backgroundColor", "transparent",
        ])
        svg = validate_svg(svg_path.read_bytes())
    encoded = base64.b64encode(svg).decode("ascii")
    escaped_source = html.escape(source)
    alt = html.escape(diagram_description(source, diagram_number))
    return (
        f'<figure class="diagram source-block" data-source-block="diagram-{diagram_number}">'
        f'<img alt="{alt}" src="data:image/svg+xml;base64,{encoded}">'
        f'<figcaption>Diagram {diagram_number}</figcaption>'
        '<details><summary>View Mermaid source</summary>'
        f'<pre><code class="language-mermaid">{escaped_source}</code></pre>'
        '</details></figure>'
    )


def diagram_description(source: str, diagram_number: int) -> str:
    labels: list[str] = []
    patterns = (r'\[\[?"?([^\]\["]+)"?\]\]?', r'\(\[?"?([^()\[]"]+)"?\]?\)', r'\|([^|]+)\|')
    for pattern in patterns:
        for value in re.findall(pattern, source):
            clean = re.sub(r"\s+", " ", value).strip(" \t\"'")
            if clean and clean not in labels:
                labels.append(clean)
    if not labels:
        prose = re.sub(r"[-=<>()[\]{}|;]+", " ", " ".join(source.splitlines()[1:]))
        prose = re.sub(r"\b(?:subgraph|end|click|classDef|style)\b", " ", prose, flags=re.IGNORECASE)
        clean = re.sub(r"\s+", " ", prose).strip()
        if clean:
            labels.append(clean)
    detail = ", ".join(labels)[:320] or "the relationships defined in the Mermaid source below"
    return f"Diagram {diagram_number} showing {detail}"


def inline_text(value: object) -> str:
    if isinstance(value, str):
        return value
    if isinstance(value, list):
        return "".join(inline_text(item) for item in value)
    if not isinstance(value, dict):
        return ""
    kind = value.get("t")
    content = value.get("c")
    if kind in {"Str", "Code", "Math"}:
        if kind == "Str":
            return str(content)
        return str(content[-1])
    if kind in {"Space", "SoftBreak", "LineBreak"}:
        return " "
    return inline_text(content)


def slugify(value: str, used: set[str]) -> str:
    normalized = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode("ascii")
    base = re.sub(r"[^a-z0-9]+", "-", normalized.lower()).strip("-") or "section"
    candidate = base
    suffix = 2
    while candidate in used:
        candidate = f"{base}-{suffix}"
        suffix += 1
    used.add(candidate)
    return candidate


def sanitize_links(node: object) -> None:
    if isinstance(node, list):
        for child in node:
            sanitize_links(child)
        return
    if not isinstance(node, dict):
        return
    if node.get("t") in {"Link", "Image"}:
        target = node["c"][2][0]
        scheme = re.match(r"^([A-Za-z][A-Za-z0-9+.-]*):", target)
        if scheme and scheme.group(1).lower() not in {"http", "https", "mailto"}:
            node["t"] = "Span"
            node["c"] = [node["c"][0], node["c"][1]]
    sanitize_links(node.get("c"))


def escape_raw_html(node: object) -> None:
    if isinstance(node, list):
        for child in node:
            escape_raw_html(child)
        return
    if not isinstance(node, dict):
        return
    if node.get("t") == "RawBlock" and node.get("c", [None])[0] == "html":
        node["t"] = "CodeBlock"
        node["c"] = [["", ["raw-html"], []], node["c"][1]]
        return
    if node.get("t") == "RawInline" and node.get("c", [None])[0] == "html":
        node["t"] = "Code"
        node["c"] = [["", ["raw-html"], []], node["c"][1]]
        return
    escape_raw_html(node.get("c"))


def role_for_heading(text: str) -> str | None:
    key = re.sub(r"[^a-z]+", "-", text.lower()).strip("-")
    roles = {
        "executive-summary": "summary", "summary": "summary", "goals": "goals",
        "non-goals": "non-goals", "requirements": "requirements",
        "acceptance-criteria": "acceptance-criteria", "decisions": "decisions",
        "invariants": "invariants", "failure-behavior": "failures",
        "failure-behavior-and-lifecycle": "failures", "risks": "risks",
        "risks-and-tradeoffs": "risks", "open-questions": "open-questions",
    }
    return roles.get(key)


def pandoc_document(markdown: str) -> dict:
    raw = run(["pandoc", "--from", "gfm-raw_html", "--to", "json"], stdin=markdown)
    return json.loads(raw)


def block_signature(block: dict) -> str:
    encoded = json.dumps(block, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def transform_document(document: dict) -> tuple[str, list[tuple[int, str, str]], list[str]]:
    used_ids: set[str] = {"document-content"}
    toc: list[tuple[int, str, str]] = []
    transformed: list[dict] = []
    diagram_number = 0
    source_blocks = document.get("blocks", [])
    signatures = [block_signature(block) for block in source_blocks]
    escape_raw_html(source_blocks)
    sanitize_links(source_blocks)
    for index, block in enumerate(source_blocks, start=1):
        kind = block.get("t")
        classes = block.get("c", [["", [], []]])[0][1] if kind == "CodeBlock" else []
        if kind == "CodeBlock" and "mermaid" in classes:
            diagram_number += 1
            rendered = render_mermaid(block["c"][1], diagram_number)
            rendered = rendered.replace(
                f'data-source-block="diagram-{diagram_number}"',
                f'data-source-block="{index}"',
            )
            rendered = rendered.replace(
                '<figure class="diagram source-block"',
                f'<figure class="diagram source-block" data-source-sha256="{signatures[index - 1]}"',
            )
            transformed.append({"t": "RawBlock", "c": ["html", rendered]})
            continue
        role = None
        if kind == "Header":
            level, attributes, inlines = block["c"]
            text = inline_text(inlines).strip()
            heading_id = slugify(text, used_ids)
            attributes[0] = heading_id
            role = role_for_heading(text)
            if level in {2, 3}:
                toc.append((level, heading_id, text))
        wrapper_classes = ["source-block"]
        if kind == "Table":
            wrapper_classes.append("table-wrap")
        if role:
            wrapper_classes.append(f"role-{role}")
        transformed.append({
            "t": "Div",
            "c": [["", wrapper_classes, [
                ["data-source-block", str(index)],
                ["data-source-sha256", signatures[index - 1]],
            ]], [block]],
        })
    document["blocks"] = transformed
    body = run(["pandoc", "--from", "json", "--to", "html5", "--no-highlight"], stdin=json.dumps(document))
    body = re.sub(r'<a href="(https?://)', r'<a rel="noopener noreferrer" href="\1', body)
    return body, toc, signatures


def title_from_document(document: dict, fallback: str) -> str:
    for block in document.get("blocks", []):
        if block.get("t") == "Header" and block["c"][0] == 1:
            title = inline_text(block["c"][2]).strip()
            if title:
                return title
    return fallback


def source_status(markdown: str) -> str | None:
    match = re.match(r"\A# [^\n]+\n\n> \*\*Status:\*\* ([^\n]+)(?:\n|\Z)", markdown)
    return match.group(1).strip() if match else None


def toc_html(items: list[tuple[int, str, str]]) -> str:
    links = "".join(
        f'<li data-level="{level}"><a href="#{html.escape(anchor)}">{html.escape(text)}</a></li>'
        for level, anchor, text in items
    )
    return f'<nav class="toc" aria-label="Document contents"><p class="toc-title">Contents</p><ol>{links}</ol></nav>'


def render_page(
    markdown: str,
    kind: str,
    source_label: str,
    fallback_title: str,
) -> tuple[str, int]:
    document = pandoc_document(markdown)
    title = title_from_document(document, fallback_title)
    has_mermaid = any(
        block.get("t") == "CodeBlock" and "mermaid" in block["c"][0][1]
        for block in document.get("blocks", [])
    )
    check_dependencies(has_mermaid)
    body, toc, source_signatures = transform_document(document)
    source_block_count = len(source_signatures)
    source_hash = hashlib.sha256(markdown.encode("utf-8")).hexdigest()
    styles = (ASSETS_DIR / "styles.css").read_text(encoding="utf-8")
    visible_kind = "PRD" if kind == "prd" else "Technical design"
    status = source_status(markdown)
    status_item = ""
    if status:
        status_item = (
            '<div class="metadata__item"><dt>Status</dt>'
            f'<dd>{html.escape(status)}</dd></div>'
        )
    page = f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta http-equiv="Content-Security-Policy" content="default-src 'none'; img-src data:; style-src 'unsafe-inline'; base-uri 'none'; form-action 'none'">
  <meta name="document-kind" content="{kind}">
  <meta name="source-path" content="{html.escape(source_label, quote=True)}">
  <meta name="source-sha256" content="{source_hash}">
  <meta name="generator" content="{GENERATOR}">
  <title>{html.escape(title)}</title>
  <style>{styles}</style>
</head>
<body>
  <a class="skip-link" href="#document-content">Skip to document</a>
  <header class="document-header">
    <div class="document-header__inner">
      <p class="eyebrow">{visible_kind}</p>
      <p class="document-title">{html.escape(title)}</p>
      <dl class="metadata">
        {status_item}
        <div class="metadata__item"><dt>Source</dt><dd>{html.escape(source_label)}</dd></div>
        <div class="metadata__item"><dt>SHA-256</dt><dd><code>{source_hash}</code></dd></div>
      </dl>
    </div>
  </header>
  <div class="page-shell">
    {toc_html(toc)}
    <main id="document-content" class="document-content" data-source-block-count="{source_block_count}">
{body}
    </main>
  </div>
  <footer class="document-footer">Generated from {html.escape(source_label)} by {GENERATOR}. Edit the Markdown source, then regenerate.</footer>
</body>
</html>
'''
    validate_html(page, source_signatures, kind, source_hash)
    return page, source_block_count


class StructureParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.ids: list[str] = []
        self.hrefs: list[str] = []
        self.source_blocks: list[tuple[str, str]] = []
        self.scripts = 0
        self.external_resources: list[str] = []
        self.metadata: dict[str, str] = {}

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if values.get("id"):
            self.ids.append(values["id"] or "")
        if values.get("data-source-block"):
            self.source_blocks.append((
                values["data-source-block"] or "",
                values.get("data-source-sha256") or "",
            ))
        if tag == "a" and (values.get("href") or "").startswith("#"):
            self.hrefs.append((values.get("href") or "")[1:])
        if tag == "script":
            self.scripts += 1
        if tag in {"img", "link", "iframe", "object", "embed", "source"}:
            resource = values.get("src") or values.get("href") or values.get("data") or ""
            if resource and not resource.startswith("data:"):
                self.external_resources.append(resource)
        if tag == "meta" and values.get("name"):
            self.metadata[values["name"] or ""] = values.get("content") or ""


def validate_html(page: str, expected_signatures: list[str], kind: str, source_hash: str) -> None:
    parser = StructureParser()
    parser.feed(page)
    expected_blocks = [(str(index), signature) for index, signature in enumerate(expected_signatures, start=1)]
    if parser.source_blocks != expected_blocks:
        raise GenerationError(
            "Parity check failed: source block identities or order changed"
        )
    if len(parser.ids) != len(set(parser.ids)):
        duplicates = sorted({value for value in parser.ids if parser.ids.count(value) > 1})
        raise GenerationError(f"Generated HTML contains duplicate IDs: {', '.join(duplicates)}")
    missing_targets = sorted({target for target in parser.hrefs if target not in parser.ids})
    if missing_targets:
        raise GenerationError(f"Generated navigation has missing targets: {', '.join(missing_targets)}")
    if parser.scripts or parser.external_resources:
        raise GenerationError("Generated HTML contains scripts or external runtime resources")
    if parser.metadata.get("document-kind") != kind:
        raise GenerationError("Generated document-kind metadata is not canonical")
    if parser.metadata.get("source-sha256") != source_hash:
        raise GenerationError("Generated source hash is incorrect")


def lock_path(output: Path) -> Path:
    return output.with_name(f".{output.name}.html-doc.lock")


def read_lock(output: Path) -> dict:
    path = lock_path(output)
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as error:
        raise GenerationError(f"No pending html-doc render exists for {output}") from error
    except (json.JSONDecodeError, UnicodeError) as error:
        raise GenerationError(f"Invalid stale lock at {path}; discard it explicitly") from error
    if not isinstance(data, dict):
        raise GenerationError(f"Invalid stale lock at {path}; discard it explicitly")
    return data


def acquire_lock(output: Path, candidate: Path, token: str) -> None:
    path = lock_path(output)
    payload = json.dumps({"token": token, "candidate": str(candidate), "output": str(output), "pid": os.getpid()})
    try:
        descriptor = os.open(path, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
    except FileExistsError as error:
        raise GenerationError(f"Output is locked by pending or stale state at {path}; finalize or discard it") from error
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8") as handle:
            handle.write(payload)
            handle.flush()
            os.fsync(handle.fileno())
    except BaseException:
        path.unlink(missing_ok=True)
        raise


def safe_candidate_from_lock(output: Path, data: dict) -> Path:
    candidate = Path(str(data.get("candidate", ""))).resolve()
    prefix = f"{output.name}."
    if candidate.parent != output.parent or not candidate.name.startswith(prefix) or not candidate.name.endswith(".candidate.html"):
        raise GenerationError("Lock contains an unsafe candidate path")
    return candidate


def cleanup(output: Path, candidate: Path | None) -> None:
    if candidate:
        candidate.unlink(missing_ok=True)
    lock_path(output).unlink(missing_ok=True)


def force_cleanup_stale(output: Path) -> None:
    prefix = f"{output.name}."
    for candidate in output.parent.iterdir():
        if candidate.is_file() and candidate.name.startswith(prefix) and candidate.name.endswith(".candidate.html"):
            candidate.unlink()
    lock_path(output).unlink(missing_ok=True)


def source_label(path: Path) -> str:
    resolved = path.resolve()
    try:
        return str(resolved.relative_to(Path.cwd().resolve()))
    except ValueError:
        return str(resolved)


def infer_kind(path: Path | None, explicit: str | None) -> str:
    if explicit:
        return explicit
    if path and path.name == "prd.md":
        return "prd"
    if path and path.name == "design.md":
        return "design"
    raise GenerationError("Document kind is required: use --kind prd or --kind design")


def existing_output_matches(output: Path, expected_source: str) -> bool:
    if not output.exists():
        return True
    match = re.search(r'<meta name="source-path" content="([^"]*)">', output.read_text(encoding="utf-8"))
    return bool(match and html.unescape(match.group(1)) == expected_source)


def command_render(args: argparse.Namespace) -> None:
    source_path: Path | None = None
    if args.inline:
        if not args.out:
            raise GenerationError("Inline Markdown requires --out")
        markdown = sys.stdin.read()
        label = "inline-input"
        fallback_title = "Untitled document"
    else:
        if not args.source:
            raise GenerationError("A Markdown source path is required")
        source_path = Path(args.source)
        if source_path.suffix.lower() not in {".md", ".markdown"}:
            raise GenerationError(f"Source is not Markdown: {source_path}")
        try:
            size = source_path.stat().st_size
        except OSError as error:
            raise GenerationError(f"Cannot read source {source_path}: {error}") from error
        if size > MAX_SOURCE_BYTES:
            raise GenerationError(f"Source exceeds the {MAX_SOURCE_BYTES}-byte limit: {source_path}")
        markdown = source_path.read_text(encoding="utf-8")
        label = source_label(source_path)
        fallback_title = source_path.stem.replace("-", " ").title()
    if len(markdown.encode("utf-8")) > MAX_SOURCE_BYTES:
        raise GenerationError(f"Source exceeds the {MAX_SOURCE_BYTES}-byte limit")
    kind = infer_kind(source_path, args.kind)
    explicit_output = bool(args.out)
    output = Path(args.out) if args.out else source_path.with_suffix(".html")  # type: ignore[union-attr]
    output = output.resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    if output.exists() and not explicit_output and not existing_output_matches(output, label):
        raise GenerationError(f"Refusing to replace unrelated output {output}; choose it explicitly with --out")
    token = uuid.uuid4().hex
    candidate = output.with_name(f"{output.name}.{token}.candidate.html")
    acquire_lock(output, candidate, token)
    try:
        page, source_blocks = render_page(markdown, kind, label, fallback_title)
        descriptor = os.open(candidate, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o644)
        with os.fdopen(descriptor, "w", encoding="utf-8") as handle:
            handle.write(page)
            handle.flush()
            os.fsync(handle.fileno())
    except BaseException:
        cleanup(output, candidate)
        raise
    print(json.dumps({
        "candidate": str(candidate), "output": str(output), "token": token,
        "source_blocks": source_blocks, "source_sha256": hashlib.sha256(markdown.encode()).hexdigest(),
    }))


def command_finalize(args: argparse.Namespace) -> None:
    output = Path(args.out).resolve()
    data = read_lock(output)
    candidate = safe_candidate_from_lock(output, data)
    if data.get("token") != args.token:
        raise GenerationError("Token does not match the pending render")
    try:
        if not candidate.is_file():
            raise GenerationError(f"Candidate is missing: {candidate}")
        os.replace(candidate, output)
    except BaseException:
        cleanup(output, candidate)
        raise
    lock_path(output).unlink(missing_ok=True)
    print(json.dumps({"output": str(output), "installed": True}))


def command_discard(args: argparse.Namespace) -> None:
    output = Path(args.out).resolve()
    try:
        data = read_lock(output)
    except GenerationError:
        if not args.force_stale:
            raise
        force_cleanup_stale(output)
        print(json.dumps({"output": str(output), "discarded": True, "stale": True}))
        return
    if not args.force_stale and data.get("token") != args.token:
        raise GenerationError("Token does not match the pending render; use --force-stale only for abandoned state")
    try:
        candidate = safe_candidate_from_lock(output, data)
    except GenerationError:
        if not args.force_stale:
            raise
        force_cleanup_stale(output)
    else:
        cleanup(output, candidate)
    print(json.dumps({"output": str(output), "discarded": True}))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    render_parser = commands.add_parser("render", help="Create a locked candidate for browser verification")
    render_parser.add_argument("source", nargs="?")
    render_parser.add_argument("--inline", action="store_true", help="Read exact Markdown from stdin")
    render_parser.add_argument("--kind", choices=("prd", "design"))
    render_parser.add_argument("--out")
    render_parser.set_defaults(function=command_render)
    finalize_parser = commands.add_parser("finalize", help="Atomically install a verified candidate")
    finalize_parser.add_argument("--out", required=True)
    finalize_parser.add_argument("--token", required=True)
    finalize_parser.set_defaults(function=command_finalize)
    discard_parser = commands.add_parser("discard", help="Remove a failed or stale candidate")
    discard_parser.add_argument("--out", required=True)
    discard_parser.add_argument("--token")
    discard_parser.add_argument("--force-stale", action="store_true")
    discard_parser.set_defaults(function=command_discard)
    return parser


def main() -> int:
    try:
        args = build_parser().parse_args()
        args.function(args)
        return 0
    except (GenerationError, OSError, UnicodeError) as error:
        print(f"html-doc: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
