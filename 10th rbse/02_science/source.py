"""Original chapter-by-chapter teaching manuscript data. Build with tools/build_rbse10_science.py."""
CHAPTERS = []

def chapter(number, title, english, marks, goals, terms, theory, worked, short, long, extended, mcqs, traps, caption, diagram, bridge, pyq=''):
    CHAPTERS.append(dict(number=number, title=title, english=english, marks=marks, goals=goals, terms=terms, theory=theory, worked=worked, short=short, long=long, extended=extended, mcqs=mcqs, traps=traps, caption=caption, diagram=diagram, bridge=bridge, pyq=pyq))

chapter(1, 'रासायनिक अभिक्रियाएँ एवं समीकरण', 'Chemical Reactions and Equations', 6,
'प्रेक्षण से रासायनिक परिवर्तन पहचानना; परमाणु गिनकर समीकरण संतुलित करना; अभिक्रियाओं का वर्गीकरण तथा दैनिक जीवन में ऑक्सीकरण समझना।',
'''अभिकारक (Reactant)|अभिक्रिया में प्रारंभ में भाग लेने वाला पदार्थ।
उत्पाद (Product)|अभिक्रिया के बाद बनने वाला पदार्थ।
संतुलित समीकरण|दोनों पक्षों में प्रत्येक तत्व के परमाणुओं की संख्या समान।
संयोजन (Combination)|दो या अधिक पदार्थों से एक मुख्य उत्पाद बनना।
वियोजन (Decomposition)|एक यौगिक से दो या अधिक पदार्थ बनना।
विस्थापन (Displacement)|अधिक सक्रिय तत्व द्वारा कम सक्रिय तत्व को हटाना।
द्विविस्थापन|दो यौगिकों के आयनों का आदान-प्रदान।
उपचयन (Oxidation)|इस स्तर पर ऑक्सीजन जुड़ना या हाइड्रोजन हटना।
अपचयन (Reduction)|इस स्तर पर ऑक्सीजन हटना या हाइड्रोजन जुड़ना।
विकृतगंधिता (Rancidity)|वसा/तेल के ऑक्सीकरण से स्वाद और गंध बिगड़ना।''',
'''### परिवर्तन से समीकरण तक
कागज काटने पर पदार्थ की पहचान कागज ही रहती है; जलाने पर नए पदार्थ बनते हैं। गैस निकलना, अवक्षेप, ताप या रंग में परिवर्तन अभिक्रिया का संकेत हो सकता है। अकेला संकेत निर्णायक नहीं: उबलते पानी में बुलबुले भौतिक परिवर्तन हैं। पदार्थ की पहचान बदलना मुख्य कसौटी है। मैग्नीशियम जलने पर सफेद मैग्नीशियम ऑक्साइड बनाता है: $2Mg + O_2 \\rightarrow 2MgO$। प्रयोग शिक्षक की देखरेख में हो; जलती पट्टी को सीधे न देखें।

### संतुलन की विधि
पहले सही रासायनिक सूत्र लिखें। $Fe + H_2O \\rightarrow Fe_3O_4 + H_2$ में Fe को 3, पानी को 4 और हाइड्रोजन को 4 का गुणांक दें। परिणाम $3Fe + 4H_2O \\rightarrow Fe_3O_4 + 4H_2$ है; यहाँ जल भाप है। सूत्र का subscript बदलना पदार्थ बदल देता है। समीकरण में (s), (l), (g), (aq) अवस्था दिखाते हैं; तीर के ऊपर ताप, प्रकाश या उत्प्रेरक लिख सकते हैं। बंद व्यवस्था में द्रव्यमान संरक्षण संतुलन का आधार है।

### अभिक्रिया के प्रकार
बिना बुझा चूना पानी से बुझा चूना बनाता है: $CaO + H_2O \\rightarrow Ca(OH)_2$; संयोजन और ऊष्माक्षेपी दोनों। $CaCO_3 \\xrightarrow{heat} CaO + CO_2$ तापीय वियोजन है। जल के विद्युत अपघटन में हाइड्रोजन और ऑक्सीजन आयतन 2:1 होता है। $2AgCl \\xrightarrow{sunlight} 2Ag + Cl_2$ प्रकाशीय वियोजन है। $Zn + CuSO_4 \\rightarrow ZnSO_4 + Cu$ विस्थापन, जबकि $Na_2SO_4 + BaCl_2 \\rightarrow BaSO_4\\downarrow + 2NaCl$ द्विविस्थापन और अवक्षेपण है। वर्गीकरण परस्पर अनन्य नहीं है।

### Redox और जीवन
$CuO + H_2 \\rightarrow Cu + H_2O$ में CuO ऑक्सीजन खोकर अपचयित, H₂ ऑक्सीजन पाकर उपचयित होता है। उपचायक दूसरे पदार्थ का उपचयन करता है और स्वयं अपचयित होता है। लोहे की जंग के लिए ऑक्सीजन तथा नमी दोनों महत्त्वपूर्ण हैं; जंग hydrated iron(III) oxide है, शुद्ध Fe₂O₃ मात्र नहीं। पेंट और जस्तीकरण संपर्क रोकते हैं। तेलयुक्त भोजन ठंडा रखना, वायुरुद्ध पैकिंग और nitrogen flushing विकृतगंधिता धीमी करते हैं; वे सभी सूक्ष्मजीवों को अनिवार्यतः समाप्त नहीं करते।''',
'''Al + O₂ → Al₂O₃ संतुलित करें।|O का LCM 6 लें: 3O₂ और 2Al₂O₃। अब Al दाईं ओर 4 हैं, अतः 4Al + 3O₂ → 2Al₂O₃। जाँच: Al 4–4, O 6–6।
CuO + H₂ में oxidising agent कौन है?|CuO, क्योंकि वह H₂ को ऑक्सीजन देकर उसका उपचयन करता है। स्वयं CuO से ऑक्सीजन निकलकर Cu बनता है; इसलिए oxidising agent का स्वयं reduction होता है।
FeSO₄ गरम करने का समीकरण और प्रेक्षण दें।|2FeSO₄ → Fe₂O₃ + SO₂ + SO₃। पहले hydrated salt का पानी निकलता है; आगे ताप पर भूरा oxide बनता है। Fe 2, S 2 और O 8 दोनों ओर हैं। यह तापीय वियोजन है।''',
'''समीकरण संतुलित करना क्यों आवश्यक है?|अभिक्रिया में परमाणु नए नहीं बनते और नष्ट नहीं होते; केवल उनका पुनर्विन्यास होता है। दोनों पक्षों में हर तत्व की संख्या बराबर करना द्रव्यमान संरक्षण दर्शाता है। गुणांक बदलें, पदार्थ के सूत्र के subscript नहीं।
संयोजन और वियोजन में अंतर उदाहरण सहित दें।|संयोजन में अनेक अभिकारक से एक मुख्य उत्पाद बनता है: CaO + H₂O → Ca(OH)₂। वियोजन में एक यौगिक कई पदार्थ देता है: CaCO₃ → CaO + CO₂। दूसरे उदाहरण के लिए ताप आवश्यक है।
ऊष्माक्षेपी और ऊष्माशोषी में अंतर करें।|ऊष्माक्षेपी अभिक्रिया आसपास को ऊष्मा देती है, जैसे ईंधन का दहन। ऊष्माशोषी अभिक्रिया ऊर्जा ग्रहण करती है, जैसे CaCO₃ का तापीय वियोजन। ऊर्जा परिवर्तन और अभिकारक/उत्पाद की संख्या अलग वर्गीकरण हैं।
लोहे को जंग से बचाने के दो उपाय समझाएँ।|पेंट की परत जल और ऑक्सीजन का संपर्क घटाती है। जस्तीकरण में zinc की परत लगती है; zinc लोहे से अधिक सक्रिय होने के कारण बलिदानी सुरक्षा भी देता है। सतह को सूखा रखने से भी जंग की गति घटती है।
अवक्षेपण अभिक्रिया क्या है?|दो जलीय विलयनों से अघुलनशील ठोस बनना अवक्षेपण है। Na₂SO₄(aq) + BaCl₂(aq) → BaSO₄(s) + 2NaCl(aq)। सफेद BaSO₄ अवक्षेप है; पदार्थ की अवस्थाएँ पहचान के लिए लिखनी चाहिए।
विकृतगंधिता के दो निवारण क्यों प्रभावी हैं?|वायुरुद्ध पैकिंग ऑक्सीजन का संपर्क घटाती है और refrigeration अभिक्रिया की गति कम करता है। दोनों उपाय वसा के ऑक्सीकरण को धीमा करते हैं। खराब भोजन को केवल गरम करके सुरक्षित मानना उचित निष्कर्ष नहीं।''',
'''Zn + CuSO₄ के प्रयोग को तीन बिंदुओं में समझाएँ।|1. साफ zinc डालने पर copper का लाल-भूरा निक्षेप होता है। 2. Cu²⁺ कम होने से नीला रंग हल्का होता है। 3. Zn + CuSO₄ → ZnSO₄ + Cu; Zn अधिक सक्रिय है। Zinc का उपचयन और copper ion का अपचयन भी होता है।
जल के विद्युत अपघटन का वर्णन करें।|1. उपयुक्त electrolyte युक्त जल में विद्युत प्रवाहित की जाती है। 2. Cathode पर H₂, anode पर O₂ मिलती है। 3. 2H₂O → 2H₂ + O₂; समान परिस्थितियों में गैस आयतन 2:1 है। अम्लीय electrolyte वाले प्रयोग में शिक्षक की देखरेख आवश्यक है।
AgCl की प्रकाशीय अभिक्रिया समझाएँ।|1. सफेद silver chloride को प्रकाश मिलने पर वह धूसर पड़ता है। 2. धूसर रंग silver बनने से है। 3. 2AgCl → 2Ag + Cl₂; तीर पर sunlight लिखें। इसलिए प्रकाश-संवेदी silver salts का पुराने photographic उपयोगों से संबंध है।
CuO + H₂ में oxidation, reduction और agents बताएँ।|1. CuO से Cu बनने पर oxygen हटती है: reduction। 2. H₂ से H₂O बनने पर oxygen जुड़ती है: oxidation। 3. CuO oxidising agent तथा H₂ reducing agent है। Agent का नाम उसके दूसरे पदार्थ पर प्रभाव से दिया जाता है।''',
'''एक छात्र H₂ + O₂ → H₂O₂ लिखकर पानी बनने का समीकरण संतुलित बताता है। त्रुटि, सही समीकरण और परमाणु-जाँच दें।|1. H₂O₂ hydrogen peroxide है; पानी का सूत्र H₂O है। 2. सही समीकरण 2H₂ + O₂ → 2H₂O। 3. बाईं और दाईं ओर H 4 तथा O 2 हैं। 4. संतुलन में गुणांक बदलते हैं, subscript नहीं; यह द्रव्यमान संरक्षण का उपयोग है।
भीगी लोहे की कील और खुले तेल के डिब्बे में परिवर्तन की तुलना तथा दो-दो बचाव बताएँ।|1. कील का संक्षारण धातु की पर्यावरण से अभिक्रिया है, जिसमें नमी और ऑक्सीजन मदद करते हैं। 2. तेल में वसा का ऑक्सीकरण विकृतगंधिता पैदा करता है। 3. लोहे को पेंट/जस्तीकरण दें। 4. तेल को वायुरुद्ध और ठंडे स्थान में रखें। दोनों oxidation से संबंधित हैं, पर corrosion और rancidity समान घटना नहीं।''',
'''2Mg + O₂ → 2MgO का मुख्य वर्ग कौन-सा है?|संयोजन|वियोजन|द्विविस्थापन|केवल भौतिक परिवर्तन|दो अभिकारक मिलकर एक प्रकार का मुख्य उत्पाद MgO बनाते हैं।
संतुलन करते समय क्या बदलना चाहिए?|गुणांक|परमाणु का प्रतीक|सूत्र के subscript|तत्व का नाम|गुणांक पूरे अणु/सूत्र इकाई की संख्या बदलता है; subscript बदलने से पदार्थ बदल जाता है।
Zn + CuSO₄ में निकलने वाली धातु कौन-सी है?|Cu|Zn|Fe|Na|Zinc copper से अधिक सक्रिय है और उसके लवण से copper विस्थापित करता है।
ताप से CaCO₃ टूटना कौन-सी अभिक्रिया है?|तापीय वियोजन|संयोजन|उदासीनीकरण|केवल विस्थापन|एक यौगिक ताप के प्रभाव में CaO और CO₂ देता है।
BaSO₄ अवक्षेप का रंग क्या है?|सफेद|नीला|काला|हरा|Barium sulfate जल में अत्यल्प विलेय सफेद ठोस है।
CuO + H₂ में अपचयित पदार्थ कौन है?|CuO|H₂|H₂O|दोनों अभिकारक|CuO ऑक्सीजन खोकर Cu बनाता है; oxygen का हटना reduction है।
तेल की विकृतगंधिता मुख्यतः किससे जुड़ी है?|ऑक्सीकरण|संघनन|जमना|उर्ध्वपातन|तेल/वसा का oxidation गंध और स्वाद बदलने वाले उत्पाद बनाता है।
जंग के लिए सामान्यतः क्या चाहिए?|ऑक्सीजन और नमी|केवल nitrogen|केवल शुष्क CO₂|केवल धूप|नमी तथा oxygen की उपलब्धता लोहे के corrosion को बढ़ाती है।
जल के विद्युत अपघटन में H₂:O₂ आयतन अनुपात क्या है?|2:1|1:2|1:1|3:1|2H₂O से 2H₂ और O₂ बनते हैं; समान दशाओं में आयतन अनुपात 2:1 है।
CaO में पानी डालने पर ऊष्मा निकलना क्या दर्शाता है?|ऊष्माक्षेपी अभिक्रिया|ऊष्माशोषी अभिक्रिया|कोई अभिक्रिया नहीं|केवल वाष्पीकरण|CaO का hydration आसपास को ऊर्जा देता है और Ca(OH)₂ बनाता है।
AgCl प्रकाश में किस धातु को देता है?|Ag|Al|Mg|Cu|Silver chloride के photodecomposition में silver और chlorine बनते हैं।
Fe + H₂O → Fe₃O₄ + H₂ में Fe का संतुलित गुणांक क्या है?|3|1|2|4|Fe₃O₄ में तीन iron atoms हैं; इसलिए बाईं ओर 3Fe चाहिए।
भोजन पैक में nitrogen क्यों भरी जाती है?|ऑक्सीजन का संपर्क घटाने के लिए|वसा को जलाने के लिए|नमी बढ़ाने के लिए|भोजन को अम्ल बनाने के लिए|Nitrogen flushing oxygen घटाकर वसा का oxidation धीमा करती है।
द्विविस्थापन में मुख्यतः क्या बदलता है?|आयनों के साथी|परमाणुओं के नाभिक|तत्व की पहचान|केवल ताप का संकेत|दो ionic compounds आयनों का आदान-प्रदान करते हैं; नए उत्पाद बनते हैं।
गैस बुलबुले दिखना अकेले chemical change का प्रमाण क्यों नहीं?|उबलते पानी में भी बुलबुले बनते हैं|हर गैस hydrogen है|हर बुलबुला ठोस है|गैसें प्रतिक्रिया नहीं करतीं|उबलना physical phase change है; नए पदार्थ बनने की जाँच भी चाहिए।''',
'- H₂O और H₂O₂ को एक पदार्थ न मानें।\n- Oxidising agent स्वयं reduced होता है।\n- अवक्षेप की अवस्था और तीर की शर्त लिखें।\n- हर वियोजन को बिना शर्त ऊष्माशोषी न घोषित करें; उदाहरण के लिए 2H₂O₂ → 2H₂O + O₂ ऊष्माक्षेपी वियोजन है।\n- तेल की विकृतगंधिता और धातु का संक्षारण अलग रखें।',
'परमाणु-संरक्षण का सांकेतिक प्रवाह: संतुलित hydrogen–oxygen reaction; चित्र मात्रा-अनुपात दिखाता है, molecular geometry नहीं।',
['2 H₂ + O₂', 'Atoms: H = 4, O = 2', '2 H₂O', 'Atoms conserved'],
'अम्ल-क्षारक अध्याय में इन्हीं समीकरणों से गैस और लवण बनना समझेंगे।',
'2025, प्रश्न 1(xv), PDF पृष्ठ 6: PbO–carbon reaction में oxidation/reduction पहचान। उत्तर-संकेत: carbon का oxidation, PbO का reduction।')

