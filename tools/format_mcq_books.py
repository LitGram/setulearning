#!/usr/bin/env python3
"""Remove print-only front matter and create clean Markdown copies of MCQ books."""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MARKDOWN_OUTPUT = ROOT / "books_markdown"
# These source imports are genuine objective/MCQ books. The short generated
# EnglishSetu placeholders and page-extracted school PDFs are intentionally not
# included here.
BOOKS = [
    ("englishsetu", "phonetics_objective_guide.json"),
    ("englishsetu", "geoffrey_leech_grammar.json"),
    ("englishsetu", "first_grade_literature_1.json"),
    ("englishsetu", "first_grade_literature_2.json"),
    ("englishsetu", "shakespeare_mcqs.json"),
    ("englishsetu", "mayor_casterbridge_mcqs.json"),
    ("englishsetu", "pg_topics_mcqs.json"),
    ("englishsetu", "first_grade_literature_mcqs.json"),
    ("englishsetu", "vendor_of_sweets_mcqs.json"),
    ("englishsetu", "second_grade_guide.json"),
    ("englishsetu", "second_grade_literature.json"),
    ("rassetu_supplementary", "paper4_language_essay.json"),
    ("rassetu_supplementary", "mains_answer_writing.json"),
]

FRONT_MATTER = re.compile(
    r"(?:^|\b)(?:copyright|all rights reserved|first (?:paperback )?edition|"
    r"published by|for (?:any )?permissions? requests?|for permission requests|"
    r"contact the author|email:|cover design|interior design|printed in|"
    r"disclaimer|about the author|books by the same author|made with .*notion press|"
    r"notionpress\.com|compiled by:|author:|by mukesh|mukesh\s+k\.?\s+sharma|"
    r"shiwali\s+sharma|\bauthors?:)",
    re.IGNORECASE,
)
INTRO_TITLE = re.compile(r"^(?:परिचय|introduction|preface|प्राक्कथन)$", re.IGNORECASE)


def clean_value(value: str) -> str | None:
    value = value.strip()
    if not value:
        return None
    lines = value.splitlines()
    # A chapter header block may carry a generated source metadata card.
    if any(re.search(r"\b(?:Book Number|Category|Authors?|Language):", line, re.I) for line in lines):
        return None
    if FRONT_MATTER.search(value):
        return None
    if value.startswith("©") or value.lower() in {"introduction", "परिचय"}:
        return None
    return value


def clean_book(data: dict) -> dict:
    if data.get('sourceImport', {}).get('kind') == 'ordered_docx':
        # These books were verified directly against Word XML. Broad author or
        # copyright filters can delete teaching paragraphs; never reapply them.
        return data
    cleaned = []
    for index, chapter in enumerate(data.get("chapters", [])):
        content = []
        for block in chapter.get("content", []):
            value = clean_value(str(block.get("value", "")))
            if value:
                content.append({**block, "value": value})
        mcqs = chapter.get("mcqs", [])
        title = str(chapter.get("title", "")).strip()

        # The DOCX converters put cover, author, and legal pages in a first
        # chapter called Introduction/परिचय. Do not expose that print matter.
        was_front_chapter = index == 0 and bool(INTRO_TITLE.fullmatch(title))
        had_cover = any(
            FRONT_MATTER.search(str(block.get("value", "")))
            for block in chapter.get("content", [])
        )
        if was_front_chapter and had_cover:
            continue
        if not content and not mcqs:
            continue
        cleaned.append({**chapter, "id": f"ch{len(cleaned) + 1}", "content": content})

    data["chapters"] = cleaned
    return data


def markdown_book(data: dict) -> str:
    lines = [f"# {data.get('book', 'Study Book')}", ""]
    for chapter in data["chapters"]:
        lines.extend([f"## {chapter['title']}", ""])
        for block in chapter.get("content", []):
            value = str(block.get("value", "")).strip()
            if block.get('type') == 'image':
                value = f'![Source illustration](../../assets/images/{value})'
            if value:
                lines.extend([value, ""])
        questions = chapter.get("mcqs", [])
        if questions:
            lines.extend(["### अभ्यास प्रश्न", ""])
            for number, question in enumerate(questions, 1):
                lines.extend([f"{number}. {question.get('question', '').strip()}"])
                for option_index, option in enumerate(question.get("options", [])):
                    lines.append(f"   {chr(65 + option_index)}. {option.strip()}")
                answer_index = question.get("correctIndex", 0)
                lines.append(f"   **उत्तर:** {chr(65 + answer_index)}")
                explanation = str(question.get("explanation", "")).strip()
                if explanation:
                    lines.append(f"   **व्याख्या:** {explanation}")
                lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def main() -> None:
    for folder, filename in BOOKS:
        path = ROOT / "assets" / "content" / folder / filename
        data = json.loads(path.read_text(encoding="utf-8"))
        clean_book(data)
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        markdown_path = MARKDOWN_OUTPUT / folder / path.with_suffix(".md").name
        markdown_path.parent.mkdir(parents=True, exist_ok=True)
        markdown_path.write_text(markdown_book(data), encoding="utf-8")
        print(f"{folder}/{filename}: {len(data['chapters'])} chapters -> {markdown_path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
