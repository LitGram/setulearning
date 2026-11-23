"""Bundle the RBSE Class 10 Markdown study guides as offline app books.

The reviewed subject Markdown remains the source of truth. Questions and keys
stay in each reading chapter as Markdown; these imported books do not invent
interactive MCQ keys.
"""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE_ROOT = ROOT / "10th rbse"
ASSETS_ROOT = ROOT / "assets" / "content"
IMAGE_ROOT = ROOT / "assets" / "images"
CONFIG = [
    ("01_maths", "rbse10_maths", "गणित", "कक्षा 10 गणित: अध्ययन एवं अभ्यास"),
    ("03_social_science", "rbse10_social", "सामाजिक विज्ञान", "कक्षा 10 सामाजिक विज्ञान: अध्ययन एवं अभ्यास"),
    ("04_hindi", "rbse10_hindi", "हिन्दी", "कक्षा 10 हिन्दी: अध्ययन एवं अभ्यास"),
    ("05_english", "rbse10_english", "English", "Class 10 English: Study and Practice"),
]
IMAGE_RE = re.compile(r"!\[([^\]]*)\]\(([^)\s]+)(?:\s+\"([^\"]*)\")?\)")
HEADING_RE = re.compile(r"^(#{2})\s+(.+?)\s*$")


def markdown_sources(folder: Path) -> list[Path]:
    readme = (folder / "README.md").read_text(encoding="utf-8")
    ordered: list[Path] = []
    seen: set[Path] = set()
    for match in re.finditer(r"(?<![\w./-])([\w-]+\.md)", readme):
        path = folder / match.group(1)
        if path.is_file() and path not in seen and path.name.upper() not in {
            "README.MD",
            "PLAN.MD",
            "REVIEW.MD",
        }:
            ordered.append(path)
            seen.add(path)
    expected = {
        path.resolve()
        for path in folder.glob("*.md")
        if path.name.upper() not in {"README.MD", "PLAN.MD", "REVIEW.MD"}
    }
    missing = sorted(expected - {path.resolve() for path in ordered})
    if missing:
        raise ValueError(
            f"README index omits source chapters in {folder.name}: "
            + ", ".join(path.name for path in missing)
        )
    if not ordered:
        raise ValueError(f"No indexed Markdown chapters found in {folder}")
    return ordered


def add_text(blocks: list[dict], value: str) -> None:
    value = value.strip()
    if value and value not in {"---", "***", "___"}:
        blocks.append({"type": "text", "value": value})


def text_and_images(value: str) -> list[dict]:
    blocks: list[dict] = []
    offset = 0
    for match in IMAGE_RE.finditer(value):
        add_text(blocks, value[offset : match.start()])
        alt, target, title = match.groups()
        filename = Path(target.replace("\\", "/")).name
        image_path = IMAGE_ROOT / filename
        caption = title or alt
        if image_path.is_file():
            blocks.append({"type": "image", "value": filename, "caption": caption})
        else:
            add_text(blocks, f"**चित्र संदर्भ:** {caption or filename}")
        offset = match.end()
    add_text(blocks, value[offset:])
    return blocks


def chapter_from_markdown(path: Path) -> dict:
    source = path.read_text(encoding="utf-8")
    source = source.replace("\x0crac", r"\frac").replace("\x0c", "")
    lines = source.splitlines()
    title = path.stem.replace("_", " ")
    start = 0
    for index, line in enumerate(lines):
        if line.strip():
            match = re.match(r"^#\s+(.+?)\s*$", line.strip())
            if match:
                title = match.group(1)
                start = index + 1
            break

    blocks: list[dict] = []
    current: list[str] = []
    fenced = False

    def flush() -> None:
        value = "\n".join(current).strip()
        if value:
            blocks.extend(text_and_images(value))
        current.clear()

    for line in lines[start:]:
        if line.strip().startswith("```"):
            fenced = not fenced
        heading = None if fenced else HEADING_RE.match(line)
        if heading:
            flush()
            blocks.append({"type": "heading", "value": heading.group(2).strip()})
            continue
        current.append(line)
    flush()

    return {
        "id": path.stem,
        "title": title,
        "content": blocks,
        "mcqs": [],
    }


def build() -> dict:
    manifest: dict = {"generatedFrom": "10th rbse Markdown indexed by each subject README"}
    for source_folder, subject_id, subject_name, book_title in CONFIG:
        folder = SOURCE_ROOT / source_folder
        chapters = [chapter_from_markdown(path) for path in markdown_sources(folder)]
        output_folder = ASSETS_ROOT / subject_id
        output_folder.mkdir(parents=True, exist_ok=True)
        output = output_folder / f"{subject_id}_book1.json"
        book = {"subject": subject_name, "book": book_title, "chapters": chapters}
        output.write_text(json.dumps(book, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        manifest[subject_id] = {
            "asset": output.relative_to(ROOT).as_posix(),
            "chapterCount": len(chapters),
            "chapters": [chapter["id"] for chapter in chapters],
            "readingBlocks": sum(len(chapter["content"]) for chapter in chapters),
            "images": sum(
                block["type"] == "image"
                for chapter in chapters
                for block in chapter["content"]
            ),
        }
        print(
            f"{subject_id}: {len(chapters)} chapters, "
            f"{manifest[subject_id]['readingBlocks']} reading blocks, "
            f"{manifest[subject_id]['images']} offline images -> {output}"
        )
    manifest_path = ROOT / "artifacts" / "rbse10_reading_assets.json"
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return manifest


if __name__ == "__main__":
    build()
