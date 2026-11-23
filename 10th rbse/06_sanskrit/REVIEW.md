# संस्कृत पुस्तक: संपादकीय स्थिति

यह संस्करण 21 विषय-अध्यायों (`san_she_ch01` से `san_vya_ch21`) और अध्याय 22 (`san_ch22`) के 234 solved previous-exam selections का उपयोग योग्य प्रारूप है। ‘संपूर्ण NCERT समाधान’ या ‘सभी विगत वर्षों के हर प्रश्न’ का दावा नहीं करता।

## उपलब्ध

- हर अध्याय के सभी 10 भाग (`भाग 1:` से `भाग 10:`); स्वतंत्र chapter IDs और अगले अध्याय की conceptual bridge (`आगे की कड़ी`)।
- 315 मुख्य चार-विकल्पीय प्रश्न (21 × 15) + 18 PYQ पुनरावृत्ति प्रश्न = 333 कुल बहुविकल्पीय प्रश्न, प्रत्येक का कारण; सही विकल्प की स्थिति बदलती है।
- 126 रिक्त स्थान, 168 खुले अतिलघु प्रश्न, 126 लघु प्रश्न, 84 दीर्घ प्रश्न और 42 विस्तृत प्रश्न; सभी की संपूर्ण व्याख्यात्मक उत्तर-कुंजी।
- 63 मौलिक solved examples (प्रत्येक अध्याय में 3); 21 नामांकित offline chapter schematics (`rbse10_san_01.png` … `rbse10_san_21.png`) तथा अध्याय 22 के लिए अतिरिक्त व्याकरण/घटिका/रचना schematics।
- 21 दस-अंकीय self-tests; स्रोत links; संस्कृत मूल पाठ/उदाहरण, हिंदी व्याख्याएँ और English grammatical terms।
- अध्याय 22 (`ch22_solved_board_papers.md`) में 234 source-located solved occurrences, 18 official papers (`2014_main` से `2026_supplementary`, `2021_main` image-only छोड़कर), तथा 18 adapted revision MCQ। स्रोत register (`pyq_provenance.json`) में year, main/supplementary, original question/subpart, PDF page, URL और downloaded PDF SHA-256 दर्ज हैं। पुराने पाठ्यक्रम ('स्पन्दना' 2018–2020 तथा 'शेमुषी' के हटाए गए पाठ 'व्यायामः सर्वदा पथ्यः' एवं 'प्राणेभ्योऽपि प्रियः सुहृद्') के प्रश्न अलग से `**पुराना पाठ्यक्रम:**` के रूप में चिह्नित हैं।

## स्रोत से जाँचे गए संरचनात्मक दावे

| दावा | निष्कर्ष | स्रोत |
|---|---|---|
| संस्कृत कोड 71, सैद्धांतिक 80, सत्रांक 20, अवधि 3:15 | 2025–26 एवं 2026–27 दोनों के लिए सत्यापित | `10_2026.pdf` (पृ. 17–18), `10_2027.pdf` (पृ. 18–19) |
| अपठित (8), रचनात्मक (15/16), व्याकरण (24), शेमुषी (33/32) | दोनों सत्रों के लिए सत्यापित; योग 80 | `10_2026.pdf` एवं `10_2027.pdf` |
| 'शेमुषी भाग-2' के 10 पुनर्संयोजित पाठ | सत्यापित (`jhsk101` से `jhsk110`) | NCERT rationalised textbook & RBSE syllabus |
| 2014 का आधिकारिक पेपर URL | `index.htm` में `S-71-Sankrit-TL-14.pdf` 404 है; वास्तविक सर्वर फाइल `S-71-Sankrit-14.pdf` (200 OK) सत्यापित | `PAPERS-2014/Sec/S-71-Sankrit-14.pdf` |
| 2021 मुख्य परीक्षा PDF | केवल स्कैन की गई छवि (image-only, 297 bytes text); इसलिए text-verified चयन से बाहर | `PAPERS-2021/Sec/S-71-Sanskrit-T-L.pdf` |

## अंतिम संस्करण में आवश्यक काम

1. प्रत्येक NCERT 'शेमुषी भाग-2' अभ्यास प्रश्न का edition-specific अनुक्रमांक रजिस्टर और स्वतंत्र समाधान।
2. 2021 के image-only पेपर का मानवीय लिप्यंतरण और 18 पेपरों के शेष अचयनित (unselected) दीर्घ विकल्पों का पूर्ण समावेश।
3. संस्कृत विषय-विशेषज्ञ (वरिष्ठ अध्यापक/व्याख्याता) द्वारा सभी संधि-विग्रह, अन्वय और विकल्पों (distractors) की स्वतंत्र समीक्षा।

## पुनर्निर्माण

```powershell
python -X utf8 tools/render_rbse10_sanskrit.py
python -X utf8 tools/build_rbse10_sanskrit.py
python -X utf8 tools/audit_rbse10_sanskrit.py
flutter test test/rbse10_sanskrit_test.dart test/all_books_schema_test.dart
```

पाठ्य सामग्री: `source.py` → `she_ch01_shuchiparyavaranam.md` … `rac_ch21_anuvada_ghatanakrama.md`; `pyq_source.py` → `ch22_solved_board_papers.md` तथा संयुक्त `assets/content/rbse10_sanskrit/sanskrit_book1.json`। स्रोत विवरण [PLAN.md](PLAN.md) में है।

## स्वतंत्र continuation review: 14 October 2026

- Lesson 1 का मूल NCERT 2026–27 पाठ, शब्दार्थ, 41 numbered practice items/keys, solved examples और self-test चयन जाँचे गए; त्रुटियाँ Markdown और संबंधित `source.py` content में सुधारी गईं। टूटे अक्षरों वाला raster इस lesson में पठनीय text-table से बदला गया; मूल asset नहीं बदला गया।
- 2026 मुख्य Q1(i), 2025 मुख्य Q1(i), 2025 मुख्य Q10(ii) का source matching सुधारा गया। पहले दो का प्रश्न-विषय गलत था; तीसरे का क्रमांक/पृष्ठ गलत था। तीनों का correction Chapter 22, `pyq_source.py` और `pyq_provenance.json` में है। मूल दोनों PDF hashes register से मेल खाते हैं, फिर भी question identity गलत थी; hash अकेला content verification नहीं है।
- शेष 231 selections को इस continuation ने independently source-match नहीं किया है। 234/18 counts संग्रह की संरचना बताते हैं, सभी entries की factual/provenance verification नहीं।
- वर्तमान Sanskrit syllabus के दृश्य परीक्षण में 8/16/24/32 क्षेत्र-भार मिले। अलग संधि/समास/प्रत्यय के 4-अंक आवंटन या अन्य subtopic weights नहीं मिले; README/Chapters 11–13 की framing सुधरी।
- Generator की legacy weight/header/diagram framing अभी audited Markdown के साथ पूरी तरह synchronized नहीं है। Blind regeneration पुराने दावे/diagram फिर ला सकता है; अन्य 20 chapters, सभी derivations और full textbook exercise register अभी लंबित हैं।
