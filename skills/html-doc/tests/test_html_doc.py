from __future__ import annotations

from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from html.parser import HTMLParser
import importlib.util
import json
from pathlib import Path
import re
import subprocess
import tempfile
import threading
from types import SimpleNamespace
import unittest
from unittest import mock


SKILL_DIR = Path(__file__).resolve().parents[1]
SCRIPT = SKILL_DIR / "scripts" / "html_doc.py"
SPEC = importlib.util.spec_from_file_location("html_doc", SCRIPT)
assert SPEC and SPEC.loader
html_doc = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(html_doc)


def ast_visible_text(node: object) -> str:
    if isinstance(node, list):
        return " ".join(ast_visible_text(child) for child in node if isinstance(child, (dict, list)))
    if not isinstance(node, dict):
        return ""
    kind = node.get("t")
    content = node.get("c")
    if kind == "Str":
        return str(content)
    if kind in {"Space", "SoftBreak", "LineBreak"}:
        return " "
    if kind in {"Code", "Math"}:
        return str(content[-1])
    if kind in {"CodeBlock", "RawBlock"}:
        return str(content[1])
    if kind in {"Link", "Image"}:
        return ast_visible_text(content[1])
    if kind == "Header":
        return ast_visible_text(content[2])
    return ast_visible_text(content)


def normalized(value: str) -> str:
    value = value.replace("☒", "").replace("☐", "")
    return re.sub(r"\s+([:,.])", r"\1", " ".join(value.split()))


class SourceTextParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.in_main = False
        self.current: str | None = None
        self.text: dict[str, list[str]] = {}

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if tag == "main":
            self.in_main = True
        if self.in_main and values.get("data-source-block"):
            self.current = values["data-source-block"]
            self.text[self.current] = []

    def handle_endtag(self, tag: str) -> None:
        if tag == "main":
            self.in_main = False
            self.current = None

    def handle_data(self, data: str) -> None:
        if self.in_main and self.current:
            self.text[self.current].append(data)


