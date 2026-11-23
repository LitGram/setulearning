#!/usr/bin/env python3
"""Import the six publication EPUBs, excluding all book-level front matter.

Uses only the standard library. Re-run with --source-root if the collection moves.
Only numbered entry pages from the EPUB reading order become app chapters.
"""

from __future__ import annotations

import argparse
import hashlib
import html
import json
import posixpath
import re
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

APP_ROOT = Path(__file__).resolve().parents[1]
SUBJECT = "100 Great Works of All Time"
BOOKS = (
    ("novels", "100 Great Novels of All Time", "100-great-novels-guide.epub"),
    ("plays", "100 Great Plays of All Time", "100-great-plays-guide.epub"),
    ("poems", "100 Great Poems of All Time", "100-great-poems-guide.epub"),
    ("short_stories", "100 Great Short Stories of All Time",
     "release-v2/100 great short stories of all time.epub"),
    ("essays", "100 Great Essays of All Time", "100-great-essays-guide.epub"),
    ("critical_works", "100 Great Critical Works of All Time",
     "100-great-critical-works-guide.epub"),
)


def tag(element: ET.Element) -> str:
    return element.tag.rsplit("}", 1)[-1]


def text_digest(text: str) -> str:
    """Ignore layout whitespace while checking every retained character."""
    return hashlib.sha256(re.sub(r"\s+", "", text).encode("utf-8")).hexdigest()


def escape(text: str) -> str:
    return re.sub(r"([\\`*_\[\]<>$])", r"\\\1", text)


def inline(element: ET.Element) -> str:
    result = escape(element.text or "")
    for child in element:
        name = tag(child)
        value = inline(child)
        if name in {"em", "i"}:
            value = emphasis(value, "*")
        elif name in {"strong", "b"}:
            value = emphasis(value, "**")
        elif name == "a":
            href = child.get("href", "")
            if not href.startswith(("https://", "http://")):
                raise ValueError(f"Unsupported link: {href}")
            value = f"[{value}](<{href}>)"
        elif name == "br":
            value = "  \n"
        elif name not in {"span", "code"}:
            raise ValueError(f"Unsupported inline element: {name}")
        elif name == "code":
            value = f"`{''.join(child.itertext())}`"
        result += value + escape(child.tail or "")
    return result


def emphasis(value: str, marker: str) -> str:
    # Whitespace belongs outside Markdown delimiters. Otherwise EPUB spans
    # such as <em> a title </em>word leak asterisks or join adjacent words.
    match = re.fullmatch(r"(\s*)(.*?)(\s*)", value, re.DOTALL)
    before, body, after = match.groups()
    return f"{before}{marker}{body}{marker}{after}" if body else value


def repair_print_markup(container: ET.Element) -> int:
    """Restore lists that the EPUB builder left as Markdown inside paragraphs."""
    repaired = 0
    for element in container.iter():
        if tag(element) != "p":
            continue
        value = "".join(element.itertext()).strip()
        if value in {"***", "---"}:
            element.clear()
            repaired += 1
            continue
        if len(element) and tag(element[0]) == "em":
            first = element[0]
            # The source builder interpreted a bullet's '* ' as the opening
            # italic marker and the book title's opening '*' as its closing one.
            prefix = first.text or ""
            if (prefix.startswith(" ") and prefix.endswith(" ")
                    and all(tag(child) == "em" and not len(child) for child in element)
                    and any("*" in (child.tail or "") for child in element)):
                original = (element.text or "") + "".join(
                    f"*{child.text or ''}*{child.tail or ''}" for child in element)
                if original.startswith("* "):
                    original = original[2:]
                    element.clear()
                    element.tag = "li"
                    element.set("data-marker", "-")
                    previous, offset = None, 0
                    for italic in re.finditer(r"\*([^*]+)\*", original):
                        plain = original[offset:italic.start()]
                        if previous is None:
                            element.text = plain
                        else:
                            previous.tail = plain
                        previous = ET.SubElement(element, "em")
                        previous.text = italic.group(1)
                        offset = italic.end()
                    if previous is None:
                        element.text = original
                    else:
                        previous.tail = original[offset:]
                    repaired += 1
                    continue
        match = re.match(r"^\s*([-*]|\d+\.)\s+", element.text or "")
        if match:
            element.text = element.text[match.end():]
            element.tag = "li"
            element.set("data-marker", match.group(1) if match.group(1)[0].isdigit() else "-")
            repaired += 1
    return repaired