chapter(2, 'अम्ल, क्षारक एवं लवण', 'Acids, Bases and Salts', 7,
'सूचक और pH से विलयन पहचानना; अम्ल-क्षारक समीकरण लिखना; सामान्य लवणों के सूत्र, निर्माण और उपयोग समझना।',
'''अम्ल (Acid)|जलीय विलयन में H₃O⁺ की मात्रा बढ़ाने वाला पदार्थ।
क्षारक (Base)|अम्ल को उदासीन करने वाला पदार्थ; कई जलीय क्षारक OH⁻ देते हैं।
क्षार (Alkali)|जल में घुलने वाला क्षारक।
सूचक (Indicator)|अम्लीय और क्षारकीय माध्यम में अलग रंग देने वाला पदार्थ।
उदासीनीकरण|अम्ल और क्षारक से लवण तथा सामान्यतः जल बनने की अभिक्रिया।
pH|जलीय विलयन की अम्लीयता/क्षारकीयता का माप।
बेकिंग सोडा|NaHCO₃; sodium hydrogencarbonate।
धावन सोडा|Na₂CO₃·10H₂O; sodium carbonate decahydrate।
विरंजक चूर्ण|विद्यालयी निरूपण CaOCl₂; disinfecting/bleaching उपयोग।
प्लास्टर ऑफ पेरिस|CaSO₄·½H₂O; calcium sulfate hemihydrate।''',
'''### सूचक और आयन
अम्ल नीले लिटमस को लाल और क्षारक लाल लिटमस को नीला करते हैं। Phenolphthalein अम्ल में रंगहीन, क्षार में गुलाबी होता है। हल्दी क्षार में लाल-भूरी होती है। स्वाद चखना पहचान की विधि नहीं। HCl जल में H₃O⁺ देता है: $HCl + H_2O \\rightarrow H_3O^+ + Cl^-$। सूखी HCl गैस सूखे लिटमस का रंग नहीं बदलती; आयन बनने के लिए जल आवश्यक है। सभी hydrogen वाले यौगिक अम्ल नहीं; glucose इसका उदाहरण है।

### अभिक्रियाओं की भाषा
$Zn + 2HCl \\rightarrow ZnCl_2 + H_2$; सक्रिय धातु से hydrogen मिलता है। $Na_2CO_3 + 2HCl \\rightarrow 2NaCl + H_2O + CO_2$; carbonate और hydrogencarbonate से CO₂ निकलती है। CO₂ चूने के पानी को दूधिया बनाती है: $Ca(OH)_2 + CO_2 \\rightarrow CaCO_3 + H_2O$। $NaOH + HCl \\rightarrow NaCl + H_2O$ उदासीनीकरण है। Metal oxides सामान्यतः basic, non-metal oxides सामान्यतः acidic होते हैं; exceptions आगे पढ़ेंगे।

### pH और dilution
25°C पर neutral aqueous solution का pH लगभग 7 है; 7 से कम acidic, अधिक basic। एक pH unit लगभग दस गुना H⁺ concentration का अंतर है। अम्ल dilute करने पर H⁺ concentration घटती है, pH बढ़ती है। अम्ल को धीरे-धीरे पानी में मिलाएँ; उल्टा करने से तीव्र ऊष्मा और छींटे पड़ सकते हैं। Strong acid और concentrated acid अलग धारणाएँ हैं: पहला ionisation, दूसरा प्रति आयतन मात्रा बताता है। दाँतों के enamel को अम्लीय वातावरण नुकसान पहुँचा सकता है; toothpaste में हल्के basic घटक अम्ल घटाते हैं।

### सामान्य नमक से उपयोगी रसायन
Brine के electrolysis में $2NaCl + 2H_2O \\rightarrow 2NaOH + Cl_2 + H_2$। Chlorine anode, hydrogen cathode पर बनते हैं। Chlorine को dry slaked lime से अभिक्रिया कराकर bleaching powder मिलता है। Baking soda गरम करने पर $2NaHCO_3 \\rightarrow Na_2CO_3 + H_2O + CO_2$; baking powder में इसके साथ edible acid होता है। Gypsum CaSO₄·2H₂O को लगभग 373 K पर आंशिक dehydration से POP मिलता है। POP पानी जोड़ने पर gypsum बनकर जमता है। Crystal water निश्चित अनुपात में संरचना का भाग है, केवल सतह का गीलापन नहीं।''',
'''pH 3 और pH 5 में किसकी H⁺ concentration अधिक है?|pH 3 की; दो units अंतर से H⁺ concentration 10² = 100 गुना है। यह concentration की तुलना है; pH मात्र से कुल acid मात्रा नहीं मिलती।
NaHCO₃ और HCl का समीकरण लिखें।|NaHCO₃ + HCl → NaCl + H₂O + CO₂। हर तत्व की गिनती दोनों ओर समान है। निकलती CO₂ की जाँच lime water से की जा सकती है।
Gypsum से POP का निर्माण लिखें।|CaSO₄·2H₂O → CaSO₄·½H₂O + 1½H₂O; लगभग 373 K पर ताप। बिना fractions के: 2CaSO₄·2H₂O → 2CaSO₄·½H₂O + 3H₂O।''',
'''सूखी HCl सूखे लिटमस को लाल क्यों नहीं करती?|जल की अनुपस्थिति में पर्याप्त hydronium ions नहीं बनते। नम लिटमस की नमी में HCl आयनित होकर अम्लीयता दिखाती है। इसलिए अम्ल के विद्यालयी गुण मुख्यतः aqueous solution में समझे जाते हैं।
Strong और concentrated acid का अंतर क्या है?|Strong acid जल में बड़ी सीमा तक ionise करता है। Concentrated acid में प्रति आयतन acid की मात्रा अधिक है। एक strong acid dilute भी हो सकता है और weak acid concentrated भी। दोनों शब्द एक-दूसरे के पर्याय नहीं।
Carbonate को अम्ल से कैसे पहचानेंगे?|नमूने में dilute acid मिलाने पर CO₂ की effervescence होती है। गैस lime water में भेजने पर CaCO₃ के कारण दूधियापन आता है। यह प्रयोग शिक्षक की देखरेख में करें और गैस सीधे न सूँघें।
पेट के antacid का सिद्धांत बताएँ।|Antacid के हल्के basic घटक अतिरिक्त gastric acid को neutralise करते हैं। यह उदासीनीकरण का उपयोग है। इससे हर पेट-दर्द का कारण acidity सिद्ध नहीं होता; यह अध्याय दवा की मात्रा या स्वयं उपचार का निर्देश नहीं देता।
Crystallisation water क्या है?|Crystal structure में प्रति formula unit निश्चित संख्या के water molecules शामिल होना crystallisation water है। CuSO₄·5H₂O इसका उदाहरण है। गर्म करने पर hydrated और anhydrous salt के गुण तथा रंग बदल सकते हैं।
Baking soda और washing soda अलग कैसे हैं?|Baking soda NaHCO₃ है; washing soda Na₂CO₃·10H₂O। पहला baking powder आदि में, दूसरा cleaning और स्थायी कठोरता घटाने में उपयोगी है। नाम की समानता से सूत्र या उपयोग परस्पर न बदलें।''',
'''Chlor-alkali प्रक्रिया के उत्पाद और स्थान बताएँ।|1. Brine aqueous NaCl है। 2. Electrolysis से Cl₂ anode तथा H₂ cathode पर बनते हैं। 3. विलयन में NaOH रहता है: 2NaCl + 2H₂O → 2NaOH + Cl₂ + H₂। उत्पाद अलग रखना आवश्यक है।
Dilution में pH परिवर्तन और सुरक्षा समझाएँ।|1. अम्ल में पानी मिलाने से प्रति आयतन H₃O⁺ घटता है, pH बढ़ता है। 2. क्षार dilute होने पर OH⁻ घटता है, pH neutral की ओर घटता है। 3. सांद्र अम्ल धीरे पानी में मिलाएँ; dilution ऊष्माक्षेपी हो सकता है।
POP के बनने और जमने की प्रक्रिया दें।|1. Gypsum को नियंत्रित ताप पर आंशिक निर्जलीकरण करें। 2. CaSO₄·½H₂O मिलता है। 3. जल मिलाने पर CaSO₄·2H₂O दोबारा बनता है और कठोर हो जाता है। नमी से बचाकर भंडारण इसलिए जरूरी है।
लवण का pH हमेशा 7 क्यों नहीं होता?|1. Strong acid–strong base salt सामान्यतः neutral होता है। 2. Strong acid–weak base salt का solution acidic हो सकता है, जैसे NH₄Cl। 3. Weak acid–strong base salt basic हो सकता है, जैसे Na₂CO₃। नमक शब्द का अर्थ neutral नहीं।''',
'''चार बोतलों में dilute HCl, NaOH, NaCl solution और distilled water हैं। Litmus से कौन-सी पहचान संभव है और कौन-सी नहीं?|1. नीला litmus लाल करने वाली HCl है। 2. लाल litmus नीला करने वाली NaOH है। 3. NaCl और distilled water दोनों litmus अपरिवर्तित छोड़ सकते हैं। 4. इन दो neutral नमूनों को केवल litmus से अलग नहीं किया जा सकता; अतिरिक्त परीक्षण चाहिए। इसलिए सूचक की सीमा भी उत्तर में दें।
सामान्य नमक से NaOH, bleaching powder और soda compounds की उपयोग-श्रृंखला समझाएँ।|1. Brine electrolysis से NaOH, Cl₂ और H₂ मिलते हैं। 2. Cl₂ तथा slaked lime से bleaching powder मिलता है। 3. NaHCO₃ ताप पर Na₂CO₃ देता है, जिसके crystallisation से washing soda बनता है। 4. इनके उपयोग क्रमशः chemical manufacture, disinfection और cleaning से जुड़े हैं; NaCl को अकेले गरम करने से ये सभी नहीं बनते।''',
'''नीला litmus अम्ल में कैसा होता है?|लाल|नीला|हरा|बैंगनी|अम्लीय माध्यम blue litmus को red करता है।
Phenolphthalein क्षारीय विलयन में कैसा होता है?|गुलाबी|रंगहीन|नीला|पीला|Phenolphthalein alkaline medium में pink रंग देता है।
25°C पर neutral solution का pH क्या है?|7|1|14|0|Neutral water में H₃O⁺ और OH⁻ concentrations बराबर होने पर pH लगभग 7 है।
Carbonate और acid से कौन-सी गैस बनती है?|CO₂|H₂|N₂|Cl₂|Carbonate में acid डालने से salt, water और carbon dioxide बनते हैं।
Baking soda का सूत्र क्या है?|NaHCO₃|Na₂CO₃·10H₂O|CaSO₄·½H₂O|NaOH|Baking soda sodium hydrogencarbonate है, washing soda नहीं।
Washing soda में crystal water कितने molecules हैं?|10|5|2|½|Na₂CO₃·10H₂O decahydrate है; दस water molecules सूत्र में शामिल हैं।
POP का सूत्र क्या है?|CaSO₄·½H₂O|CaSO₄·2H₂O|CaCO₃|Ca(OH)₂|POP hemihydrate है; gypsum dihydrate होता है।
Brine electrolysis के anode पर कौन-सी गैस मिलती है?|Cl₂|H₂|CO₂|SO₂|Chloride ions oxidation से anode पर chlorine बनाते हैं।
अम्ल को dilute करने पर pH सामान्यतः क्या करता है?|बढ़ता है|घटता है|हमेशा शून्य होता है|हमेशा 14 होता है|H₃O⁺ concentration घटती है, इसलिए pH neutral की ओर बढ़ता है।
हर hydrogen युक्त compound acid है, इस दावे का counterexample कौन है?|Glucose|HCl|HNO₃|H₂SO₄|Glucose में H होने पर भी जल में acid जैसा H₃O⁺ नहीं बनता।
जल में घुलने वाले base को क्या कहते हैं?|Alkali|Ore|Alloy|Ester|Alkali soluble base है; सभी bases soluble नहीं।
अम्ल dilution का सुरक्षित क्रम क्या है?|अम्ल धीरे पानी में|पानी तेजी से अम्ल में|दोनों उबालकर|बिना आँख सुरक्षा के|Water का बड़ा आयतन ऊष्मा संभालता है; acid धीरे मिलाने से छींटे कम होते हैं।
CuSO₄·5H₂O का सामान्य रंग क्या है?|नीला|सफेद|काला|पीला|Hydrated copper sulfate blue होता है; anhydrous salt सामान्यतः white है।
NaOH + HCl में कौन-सा salt बनता है?|NaCl|Na₂SO₄|CaCl₂|NaHCO₃|Sodium ion और chloride ion से sodium chloride बनता है।
नमक का solution हमेशा neutral होता है क्या?|नहीं, acid/base पर निर्भर है|हाँ, सभी salts के लिए|हाँ, केवल रंगीन salts के लिए|नहीं, सभी acidic हैं|Salt solution का pH उसके ions की जल से प्रतिक्रिया पर निर्भर करता है।''',
'- pH और acid concentration को strength से न मिलाएँ।\n- NaHCO₃ तथा Na₂CO₃·10H₂O के सूत्र अलग हैं।\n- हर salt neutral नहीं।\n- POP में ½ water है, gypsum में 2।\n- अम्ल/क्षार को चखकर या हाथ लगाकर पहचानना प्रयोग नहीं।',
'सामान्य नमक से chlor-alkali उत्पादों का process schematic; गैसें अलग electrodes पर बनती हैं।',
['Brine: NaCl(aq)', 'Electrolysis', 'Anode: Cl₂', 'Cathode: H₂', 'Solution: NaOH'],
'अगले अध्याय में धातुओं की acid, water और salt solutions से प्रतिक्रियाएँ आएँगी।')

chapter(3, 'धातु एवं अधातु', 'Metals and Non-metals', 5,
'गुणों और exceptions की तुलना; activity series से प्रतिक्रिया का अनुमान; ionic compounds, extraction और corrosion protection समझना।',
'''आघातवर्धनीयता (Malleability)|पीटकर चादर बनने का गुण।
तन्यता (Ductility)|खींचकर तार बनने का गुण।
ध्वानिकता (Sonority)|प्रहार पर ringing sound देने का गुण।
सक्रियता श्रेणी|धातुओं का घटती रासायनिक सक्रियता में क्रम।
आयनिक आबंध|इलेक्ट्रॉन transfer के बाद विपरीत ions का आकर्षण।
खनिज (Mineral)|प्राकृतिक रूप में मिलने वाला तत्व/यौगिकयुक्त पदार्थ।
अयस्क (Ore)|जिससे धातु का निष्कर्षण आर्थिक रूप से उपयुक्त हो।
निस्तापन (Calcination)|सीमित/अनुपस्थित वायु में carbonate ore का ताप।
भर्जन (Roasting)|अधिक वायु में sulfide ore का ताप।
मिश्रधातु (Alloy)|धातु का दूसरी धातु/अधातु के साथ मिश्रण।''',
'''### गुण और अपवाद
धातुएँ सामान्यतः चमकीली, चालक, तन्य और आघातवर्धनीय होती हैं। Mercury room temperature पर liquid metal है। Sodium/potassium नरम होते हैं। अधातुएँ सामान्यतः कुचालक और भंगुर हैं; graphite विद्युत का चालक और iodine चमकीला है। इसलिए किसी एक गुण से अंतिम पहचान न करें। Oxides में Al₂O₃ और ZnO amphoteric हैं: acid और base दोनों से प्रतिक्रिया कर सकते हैं।

### प्रतिक्रियाओं का अनुमान
एक उपयोगी क्रम है K > Na > Ca > Mg > Al > Zn > Fe > Pb > H > Cu > Hg > Ag > Au। H धातु नहीं, acid से hydrogen विस्थापन का comparison reference है। Sodium ठंडे पानी से तीव्रता से, magnesium गर्म पानी/भाप से, iron भाप से प्रतिक्रिया करता है। Copper साधारण पानी से नहीं। Hydrogen से ऊपर की कई metals dilute non-oxidising acids से H₂ देती हैं। HNO₃ oxidising acid है; साधारण ‘metal + acid = H₂’ नियम उस पर बिना शर्त लागू न करें।

### Ionic compound की रचना
Na एक electron खोकर Na⁺, Cl एक electron लेकर Cl⁻ बनाता है। विपरीत charges के आकर्षण से NaCl ionic lattice बनता है। Solid में ions fixed हैं, इसलिए electrical conduction नहीं; molten या aqueous state में mobile ions current ले जाते हैं। Strong electrostatic attractions उच्च melting point का कारण हैं। MgCl₂ में Mg²⁺ को balance करने के लिए दो Cl⁻ चाहिए।

### अयस्क से धातु
Gangue हटाकर enrichment होता है। Medium-reactivity metals के sulfides roasting और carbonates calcination से oxides बनते हैं: $2ZnS + 3O_2 \\rightarrow 2ZnO + 2SO_2$; $ZnCO_3 \\rightarrow ZnO + CO_2$। फिर oxide reduction: $ZnO + C \\rightarrow Zn + CO$। Highly reactive Na/Mg/Al के लिए molten salts/appropriate electrolytes का electrolysis उपयोगी है; carbon reduction सामान्यतः पर्याप्त नहीं। Copper electrolytic refining में impure Cu anode, pure Cu cathode और CuSO₄ electrolyte है। Alloying, galvanising और painting corrosion घटाते हैं।''',
'''Fe की कील CuSO₄ में डालने पर क्या होगा?|Fe + CuSO₄ → FeSO₄ + Cu। Iron अधिक active है; copper की coating और solution में Fe²⁺ बनते हैं। Zinc sulfate में iron डालकर यही displacement अपेक्षित नहीं।
Mg और Cl से बनने वाले ionic compound का सूत्र दें।|Mg → Mg²⁺ + 2e⁻; दो Cl atoms दो electrons लेते हैं। Charges +2 तथा 2×−1 balance होते हैं; सूत्र MgCl₂ है, MgCl नहीं।
Thermite reaction संतुलित करें और उपयोग दें।|Fe₂O₃ + 2Al → Al₂O₃ + 2Fe। Al iron oxide reduce करता है; बहुत ऊष्मा निकलती है। इसे rail joints welding जैसे उपयोगों से समझा जाता है; classroom में स्वयं न करें।''',
'''धातुओं के गुण लिखते समय exceptions क्यों देने चाहिए?|‘सभी’ धातु कठोर और ठोस कहना गलत है। Sodium नरम और mercury liquid है। इसी तरह graphite अधातु होकर conductor है। सामान्य गुण उपयोगी हैं, पर classification को exceptions सहित लिखने से उत्तर वैज्ञानिक बनता है।
Solid NaCl बिजली क्यों नहीं चलाता?|Solid ionic lattice में ions स्थान बदलकर charge carry नहीं कर सकते। पिघले या जलीय NaCl में ions mobile होते हैं, इसलिए conduction होती है। इसका कारण free electrons नहीं, mobile ions हैं।
Ore और mineral में अंतर दें।|खनिज प्राकृतिक metal-bearing पदार्थ है। जिस mineral से extraction आर्थिक रूप से उपयुक्त हो, वह ore कहलाता है। इसलिए हर ore mineral है, लेकिन हर mineral ore नहीं; metal प्रतिशत के साथ लागत भी महत्त्वपूर्ण है।
भर्जन और निस्तापन की तुलना करें।|Roasting में sulfide ore को पर्याप्त oxygen के साथ गरम कर oxide बनाते हैं। Calcination में carbonate ore को सीमित/बिना वायु गरम कर oxide और CO₂ बनाते हैं। Ore प्रकार और oxygen availability दो स्पष्ट अंतर हैं।
Aluminium को जंग से कुछ सुरक्षा कैसे मिलती है?|Al की सतह पर पतली adherent Al₂O₃ layer बनती है, जो अंदर की metal का संपर्क घटाती है। Anodising इस oxide layer को मजबूत करता है। इसका अर्थ aluminium बिल्कुल प्रतिक्रिया नहीं करता, ऐसा नहीं।
मिश्रधातु बनाने का लाभ बताएँ।|Alloying से hardness, corrosion resistance और उपयोगी गुण बदल सकते हैं। Brass Cu–Zn और bronze Cu–Sn हैं। Stainless steel में Fe के साथ chromium और अन्य घटक होते हैं; composition के अनुसार गुण बदलते हैं।''',
'''Activity series से तीन salt-solution predictions दें।|1. Zn, CuSO₄ से Cu हटाता है। 2. Fe, ZnSO₄ से Zn नहीं हटाता क्योंकि Zn अधिक active है। 3. Cu, AgNO₃ से Ag हटाता है: Cu + 2AgNO₃ → Cu(NO₃)₂ + 2Ag। तुलना आवश्यक है, केवल metal होने से displacement नहीं।
NaCl का electron transfer और conduction समझाएँ।|1. Na एक electron छोड़कर Na⁺ बनाता है। 2. Cl उसे लेकर Cl⁻ बनाता है; attraction ionic bond है। 3. Solid में fixed ions, molten/aqueous में mobile ions होते हैं। Neutral atoms का बनना conduction का कारण नहीं।
Copper refining के electrodes और परिवर्तन दें।|1. Impure copper anode तथा pure copper sheet cathode है। 2. Anode का Cu, Cu²⁺ होकर solution में आता है। 3. Cathode पर Cu²⁺ electrons लेकर Cu जमता है; कुछ insoluble impurities anode mud बनती हैं।
Reactive metals के extraction के तीन स्तर दें।|1. Low-reactivity metals के कुछ ores heating से metal दे सकते हैं। 2. Medium-reactivity metal oxides को carbon/appropriate reducing agents से reduce करते हैं। 3. High-reactivity metals को electrolysis चाहिए। प्रक्रिया ore और metal पर निर्भर है; एक ही विधि सब पर लागू नहीं।''',
'''ZnCO₃ से zinc पाने के चरण, समीकरण और विधि का कारण लिखें।|1. Enrichment से gangue घटाएँ। 2. Calcination: ZnCO₃ → ZnO + CO₂। 3. Reduction: ZnO + C → Zn + CO। 4. Zinc की medium reactivity इस route को उपयुक्त बनाती है; प्राप्त metal का refining किया जाता है। पहले sulfide मानकर roasting लिखना इस ore के लिए गलत होगा।
जस्तीकरण और electrolytic refining की तुलना करें।|1. Galvanising में iron पर zinc protective layer लगती है। 2. इसका उद्देश्य corrosion protection है। 3. Electrolytic refining में impure copper anode से copper pure cathode पर transfer होता है। 4. इसका उद्देश्य purity बढ़ाना है। दोनों metal treatment हैं, पर electrodes और उद्देश्यों को interchange नहीं करें।''',
'''कमरे के ताप पर liquid metal कौन है?|Mercury|Iron|Copper|Aluminium|Mercury सामान्य room temperature पर liquid है।
विद्युत-चालक अधातु का उदाहरण कौन है?|Graphite|Sulfur|Phosphorus|Bromine|Graphite में delocalised electrons conduction संभव बनाते हैं।
Metal को तार में खींचने का गुण क्या है?|Ductility|Malleability|Brittleness|Transparency|Ductility तार बनाने का गुण है; malleability चादर बनाने का।
Amphoteric oxide कौन है?|Al₂O₃|Na₂O|CO₂|SO₂|Aluminium oxide acid और base दोनों से reaction कर सकता है।
Fe किस solution से metal विस्थापित करेगा?|CuSO₄|ZnSO₄|MgSO₄|NaCl|Iron copper से ऊपर है, पर zinc, magnesium और sodium से नीचे।
MgCl₂ में Mg ion का charge क्या है?|+2|+1|−1|−2|Magnesium दो electrons खोकर Mg²⁺ बनाता है।
Molten NaCl में current कौन carry करता है?|Mobile ions|केवल neutral atoms|Fixed ions|Photons|Molten ionic salt में ions चल सकते हैं और charge ले जाते हैं।
Sulfide ore को हवा में गरम करना क्या है?|Roasting|Calcination|Galvanising|Alloying|Roasting oxygen की उपस्थिति में sulfide को oxide में बदलता है।
Carbonate ore में उपयुक्त प्रथम thermal प्रक्रिया क्या है?|Calcination|केवल electroplating|Neutralisation|Polymerisation|Calcination से carbonate टूटकर oxide और CO₂ देता है।
Copper refining का anode कौन है?|Impure copper|Pure copper sheet|Graphite ही अनिवार्य|Zinc sheet|Impure copper anode से Cu²⁺ solution में जाता है।
Galvanising में iron पर कौन-सी metal चढ़ती है?|Zinc|Gold|Mercury|Silver|Zinc layer और उसकी अधिक activity corrosion protection में मदद करती है।
Brass के मुख्य metals क्या हैं?|Cu और Zn|Cu और Sn|Fe और Hg|Al और Ag|Brass copper–zinc alloy है; bronze copper–tin है।
Na extraction में carbon reduction सामान्यतः पर्याप्त क्यों नहीं?|Na बहुत reactive है|Na एक अधातु है|Na में electrons नहीं|Na water में inert है|Highly reactive sodium के compounds से metal पाने के लिए electrolysis उपयोग होता है।
Mineral और ore का सही संबंध क्या है?|हर ore mineral है|हर mineral ore है|दोनों हमेशा समान हैं|Ore कृत्रिम ही होता है|Ore extraction के लिए economically useful mineral है।
Metal + HNO₃ से हमेशा H₂ मिलता है क्या?|नहीं, HNO₃ oxidising acid है|हाँ, सभी metals से|हाँ, केवल Cu से|हाँ, केवल Au से|Nitric acid की oxidising nature सामान्य hydrogen-evolution rule को सीमित करती है।''',
'- Graphite/mercury जैसे exceptions याद रखें।\n- H को activity series में metal न कहें।\n- Solid salt में conduction का दावा न करें।\n- Roasting और calcination को ore के अनुसार लिखें।\n- Refining, extraction और corrosion protection अलग प्रक्रियाएँ हैं।',
'Carbonate ore से metal तक process schematic; gangue removal और refining अलग चरण हैं।',
['Carbonate ore', 'Enrichment', 'Calcination: oxide', 'Reduction: metal', 'Refining'],
'अगले अध्याय में electron transfer के बजाय carbon का electron sharing आएगा।')

