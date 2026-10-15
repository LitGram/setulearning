"""Build the 22 core Punjabi chapter manuscripts, Chapter 23 PYQ manuscript, and app JSON asset
without dropping post-quiz sections."""

from pathlib import Path
import importlib.util
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(Path(__file__).resolve().parent) not in sys.path:
    sys.path.insert(0, str(Path(__file__).resolve().parent))

SOURCE = ROOT / "10th rbse/07_punjabi"
LABELS = "ੳਅੲਸ"
SYLLABUS = "https://rajeduboard.rajasthan.gov.in/anudeshika-etc/10_2026.pdf"
PAPER = "https://rajeduboard.rajasthan.gov.in/books/PAPERS-2026/Sec/S-75.pdf"
TEXTBOOK_PDF = "../../artifacts/rbse10_punjabi/reference/textbook_cls10_punjabi.pdf"


def rows(text, min_count=1):
    result = [line.split("|") for line in text.strip().splitlines() if line.strip()]
    assert len(result) >= min_count, (len(result), min_count)
    return result


def build():
    spec = importlib.util.spec_from_file_location("punjabi_source", SOURCE / "source.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    chapters = []
    stats = []
    for ch in module.CHAPTERS:
        n = ch["number"]
        terms = rows(ch["terms"], 7)
        worked = rows(ch["worked"], 3)
        short = rows(ch["short"], 4)
        long = rows(ch["long"], 2)
        extended = rows(ch["extended"], 2)
        raw_mcqs = rows(ch["mcqs"], 15)
        mcqs = []
        for i, (question, correct, b, c, d, why) in enumerate(raw_mcqs):
            options = [correct, b, c, d]
            rotation = (i + n) % 4
            options = options[rotation:] + options[:rotation]
            mcqs.append(
                dict(
                    question=question,
                    options=options,
                    correctIndex=options.index(correct),
                    explanation=why,
                )
            )
        blocks = []

        def add(kind, value, **kwargs):
            blocks.append(dict(type=kind, value=value.strip(), **kwargs))

        def heading(text):
            add("heading", text)

        heading("भाग 1: अध्याय प्रवेश एवं पाठ्यक्रम मैपिंग (ਪਾਠ-ਪ੍ਰਵੇਸ਼ ਅਤੇ ਪਾਠਕ੍ਰਮ ਮੈਪਿੰਗ)")
        add(
            "callout",
            "ਪਹਿਲਾ ਸੰਪਾਦਕੀ ਪ੍ਰਾਰੂਪ (प्रथम संपादकीय प्रारूप)। RBSE ਜਮਾਤ 10 ਪੰਜਾਬੀ ਪਾਠ-ਪੁਸਤਕ 'ਸਾਹਿਤ ਸੁਗੰਧੀਆਂ' ਦੇ ਸਾਰੇ ਪ੍ਰਸ਼ਨਾਂ ਦੇ ਹੱਲ ਅਤੇ 2014–2026 ਦਾ ਪੂਰਾ ਇਤਿਹਾਸਕ PYQ ਸੰਗ੍ਰਹਿ ਸਰੋਤ-ਪ੍ਰੀਖਣ ਸਮੇਤ ਸੰਕਲਿਤ ਹਨ।",
        )
        add(
            "text",
            f"**ਵਿਸ਼ਾ ਕੋਡ (विषय कोड):** 75 (ਤੀਜੀ ਭਾਸ਼ਾ — ਪੰਜਾਬੀ / तृतीया भाषा — पंजाबी) · **ਲੜੀ ਪੁਸਤਕ (श्रृंखला पुस्तक):** 7\n\n"
            f"**ਪ੍ਰਮਾਣਿਤ ਆਧਾਰ:** RBSE 2025–26 · **ਪਾਠ ਅੰਕ-ਭਾਰ:** {ch['marks']} ਅੰਕ। ਇਹ ਭਾਰ ਉਸੇ ਸੰਸਕਰਣ ਦਾ ਹੈ; ਅਸਲ ਪ੍ਰਸ਼ਨ-ਵੰਡ ਦੀ ਭਵਿੱਖਬਾਣੀ ਨਹੀਂ।\n\n"
            f"**ਸਿੱਖਣ ਦੇ ਉਦੇਸ਼ (सीखने के लक्ष्य):** {ch['goals']}",
        )
        heading("भाग 2: शब्दावली एवं अवधारणा कैप्सूल (ਸ਼ਬਦਾਵਲੀ ਅਤੇ ਸੰਕਲਪ ਕੈਪਸੂਲ)")
        add(
            "text",
            "| ਸ਼ਬਦ / ਸੰਕਲਪ | ਅਰਥ / ਵਿਆਖਿਆ |\n|---|---|\n"
            + "\n".join(f"| {t} | {v} |" for t, v in terms),
        )
        heading("भाग 3: विस्तृत शिक्षण पाठ (ਵਿਸਤ੍ਰਿਤ ਅਧਿਆਪਨ ਪਾਠ)")
        for para in ch["theory"].strip().split("\n\n"):
            add("text", para)
        add("image", f"rbse10_pun_{n:02}.png", caption=ch["caption"])
        heading("भाग 4: पाठ्यपुस्तक-अवधारणाओं पर मौलिक हल किए उदाहरण (ਹੱਲ ਕੀਤੇ ਮਿਆਰੀ ਉਦਾਹਰਣ)")
        add(
            "text",
            "ਹੇਠਾਂ ਦਿੱਤੇ ਪ੍ਰਸ਼ਨ ਪਾਠ-ਪੁਸਤਕ 'ਸਾਹਿਤ ਸੁਗੰਧੀਆਂ' ਅਤੇ ਵਿਆਕਰਣ ਦੇ ਸੰਕਲਪਾਂ ਉੱਤੇ ਆਧਾਰਿਤ ਮੌਲਿਕ ਆਦਰਸ਼ ਹੱਲ ਹਨ।",
        )
        for i, (q, a) in enumerate(worked, 1):
            add("text", f"**ਹੱਲ ਕੀਤਾ ਉਦਾਹਰਣ {i}: {q}**\n\n{a}")
        heading("भाग 5: सत्यापित बोर्ड प्रश्न एवं स्रोत-स्थिति (ਪ੍ਰਮਾਣਿਤ ਬੋਰਡ ਪ੍ਰਸ਼ਨ ਅਤੇ ਸਰੋਤ-ਸਥਿਤੀ)")
        if ch.get("pyq"):
            add(
                "text",
                ch["pyq"]
                + f"\n\n[RBSE 2026 ਮੂਲ ਪੇਪਰ (S-75)]({PAPER})। ਪ੍ਰਸ਼ਨ ਦਾ ਸੰਖੇਪ ਵਿਸ਼ਾ-ਸੰਦਰਭ ਹੈ; ਸ਼ਬਦ-ਬ-ਸ਼ਬਦ ਪੁਨਰ-ਮੁਦਰਣ ਨਹੀਂ।",
            )
        else:
            add(
                "text",
                f"ਇਸ ਪਾਠ ਦਾ ਸਾਲ-ਵਾਰ PYQ ਆਡਿਟ ਪਾਠ 23 ਵਿੱਚ ਦਿੱਤਾ ਗਿਆ ਹੈ। [ਅਸਲੀ 2026 ਬੋਰਡ ਪੇਪਰ]({PAPER}) ਤੋਂ ਪ੍ਰਸ਼ਨ, ਉਪ-ਭਾਗ ਅਤੇ ਅੰਕ ਮਿਲਾ ਕੇ ਹੀ ਨਵਾਂ PYQ ਜੋੜਿਆ ਜਾਵੇ।",
            )
        heading("भाग 6: खंडवार मौलिक अभ्यास बैंक (ਖੰਡ-ਵਾਰ ਮੌਲਿਕ ਅਭਿਆਸ ਬੈਂਕ)")
        add(
            "text",
            "**ਅਭਿਆਸ-ਅੰਕ:** ਵਿਦਿਆਰਥੀਆਂ ਦੇ ਸਵੈ-ਅਭਿਆਸ ਲਈ ਹਨ; ਉੱਤਰ ਪਹਿਲਾਂ ਆਪ ਲਿਖੋ, ਫਿਰ ਭਾਗ 9 ਵੇਖੋ।",
        )
        heading("ੳ: ਬਹੁ-ਵਿਕਲਪੀ ਪ੍ਰਸ਼ਨ (MCQ) — 15 × 1 ਅੰਕ")
        for i, m in enumerate(mcqs, 1):
            add(
                "text",
                f"**MCQ {i}. {m['question']}**\n\n"
                + "\n".join(f"{LABELS[j]}) {o}  " for j, o in enumerate(m["options"])),
            )
        heading("ੳ: ਖਾਲੀ ਥਾਵਾਂ ਭਰੋ — 6 × 1 ਅੰਕ")
        blanks = [
            f"{definition} — ਇਸ ਸ਼ਬਦ/ਸੰਕਲਪ ਦਾ ਨਾਂ ਹੈ: ____।"
            for term, definition in terms[:6]
        ]
        add("text", "\n".join(f"{i}. {q}  " for i, q in enumerate(blanks, 1)))
        heading("ੳ: ਅਤਿ-ਲਘੂ ਉੱਤਰਾਂ ਵਾਲੇ ਪ੍ਰਸ਼ਨ — 8 × 1 ਅੰਕ")
        add("text", "\n".join(f"{i}. {m[0]}  " for i, m in enumerate(raw_mcqs[:8], 1)))
        heading(f"ਅ: ਲਘੂ ਉੱਤਰਾਂ ਵਾਲੇ ਪ੍ਰਸ਼ਨ — {len(short)} × 2 ਅੰਕ")
        add("text", "\n\n".join(f"**B{i}.** {q}" for i, (q, _) in enumerate(short, 1)))
        heading(f"ੲ: ਦੀਰਘ ਉੱਤਰਾਂ ਵਾਲੇ ਪ੍ਰਸ਼ਨ — {len(long)} × 3 ਅੰਕ")
        add(
            "text",
            "ਅੰਦਰੂਨੀ ਵਿਕਲਪ ਅਭਿਆਸ: ਪਹਿਲਾਂ ਇੱਕ ਵਿਕਲਪ ਹੱਲ ਕਰੋ ਅਤੇ ਦੁਹਰਾਈ ਵੇਲੇ ਬਾਕੀ ਪ੍ਰਸ਼ਨ ਵੀ ਹੱਲ ਕਰੋ।",
        )
        add("text", "\n\n".join(f"**C{i}.** {q}" for i, (q, _) in enumerate(long, 1)))
        heading(f"ਸ: ਨਿਬੰਧਾਤਮਕ / ਵਿਸਤ੍ਰਿਤ ਉੱਤਰਾਂ ਵਾਲੇ ਪ੍ਰਸ਼ਨ — {len(extended)} × 4 ਅੰਕ")
        add("text", "ਅੰਦਰੂਨੀ ਵਿਕਲਪ ਅਭਿਆਸ: D1 ਜਾਂ D2 ਚੁਣੋ; ਬਾਅਦ ਵਿੱਚ ਦੂਜਾ ਵੀ ਹੱਲ ਕਰੋ।")
        add("text", "\n\n".join(f"**D{i}.** {q}" for i, (q, _) in enumerate(extended, 1)))
        heading("भाग 7: सावधानियाँ एवं परीक्षा-त्रुटियाँ (ਸਾਵਧਾਨੀਆਂ ਅਤੇ ਪ੍ਰੀਖਿਆ-ਗ਼ਲਤੀਆਂ)")
        add("text", ch["traps"])
        heading("भाग 8: फटाफट पुनरावृत्ति — 25 बिंदु (ਫਟਾਫਟ ਦੁਹਰਾਈ — 25 ਬਿੰਦੂ)")
        revision = (
            [f"{t}: {d}" for t, d in terms]
            + [m[-1] for m in raw_mcqs]
            + [f"{q} — {a}" for q, a in worked]
        )[:25]
        add("text", "\n".join(f"{i}. {v}  " for i, v in enumerate(revision, 1)))
        heading("भाग 9: संपूर्ण अभ्यास उत्तर-कुंजी (ਸੰਪੂਰਨ ਅਭਿਆਸ ਉੱਤਰ-ਕੁੰਜੀ)")
        heading("MCQ: ਸਹੀ ਵਿਕਲਪ ਅਤੇ ਕਾਰਨ")
        add(
            "text",
            "\n\n".join(
                f"**{i}. {LABELS[m['correctIndex']]} — {m['options'][m['correctIndex']]}।** {m['explanation']}"
                for i, m in enumerate(mcqs, 1)
            ),
        )
        add(
            "text",
            "**ਖਾਲੀ ਥਾਵਾਂ:** " + "; ".join(f"{i}. {t}" for i, (t, _) in enumerate(terms[:6], 1)),
        )
        add(
            "text",
            "**ਅਤਿ-ਲਘੂ ਉੱਤਰ:**\n\n"
            + "\n\n".join(f"{i}. {m[1]}। {m[-1]}" for i, m in enumerate(raw_mcqs[:8], 1)),
        )
        for code, questions in [("B", short), ("C", long), ("D", extended)]:
            for i, (q, a) in enumerate(questions, 1):
                add("text", f"**{code}{i}. {q}**\n\n{a}")
        heading("भाग 10: 10 मिनट / 10 अंक आत्म-मूल्यांकन एवं संदर्भ (10 ਮਿੰਟ / 10 ਅੰਕ ਸਵੈ-ਮੁਲਾਂਕਣ)")
        add(
            "text",
            f"ਸਮਾਂ: 10 ਮਿੰਟ। ਪਹਿਲਾਂ ਪੁਸਤਕ ਬੰਦ ਕਰੋ।\n\n"
            f"1. MCQ 3 ਅਤੇ 11 ਹੱਲ ਕਰੋ। (1 + 1)\n"
            f"2. B1 ਅਤੇ B3 ਦੇ ਉੱਤਰ ਲਿਖੋ। (2 + 2)\n"
            f"3. D1 ਹੱਲ ਕਰੋ। (4)\n\n"
            f"**ਉੱਤਰ-ਕੁੰਜੀ:** ਭਾਗ 9 ਵਿੱਚ ਸੰਬੰਧਿਤ ਕ੍ਰਮਾਂਕ ਵੇਖੋ। **ਸਵੈ-ਮੁਲਾਂਕਣ:** 8–10: ਅੱਗੇ ਵਧੋ; 5–7: ਛੁੱਟੇ ਵਿਸ਼ੇ ਦੀ ਦੁਹਰਾਈ; 0–4: ਭਾਗ 2–4 ਦੁਬਾਰਾ ਪੜ੍ਹੋ।\n\n"
            f"[ਪ੍ਰਮਾਣਿਤ RBSE 2025–26 ਪਾਠਕ੍ਰਮ]({SYLLABUS}) · [RBSE ਸਾਹਿਤ ਸੁਗੰਧੀਆਂ ਪਾਠ-ਪੁਸਤਕ PDF]({TEXTBOOK_PDF})\n\n"
            f"**ਅੱਗੇ ਦੀ ਕੜੀ:** {ch['bridge']}",
        )
        chapter = dict(
            id=ch["id"],
            title=ch["title"],
            subtitle=ch["english"],
            content=blocks,
            mcqs=mcqs,
        )
        chapters.append(chapter)
        md = [f"# {chapter['title']} ({ch['english']})", ""]
        for b in blocks:
            if b["type"] == "heading":
                md.extend(["## " + b["value"], ""])
            elif b["type"] == "image":
                md.extend(
                    [f"![{b['caption']}](../../assets/images/{b['value']})", "", b["caption"], ""]
                )
            elif b["type"] == "callout":
                md.extend(["> " + b["value"], ""])
            else:
                md.extend([b["value"], ""])
        path = SOURCE / ch["filename"]
        md_text = "\n".join(md)
        path.write_text(md_text, encoding="utf-8")
        # Also write short alias ch01.md .. ch22.md for convenience
        (SOURCE / f"ch{n:02}.md").write_text(md_text, encoding="utf-8")
        stats.append(
            dict(
                id=chapter["id"],
                file=str(path.relative_to(ROOT)),
                mcqs=len(mcqs),
                blocks=len(blocks),
                characters=sum(len(b["value"]) for b in blocks),
                marks=ch["marks"],
            )
        )

    expected_ids = (
        [f"pun_kav_ch{i:02}" for i in range(1, 8)]
        + [f"pun_nib_ch{i:02}" for i in range(8, 14)]
        + [f"pun_kah_ch{i:02}" for i in range(14, 19)]
        + ["pun_vya_ch19", "pun_vya_ch20", "pun_rac_ch21", "pun_rac_ch22"]
    )
    assert [c["id"] for c in chapters] == expected_ids, [c["id"] for c in chapters]
    assert sum(s["marks"] for s in stats) == 80

    from build_rbse10_punjabi_pyq import create_chapter

    pyq_chapter, pyq_stats = create_chapter()
    chapters.append(pyq_chapter)
    stats.append(pyq_stats)

    asset = ROOT / "assets/content/rbse10_punjabi/punjabi_book1.json"
    asset.parent.mkdir(parents=True, exist_ok=True)
    asset.write_text(
        json.dumps(
            dict(
                subject="RBSE 10th Punjabi",
                book="ਜਮਾਤ 10 ਪੰਜਾਬੀ: ਸਾਹਿਤ ਸੁਗੰਧੀਆਂ ਅਤੇ ਵਿਆਕਰਣ ਗਾਈਡ (प्रारूप)",
                editorialStatus="first-draft",
                verifiedSyllabus="2025-26",
                chapters=chapters,
            ),
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    report = ROOT / "artifacts/rbse10_punjabi/completeness.json"
    report.parent.mkdir(parents=True, exist_ok=True)
    report.write_text(
        json.dumps(
            dict(
                chapters=stats,
                total_mcqs=sum(s["mcqs"] for s in stats),
                solved_pyqs=pyq_stats["solved_questions"],
                official_papers=pyq_stats["papers"],
                pending=[
                    "regular 2026-27 syllabus confirmation",
                    "unselected past-paper subquestions and image-only 2021 file",
                    "independent Punjabi subject-expert review",
                ],
            ),
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    print(f"Built {len(chapters)} chapters ({sum(s['mcqs'] for s in stats)} MCQs) -> {asset}")


if __name__ == "__main__":
    build()
