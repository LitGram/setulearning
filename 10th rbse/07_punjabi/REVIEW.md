# पंजाबी पुस्तक: संपादकीय स्थिति

यह संस्करण 22 विषय-अध्यायों (`pun_kav_ch01` से `pun_rac_ch22`) और अध्याय 23 (`pun_ch23`) के 221 solved previous-exam selections का उपयोग योग्य प्रारूप है। ‘संपूर्ण पाठ्यपुस्तक समाधान’ या ‘सभी विगत वर्षों के हर प्रश्न’ का दावा नहीं करता।

## उपलब्ध

- हर अध्याय के सभी 10 भाग (`भाग 1:` से `भाग 10:`); स्वतंत्र chapter IDs और अगले अध्याय की conceptual bridge (`आगे की कड़ी`)।
- 330 मुख्य चार-विकल्पीय प्रश्न (22 × 15) + 18 PYQ पुनरावृत्ति प्रश्न = 348 कुल बहुविकल्पीय प्रश्न, प्रत्येक का कारण; सही विकल्प की स्थिति बदलती है।
- 132 रिक्त स्थान, 176 खुले अतिलघु प्रश्न, 132 लघु प्रश्न, 88 दीर्घ प्रश्न और 44 विस्तृत प्रश्न; सभी की संपूर्ण व्याख्यात्मक उत्तर-कुंजी।
- 66 मौलिक solved examples (प्रत्येक अध्याय में 3); 22 नामांकित offline chapter schematics (`rbse10_pun_01.png` … `rbse10_pun_22.png`) तथा अध्याय 23 के लिए 4 अतिरिक्त व्याकरण/साहित्य schematics (`pyq_pun_upbhasha.png`, `pyq_pun_lipi.png`, `pyq_pun_kile.png`, `pyq_pun_gangnahar.png`)।
- 22 दस-अंकीय self-tests; स्रोत links; गुरमुखी पंजाबी मूल पाठ/उदाहरण, देवनागरी हिंदी व्याख्याएँ और English grammatical/literary terms।
- अध्याय 23 (`ch23_solved_board_papers.md`) में 221 source-located solved occurrences, 17 official papers (`2014_main` से `2026_supplementary`, `2021_main` image-only छोड़कर; 2017 में पंजाबी का पूरक पेपर बोर्ड पोर्टल पर प्रकाशित नहीं था), तथा 18 adapted revision MCQ। स्रोत register (`pyq_provenance.json`) में year, main/supplementary, original question/subpart, PDF page, URL और downloaded PDF SHA-256 दर्ज हैं। पुराने पाठ्यक्रम (2014–2017 के अगेतर-पिछेतर, संक्षेप रचना, 'करामात', 'गश्त', 'दुश्मन' एकांगी, 'टालस्टाय', 'गुरु तेग बहादुर जी' आदि) के प्रश्न अलग से `**पुराना पाठ्यक्रम (2014–2017):**` के रूप में चिह्नित हैं।

## स्रोत से जाँचे गए संरचनात्मक दावे

| दावा | निष्कर्ष | स्रोत |
|---|---|---|
| पंजाबी कोड 75, सैद्धांतिक 80, सत्रांक 20, अवधि 3:15 | आधिकारिक बोर्ड पाठ्यक्रम से सत्यापित | `10_2026.pdf` (पृ. 27–28) |
| अपठित (10), निबंध (4), पत्र (4), व्याकरण (15), साहित्य सुगंधियाँ (47: कविता 20 + कहानी 14 + निबंध 13) | सत्यापित; योग = 80 अंक | `10_2026.pdf` (पृ. 27–28) एवं `2025_main.pdf`, `2026_main.pdf` |
| 'साहित्य सुगंधियाँ' (`ਸਾਹਿਤ ਸੁਗੰਧੀਆਂ`) के 13 कवि, 6 निबंध और 5 कहानियाँ | 161-पृष्ठीय आधिकारिक पाठ्यपुस्तक से पूर्णतः सत्यापित | `https://rajeduboard.rajasthan.gov.in/books-2019/cls10/Punjabi.pdf` |
| 2021 मुख्य परीक्षा PDF | केवल स्कैन की गई छवि (image-only); इसलिए text-verified चयन से बाहर | `PAPERS-2021/Sec/S-75-Punjabi.pdf` |

## अंतिम संस्करण में आवश्यक काम

1. 'साहित्य सुगंधियाँ' के प्रत्येक पाठ के अंत में दिए गए सभी पाठ्यपुस्तकीय अभ्यास प्रश्नों का अनुक्रमांक रजिस्टर और स्वतंत्र समाधान।
2. 2021 के image-only पेपर का मानवीय लिप्यंतरण और 17 पेपरों के शेष अचयनित (unselected) दीर्घ विकल्पों का पूर्ण समावेश।
3. पंजाबी विषय-विशेषज्ञ (वरिष्ठ अध्यापक/व्याख्याता) द्वारा सभी गुरमुखी वर्तनी, लगां-मात्राओं और विकल्पों (distractors) की स्वतंत्र समीक्षा।

## पुनर्निर्माण

```powershell
python -X utf8 tools/render_rbse10_punjabi.py
python -X utf8 tools/build_rbse10_punjabi_pyq.py
python -X utf8 tools/build_rbse10_punjabi.py
python -X utf8 tools/audit_rbse10_punjabi.py
flutter test test/rbse10_punjabi_test.dart test/learning_flow_test.dart
```

पाठ्य सामग्री: `source.py` → `kav_ch01_sheikh_farid_guru_nanak.md` … `rac_ch22_nibandh_ate_patar_rachna.md`; `pyq_source.py` → `ch23_solved_board_papers.md` तथा संयुक्त `assets/content/rbse10_punjabi/punjabi_book1.json`। स्रोत विवरण [PLAN.md](PLAN.md) में है।