chapter(4, 'कार्बन एवं उसके यौगिक', 'Carbon and its Compounds', 7,
'Carbon bonding, homologous series और नामकरण समझना; ethanol/ethanoic acid reactions लिखना; soap cleaning का mechanism बताना।',
'''चतुःसंयोजकता|Carbon की चार covalent bonds बनाने की क्षमता।
शृंखलन (Catenation)|Carbon atoms का आपस में chains/branches/rings बनाना।
सहसंयोजी आबंध|Atoms के बीच electron pairs का sharing।
संतृप्त hydrocarbon|Carbon–carbon bonds केवल single; open-chain alkane सूत्र CₙH₂ₙ₊₂।
असंतृप्त hydrocarbon|कम से कम एक C=C या C≡C bond वाला hydrocarbon।
समजातीय श्रेणी|समान functional group और समान सामान्य सूत्र वाले compounds की श्रेणी।
प्रकार्यात्मक समूह|Compound के characteristic chemical properties निर्धारित करने वाला group।
Ethanol|C₂H₅OH; alcohol functional group –OH।
Ethanoic acid|CH₃COOH; carboxylic acid functional group –COOH।
Micelle|Water में soap tails अंदर और ionic heads बाहर वाली aggregate संरचना।''',
'''### Carbon इतना विविध क्यों है?
Carbon के valence shell में चार electrons हैं। चार electrons पूरी तरह खोना या पाना energetically कठिन है, इसलिए sharing से covalent bonds बनते हैं। Methane में चार C–H single bonds; ethene में C=C double bond, ethyne में C≡C triple bond है। Carbon–carbon bonds की स्थिरता catenation संभव करती है। Covalent compounds सामान्यतः low melting/boiling points और poor electrical conduction दिखाते हैं, पर सभी carbon compounds पर बिना exception यही कथन न लगाएँ।

### संरचना और नाम
Open-chain alkanes में CₙH₂ₙ₊₂, एक double bond वाले alkenes में CₙH₂ₙ, एक triple bond वाले alkynes में CₙH₂ₙ₋₂ सामान्य सूत्र है। Chain length prefixes meth-, eth-, prop-, but- हैं। Functional groups –OH alcohol, –CHO aldehyde, >C=O ketone और –COOH acid हैं। Successive homologues में –CH₂– तथा molecular mass में 14 u का अंतर होता है। Butane और isobutane same molecular formula पर different connectivity दिखाते हैं: structural isomerism।

### महत्वपूर्ण reactions
Complete combustion: $CH_4 + 2O_2 \\rightarrow CO_2 + 2H_2O$। कम oxygen में CO/soot बन सकते हैं। Hydrogen addition: $CH_2=CH_2 + H_2 \\xrightarrow{Ni} CH_3-CH_3$। Methane substitution: $CH_4 + Cl_2 \\xrightarrow{sunlight} CH_3Cl + HCl$। Ethanol oxidation suitable oxidising agent से ethanoic acid देता है। $2C_2H_5OH + 2Na \\rightarrow 2C_2H_5ONa + H_2$। Ethanoic acid और ethanol, acid catalyst की उपस्थिति में ester और water देते हैं; यह esterification है। Alkali से ester टूटना saponification कहलाता है।

### साबुन कैसे साफ करता है?
Soap long-chain fatty acid का sodium/potassium salt है। इसका hydrophobic tail grease से जुड़ता है और hydrophilic head water की ओर रहता है। Micelles dirt को water में disperse कर देते हैं, जिससे rinsing में निकलती है। Hard water के Ca²⁺/Mg²⁺ soap से insoluble scum बनाते हैं। Detergents ऐसी समस्या कम दिखाते हैं; लेकिन हर detergent biodegradable या pollution-free हो, ऐसा निष्कर्ष गलत है।''',
'''C₃H₈ का नाम और hydrogen संख्या का कारण दें।|तीन carbon वाला saturated open-chain compound propane है। Alkane formula CₙH₂ₙ₊₂ में n=3 देने पर H=8 मिलता है। सूत्र को alkene पर लागू न करें।
Ethanoic acid और carbonate का समीकरण लिखें।|2CH₃COOH + Na₂CO₃ → 2CH₃COONa + H₂O + CO₂। Sodium ethanoate salt बनता है। Carbonate के दो negative charges के कारण acid के दो molecules चाहिए।
Ethanol से ester बनाने की reaction दें।|CH₃COOH + C₂H₅OH ⇌ CH₃COOC₂H₅ + H₂O; concentrated H₂SO₄ catalyst और heat की उपस्थिति में ethyl ethanoate बनता है। यह equilibrium reaction है; ether बनने की reaction नहीं।''',
'''Carbon ionic bond की जगह sharing क्यों करता है?|चार electrons खोने में बहुत ऊर्जा और चार पाने पर nucleus के लिए अतिरिक्त electrons संभालना कठिन है। Sharing से valence shell भरता है। इसलिए carbon compounds में covalent bonding प्रमुख है; यह carbon की tetravalency से जुड़ा है।
Homologous series की दो विशेषताएँ दें।|सभी members का functional group और general formula समान होता है। पास-पास members में CH₂ और 14 u का अंतर होता है। Chemical properties समान दिशा में, physical properties क्रमिक ढंग से बदलती हैं।
Addition और substitution का अंतर दें।|Addition में unsaturated bond पर atoms जुड़ते हैं, जैसे ethene + H₂ से ethane। Substitution में atom/group के स्थान पर दूसरा आता है, जैसे sunlight में methane का H chlorine से बदलता है। दोनों में reaction conditions लिखें।
Ethanol और ethanoic acid में अंतर दें।|Ethanol में –OH और ethanoic acid में –COOH group है। Acid carbonate से CO₂ निकालता है, alcohol ऐसा सामान्यतः नहीं करता। दोनों organic compounds हैं, लेकिन उनके functional groups के कारण chemical properties अलग हैं।
Soap hard water में कम प्रभावी क्यों है?|Ca²⁺ और Mg²⁺ soap के साथ insoluble salts बनाकर scum देते हैं। इससे cleaning के लिए उपलब्ध soap कम हो जाता है। Detergent formulation ऐसी insoluble precipitation को कम कर सकती है।
Incomplete combustion क्यों खतरनाक है?|कम oxygen में carbon monoxide बन सकती है; यह रंगहीन gas रक्त की oxygen-carrying क्षमता को बाधित करती है। बंद कमरे में ईंधन जलाना खतरा बढ़ाता है। नीली/पीली flame से alone safety का पूर्ण निर्णय न लें।''',
'''Methane का electron-sharing विवरण दें।|1. Carbon के चार valence electrons हैं। 2. चार H atoms अपना एक-एक electron share करते हैं। 3. चार shared pairs से चार single covalent bonds बनते हैं; carbon octet और हर H duplet प्राप्त करता है। CH₄ में double bond नहीं।
Ethanol की तीन reactions समझाएँ।|1. Combustion: C₂H₅OH + 3O₂ → 2CO₂ + 3H₂O। 2. Sodium reaction hydrogen तथा sodium ethoxide देती है। 3. Suitable oxidant से ethanol का oxidation ethanoic acid तक होता है। Conditions और उत्पादों को अलग रखें।
Esterification और saponification का संबंध दें।|1. Alcohol और carboxylic acid से ester + water बनते हैं। 2. उपयुक्त alkali से ester hydrolysis में alcohol और carboxylate salt मिलते हैं। 3. Fat/oil के alkaline hydrolysis से soap बनाना इसी प्रकार का उपयोग है।
Micelle में orientation और cleaning समझाएँ।|1. Nonpolar tails grease/oil में भीतर की ओर। 2. Charged hydrophilic heads बाहर water में। 3. Grease droplets dispersed होकर rinsing में निकलते हैं। Soap dirt को chemical combustion से नष्ट नहीं करता।''',
'''Ethane, ethene और ethyne की bonding, formula और hydrogenation की तुलना करें।|1. Ethane C₂H₆ में C–C single bond और saturation है। 2. Ethene C₂H₄ में double, ethyne C₂H₂ में triple bond है। 3. Unsaturated compounds hydrogen addition कर सकते हैं, catalyst सहित। 4. Ethene + H₂ → ethane; ethyne की पूर्ण hydrogenation में 2H₂ चाहिए। Hydrogen संख्या और bonds दोनों तुलना में दें।
साबुन की cleaning का चित्रात्मक वर्णन तथा hard water की सीमा लिखें।|1. एक गोल grease droplet बनाएँ। 2. Tails droplet के भीतर, ionic heads बाहर water की ओर दिखाएँ। 3. Micelle oil को disperse करता है और rinsing हटाती है। 4. Hard-water ions insoluble scum बनाते हैं, इसलिए detergent विकल्प उपयोगी हो सकता है। चित्र surface aggregate का schematic है, single soap molecule का आकार नहीं।''',
'''Carbon की सामान्य valency क्या है?|4|1|2|3|Carbon चार electron pairs share करके सामान्यतः चार covalent bonds बनाता है।
Carbon atoms के chain बनाने के गुण का नाम क्या है?|Catenation|Ionisation|Neutralisation|Corrosion|Catenation same element atoms के परस्पर जुड़ने की क्षमता है।
Ethene का formula क्या है?|C₂H₄|C₂H₆|C₂H₂|CH₄|Ethene के दो carbon के बीच double bond है और चार hydrogen हैं।
Successive homologues के mass का अंतर कितना है?|14 u|2 u|12 u|16 u|CH₂ का mass 12 + 2 = 14 u है।
Alcohol का functional group कौन है?|–OH|–COOH|–CHO|–Cl|Alcohol में hydroxyl group –OH characteristic है।
Ethanoic acid का formula क्या है?|CH₃COOH|C₂H₅OH|CH₄|CH₃CHO|Ethanoic acid में carboxyl group –COOH होता है।
Methane में कितने single covalent bonds हैं?|4|2|1|8|चार C–H shared pairs चार single covalent bonds बनाते हैं।
Hydrogenation किसका उदाहरण है?|Addition|Substitution|Displacement|Precipitation|Hydrogen unsaturated carbon bond पर जुड़कर saturation बढ़ाता है।
Methane chlorination में कौन-सी condition उपयोगी है?|Sunlight|केवल ice|केवल vacuum|बिना chlorine|Sunlight substitution reaction शुरू करने में सहायता करती है।
Soap micelle में heads water की ओर क्यों होते हैं?|वे hydrophilic हैं|वे nonpolar हैं|वे metal sheets हैं|वे gas बनाते हैं|Ionic heads water से interaction करते हैं और tails grease की ओर रहते हैं।
Hard water में soap का insoluble पदार्थ क्या कहलाता है?|Scum|Ester|Ozone|Alloy|Ca/Mg के insoluble fatty-acid salts scum बनाते हैं।
Ester alkaline hydrolysis का नाम क्या है?|Saponification|Roasting|Sublimation|Galvanisation|Saponification ester का alkali से hydrolysis है।
Open-chain alkane का general formula क्या है?|CₙH₂ₙ₊₂|CₙH₂ₙ|CₙH₂ₙ₋₂|CₙHₙ|केवल acyclic saturated alkanes के लिए CₙH₂ₙ₊₂ लागू है।
Same formula और अलग connectivity को क्या कहते हैं?|Structural isomerism|Homology|Neutralisation|Dispersion|Structural isomers में molecular formula समान, atom connections अलग हैं।
कम oxygen में carbon combustion का toxic product कौन हो सकता है?|CO|O₂|NaCl|H₂O ही अनिवार्य|Incomplete combustion carbon monoxide दे सकती है, जो toxic है।''',
'- Alkane का formula ring compounds पर बिना जाँच न लगाएँ।\n- –OH और –COOH अलग हैं।\n- Esterification और ether formation न मिलाएँ।\n- Soap head water की ओर होता है, tail नहीं।\n- Detergent को हमेशा biodegradable न लिखें।',
'साबुन की cleaning का प्रक्रिया schematic; head/tail orientation का वर्णन पाठ में दिया है।',
['Soap in water', 'Tail binds oil', 'Head faces water', 'Micelle disperses oil', 'Rinse removes dirt'],
'जैव प्रक्रम में carbohydrates, fats और energy release की भूमिका पढ़ेंगे।')

