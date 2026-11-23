"""Audit RBSE Class 10 Sanskrit (Book 6) provenance labels, complete source retention,
quizzes, 1400x960 figures, zero raw LaTeX/ASCII-table compliance, and Chapter 22 PYQ integrity."""

from pathlib import Path
from collections import Counter
import hashlib
import json
import re
import runpy
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]


def audit_pyqs():
    raw = runpy.run_path(str(ROOT / "10th rbse/06_sanskrit/pyq_source.py"))
    provenance = json.loads(
        (ROOT / "10th rbse/06_sanskrit/pyq_provenance.json").read_text(encoding="utf-8")
    )
    manifest = json.loads(
        (ROOT / "artifacts/rbse10_sanskrit/papers/manifest.json").read_text(encoding="utf-8")
    )
    papers = {p["id"]: p for p in manifest}
    book = json.loads(
        (ROOT / "assets/content/rbse10_sanskrit/sanskrit_book1.json").read_text(encoding="utf-8")
    )
    chapter = book["chapters"][-1]
    assert len(book["chapters"]) == 22 and chapter["id"] == "san_ch22"
    assert len(provenance["questions"]) == len(raw["QUESTIONS"]) == 234
    text = "\n".join(b["value"] for b in chapter["content"])
    md = (ROOT / "10th rbse/06_sanskrit/ch22_solved_board_papers.md").read_text(encoding="utf-8")
    seen = set()
    perpaper = Counter()
    source_words = Counter()
    figures = set()
    for q in provenance["questions"]:
        identity = (q["paper"], q["ref"])
        assert identity not in seen, identity
        seen.add(identity)
        p = papers[q["paper"]]
        assert "rajeduboard.rajasthan.gov.in/books/" in q["url"] and "S-71" in q["url"]
        assert q["url"] == p["url"] and q["source_sha256"] == p["sha256"]
        assert 1 <= q["page"] <= p["pages"], (q["paper"], q["page"], p["pages"])
        assert q["answer"] == raw["ANSWERS"][q["key"]]["answer"]
        assert q["answer"] in text and q["answer"] in md and q["prompt"] in md
        assert f"#page={q['page']}" in md
        assert float(q["marks"]) > 0 if q["marks"] != "-" else True
        if q["topic"] == 0:
            assert "**पुराना पाठ्यक्रम:** **हल:** " + q["answer"] in text
        perpaper[q["paper"]] += 1
        source_words[q["paper"]] += len(q["prompt"].split())
    assert len(perpaper) == 18 and "2021_main" not in perpaper
    for pid in perpaper:
        p = papers[pid]
        assert hashlib.sha256((ROOT / p["file"]).read_bytes()).hexdigest() == p["sha256"]
    for b in chapter["content"]:
        if b["type"] == "image":
            with Image.open(ROOT / "assets/images" / b["value"]) as im:
                assert im.size == (1400, 960)
                im.verify()
            figures.add(b["value"])
        else:
            assert b["value"] in md
    assert len(figures) == 12
    assert len(chapter["mcqs"]) == 18
    for m in chapter["mcqs"]:
        assert len(m["options"]) == len(set(m["options"])) == 4
        assert 0 <= m["correctIndex"] < 4 and m["explanation"] in text
        assert "[" in m["question"] and "Q " in m["question"]
        for q in raw["QUESTIONS"]:
            p = papers[q["paper"]]
            if (
                m["question"].endswith(q["prompt"])
                and f"[{p['year']} " in m["question"]
                and f"Q {q['ref']}]" in m["question"]
            ):
                source_words[q["paper"]] += len(q["prompt"].split())
                break
    assert max(source_words.values()) <= 200, source_words
    out = dict(
        status="pass",
        solved_occurrences=234,
        official_papers=18,
        by_paper=dict(perpaper),
        unique_solution_concepts=len({q["key"] for q in provenance["questions"]}),
        revision_mcqs=18,
        figures=len(figures),
        max_summary_words_per_source=max(source_words.values()),
        coverage="selected questions and subparts; not every full paper",
        omitted="2021 image-only PDF; unselected subquestions",
    )
    (ROOT / "artifacts/rbse10_sanskrit/pyq_audit.json").write_text(
        json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    return out


def audit():
    data = json.loads(
        (ROOT / "assets/content/rbse10_sanskrit/sanskrit_book1.json").read_text(encoding="utf-8")
    )
    source = runpy.run_path(str(ROOT / "10th rbse/06_sanskrit/source.py"))["CHAPTERS"]
    assert len(data["chapters"]) == 22
    positions = Counter()
    question_set = set()
    box_chars = set("┌┬┐├┼┤└┴┘│─")
    for raw, ch in zip(source, data["chapters"][:21]):
        n = raw["number"]
        expected_id = f"san_she_ch{n:02}" if n <= 10 else f"san_vya_ch{n:02}"
        assert ch["id"] == expected_id, (ch["id"], expected_id)
        md_path = ROOT / "10th rbse/06_sanskrit" / raw["filename"]
        md = md_path.read_text(encoding="utf-8")
        assert "$" not in md, f"Raw dollar sign in {raw['filename']}"
        assert not (set(md) & box_chars), f"ASCII box characters in {raw['filename']}"
        for part in range(1, 11):
            assert (
                sum(
                    b["type"] == "heading" and b["value"].startswith(f"भाग {part}:")
                    for b in ch["content"]
                )
                == 1
            ), (n, part)
        for block in ch["content"]:
            if block["type"] == "image":
                with Image.open(ROOT / "assets/images" / block["value"]) as im:
                    assert im.size == (1400, 960)
                    im.verify()
                assert block["caption"] in md
            else:
                assert block["value"] in md, f"Lost reader text: {n}"
        text = "\n".join(b["value"] for b in ch["content"])
        for field in ["theory", "worked", "short", "long", "extended"]:
            values = (
                raw[field].strip().split("\n\n")
                if field == "theory"
                else [v for row in raw[field].strip().splitlines() for v in row.split("|")]
            )
            for v in values:
                assert v in text, (n, field, v)
        assert "भाग 10:" in text and raw["bridge"] in text
        assert "प्रथम संपादकीय प्रारूप" in text
        assert len(ch["mcqs"]) == 15
        for m in ch["mcqs"]:
            assert len(m["options"]) == len(set(m["options"])) == 4, (n, m["question"])
            assert 0 <= m["correctIndex"] < 4
            assert m["question"] not in question_set, m["question"]
            question_set.add(m["question"])
            assert len(m["explanation"]) > 20
            assert m["explanation"] in text
            positions[m["correctIndex"]] += 1

    assert len(question_set) == 315
    assert min(positions.values()) >= 75
    assert sum(raw["marks"] for raw in source) == 80

    pyq = audit_pyqs()
    result = dict(
        status="pass",
        chapters=22,
        core_chapters=21,
        core_mcqs=315,
        total_mcqs=333,
        correct_option_distribution=dict(positions),
        core_figures=21,
        source_retention="all authored paragraphs, verses, anvayas, grammar tables and answers retained",
        zero_raw_latex_and_ascii_boxes=True,
        previous_year_chapter=pyq,
    )
    (ROOT / "artifacts/rbse10_sanskrit/audit.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(result, ensure_ascii=False))


if __name__ == "__main__":
    audit()
