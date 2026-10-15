"""Append the independently solved official RBSE Sanskrit (S-71) paper selections as Chapter 22."""

from pathlib import Path
from collections import Counter
import json
import runpy

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "10th rbse/06_sanskrit"
LABELS = "अबसद"


def create_chapter():
    d = runpy.run_path(str(SOURCE / "pyq_source.py"))
    answers, questions = d["ANSWERS"], d["QUESTIONS"]
    manifest = json.loads(
        (ROOT / "artifacts/rbse10_sanskrit/papers/manifest.json").read_text(encoding="utf-8")
    )
    papers = {p["id"]: p for p in manifest if "id" in p}
    source = runpy.run_path(str(SOURCE / "source.py"))["CHAPTERS"]
    topics = {c["number"]: c["title"] for c in source}
    topics[0] = "पुराना पाठ्यक्रम (स्पन्दना / हटाए गए अध्याय): वर्तमान शेमुषी core से बाहर"

    blocks = []

    def add(kind, value, **kw):
        blocks.append(dict(type=kind, value=value.strip(), **kw))

    add("heading", "अध्याय का उपयोग और स्रोत सीमा")
    counts = Counter(q["paper"] for q in questions)
    add(
        "callout",
        f"{len(questions)} स्रोत-संदर्भित हल किए प्रश्न/उपभाग, {len(counts)} आधिकारिक मुख्य/पूरक पेपरों (2014–2026) से। प्रश्नों के संक्षिप्त संस्कृत/हिंदी सार और मौलिक शिक्षण-समाधान हैं; पूरे पेपरों का शब्दशः पुनर्मुद्रण या आधिकारिक उत्तर-कुंजी नहीं।",
    )
    add(
        "text",
        "प्रत्येक प्रश्न का वर्ष, मुख्य/पूरक परीक्षा, मूल प्रश्न/उपभाग क्रमांक और PDF viewer पृष्ठ दिया है। मुद्रित पृष्ठ और PDF पृष्ठ अलग हो सकते हैं। बड़े प्रश्न (अपठित गद्यांश, निबंधात्मक/रचनात्मक कार्य) का चयनित सार और आदर्श समाधान दिया गया है; इसे पूरे प्रश्न-पत्र का शब्दशः पुनर्मुद्रण न मानें।\n\n"
        "मुख्य अध्याय 1–21 के 80-अंक भार में यह अभ्यास अध्याय अलग अतिरिक्त भार नहीं जोड़ता। 2021 का अभिलेखीय PDF केवल स्कैन इमेज होने के कारण यहाँ पाठ-सत्यापित स्रोत में सम्मिलित नहीं है। 2018–2020 के स्पन्दना पाठ्यपुस्तक एवं हटाए गए अध्यायों के प्रश्नों पर स्पष्ट 'पुराना पाठ्यक्रम' टैग लगाया गया है।",
    )
    add("heading", "वर्षवार स्रोत रजिस्टर (2014–2026)")
    lines = [
        "| वर्ष / परीक्षा | चुने प्रश्न/उपभाग | मूल स्रोत |",
        "|---|---:|---|",
    ]
    ids = sorted(counts, key=lambda k: (-papers[k]["year"], papers[k]["session"]))
    for pid in ids:
        p = papers[pid]
        session = (
            "मुख्य"
            if p["session"] == "main"
            else ("विशेष पूरक" if pid == "2017_supplementary" else "पूरक")
        )
        lines.append(f"| {p['year']} / {session} | {counts[pid]} | [S-71 मूल पेपर]({p['url']}) |")
    add("text", "\n".join(lines))

    add("heading", "लिखित उत्तर की प्रस्तुति विधि")
    add(
        "text",
        "पहले मूल प्रश्न-पत्र का पूरा प्रश्न पढ़ें, फिर उत्तर छिपाकर स्वयं हल करें। संधि में संधि-विच्छेद और संधि का नाम दोनों लिखें; समास में विग्रह और समास का नाम दोनों दें; कारक प्रश्न में विभक्ति और कारण दोनों स्पष्ट लिखें; पत्र व संवाद में पूरी पंक्तियाँ लिखकर रिक्त-स्थान के शब्दों को रेखांकित करें; तथा घटनाक्रम में पूरे ६ वाक्य सही क्रम में लिखें।",
    )

    provenance = []
    figures = {
        "samaya_ghatika": "pyq_san_ghatika.png",
        "sandhi_purvarupa_yan": "pyq_san_sandhi.png",
        "samasa_bahuvrihi": "pyq_san_samasa.png",
        "vachya_parivartanam": "pyq_san_vachya.png",
        "vashpayanamala": "rbse10_san_01.png",
        "buddhirbalavati_sara": "rbse10_san_02.png",
        "kushalavau_ankam": "rbse10_san_03.png",
        "janani_sara": "rbse10_san_04.png",
        "sevitavyo_mahavrikshah": "rbse10_san_05.png",
        "vichitrah_sakshi_sara": "rbse10_san_07.png",
        "bhukampa_sara": "rbse10_san_09.png",
        "ekena_rajahamsena": "rbse10_san_10.png",
    }
    shown = set()

    for pid in ids:
        p = papers[pid]
        session = (
            "मुख्य"
            if p["session"] == "main"
            else ("विशेष पूरक" if pid == "2017_supplementary" else "पूरक")
        )
        add("heading", f"{p['year']} — {session} परीक्षा")
        add("text", f"[{p['year']} {session}: पूरा आधिकारिक प्रश्न-पत्र (S-71)]({p['url']})")
        for q in [q for q in questions if q["paper"] == pid]:
            answer = answers[q["key"]]
            topic = answer["topic"]
            number = len(provenance) + 1
            uid = f"pyq_{pid}_{number:03}"
            mark = q["marks"] + " अंक" if q["marks"] != "-" else "अलग अंक सत्यापित नहीं"
            tag = "**पुराना पाठ्यक्रम:** " if topic == 0 else ""
            add("heading", f"{number}. {q['prompt']}")
            add(
                "text",
                f"**स्रोत:** {p['year']} {session}, प्रश्न {q['ref']}, PDF पृष्ठ {q['page']} · **अंक:** {mark}\n\n"
                f"**अध्याय-संबंध:** {topics[topic]}\n\n"
                f"{tag}**हल:** {answer['answer']}\n\n"
                f"[मूल प्रश्न देखें]({p['url']}#page={q['page']})",
            )
            if q["key"] in figures:
                fig = figures[q["key"]]
                if fig not in shown:
                    add(
                        "image",
                        fig,
                        caption=f"मौलिक शिक्षण schematic: {q['prompt']} — मूल प्रश्न-पत्र का स्कैन नहीं।",
                    )
                    shown.add(fig)
                else:
                    add(
                        "text",
                        "चित्र सहायता: इसी अध्याय में इस अवधारणा का पहले दिया नामांकित schematic देखें।",
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
        ("2026_main", "1(x)", "सञ्जाता", ["सन्जाता", "समजाता", "सङ्जाता"]),
        ("2026_supplementary", "1(xi)", "सत् + चित्", ["सच् + चित्", "सद् + चित्", "सः + चित्"]),
        ("2025_main", "5", "पञ्चाधिकशतम् तथा पञ्चाशदधिकशतम्", ["पञ्चशतम् तथा पञ्चदशशतम्", "पञ्चाशत् तथा शतम्", "अष्टाधिकशतम् तथा द्विशतम्"]),
        ("2025_supplementary", "2(v)", "सेवमानः", ["सेवन्", "सेवितव्यः", "सेवनीयः"]),
        ("2024_main", "2(i)", "कुमारी", ["कुमारा", "कुमारिका", "कौमारी"]),
        ("2024_supplementary", "3(ब)", "पञ्चविंशत्यधिकशतम्", ["पञ्चाधिकद्विशतम्", "विंशत्यधिकशतम्", "पञ्चत्रिंशदधिकशतम्"]),
        ("2023_main", "5(ii)", "पिकः च काकः च तयोः (द्वन्द्वः)", ["पिकस्य काकः (तत्पुरुषः)", "पिकम् इव काकः (कर्मधारयः)", "पीतः काकः यस्य (बहुव्रीहिः)"]),
        ("2022_main", "4(ii)", "वाक् + ईशः (जश्त्वसन्धिः)", ["वाग + ईशः (दीर्घसन्धिः)", "वाच् + ईशः (श्चुत्वसन्धिः)", "वाः + ईशः (विसर्गसन्धिः)"]),
        ("2020_main", "16", "नाविकः", ["नाववान्", "नावता", "नावी"]),
        ("2020_supplementary", "14(iii)", "कृष्णस्य समीपम्", ["कृष्णेन सहितम्", "कृष्णं प्रति", "कृष्णानाम् अभावः"]),
        ("2019_main", "17", "शिक्षिका", ["शिक्षकी", "शैक्षिकी", "शिक्षका"]),
        ("2018_main", "18", "त्वं पाठं लिखसि", ["त्वं पाठं लिखति", "त्वया पाठं लिखसि", "अहं पाठं लिखामि"]),
        ("2018_supplementary", "15", "नृत्यन्ती", ["नृत्यमाना", "नर्तितव्या", "नृत्यता"]),
        ("2017_main", "8(i)", "जनानाम् अभावः", ["जनस्य समीपम्", "जनेन सहितम्", "जनं जनं प्रति"]),
        ("2017_supplementary", "7", "दिक् + गजः", ["दिग + गजः", "दिग् + गजः", "दिः + गजः"]),
        ("2016_main", "7", "मनः + रथः", ["मनो + रथः", "मना + रथः", "मनस् + अरथः"]),
        ("2015_main", "5", "जगत् + ईशः", ["जगद् + ईशः", "जग + दीशः", "जगः + ईशः"]),
        ("2014_main", "7(i)", "शक्तिम् अनतिक्रम्य (अव्ययीभावः)", ["शक्तेः अभावः (तत्पुरुषः)", "शक्त्या सहितम् (बहुव्रीहिः)", "शक्तिः च भक्तिः च (द्वन्द्वः)"]),
    ]
    lookup = {(q["paper"], q["ref"]): q for q in questions}
    mcqs = []
    add("heading", "PYQ आधारित पुनरावृत्ति क्विज़ — 18 प्रश्न")
    add(
        "text",
        "वर्ष-संदर्भ वास्तविक हैं। नीचे प्रश्न-सार और distractor विकल्प लेखक द्वारा पुनर्गठित हैं; इन्हें मूल पेपर के विकल्प अक्षरों का पुनर्मुद्रण न मानें।",
    )
    for i, (pid, ref, correct, distractors) in enumerate(quiz_specs):
        q = lookup[(pid, ref)]
        choices = [correct] + distractors
        rotation = i % 4
        choices = choices[rotation:] + choices[:rotation]
        m = dict(
            question=f"[{papers[pid]['year']} {'मुख्य' if papers[pid]['session'] == 'main' else 'पूरक'}, Q {ref}] {q['prompt']}",
            options=choices,
            correctIndex=choices.index(correct),
            explanation=answers[q["key"]]["answer"] + f" स्रोत: प्रश्न {ref}, PDF पृष्ठ {q['page']}।",
            sourceQuestionId=next(
                r["id"] for r in provenance if r["paper"] == pid and r["ref"] == ref
            ),
        )
        mcqs.append(m)
        add(
            "text",
            f"**क्विज़ {i + 1}. {m['question']}**\n\n"
            + "\n".join(f"{LABELS[j]}) {v}  " for j, v in enumerate(choices))
            + f"\n\n**उत्तर: {LABELS[m['correctIndex']]} — {correct}।** {m['explanation']}",
        )

    add("heading", "अंतिम अभ्यास और आगे की कड़ी")
    add(
        "text",
        "किसी एक वर्ष का मूल प्रश्न-पत्र खोलकर ३ घंटे १५ मिनट के टाइमर के साथ पूरा पेपर हल करें। चयनित समाधानों से अपने उत्तर मिलाएँ; अचयनित प्रश्नों को इस बैंक के नाम पर हल किया हुआ न मानें। गलत हुए प्रश्नों को चार सूचियों में बाँटें — (१) शेमुषी अन्वय व भावार्थ, (२) संधि-समास-प्रत्यय, (३) घटिका, वाच्य व कारक-संशोधन, (४) पत्र, चित्र/संवाद, अनुवाद व घटनाक्रम।\n\n"
        "**आगे की कड़ी:** मुख्य अध्याय 1–21 में जिस प्रकरण में त्रुटि हुई हो, उस अध्याय के भाग 2–4 का पुनः अभ्यास करें। यह अंतिम अभ्यास अध्याय है।",
    )

    for m in mcqs:
        m.pop("sourceQuestionId")

    chapter = dict(
        id="san_ch22",
        title="अध्याय 22: विगत वर्षों के हल किए बोर्ड प्रश्न-पत्र (2014–2026)",
        subtitle="Solved Previous-Year RBSE Sanskrit Examination Questions (2014–2026 Selections)",
        content=blocks,
        mcqs=mcqs,
    )
    markdown = [
        "# " + chapter["title"],
        "",
        f"**चयनित हल:** {len(provenance)} · **आधिकारिक पेपर:** {len(ids)}",
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

    (SOURCE / "ch22_solved_board_papers.md").write_text("\n".join(markdown), encoding="utf-8")
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
        id="san_ch22",
        file="10th rbse/06_sanskrit/ch22_solved_board_papers.md",
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
