from html.parser import HTMLParser
from pathlib import Path
import re
import subprocess
import tempfile
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parents[2]
HTML_PATH = ROOT / "index.html"
README_PATH = ROOT / "README.md"


class PageAudit(HTMLParser):
    def __init__(self):
        super().__init__()
        self.local_refs = []
        self.inline_scripts = []
        self._capture_script = False
        self._script_parts = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        for key in ("src", "href"):
            value = attrs.get(key)
            if value:
                self.local_refs.append(value)
        if tag == "script":
            self._capture_script = not attrs.get("src")
            self._script_parts = []

    def handle_data(self, data):
        if self._capture_script:
            self._script_parts.append(data)

    def handle_endtag(self, tag):
        if tag == "script":
            if self._capture_script:
                self.inline_scripts.append("".join(self._script_parts))
            self._capture_script = False
            self._script_parts = []


def is_external_or_anchor(value):
    parsed = urlparse(value)
    return bool(parsed.scheme or parsed.netloc or value.startswith("#"))


def check_local_reference(value, base_dir):
    if is_external_or_anchor(value):
        return
    path = unquote(urlparse(value).path)
    if not path:
        return
    target = (base_dir / path.lstrip("/")).resolve()
    if not target.is_file():
        raise SystemExit(f"Missing local reference: {value} (resolved to {target})")


def main():
    html = HTML_PATH.read_text(encoding="utf-8")
    parser = PageAudit()
    parser.feed(html)
    if "<title" not in html.lower():
        raise SystemExit("index.html has no title element")

    for ref in parser.local_refs:
        check_local_reference(ref, ROOT)

    links = re.findall(r"\[[^\]]+\]\(([^)]+)\)", README_PATH.read_text(encoding="utf-8"))
    for ref in links:
        check_local_reference(ref, ROOT)

    if not parser.inline_scripts:
        raise SystemExit("No inline scripts found to validate")
    for index, script in enumerate(parser.inline_scripts, start=1):
        with tempfile.NamedTemporaryFile("w", suffix=".js", encoding="utf-8") as temp:
            temp.write(script)
            temp.flush()
            subprocess.run(["node", "--check", temp.name], check=True)
        print(f"Inline script {index}: syntax OK")

    print(f"HTML and README links: {len(parser.local_refs) + len(links)} checked; all local targets exist")


if __name__ == "__main__":
    main()