class HtmlDocTests(unittest.TestCase):
    def run_cli(self, *arguments: str, stdin: str | None = None) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            ["python3", str(SCRIPT), *arguments],
            input=stdin,
            text=True,
            capture_output=True,
            check=False,
        )

    def test_render_candidate_then_finalize(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "design.md"
            output = root / "design.html"
            markdown = (SKILL_DIR / "tests" / "fixtures" / "design.md").read_text()
            source.write_text(markdown)

            rendered = self.run_cli("render", str(source), "--out", str(output))
            self.assertEqual(rendered.returncode, 0, rendered.stderr)
            result = json.loads(rendered.stdout)
            candidate = Path(result["candidate"])
            self.assertTrue(candidate.is_file())
            self.assertFalse(output.exists())
            self.assertEqual(source.read_text(), markdown)

            page = candidate.read_text()
            self.assertIn('<meta name="document-kind" content="design">', page)
            self.assertIn('<dd>Proposed</dd>', page)
            self.assertIn('id="repeated"', page)
            self.assertIn('id="repeated-2"', page)
            self.assertIn('id="section"', page)
            self.assertIn('id="section-2"', page)
            self.assertIn("data:image/svg+xml;base64,", page)
            self.assertIn("Diagram 1 showing Queue Worker", page)
            self.assertEqual(page.count("data-source-block="), result["source_blocks"])

            finalized = self.run_cli(
                "finalize", "--out", str(output), "--token", result["token"]
            )
            self.assertEqual(finalized.returncode, 0, finalized.stderr)
            self.assertEqual(output.read_text(), page)
            self.assertFalse(candidate.exists())

    def test_prd_and_design_ast_content_stays_in_source_order(self) -> None:
        for name, kind in (("prd.md", "prd"), ("design.md", "design")):
            with self.subTest(name=name):
                markdown = (SKILL_DIR / "tests" / "fixtures" / name).read_text()
                document = html_doc.pandoc_document(markdown)
                original_blocks = document["blocks"]
                expected_signatures = [html_doc.block_signature(block) for block in original_blocks]
                page, count = html_doc.render_page(markdown, kind, f"fixtures/{name}", name)
                structure = html_doc.StructureParser()
                structure.feed(page)
                self.assertEqual(count, len(original_blocks))
                self.assertEqual(
                    structure.source_blocks,
                    [(str(index), signature) for index, signature in enumerate(expected_signatures, 1)],
                )
                rendered_text = SourceTextParser()
                rendered_text.feed(page)
                for index, block in enumerate(original_blocks, 1):
                    classes = block.get("c", [["", [], []]])[0][1] if block.get("t") == "CodeBlock" else []
                    if "mermaid" in classes:
                        continue
                    self.assertEqual(
                        normalized("".join(rendered_text.text[str(index)])),
                        normalized(ast_visible_text(block)),
                        f"content changed in source block {index} of {name}",
                    )

    def test_pending_render_excludes_concurrent_render_and_can_be_discarded(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "design.md"
            output = root / "view.html"
            source.write_text("# Design\n\n## Decision\n\nKeep one writer.\n")
            first = self.run_cli("render", str(source), "--out", str(output))
            self.assertEqual(first.returncode, 0, first.stderr)
            first_result = json.loads(first.stdout)

            second = self.run_cli("render", str(source), "--out", str(output))
            self.assertNotEqual(second.returncode, 0)
            self.assertIn("locked", second.stderr)

            discarded = self.run_cli(
                "discard", "--out", str(output), "--token", first_result["token"]
            )
            self.assertEqual(discarded.returncode, 0, discarded.stderr)
            self.assertFalse(Path(first_result["candidate"]).exists())
            self.assertFalse(html_doc.lock_path(output.resolve()).exists())

    def test_interrupted_render_cleans_candidate_and_lock(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "design.md"
            output = root / "view.html"
            source.write_text("# Design\n")
            arguments = SimpleNamespace(
                inline=False, source=str(source), out=str(output), kind=None
            )
            with mock.patch.object(html_doc, "render_page", side_effect=KeyboardInterrupt):
                with self.assertRaises(KeyboardInterrupt):
                    html_doc.command_render(arguments)
            self.assertFalse(html_doc.lock_path(output.resolve()).exists())
            self.assertEqual(list(root.glob("*.candidate.html")), [])

    def test_default_output_does_not_replace_unrelated_html(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "design.md"
            output = root / "design.html"
            source.write_text("# Design\n")
            output.write_text("unrelated")
            rendered = self.run_cli("render", str(source))
            self.assertNotEqual(rendered.returncode, 0)
            self.assertIn("unrelated output", rendered.stderr)
            self.assertEqual(output.read_text(), "unrelated")

    def test_failed_final_replace_preserves_previous_output_and_cleans_state(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "design.md"
            output = root / "view.html"
            old = b"previous verified output"
            source.write_text("# Design\n\n## Decision\n\nKeep one writer.\n")
            output.write_bytes(old)
            rendered = self.run_cli("render", str(source), "--out", str(output))
            self.assertEqual(rendered.returncode, 0, rendered.stderr)
            result = json.loads(rendered.stdout)

            with mock.patch.object(html_doc.os, "replace", side_effect=OSError("simulated")):
                with self.assertRaises(OSError):
                    html_doc.command_finalize(SimpleNamespace(out=str(output), token=result["token"]))
            self.assertEqual(output.read_bytes(), old)
            self.assertFalse(Path(result["candidate"]).exists())
            self.assertFalse(html_doc.lock_path(output.resolve()).exists())

    def test_resource_bearing_mermaid_is_rejected_before_render(self) -> None:
        hostile = "flowchart LR\nA-->B\nclick A https://127.0.0.1:8765/steal"
        with mock.patch.object(html_doc, "run") as renderer:
            with self.assertRaisesRegex(html_doc.GenerationError, "forbidden resource syntax"):
                html_doc.render_mermaid(hostile, 1)
        renderer.assert_not_called()

    def test_svg_allowlist_rejects_active_content_and_external_urls(self) -> None:
        fixtures = (
            b'<svg xmlns="http://www.w3.org/2000/svg"><script>bad()</script></svg>',
            b'<svg xmlns="http://www.w3.org/2000/svg"><image href="https://bad.test/x"/></svg>',
            b'<svg xmlns="http://www.w3.org/2000/svg" onload="bad()"/>',
            b'<svg xmlns="http://www.w3.org/2000/svg"><style>.x{fill:u\\72l(\\68ttps://bad.test/x)}</style></svg>',
        )
        for fixture in fixtures:
            with self.subTest(fixture=fixture):
                with self.assertRaises(html_doc.GenerationError):
                    html_doc.validate_svg(fixture)

    def test_unsafe_html_and_url_schemes_do_not_enter_generated_dom(self) -> None:
        markdown = "# Design\n\n<script>alert(1)</script>\n\n[bad](javascript:alert(1))\n"
        page, _ = html_doc.render_page(markdown, "design", "inline-input", "Design")
        self.assertNotIn("<script>", page)
        self.assertNotIn('href="javascript:', page)
        self.assertIn("&lt;script&gt;", page)

    def test_locked_package_versions_and_real_mermaid_render(self) -> None:
        html_doc.check_dependencies(True)
        markdown = (SKILL_DIR / "tests" / "fixtures" / "design.md").read_text()
        page, blocks = html_doc.render_page(markdown, "design", "tests/fixtures/design.md", "Design")
        self.assertGreater(blocks, 1)
        self.assertIn("data:image/svg+xml;base64,", page)

    def test_generated_ids_cannot_collide_with_source_headings(self) -> None:
        markdown = "# Design\n\n## Document content\n\nOne.\n\n## Source block 1\n\nTwo.\n\n## cb1\n\n```python\nprint(1)\n```\n"
        page, _ = html_doc.render_page(markdown, "design", "inline-input", "Design")
        parser = html_doc.StructureParser()
        parser.feed(page)
        self.assertEqual(len(parser.ids), len(set(parser.ids)))
        self.assertIn("document-content-2", parser.ids)
        self.assertIn("source-block-1", parser.ids)
        self.assertIn("cb1", parser.ids)

    def test_force_stale_removes_malformed_lock_and_known_candidates(self) -> None:
        for output_name, other_name in (
            ("view.html", "other.html.deadbeef.candidate.html"),
            ("view[1].html", "view1.html.deadbeef.candidate.html"),
            ("*.html", "unrelated.html.deadbeef.candidate.html"),
        ):
            with self.subTest(output=output_name), tempfile.TemporaryDirectory() as directory:
                output = Path(directory) / output_name
                candidate = output.with_name(f"{output.name}.deadbeef.candidate.html")
                other = output.with_name(other_name)
                candidate.write_text("partial")
                other.write_text("keep")
                html_doc.lock_path(output).write_text("{partial")
                discarded = self.run_cli("discard", "--out", str(output), "--force-stale")
                self.assertEqual(discarded.returncode, 0, discarded.stderr)
                self.assertFalse(candidate.exists())
                self.assertEqual(other.read_text(), "keep")
                self.assertFalse(html_doc.lock_path(output).exists())

    def test_chromium_cannot_reach_controlled_endpoint(self) -> None:
        class Handler(BaseHTTPRequestHandler):
            requests = 0

            def do_GET(self) -> None:  # noqa: N802
                Handler.requests += 1
                self.send_response(204)
                self.end_headers()

            def log_message(self, format: str, *args: object) -> None:
                pass

        server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        url = f"http://127.0.0.1:{server.server_port}/probe"
        config = json.loads((SKILL_DIR / "assets" / "puppeteer.json").read_text())
        script = f'''
import puppeteer from "puppeteer";
const browser = await puppeteer.launch({{headless: true, args: {json.dumps(config["args"])}}});
const page = await browser.newPage();
let blocked = false;
try {{ await page.goto({json.dumps(url)}, {{timeout: 3000}}); }} catch {{ blocked = true; }}
await browser.close();
if (!blocked) process.exit(2);
'''
        try:
            result = subprocess.run(
                ["node", "--input-type=module", "--eval", script],
                cwd=SKILL_DIR,
                text=True,
                capture_output=True,
                timeout=15,
                check=False,
            )
        finally:
            server.shutdown()
            server.server_close()
            thread.join(timeout=2)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(Handler.requests, 0)


if __name__ == "__main__":
    unittest.main()
