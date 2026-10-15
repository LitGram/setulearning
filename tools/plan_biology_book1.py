"""Durable figure briefs, bilingual notes and insertion anchors for Biology I."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def plan():
    figures = []

    def add(ch, id, anchor, caption, note, kind='raster', **data):
        figures.append(dict(chapter=f'ch{ch}', id=id, anchor=anchor,
            caption=caption, note=note, kind=kind, **data))

    add(1, 'organisation', '## भाग 4:', 'जीवन का संगठन: कोशिका से जीवमंडल तक',
        'कोशिका → ऊतक → अंग → अंग तंत्र → जीव → जनसंख्या → समुदाय → पारितंत्र → जीवमंडल। ऊतक और अंग वाले चरण बहुकोशिकीय जीवों पर लागू होते हैं। समुदाय में अनेक प्रजातियां होती हैं; पारितंत्र में उनका अजैव पर्यावरण भी शामिल है।',
        'flow', title='Levels of biological organisation', nodes=['Cell', 'Tissue', 'Organ', 'Organ system', 'Organism', 'Population', 'Community', 'Ecosystem', 'Biosphere'], footer='Population: one species. Community: many species. Ecosystem: life + environment.')
    add(2, 'taxonomy', '### 4.3 ', 'वर्गिकी पदानुक्रम: मनुष्य का उदाहरण',
        'जगत (Kingdom) → संघ (Phylum) → वर्ग (Class) → गण (Order) → कुल (Family) → वंश (Genus) → जाति (Species)। ऊपर से नीचे जाने पर समूह अधिक विशिष्ट बनते हैं। Homo वंश है; वैज्ञानिक नाम Homo sapiens में दोनों शब्द मिलकर जाति बताते हैं।',
        'flow', title='Taxonomic hierarchy: human example', nodes=['Kingdom · Animalia', 'Phylum · Chordata', 'Class · Mammalia', 'Order · Primates', 'Family · Hominidae', 'Genus · Homo', 'Species · Homo sapiens'], footer='From broad groups to increasingly specific groups')
    add(2, 'domains', '### 4.2 ', 'तीन डोमेन और पांच जगत: अलग वर्गीकरण प्रणालियां',
        'डोमेन (Domain) और जगत (Kingdom) एक ही स्तर नहीं हैं। वूज के तीन डोमेन हैं Bacteria, Archaea और Eukarya। व्हिटेकर की ऐतिहासिक पांच-जगत प्रणाली में Monera, Protista, Fungi, Plantae और Animalia हैं। Monera में वे प्रोकैरियोट रखे गए जिन्हें आधुनिक डोमेन प्रणाली अलग करती है।',
        'domains', title='Three domains ≠ five kingdoms', footer='Historical schemes are compared here; the ranks are not interchangeable.')
    add(3, 'cells', '### 4.5 ', 'पादप एवं जंतु कोशिका: संरचनात्मक तुलना',
        'Cell wall = कोशिका भित्ति; Cell membrane = कोशिका झिल्ली; Nucleus = केंद्रक; Chloroplast = हरितलवक; Vacuole = रिक्तिका; Cytoplasm = कोशिकाद्रव्य। दोनों कोशिकाओं में माइटोकॉन्ड्रिया हैं। यह प्रकाश-संश्लेषी पादप कोशिका है; जड़ की अधिकांश कोशिकाओं में हरितलवक नहीं होते।', 'existing', source='biology_cells.png')
    add(3, 'prokaryote_eukaryote', '### 4.2 ', 'प्रोकैरियोट और यूकैरियोट: केंद्रक का मुख्य अंतर',
        'प्रोकैरियोट में झिल्ली से घिरा केंद्रक नहीं होता; DNA न्यूक्लिऑइड क्षेत्र में रहता है। यूकैरियोट में केंद्रक और झिल्लीबद्ध कोशिकांग होते हैं। दोनों में प्लाज्मा झिल्ली, कोशिकाद्रव्य, DNA और राइबोसोम होते हैं। आकार योजनाबद्ध है।',
        'cells', title='Prokaryote versus eukaryote', footer='Both have DNA, cytoplasm, ribosomes and a plasma membrane. Not to scale.')
    add(3, 'bacterial_cell', '### 4.3 ', 'जीवाणु कोशिका: आवरण, DNA और उपांग',
        'Nucleoid = न्यूक्लिऑइड; Plasmid = प्लाज्मिड; Ribosomes = राइबोसोम; Pili = पिली; Flagellum = कशाभिका। जीवाणु के DNA को केंद्रकीय झिल्ली नहीं घेरती। कैप्सूल, प्लाज्मिड, पिली और कशाभिका सभी जीवाणुओं में अनिवार्य नहीं हैं। यह एक प्रतिनिधि मॉडल है।')
    add(4, 'secretory_pathway', '### 4.2 ', 'प्रोटीन का स्रावी मार्ग: ER से गॉल्जी तक',
        'स्रावी प्रोटीन खुरदरी ER से परिवहन पुटिका द्वारा गॉल्जी तक जाते हैं। गॉल्जी में संशोधन और छंटाई के बाद स्रावी पुटिका कोशिका झिल्ली से मिल सकती है। सभी प्रोटीन इस मार्ग से बाहर नहीं निकलते। ER = अंतःप्रद्रव्यी जालिका; Golgi = गॉल्जी उपकरण।',
        'flow', title='Secretory protein pathway', nodes=['Ribosome on rough ER', 'Protein enters ER', 'Transport vesicle', 'Golgi: modification + sorting', 'Secretory vesicle', 'Plasma membrane', 'Exocytosis'], footer='A pathway for secreted proteins; not the route of every cellular protein.')
    add(4, 'mitochondrion', '### 4.3 ', 'माइटोकॉन्ड्रिया: क्रिस्टी और मैट्रिक्स',
        'Cristae = आंतरिक झिल्ली की तहें; Matrix = मैट्रिक्स; Intermembrane space = अंतरझिल्ली स्थान। इलेक्ट्रॉन परिवहन और ATP संश्लेषण आंतरिक झिल्ली से जुड़े हैं। साइट्रिक अम्ल चक्र के अधिकांश एंजाइम मैट्रिक्स में होते हैं। माइटोकॉन्ड्रिया में अपना DNA और राइबोसोम भी होते हैं।')
    add(4, 'chloroplast', '### 4.3 ', 'हरितलवक: थाइलेकोइड, ग्रेना और स्ट्रोमा',
        'Thylakoid = थाइलेकोइड; Granum = थाइलेकोइड का ढेर; Stroma = स्ट्रोमा। प्रकाश अभिक्रियाएं थाइलेकोइड झिल्लियों पर तथा कैल्विन चक्र स्ट्रोमा में होता है। ग्रेनम एक ढेर है, पूरा हरितलवक नहीं।')
    add(4, 'mitosis', '### 4.6 ', 'समसूत्री विभाजन: 2n = 4 का मॉडल',
        'पूर्वावस्था → मध्यावस्था → पश्चावस्था → अंत्यावस्था। DNA की प्रतिकृति इससे पहले S-प्रावस्था में होती है। पश्चावस्था में सहोदरा क्रोमैटिड अलग होकर संतति गुणसूत्र बनते हैं। अंत में प्रत्येक नई कोशिका में चार गुणसूत्र हैं; यह उदाहरण मानव की 46-गुणसूत्रीय कोशिका नहीं है।', 'existing', source='biology_mitosis.png')
    add(4, 'meiosis', '### 4.7 ', 'अर्धसूत्री विभाजन: दो विभाजन, चार अगुणित उत्पाद',
        'पहले विभाजन में समजात गुणसूत्र और दूसरे में सहोदरा क्रोमैटिड अलग होते हैं। चित्र में 2n = 4 से n = 2 वाले चार उत्पाद बनते हैं। जीन-विनिमय पूर्वावस्था-I में समजात गुणसूत्रों की असहोदरा क्रोमैटिड के बीच होता है। अंडजनन में सभी चार उत्पाद समान आकार के कार्यात्मक अंडाणु नहीं बनते।',
        'meiosis', title='Meiosis: a 2n = 4 model', footer='Meiosis I: homologues separate. Meiosis II: sister chromatids separate.')
    add(5, 'plant_tissues', '### 4.1 ', 'पादप ऊतक: विभज्योतक और स्थायी ऊतक',
        'Meristematic = विभज्योतक; Permanent = स्थायी। सरल स्थायी ऊतकों में पैरेंकाइमा, कॉलेंकाइमा और स्क्लेरेंकाइमा हैं। जटिल ऊतकों में जाइलम और फ्लोएम हैं। यह मुख्य वर्गों का मानचित्र है; रक्षी एवं स्रावी ऊतक विस्तार से पाठ में पढ़ें।',
        'tree', title='Plant tissues: a classification map', root='Plant tissues', groups=[['Meristematic', 'Apical', 'Intercalary', 'Lateral'], ['Simple permanent', 'Parenchyma', 'Collenchyma', 'Sclerenchyma'], ['Complex permanent', 'Xylem', 'Phloem']], footer='Meristems divide actively; mature tissues acquire specialised functions.')
    add(5, 'vascular_tissues', '### 4.3 ', 'जाइलम और फ्लोएम: पदार्थ परिवहन',
        'Xylem = जाइलम; Phloem = फ्लोएम; Sieve plate = चालनी पट्टिका; Companion cell = सहचर कोशिका। जाइलम जल और खनिज पहुंचाता है; फ्लोएम शर्करा को स्रोत से सिंक तक पहुंचाता है। फ्लोएम प्रवाह केवल नीचे की ओर नहीं होता। चालनी नलिका का तत्व जीवित होता है, लेकिन परिपक्व अवस्था में केंद्रक नहीं होता।')
    add(5, 'epithelial_connective', '### 4.4 ', 'उपकला और संयोजी ऊतक: चार उदाहरण',
        'Squamous = शल्की; Columnar = स्तंभाकार; Areolar = एरिओलर; Adipose = वसा ऊतक। उपकला में कोशिकाएं सघन व्यवस्थित हैं; संयोजी ऊतक में बाह्यकोशिकीय मैट्रिक्स स्पष्ट होता है। चित्र पहचान के लिए योजनाबद्ध हैं, वास्तविक सूक्ष्मचित्र नहीं।')
    add(5, 'muscle_nerve', '### 4.4 ', 'तीन पेशी ऊतक और न्यूरॉन',
        'Skeletal = कंकाली; Smooth = चिकनी; Cardiac = हृदय पेशी। कंकाली पेशी बहुकेंद्रकी और रेखित, चिकनी पेशी अरेखित तथा हृदय पेशी शाखित और रेखित होती है। Intercalated disc = अंतरविष्ट पट्टिका; Dendrite = डेंड्राइट; Axon = अक्षतंतु।')
    add(6, 'biomolecules', '### 4.1 ', 'मुख्य जैव-अणु: निर्माण इकाइयां और कार्य',
        'कार्बोहाइड्रेट ऊर्जा और संरचना में, लिपिड झिल्लियों और ऊर्जा संग्रह में, प्रोटीन विविध संरचनात्मक व एंजाइमी कार्यों में और न्यूक्लिक अम्ल आनुवंशिक सूचना में भाग लेते हैं। लिपिड सामान्यतः प्रोटीन जैसे दोहराव वाले मोनोमर बहुलक नहीं हैं।',
        'molecules', title='Four major biomolecule groups', footer='Lipids are a diverse group; they are not generally repeating-monomer polymers.')
    add(6, 'dna_rna', '### 4.6 ', 'DNA और RNA: आधार और शर्करा में अंतर',
        'DNA में डिऑक्सीराइबोज और A,T,G,C; RNA में राइबोज और A,U,G,C होते हैं। DNA की दो विपरीत दिशाओं वाली शृंखलाओं में A-T और G-C युग्म बनते हैं। RNA सामान्यतः एकल शृंखला होता है, लेकिन मुड़कर आधार-युग्मित भाग बना सकता है।',
        'dna', title='DNA and RNA', footer='DNA strands are antiparallel. RNA is usually single-stranded and can fold.')
    add(6, 'enzyme_action', '### 4.5 ', 'एंजाइम क्रिया: सब्सट्रेट से उत्पाद तक',
        'Enzyme = एंजाइम; Substrate = सब्सट्रेट; Active site = सक्रिय स्थल। एंजाइम-सब्सट्रेट संकुल बनने के बाद उत्पाद निकलते हैं और एंजाइम पुनः काम कर सकता है। आकृति केवल संकल्पना समझाती है; वास्तविक बंधन में induced fit भी हो सकता है।',
        'enzyme', title='Enzyme action: binding, reaction, release', footer='The enzyme is regenerated; real binding may involve induced fit.')
    add(7, 'bacterial_shapes', '## भाग 4:', 'जीवाणुओं के चार सामान्य आकार',
        'Cocci = गोलाकार; Bacilli = दंडाकार; Vibrios = अल्पविरामाकार; Spirilla = सर्पिल। केवल आकार देखकर जीवाणु की जाति, लाभ या रोगजनकता निश्चित नहीं की जा सकती।')
    add(7, 'virus_bacterium', '## भाग 4:', 'विषाणु बनाम जीवाणु: अकोशिकीय और कोशिकीय',
        'विषाणु कोशिका नहीं है; उसका जीनोम DNA या RNA हो सकता है और प्रतिकृति के लिए उपयुक्त मेजबान कोशिका चाहिए। जीवाणु कोशिका है और उसमें राइबोसोम होते हैं। प्रतिजैविक जीवाणुओं पर कार्य कर सकते हैं; विषाणुओं के लिए वही सामान्य प्रभाव नहीं होता।',
        'virus', title='Virus versus bacterium', footer='Viruses require suitable host cells for replication. Bacteria are cells.')
    add(7, 'fungi_protists', '## भाग 4:', 'कवक और प्रोटिस्ट: पहचान के उदाहरण',
        'अमीबा, पैरामीशियम और यूग्लीना प्रोटिस्ट के उदाहरण हैं। यीस्ट, राइजोपस और मशरूम कवक हैं। Pseudopodia = कूटपाद; Cilia = पक्ष्माभ; Hyphae = कवकतंतु; Sporangium = बीजाणुधानी। वर्गीकरण की प्रणालियां बदल सकती हैं; यहां पुस्तक के शैक्षिक समूहों का प्रयोग है।')
    add(8, 'fermentation', '## भाग 4:', 'किण्वन: यीस्ट और लैक्टिक अम्ल जीवाणु',
        'यीस्ट के अल्कोहलीय किण्वन में ग्लूकोज से एथेनॉल और CO₂ बनते हैं। लैक्टिक अम्ल किण्वन में लैक्टेट बनता है। दोनों मार्गों में ग्लाइकोलाइसिस से ATP मिलता है और NAD⁺ पुनर्जनित होता है। सभी किण्वन उत्पाद एक जैसे नहीं हैं।',
        'tree', title='Two fermentation routes', root='Glucose → glycolysis → pyruvate', groups=[['Alcoholic fermentation', 'Yeast', 'Ethanol + carbon dioxide', 'NAD+ regenerated'], ['Lactic acid fermentation', 'Lactic acid bacteria', 'Lactate', 'NAD+ regenerated']], footer='Glycolysis supplies ATP; fermentation regenerates NAD+ for glycolysis.')
    add(8, 'nitrogen_fixation', '## भाग 4:', 'नाइट्रोजन चक्र: स्थिरीकरण और पुनर्चक्रण',
        'Nitrogen fixation = स्थिरीकरण; Nitrification = नाइट्रीकरण; Denitrification = विनाइट्रीकरण। पौधे सामान्यतः वायुमंडलीय N₂ सीधे नहीं लेते। जैविक स्थिरीकरण उसे उपयोगी नाइट्रोजन रूपों में बदलता है; विनाइट्रीकरण नाइट्रोजन गैस वापस वातावरण में भेजता है।',
        'nitrogen', title='Nitrogen cycle: key transformations', footer='Plants generally absorb nitrate or ammonium, not atmospheric N2 directly.')
    add(8, 'sewage_biogas', '## भाग 4:', 'वाहित मल से सक्रिय आपंक और बायोगैस तक',
        'प्राथमिक उपचार में ठोस पदार्थ अलग होते हैं। वातन टैंक में सूक्ष्मजीव कार्बनिक पदार्थ कम करते हैं। आपंक का कुछ भाग फिर वातन टैंक में जाता है; शेष का अवायवीय पाचन मीथेन-युक्त बायोगैस दे सकता है। अंतिम जल को आवश्यक अतिरिक्त उपचार और मानकों के बाद ही छोड़ा जाता है।',
        'sewage', title='Sewage treatment and biogas', footer='Treated water still requires appropriate final treatment and quality checks.')
    add(9, 'plant_groups', '## भाग 4:', 'पादप समूह: बीज और संवहनी ऊतक के आधार पर',
        'ब्रायोफाइट में वास्तविक जाइलम-फ्लोएम नहीं; टेरिडोफाइट बीजरहित संवहनी पादप हैं। जिम्नोस्पर्म के बीज अंडाशय से बने फल में बंद नहीं होते; एंजियोस्पर्म में फूल और अंडाशय से बने फल मिलते हैं। यह पारंपरिक शैक्षिक समूह तुलना है, आधुनिक वंशवृक्ष नहीं।',
        'plantgroups', title='Plant groups: diagnostic features', footer='Traditional teaching groups; this comparison is not a modern phylogenetic tree.')
    add(9, 'plant_examples', '## भाग 4:', 'शैवाल से पुष्पीय पादप तक: प्रतिनिधि रूप',
        'स्पाइरोगाइरा का सर्पिल हरितलवक, मॉस का कैप्सूल, फर्न के सोराई, पाइन का शंकु और पुष्पीय पादप का फूल/फल पहचानें। हर समूह में अनेक रूप होते हैं; इन उदाहरणों को पूरे समूह की एकमात्र बनावट न मानें।')
    add(9, 'alternation', '## भाग 4:', 'पीढ़ियों का एकांतरण: n और 2n का चक्र',
        'द्विगुणित बीजाणुद्भिद (Sporophyte) में अर्धसूत्री विभाजन से अगुणित बीजाणु बनते हैं। बीजाणु समसूत्री विभाजन से युग्मकोद्भिद (Gametophyte) बनाते हैं, जो समसूत्री विभाजन से युग्मक बनाता है। निषेचन से 2n युग्मनज बनता है।',
        'alternation', title='Alternation of generations', footer='Meiosis produces spores. Gametes form by mitosis in the haploid gametophyte.')
    add(10, 'invertebrates', '## भाग 4:', 'अकशेरुकी संघ: आठ प्रतिनिधि जीव',
        'स्पंज–Porifera; हाइड्रा–Cnidaria; प्लेनेरिया–Platyhelminthes; गोलकृमि–Nematoda; केंचुआ–Annelida; तितली–Arthropoda; घोंघा–Mollusca; तारामछली–Echinodermata। इन चित्रों के साथ पाठ में ऊतक संगठन, देहगुहा और सममिति भी मिलाएं।')
    add(10, 'symmetry', '## भाग 4:', 'असममिति, अरीय और द्विपार्श्व सममिति',
        'Asymmetry = असममिति; Radial = अरीय; Bilateral = द्विपार्श्व। चित्र की रेखाएं विभाजन तल का संकेत हैं। वयस्क एकाइनोडर्म अरीय होते हैं, लेकिन उनके लार्वा द्विपार्श्व होते हैं।')
    add(10, 'vertebrates', '### 4. उप-संघ वर्टिब्रेटा', 'कशेरुकी वर्ग: पहचान के प्रमुख लक्षण',
        'उपास्थिल मछली, अस्थिल मछली, उभयचर, सरीसृप, पक्षी और स्तनधारी के उदाहरण देखें। ये वर्ग किसी सीढ़ी पर लगातार बनने वाले चरण नहीं हैं। बाल और दुग्ध ग्रंथियां स्तनधारियों तथा पंख पक्षियों के महत्वपूर्ण लक्षण हैं।')
    add(10, 'chordate_features', '## भाग 4:', 'कॉर्डेट के मुख्य लक्षण: लैंसलेट का मॉडल',
        'Notochord = पृष्ठरज्जु; Dorsal hollow nerve cord = पृष्ठीय खोखली तंत्रिका रज्जु; Pharyngeal slits = ग्रसनी छिद्र; Post-anal tail = गुदापश्च पुच्छ। ये लक्षण जीवन की किसी अवस्था में पाए जाते हैं। प्रत्येक कॉर्डेट में कशेरुक स्तंभ होना आवश्यक नहीं।')
    add(11, 'monohybrid', '### 4.2 ', 'एकसंकर संकरण: Tt × Tt',
        'इस पूर्ण प्रभाविता मॉडल में TT और Tt लंबे तथा tt बौने हैं। संतति का जीनप्रारूप अनुपात 1:2:1 और लक्षणप्रारूप अनुपात 3:1 है। प्रत्येक खाने की संभावना 1/4 है; छोटी वास्तविक संतति में अनुपात ठीक इतना होना अनिवार्य नहीं।',
        'punnett', title='Monohybrid cross: Tt × Tt', gametes=['T', 't'], cells=[['TT', 'Tt'], ['Tt', 'tt']], footer='Genotypes 1 TT : 2 Tt : 1 tt. Complete dominance gives 3 tall : 1 dwarf.')
    add(11, 'dihybrid', '### 4.4 ', 'द्विसंकर संकरण: RrYy × RrYy',
        'RY, Ry, rY और ry युग्मक स्वतंत्र अपव्यूहन मॉडल में समान संभाव्य हैं। पूर्ण प्रभाविता और स्वतंत्र जीनों के लिए 9 गोल-पीले : 3 गोल-हरे : 3 झुर्रीदार-पीले : 1 झुर्रीदार-हरा अनुपात मिलता है। सहलग्नता होने पर यही अनुपात आवश्यक नहीं।',
        'punnett', title='Dihybrid cross: RrYy × RrYy', gametes=['RY', 'Ry', 'rY', 'ry'], cells=[['RRYY','RRYy','RrYY','RrYy'],['RRYy','RRyy','RrYy','Rryy'],['RrYY','RrYy','rrYY','rrYy'],['RrYy','Rryy','rrYy','rryy']], footer='Independent genes + complete dominance: 9 round/yellow : 3 round/green : 3 wrinkled/yellow : 1 wrinkled/green.')
    add(11, 'test_cross', '### 4.3 ', 'परीक्षण संकरण: अज्ञात प्रभावी जीनप्रारूप पहचानें',
        'प्रभावी लक्षण वाले पौधे को समयुग्मजी अप्रभावी tt से संकरित करते हैं। TT × tt में सभी Tt; Tt × tt में अपेक्षित आधे Tt और आधे tt बनते हैं। सभी संतति प्रभावी होने का छोटा नमूना अकेले TT का पूर्ण प्रमाण नहीं।',
        'testcross', title='Test cross: TT or Tt?', footer='A recessive offspring reveals a recessive allele in the dominant-looking parent.')
    add(11, 'dominance', '### 4.5 ', 'अपूर्ण प्रभाविता और सहप्रभाविता',
        'अपूर्ण प्रभाविता में लाल RR और सफेद rr का Rr संकर गुलाबी है। सहप्रभाविता में दोनों युग्मविकल्प व्यक्त होते हैं; उदाहरण ABO में IᴬIᴮ का AB समूह। अपूर्ण प्रभाविता में एलील नष्ट या स्थायी रूप से घुल-मिल नहीं जाते।',
        'dominance', title='Incomplete dominance versus codominance', footer='Alleles remain distinct; heterozygotes can show an intermediate or both contributions.')
    add(12, 'sex_determination', '### 4.2 ', 'मानव का सामान्य XX–XY निर्धारण मॉडल',
        'इस सामान्य गुणसूत्र मॉडल में अंडाणु X और शुक्राणु X या Y देता है। XX या XY संयोजन की अपेक्षित संभावना लगभग बराबर है। यह पिता या माता के चुनाव से नियंत्रित नहीं होता; वास्तविक जैविक लिंग विकास में अन्य जीन और विविधताएं भी हैं।',
        'sex', title='Typical human XX–XY chromosome model', footer='Egg contributes X; sperm contributes X or Y. This is a chromosome model, not every variation of sex development.')
    add(12, 'abo', '### 4.5 ', 'ABO वंशागति: सहप्रभाविता और अप्रभावी i',
        'Iᴬ और Iᴮ सहप्रभावी हैं; दोनों i पर प्रभावी हैं। A समूह IᴬIᴬ या Iᴬi; B समूह IᴮIᴮ या Iᴮi; AB समूह IᴬIᴮ; O समूह ii। यह वंशागति का चित्र है, रक्त चढ़ाने की अनुकूलता मार्गदर्शिका नहीं।',
        'abo', title='ABO inheritance: alleles and phenotypes', footer='IA and IB are codominant; each is dominant over i. Inheritance chart only.')
    add(12, 'linkage', '### 4.7 ', 'सहलग्नता और जीन-विनिमय',
        'AB/ab व्यवस्था में बिना विनिमय के AB और ab पैतृक संयोजन हैं। A और B के बीच असहोदरा क्रोमैटिड का विनिमय Ab और aB पुनर्संयोजक बनाता है। एक विनिमय में चार क्रोमैटिड में से दो भाग लेते हैं। चित्र आवृत्ति या मानचित्र दूरी नहीं बताता।',
        'linkage', title='Crossing-over creates new allele combinations', footer='One exchange between non-sister chromatids gives 2 parental + 2 recombinant chromatids.')
    add(13, 'mutations', '### 4.1 ', 'उत्परिवर्तन: प्रतिस्थापन, विलोपन और निवेशन',
        'Substitution = प्रतिस्थापन; Deletion = विलोपन; Insertion = निवेशन। अनुक्रम के अक्षर क्रम समझाने के लिए हैं, किसी वास्तविक जीन का निदान नहीं। प्रोटीन-कोडिंग भाग में तीन के गुणज से अलग आधार निवेशन/विलोपन reading frame बदल सकता है।',
        'mutations', title='Sequence changes: substitution, deletion, insertion', footer='In coding regions, an insertion/deletion not divisible by 3 can shift the reading frame.')
    add(13, 'nondisjunction', '### 4.3 ', 'अवियोजन: गुणसूत्र अलग न होने का परिणाम',
        'Nondisjunction = अवियोजन। अर्धसूत्री विभाजन-I में एक समजात जोड़ा साथ चला जाए तो उस जोड़े के लिए सभी चार युग्मक असामान्य हो सकते हैं: दो n+1 और दो n−1। यह पूरे मानव गुणसूत्र समुच्चय का चित्र नहीं, एक जोड़े का मॉडल है।',
        'nondisjunction', title='Meiosis I nondisjunction: one pair model', footer='Both homologues go to one pole → two n+1 gametes and two n−1 gametes.')
    add(14, 'selection', '### 4.3 ', 'प्राकृतिक वरण: वंशानुगत भिन्नता का चयन',
        'पर्यावरण में कुछ वंशानुगत रूप अधिक संतति छोड़ते हैं, इसलिए पीढ़ियों में उनकी आवृत्ति बदल सकती है। किसी जीव को जरूरत होने से वह इच्छानुसार नया अनुकूल लक्षण नहीं बनाता। चित्र में रंग काल्पनिक चयन मॉडल है।',
        'selection', title='Natural selection changes trait frequencies', footer='Selection acts on existing heritable variation through differential reproduction.')
    add(14, 'homology_analogy', '### 4.2 ', 'समजात और समवृत्ति संरचनाएं',
        'Homologous = समजात: समान मूल संरचना, कार्य अलग हो सकते हैं। Analogous = समवृत्ति: समान कार्य, उद्भव अलग। पक्षी और तितली का पंख उड़ान के लिए समवृत्ति है; पक्षी और चमगादड़ के अग्रपाद की अस्थियां साझा कशेरुकी मूल रखती हैं।')
    add(14, 'evolution_tree', '### 4.4 ', 'विकास शाखाओं में होता है: साझा पूर्वज का मॉडल',
        'वंशवृक्ष में शाखा बिंदु साझा पूर्वज दर्शाता है। आज की प्रजातियां एक-दूसरे की अनिवार्य पूर्वज नहीं हैं। यह काल्पनिक A–D प्रजातियों का वृक्ष है; शाखा लंबाई समय नहीं बताती।',
        'phylogeny', title='Evolution is branching, not a ladder', footer='Hypothetical taxa A–D. Branch lengths do not represent time or amount of change.')
    add(15, 'root_symbiosis', '### 4.2 ', 'जड़ सहजीवन: मूल ग्रंथिका और माइकोराइजा',
        'दलहनी ग्रंथिका में राइजोबियम-जैसे सहजीवी नाइट्रोजन स्थिरीकरण में भाग लेते हैं। माइकोराइजा के कवकतंतु जल और फॉस्फेट उपलब्धता में सहायक होते हैं। पौधा सूक्ष्मजीव को कार्बनिक पदार्थ देता है। दोनों सहजीवन को एक प्रक्रिया न मानें।')
    add(15, 'rajasthan_flora', '### 4.7 ', 'राजस्थान के पादप: खेजड़ी, रोहिड़ा, कैर और बेर',
        'खेजड़ी = Prosopis cineraria; रोहिड़ा = Tecomella undulata; कैर = Capparis decidua; बेर = Ziziphus mauritiana। पत्तियां, फल, फूल और वृद्धि रूप साथ देखकर पहचानें। चित्र शैक्षिक संकेत हैं, वनस्पति पहचान का अकेला प्रमाण नहीं।')
    add(16, 'revision_map', '## भाग 4:', 'जीव विज्ञान-I: अवधारणाओं का पुनरावृत्ति मानचित्र',
        'कोशिका और जैव-अणु संरचना का आधार हैं; ऊतक कार्य विभाजित करते हैं; वर्गीकरण विविधता व्यवस्थित करता है; वंशागति लक्षणों का संचरण बताती है; विकास पीढ़ियों में परिवर्तन और साझा मूल समझाता है। मानचित्र देखने के बाद प्रत्येक शाखा से एक उदाहरण याद करें।',
        'tree', title='Biology I: connect the ideas', root='Biology I', groups=[['Structure + function', 'Cells and organelles', 'Tissues', 'Biomolecules + enzymes'], ['Diversity + applications', 'Plant and animal groups', 'Microorganisms', 'Biofertilisers + botany'], ['Inheritance + evolution', 'Mendelian crosses', 'Linkage + mutation', 'Selection + ancestry']], footer='Recall one example and one mechanism for every branch.')
    assert len(figures) == 46, len(figures)
    return figures


if __name__ == '__main__':
    path = ROOT / 'artifacts/biology_book1_figure_briefs.json'
    path.write_text(json.dumps(plan(), ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(f'Wrote {len(plan())} figure briefs')