chapter(5, 'जैव प्रक्रम', 'Life Processes', 8,
'Nutrition, respiration, transport और excretion को जोड़ना; human और plant pathways की तुलना; heart तथा nephron के functional stages बताना।',
'''स्वपोषण|Inorganic पदार्थों से अपना organic food बनाना।
प्रकाश संश्लेषण|Light energy से CO₂ और water से carbohydrate बनना।
रंध्र (Stomata)|पत्ती में guard cells द्वारा नियंत्रित pores।
पेरिस्टाल्सिस|Alimentary canal की wave-like contractions से food movement।
श्वसन (Respiration)|Food से usable energy प्राप्त करने की cellular प्रक्रिया।
Alveoli|Lungs में thin-walled air sacs, gas exchange का स्थल।
Double circulation|एक पूर्ण circuit में blood का heart से दो बार गुजरना।
Xylem|Water/minerals का मुख्य conducting tissue।
Phloem|Food का source से sink तक translocation tissue।
Nephron|Kidney की functional filtration/reabsorption unit।''',
'''### जीवन बनाए रखने के प्रक्रम
जीवों को molecules, energy और waste removal लगातार चाहिए। Nutrition भोजन उपलब्ध करता है; respiration उसकी ऊर्जा usable रूप में देता है; transport सामग्री पहुँचाता है; excretion metabolic waste हटाता है। किसी जीव में बाहरी movement न दिखने पर भी cell-level activity जारी रह सकती है। पौधों में simplified photosynthesis equation $6CO_2 + 6H_2O \\rightarrow C_6H_{12}O_6 + 6O_2$ है; light और chlorophyll आवश्यक conditions हैं। रंध्र CO₂ exchange और transpiration में काम करते हैं।

### भोजन से absorption तक
Mouth में chewing और salivary amylase starch breakdown शुरू करते हैं। Oesophagus में peristalsis भोजन ले जाता है। Stomach का HCl acidic medium देता है; pepsin protein पर काम करता है और mucus lining की रक्षा करता है। Small intestine में bile fat को छोटे droplets में emulsify करता है; bile enzyme नहीं है। Pancreatic enzymes और intestinal enzymes digestion आगे बढ़ाते हैं। Villi surface area बढ़ाकर nutrients absorb करते हैं। Large intestine मुख्यतः water absorption में मदद करता है।

### Respiration और gas exchange
Glucose पहले cytoplasm में 3-carbon pyruvate बनाता है। Oxygen की उपलब्धता में mitochondria में आगे breakdown से CO₂, H₂O और अधिक usable energy बनती है। Yeast में ethanol + CO₂, oxygen deficit में muscles में lactate बन सकता है। Breathing air movement है; respiration cellular chemical process। Alveolar thin walls, large area और capillaries diffusion में मदद करते हैं। Haemoglobin oxygen transport करता है; अधिकांश CO₂ अन्य रूपों सहित blood में transport होती है।

### Circulation, plants और excretion
Right heart deoxygenated blood lungs को और left heart oxygenated blood body को भेजता है। Valves backflow रोकते हैं। Pulmonary artery deoxygenated और pulmonary vein oxygenated blood लेती है; artery/vein नाम दिशा से है। Plants में root uptake और transpiration pull xylem transport में मदद करते हैं। Phloem source–sink movement ATP उपयोग कर सकता है और दिशा जरूरत के अनुसार होती है। Nephron में glomerular filtration, selective reabsorption तथा tubular secretion urine बनाते हैं। Urine kidney → ureter → bladder → urethra चलता है। Plants gases, storage, leaf shedding और resins/gums से wastes संभालते हैं।''',
'''Heart में blood का पूरा मार्ग लिखें।|Body → venae cavae → right atrium → right ventricle → pulmonary artery → lungs → pulmonary veins → left atrium → left ventricle → aorta → body। हर chamber और lung passage को क्रम में रखें।
Yeast के anaerobic breakdown का result दें।|Glucose → ethanol + CO₂ + energy। शुरू में glycolysis cytoplasm में होती है। Yeast के उत्पादों को human muscle से न मिलाएँ; muscle oxygen deficit में lactate बन सकता है।
Absorption के लिए villi उपयुक्त क्यों हैं?|Villi और microvilli area बढ़ाते हैं। Thin epithelium तथा capillary supply nutrient uptake में मदद करते हैं। Digestion बड़े molecules को छोटे करता है; absorption छोटे molecules को body fluids तक पहुँचाता है।''',
'''Autotrophic और heterotrophic nutrition का अंतर दें।|Autotrophs CO₂ जैसे inorganic sources से organic food बनाते हैं। Heterotrophs अन्य organisms से organic food लेते हैं। Green plants photosynthetic autotrophs हैं; humans heterotrophs। दोनों को cellular respiration से usable energy चाहिए।
Bile का कार्य और enzyme से अंतर बताइए।|Bile liver में बनता और gall bladder में संग्रहित होता है। यह fats को छोटे droplets में emulsify करता तथा acidic chyme के neutralisation में मदद करता है। इसमें digestive enzymes नहीं; emulsification enzyme action के लिए area बढ़ाती है।
Breathing और respiration का अंतर क्या है?|Breathing air को lungs में लाने-ले जाने की physical प्रक्रिया है। Cellular respiration food molecules से usable energy मिलने की chemical प्रक्रिया है। Aerobic respiration में oxygen उपयोगी है, पर हर respiration oxygen-dependent नहीं।
Artery और vein की परिभाषा दें।|Arteries blood को heart से दूर और veins heart की ओर ले जाती हैं। Oxygen content पर परिभाषा आधारित नहीं। Pulmonary artery deoxygenated तथा pulmonary vein oxygenated blood लेती है, इसलिए ‘सभी arteries oxygenated’ गलत है।
Xylem और phloem की तुलना करें।|Xylem water/minerals मुख्यतः roots से ऊपर transport करता है; transpiration pull महत्त्वपूर्ण है। Phloem organic food source से sink ले जाता है और ATP का उपयोग कर सकता है। Food movement केवल नीचे ही हो, ऐसा जरूरी नहीं।
Excretion और egestion अलग कैसे हैं?|Excretion metabolic wastes हटाना है, जैसे kidney द्वारा nitrogenous waste। Egestion undigested food को anus से निकालना है। दोनों unwanted material हटाते हैं, पर उत्पत्ति तथा संबंधित organs अलग हैं।''',
'''Human small intestine के digestion/absorption के तीन बिंदु दें।|1. Bile fat emulsification तथा pancreatic enzymes breakdown में मदद करते हैं। 2. Intestinal enzymes absorbable molecules बनाते हैं। 3. Villi large area और vessels देकर uptake संभव करते हैं; digestion और absorption क्रमशः chemical breakdown और transfer हैं।
Double circulation की functional आवश्यकता बताएँ।|1. Pulmonary circuit right ventricle से lungs होकर left atrium आता है। 2. Systemic circuit left ventricle से body होकर right atrium आता है। 3. चार chambers oxygenated और deoxygenated blood का mixing घटाते हैं और oxygen supply कुशल बनाते हैं।
Urine formation के तीन stages लिखें।|1. Glomerulus में pressure filtration से filtrate बनता है। 2. Tubule useful substances और आवश्यक water selectively reabsorb करता है। 3. Tubular secretion अतिरिक्त wastes/ions जोड़ सकती है; शेष fluid urine बनता है। सभी filtered water का निकलना आवश्यक नहीं।
Stomata के दो कार्य और guard cells की भूमिका दें।|1. CO₂/O₂ exchange होता है। 2. Water vapour loss transpiration में योगदान करता है। 3. Guard-cell turgor aperture नियंत्रित करता है; opening–closing की परिस्थितियाँ species और environment पर निर्भर करती हैं।''',
'''Human oxygen supply को breathing से cellular energy तक चार चरणों में समझाएँ।|1. Inhalation air alveoli तक लाती है। 2. Oxygen alveolar wall पार करके capillary blood में diffuses होती है। 3. Haemoglobin और circulation oxygen tissues तक ले जाते हैं। 4. Cells aerobic respiration में oxygen उपयोग कर food से energy प्राप्त करते हैं। CO₂ reverse दिशा से lungs लौटती है; breathing और respiration को एक stage न मानें।
Nephron का schematic बनाने के labels तथा function लिखें।|1. Glomerulus को Bowman's capsule के भीतर filtration स्थल दिखाएँ। 2. Tubule और capillary interface पर reabsorption arrow दिखाएँ। 3. Tubule से collecting duct तथा urine flow का मार्ग दिखाएँ। 4. Tubular secretion को blood से tubule की ओर अलग arrow दें। यह functional schematic है; kidney का anatomical cross-section नहीं।''',
'''Photosynthesis में carbon source क्या है?|CO₂|O₂|N₂|NaCl|Plant carbohydrate का carbon atmospheric/available CO₂ से लेता है।
Salivary amylase मुख्यतः किस पर काम करता है?|Starch|Fat|Cellulose|DNA|Mouth में amylase starch digestion शुरू करता है।
Bile कहाँ बनता है?|Liver|Stomach|Kidney|Lungs|Bile liver में बनता और gall bladder में stored हो सकता है।
Bile का मुख्य fat-related काम क्या है?|Emulsification|Protein digestion|Urea formation|Oxygen transport|Emulsification बड़े fat droplets छोटे करता है; bile enzyme नहीं।
Pyruvate का प्रथम निर्माण कहाँ होता है?|Cytoplasm|केवल nucleus|केवल lungs|केवल kidney|Glycolysis cytoplasm में glucose को pyruvate में बदलती है।
Yeast में anaerobic products कौन-से हैं?|Ethanol और CO₂|Lactate ही|O₂ और water|Urea और ammonia|Yeast fermentation ethanol तथा carbon dioxide देता है।
Lungs में gas exchange का मुख्य स्थल क्या है?|Alveoli|Oesophagus|Ureter|Villi|Alveoli की बड़ी thin-walled surface gas diffusion में मदद करती है।
Pulmonary artery blood कहाँ ले जाती है?|Heart से lungs|Lungs से heart|Kidney से bladder|Liver से stomach|Pulmonary artery right ventricle से lungs को deoxygenated blood ले जाती है।
Left ventricle से body में कौन-सी vessel जाती है?|Aorta|Pulmonary vein|Vena cava|Ureter|Aorta systemic circulation के लिए oxygenated blood ले जाती है।
Water/minerals का मुख्य plant tissue क्या है?|Xylem|Phloem|Epidermis ही|Pollen|Xylem root से water और dissolved minerals का transport करता है।
Plant food translocation का tissue क्या है?|Phloem|Xylem|Bone|Cartilage|Phloem source से sink तक photosynthates ले जाता है।
Kidney की functional unit क्या है?|Nephron|Neuron|Alveolus|Villus|Nephron filtration, reabsorption और secretion में काम करता है।
Kidney से bladder जाने वाली tube क्या है?|Ureter|Urethra|Trachea|Aorta|Ureter kidney का urine bladder तक पहुँचाता है; urethra बाहर ले जाती है।
Undigested food का निष्कासन क्या है?|Egestion|Excretion ही|Photosynthesis|Transpiration|Egestion undigested food हटाना है, metabolic waste removal नहीं।
Villi का मुख्य लाभ क्या है?|Absorption area बढ़ाना|Blood pump करना|Urine बनाना|Nerve impulses देना|Villi intestine का nutrient-absorbing surface area बढ़ाते हैं।''',
'- Bile enzyme नहीं है।\n- Artery/vein को oxygen content से परिभाषित न करें।\n- Ureter और urethra अलग हैं।\n- Yeast में ethanol, muscles में lactate याद रखें।\n- Excretion और egestion न मिलाएँ।',
'Double circulation का क्रम-चित्र। यह मार्ग दिखाता है; anatomical heart diagram नहीं।',
['Right heart', 'Lungs', 'Left heart', 'Body tissues', 'Return to right heart'],
'अगले अध्याय में इन्हीं processes का nervous और hormonal नियंत्रण पढ़ेंगे।')

chapter(6, 'नियंत्रण एवं समन्वय', 'Control and Coordination', 6,
'Neuron और reflex pathway समझना; brain functions, plant movements और endocrine feedback की तुलना करना।',
'''Neuron|Nervous system की impulse-transmitting cell।
Dendrite|Neuron का संकेत ग्रहण करने वाला branched भाग।
Axon|Cell body से impulse आगे ले जाने वाला लंबा भाग।
Synapse|दो neurons अथवा neuron और target के बीच functional junction।
Reflex action|उद्दीपन की तीव्र automatic प्रतिक्रिया।
Cerebrum|Forebrain का भाग; conscious activities और interpretation में भूमिका।
Cerebellum|Balance, posture और movements की precision में भूमिका।
Tropism|Stimulus की दिशा से संबंधित growth movement।
Hormone|Endocrine gland का chemical messenger, blood से target तक जाता है।
Feedback|Response के अनुसार hormone secretion का नियमन।''',
'''### संकेत का मार्ग
Stimulus को receptor पहचानता है। Neuron में dendrite → cell body → axon दिशा में electrical signal आगे जाता है। Chemical synapse पर axon terminal neurotransmitter छोड़ता है; अगली cell के receptor signal ग्रहण करते हैं। इसलिए synaptic crossing chemical और cell के भीतर conduction electrical होती है। Motor neuron effector muscle/gland तक संदेश ले जाता है।

### Reflex और brain
गर्म वस्तु से हाथ हटाने में receptor → sensory neuron → spinal relay → motor neuron → muscle का reflex arc काम कर सकता है। Brain बाद में/साथ में जानकारी प्राप्त करता है; ‘brain को कभी पता नहीं चलता’ गलत है। Cerebrum conscious thinking और sensory interpretation में, cerebellum balance तथा precision में, medulla breathing जैसे involuntary functions में काम करता है। Skull, meninges और cerebrospinal fluid protection देते हैं।

### Plants में coordination
Shoot का light की ओर growth positive phototropism है। Auxin shaded side पर अधिक elongation कराकर shoot को light की ओर मोड़ सकता है। Root सामान्यतः positive gravitropism, shoot negative gravitropism दिखाता है। Tendril touch के अनुसार grows: thigmotropism। Mimosa leaf folding turgor change से होता है; यह growth-based tropism नहीं। Auxin elongation, gibberellin stem growth, cytokinin cell division और ABA growth inhibition/stomatal closure से जुड़े हैं।

### Hormones और feedback
Pituitary growth hormone, thyroid thyroxine, pancreas insulin और adrenal glands adrenaline देते हैं। Thyroxine synthesis के लिए iodine जरूरी है। Insulin blood glucose control में मदद करता है; हर diabetes केवल insulin की पूर्ण अनुपस्थिति नहीं। Adrenaline fight-or-flight में heart rate और respiratory activity जैसे responses बढ़ा सकता है। Blood glucose बढ़ने पर insulin secretion बढ़ना और glucose normal होने पर घटना feedback का उदाहरण है। Hormonal responses अक्सर nervous signalling से धीमे, पर लंबे समय तक प्रभावी होते हैं।''',
'''गर्म तवे से हाथ हटाने का pathway दें।|Skin receptor → sensory neuron → spinal cord relay → motor neuron → arm muscle। Withdrawal reflex तेज protective response है। Brain भी संकेत प्राप्त करता है; reflex होने का अर्थ consciousness हमेशा absent नहीं।
Shoot phototropism में shaded side की वृद्धि अधिक हो तो झुकाव कैसा होगा?|Shaded side अधिक लंबी होने से shoot light की ओर bends करता है। Shoot में auxin का unequal distribution differential elongation करता है; light की ओर वाली side को ही अधिक बढ़ना लिखना उल्टा होगा।
Iodine deficiency और thyroid का संबंध दें।|Iodine thyroxine synthesis का घटक है। कमी से thyroid function प्रभावित और gland enlargement/goitre हो सकता है। यह पाठ कारण-संबंध समझाता है; सभी neck swellings को goitre कहकर diagnosis नहीं करता।''',
'''Electrical और chemical signals neuron में कहाँ काम करते हैं?|Neuron membrane के along impulse electrochemical changes से travels करता है। Chemical synapse पर neurotransmitter gap पार करके next cell को signal देता है। इसीलिए ‘impulse हर स्थान पर केवल electrical jump है’ उचित नहीं।
Reflex और voluntary action में अंतर दें।|Reflex rapid automatic response है, जैसे withdrawal। Voluntary action conscious control से होता है, जैसे लिखना। दोनों में neurons और muscles काम करते हैं, लेकिन pathways और initiation अलग हो सकते हैं।
Cerebellum और medulla की तुलना करें।|Cerebellum posture, balance और precise movement में भूमिका निभाता है। Medulla breathing तथा अन्य involuntary functions में भूमिका निभाता है। Brain भागों के कामों को एक-दूसरे पर न लिखें।
Tropism और Mimosa folding में अंतर दें।|Tropism stimulus direction से संबंधित growth movement है। Mimosa folding mainly cell turgor change से rapid response है, growth से नहीं। इसलिए हर plant movement को tropism कहना गलत है।
Nervous और hormonal control की तुलना करें।|Nervous control specific neural pathways से signals भेजता और सामान्यतः तेज response देता है। Hormones blood से target cells तक जाते और अक्सर धीमे/दीर्घकालीन effects देते हैं। Target receptors specificity देते हैं; blood सभी cells तक पहुँचना समान response का अर्थ नहीं।
Insulin feedback का सरल उदाहरण दें।|Blood glucose बढ़ने पर pancreas की insulin secretion बढ़ सकती है। Cells glucose uptake/storage बढ़ाते हैं और glucose घटता है। फिर insulin stimulus कम हो जाता है। Response द्वारा initial signal घटाना negative feedback है।''',
'''Neuron के तीन मुख्य भाग और दिशा लिखें।|1. Dendrites signals receive करते हैं। 2. Cell body cell metabolism और signal integration में भाग लेता है। 3. Axon terminal तक impulse ले जाता है, जहाँ neurotransmitter निकल सकता है। Diagram arrows dendrite से terminal की ओर दिखाएँ।
Reflex arc का labelled schematic कैसे बनाएँ?|1. Receptor से sensory neuron का arrow spinal cord की ओर। 2. Cord में relay/interneuron junction दिखाएँ। 3. Motor neuron का arrow effector muscle की ओर और response लिखें। Brain connection छूटने पर ‘brain असंबद्ध’ का दावा न जोड़ें।
चार plant hormones का एक-एक काम दें।|1. Auxin shoot cell elongation तथा tropic growth में मदद करता है। 2. Gibberellin stem growth और cytokinin cell division से जुड़े हैं। 3. ABA growth inhibition तथा water-stress में stomatal closing में भूमिका निभाता है। Effects tissue/conditions से बदलते हैं।
Adrenaline response के तीन effects दें।|1. Heart rate/force बढ़ सकते हैं, tissues को blood supply बदलती है। 2. Airways और breathing-related responses oxygen availability बढ़ाते हैं। 3. Energy substrates की availability बढ़ती है। यह acute response है; hormone की हर भूमिका growth नहीं।''',
'''Nervous और endocrine coordination को भोजन के बाद glucose regulation तथा गर्म वस्तु छूने के उदाहरणों से समझाएँ।|1. भोजन के बाद blood glucose signal pancreas तक पहुँचता है। 2. Insulin blood द्वारा target tissues पर uptake/storage बढ़ाता है; negative feedback secretion घटाता है। 3. गर्म वस्तु पर receptors और reflex neural pathway withdrawal कराते हैं। 4. दोनों communication systems हैं, पर messenger, route और timescale अलग हैं।
Shoot phototropism और root gravitropism की तुलना labelled arrows से करें।|1. Light source एक ओर और shoot curvature उसकी ओर दिखाएँ: positive phototropism। 2. Shoot की shaded side पर relatively more elongation लिखें। 3. Root growth gravity की ओर दिखाएँ: positive gravitropism। 4. Shoot gravity से विपरीत: negative gravitropism। Stimulus direction और positive/negative relation स्पष्ट रखें।''',
'''Neuron में reception का प्रमुख branched भाग कौन है?|Dendrite|Axon terminal ही|Myelin ही|Bone|Dendrites incoming signals receive करते हैं।
Chemical synapse पर messenger क्या है?|Neurotransmitter|Urea|Bile|Haemoglobin|Neurotransmitter axon terminal से released होकर next cell receptors पर काम करता है।
Withdrawal reflex में common relay center क्या है?|Spinal cord|Kidney|Liver|Pancreas|Spinal pathways तेज withdrawal response सम्भव करते हैं; brain को सूचना भी मिलती है।
Balance और movement precision में कौन-सा भाग काम करता है?|Cerebellum|Thyroid|Medulla ही|Retina|Cerebellum posture, balance और coordination में महत्त्वपूर्ण है।
Breathing जैसे involuntary functions से कौन जुड़ा है?|Medulla|Cerebellum ही|Pituitary ही|Lens|Medulla hindbrain का भाग है और involuntary control में भूमिका निभाता है।
Shoot का light की ओर growth क्या है?|Positive phototropism|Negative phototropism|Positive hydrotropism|Nastic folding|Stimulus light है और growth उसकी ओर, इसलिए positive phototropism।
Root का gravity की ओर growth क्या है?|Positive gravitropism|Negative gravitropism|Photolysis|Chemolysis|Root growth gravity की दिशा में होने से positive gravitropism है।
Mimosa leaf folding का मुख्य immediate कारण क्या है?|Turgor change|नई bone बनना|केवल cell division|Photosynthesis बंद होना|Rapid leaf folding growth के बजाय cells के turgor changes से जुड़ा है।
Cell division को promote करने वाला plant hormone कौन है?|Cytokinin|Insulin|Thyroxine|Testosterone|Cytokinins plant cell division को promote कर सकते हैं।
Thyroxine synthesis के लिए कौन-सा element जरूरी है?|Iodine|Iron ही|Sodium ही|Calcium ही|Thyroxine molecule में iodine शामिल है।
Insulin का source कौन है?|Pancreas|Thyroid|Testis|Pituitary|Pancreas के endocrine cells insulin secretion करते हैं।
Fight-or-flight hormone कौन है?|Adrenaline|Auxin|Pepsin|Bile|Adrenaline acute stress response में multiple physiological changes करता है।
Growth-inhibiting plant hormone कौन है?|ABA|Gibberellin|Cytokinin|Insulin|Abscisic acid growth inhibition और stress responses से जुड़ा है।
Target cell hormone को कैसे पहचानती है?|Specific receptors|केवल आकार बड़ा होने से|Blood का रंग देखकर|हर cell एक जैसा respond करता है|Hormone response के लिए suitable receptors और cell machinery जरूरी हैं।
Negative feedback में response मूल stimulus पर क्या करता है?|उसे घटाता है|हमेशा बढ़ाता है|उसे metal बनाता है|उससे कोई संबंध नहीं|Negative feedback initial change को counter करके regulation में मदद करता है।''',
'- Cerebellum को breathing center न लिखें।\n- Reflex में brain को सूचना मिलती है।\n- Mimosa folding growth tropism नहीं।\n- Iodine gland नहीं, thyroxine का आवश्यक घटक है।\n- Insulin feedback को positive feedback न कहें।',
'Withdrawal reflex का simplified functional path; arrows signal direction दिखाते हैं।',
['Skin receptor', 'Sensory neuron', 'Spinal relay', 'Motor neuron', 'Muscle response'],
'अगले अध्याय में reproductive hormones और नए organisms बनने के processes आएँगे।',
'2025, प्रश्न 1(iv), PDF पृष्ठ 3: plant hormone की पहचान। उत्तर-संकेत: cytokinin।')

