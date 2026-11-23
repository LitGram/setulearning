#!/usr/bin/env python3
"""Import local Markdown, DOCX, and PDF study books as Setu JSON assets."""

from __future__ import annotations

import json
import logging
import re
import sys
from dataclasses import dataclass
from pathlib import Path

from docx import Document
import pdfplumber


APP_ROOT = Path(__file__).resolve().parents[1]
ASSETS = APP_ROOT / "assets" / "content"
NEW_PROJECTS = Path(r"D:\new projects")
logging.getLogger("pdfminer").setLevel(logging.ERROR)


@dataclass(frozen=True)
class BookSpec:
    subject_id: str
    subject_name: str
    asset_name: str
    app_title: str
    source_path: Path
    source_kind: str
    book_number: int
    asset_folder: str | None = None


BOOKS = [
    # Full short-form books that fit an existing subject and have complete prose.
    BookSpec("rassetu", "RASSetu", "book52.json", "Rajasthan Flagship Schemes", NEW_PROJECTS / "short books/Book_52_Flagship_Schemes", "markdown_dir", 10, "rassetu_supplementary"),
    BookSpec("rassetu", "RASSetu", "book53.json", "Rajasthan Economy and Budget", NEW_PROJECTS / "short books/Book_53_Rajasthan_Economy", "markdown_dir", 11, "rassetu_supplementary"),
    BookSpec("rassetu", "RASSetu", "book55.json", "Administrative and General Hindi", NEW_PROJECTS / "short books/Book_55_Administrative_Hindi", "markdown_dir", 12, "rassetu_supplementary"),

    # RAS and Rajasthan competitive-exam supplements
    BookSpec("rassetu", "RASSetu", "mains_answer_writing.json", "RAS Mains: Answer Writing", NEW_PROJECTS / "ras books/book_ras_mains_answer_writing", "markdown_dir", 7, "rassetu_supplementary"),
    BookSpec("rassetu", "RASSetu", "paper4_language_essay.json", "RAS Paper IV: Language and Essay", NEW_PROJECTS / "ras books/book_paper4_language_essay", "markdown_dir", 8, "rassetu_supplementary"),
    BookSpec("rassetu", "RASSetu", "general_science.json", "General Science for Competitive Exams", NEW_PROJECTS / "ras books/general science book", "markdown_dir", 9, "rassetu_supplementary"),
    # English exam books from the archive's DOCX source files
    BookSpec("englishsetu", "EnglishSetu", "phonetics_objective_guide.json", "An Introduction to English Phonetics: Objective Guide", NEW_PROJECTS / "desktop books archive/source_docx/AN OBJECTIVE APPROACH TO English Phonetics.docx", "docx", 9),
    BookSpec("englishsetu", "EnglishSetu", "geoffrey_leech_grammar.json", "A Glossary of English Grammar: Objective Guide", NEW_PROJECTS / "desktop books archive/source_docx/AN OBJECTIVE APPROACH TO G LEECH.docx", "docx", 10),
    BookSpec("englishsetu", "EnglishSetu", "first_grade_literature_1.json", "RPSC First Grade English Literature: Part 1", NEW_PROJECTS / "desktop books archive/source_docx/RPSC First Grade (part 1).docx", "docx", 11),
    BookSpec("englishsetu", "EnglishSetu", "first_grade_literature_2.json", "RPSC First Grade English Literature: Part 2", NEW_PROJECTS / "desktop books archive/source_docx/first grade literature part 2.docx", "docx", 12),
    BookSpec("englishsetu", "EnglishSetu", "shakespeare_mcqs.json", "Mastering Shakespeare: RPSC Exam MCQs", NEW_PROJECTS / "desktop books archive/source_docx/Mastering Shakespeare MCQs for RPSC Exams.docx", "docx", 13),
    BookSpec("englishsetu", "EnglishSetu", "mayor_casterbridge_mcqs.json", "The Mayor of Casterbridge: Objective Guide", NEW_PROJECTS / "desktop books archive/source_docx/mayor of casterbridge.docx", "docx", 14),
    BookSpec("englishsetu", "EnglishSetu", "pg_topics_mcqs.json", "RPSC Postgraduate Topics: Literature MCQs", NEW_PROJECTS / "desktop books archive/source_docx/pg rpsc.docx", "docx", 15),
    BookSpec("englishsetu", "EnglishSetu", "first_grade_literature_mcqs.json", "RPSC First Grade: Literature MCQs", NEW_PROJECTS / "desktop books archive/source_docx/RPSC First Grade Exam MCQs on Literature.docx", "docx", 16),
    BookSpec("englishsetu", "EnglishSetu", "vendor_of_sweets_mcqs.json", "The Vendor of Sweets: Objective Guide", NEW_PROJECTS / "desktop books archive/source_docx/Vendor of sweets.docx", "docx", 17),
    BookSpec("englishsetu", "EnglishSetu", "second_grade_guide.json", "RPSC Second Grade English: Complete Guide", NEW_PROJECTS / "desktop books archive/source_docx/second grade new syllabus book.docx", "docx", 18),
    BookSpec("englishsetu", "EnglishSetu", "second_grade_literature.json", "RPSC Second Grade English: Literature MCQs", NEW_PROJECTS / "desktop books archive/source_docx/second grade.docx", "docx", 19),

]


