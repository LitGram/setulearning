# RBSE कक्षा 10: पुस्तक 2 — विज्ञान

13 विषय-अध्याय तथा अंतिम **अध्याय 14: पिछले वर्षों के हल किए परीक्षा प्रश्न** तैयार हैं और ऐप catalog में **कक्षा 10 विज्ञान** के अंतर्गत उपलब्ध होंगे। APK दोबारा build/install करने पर नया catalog मिलेगा; पहले से installed APK अपने-आप नहीं बदलता।

[अध्यायवार योजना](PLAN.md) · [संपादकीय समीक्षा और शेष कार्य](REVIEW.md)

| अध्याय | पाठ |
|---|---|
| 1 | [रासायनिक अभिक्रियाएँ एवं समीकरण](ch01.md) |
| 2 | [अम्ल, क्षारक एवं लवण](ch02.md) |
| 3 | [धातु एवं अधातु](ch03.md) |
| 4 | [कार्बन एवं उसके यौगिक](ch04.md) |
| 5 | [जैव प्रक्रम](ch05.md) |
| 6 | [नियंत्रण एवं समन्वय](ch06.md) |
| 7 | [जीव जनन कैसे करते हैं?](ch07.md) |
| 8 | [आनुवंशिकता](ch08.md) |
| 9 | [प्रकाश: परावर्तन तथा अपवर्तन](ch09.md) |
| 10 | [मानव नेत्र तथा रंगबिरंगा संसार](ch10.md) |
| 11 | [विद्युत](ch11.md) |
| 12 | [विद्युत धारा के चुंबकीय प्रभाव](ch12.md) |
| 13 | [हमारा पर्यावरण](ch13.md) |
| 14 | [पिछले वर्षों के हल किए परीक्षा प्रश्न](ch14_previous_year_exams.md) |

मुख्य 13 पाठों में 10 शिक्षण भाग, 15 MCQ, हल किए उदाहरण, written practice, answer key, revision और self-test हैं। अंतिम अध्याय में **361 हल किए परीक्षा-प्रश्न/उपभाग**, **18 आधिकारिक पेपर**, वर्ष/परीक्षा/प्रश्न/PDF-page references, 18 adapted revision MCQ तथा 10 नए diagrams हैं। पूरे book में 213 MCQ और 23 अलग offline figures हैं। Repeated exam occurrences अलग references सहित हैं; count unique concepts की नहीं।

स्रोत वर्ष: 2014–2020 तथा 2022–2026। Main papers के साथ 2017, 2018, 2020, 2024, 2025 और 2026 supplementary selections शामिल हैं। 2021 image-only source को verified question bank में नहीं जोड़ा गया। Exact original wording के लिए प्रत्येक solution का official link खोलें; यहाँ question summaries तथा मौलिक teaching answers हैं, official marking key नहीं।

## सत्यापन

- Python content/source-retention audit: pass; 14 chapter IDs, 213 valid MCQ; PYQ references/source hashes और 25 numerical checks।
- Flutter focused checks: 4 passed; actual bundled asset loading, सभी PYQ answers/references retained, science catalog schema तथा phone-width diagram display/zoom। Log: `artifacts/rbse10_science/pyq_flutter_tests.log`।
- Targeted Flutter analysis: no issues found।
- Library-wide suite: science schema passed; existing RAS geography catalog mismatch (27 expected versus 39 actual) remains unresolved outside this book's scope।
- Scientific teacher peer review: pending; structural tests उसके बराबर नहीं हैं।

## पुनर्निर्माण

मौलिक authoring data [source.py](source.py) तथा [pyq_source.py](pyq_source.py) में है। Source references और solutions का register [pyq_provenance.json](pyq_provenance.json) में है। Generated Markdown और JSON को सीधे बदलने की जगह source बदलें और `python tools/build_rbse10_science.py` चलाएँ। मुख्य चित्रों के लिए `python tools/render_rbse10_science.py`; PYQ चित्रों के लिए `python tools/render_rbse10_science_pyq.py`।

ऐप JSON: `assets/content/rbse10_science/science_book1.json`। Build/audit output: `artifacts/rbse10_science/`।
