"""Build the 21 core Sanskrit chapter manuscripts, Chapter 22 PYQ manuscript, and app JSON asset
without dropping post-quiz sections."""

from pathlib import Path
import importlib.util
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(Path(__file__).resolve().parent) not in sys.path:
    sys.path.insert(0, str(Path(__file__).resolve().parent))

SOURCE = ROOT / "10th rbse/06_sanskrit"
LABELS = "अबसद"
SYLLABUS = "https://rajeduboard.rajasthan.gov.in/anudeshika-etc/10_2027.pdf"
PAPER = "https://rajeduboard.rajasthan.gov.in/books/PAPERS-2026/Sec/S-71.pdf"


def rows(text, count=None):
    result = [line.split("|") for line in text.strip().splitlines() if line.strip()]
    if count is not None:
        assert len(result) == count, (len(result), count)
    return result


def build():
    spec = importlib.util.spec_from_file_location("sanskrit_source", SOURCE / "source.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    chapters = []
    stats = []
    for ch in module.CHAPTERS:
        n = ch["number"]
        terms = rows(ch["terms"], 10)
        worked = rows(ch["worked"], 3)
        short = rows(ch["short"], 6)
        long = rows(ch["long"], 4)
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

        heading("भाग 1: अध्याय प्रवेश एवं पाठ्यक्रम मैपिंग")
        add(
            "callout",
            "यह अध्ययन-सहायिका NCERT पाठ पर आधारित है। लेखक-रचित अभ्यासों को आधिकारिक RBSE प्रश्नों से अलग पहचानें; यह पूर्ण NCERT समाधान-संग्रह या संपूर्ण PYQ संग्रह नहीं है।",
        )
        add(
            "text",
            f"**विषय कोड:** 71 (तृतीया भाषा — संस्कृतम्) · **श्रृंखला पुस्तक:** 6\n\n"
            f"**पाठ्यक्रम आधार:** RBSE 2026–27 · **पठित-अवबोधनम्:** पूरे खंड के 32 अंक; किसी पाठ का अलग भार प्रकाशित नहीं है।\n\n"
            f"**सीखने के लक्ष्य:** {ch['goals']}",
        )
        heading("भाग 2: शब्दावली एवं अवधारणा कैप्सूल")
        add(
            "text",
            "| शब्द / सूत्र | अर्थ / उपयोग |\n|---|---|\n"
            + "\n".join(f"| {t} | {v} |" for t, v in terms),
        )
        heading("भाग 3: विस्तृत शिक्षण पाठ")
        for para in ch["theory"].strip().split("\n\n"):
            add("text", para)
        add("image", f"rbse10_san_{n:02}.png", caption=ch["caption"])
        heading("भाग 4: पाठ्यपुस्तक-अवधारणाओं पर मौलिक हल किए उदाहरण")
        add(
            "text",
            "नीचे के प्रश्न लेखक के मौलिक मॉडल हैं। ये किसी NCERT edition के प्रश्न क्रमांक या संपूर्ण in-text/exercise solution bank होने का दावा नहीं करते।",
        )
        for i, (q, a) in enumerate(worked, 1):
            add("text", f"**हल किया उदाहरण {i}: {q}**\n\n{a}")
        heading("भाग 5: सत्यापित बोर्ड प्रश्न एवं स्रोत-स्थिति")
        if ch.get("pyq"):
            add(
                "text",
                ch["pyq"]
                + f"\n\n[RBSE 2026 मूल पेपर (S-71)]({PAPER})। प्रश्न का संक्षिप्त विषय-संदर्भ है; शब्दशः पुनर्मुद्रण नहीं।",
            )
        else:
            add(
                "text",
                f"इस अध्याय का वर्षवार PYQ audit अध्याय 22 में दिया गया है। [असली 2026 बोर्ड पेपर]({PAPER}) से प्रश्न, उपभाग और अंक मिलाकर ही नया PYQ जोड़ा जाए।",
            )
        heading("भाग 6: खंडवार मौलिक अभ्यास बैंक")
        add(
            "text",
            "**अभ्यास-अंक:** लेखक के स्व-अभ्यास के लिए हैं; RBSE की आधिकारिक marking scheme नहीं। उत्तर पहले स्वयं लिखें, फिर भाग 9 देखें।",
        )
        heading("अ: बहुविकल्पीय प्रश्न — 15 × 1 अंक")
        for i, m in enumerate(mcqs, 1):
            add(
                "text",
                f"**MCQ {i}. {m['question']}**\n\n"
                + "\n".join(f"{LABELS[j]}) {o}  " for j, o in enumerate(m["options"])),
            )
        heading("अ: रिक्त स्थान — 6 × 1 अंक")
        blanks = [
            f"{definition} — इस शब्द/सूत्र का नाम है: ____।"
            for term, definition in terms[:6]
        ]
        add("text", "\n".join(f"{i}. {q}  " for i, q in enumerate(blanks, 1)))
        heading("अ: अतिलघु उत्तर — 8 × 1 अंक")
        add("text", "\n".join(f"{i}. {m[0]}  " for i, m in enumerate(raw_mcqs[:8], 1)))
        heading("ब: लघु उत्तर — 6 × 2 अंक")
        add("text", "\n\n".join(f"**B{i}.** {q}" for i, (q, _) in enumerate(short, 1)))
        heading("स: दीर्घ उत्तर — 4 × 3 अंक")
        add(
            "text",
            "आंतरिक विकल्प अभ्यास: C1 अथवा C2, तथा C3 अथवा C4 चुनें। पुनरावृत्ति में बचा विकल्प भी हल करें। यह लेखक की अभ्यास व्यवस्था है।",
        )
        add("text", "\n\n".join(f"**C{i}.** {q}" for i, (q, _) in enumerate(long, 1)))
        heading("द: विस्तृत उत्तर — 2 × 4 अंक")
        add("text", "आंतरिक विकल्प अभ्यास: D1 अथवा D2 चुनें; बाद में दूसरा भी हल करें।")
        add("text", "\n\n".join(f"**D{i}.** {q}" for i, (q, _) in enumerate(extended, 1)))
        heading("भाग 7: सावधानियाँ एवं परीक्षा-त्रुटियाँ")
        add("text", ch["traps"])
        heading("भाग 8: फटाफट पुनरावृत्ति — 25 बिंदु")
        revision = [f"{t}: {d}" for t, d in terms] + [m[-1] for m in raw_mcqs]
        add("text", "\n".join(f"{i}. {v}  " for i, v in enumerate(revision, 1)))
        heading("भाग 9: संपूर्ण अभ्यास उत्तर-कुंजी")
        heading("MCQ: सही विकल्प और कारण")
        add(
            "text",
            "\n\n".join(
                f"**{i}. {LABELS[m['correctIndex']]} — {m['options'][m['correctIndex']]}।** {m['explanation']}"
                for i, m in enumerate(mcqs, 1)
            ),
        )
        add(
            "text",
            "**रिक्त स्थान:** " + "; ".join(f"{i}. {t}" for i, (t, _) in enumerate(terms[:6], 1)),
        )
        add(
            "text",
            "**अतिलघु उत्तर:**\n\n"
            + "\n\n".join(f"{i}. {m[1]}। {m[-1]}" for i, m in enumerate(raw_mcqs[:8], 1)),
        )
        for code, questions in [("B", short), ("C", long), ("D", extended)]:
            for i, (q, a) in enumerate(questions, 1):
                add("text", f"**{code}{i}. {q}**\n\n{a}")
        heading("भाग 10: 10 मिनट / 10 अंक आत्म-मूल्यांकन एवं संदर्भ")
        ncert_link = (
            f"https://ncert.nic.in/textbook/pdf/jhsk1{n:02}.pdf"
            if n <= 10
            else "https://ncert.nic.in/textbook.php?jhsk1=0-12"
        )
        add(
            "text",
            f"समय: 10 मिनट। पहले पुस्तक बंद करें।\n\n"
            f"1. MCQ 3 और 11 हल करें। (1 + 1)\n"
            f"2. B2 और B5 के उत्तर लिखें। (2 + 2)\n"
            f"3. D1 हल करें। (4)\n\n"
            f"**कुंजी:** भाग 9 में संबंधित क्रमांक देखें। **स्व-मूल्यांकन:** 8–10: आगे बढ़ें; 5–7: छूटे कौशल का दोहराव; 0–4: भाग 2–4 फिर पढ़ें। यह अभ्यास-सुझाव है, बोर्ड grade नहीं।\n\n"
            f"[RBSE 2026–27 पाठ्यक्रम]({SYLLABUS}) · [NCERT शेमुषी भाग-2 संदर्भ]({ncert_link})\n\n"
            f"**आगे की कड़ी:** {ch['bridge']}",
        )
        chapter = dict(
            id=ch["id"],
            title=f"अध्याय {n}: {ch['title']}",
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
        path.write_text("\n".join(md), encoding="utf-8")
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

    expected_ids = [f"san_she_ch{i:02}" for i in range(1, 11)] + [
        f"san_vya_ch{i:02}" for i in range(11, 22)
    ]
    assert [c["id"] for c in chapters] == expected_ids
    assert sum(s["marks"] for s in stats) == 80

    from build_rbse10_sanskrit_pyq import create_chapter

    pyq_chapter, pyq_stats = create_chapter()
    chapters.append(pyq_chapter)
    stats.append(pyq_stats)

    asset = ROOT / "assets/content/rbse10_sanskrit/sanskrit_book1.json"
    asset.parent.mkdir(parents=True, exist_ok=True)
    asset.write_text(
        json.dumps(
            dict(
                subject="RBSE 10th Sanskrit",
                book="कक्षा 10 संस्कृत: शेमुषी एवं व्याकरण गाइड (प्रारूप)",
                editorialStatus="first-draft",
                verifiedSyllabus="2026-27",
                chapters=chapters,
            ),
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    report = ROOT / "artifacts/rbse10_sanskrit/completeness.json"
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
                    "exhaustive NCERT Abhyaswaan Bhav question coverage",
                    "unselected past-paper questions and image-only 2021 file",
                    "independent Sanskrit Acharya review",
                ],
            ),
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    print(f"Built {len(chapters)} chapters / {sum(s['mcqs'] for s in stats)} MCQs.")


if __name__ == "__main__":
    build()