chapter(7, 'जीव जनन कैसे करते हैं?', 'How do Organisms Reproduce?', 7,
'Asexual/sexual reproduction अलग करना; flower और human reproductive pathways समझना; contraception और infection prevention की सीमाएँ बताना।',
'''DNA copying|Genetic information की replication; reproduction में continuity का आधार।
Binary fission|एक cell का दो daughter cells में विभाजन।
Fragmentation|Body fragments से उपयुक्त organisms में नए individuals बनना।
Regeneration|Specialised cells से खोए भाग/कुछ organisms में पूरा organism पुनः बनना।
Budding|Parent पर outgrowth से नया individual बनना।
Vegetative propagation|Root/stem/leaf से नए plants बनना।
Pollination|Pollen का anther से stigma तक पहुँचना।
Fertilisation|Male और female gametes का fusion।
Placenta|Maternal–fetal exchange का interface।
Contraception|Pregnancy की संभावना घटाने की विधियाँ।''',
'''### Continuity और variation
Reproduction individual survival के लिए अनिवार्य नहीं, species continuity के लिए महत्त्वपूर्ण है। DNA copying information आगे देती है, और copying differences variation ला सकते हैं। Sexual reproduction दो parents के genetic contributions मिलाकर variation बढ़ा सकता है; asexual offspring भी हमेशा absolutely identical नहीं होते।

### Asexual methods
Amoeba binary fission, Plasmodium multiple fission, yeast/Hydra budding, Spirogyra fragmentation तथा Rhizopus spores से reproduction के उदाहरण हैं। Planaria में suitable fragments specialised regenerative cells से नए individuals बना सकते हैं; हर cut body part ऐसा नहीं करता। Bryophyllum leaf buds और potato stem tuber vegetative propagation दिखाते हैं। यह plants के उपयोगी गुण जल्दी बनाए रखने में मदद कर सकता है।

### Flower में sexual reproduction
Stamen में anther pollen बनाता है। Pistil के stigma पर suitable pollen germinate होकर style से pollen tube भेजता है। Male gamete ovule में female gamete से fertilises करके zygote बनाता है। Ovule seed और ovary fruit बनता है। Pollination gamete fusion नहीं; fertilisation उसके बाद की अलग stage है। Flowering plants में embryo seed में विकसित होता है।

### Human reproduction और health
Testes sperm और testosterone बनाते हैं; scrotal location sperm formation के लिए suitable lower temperature देती है। Sperm ducts से urethra की ओर जाते हैं और glands के fluids semen बनाते हैं। Ovaries ova और hormones देते हैं। Fertilisation सामान्यतः oviduct में; embryo uterus lining में implants होता है। Placenta nutrients, oxygen और wastes exchange करता है; maternal और fetal blood normally सीधे एक common pool नहीं बनाते। Fertilisation न होने पर uterine lining का shedding menstruation है; cycle length व्यक्ति और समय के अनुसार बदल सकती है। Condoms pregnancy के साथ कई sexually transmitted infections का risk भी घटाते हैं। Hormonal pills/IUDs pregnancy prevention देते हैं लेकिन STI protection नहीं। Reproductive health में consent, reliable information, hygiene और clinical help शामिल हैं।''',
'''Pollination से seed बनने का क्रम दें।|Anther → stigma पर pollen transfer → pollen tube growth → ovule में gamete fusion → zygote/embryo → seed। Ovary fruit बनती है। Pollen transfer और fertilisation को एक ही घटना न लिखें।
Potato और Bryophyllum में reproductive structures पहचानें।|Potato के eyes stem tuber buds हैं, roots नहीं। Bryophyllum leaf margins पर buds नए plants बना सकते हैं। दोनों vegetative propagation हैं और seed formation आवश्यक नहीं।
Human fertilisation और implantation के स्थान दें।|Fertilisation सामान्यतः oviduct/fallopian tube में होता है। विकसित embryo uterus की endometrium में implants होता है। Uterus में sperm और ovum का fusion होना सामान्य anatomical answer नहीं।''',
'''DNA copying के साथ variation क्यों उपयोगी है?|Copying genetic continuity देता है; occasional changes variation ला सकते हैं। Changing environment में कुछ variants survival/reproduction में लाभ दे सकते हैं। हर variation लाभदायक नहीं और reproduction individual के जीवित रहने की शर्त नहीं।
Fission और budding की तुलना दें।|Binary fission में parent cell दो daughter cells में divides होता है। Budding में parent पर छोटा outgrowth विकसित होकर नया individual बन सकता है। Amoeba तथा yeast क्रमशः standard उदाहरण हैं।
Fragmentation और regeneration अलग कैसे हैं?|Fragmentation में सरल body fragments से नए organisms बनते हैं, जैसे Spirogyra। Regeneration specialised cells द्वारा repair या कुछ organisms में पूरा नया organism बनना है। हर multicellular animal का टुकड़ा नया organism नहीं बना सकता।
Testes के दो functions तथा scrotum का महत्व दें।|Testes sperms और testosterone बनाते हैं। Scrotum उन्हें body core से कुछ कम ताप पर रखने में मदद करता है, जो sperm formation के लिए उपयुक्त है। Ducts sperm बनाते नहीं; उनका transport करते हैं।
Placenta का function क्या है?|Placenta maternal और fetal sides के बीच oxygen/nutrients तथा wastes exchange का interface है। यह embryo को nourishment और gas exchange उपलब्ध करता है। दोनों blood systems सामान्यतः सीधे मिश्रित common circulation नहीं बनाते।
Condom और pills की protection अलग कैसे है?|Condom barrier method है जो pregnancy तथा कई STIs का risk कम करता है, पूर्ण गारंटी नहीं। Hormonal pills pregnancy prevention के लिए हैं और STI protection नहीं देतीं। Method choice trained health professional और informed consent से होनी चाहिए।''',
'''Flower के reproductive parts और fertilisation समझाएँ।|1. Anther pollen बनाता है; stigma pollen ग्रहण करता है। 2. Pollen tube style से ovule तक male gamete पहुँचाती है। 3. Gamete fusion से zygote, आगे embryo बनता है; ovule seed और ovary fruit बनती है।
Human female pathway का labelled क्रम दें।|1. Ovary से ovum release होता है। 2. Oviduct सामान्य fertilisation site है। 3. Embryo uterus lining में implantation करता है; cervix uterus का lower opening और vagina birth canal का भाग है। Diagram organs का connection दिखाए।
Menstruation के कारण और cycle variation लिखें।|1. Cycle में uterus lining potential pregnancy के लिए तैयार होती है। 2. Pregnancy न होने पर hormonal changes से lining shed हो सकती है। 3. Blood और tissue vagina से बाहर आते हैं; duration/cycle length में variation है। इसे बीमारी या ‘impure blood’ न कहें।
Three contraception categories और सीमा दें।|1. Barrier condom sperm entry घटाता और STI risk कम करता है। 2. Hormonal methods ovulation/अन्य reproductive processes बदल सकते हैं। 3. IUD/surgical methods pregnancy prevention में इस्तेमाल होते हैं; सभी methods STI protection नहीं देते। Clinical counselling जरूरी है।''',
'''Asexual reproduction की चार विधियाँ उदाहरण सहित दें।|1. Amoeba: binary fission, एक cell से दो। 2. Yeast/Hydra: budding, parent पर outgrowth। 3. Spirogyra: fragmentation, body pieces से growth। 4. Rhizopus: spores, suitable conditions में germination। Examples और methods अलग लिखें; regeneration को हर organism का universal reproduction न बनाएँ।
Fertilisation से birth तक simplified stages और placenta की भूमिका समझाएँ।|1. Oviduct में sperm–ovum fusion से zygote बनता है। 2. Divisions के बाद embryo uterus में implants करता है। 3. Placenta oxygen/nutrients देता और wastes transfer करता है; fetus uterus में grows करता है। 4. Birth पर baby बाहर आता है। Diagram stage order है, fetus या reproductive organs की anatomical scale नहीं।''',
'''Amoeba का सामान्य reproduction mode क्या है?|Binary fission|Budding|Seed formation|Vegetative propagation|Amoeba cell division से दो daughter cells बना सकता है।
Yeast का सामान्य asexual mode क्या है?|Budding|Pollination|Fertilisation|Fragmentation ही|Yeast में parent पर bud निकलकर नया cell बन सकता है।
Spirogyra किस विधि का उदाहरण है?|Fragmentation|Budding|Binary fission|Seed formation|Spirogyra filament के fragments suitable conditions में grow कर सकते हैं।
Rhizopus में dispersal reproductive structures क्या हैं?|Spores|Sperms|Ovules|Potato eyes|Rhizopus sporangia में spores बनते हैं।
Bryophyllum vegetative propagation कहाँ से कर सकता है?|Leaf buds|केवल flower pollen|केवल roots ही|केवल seed coat|Leaf margin buds नए plants बना सकते हैं।
Pollen transfer anther से stigma तक क्या है?|Pollination|Fertilisation|Implantation|Menstruation|Pollination pollen transfer है; gamete fusion fertilisation है।
Fertilisation के बाद ovule क्या बनता है?|Seed|Fruit ही|Stigma|Anther|Ovule seed बनता है; ovary fruit बनती है।
Human fertilisation का सामान्य स्थान क्या है?|Oviduct|Uterus ही|Vagina|Ovary surface ही|Fertilisation सामान्यतः fallopian tube/oviduct में होता है।
Embryo implantation का स्थान क्या है?|Uterus lining|Testis|Ureter|Anther|Endometrium embryo implantation का site है।
Sperm का production site कौन है?|Testes|Prostate|Urethra|Seminal vesicle|Testes sperm बनाते हैं; accessory glands fluids देती हैं।
Testosterone का मुख्य male source कौन है?|Testes|Kidneys|Lungs|Thyroid|Testes testosterone secrete करते हैं।
Maternal–fetal exchange interface क्या है?|Placenta|Cerebellum|Nephron|Villus ही|Placenta fetus को nutrient/gas exchange interface देता है।
Pregnancy और कई STI risks दोनों घटाने का barrier कौन है?|Condom|Hormonal pill ही|IUD ही|Withdrawal की गारंटी|Condom barrier protection देता है; सही उपयोग के बावजूद risk zero नहीं।
Potato के eyes क्या हैं?|Stem buds|Roots|Pollen grains|Ovules|Potato tuber modified stem है; eyes buds हैं।
Species continuity के लिए reproduction क्यों महत्त्वपूर्ण है?|नए individuals बनते हैं|हर individual तभी साँस लेता है|हर variation समान होता है|DNA हमेशा बदलता ही नहीं|Reproduction generations के बीच population continuity रखता है।''',
'- Pollination और fertilisation अलग stages हैं।\n- Ovule से seed, ovary से fruit।\n- Fertilisation oviduct, implantation uterus में।\n- Placenta में दोनों blood systems का सामान्य direct mixing न लिखें।\n- Pills को STI prevention न कहें।',
'Flower में pollination से seed/fruit बनने का stage schematic; anatomical drawing नहीं।',
['Pollen to stigma', 'Pollen tube', 'Fertilisation in ovule', 'Ovule: seed', 'Ovary: fruit'],
'अगले अध्याय में reproduction से आने वाले inherited traits के ratios समझेंगे।',
'2025, प्रश्न 1(ii), PDF पृष्ठ 2: regeneration से नया organism बनने का उदाहरण। उत्तर-संकेत: Planaria।')

chapter(8, 'आनुवंशिकता', 'Heredity', 4,
'Genotype/phenotype अलग करना; mono/dihybrid crosses के ratios सही शर्तों सहित निकालना; human sex determination का वैज्ञानिक विवरण देना।',
'''Heredity|Parents से offspring तक genetic traits का transmission।
Variation|Individuals के लक्षणों में differences।
Gene|DNA का functional hereditary information वाला segment।
Allele|Gene का alternative form।
Genotype|किसी trait के लिए genetic constitution, जैसे Tt।
Phenotype|Expressed/observable characteristic, जैसे tall।
Dominant allele|Heterozygous condition में recessive के ऊपर expressed allele।
Recessive allele|Simple complete dominance में homozygous होने पर expressed allele।
Monohybrid cross|एक trait के contrasting forms पर केंद्रित cross।
Segregation|Gamete formation में allele pair के अलग होना।''',
'''### लक्षण का genetic आधार
DNA information से proteins बनते हैं; proteins और cellular processes traits के expression में भूमिका निभाते हैं। Environment भी phenotype को प्रभावित कर सकता है। Mendel ने peas में contrasting traits और controlled crosses का उपयोग किया। Dominant का अर्थ अधिक common, बेहतर या ताकतवर नहीं; heterozygote में expression का संबंध है। Bodybuilding से बढ़ी muscle जैसी acquired change स्वतः inherited gene change नहीं बन जाती।

### एक trait की गणना
Pure tall TT × dwarf tt से F₁ सभी Tt और complete dominance में tall होते हैं। F₁ selfing Tt × Tt में दोनों parents T और t gametes देते हैं। Punnett outcomes TT, Tt, Tt, tt हैं। Genotype ratio 1:2:1 और phenotype ratio 3 tall:1 dwarf। ये expected probabilities हैं, हर चार plants का exact count नहीं। Recessive allele F₁ में गायब नहीं हुआ; hidden expression था।

### दो traits और independence
RRYY × rryy से F₁ RrYy मिलता है। Unlinked/independently assorting traits और complete dominance की school model conditions में F₁ gametes RY, Ry, rY, ry equal probabilities से बनते हैं। Selfing में phenotype ratio 9:3:3:1 हो सकता है। हर pair of human genes पर यही ratio लागू नहीं; linkage और अन्य inheritance patterns अलग हो सकते हैं।

### Human sex determination
विद्यालयी XX–XY model में egg X देता है, sperm X या Y दे सकता है। X sperm से XX और Y sperm से XY outcome मिलता है; simplified expectation लगभग equal probabilities है। Child का chromosomal sex mother के X egg से तय करने का दावा गलत है। यह biological probability है; किसी parent को दोष देने का आधार नहीं। वास्तविक sex development में अन्य biological variation भी हो सकती है; यह model सभी complexities का वर्णन नहीं।''',
'''Tt × tt से offspring ratio निकालें।|Tt parent T या t gametes, tt parent केवल t देता है। Outcomes Tt और tt समान expected probability से मिलते हैं। Complete dominance में tall:dwarf = 1:1, genotype Tt:tt = 1:1।
Tt × Tt में recessive phenotype की probability दें।|Punnett square: TT, Tt, Tt, tt। केवल tt recessive phenotype देता है, इसलिए 1/4 = 25% expected probability। चार actual offspring में exactly एक recessive अनिवार्य नहीं।
XX–XY cross लिखें।|Egg gametes X; sperm gametes X या Y। Outcomes XX और XY लगभग 1:1 expected हैं। Maternal contribution दोनों cases में X है; variation paternal gamete से आती है।''',
'''Genotype और phenotype में अंतर दें।|Genotype genetic constitution है, जैसे TT या Tt। Phenotype expressed trait है, जैसे tall। Complete dominance में TT और Tt का phenotype समान हो सकता है; इसलिए केवल appearance से genotype हमेशा नहीं मिलता।
Dominant का अर्थ stronger क्यों नहीं है?|Dominance heterozygote में allele expression बताती है। यह allele की physical strength, नैतिक श्रेष्ठता या population frequency का दावा नहीं। Rare allele भी dominant हो सकता है।
F₁ में recessive trait कहाँ गया?|Tt genotype में recessive allele t मौजूद है, पर dominant T के साथ उसका phenotype expressed नहीं होता। Gamete formation पर t अलग होकर आगे जा सकता है; F₂ tt होने पर recessive phenotype लौटता है।
Inherited और acquired traits अलग कैसे हैं?|Inherited genetic information offspring को gametes से मिलती है। Acquired body changes, जैसे training से muscle, अपने आप gamete DNA में समान बदलाव नहीं करतीं। इसलिए parent के अभ्यास का identical biological trait inheritance दावा गलत है।
Mendel का segregation नियम समझाएँ।|Allele pair gamete formation के दौरान अलग होता है और प्रत्येक gamete में pair का एक allele जाता है। Tt individual T और t gametes दे सकता है। Fertilisation में दो gametes फिर pair बनाते हैं।
9:3:3:1 ratio की शर्तें बताइए।|दो independently assorting traits, complete dominance और suitable dihybrid self-cross की school model conditions में यह phenotype ratio है। Linked genes तथा अलग inheritance patterns में ratio बदल सकता है। इसे universal genetic ratio न लिखें।''',
'''TT × tt और F₁ selfing का पूरा monohybrid result दें।|1. Parents TT और tt gametes T तथा t देते हैं। 2. F₁ सभी Tt, phenotype dominant। 3. Tt × Tt से TT:Tt:tt = 1:2:1 और phenotype 3:1। दोनों ratios को अलग label दें।
Genotype से gametes निकालना समझाएँ।|1. TT केवल T allele वाले gametes देता है। 2. Tt, T और t gametes दे सकता है। 3. Independent assortment में RrYy चार प्रकार RY, Ry, rY, ry दे सकता है। Gamete में diploid pair पूरा न लिखें।
Sex determination के model की तीन बातें दें।|1. XX parent के eggs X-containing हैं। 2. XY parent के sperms X अथवा Y-containing हो सकते हैं। 3. Fusion से XX/XY outcomes मिलते हैं; कोई parent ‘जानबूझकर’ outcome नहीं चुनता। Model और social blame को न जोड़ें।
Trait expression को protein से जोड़ें।|1. Gene DNA information देता है। 2. इससे बनने वाले proteins/enzymes cell pathways को प्रभावित करते हैं। 3. Growth जैसे traits pathway activity और environment से प्रभावित हो सकते हैं। Gene को सीधे हर trait का अकेला visible particle न कहें।''',
'''Tt × Tt का Punnett square बनाकर genotype, phenotype और probabilities दें।|1. ऊपर T,t तथा बाईं ओर T,t gametes लिखें। 2. Four boxes में TT, Tt, Tt, tt लिखें। 3. Genotype probabilities 1/4, 1/2, 1/4 हैं। 4. Complete dominance में tall 3/4 और dwarf 1/4। Small actual sample में ratio expected से अलग हो सकता है।
Independent dihybrid cross में 9:3:3:1 का अर्थ तथा सीमा लिखें।|1. RrYy parents चार gamete types देते हैं। 2. 16-cell square में दोनों dominant phenotypes 9, पहला dominant/दूसरा recessive 3। 3. पहला recessive/दूसरा dominant 3 और दोनों recessive 1। 4. Independent assortment तथा complete dominance जरूरी हैं; यह genotype ratio नहीं और सभी genes पर लागू नहीं।''',
'''Tt का genotype किस प्रकार का है?|Heterozygous|Homozygous dominant|Homozygous recessive|Gamete|Tt में एक gene के दो अलग alleles हैं।
TT × tt के F₁ genotype क्या होंगे?|सभी Tt|सभी TT|सभी tt|आधे TT आधे tt|Parents केवल T और t gametes देते हैं, इसलिए offspring Tt होते हैं।
Tt × Tt का genotype ratio क्या है?|1:2:1|3:1|9:3:3:1|1:1|TT,Tt,Tt,tt से 1 TT : 2 Tt : 1 tt मिलता है।
Complete dominance में F₂ phenotype ratio क्या है?|3:1|1:2:1|1:1|4:0|TT तथा दो Tt dominant, एक tt recessive phenotype देता है।
Tt × tt का phenotype ratio क्या है?|1:1|3:1|9:3:3:1|1:2:1|एक parent T/t, दूसरा t gametes देता है, इसलिए Tt और tt बराबर expected हैं।
Gene का alternative form क्या कहलाता है?|Allele|Neuron|Villus|Hormone|Alleles एक gene के alternative versions हैं।
Expressed characteristic का नाम क्या है?|Phenotype|Genotype ही|Gamete|Chromatid ही|Phenotype observable/expressed trait है।
Dominant allele का सही अर्थ क्या है?|Heterozygote में expressed|हमेशा सबसे common|हमेशा बेहतर|हमेशा बड़ा chromosome|Dominance expression का संबंध है, quality या frequency का नहीं।
Tt से कौन-से gametes बनते हैं?|T और t|केवल Tt|TT और tt|केवल TT|Segregation gamete में pair का एक allele पहुँचाता है।
Independent RrYy से gamete कौन हो सकता है?|Ry|Rr|Yy|RrYy|Gamete में दोनों genes के लिए एक-एक allele चाहिए।
Dihybrid expected phenotype ratio क्या है?|9:3:3:1|1:2:1|3:1|2:2:2|Independent assortment और complete dominance में school dihybrid ratio 9:3:3:1 है।
Human egg में सामान्य sex chromosome कौन है?|X|Y ही|XY pair|कोई नहीं|XX–XY school model में egg X-containing होता है।
XY outcome किस sperm से बनता है?|Y-containing sperm|X-containing sperm|केवल XX sperm|बिना sperm|X egg और Y sperm के fusion से XY chromosome combination मिलता है।
Tt × Tt में tt की probability क्या है?|25%|50%|75%|100%|चार equal expected combinations में एक tt है।
Training से muscle बढ़ना किसका उदाहरण है?|Acquired trait|हर बार inherited mutation|Sex chromosome|Allele segregation|Training-related body change acquired है; gamete DNA में वही परिवर्तन जरूरी नहीं।''',
'- 3:1 phenotype, 1:2:1 genotype है।\n- Dominant का अर्थ श्रेष्ठ/अधिक common नहीं।\n- Gamete में allele pair न रखें।\n- Ratios probabilities हैं, छोटी sample की guarantee नहीं।\n- Sex determination में mother को दोष देने का scientific आधार नहीं।',
'Monohybrid cross का simplified genotype summary; विस्तृत 2×2 Punnett square उत्तर में बनाने का निर्देश है।',
['Tt × Tt', 'Gametes: T / t', 'TT, Tt, Tt, tt', 'Genotype 1:2:1', 'Phenotype 3:1'],
'अब genetics से optics की ओर: अगले अध्याय में signs और geometric rays की नई भाषा आएगी।',
'2025, प्रश्न 1(v), PDF पृष्ठ 3: monohybrid F₂ genotype ratio। उत्तर-संकेत: 1:2:1।')

