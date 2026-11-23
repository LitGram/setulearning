# विज्ञान पुस्तक: संपादकीय स्थिति

यह संस्करण 13 विषय-अध्यायों और अध्याय 14 के 361 solved previous-exam selections का उपयोग योग्य प्रारूप है। ‘संपूर्ण NCERT समाधान’ या ‘सभी विगत वर्षों के हर प्रश्न’ का दावा नहीं करता।

## उपलब्ध

- हर अध्याय के सभी 10 भाग; स्वतंत्र chapter IDs और अगले अध्याय की conceptual bridge।
- 195 चार-विकल्पीय प्रश्न, प्रत्येक का कारण; सही विकल्प की स्थिति बदलती है।
- 78 रिक्त स्थान, 104 खुले अतिलघु प्रश्न, 78 लघु प्रश्न, 52 दीर्घ प्रश्न और 26 विस्तृत प्रश्न; सभी की answer key। MCQ/अतिलघु तथा capsule/revision जानबूझकर retrieval practice के लिए अवधारणाएँ दोहराते हैं; इन्हें कुल ‘unique questions’ की संख्या में जोड़कर दावा न करें।
- 39 मौलिक solved examples; 13 नामांकित offline diagrams; optics में वास्तविक दो-ray construction और electricity में series ammeter/parallel voltmeter circuit। शेष मुख्यतः process schematics हैं।
- 13 दस-अंकीय self-tests; स्रोत links; Hindi explanations और English terms।
- अध्याय 14 में 361 source-located solved occurrences, 18 official papers, 18 adapted revision MCQ तथा 10 नए diagrams। स्रोत register में year, main/supplementary, original question/subpart, PDF page, URL और downloaded PDF SHA-256 हैं। पुराने mechanics प्रश्न अलग flagged हैं। पूरे पेपरों के unselected questions अभी bank का हिस्सा नहीं।

## स्रोत से जाँचे गए संरचनात्मक दावे

| दावा | निष्कर्ष | स्रोत |
|---|---|---|
| विज्ञान code 07, theory 80, internal 20, अवधि 3:15 | 2026–27 के लिए सत्यापित | सामान्य 10_2027.pdf, PDF पृष्ठ 5 |
| 13 अध्याय और 6,7,5,7,8,6,7,4,8,4,7,6,5 भार | 2026–27 के लिए सत्यापित; योग 80 | उसी PDF का विज्ञान भाग |
| मोटर और induction को current core कहना | मूल योजना से हटाकर सीमा स्पष्ट | सामान्य syllabus chapter 12 में explicit सूची नहीं |
| सभी विषयों पर generic ‘लगभग 50 प्रश्न’ लागू | उपयोग नहीं किया | 2025 विज्ञान पेपर में 20 numbered questions, कई subparts |
| 2014–24 = दस परीक्षा वर्ष | गलत inclusive count; 11 वर्ष | संपादकीय सीमा स्पष्ट करनी है |
| 2026–27 सामान्य माध्यमिक syllabus से अध्याय और भार मिलान | पूरा; 13/13 अध्याय, वही भार, योग 80 | official 10_2027.pdf, PDF पृष्ठ 5–7 |
| 2026–27 सूची के विरुद्ध अध्याय-क्षेत्र मिलान | पूरा; सूचीकृत प्रमुख विषय मेल खाते हैं | official 10_2027.pdf, PDF पृष्ठ 5–7; scope notes/chapter content inspection |

## अंतिम संस्करण में आवश्यक काम

1. Official 2027 model paper review, if published, is separate from syllabus alignment. Do not substitute Praveshika or deaf-and-mute syllabi for regular Secondary.
2. प्रत्येक NCERT in-text/exercise प्रश्न का edition-specific register, paraphrased question और पूर्ण मौलिक solution; अभी examples selected concept practice हैं।
3. Selected questions का source register तैयार है; year/page/question/provenance matching still remains incomplete for historical claims elsewhere in the book. Unselected parts and the image-only 2021 file still need human/OCR verification. No claim is made that all questions in every main/supplementary paper from 2014–24 are covered.
4. सभी anatomical diagrams, nephron details, flower/human reproductive systems तथा full mirror/lens case gallery।
5. शिक्षक द्वारा claim-by-claim स्वतंत्र science accuracy और distractor review। अभी structural/data tests वैज्ञानिक peer review का विकल्प नहीं हैं।

## पुनर्निर्माण

```powershell
python tools/render_rbse10_science.py
python tools/render_rbse10_science_pyq.py
python tools/build_rbse10_science.py
python tools/audit_rbse10_science.py
flutter test test/rbse10_science_test.dart test/all_books_schema_test.dart
```

पाठ्य सामग्री: `source.py` → `ch01.md` … `ch13.md`; `pyq_source.py` → `ch14_previous_year_exams.md` तथा संयुक्त `assets/content/rbse10_science/science_book1.json`। स्रोत विवरण [PLAN.md](PLAN.md) में है।