QUESTION_START = re.compile(
    r"^\s*(?:#{1,6}\s*)?(?:\*\*)?(?:Q\s*\d+|Question\s*\d+|प्रश्न\s*\d+)\b\s*[.:)\-]*\s*(.*)$",
    re.IGNORECASE,
)
PLAIN_NUMBER_START = re.compile(r"^\s*(?:\*\*)?\d{1,3}[.)]\s+(.+)$")
OPTION = re.compile(r"^\s*(?:\*\*)?\(?([A-D])\)?[.)]\s*(.+?)\s*(?:\*\*)?$", re.IGNORECASE)
ANSWER = re.compile(r"(?:correct\s+answer|right\s+answer|answer|सही\s+उत्तर|उत्तर)\s*[:\-–]?\s*\(?([A-D])\)?", re.IGNORECASE)


def parse_mcqs(text: str) -> list[dict]:
    """Extract four-option questions when the source gives an explicit key."""
    lines = text.splitlines()
    starts: list[tuple[int, str]] = []
    for index, line in enumerate(lines):
        match = QUESTION_START.match(line)
        if match:
            starts.append((index, match.group(1).strip().strip("*")))
            continue
        plain = PLAIN_NUMBER_START.match(line)
        if plain and any(OPTION.match(candidate) for candidate in lines[index + 1:index + 10]):
            starts.append((index, plain.group(1).strip().strip("*")))

    mcqs = []
    for entry, (start, inline_stem) in enumerate(starts):
        end = starts[entry + 1][0] if entry + 1 < len(starts) else len(lines)
        block = lines[start:end]
        stem = [inline_stem] if inline_stem else []
        options = []
        answer_index = None
        explanation = []
        saw_answer = False
        for line in block[1:] if not inline_stem else block[1:]:
            opt = OPTION.match(line.strip().strip("*"))
            if opt and len(options) < 4:
                options.append(opt.group(2).strip().strip("*"))
                continue
            answer = ANSWER.search(line)
            if answer:
                answer_index = ord(answer.group(1).upper()) - ord("A")
                saw_answer = True
                remainder = re.sub(ANSWER, "", line, count=1).strip(" :.-–*")
                if remainder:
                    explanation.append(remainder)
                continue
            if len(options) < 4:
                cleaned = line.strip().strip("*")
                if cleaned:
                    stem.append(cleaned)
            elif saw_answer:
                cleaned = line.strip().strip("*")
                if cleaned:
                    explanation.append(cleaned)
        question = " ".join(stem).strip()
        if question and len(options) == 4 and answer_index is not None:
            mcqs.append({
                "question": question,
                "options": options,
                "correctIndex": answer_index,
                "explanation": " ".join(explanation).strip() or "उत्तर स्रोत पुस्तक की उत्तर-कुंजी के अनुसार है।",
            })
    return mcqs


def chapter_from_text(chapter_id: str, title: str, text: str, *, mcqs: list[dict] | None = None) -> dict:
    clean = text.replace("\r\n", "\n").replace("\r", "\n").strip()
    blocks = []
    for paragraph in re.split(r"\n\s*\n", clean):
        value = paragraph.strip()
        if not value:
            continue
        if value.startswith("# ") and len(value.splitlines()) == 1:
            continue
        if value in {"---", "***"}:
            continue
        blocks.append({"type": "text", "value": value})
    return {
        "id": chapter_id,
        "title": title,
        "content": blocks,
        "mcqs": mcqs if mcqs is not None else parse_mcqs(clean),
    }