chapter(9, 'प्रकाश: परावर्तन तथा अपवर्तन', 'Light — Reflection and Refraction', 8,
'Reflection/refraction laws, mirror और lens signs का उपयोग; image cases समझना; distance, magnification और power की गणना करना।',
'''परावर्तन|Light का उसी medium में surface से वापस लौटना।
अपवर्तन|Medium बदलने पर light speed और सामान्यतः direction बदलना।
Principal axis|Mirror pole/curvature center अथवा lens optical center से जाने वाली axis।
Focus|Axis-parallel paraxial rays का मिलने/मिलते प्रतीत होने वाला बिंदु।
Mirror formula|1/f = 1/v + 1/u; Cartesian signs सहित।
Mirror magnification|m = −v/u = hᵢ/hₒ।
Lens formula|1/f = 1/v − 1/u; Cartesian signs सहित।
Lens magnification|m = v/u = hᵢ/hₒ।
Refractive index|n = c/v; vacuum speed / medium speed।
Lens power|P = 1/f, f metre में; unit dioptre (D)।''',
'''### नियम और conventions
Reflection में incident ray, reflected ray और normal एक plane में तथा angle i = angle r होता है। Angles normal से मापें, surface से नहीं। Refraction के लिए same plane और $\\sin i/\\sin r=n_{21}$, fixed media और wavelength के लिए। Normal incidence पर speed बदल सकती है जबकि direction नहीं बदलती। Optically denser में oblique ray normal की ओर और rarer में दूर bends करती है। Optical density mass density का पर्याय नहीं।

### Mirrors और image cases
New Cartesian convention में pole origin; incident light की दिशा positive, opposite negative; axis के ऊपर height positive। Left-side object के लिए u negative है। Concave mirror f negative, convex f positive। Concave में object beyond C: image F–C, real/inverted/diminished; at C: at C/same size; C–F: beyond C/enlarged; at F: infinity; F–P: virtual/erect/enlarged behind mirror। Convex finite object के लिए virtual/erect/diminished image P–F behind mirror देता है। Paraxial spherical mirrors में R = 2f।

### Lenses और rays
Convex lens positive f; concave negative f। Axis-parallel ray convex lens के far focus की ओर जाती है; optical-center ray thin-lens approximation में undeviated है। Convex object beyond 2F: image F–2F; at 2F: at 2F/same size; F–2F: beyond 2F/enlarged; at F: infinity; within F: virtual/erect/enlarged object side। Concave lens finite real object के लिए virtual/erect/diminished image object side O–F देता है। Image तभी बनती है जब rays intersect या backward extensions intersect करते हैं; अकेली ray पर्याप्त नहीं।

### Formula से उत्तर की जाँच
Mirror में $1/f=1/v+1/u$ और $m=-v/u$; lens में $1/f=1/v-1/u$ और $m=v/u$। Negative magnification inverted, positive erect image दर्शाता है। Distance units एक जैसी रखें। Lens power metre वाली focal length का reciprocal है: +0.5 m convex lens का +2 D। Rectangular slab emergent ray parallel लेकिन laterally displaced हो सकती है; normal incidence पर displacement शून्य है।''',
'''Concave mirror: u = −30 cm, f = −15 cm। v और m निकालें।|1/v = 1/f − 1/u = −1/15 + 1/30 = −1/30। v = −30 cm। m = −v/u = −1; image real, inverted और same size है, object C पर है।
Convex lens: u = −30 cm, f = +20 cm। v तथा m दें।|1/v = 1/f + 1/u = 1/20 − 1/30 = 1/60। v = +60 cm। m = v/u = −2। Image lens के दूसरी ओर real, inverted, double height है।
Concave lens f = −25 cm की power निकालें।|f = −0.25 m। P = 1/f = −4 D। Minus sign diverging lens दर्शाता है। 1/(−25) D लिखना cm को metre में न बदलने की गलती होगी।''',
'''Reflection angles normal से क्यों मापें?|Reflection law i=r में incidence/reflection angles normal और respective ray के बीच हैं। Surface से measured angles complementary होते हैं; question का angle किस reference से है, पहले पहचानें। Diagram में normal अलग dashed line दिखाएँ।
Real और virtual image का अंतर दें।|Real image actual light rays के intersection से बनती है और screen पर प्राप्त हो सकती है। Virtual image backward extensions के apparent intersection से बनती है; उसे उसी स्थान पर screen से capture नहीं कर सकते। Orientation alone परिभाषा नहीं।
Convex mirror vehicle rear-view में क्यों उपयोगी है?|यह finite objects की erect, diminished virtual image और wide field of view देता है। इसलिए अधिक पीछे का क्षेत्र दिखाई देता है। Objects छोटे दिखने से distance का गलत अनुमान हो सकता है; इसे magnifying mirror न कहें।
Lens और mirror magnification का अंतर बताइए।|Mirror formula m=−v/u और thin lens formula m=v/u है। दोनों में m=hᵢ/hₒ; negative sign inverted image का संकेत है। Formula बदलने पर एक ही memorised sign न लगाएँ।
Optical density और mass density अलग कैसे हैं?|Optical density light speed/refractive index से संबंधित है। Mass density mass per unit volume है। Mass-density comparison से refraction की दिशा का universal निर्णय नहीं किया जा सकता; refractive indices उपयोग करें।
Glass slab से emergent ray parallel क्यों होती है?|Slab की opposite refracting faces parallel हैं। दूसरे interface का bending पहले के angular deviation को compensate करता है, इसलिए बाहर same medium में emergent ray incident ray के parallel होती है। Path में lateral shift रह सकता है।''',
'''Concave mirror के three standard construction rays दें।|1. Parallel ray reflection के बाद F से गुजरती है। 2. F से होकर आने वाली ray axis parallel reflect होती है। 3. C की ओर ray normal incidence के कारण अपना path retrace करती है। कम से कम दो rays से image locate करें।
Convex lens beyond 2F case समझाएँ।|1. Object को 2F से दूर रखें। 2. Top से axis-parallel ray far F की ओर और optical-center ray straight draw करें। 3. Rays lens की दूसरी ओर F–2F में मिलती हैं; image real, inverted और diminished है।
Snell law और normal incidence की सीमा दें।|1. Fixed media के लिए sin i/sin r relative index है। 2. Denser medium में oblique ray normal की ओर मुड़ती है। 3. i=0 पर r=0, direction unchanged रहती है; speed/wavelength बदल सकती है। 0/0 को ordinary quotient की तरह न compute करें।
Convex lens within-focus case समझाएँ।|1. Object lens और near F के बीच हो। 2. Refracted rays diverge; backward extensions object side पर मिलती हैं। 3. Image virtual, erect और magnified है; real rays सामने screen पर इस image को नहीं बनातीं।''',
'''Concave mirror f = −10 cm में u = −15 cm पर object है। v, m और nature दें।|1. 1/v = −1/10 + 1/15 = −1/30। 2. v = −30 cm। 3. m = −(−30)/(−15) = −2। 4. Image real, inverted और twice size; C से परे बनती है। Sign, magnitude और qualitative ray case तीनों consistent हैं।
Convex lens f = +15 cm, u = −10 cm के लिए image दें तथा diagram steps लिखें।|1. 1/v = 1/15 − 1/10 = −1/30, v = −30 cm। 2. m = (−30)/(−10) = +3। 3. Virtual, erect, three times size, object side। 4. Parallel-to-focus ray और optical-center ray की backward extensions draw करें; object F के भीतर है।''',
'''Reflection में i और r का संबंध क्या है?|i = r|i = 2r|i + r = 180° हमेशा|i = 0 हमेशा|दोनों angles surface normal से मापने पर बराबर हैं।
Concave mirror की f sign क्या है?|Negative|Positive|Zero हमेशा|कोई sign नहीं|Incident-light direction positive रखने पर concave focus object side में negative है।
Convex mirror finite object की image कैसी है?|Virtual erect diminished|Real inverted enlarged|Real erect same size|Virtual inverted|Convex mirror reflected rays diverge करता है; extensions behind mirror मिलती हैं।
Mirror magnification formula कौन है?|−v/u|v/u|u/v|f/u|Mirror geometry और Cartesian convention से m=−v/u मिलता है।
Lens magnification formula कौन है?|v/u|−v/u|−u/v|f/v|Thin lens के लिए m=v/u है; mirror वाला minus न लगाएँ।
Convex lens की f sign क्या है?|Positive|Negative|Zero|हमेशा undefined|Converging convex lens का far-side principal focus positive है।
Lens power की unit क्या है?|Dioptre|Ohm|Ampere|Joule|P=1/f metre में होने से unit m⁻¹ यानी dioptre है।
f = +50 cm lens की power क्या है?|+2 D|+0.02 D|−2 D|+50 D|50 cm=0.5 m, reciprocal +2 D है।
Vacuum से medium का refractive index क्या है?|c/v|v/c|c+v|c−v|Absolute refractive index vacuum speed divided by medium speed है।
Denser medium में oblique ray सामान्यतः कैसे bends करती है?|Normal की ओर|Normal से दूर|हमेशा वापस|कभी speed नहीं बदलती|Higher index में speed कम होती है और oblique ray normal की ओर मुड़ती है।
Concave mirror में object C पर हो तो image कहाँ है?|C पर|F पर|P पर|Behind mirror F पर|C case में image real inverted और same size C पर बनती है।
Paraxial spherical mirror के R और f का संबंध क्या है?|R = 2f|R = f/2|R = f|R = 4f|Spherical mirror का principal focal length radius का आधा है।
Negative magnification का अर्थ क्या है?|Inverted image|Erect image|हमेशा virtual|हमेशा enlarged|m<0 image height का object से opposite sign दर्शाता है।
Concave lens finite real object की image कैसी है?|Virtual erect diminished|Real inverted enlarged|Real same size|Virtual inverted|Diverging lens object side focus और center के बीच virtual image देता है।
Normal incidence पर refraction में direction क्या कर सकती है?|Unchanged रह सकती है|हमेशा 90° घूमती है|हमेशा वापस आती है|Medium speed बराबर जरूरी|Normal incidence पर ray straight चलती है, भले speed बदले।''',
'- Mirror और lens equations अलग हैं।\n- Power में f metre में लें।\n- Angle normal से मापें।\n- Virtual image की backward extensions dashed रखें।\n- v/m के signs के साथ ray-case मिलाएँ।',
'Thin convex lens ray diagram: object 2F से परे; image F और 2F के बीच real, inverted और छोटी। दूरी schematic है।',
['Convex lens', 'Object beyond 2F', 'Parallel ray via F', 'Ray through center', 'Image between F and 2F'],
'अगले अध्याय में lens और refraction का उपयोग human eye और colour phenomena में करेंगे।')

