"""Append the independently solved official RBSE Punjabi (S-75) paper selections as Chapter 23."""

from pathlib import Path
from collections import Counter
import json
import runpy

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "10th rbse/07_punjabi"
LABELS = "ੳਅੲਸ"


def create_chapter():
    d = runpy.run_path(str(SOURCE / "pyq_source.py"))
    answers, questions = d["ANSWERS"], d["QUESTIONS"]
    manifest = json.loads(
        (ROOT / "artifacts/rbse10_punjabi/papers/manifest.json").read_text(encoding="utf-8")
    )
    papers = {p["id"]: p for p in manifest if "id" in p}
    source = runpy.run_path(str(SOURCE / "source.py"))["CHAPTERS"]
    topics = {c["number"]: c["title"] for c in source}
    topics[0] = "ਪੁਰਾਣਾ ਪਾਠਕ੍ਰਮ (2014–2017): ਵਰਤਮਾਨ 'ਸਾਹਿਤ ਸੁਗੰਧੀਆਂ' ਅਤੇ 2026 ਦੇ 80-ਅੰਕ ਬਲੂਪ੍ਰਿੰਟ ਤੋਂ ਬਾਹਰ"

    blocks = []

    def add(kind, value, **kw):
        blocks.append(dict(type=kind, value=value.strip(), **kw))

    add("heading", "ਪਾਠ ਦਾ ਉਪਯੋਗ ਅਤੇ ਸਰੋਤ ਸੀਮਾ (अध्याय का उपयोग और स्रोत सीमा)")
    counts = Counter(q["paper"] for q in questions)
    add(
        "callout",
        f"{len(questions)} ਸਰੋਤ-ਸੰਦਰਭਿਤ ਹੱਲ ਕੀਤੇ ਪ੍ਰਸ਼ਨ/ਉਪ-ਭਾਗ, {len(counts)} ਅਧਿਕਾਰਤ ਮੁੱਖ/ਪੂਰਕ ਪੇਪਰਾਂ (2014–2026) ਵਿੱਚੋਂ। ਪ੍ਰਸ਼ਨਾਂ ਦੇ ਸੰਖੇਪ ਪੰਜਾਬੀ/ਹਿੰਦੀ ਸਾਰ ਅਤੇ ਮੌਲਿਕ ਅਧਿਆਪਨ-ਹੱਲ ਦਿੱਤੇ ਗਏ ਹਨ; ਇਹ ਪੂਰੇ ਪੇਪਰਾਂ ਦਾ ਸ਼ਬਦ-ਬ-ਸ਼ਬਦ ਪੁਨਰ-ਮੁਦਰਣ ਜਾਂ ਅਧਿਕਾਰਤ ਉੱਤਰ-ਕੁੰਜੀ ਨਹੀਂ ਹੈ।",
    )
    add(
        "text",
        "ਹਰੇਕ ਪ੍ਰਸ਼ਨ ਦਾ ਸਾਲ, ਮੁੱਖ/ਪੂਰਕ ਪ੍ਰੀਖਿਆ, ਮੂਲ ਪ੍ਰਸ਼ਨ/ਉਪ-ਭਾਗ ਕ੍ਰਮਾਂਕ ਅਤੇ PDF viewer ਪੰਨਾ ਦਿੱਤਾ ਗਿਆ ਹੈ। ਛਪਿਆ ਹੋਇਆ ਪੰਨਾ ਅਤੇ PDF ਪੰਨਾ ਵੱਖ-ਵੱਖ ਹੋ ਸਕਦੇ ਹਨ। ਵੱਡੇ ਪ੍ਰਸ਼ਨਾਂ (ਅਣਡਿੱਠਾ ਪੈਰ੍ਹਾ, ਕਾਵਿ-ਵਿਆਖਿਆ, ਨਿਬੰਧ ਤੇ ਪੱਤਰ) ਦਾ ਚੋਣਵਾਂ ਸਾਰ ਅਤੇ ਆਦਰਸ਼ ਹੱਲ ਦਿੱਤਾ ਗਿਆ ਹੈ।\n\n"
        "ਮੁੱਖ ਪਾਠ 1–22 ਦੇ 80-ਅੰਕ ਭਾਰ ਵਿੱਚ ਇਹ ਅਭਿਆਸ ਪਾਠ ਵੱਖਰਾ ਵਾਧੂ ਭਾਰ ਨਹੀਂ ਜੋੜਦਾ। 2021 ਦਾ ਅभिਲੇਖੀ PDF ਕੇਵਲ ਸਕੈਨ ਇਮੇਜ ਹੋਣ ਕਾਰਨ ਇੱਥੇ ਪਾਠ-ਪ੍ਰਮਾਣਿਤ ਸਰੋਤ ਵਿੱਚ ਸ਼ਾਮਲ ਨਹੀਂ ਹੈ। 2014–2017 ਦੇ ਪੁਰਾਣੇ ਪਾਠਕ੍ਰਮ ਦੇ ਪ੍ਰਸ਼ਨਾਂ ਉੱਤੇ ਸਪੱਸ਼ਟ 'ਪੁਰਾਣਾ ਪਾਠਕ੍ਰਮ' ਟੈਗ ਲਗਾਇਆ ਗਿਆ ਹੈ।",
    )
    add("heading", "ਸਾਲ-ਵਾਰ ਸਰੋਤ ਰਜਿਸਟਰ (2014–2026)")
    lines = [
        "| ਸਾਲ / ਪ੍ਰੀਖਿਆ | ਚੁਣੇ ਪ੍ਰਸ਼ਨ/ਉਪ-ਭਾਗ | ਮੂਲ ਸਰੋਤ |",
        "|---|---:|---|",
    ]
    ids = sorted(counts, key=lambda k: (-papers[k]["year"], papers[k]["session"]))
    for pid in ids:
        p = papers[pid]
        session = "ਮੁੱਖ (Main)" if p["session"] == "main" else "ਪੂਰਕ (Supp)"
        lines.append(f"| {p['year']} / {session} | {counts[pid]} | [S-75 ਮੂਲ ਪੇਪਰ]({p['url']}) |")
    add("text", "\n".join(lines))

    add("heading", "ਲਿਖਤੀ ਉੱਤਰ ਦੀ ਪੇਸ਼ਕਾਰੀ ਵਿਧੀ")
    add(
        "text",
        "ਪਹਿਲਾਂ ਮੂਲ ਪ੍ਰਸ਼ਨ-ਪੱਤਰ ਦਾ ਪੂਰਾ ਪ੍ਰਸ਼ਨ ਪੜ੍ਹੋ, ਫਿਰ ਉੱਤਰ ਲੁਕਾ ਕੇ ਆਪ ਹੱਲ ਕਰੋ। ਕਾਵਿ-ਬੰਦ ਦੀ ਵਿਆਖਿਆ ਵਿੱਚ 'ਪ੍ਰਸੰਗ' (ਪੁਸਤਕ 'ਸਾਹਿਤ ਸੁਗੰਧੀਆਂ', ਕਵੀ ਅਤੇ ਕਵਿਤਾ ਦਾ ਨਾਂ) ਅਤੇ 'ਵਿਆਖਿਆ' ਦੋਵੇਂ ਵੱਖਰੇ ਸਿਰਲੇਖਾਂ ਹੇਠ ਲਿਖੋ; ਬਹੁ-ਅਰਥਕ ਸ਼ਬਦਾਂ ਵਿੱਚ ਅਰਥ ਦੱਸ ਕੇ ਵਾਕ ਜ਼ਰੂਰ ਬਣਾਓ; ਅਤੇ ਪੱਤਰ-ਰਚਨਾ ਵਿੱਚ ਸਹੀ ਫਾਰਮੈਟ ('ਸੇਵਾ ਵਿਖੇ' / 'ਪ੍ਰੀਖਿਆ ਭਵਨ') ਵਰਤੋ।",
    )

    provenance = []
    figures = {
        "bhasha_upbhasha_dhuni_lipi": "pyq_pun_upbhasha.png",
        "arth_bodh_virodhi_samanarthak": "pyq_pun_lipi.png",
        "rajasthan_kile_bhullar": "pyq_pun_kile.png",
        "gang_nahar_lakhiyan": "pyq_pun_gangnahar.png",
        "farid_shabad_vichar": "rbse10_pun_01.png",
        "mohan_singh_amrita_pritam": "rbse10_pun_06.png",
        "shiv_kumar_surjit_patar": "rbse10_pun_07.png",
        "ganga_din_teja_singh": "rbse10_pun_09.png",
        "milkha_singh_sarwan_singh": "rbse10_pun_10.png",
        "baghi_di_dhi_preetlari": "rbse10_pun_14.png",
        "sanjhi_kandh_dhir": "rbse10_pun_16.png",
        "dudh_da_chhappar_virk": "rbse10_pun_17.png",
    }
    shown = set()

    for pid in ids:
        p = papers[pid]
        session = "ਮੁੱਖ" if p["session"] == "main" else "ਪੂਰਕ"
        add("heading", f"{p['year']} — {session} ਪ੍ਰੀਖਿਆ")
        add("text", f"[{p['year']} {session}: ਪੂਰਾ ਅਧਿਕਾਰਤ ਪ੍ਰਸ਼ਨ-ਪੱਤਰ (S-75)]({p['url']})")
        for q in [q for q in questions if q["paper"] == pid]:
            answer = answers[q["key"]]
            topic = answer["topic"]
            number = len(provenance) + 1
            uid = f"pyq_{pid}_{number:03}"
            mark = q["marks"] + " ਅੰਕ" if q["marks"] != "-" else "ਵੱਖਰੇ ਅੰਕ ਪ੍ਰਮਾਣਿਤ ਨਹੀਂ"
            tag = "**ਪੁਰਾਣਾ ਪਾਠਕ੍ਰਮ (2014–2017):** " if topic == 0 else ""
            add("heading", f"{number}. {q['prompt']}")
            add(
                "text",
                f"**ਸਰੋਤ:** {p['year']} {session}, ਪ੍ਰਸ਼ਨ {q['ref']}, PDF ਪੰਨਾ {q['page']} · **ਅੰਕ:** {mark}\n\n"
                f"**ਪਾਠ-ਸੰਬੰਧ:** {topics[topic]}\n\n"
                f"{tag}**ਹੱਲ:** {answer['answer']}\n\n"
                f"[ਮੂਲ ਪ੍ਰਸ਼ਨ ਵੇਖੋ]({p['url']}#page={q['page']})",
            )
            if q["key"] in figures:
                fig = figures[q["key"]]
                if fig not in shown:
                    add(
                        "image",
                        fig,
                        caption=f"ਮੌਲਿਕ ਅਧਿਆਪਨ schematic: {q['prompt']} — ਮੂਲ ਪ੍ਰਸ਼ਨ-ਪੱਤਰ ਦਾ ਸਕੈਨ ਨਹੀਂ।",
                    )
                    shown.add(fig)
                else:
                    add(
                        "text",
                        "ਚਿੱਤਰ ਸਹਾਇਤਾ: ਇਸੇ ਪਾਠ ਵਿੱਚ ਇਸ ਸੰਕਲਪ ਦਾ ਪਹਿਲਾਂ ਦਿੱਤਾ ਗਿਆ ਨਾਮਾਂਕਿਤ schematic ਵੇਖੋ।",
                    )
            provenance.append(
                dict(
                    id=uid,
                    **q,
                    year=p["year"],
                    session=p["session"],
                    url=p["url"],
                    source_sha256=p["sha256"],
                    topic=topic,
                    answer=answer["answer"],
                    scope="selected original subquestion / concise paraphrase",
                    solution_author="Setu Learning; not official marking key",
                )
            )

    quiz_specs = [
        ("2026_main", "1(i)", "1173 ਈ. (ਪਿੰਡ ਖੋਤਵਾਲ, ਮੁਲਤਾਨ)", ["1469 ਈ. (ਤਲਵੰਡੀ)", "1539 ਈ. (ਲਾਹੌਰ)", "1680 ਈ. (ਕਸੂਰ)"]),
        ("2026_supplementary", "3(IX)", "ਰਾਮ ਰਤਨ ਪਟਵਾਰੀ, ਧੰਮਾ ਸਿੰਘ ਸਰਪੰਚ ਅਤੇ ਟੁੰਡਾ ਲੰਬੜਦਾਰ", ["ਹਰਨਾਮ ਸਿੰਘ, ਬਚਨ ਸਿੰਘ ਤੇ ਕਰਤਾਰਾ", "ਲਾਲ, ਦਿਆਲ ਤੇ ਜੱਗਰ", "ਕੈਲਾ, ਦੀਪਾ ਤੇ ਸੁੱਚਾ ਸਿੰਘ"]),
        ("2025_main", "1(xiii)", "ਅਗਨੀ ਕਲਸ਼ (ਗੁਰਬਚਨ ਸਿੰਘ ਭੁੱਲਰ)", ["ਨਵੇਂ ਲੋਕ (ਕੁਲਵੰਤ ਸਿੰਘ ਵਿਰਕ)", "ਪੱਖੀ (ਸੰਤੋਖ ਸਿੰਘ ਧੀਰ)", "ਮਿੱਤਰ ਪਿਆਰਾ (ਸੰਤ ਸਿੰਘ ਸੇਖੋਂ)"]),
        ("2025_supplementary", "1(xiii)", "ਖੇਤ (ਬਾਪੂ ਲਈ ਰੋਟੀ ਲੈ ਕੇ)", ["ਸਕੂਲ", "ਸ਼ਹਿਰ ਦੇ ਬਾਜ਼ਾਰ", "ਗੁਰਦੁਆਰੇ"]),
        ("2024_main", "1(ix)", "41 ਅੱਖਰ (35 ਪੈਂਤੀ + 6 ਨਵੀਨ ਟੋਲੀ)", ["35 ਅੱਖਰ", "52 ਅੱਖਰ", "26 ਅੱਖਰ"]),
        ("2024_supplementary", "1(v)", "26 ਅਕਤੂਬਰ 1927 ਈ. (ਲਾਰਡ ਇਰਵਿਨ ਵੱਲੋਂ)", ["5 ਦਸੰਬਰ 1925 ਈ.", "13 ਅਕਤੂਬਰ 1880 ਈ.", "15 ਅਗਸਤ 1947 ਈ."]),
        ("2023_main", "1(v)", "ਪਾਕਿਸਤਾਨ ਦੇ ਰਾਸ਼ਟਰਪਤੀ ਜਨਰਲ ਅਯੂਬ ਖ਼ਾਨ ਨੇ", ["ਪੰਡਿਤ ਜਵਾਹਰ ਲਾਲ ਨਹਿਰੂ ਨੇ", "ਉਸਤਾਦ ਗੁਰਦੇਵ ਸਿੰਘ ਨੇ", "ਲਾਰਡ ਇਰਵਿਨ ਨੇ"]),
        ("2022_main", "1(xi)", "ਨਿੰਦਿਆ", ["ਪ੍ਰਸ਼ੰਸਾ", "ਵਡਿਆਈ", "ਸਤਿਕਾਰ"]),
        ("2020_main", "8(ਹ)", "ਉਹਨਾਂ ਦੇ ਮਾਮੇ ਦੀ ਦਲੇਰੀ ਦੀਆਂ ਗੱਲਾਂ", ["ਪਿੰਡ ਦੇ ਸਰਪੰਚ ਦੀਆਂ ਗੱਲਾਂ", "ਪੁਲਿਸ ਵਾਲੇ ਦੀਆਂ ਗੱਲਾਂ", "ਰਾਸ਼ੇ ਦੀਆਂ ਗੱਲਾਂ"]),
        ("2020_supplementary", "8(ਠ)", "ਆਪਣੇ ਭਤੀਜੇ ਨੂੰ ਮਾਰ ਕੇ ਜੱਗਰ ਦੀ 15 ਘੁਮਾਂ ਜ਼ਮੀਨ ਹੜੱਪਣ ਲਈ", ["ਸ਼ਿਕਾਰ ਖੇਡਣ ਲਈ", "ਵਿਆਹ ਵਿੱਚ ਸ਼ਾਮਲ ਹੋਣ ਲਈ", "ਤਲਵਾਰ ਵੇਚਣ ਲਈ"]),
        ("2019_main", "8(ੲ)", "ਕਾਲੀ ਸਿੰਧ ਅਤੇ ਆਹੂ ਨਦੀਆਂ ਦੇ ਸੰਗਮ 'ਤੇ ਬਣਿਆ ਜਲ-ਦੁਰਗ", ["ਰੇਤ ਦੇ ਟਿੱਬਿਆਂ 'ਤੇ ਬਣਿਆ ਕਿਲ੍ਹਾ", "ਚਿੜੀਆ ਟੂੰਕ ਪਹਾੜੀ ਦਾ ਕਿਲ੍ਹਾ", "33 ਕਰੋੜ ਦੇਵਤਿਆਂ ਦਾ ਮੰਦਰ"]),
        ("2018_main", "8(ੲ)", "ਕੈਲੇ ਅਤੇ ਦੀਪੇ ਨੇ (ਗਹਿਣੇ ਵਾਲੀ ਜ਼ਮੀਨ ਦੇ ਝਗੜੇ ਕਾਰਨ)", ["ਕਰਤਾਰੇ ਨੇ", "ਸੁੱਚਾ ਸਿੰਘ ਨੇ", "ਦਰਬਾਰਾ ਸਿੰਘ ਨੇ"]),
        ("2018_supplementary", "8(ਸ)", "1459 ਈ. ਵਿੱਚ ਤਲਵੰਡੀ ਵਿਖੇ; ਉਹ 'ਰਬਾਬ' ਵਜਾਉਂਦੇ ਸਨ", ["1479 ਈ. ਵਿੱਚ ਬਾਸਰਕੇ ਵਿਖੇ; ਸਿਤਾਰ", ["1534 ਈ. ਵਿੱਚ ਲਾਹੌਰ ਵਿਖੇ; ਤਬਲਾ", "1563 ਈ. ਵਿੱਚ ਗੋਇੰਦਵਾਲ ਵਿਖੇ; ਢੋਲਕ"][0], "1666 ਈ. ਵਿੱਚ ਪਟਨਾ ਸਾਹਿਬ ਵਿਖੇ; ਸਰੰਗੀ"]),
        ("2017_main", "5(i)", "ਉਸਤਤ × ਨਿੰਦਿਆ ਅਤੇ ਉੱਦਮ = ਮਿਹਨਤ, ਕੋਸ਼ਿਸ਼", ["ਉਸਤਤ × ਵਡਿਆਈ", "ਆਸਤਕ × ਧਾਰਮਿਕ", "ਸੰਜੋਗ × ਮਿਲਾਪ"]),
        ("2016_main", "5(iii)", "ਬਿੰਦੀ (6 ਲਗਾਂ ਨਾਲ), ਟਿੱਪੀ (4 ਲਗਾਂ ਨਾਲ) ਅਤੇ ਅੱਧਕ (3 ਲਗਾਂ ਨਾਲ)", ["ਕੇਵਲ 1 ਲਗਾਖਰ", "5 ਦੁੱਤ ਅੱਖਰ", "12 ਸਵਰ ਅੱਖਰ"]),
        ("2015_main", "9(ਅ)", "ਭਾਈ ਵੀਰ ਸਿੰਘ ('ਸਮਾਂ' — ਰਹੀ ਵਾਸਤੇ ਘੱਤ ਸਮੇਂ ਨੇ ਇੱਕ ਨਾ ਮੰਨੀ)", ["ਸ਼ੇਖ਼ ਫ਼ਰੀਦ ਜੀ", "ਸ਼ਾਹ ਹੁਸੈਨ", "ਬੁੱਲ੍ਹੇ ਸ਼ਾਹ"]),
        ("2014_main", "1", "2 ਤੋਂ 4 ਸ਼ਬਦਾਂ ਦਾ ਕੇਂਦਰੀ ਵਿਸ਼ੇ ਉੱਤੇ ਆਧਾਰਿਤ ਸਿਰਲੇਖ", ["25 ਸ਼ਬਦਾਂ ਦਾ ਲੰਮਾ ਵਾਕ", "ਕਿਸੇ ਕਵਿਤਾ ਦੀ ਤੁਕ", "ਸਿਰਲੇਖ ਲਿਖਣ ਦੀ ਲੋੜ ਨਹੀਂ"]),
        ("2026_main", "2(vi)", "3 ਦੁੱਤ ਅੱਖਰ (ਹ, ਰ ਅਤੇ ਵ)", ["3 ਸਵਰ ਅੱਖਰ (ੳ, ਅ, ੲ)", "5 ਅਨੁਨਾਸਕੀ (ਙ, ਞ, ਣ, ਨ, ਮ)", "6 ਨਵੀਨ ਅੱਖਰ"]),
    ]
    lookup = {(q["paper"], q["ref"]): q for q in questions}
    mcqs = []
    add("heading", "PYQ ਆਧਾਰਿਤ ਦੁਹਰਾਈ ਕੁਇਜ਼ — 18 ਪ੍ਰਸ਼ਨ")
    add(
        "text",
        "ਸਾਲ-ਸੰਦਰਭ ਪ੍ਰਮਾਣਿਕ ਹਨ। ਹੇਠਾਂ ਪ੍ਰਸ਼ਨ-ਸਾਰ ਅਤੇ distractor ਵਿਕਲਪ ਲੇਖਕ ਵੱਲੋਂ ਮੁੜ-ਗਠਿਤ ਕੀਤੇ ਗਏ ਹਨ; ਇਹਨਾਂ ਨੂੰ ਮੂਲ ਪੇਪਰ ਦੇ ਵਿਕਲਪ ਅੱਖਰਾਂ ਦਾ ਪੁਨਰ-ਮੁਦਰਣ ਨਾ ਮੰਨਿਆ ਜਾਵੇ।",
    )
    for i, (pid, ref, correct, distractors) in enumerate(quiz_specs):
        q = lookup[(pid, ref)]
        choices = [correct] + distractors
        rotation = i % 4
        choices = choices[rotation:] + choices[:rotation]
        m = dict(
            question=f"[{papers[pid]['year']} {'ਮੁੱਖ' if papers[pid]['session'] == 'main' else 'ਪੂਰਕ'}, Q {ref}] {q['prompt']}",
            options=choices,
            correctIndex=choices.index(correct),
            explanation=answers[q["key"]]["answer"] + f" ਸਰੋਤ: ਪ੍ਰਸ਼ਨ {ref}, PDF ਪੰਨਾ {q['page']}।",
            sourceQuestionId=next(
                r["id"] for r in provenance if r["paper"] == pid and r["ref"] == ref
            ),
        )
        mcqs.append(m)
        add(
            "text",
            f"**ਕੁਇਜ਼ {i + 1}. {m['question']}**\n\n"
            + "\n".join(f"{LABELS[j]}) {v}  " for j, v in enumerate(choices))
            + f"\n\n**ਉੱਤਰ: {LABELS[m['correctIndex']]} — {correct}।** {m['explanation']}",
        )

    add("heading", "ਅੰਤਿਮ ਅਭਿਆਸ ਅਤੇ ਅੱਗੇ ਦੀ ਕੜੀ")
    add(
        "text",
        "ਕਿਸੇ ਇੱਕ ਸਾਲ ਦਾ ਮੂਲ ਪ੍ਰਸ਼ਨ-ਪੱਤਰ ਖੋਲ੍ਹ ਕੇ 3 ਘੰਟੇ 15 ਮਿੰਟ ਦੇ ਟਾਈਮਰ ਨਾਲ ਪੂਰਾ ਪੇਪਰ ਹੱਲ ਕਰੋ। ਚੋਣਵੇਂ ਹੱਲਾਂ ਨਾਲ ਆਪਣੇ ਉੱਤਰ ਮਿਲਾਓ। ਗ਼ਲਤ ਹੋਏ ਪ੍ਰਸ਼ਨਾਂ ਨੂੰ ਚਾਰ ਸੂਚੀਆਂ ਵਿੱਚ ਵੰਡੋ — (1) ਸਾਹਿਤ ਸੁਗੰਧੀਆਂ ਕਾਵਿ-ਵਿਆਖਿਆ ਤੇ ਕੇਂਦਰੀ ਭਾਵ, (2) ਨਿਬੰਧ ਅਤੇ ਕਹਾਣੀ ਭਾਗ ਦੇ ਸਾਰ ਤੇ ਪਾਤਰ-ਚਿਤਰਣ, (3) ਭਾਸ਼ਾ, ਉਪ-ਭਾਸ਼ਾਵਾਂ, ਧੁਨੀ, ਗੁਰਮੁਖੀ ਲਿਪੀ ਅਤੇ ਅਰਥ-ਬੋਧ, (4) ਅਣਡਿੱਠਾ ਪੈਰ੍ਹਾ, ਪੱਤਰ ਅਤੇ ਲੇਖ ਰਚਨਾ।\n\n"
        "**ਅੱਗੇ ਦੀ ਕੜੀ:** ਮੁੱਖ ਪਾਠ 1–22 ਵਿੱਚ ਜਿਸ ਵਿਸ਼ੇ ਵਿੱਚ ਗ਼ਲਤੀ ਹੋਈ ਹੋਵੇ, ਉਸ ਪਾਠ ਦੇ ਭਾਗ 2–4 ਦਾ ਦੁਬਾਰਾ ਅਭਿਆਸ ਕਰੋ। ਇਹ ਅੰਤਿਮ ਅਭਿਆਸ ਪਾਠ ਹੈ।",
    )

    for m in mcqs:
        m.pop("sourceQuestionId")

    chapter = dict(
        id="pun_ch23",
        title="ਪਾਠ 23: ਰਾਜਸਥਾਨ ਬੋਰਡ ਜਮਾਤ 10 ਪੰਜਾਬੀ — ਹੱਲ ਕੀਤੇ ਪੁਰਾਣੇ ਪ੍ਰਸ਼ਨ-ਪੱਤਰ (2014–2026)",
        subtitle="Solved Previous-Year RBSE Punjabi Examination Questions (2014–2026 Selections)",
        content=blocks,
        mcqs=mcqs,
    )
    markdown = [
        "# " + chapter["title"],
        "",
        f"**ਚੋਣਵੇਂ ਹੱਲ:** {len(provenance)} · **ਅਧਿਕਾਰਤ ਪੇਪਰ:** {len(ids)}",
        "",
    ]
    for b in blocks:
        if b["type"] == "heading":
            markdown.extend(["## " + b["value"], ""])
        elif b["type"] == "image":
            markdown.extend([f"![{b['caption']}](../../assets/images/{b['value']})", ""])
        elif b["type"] == "callout":
            markdown.extend(["> " + b["value"], ""])
        else:
            markdown.extend([b["value"], ""])

    (SOURCE / "ch23_solved_board_papers.md").write_text("\n".join(markdown), encoding="utf-8")
    (SOURCE / "pyq_provenance.json").write_text(
        json.dumps(
            dict(
                verified_date="2026-10-13",
                solved_occurrences=len(provenance),
                papers=len(ids),
                unique_solution_concepts=len({q["key"] for q in questions}),
                questions=provenance,
            ),
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    return chapter, dict(
        id="pun_ch23",
        file="10th rbse/07_punjabi/ch23_solved_board_papers.md",
        mcqs=len(mcqs),
        blocks=len(blocks),
        characters=sum(len(b["value"]) for b in blocks),
        marks=0,
        solved_questions=len(provenance),
        papers=len(ids),
    )


if __name__ == "__main__":
    chapter, stats = create_chapter()
    print(stats)