def _markdown_paths(spec: BookSpec) -> list[Path]:
    if spec.source_kind == "markdown_dir":
        candidates = list(spec.source_path.glob("Chapter_[0-9][0-9].md"))
        if not candidates:
            candidates = list(spec.source_path.glob("[0-9][0-9]-*.md"))
        return sorted(candidates)
    if spec.source_kind == "mahila_dir":
        candidates = list(spec.source_path.glob("day*_chapter*.md"))
        candidates += list(spec.source_path.glob("day*_practice_set.md"))
        candidates += list(spec.source_path.glob("back_matter*.md"))
        return sorted(candidates)
    return []


def _markdown_chapters(spec: BookSpec) -> list[dict]:
    paths = _markdown_paths(spec)
    if not paths:
        raise ValueError(f"No Markdown chapters found for {spec.app_title}: {spec.source_path}")
    chapters = []
    for path in paths:
        text = path.read_text(encoding="utf-8-sig")
        first_heading = re.search(r"^#\s+(.+)$", text, re.MULTILINE)
        title = first_heading.group(1).strip() if first_heading else path.stem.replace("_", " ")
        chapters.append(chapter_from_text(f"ch{len(chapters) + 1}", title, text))
    return chapters


def _docx_chapters(spec: BookSpec) -> list[dict]:
    from recover_english_docx import recover
    asset = ASSETS / (spec.asset_folder or spec.subject_id) / spec.asset_name
    data, _, _ = recover(asset, spec.source_path)
    return data['chapters']


def _pdf_chapters(spec: BookSpec) -> list[dict]:
    chapters = []
    with pdfplumber.open(spec.source_path) as pdf:
        extracted = [(page.page_number, (page.extract_text() or "").strip()) for page in pdf.pages]
    text_pages = [(number, text) for number, text in extracted if text]
    if len(text_pages) < max(1, int(len(extracted) * 0.8)):
        raise ValueError(f"PDF text extraction coverage is too low for {spec.app_title}: {len(text_pages)}/{len(extracted)} pages")
    chunk_size = 8
    for offset in range(0, len(text_pages), chunk_size):
        chunk = text_pages[offset:offset + chunk_size]
        first_page, last_page = chunk[0][0], chunk[-1][0]
        body = "\n\n".join(f"### पृष्ठ {page_number}\n{text}" for page_number, text in chunk)
        chapters.append(chapter_from_text(
            f"ch{len(chapters) + 1}",
            f"पृष्ठ {first_page}–{last_page}",
            body,
        ))
    return chapters


def import_book(spec: BookSpec) -> tuple[int, int, int]:
    if not spec.source_path.exists():
        raise FileNotFoundError(spec.source_path)
    if spec.source_kind in {"markdown_dir", "mahila_dir"}:
        chapters = _markdown_chapters(spec)
    elif spec.source_kind == "docx":
        chapters = _docx_chapters(spec)
    elif spec.source_kind == "pdf":
        chapters = _pdf_chapters(spec)
    else:
        raise ValueError(f"Unsupported source kind: {spec.source_kind}")

    output_path = ASSETS / (spec.asset_folder or spec.subject_id) / spec.asset_name
    output_path.parent.mkdir(parents=True, exist_ok=True)
    book = {"subject": spec.subject_name, "book": spec.app_title, "chapters": chapters}
    if spec.source_kind == 'docx':
        book['sourceImport'] = {'kind': 'ordered_docx'}
    with output_path.open("w", encoding="utf-8", newline="\n") as stream:
        json.dump(book, stream, ensure_ascii=False, indent=2)
        stream.write("\n")
    return len(chapters), sum(len(ch["mcqs"]) for ch in chapters), output_path.stat().st_size


def main() -> None:
    results = []
    errors = []
    for spec in BOOKS:
        try:
            chapters, mcqs, size = import_book(spec)
            results.append((spec, chapters, mcqs, size))
            print(f"{spec.subject_id:16} {spec.app_title}: {chapters} chapters, {mcqs} interactive MCQs, {size:,} bytes")
        except Exception as error:
            errors.append((spec, error))
            print(f"ERROR {spec.app_title}: {error}", file=sys.stderr)
    if errors:
        raise SystemExit(f"Imported {len(results)} books; {len(errors)} failed")
    print(f"Imported {len(results)} books successfully.")
    import subprocess

    subprocess.run(
        [sys.executable, str(APP_ROOT / "tools" / "format_mcq_books.py")],
        check=True,
    )


if __name__ == "__main__":
    main()