chapter(10, 'मानव नेत्र तथा रंगबिरंगा संसार', 'The Human Eye and the Colourful World', 4,
'Eye optics, accommodation और vision defects; prism dispersion, atmospheric refraction और scattering के कारण समझना।',
'''Cornea|Eye का transparent front surface; refraction का बड़ा भाग यहाँ।
Iris|Pupil size नियंत्रित करने वाला coloured diaphragm।
Pupil|Light के प्रवेश का opening; iris से नियंत्रित।
Retina|Light-sensitive layer जहाँ optical image बनती है।
Accommodation|Ciliary muscles द्वारा lens curvature/focal length बदलना।
Myopia|Distant objects स्पष्ट नहीं; image retina के आगे बनती है।
Hypermetropia|Near objects स्पष्ट नहीं; image retina के पीछे बनने की प्रवृत्ति।
Presbyopia|Age-related accommodation decrease से near vision कठिन।
Dispersion|White light का constituent colours में separation।
Scattering|Particles द्वारा light को विभिन्न दिशाओं में भेजना।''',
'''### Eye एक adjustable optical system
Cornea और lens light refract करके retina पर real, inverted image बनाते हैं। Optic nerve signals brain तक ले जाती है। Iris pupil का aperture नियंत्रित करता है, lens की focal length नहीं। Ciliary muscles lens curvature बदलते हैं। Near object पर lens अधिक convex होकर focal length घटाता है; distant object पर flatter होकर बढ़ाता है। Typical normal near point लगभग 25 cm और far point infinity school model में माना जाता है; यह हर व्यक्ति की exact measurement नहीं।

### Defects और correction
Myopia में distant-object image retina के आगे focus होती है; concave lens rays diverge कर corrected focusing में मदद करता है। Hypermetropia में near-object image retina के पीछे बनने की tendency है; convex lens convergence बढ़ाता है। Presbyopia में aging से accommodation घटती है; correction individual need के अनुसार होती है और combined defects में bifocal/progressive lenses useful हो सकते हैं। Cataract lens clouding है, केवल focal defect नहीं; clinical treatment अलग है।

### Prism और atmosphere
Glass prism different wavelengths को अलग refractive index से refract करता है; violet का deviation red से अधिक होता है। White light separation dispersion, लेकिन single-colour beam का bending refraction है। Rainbow में droplets का refraction, dispersion और internal reflection योगदान करते हैं। Atmosphere की changing optical density stars की apparent brightness/position fluctuation देती है। Planets extended apparent sources होने से scintillation काफी average out करते हैं। Atmospheric refraction sun को geometric sunrise से कुछ पहले visible बना सकती है।

### Sky blue क्यों?
Small-particle/molecular scattering short wavelengths के लिए अधिक है। Blue wavelengths red से अधिक scattered होती हैं; spectral distribution और eye response के साथ sky blue दिखाई देता है, केवल ‘violet नहीं मौजूद’ कारण नहीं। Larger colloidal particles के path-visible scattering को Tyndall effect कहते हैं। Red light relatively कम scattered होती है, इसलिए warning signals में useful है। Moon जैसे atmosphere-रहित स्थान पर sky dark दिखता है।''',
'''Myopic eye का far point 2 m है। Correction power का school-model estimate दें।|Distant object u=−∞ की virtual image far point v=−2 m पर चाहिए। Lens equation 1/f=1/v−1/u≈−1/2, f=−2 m और P=−0.5 D। Prescription की वास्तविक जाँच clinician करता है।
Near object देखते समय ciliary muscles और lens कैसे बदलते हैं?|Ciliary muscles contract, lens अधिक convex/thicker हो सकता है, focal length घटती और power बढ़ती है। इससे पास के object की rays retina पर focus हो पाती हैं।
Prism में red और violet का relative deviation दें।|Normal glass prism में violet wavelength के लिए refractive index अधिक, इसलिए deviation अधिक है। Red का deviation सबसे कम होता है। यह dispersion का school-level pattern है।''',
'''Iris और ciliary muscles की भूमिकाएँ अलग करें।|Iris pupil opening बदलकर light entry नियंत्रित करता है। Ciliary muscles lens curvature बदलकर accommodation करते हैं। इसलिए brightness control और near/far focusing एक ही mechanism नहीं।
Myopia का cause और correction दें।|Eyeball लंबा या optical power अधिक होने पर दूर object की image retina से पहले focus हो सकती है। Concave lens divergence देकर focus retina की ओर adjust करता है। Image retina के पीछे लिखना hypermetropia से मिश्रण होगा।
Hypermetropia का cause और correction दें।|Eyeball छोटा या optical power कम होने पर near object की image retina के पीछे बनने की प्रवृत्ति होती है। Convex lens अतिरिक्त convergence देता है। Optical correction defect के measurement पर निर्भर है।
Presbyopia और cataract का अंतर दें।|Presbyopia age-related accommodation loss है, जिससे near focusing कठिन होती है। Cataract lens clouding है, जिससे transmission और clarity प्रभावित होती है। दोनों aging से जुड़े हो सकते हैं, लेकिन cause और treatment समान नहीं।
Stars twinkle और planets कम क्यों करते हैं?|Stars point-like sources हैं; changing atmosphere से intensity/position fluctuation स्पष्ट दिखती है। Planets का apparent disk extended होता है; अनेक points के fluctuations average होकर कम twinkling दिखाते हैं। दूरी अकेला पूर्ण कारण नहीं।
Blue sky और Tyndall effect का संबंध और अंतर दें।|दोनों scattering से जुड़े हैं। Clear sky मुख्यतः molecules/small particles द्वारा short wavelengths के अधिक scattering से blue दिखता है। Tyndall effect colloidal/larger particles में beam path visible होने का उदाहरण है।''',
'''Eye light path और retina image बताएँ।|1. Light cornea, pupil और lens से होकर अंदर जाती है। 2. Cornea/lens refraction retina पर real inverted optical image देता है। 3. Retinal cells signals बनाती हैं; optic nerve brain तक ले जाती है। Retina को convex lens न कहें।
Myopia/hypermetropia का diagram कैसे अलग बनाएँ?|1. Uncorrected myopia focus retina के आगे। 2. Hypermetropia near-object focus पीछे। 3. Correction क्रमशः concave और convex external lenses से show करें; outgoing rays corrected case में retina पर meet हों। Labels में defect और lens दोनों दें।
Prism dispersion के तीन बिंदु दें।|1. White light में अनेक wavelengths हैं। 2. Glass का refractive index wavelength-dependent है। 3. Violet अधिक और red कम deviate होकर spectrum बनाते हैं। Prism colours ‘बनाता’ नहीं, existing components अलग करता है।
Atmospheric refraction के दो examples और mechanism दें।|1. Star apparent position बदल सकती है। 2. Sun geometric horizon के नीचे होने पर भी कुछ समय visible हो सकता है। 3. Atmosphere का refractive index altitude/conditions से बदलता है, जिससे light path bends करता है। यह reflection नहीं।''',
'''Normal near vision, myopia और hypermetropia को image location और correction से तुलना करें।|1. Normal accommodated eye near object का focus retina पर रखती है। 2. Myopic eye में distant rays retina से पहले focus हो सकती हैं; concave lens उपयोगी। 3. Hypermetropic eye में near-object focus retina के पीछे की tendency; convex lens useful। 4. Diagrams में retina position स्थिर रखें और ray intersections सही स्थान दिखाएँ।
Sky colour, red warning signal और stars twinkling का कारण अलग-अलग समझाएँ।|1. Short wavelengths का अधिक scattering blue sky में योगदान देता है। 2. Red wavelength का comparatively कम scattering warning visibility में मदद करता है। 3. Star twinkling atmospheric refractive-index fluctuations से है। 4. पहली दो scattering हैं, तीसरी refraction-related है; सभी को prism dispersion कहना गलत होगा।''',
'''Eye की light-sensitive layer कौन है?|Retina|Iris|Cornea ही|Pupil|Retina में light-sensitive cells visual signals बनाती हैं।
Pupil size कौन नियंत्रित करता है?|Iris|Retina|Optic nerve ही|Tear gland|Iris aperture बदलकर pupil size नियंत्रित करता है।
Accommodation मुख्यतः किससे होती है?|Lens curvature change|Retina की daily growth|Eye colour change|Pupil का lens बनना|Ciliary muscles lens curvature बदलकर focal length adjust करते हैं।
Near object के लिए lens focal length सामान्यतः क्या करती है?|घटती है|बढ़ती है|हमेशा infinity|शून्य ही|Lens अधिक convex होने से focal length घटती और power बढ़ती है।
Myopia correction का lens कौन है?|Concave|Convex|Plane glass ही|Prism ही|Concave lens rays diverge करके premature focusing सुधारता है।
Hypermetropia correction का lens कौन है?|Convex|Concave|Plane mirror|Opaque glass|Convex lens convergence बढ़ाता है और near focusing में मदद करता है।
School model में normal near point लगभग कितना है?|25 cm|25 m|2.5 mm|Infinity|Typical near point लगभग 25 cm लिया जाता है; individual variation होती है।
Prism में least deviation colour कौन है?|Red|Violet|Blue|Indigo|Ordinary glass prism में red light least deviate करती है।
White light का colour separation क्या है?|Dispersion|केवल reflection|Neutralisation|Conduction|Wavelength-dependent refraction components अलग करती है।
Clear sky blue होने का मुख्य phenomenon क्या है?|Scattering|केवल total reflection|Nuclear fusion|Magnetism|Short visible wavelengths अधिक scattered होती हैं।
Colloid में beam path दिखने का नाम क्या है?|Tyndall effect|Joule effect|Ohm law|Mendel law|Particles की scattering से beam path visible हो सकता है।
Star twinkling मुख्यतः किससे जुड़ा है?|Atmospheric refraction fluctuations|Star का रोज बुझना|Moon reflection ही|Glass lens defect|Changing atmosphere star light के apparent intensity/position को बदलता है।
Presbyopia मुख्यतः क्या है?|Age-related accommodation decrease|Pupil का रंग लाल|हर बार infection|Retina आगे बढ़ना|Aging में lens elasticity/muscle-related accommodation घट सकती है।
Cataract क्या है?|Lens clouding|केवल myopia|केवल colour blindness|Pupil widening|Cataract transparency का defect है, simple focusing error मात्र नहीं।
Retina पर optical image कैसी होती है?|Real inverted|Virtual erect|Virtual inverted हमेशा|Real erect|Eye optics real inverted image retina पर बनाते हैं; brain signals interpret करता है।''',
'- Myopia concave, hypermetropia convex।\n- Iris और ciliary muscle के काम अलग।\n- Twinkling refraction, sky colour scattering।\n- Cataract को presbyopia न कहें।\n- 25 cm typical model है, सभी लोगों का fixed near point नहीं।',
'Eye optics का simplified route; accommodation और pupil control अलग mechanisms हैं।',
['Cornea', 'Pupil / iris', 'Adjustable lens', 'Retina image', 'Optic nerve signals'],
'अगले अध्याय में current, potential difference और electric energy की गणना करेंगे।')

chapter(11, 'विद्युत', 'Electricity', 7,
'Current/voltage/resistance की units; circuit combinations, Ohm law और heating; power एवं commercial energy numericals हल करना।',
'''Current|I = Q/t; unit ampere (A), 1 A = 1 C/s।
Potential difference|V = W/Q; unit volt (V), 1 V = 1 J/C।
Resistance|R = V/I; unit ohm (Ω)।
Ohm law|Fixed physical conditions में V = IR।
Resistivity|ρ = RA/l; material property, unit Ω·m।
Series resistance|Rₛ = R₁ + R₂ + …।
Parallel resistance|1/Rₚ = 1/R₁ + 1/R₂ + …।
Joule heating|H = I²Rt; current ampere, resistance ohm, time second।
Power|P = VI = I²R = V²/R; unit watt।
Commercial energy|1 kWh = 3.6 × 10⁶ J; kWh ऊर्जा है, power नहीं।''',
'''### Charge से current तक
Potential difference charges को move करने का driving condition देता है; current charge-flow rate है। Conventional current positive-charge flow की direction है; metals में electrons उसके opposite drift करते हैं। Ammeter series में, voltmeter measured component के parallel में लगता है। Open circuit में steady current नहीं flows करता। Potential difference होने से बिना closed conductive path current हमेशा flows करेगा, ऐसा नहीं।

### Ohm और material
Ohm law fixed temperature और physical conditions पर V proportional I बताता है। $V=IR$; V–I graph में V vertical हो तो slope R है, I vertical हो तो slope 1/R। Wire resistance $R=\\rho l/A$; length double हो और area constant तो R double। Area double हो तो half। Resistivity material तथा temperature से जुड़ी है; ordinary geometry बदलने से resistivity नहीं बदलती।

### Series और parallel
Series में current same, voltage drops add: Rₛ=R₁+R₂। Parallel में branch voltage same, currents add और reciprocal resistances add। Positive finite resistors का parallel equivalent smallest branch resistance से भी कम है। Household appliances parallel में लगते हैं ताकि rated voltage मिले और independently switch हो सकें। एक wire short circuit unintended low-resistance path बनाकर बहुत current दे सकता है।

### Heat, power और bill
Resistor heating $H=I^2Rt$ है। Power energy per time है: $P=VI$ तथा ohmic resistor के लिए $I^2R$ और $V^2/R$। Fixed current में larger R अधिक heat, fixed voltage में larger R कम power देता है; held-constant quantity पहचानें। Appliance bill energy kW × hours से निकलेगा। 1000 W=1 kW; 1 kWh=1000 J/s ×3600 s=3.6×10⁶ J। Electrical safety devices और household wiring अगले अध्याय में आएँगे; mains पर छात्र प्रयोग न करें।''',
'''2 Ω और 3 Ω resistors को 6 V पर series में लगाएँ। I और drops निकालें।|R=2+3=5 Ω। I=6/5=1.2 A। V₁=1.2×2=2.4 V, V₂=1.2×3=3.6 V। Sum 6 V; series current दोनों में 1.2 A है।
6 Ω और 3 Ω parallel में 6 V पर हैं। R और total current दें।|1/R=1/6+1/3=1/2, R=2 Ω। Branch currents 1 A और 2 A; total=3 A। जाँच V/R=6/2=3 A।
100 W lamp रोज 5 hours, 30 days चले तो energy और ₹6/unit पर cost दें।|P=0.1 kW, t=150 h। E=15 kWh अर्थात 15 units। Energy charge=15×₹6=₹90; fixed charges/taxes इस illustrative calculation में शामिल नहीं।''',
'''Current और potential difference की तुलना करें।|Current charge प्रति time, I=Q/t और unit ampere है। Potential difference energy/work प्रति charge, V=W/Q और unit volt है। दोनों related हैं पर समान quantity नहीं; 1 A को 1 J/C नहीं लिखें।
Ammeter series और voltmeter parallel क्यों लगाते हैं?|Ammeter branch current मापने के लिए उसी current path में रहता है और ideal resistance low है। Voltmeter दो terminals का potential difference मापता है तथा ideal resistance high है। Ammeter को source के across सीधे जोड़ना unsafe है।
Resistance और resistivity अलग कैसे हैं?|Resistance किसी conductor के geometry तथा material पर निर्भर R=ρl/A है। Resistivity material/temperature property है। Same material का longer wire larger R रखता है, लेकिन same temperature पर उसकी ρ length के कारण नहीं बदलती।
Series और parallel में voltage/current की तुलना दें।|Series में current समान और voltage drops का sum source voltage है। Parallel में प्रत्येक branch पर voltage समान और branch currents का sum total है। दोनों rules interchange करने पर equivalent resistance तथा numericals गलत होंगे।
Fuse में heating का उपयोग कैसे है?|Excess current से fuse element I²Rt heating के कारण melt होकर circuit खोल सकता है। Element rating, material और construction उपयुक्त होनी चाहिए। Fuse को मोटे साधारण wire से बदलना protection समाप्त कर सकता है।
kW और kWh का अंतर क्या है?|kW power की unit, energy-use rate है। kWh energy की unit, 1 kW power के 1 hour में उपयोग की energy है। Electricity bill units kWh हैं; ‘kilowatt प्रति hour’ इसका समान अर्थ नहीं।''',
'''Ohm law experiment के तीन measurement steps दें।|1. Low-voltage source, resistor और ammeter series; voltmeter resistor के parallel लगाएँ। 2. Voltage बदलकर V,I pairs लें, temperature लगभग constant रखें। 3. V/I लगभग constant हो तो ohmic behaviour है। Graph axes देखकर slope पहचानें।
Series equivalent resistance derive करें।|1. हर resistor में same I होता है। 2. V=V₁+V₂=IR₁+IR₂। 3. V=IRₛ से Rₛ=R₁+R₂। Derivation positive fixed resistors के सामान्य series circuit पर लागू है।
Parallel equivalent resistance derive करें।|1. हर branch पर same V है। 2. I=I₁+I₂=V/R₁+V/R₂। 3. I=V/Rₚ से 1/Rₚ=1/R₁+1/R₂। Equivalent smallest branch resistance से कम होना qualitative check है।
Electrical power और energy के formulas जोड़ें।|1. W=VQ और Q=It से energy W=VIt। 2. P=W/t=VI। 3. Ohmic relation लगाने पर P=I²R=V²/R; energy E=Pt। Formula में variable W को watt unit के साथ confusion से बचाएँ।''',
'''220 V पर 1100 W heater के current, resistance और 2 h energy निकालें।|1. I=P/V=1100/220=5 A। 2. R=V²/P=48400/1100=44 Ω। 3. E=1.1 kW×2 h=2.2 kWh। 4. Joules में E=2.2×3.6×10⁶=7.92×10⁶ J। Rated values steady ideal calculation के लिए हैं।
2 Ω और 4 Ω को 12 V पर series तथा parallel में तुलना करें।|1. Series R=6 Ω और I=2 A। 2. Drops 4 V और 8 V। 3. Parallel R=(2×4)/(2+4)=4/3 Ω। 4. Branch currents 6 A और 3 A, total 9 A। Same voltage पर parallel total current अधिक है; voltage को resistance से बिना circuit पहचान divide न करें।''',
'''Current की SI unit क्या है?|Ampere|Volt|Ohm|Watt|Current charge प्रति second है और SI unit ampere है।
Potential difference का formula कौन है?|W/Q|Q/t|I/t|R/A|Volt work/energy प्रति charge का माप है।
Ohm law किन conditions में लागू है?|Temperature/physical conditions स्थिर|हर device हर दशा में|केवल open circuit|Resistance शून्य हो|Ohmic proportionality physical conditions स्थिर होने पर लागू है।
Ammeter circuit में कहाँ लगता है?|Series|Parallel across source सीधे|केवल earth|बिना wire|Ammeter मापी जाने वाली branch का current carry करता है।
Voltmeter component के कैसे लगता है?|Parallel|Series हमेशा|केवल neutral|बिना terminals|Potential difference component के दो terminals के across मापा जाता है।
Same material wire की length double, area same: R क्या होगा?|Double|Half|Unchanged|Four times|R=ρl/A से length double करने पर R double है।
Resistivity की SI unit क्या है?|Ω·m|Ω/m|A/m|V·s|ρ=RA/l से ohm × square metre / metre = Ω·m।
2 Ω तथा 3 Ω series equivalent क्या है?|5 Ω|1.2 Ω|6 Ω|0.5 Ω|Series resistances add होकर 5 Ω होते हैं।
6 Ω तथा 3 Ω parallel equivalent क्या है?|2 Ω|9 Ω|3 Ω|6 Ω|1/R=1/6+1/3=1/2, इसलिए R=2 Ω।
Joule heat formula कौन है?|I²Rt|IR/t|V/t|R²It|Resistive heat current square, resistance और time के proportional है।
1 kWh कितने joules हैं?|3.6×10⁶ J|3600 J|1000 J|3.6×10⁵ J|1000 W ×3600 s=3,600,000 J।
220 V, 1100 W heater का current क्या है?|5 A|0.2 A|242 A|1100 A|P=VI से I=P/V=1100/220=5 A। Watt को volt से भाग देने पर ampere मिलता है।
House appliances सामान्यतः किस combination में हैं?|Parallel|Series ही|कोई circuit नहीं|केवल short circuit|Parallel में same supply voltage और independent operation मिलता है।
V vertical, I horizontal graph का slope क्या है?|Resistance|Conductance|Power|Charge|Slope ΔV/ΔI=R ohmic resistor के लिए है।
Fixed voltage पर R double होने पर P क्या होगा?|Half|Double|Four times|Unchanged|P=V²/R में V स्थिर हो तो resistance double से power half है।''',
'- kWh energy है, power नहीं।\n- Graph axes देखे बिना slope R न लिखें।\n- Parallel में voltage same; series में current same।\n- ρ और R की units अलग हैं।\n- Fixed V या fixed I पहचानकर heating की तुलना करें।',
'Low-voltage resistor experiment: ammeter series और voltmeter resistor के parallel में।',
['Low-voltage source', 'Ammeter in series', 'Resistor', 'Voltmeter across R', 'Closed return path'],
'अगले अध्याय में current से magnetic field और household protection आएँगे।')