def blocks(element: ET.Element) -> list[str]:
    name = tag(element)
    if name in {"body", "main", "section"} or (name == "div" and len(element)
            and any(tag(child) in {"div", "p", "dl"} for child in element)):
        values = []
        pending = []
        for child in element:
            if tag(child) == "li":
                pending.extend(blocks(child))
                continue
            if pending:
                values.append("\n".join(pending))
                pending = []
            values.extend(blocks(child))
        if pending:
            values.append("\n".join(pending))
        return values
    if name in {"p", "div"}:
        return [inline(element).strip()]
    if name == "li":
        return [f"{element.get('data-marker', '-')} {inline(element).strip()}"]
    if re.fullmatch(r"h[1-6]", name):
        return [f"{'#' * int(name[1])} {inline(element)}"]
    if name == "blockquote":
        # Keep each printed verse line, with hard breaks, in one quotation.
        lines = [line for child in element for value in blocks(child)
                 for line in value.splitlines()]
        return ["\n".join(f"> {line}  " for line in lines)]
    if name in {"ul", "ol"}:
        return ["\n".join(
            f"{index}. {inline(child)}" if name == "ol" else f"- {inline(child)}"
            for index, child in enumerate(element, start=1))]
    if name == "dl":
        children = list(element)
        if len(children) % 2:
            raise ValueError("Incomplete metadata definition list")
        lines = []
        for index in range(0, len(children), 2):
            term, definition = children[index:index + 2]
            if (tag(term), tag(definition)) != ("dt", "dd"):
                raise ValueError("Unexpected metadata definition order")
            lines.append(f"**{inline(term)}** {inline(definition)}  ")
        return ["\n".join(lines)]
    raise ValueError(f"Unsupported block element: {name}")


def read_book(source: Path, title: str) -> tuple[dict, dict]:
    chapters, checks, omitted = [], [], []
    repairs = 0
    with zipfile.ZipFile(source) as archive:
        container = ET.fromstring(archive.read("META-INF/container.xml"))
        package_path = next(e.get("full-path") for e in container.iter()
                            if tag(e) == "rootfile")
        package = ET.fromstring(archive.read(package_path))
        folder = posixpath.dirname(package_path)
        manifest = {e.get("id"): posixpath.normpath(posixpath.join(folder, e.get("href")))
                    for e in package.iter() if tag(e) == "item"}
        for reference in (e for e in package.iter() if tag(e) == "itemref"):
            path = manifest[reference.get("idref")]
            match = re.search(r"(?:^|/)entry_(\d{3})\.xhtml$", path)
            if not match:
                omitted.append(path)
                continue
            number = int(match.group(1))
            if number != len(chapters) + 1:
                raise ValueError(f"{source.name}: missing or reordered entry {number}")
            document = ET.fromstring(archive.read(path))
            body = next(e for e in document.iter() if tag(e) == "body")
            container = next(iter(body)) if tag(next(iter(body))) == "main" else body
            heading = next(iter(container))
            if tag(heading) != "h1":
                raise ValueError(f"{path}: missing lesson heading")
            lesson_title = "".join(heading.itertext()).strip()
            lesson_title = re.sub(r"^\d+\.\s*", "", lesson_title)
            container.remove(heading)  # The reader displays the title itself.
            repairs += repair_print_markup(container)
            retained_text = "".join(container.itertext())
            content = [value for value in blocks(container) if value.strip()]
            if not content or "\ufffd" in retained_text:
                raise ValueError(f"{path}: empty or damaged text")
            chapters.append({
                "id": f"ch{number}", "title": f"{number}. {lesson_title}",
                "content": [{"type": "text", "value": value} for value in content],
                "mcqs": [],
            })
            checks.append({"id": f"ch{number}", "entry": path,
                           "source_text_sha256": text_digest(retained_text)})
    if len(chapters) != 100:
        raise ValueError(f"{source.name}: expected 100 lessons, found {len(chapters)}")
    return {"subject": SUBJECT, "book": title, "chapters": chapters}, {
        "source": str(source),
        "source_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
        "omitted_book_pages": omitted, "chapters": checks,
        "restored_list_or_emphasis_markup": repairs,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-root", type=Path,
                        default=Path(r"D:\new projects\100 great works\manuscript"))
    parser.add_argument("--verify-render", type=Path,
                        help="Check plain text emitted by audit_great_works.dart")
    args = parser.parse_args()
    report_path = APP_ROOT / "artifacts/great_works_import.json"
    if args.verify_render:
        expected = json.loads(report_path.read_text(encoding="utf-8"))
        rendered = json.loads(args.verify_render.read_text(encoding="utf-8-sig"))
        for book_id, info in expected.items():
            if len(rendered[book_id]) != 100:
                raise ValueError(f"{book_id}: rendered chapter count differs")
            for chapter in info["chapters"]:
                digest = text_digest(html.unescape(rendered[book_id][chapter["id"]]))
                if digest != chapter["source_text_sha256"]:
                    raise ValueError(f"Text changed: {book_id}/{chapter['id']}")
        print("Verified every retained character in all 600 rendered lessons.")
        return
    # Prepare all six books before writing any output.
    prepared = [(key, *read_book(args.source_root / filename, title))
                for key, title, filename in BOOKS]
    assets = APP_ROOT / "assets/content/greatworks"
    markdown = APP_ROOT / "books_markdown/great_works"
    for directory in (assets, markdown, report_path.parent):
        directory.mkdir(parents=True, exist_ok=True)
    report = {}
    for key, data, audit in prepared:
        (assets / f"{key}.json").write_text(
            json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        source = "\n\n".join(
            f"# {chapter['title']}\n\n" + "\n\n".join(b["value"] for b in chapter["content"])
            for chapter in data["chapters"])
        (markdown / f"{key}.md").write_text(source + "\n", encoding="utf-8")
        report[key] = audit
        print(f"{key}: 100 lessons; omitted {len(audit['omitted_book_pages'])} book pages")
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n",
                           encoding="utf-8")


if __name__ == "__main__":
    main()