chapter(12, 'विद्युत धारा के चुंबकीय प्रभाव', 'Magnetic Effects of Electric Current', 6,
'Field direction, right-hand rule और solenoid समझना; current-carrying conductor पर force; domestic wiring में earth/fuse/parallel connections की भूमिका।',
'''Magnetic field|वह क्षेत्र जहाँ magnetic influence अनुभव होता है।
Field line|Local tangent से field direction दर्शाने वाली कल्पित रेखा।
Right-hand thumb rule|Thumb current direction, curled fingers field direction।
Circular loop|Circular conductor में current से magnetic field बनता है।
Solenoid|Many closely wound turns वाला लंबा coil।
Electromagnet|Current-driven coil तथा suitable core से बनने वाला magnet।
Fleming left-hand rule|Forefinger field, middle finger current, thumb force/motion।
Live wire|Supply का hazardous potential वाला conductor।
Earth wire|Exposed metal body के लिए protective low-resistance fault path।
Overloading|Circuit rating से अधिक total current demand।''',
'''### Field का चित्र
Compass field direction बताता है। Magnet के बाहर field lines N से S और अंदर S से N होकर closed loops होती हैं। Lines पास हों तो field comparatively strong। Two lines intersect नहीं करतीं, क्योंकि एक point पर field की direction unique है। Lines वास्तविक strings नहीं; drawing field representation है।

### Current से field
Straight current-carrying wire के आसपास concentric circles हैं। Right-hand thumb current की दिशा, fingers field की। Current reverse करने पर field reverse होता है; current बढ़ाने पर field बढ़ता, distance बढ़ाने पर घटता है। Circular loop में near-wire curved lines और center पर roughly axis-directed field होता है। Coil turns बढ़ाना field मजबूत कर सकता है। Solenoid के अंदर away from ends field लगभग uniform और outside pattern bar magnet जैसा है। Soft iron core suitable electromagnet को stronger बनाता है।

### Field में current-carrying wire पर force
Magnetic field में current-carrying conductor पर force direction field और current पर निर्भर है। Fleming left-hand rule में first finger B, middle finger I, thumb force है। Current या field अकेला reverse हो तो force reverse; दोनों reverse हों तो force direction same रह सकती है। Force perpendicular configuration में maximum, parallel में zero school model में है। Right-hand thumb rule field-from-current देता है; left-hand rule force direction देता है।

### घरेलू circuit
Appliances live–neutral के across parallel branches में लगे होते हैं। भारत की सामान्य single-phase घरेलू आपूर्ति का nominal voltage 230 V और frequency 50 Hz है ([BIS](https://www.bis.gov.in/wp-content/uploads/2023/08/Plugs-and-Sockets-20.pdf)); कुछ school numericals में 220 V दिया जाता है, इसलिए सवाल में दी गई supply लें। Switch/fuse live conductor में रखना isolation में मदद करता है; neutral को ‘हर समय safe’ न मानें। Earth exposed metal casing से protective fault path देता है जिससे suitable protection trip हो सकती है। Fuse/MCB excessive current protection देते हैं; leakage protection अलग device function है। Damaged insulation से short circuit, अधिक load से overloading हो सकती है। 2026–27 regular syllabus में motor, electromagnetic induction और generator अलग explicit topics नहीं हैं; उन्हें यहाँ board-core के रूप में नहीं जोड़ा गया।''',
'''Wire में current page से बाहर आ रहा है। Field direction बताइए।|Right-hand thumb observer की ओर रखें; curled fingers anticlockwise हैं। इसलिए बाहर आते current के चारों ओर field anticlockwise; अंदर जाते current के लिए clockwise है।
Field right और conventional current up हो तो force कहाँ होगी?|Fleming left-hand rule अथवा I×B दिशा से force page के भीतर है। Diagram symbols × into page और • out of page स्पष्ट रखें। Current down करने से force बाहर होगी।
220 V पर 2 kW और 1 kW appliances साथ चलें तो total current estimate दें।|Total P=3000 W। Ideal rated estimate I=P/V=3000/220≈13.64 A। 5 A-rated circuit के लिए यह load बहुत अधिक है; calculation protection को bypass करने का निर्देश नहीं।''',
'''Field lines intersect क्यों नहीं करतीं?|Intersection पर एक point में दो tangents और दो field directions बन जाएँगी। Magnetic field की local direction unique होती है। इसलिए field-line representation में crossing स्वीकार्य नहीं।
Straight wire में current reverse करने का effect दें।|Magnetic field circulation reverse हो जाता है। Right-hand thumb opposite direction में रखने पर curled fingers भी उलटे घूमते हैं। Current magnitude same हो तो comparable position पर strength का magnitude समान हो सकता है।
Solenoid को bar magnet जैसा क्यों कहते हैं?|Solenoid का outside field pattern north/south poles वाला bar magnet जैसा है। Interior में many turns का combined field approximately uniform होता है। Current reverse करने पर poles swap हो जाते हैं।
Right-hand thumb और left-hand rules अलग कैसे हैं?|Right-hand thumb rule straight current के magnetic field की direction देता है। Fleming left-hand rule field में current-carrying conductor पर force की direction देता है। Thumb की भूमिका दोनों में अलग है; नाम के आधार पर arrows interchange न करें।
Earth wire की आवश्यकता क्या है?|Metal casing fault से live हो जाए तो earth low-resistance protective path देता है। Suitable fuse/MCB/RCD arrangement fault को disconnect करने में मदद कर सकता है। Earth सामान्य appliance operating-current return path नहीं; neutral से अलग function है।
Short circuit और overload में अंतर दें।|Short circuit unintended very low-resistance connection से current अचानक बढ़ना है। Overload अनेक/high-power loads से rated current exceed करना है। दोनों heating risk बढ़ाते हैं, लेकिन causes अलग हैं।''',
'''Magnetic field lines की तीन properties दें।|1. Outside magnet N→S और अंदर S→N closed loops। 2. Tangent local field direction देता है। 3. Close spacing stronger field दर्शाती है और lines intersect नहीं करतीं। Pole के पास line density comparatively अधिक हो सकती है।
Electromagnet की strength कैसे बदल सकती है?|1. Coil current बढ़ने पर field बढ़ सकता है। 2. Turns बढ़ाने से combined field मजबूत हो सकता है। 3. Suitable soft-iron core flux बढ़ा सकता है। Heating और device limits के कारण unlimited current उचित नहीं।
Force direction में reversals का प्रभाव दें।|1. Current alone reverse करने पर force reverse। 2. Field alone reverse करने पर भी force reverse। 3. दोनों reverse करने पर force direction same; current parallel B हो तो ideal magnetic force zero। Left-hand rule से check करें।
Domestic parallel wiring का schematic समझाएँ।|1. Each appliance live–neutral के across branch में हो। 2. Each branch switch live side पर दिखाएँ। 3. Exposed casing को earth से जोड़ें और suitable protection supply side पर दिखाएँ। Earth को heating element के series return की तरह न draw करें।''',
'''एक metal-cased appliance में live wire casing छूती है। Fault, earth path तथा protection समझाएँ।|1. Insulation failure casing पर dangerous potential ला सकता है। 2. Protective earth low-resistance path देकर fault current route उपलब्ध करती है। 3. Correctly rated protection supply disconnect कर सकती है; leakage devices का function अलग है। 4. Appliance उपयोग रोककर qualified electrician से repair चाहिए; earth wire निकालना समाधान नहीं।
Straight wire और solenoid के field diagrams की तुलना करें।|1. Straight wire cross-section पर concentric circles तथा current •/× दिखाएँ। 2. Right-hand rule से circulation arrows लगाएँ। 3. Solenoid में inside लगभग parallel field lines और outside return loops draw करें। 4. Current reverse करने पर solenoid poles तथा wire circulation बदलते हैं। दोनों current-generated fields हैं, geometry अलग है।''',
'''Magnet के बाहर field lines किस दिशा में हैं?|N से S|S से N|हमेशा ऊपर|हमेशा नीचे|External field direction north pole से south pole है; अंदर return path होता है।
Field-line tangent क्या बताता है?|Local field direction|केवल temperature|केवल charge mass|केवल voltage|किसी point पर tangent magnetic field direction दर्शाता है।
Field lines intersect क्यों नहीं करतीं?|एक point पर field direction unique है|Lines metal की हैं|Field शून्य ही है|Compass नहीं चलता|Crossing दो directions imply करेगी, जो representation से असंगत है।
Right-hand thumb क्या दिखाता है?|Current direction|Force ही|Voltage|Resistance|Thumb current direction और fingers circular magnetic field direction देती हैं।
Page से बाहर current का field circulation क्या है?|Anticlockwise|Clockwise|Straight ऊपर|कोई field नहीं|Right-hand thumb observer की ओर रखने पर fingers anticlockwise curl करती हैं।
Straight wire से distance बढ़ने पर field सामान्यतः कैसा होता है?|कमजोर|मजबूत|Unchanged हमेशा|हमेशा zero|Same current में wire से दूर field strength घटती है।
Solenoid interior away from ends field कैसा है?|लगभग uniform|हर जगह zero|केवल random|केवल electric|Many turns interior में nearly parallel field देते हैं।
Electromagnet में common suitable core कौन है?|Soft iron|Wood|Plastic|Glass|Soft iron magnetic field को मजबूत करने में उपयोगी है।
Fleming left-hand middle finger क्या देती है?|Current|Field|Force|Earth direction|First finger field, middle current और thumb force है।
Current और B parallel हों तो force का ideal value क्या है?|Zero|Maximum|हमेशा upward|हमेशा 1 N|Magnetic force direction factor parallel orientation में zero होता है।
Earth wire का primary function क्या है?|Protective fault path|Normal neutral return ही|Current बढ़ाकर bill बनाना|Voltage double करना|Earth exposed metal casing से fault current का protective route देती है।
Household appliance connection सामान्यतः क्या है?|Parallel|Series|केवल coil|केवल open|Parallel branches में समान supply voltage और independent control मिलता है।
Unintended low-resistance live-neutral path क्या है?|Short circuit|Normal loading|Photosynthesis|Refraction|Short circuit से बहुत current तथा heating risk हो सकते हैं।
Rated current से अधिक demand क्या कहलाती है?|Overloading|Earthing|Polarisation|Dispersion|Overloading circuit capacity से अधिक current demand है।
School model domestic AC frequency क्या है?|50 Hz|5 Hz|5000 Hz|0 Hz|भारत की सामान्य domestic AC supply के लिए 50 Hz school value है।''',
'- Right-hand thumb और Fleming left-hand न मिलाएँ।\n- • बाहर, × भीतर है।\n- Field lines closed loops हैं।\n- Earth और neutral अलग functions हैं।\n- Mains wiring के diagrams learning के लिए हैं, स्वयं repair के लिए नहीं।',
'Current से field और field में conductor force का functional schematic; दोनों नियमों का कार्य अलग है।',
['Current in wire', 'Right-hand: field', 'Coil / solenoid', 'Conductor in field', 'Left-hand: force'],
'अंतिम अध्याय में energy flow और human environmental impact को जोड़ेंगे।',
'2025, प्रश्न 1(xi), PDF पृष्ठ 5: right-hand thumb rule में thumb। उत्तर-संकेत: current direction।')

chapter(13, 'हमारा पर्यावरण', 'Our Environment', 5,
'Ecosystem components और food webs; trophic energy transfer तथा biomagnification; ozone depletion और waste-management choices समझना।',
'''Ecosystem|Organisms और physical environment का interacting system।
Biotic component|Living organisms जैसे plants, animals और microbes।
Abiotic component|Nonliving conditions जैसे light, water, temperature।
Producer|Organic food बनाने वाला organism; green plants सामान्य उदाहरण।
Consumer|दूसरे organisms/organic material से food लेने वाला organism।
Decomposer|Dead matter breakdown करने वाले bacteria/fungi आदि।
Trophic level|Food chain में feeding position।
10% model|अगले trophic level को लगभग 10% energy transfer का school approximation।
Biomagnification|Persistent pollutants की higher trophic levels पर concentration बढ़ना।
Ozone|O₃; stratospheric layer harmful UV का कुछ भाग absorb करती है।''',
'''### Ecosystem में संबंध
Pond, forest या garden में organisms light, soil, water और temperature से interact करते हैं। Plants producers; herbivores primary consumers; predators secondary/higher consumers हो सकते हैं। Decomposers dead matter से nutrients recycle करते हैं और सभी trophic levels से जुड़े रहते हैं; उन्हें केवल ‘last animal’ न दिखाएँ। Artificial aquarium भी ecosystem है, लेकिन external maintenance की जरूरत हो सकती है।

### Food chain और energy
Food-chain arrows food/energy transfer source से recipient की ओर हैं: grass → grasshopper → frog → snake। Food web multiple interconnected chains है। Solar energy producers capture करते हैं; energy respiration/heat और activities में जाती है। लगभग 10% next level available energy का school model है, exact universal law नहीं। Energy flow one-way है; nutrients cycle कर सकते हैं। इसलिए ‘energy decomposers से sun को लौटती है’ गलत है।

### Pollutant और ozone
कुछ persistent, poorly metabolised chemicals organisms में accumulate हो सकते हैं। Higher consumers कई contaminated organisms खाते हैं, इसलिए concentration बढ़ सकती है: biomagnification। यह energy amplification नहीं। Stratosphere का ozone useful UV shielding देता है; ground-level ozone harmful pollutant हो सकता है। UV oxygen molecules तोड़ सकती है और O atoms O₂ से O₃ बनाते हैं। CFC-related chlorine chemistry stratospheric ozone depletion में भूमिका निभाती है। Ozone depletion और greenhouse warming अलग mechanisms हैं, भले कुछ substances दोनों से संबंधित हों।

### Waste का जिम्मेदार प्रबंधन
Biodegradable matter microorganisms द्वारा suitable conditions में breakdown हो सकता है; सभी biodegradable waste तुरन्त disappear या harmless नहीं। Plastic/glass जैसे non-biodegradable materials लंबे समय रह सकते हैं। Reduce, reuse, recycle तथा source segregation useful हैं। Clean wet organic waste composting, clean dry recyclables अलग collection, e-waste authorised handling में जाएँ। Plastic खुले में जलाने से harmful emissions हो सकती हैं। Waste-management choice material और local collection व्यवस्था पर निर्भर है।''',
'''Producer level पर 20,000 J हों तो तीन transfers बाद energy estimate दें।|10% model में primary consumers 2,000 J; secondary 200 J; tertiary 20 J। हर transfer पर previous level ×0.1 करें। 20 J fourth trophic level का estimate है, exact real ecosystem measurement नहीं।
Grass → deer → tiger में trophic levels पहचानें।|Grass producer/level 1; deer primary consumer/level 2; tiger secondary consumer/level 3। Arrow deer की ओर grass energy transfer दिखाता है; predator से prey की ओर arrow उल्टा होगा।
Wet food waste और used batteries का management अलग करें।|Suitable clean organic waste composting में जा सकता है। Batteries hazardous/e-waste collection channel में जाएँ; compost में न मिलाएँ। ‘सब biodegradable bin में’ sorting का सही उत्तर नहीं।''',
'''Biotic और abiotic components उदाहरण सहित दें।|Plants, animals और microbes living biotic components हैं। Water, light, soil conditions तथा temperature abiotic हैं। Ecosystem में दोनों interact करते हैं; केवल animals की list पूरी ecosystem definition नहीं।
Food chain और food web में अंतर करें।|Food chain feeding transfer का एक linear route दिखाती है। Food web multiple interconnected routes दिखाता है, क्योंकि organisms के कई food sources/predators हो सकते हैं। Web वास्तविक feeding complexity को बेहतर दर्शा सकता है।
Decomposers क्यों आवश्यक हैं?|Bacteria/fungi dead organic matter breakdown करके nutrients environment में उपलब्ध कराते हैं। इससे nutrient recycling में मदद मिलती है। Decomposition energy को नए sunlight में बदलना नहीं; energy dissipation जारी रहता है।
10% energy transfer model की सीमा दें।|यह school-level approximate model है, हर ecosystem में exactly 10.000% नहीं। Organism metabolism और ecological conditions transfer efficiency बदलते हैं। गणना में question का दिया assumption लें और result को estimate label करें।
Biomagnification और bioaccumulation में अंतर दें।|Bioaccumulation एक organism में समय के साथ chemical build-up है। Biomagnification food chain के higher levels पर concentration बढ़ना है। दोनों persistent pollutants से जुड़े हो सकते हैं, पर comparison scale अलग है।
Biodegradable का अर्थ harmless क्यों नहीं है?|Organic waste decomposition में oxygen demand, odour या disease-related problems हो सकती हैं। Breakdown conditions तथा समय महत्त्वपूर्ण हैं। इसलिए biodegradable waste भी segregation और उचित treatment माँगता है।''',
'''Energy flow और nutrient cycle की तुलना दें।|1. Solar input से ecosystem energy आती है। 2. Trophic transfer में energy heat के रूप में dissipates होती है; flow unidirectional है। 3. Nutrients decomposition तथा uptake से circulate कर सकते हैं। ‘Energy cycle’ को nutrient cycle जैसा न draw करें।
Ozone formation और protective function लिखें।|1. UV से O₂ टूटकर oxygen atoms बन सकते हैं। 2. O atoms O₂ से मिलकर O₃ देते हैं। 3. Stratospheric ozone harmful UV का कुछ भाग absorb करता है। Near-ground ozone की effects अलग और harmful हो सकती हैं।
Biomagnification food chain में कैसे बढ़ सकती है?|1. Persistent chemical lower levels के tissues में रहता है। 2. Predator अनेक contaminated prey खाता है। 3. Higher level concentration बढ़ सकती है, यदि elimination/metabolism कम हो। इसे सभी biodegradable nutrients पर लागू न करें।
घर के waste segregation के तीन streams दें।|1. Clean biodegradable wet waste compost/appropriate collection में। 2. Clean dry recyclables अलग रखें। 3. Batteries/e-waste तथा hazardous materials authorised channels में दें। Local rules के अनुसार streams adjust करें; mixed burning समाधान नहीं।''',
'''10% model से grass → insect → frog → snake में 50,000 J की energy तथा arrows समझाएँ।|1. Grass level 1 पर 50,000 J। 2. Insect 5,000 J और frog 500 J। 3. Snake 50 J। 4. Arrows grass से insect और आगे transfer recipient की ओर हैं। यह provided approximation की calculation है; प्रत्येक level को पूरा starting energy नहीं मिलता।
Ozone depletion, biomagnification और solid-waste pollution में अंतर और एक-एक निवारण दिशा दें।|1. Ozone depletion stratospheric shielding loss है; ozone-depleting substances को नियंत्रित करना दिशा है। 2. Biomagnification persistent chemical concentration का trophic increase है; ऐसे pollutants का release घटाना जरूरी है। 3. Solid waste accumulation के लिए reduce/reuse/segregation/recycling useful हैं। 4. Problems जुड़े हो सकते हैं लेकिन एक ही mechanism नहीं; plastic recycling अकेले ozone को नहीं सुधारती।''',
'''Ecosystem का abiotic component कौन है?|Temperature|Grass|Frog|Bacterium|Temperature nonliving physical condition है।
Green plants का सामान्य trophic role क्या है?|Producer|Primary consumer|Secondary consumer|केवल decomposer|Plants photosynthesis से organic food बनाकर energy उपलब्ध करते हैं।
Herbivore किस consumer level पर है?|Primary|Secondary|Tertiary हमेशा|Producer|Herbivore producer को खाकर primary consumer होता है।
Food-chain arrow क्या दर्शाता है?|Food/energy transfer|केवल predator का hunting direction|Wind direction|Sex determination|Arrow source organism से खाने वाले recipient की ओर है।
Multiple food chains का interconnected रूप क्या है?|Food web|Reflex arc|Electric circuit|Homologous series|Food web feeding relationships के कई routes जोड़ता है।
20,000 J का 10% कितना है?|2,000 J|200 J|20 J|20,000 J|एक transfer में 20,000×0.1=2,000 J estimated available energy है।
Energy flow की दिशा कैसी है?|Unidirectional|पूर्ण cycle वापस sun में|सभी levels पर equal|केवल reverse|Energy dissipates होकर heat बनती है; nutrients जैसे cycle नहीं करती।
Dead matter breakdown में common organisms कौन हैं?|Bacteria और fungi|केवल tiger|केवल deer|केवल fish|Decomposer microbes nutrient recycling में योगदान देते हैं।
Ozone का molecular formula क्या है?|O₃|O₂|CO₂|N₂|Ozone oxygen का triatomic form है।
Protective ozone layer मुख्यतः कहाँ है?|Stratosphere|केवल ocean bottom|Earth core|केवल tropospheric street|Stratospheric ozone harmful ultraviolet का कुछ भाग absorb करता है।
Ozone depletion से किस exposure का risk बढ़ सकता है?|Ultraviolet|केवल sound|केवल radio|केवल gravity|Ozone shielding कम होने पर harmful UV reach बढ़ सकती है।
Biomagnification में क्या बढ़ता है?|Persistent pollutant concentration|Energy हर level पर|Oxygen हर predator में|सभी genes का आकार|Higher trophic levels में poorly eliminated pollutants की concentration बढ़ सकती है।
Compost के लिए suitable material कौन है?|Clean vegetable peels|Used batteries|Glass shards|Electronic boards|Clean organic waste suitable conditions में compost हो सकता है।
Plastic को खुले में जलाना क्यों अनुचित है?|Harmful emissions हो सकती हैं|हर plastic oxygen बनाता है|सब तुरंत harmless होता है|कोई smoke नहीं होता|Uncontrolled burning harmful gases/particles दे सकता है।
Ozone depletion और global warming समान हैं क्या?|नहीं, mechanisms अलग हैं|हाँ, पूर्ण synonyms|हाँ, दोनों केवल acid rain|हाँ, दोनों केवल litter|Ozone shielding loss और greenhouse energy trapping अलग environmental mechanisms हैं।''',
'- Food arrow energy recipient की ओर है।\n- Energy flow और nutrient cycle अलग हैं।\n- 10% approximation है, exact universal constant नहीं।\n- Ozone depletion और warming समान नहीं।\n- Biodegradable waste को बिना management harmless न कहें।',
'चार trophic levels में 10% model का energy schematic; वास्तविक efficiency बदल सकती है।',
['Producer: 20,000 J', 'Primary: 2,000 J', 'Secondary: 200 J', 'Tertiary: 20 J', 'Energy lost as heat'],
'पूरी पुस्तक दोहराएँ: chemical reactions → biological energy → electricity → ecosystem energy; हर जगह quantities और mechanisms अलग रखें।')

