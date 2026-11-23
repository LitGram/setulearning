"""Selected, source-located exam subquestions; Hindi summaries and independently written solutions."""
from pathlib import Path
import json

ANSWERS = {}
def answers(text):
    for line in text.strip().splitlines():
        key,topic,answer=line.split('|')
        ANSWERS[key]=dict(topic=int(topic),answer=answer)

answers('''neutral|2|लगभग 25°C पर उदासीन जलीय विलयन का pH 7 होता है। इसमें H₃O⁺ और OH⁻ की concentrations समान होती हैं।
formic|2|विद्यालयी उत्तर methanoic/formic acid, HCOOH है। अम्लीय प्रभाव को उपयुक्त क्षारक द्वारा neutralisation से समझा जाता है।
multiple|7|Plasmodium में multiple fission: एक parent cell से अनेक daughter cells बन सकते हैं। Binary fission में केवल दो बनते हैं।
ozonecause|13|CFCs जैसे ozone-depleting substances से stratosphere में chlorine-related catalytic reactions ozone घटा सकती हैं। इससे UV shielding कम होती है; यह greenhouse warming का समानार्थी नहीं।
overload|12|एक socket/circuit पर बहुत appliances से total current rating से अधिक हो सकता है: overloading। I²R heating बढ़ सकती है। Load rating मानें और suitable protective devices रखें; एक socket में high-power loads न जोड़ें।
redox|1|CuO + H₂ → Cu + H₂O में H₂ oxygen पाकर oxidised, CuO oxygen खोकर reduced है। Oxidation तथा reduction एक साथ होना redox है; दूसरा उदाहरण ZnO + C → Zn + CO है।
electrolysis|1|2H₂O → 2H₂ + O₂, electrical energy की उपस्थिति में। Diagram में electrolyte युक्त water, दो electrodes, DC source, cathode पर H₂ और anode पर O₂ दिखाएँ; समान परिस्थितियों में gas volumes 2:1 हैं।
photo|5|Light/chlorophyll energy absorb करते हैं; water से oxygen liberation तथा CO₂ का carbohydrate में reduction होता है। Simplified equation 6CO₂ + 6H₂O → C₆H₁₂O₆ + 6O₂ है; light/chlorophyll condition लिखें।
vegetative|7|Root, stem अथवा leaf के vegetative parts से नए plants बनाना vegetative propagation है। Potato stem buds और Bryophyllum leaf buds उदाहरण हैं। Seed-less plants को बढ़ाने और useful traits बनाए रखने में उपयोगी है।
darksky|10|Atmosphere न होने या अत्यल्प होने पर sunlight का scattering पर्याप्त नहीं होता। इसलिए atmosphere से बाहर astronaut को सूर्य चमकने के बावजूद background sky dark दिखाई देता है।
iris|10|Iris की muscles pupil opening का size नियंत्रित करती हैं। Lens की curvature ciliary muscles बदलती हैं; light entry और accommodation के mechanisms अलग हैं।
zincalkali|2|Hydrogen निकलती है। विद्यालयी समीकरण: Zn + 2NaOH → Na₂ZnO₂ + H₂। Aqueous complex formulation में zincate को hydroxo-complex से भी लिखा जाता है; prescribed school representation का उपयोग करें।
saltsuses|2|Germ-free water के लिए bleaching powder, baking के लिए NaHCO₃, स्थायी कठोरता घटाने के लिए washing soda और moulds/toys के लिए POP। क्रमशः CaOCl₂, NaHCO₃, Na₂CO₃·10H₂O और CaSO₄·½H₂O लिखें।
displacement|1|अधिक active element कम active को compound से हटाता है। Zn + CuSO₄ → ZnSO₄ + Cu उदाहरण है; zinc copper से अधिक active है।
znso4|1|ZnSO₄ बनता है: Zn + CuSO₄ → ZnSO₄ + Cu। यह displacement तथा redox दोनों है; Cu²⁺ reduced और zinc oxidised होता है।
baso4|1|BaSO₄ सफेद insoluble precipitate है: Na₂SO₄ + BaCl₂ → BaSO₄↓ + 2NaCl। यह double displacement तथा precipitation है।
dialysis|5|Haemodialysis में blood semipermeable interface के across dialysing fluid से संपर्क करता है और wastes/अतिरिक्त solutes हटाए जा सकते हैं। Kidney failure में clinical use है; यह kidney के सभी functions का पूर्ण replacement नहीं।
budding|7|Hydra में repeated cell division से body wall पर bud निकलता है, mouth/tentacles बनते हैं और mature bud अलग individual हो सकता है। Diagram में parent, bud, tentacles और detachment stages label करें।
sexhormones|6|विद्यालयी प्रमुख male hormone testosterone है; female reproductive hormones में oestrogen और progesterone शामिल हैं। ये सामान्य sex characteristics तथा reproductive functions में भूमिका निभाते हैं; hormone केवल एक sex में ही पाया जाता है, ऐसा absolute दावा न करें।
threeR|13|Reduce: unnecessary consumption/waste घटाएँ। Reuse: वस्तु फिर उपयोग करें। Recycle: waste material से उपयोगी material बनाएं। उदाहरण bottle reuse, कम packaging और separated paper recycling हैं।
focusmirror|9|Concave mirror पर principal axis के parallel paraxial rays reflect होकर principal focus पर मिलती हैं। Convex mirrors rear-view तथा wide-angle security viewing में useful हैं; virtual erect diminished image देते हैं।
ohm|11|स्थिर temperature/physical conditions में V ∝ I, इसलिए V=IR। Low-voltage circuit में ammeter series, voltmeter resistor के parallel; कई V,I readings में V/I लगभग constant और V-vertical/I-horizontal graph straight line होता है।
amphoteric|3|Amphoteric oxides acids और bases दोनों से reaction करते हैं। Al₂O₃ तथा ZnO उदाहरण हैं। केवल सभी metal oxides acidic या सभी केवल basic लिखना उचित नहीं।
brass|3|Brass copper और zinc की alloy है। Bronze copper–tin है; इन दोनों मिश्रधातुओं के घटक अलग हैं।
foodenergy|13|Food chain organisms के बीच feeding/energy transfer दिखाती है: grass → grasshopper → frog → snake। Solar energy producer से consumers तक जाती है और हर step में heat/metabolism से घटती है; लगभग 10% transfer school model है। Nutrients cycle कर सकते हैं, energy flow one-way है।
thumb|12|Right-hand thumb conventional current की दिशा में रखें; curled fingers wire के circular magnetic field की direction देती हैं। Thumb force नहीं बताता; force के लिए Fleming left-hand rule है।
solenoid|12|Solenoid के भीतर, ends से दूर लगभग parallel equally spaced field lines draw करें; बाहर N→S तथा अंदर S→N return direction, closed loops। Current और coil turns field को प्रभावित करते हैं; suitable iron core से electromagnet बनाया जा सकता है।
covalent|4|Covalent bond electron pair के sharing से बनता है। CH₄ में चार C–H single bonds और ethene में C=C double bond है। Electron-dot diagram में हर shared pair दिखाएँ; ionic electron transfer की तरह पूर्ण charge formation न दिखाएँ।
neuron|6|Dendrites incoming signals ग्रहण, cell body integration और axon terminal तक conduction करता है। Chemical synapse पर neurotransmitter next cell तक signal पहुँचाता है। Diagram arrows dendrite → body → axon → terminal तथा labels दें।
respiration|5|Cellular respiration food का breakdown करके usable energy release करने की प्रक्रिया है। Cytoplasm में glucose से pyruvate; aerobic mitochondrial route CO₂/water देता है। Yeast anaerobic route ethanol/CO₂ तथा oxygen-deficit muscles lactate दे सकते हैं।
lenspower|9|Lens power P=1/f है, f metre में; unit dioptre। Convex/converging lens positive, concave/diverging lens negative power रखता है। Centimetre में f का reciprocal सीधे dioptres नहीं देता।
normalincidence|9|Normal incidence पर ray की direction सामान्यतः unchanged रहती है, लेकिन medium बदलने से speed और wavelength बदल सकते हैं। Frequency interface पार करते समय unchanged रहती है।
defects|10|Myopia: दूर वस्तु की image retina के आगे; correction concave lens। Hypermetropia: near-object focus retina के पीछे की tendency; correction convex lens। Diagrams में retina और corrected focus label करें।
indicators|2|Phenolphthalein और methyl orange दो synthetic indicators हैं। Phenolphthalein acidic medium में colourless और basic में pink है।
placenta|7|Placenta maternal–fetal exchange interface है: oxygen/nutrients fetus को तथा metabolic wastes maternal side को transfer होते हैं। दोनों blood systems सामान्यतः सीधे common pool में नहीं मिलते। Damage से fetal nutrition/oxygen supply प्रभावित हो सकती है।
phcompare|2|Blood का typical pH लगभग 7.4, distilled water लगभग 7; blood अधिक pH वाला है। Gastric juice का pH सामान्यतः lemon juice से कम, इसलिए lemon juice अपेक्षाकृत अधिक pH वाला है। Actual values conditions पर निर्भर हैं।
accommodation|10|Eye lens की focal length adjust करने की क्षमता accommodation है। Ciliary muscles curvature बदलती हैं: near object के लिए lens अधिक convex और focal length कम होती है।
combdecomp|1|Combination: CaO + H₂O → Ca(OH)₂; अनेक reactants से एक मुख्य product। Decomposition: CaCO₃ → CaO + CO₂ (heat); एक compound कई products देता है। दोनों equations balanced रखें।
uv|13|Stratospheric ozone harmful ultraviolet radiation के कुछ हिस्से को absorb करता है। UV shielding घटने को ozone depletion से जोड़ें, visible colours के dispersion से नहीं।
sexdetermination|8|XX–XY school model में egg X और sperm X या Y देता है। X+X → XX, X+Y → XY; expected probability लगभग बराबर। Mother को outcome के लिए दोष देने का scientific आधार नहीं।
stomachacid|5|HCl stomach में acidic environment बनाता है, pepsin action के अनुकूल है और कई microbes के विरुद्ध मदद करता है। Mucus lining रक्षा करती है; HCl स्वयं protein-digesting enzyme नहीं।
nutrition|5|Autotroph inorganic sources से organic food बनाते हैं; green plants photosynthesis से। Heterotroph दूसरे organisms से organic food लेते हैं; humans इसका उदाहरण हैं। दोनों usable energy के लिए cellular processes रखते हैं।
nervoushormonal|6|Nervous messages specific neural paths से सामान्यतः तेज और short-lived responses देते हैं। Hormones blood से receptor-bearing targets तक जाते और अक्सर slower/longer responses देते हैं। Messenger, route और timescale स्पष्ट तुलना-बिंदु हैं।
realvirtual|9|Real image actual rays के meeting से screen पर प्राप्त हो सकती है। Virtual image backward extensions से apparent meeting है और उसी location पर screen image नहीं बनती। Mirror surface inward concave, outward convex होता है।
insulinthyroxine|6|Insulin pancreas से blood glucose regulation में सहायता करता है। Thyroxine thyroid से metabolic regulation में काम करता है और iodine चाहिए। Insulin deficiency diabetes mellitus से संबंधित हो सकती है; सभी diabetes केवल complete absence नहीं।
dispersion|10|White light का constituent wavelengths/colours में separation dispersion है। Prism का refractive index wavelength-dependent होने से colours अलग deviate करते हैं; ordinary glass में violet अधिक, red कम deviates है।
fragmentregbud|7|Fragmentation: Spirogyra filament pieces नए individuals बन सकते हैं। Regeneration: Planaria suitable fragments से body पुनः बना सकती है। Budding: Hydra/yeast में outgrowth नया organism देता है। हर animal body fragment reproduce नहीं करता।
zincacid|2|Zn + H₂SO₄(dil.) → ZnSO₄ + H₂। Gas hydrogen है; prescribed supervised test में burning splint से characteristic pop मिल सकता है। Acid/gas experiment स्वयं न करें।
slab|9|Parallel-sided glass slab में oblique ray entry पर normal की ओर और exit पर normal से दूर bends करती है। Same external medium में emergent ray incident के parallel लेकिन laterally displaced होती है; normal incidence पर displacement शून्य।
ecosystem|13|Biotic: plants, animals, microbes। Abiotic: light, water, temperature, soil conditions। इनके interactions ecosystem बनाते हैं। उदाहरण pond में algae producer और organisms consumers हैं; decomposers nutrient recycling करते हैं।
mercury|3|Mercury सामान्य room temperature पर liquid metal है। इसका अर्थ सभी metals liquid हैं या liquid पदार्थ metal ही है, ऐसा नहीं।
mgcl2|3|Mg configuration 2,8,2 और Cl 2,8,7 है। Mg दो electrons खोकर Mg²⁺, दो Cl एक-एक लेकर Cl⁻ बनाते हैं। +2 तथा 2×−1 charges balance से MgCl₂ ionic lattice बनता है।
left|12|Left-hand thumb, forefinger और middle finger mutually perpendicular रखें। Forefinger B, middle conventional I तथा thumb force/motion देता है। Current या field अकेला reverse हो तो force reverse होता है।
doublecirculation|5|Body → right atrium/ventricle → lungs → left atrium/ventricle → body। Pulmonary तथा systemic circuits में blood heart से twice passes; चार chambers mixing घटाते और oxygen delivery कुशल करते हैं।
salivabile|5|Salivary amylase starch digestion शुरू करता है। Bile liver में बनता है; fat emulsification तथा intestinal medium में मदद करता है, digestive enzyme नहीं। Small intestine में fat digestion और absorption प्रमुख हैं।
resistivity|11|R=ρl/A: length, cross-section, material तथा temperature matter करते हैं। ρ=RA/l, unit Ω·m। Same material/temperature में geometry बदलने से R बदलता है, intrinsic resistivity नहीं।
joule|11|H=I²Rt: current square, resistance और time का product joules देता है। Filament bulbs में inert gases जैसे argon तथा nitrogen oxidation/evaporation घटाने में मदद करते हैं। Power और heat-energy units अलग रखें।
homology|4|Same functional group/general formula; successive members differ by CH₂ (14 u)। Similar chemical properties और gradual physical-property changes होते हैं। Ethane के अगले homologues propane C₃H₈ तथा butane C₄H₁₀ हैं।
carbonfeatures|4|Tetravalency से चार covalent bonds और catenation से chains/branches/rings बनते हैं। Stable C–C bonding carbon compounds की विविधता में मदद करती है। Organic compounds में electron sharing प्रमुख है।
bakingpowder|2|Baking powder में NaHCO₃ तथा edible weak acid, जैसे tartaric acid, होते हैं। Heating पर CO₂ food को rise देती है; acid residual carbonate की bitter/basic effect कम करता है।
uniformfield|12|Uniform magnetic field को parallel, equally spaced straight lines और same direction arrowheads से draw करें। Lines की spacing uniform strength तथा tangent direction दर्शाती है।
eastwest|12|Current east→west और point सीधे नीचे हो तो right-hand rule से field south की ओर है। Directions को coordinate cross-product से check करें; above-wire point पर direction उलटी होगी।
reflex|6|Receptor → sensory neuron → spinal relay → motor neuron → effector muscle। तेज automatic withdrawal response reflex है; brain को information भी मिलती है। Arc diagram में nerve direction और effector label करें।
menstruation|7|Ovum fertilised न हो और pregnancy न बने तो hormonal changes के साथ uterine lining shed हो सकती है। Blood/tissue vagina से बाहर आते हैं: menstruation। Cycle length vary करती है; इसे ‘impure blood’ नहीं कहें।
toothpH|2|Bacterial sugar metabolism acid बनाता है; mouth pH लगभग 5.5 से नीचे गिरने पर enamel demineralisation बढ़ सकती है। Mildly basic toothpaste acid neutralisation में मदद करता है। pH acid strength और total amount का अकेला प्रमाण नहीं।
calcroast|3|Calcination में carbonate ore limited/no air पर oxide+CO₂ देता है। Roasting में sulfide ore excess air से oxide और SO₂ देता है। ZnCO₃ → ZnO+CO₂; 2ZnS+3O₂ → 2ZnO+2SO₂।
rust|3|Painting और galvanising iron को moisture/oxygen से बचाते हैं। Zinc coating sacrificial protection भी दे सकती है; iron का corrosion नमी तथा oxygen से जुड़ा है।
mgo|1|2Mg + O₂ → 2MgO। Product magnesium oxide है, combination reaction का उदाहरण। Mg और O दोनों sides पर 2 atoms हैं।
nearpoint|10|Normal young-adult school model में least distance of distinct vision लगभग 25 cm है। यह typical approximation है, हर individual का fixed measured near point नहीं।
dihybrid|8|Independent assortment और complete dominance के model में pure dominant × pure recessive से F₁ दोनों dominant traits वाला heterozygote है। F₁ selfing से expected F₂ phenotypes 9:3:3:1। यह universal genetic ratio नहीं।
rearview|9|Convex mirror wide field of view तथा erect, diminished virtual image देता है। इसलिए vehicle rear-view में useful है; concave magnified-image case से अलग रखें।
parallel|11|Parallel branches पर समान supply voltage और independent switching मिलता है। एक appliance बंद/खराब होने पर अन्य branches चल सकती हैं। Series circuit में voltage sharing और common current होता है।
rancidity|1|Fat oxidation rancidity देती है। Airtight packs/nitrogen flushing oxygen exposure घटाते; refrigeration rate घटाती है। Rancid food को गरम करना हर hazard को खत्म करने की गारंटी नहीं।
metalproperties|3|Metals सामान्यतः lustrous, malleable, ductile तथा good conductors हैं। Sodium नरम और mercury liquid exceptions हैं। General property को ‘सभी’ के absolute statement में न बदलें।
alloy|3|Alloy metal का दूसरे metal/nonmetal के साथ mixture है। Brass Cu–Zn, bronze Cu–Sn; composition से hardness, corrosion resistance आदि बदलते हैं।
oxides|3|Metal oxides सामान्यतः basic, nonmetal oxides सामान्यतः acidic। Al₂O₃/ZnO amphoteric और CO जैसे neutral oxides exceptions हैं।
tyndall|10|Colloidal/suitable small particles light scatter करके beam path visible करते हैं: Tyndall effect। Clear blue sky molecular scattering और star twinkling atmospheric refraction से जुड़े हैं।
acidwater|2|Acid dilution heat release कर सकता है। Acid धीरे large water volume में डालने से heat dissipation बेहतर और splashing कम; water को concentrated acid में अचानक न डालें।
chloralkali|2|Brine electrolysis: 2NaCl+2H₂O → 2NaOH+Cl₂+H₂। Anode पर Cl₂, cathode पर H₂ और solution में NaOH; products को अलग रखें।
bleachpop|2|Bleaching powder का school formula CaOCl₂; water disinfection/bleaching में उपयोग। POP CaSO₄·½H₂O, plaster/moulds के लिए; water जोड़कर gypsum CaSO₄·2H₂O बनकर जमता है।
crystalwater|2|Salt crystal structure में निश्चित संख्या के water molecules crystallisation water हैं। CuSO₄·5H₂O तथा Na₂CO₃·10H₂O examples हैं; यह केवल बाहरी गीलापन नहीं।
aba|6|Abscisic acid (ABA) growth inhibition और stress responses से संबंधित है। Water stress में stomatal closing में भी भूमिका निभाता है।
cytokinin|6|Cytokinin plant cell division promote कर सकता है। Insulin, thyroxine और oestrogen animal hormones हैं, इसलिए plant-hormone MCQ में cytokinin चुनें।
amylase|5|Salivary amylase/ptyalin saliva में starch breakdown शुरू करता है। यह fat emulsification नहीं करता; fat पर bile और lipase-related processes अलग हैं।
alkyne|4|एक triple bond वाले acyclic alkyne की general formula CₙH₂ₙ₋₂ है। Example ethyne C₂H₂; cyclic/multiple-unsaturation compounds पर formula बिना जाँच न लगाएँ।
waste|13|Discarded unwanted material waste है। Source segregation, reduce/reuse और suitable recycling/composting useful methods हैं। E-waste/batteries organic compost में न मिलाएँ।
backdominant|8|Monohybrid complete-dominance model में F₁ Tt × homozygous dominant TT से TT तथा Tt 1:1 genotype ratio। दोनों tall, इसलिए phenotype सभी dominant (1:0)। Reciprocal cross में sexes की parental roles interchange होती हैं; वह backcross का synonym नहीं।
backtest|8|Backcross F₁ को किसी parent-type से cross करना है। Testcross unknown dominant phenotype को homozygous recessive से cross करता है; Tt×tt से expected 1:1, TT×tt से सभी dominant। Testcross backcross का special case हो सकता है।
arrhenius|2|Arrhenius acid aqueous H⁺/H₃O⁺ बढ़ाता है, जैसे HCl; base OH⁻ बढ़ाता है, जैसे NaOH। NaOH+HCl→NaCl+H₂O neutralisation है। सभी hydrogen compounds aqueous acids नहीं।
neutralisation|2|Acid और base से salt और सामान्यतः water बनना neutralisation है। HCl+NaOH→NaCl+H₂O balanced example है।
heart|5|Heart circulatory system का pump है। Chambers blood को lungs और body circuits में भेजते हैं; यह kidney की तरह metabolic-waste filtration organ नहीं।
iodine|6|Thyroid को thyroxine बनाने के लिए iodine आवश्यक है। Thyroxine metabolic regulation में भूमिका निभाता है; iodine gland या hormone का नाम नहीं है।
medulla|6|इस board MCQ का अपेक्षित विकल्प medulla है, जो breathing, blood-pressure-related responses, salivation/vomiting जैसे involuntary functions में काम करता है। ‘सभी involuntary actions केवल medulla’ वैज्ञानिक रूप से अत्यधिक व्यापक कथन है।
nocryswater|2|NaHCO₃ यानी baking soda में formula-bound water of crystallisation नहीं। Washing soda decahydrate, gypsum dihydrate और POP hemihydrate हैं।
potassium|3|दिए K, Ag, Cu, Pb विकल्पों में K soft और cold water से vigorous reaction करता है। Alkali metals को lab में carefully handle करते हैं; यह self-experiment निर्देश नहीं।
reflectionall|9|Reflection laws plane, concave और convex mirrors सभी के हर local surface point पर लागू हैं। Normal curved surface पर local perpendicular के अनुसार खींचें।
chargeunit|11|Electric charge का SI unit coulomb (C) है। Current ampere, potential difference volt और resistance ohm में मापते हैं।
feedback|6|Feedback mechanism hormone release के time/amount को regulate कर सकता है। उदाहरण blood glucose बढ़ने से insulin stimulus बढ़ता, glucose घटने पर stimulus कम होता है।
impulse|6|Nervous tissue में electrical/electrochemical impulses messages transmit करते हैं; chemical synapses पर neurotransmitter crossing होती है। पूरे pathway को केवल chemical diffusion न कहें।
energyloss|13|Trophic transfer पर usable energy घटती है; respiration/heat/activities में losses होते हैं। लगभग 10% next level transfer school estimate है, सभी ecosystems में exact constant नहीं।
tungsten|11|Filament incandescent bulbs में tungsten उपयोगी है क्योंकि melting point बहुत ऊँचा और heating पर incandescence मिलती है। यह modern LED का filament होने का दावा नहीं।
aba2|6|ABA growth-inhibiting plant hormone है। इसे abscisic acid कहते हैं; gibberellin growth-promoting और cytokinin division-promoting भूमिकाओं से अलग रखें।
cerebellum|6|Cerebellum posture, balance तथा precise movement में मदद करता है। Walking straight/riding bicycle coordination के ऐसे examples हैं।
rryy|8|Complete dominance के pea model में RrYy phenotype round और yellow है। R round, Y yellow dominant; genotype heterozygous होने पर recessive traits hidden हो सकते हैं।
silvercorrosion|3|Silver की environmental black coating corrosion/tarnishing है; sulfur compounds के साथ Ag₂S बन सकता है। इसे fat rancidity या metal का केवल melting न कहें।
activityAl|3|Ascending reactivity: Fe < Zn < Al। Activity-series position displaced metal और reaction tendency के school predictions में उपयोगी है।
ester|4|Ethanoic acid+ethanol से CH₃COOC₂H₅ (ethyl ethanoate) और water बनते हैं, acid catalyst/heat सहित। Ester का group –COO– है; ether option सही नहीं।
clones|7|Vegetative offspring सामान्यतः parent जैसे genetically similar/clone होते हैं। DNA copying में mutations संभव हैं; ‘हर molecule बिल्कुल समान’ absolute claim से बचें।
biodegradable|13|Biological processes द्वारा breakdown होने वाले substances biodegradable हैं। Suitable conditions/समय चाहिए; biodegradable का अर्थ तत्काल harmless नहीं।
repel|12|Like magnetic poles repel, unlike poles attract। Field-direction rules और poles के attraction को current direction का synonym न बनाएं।
vinegar|4|Vinegar का प्रमुख characteristic acid ethanoic/acetic acid, CH₃COOH है। Dilute vinegar और pure glacial acetic acid की concentration अलग है।
abiotic|13|Water, sunlight या temperature ecosystem का abiotic component है। Plants/animals/bacteria biotic components हैं।
nolinescross|12|एक point पर field की unique direction है। Two field lines crossing करें तो दो tangents/directions मिलेंगी; इसलिए magnetic field lines intersect नहीं करतीं।
thyroid|6|Thyroid gland thyroxine के द्वारा metabolism regulate करती है और growth/development में सहयोग देती है। इसे pituitary growth hormone के सीधे नाम से न बदलें।
planaria|7|Planaria में suitable fragments regeneration से पूरा organism बना सकते हैं। Leishmania binary fission, Plasmodium multiple fission और Hydra budding के standard examples हैं।
excretion|5|Kidneys excretory system का भाग हैं; blood से filtrate, selective reabsorption तथा secretion के बाद urine बनता है। Nutrition, breathing और excretion अलग functions हैं।
genotypic|8|Tt×Tt से TT,Tt,Tt,tt; expected genotype ratio 1:2:1। Complete dominance का phenotype ratio 3:1 है। दोनों को swap न करें।
producer|13|Photosynthetic producers solar energy को organic compounds में fix करते हैं, जो heterotrophs को food-chain transfer से उपलब्ध होती है। Primary consumers स्वयं producers नहीं।
radius|9|Paraxial spherical mirror में R=2f अथवा f=R/2। Radius of curvature तथा focus distance समान units और signs में रखें।
redleast|10|Ordinary glass prism में red light least और violet greatest deviation देती है। Wavelength-dependent refractive index dispersion का कारण है।
silverconduct|3|दिए iron/aluminium/copper/silver विकल्पों में silver सबसे अच्छा electrical conductor है। Practical wires में cost, ductility और other factors से copper useful है।
pbredox|1|2PbO+C→2Pb+CO₂ में carbon oxidised और PbO reduced होता है। Product CO₂ को फिर oxidised reactant कहना गलत है।
phosphorus|3|Phosphorus atomic number 15 का shell distribution 2,8,5 है; M shell में 5 electrons। यह electronic configuration का प्रश्न है।
ethane|4|दिए C₂H₂,C₂H₄,C₂H₆,C₆H₆ विकल्पों में ethane C₂H₆ saturated acyclic hydrocarbon है; C–C single bond है।
methanebonds|4|Methane CH₄ में चार C–H covalent single bonds हैं। Carbon चार pairs share करके octet, हर H duplet पूरा करता है।
pancreas|6|Pancreas insulin सहित hormones से blood glucose regulation में भूमिका निभाता है। Thyroid metabolism और adrenal acute-stress responses से अलग हैं।
leishmania|7|दिए options में Leishmania binary fission करता है, सामान्यतः longitudinal orientation में। Amoeba भी binary fission का example है, लेकिन यहाँ source options में Leishmania है।
mitochondria|5|Aerobic pyruvate breakdown mitochondrial pathways में CO₂, water और usable energy देता है। Glycolysis cytoplasm में pyruvate बनाती है; दोनों stages अलग हैं।
asexualone|7|School definition में asexual reproduction एक parent से होती है; gamete fusion नहीं। Offspring में occasional variation फिर भी संभव है।
decomposer|13|इस MCQ में microbes की अपेक्षित प्रमुख भूमिका decomposers है; bacteria/fungi dead organic matter breakdown तथा nutrient recycling में काम करते हैं। सभी microorganisms केवल decomposer हैं, ऐसा universal statement नहीं।
biomag|13|Persistent pesticide concentration का higher trophic levels पर बढ़ना biomagnification है। Individual में time-based buildup bioaccumulation है; food-chain energy बढ़ना नहीं।
twinkle|10|Stars की twinkling changing atmospheric refractive index से apparent brightness/position fluctuations है। Point-like source होने से effect prominent है; यह prism dispersion नहीं।
ampere|11|Electric current का SI unit ampere (A), 1 A=1 C/s है। Coulomb charge और joule energy की units हैं।
insidefield|12|Bar magnet के भीतर field lines south→north, बाहर north→south हैं; मिलकर closed loops बनती हैं।
quicklime|2|Quicklime calcium oxide CaO है; slaked lime Ca(OH)₂। CaO+H₂O→Ca(OH)₂ heat-releasing combination है।
febalance|1|3Fe+4H₂O(steam)→Fe₃O₄+4H₂ में Fe coefficient 3 है। Fe 3, H 8, O 4 atoms दोनों sides पर equal हैं।
sodiumwater|3|दिए Na,Ag,Fe,Mn विकल्पों में sodium cold water से vigorous H₂ evolution देता है: 2Na+2H₂O→2NaOH+H₂।
activityMg|3|Decreasing reactivity Mg > Zn > Fe है। Metals के activity-series क्रम के अनुसार अधिक active metal lower metal को suitable salt solution से हटा सकती है।
carboxyl|4|Carboxylic acid का functional group –COOH है। Alcohol –OH, aldehyde –CHO और ketone >C=O से इसे अलग रखें।
atomicH|3|Hydrogen atomic number 1 है, यानी nucleus में एक proton। Atomic number को isotope mass number से न मिलाएँ।
lifeprocesses|5|Nutrition, respiration, transport, excretion जैसे collective maintenance functions life processes हैं। Reproduction species continuity के लिए है, individual maintenance की immediate शर्त नहीं।
foodvacuole|5|Amoeba pseudopodia से food engulf करके food vacuole बनाता है। Vacuole में digestion और आगे nutrients का उपयोग होता है।
mendel|8|Gregor Mendel ने pea crosses से trait inheritance के महत्वपूर्ण rules निकाले। Dominance, segregation तथा suitable traits में independent assortment को अलग समझें।
chloride|2|HCl aqueous dissociation का anion chloride, Cl⁻ है। Cation का school representation H⁺/hydronium है; Cl₂ molecule नहीं बनता।
pituitary|6|दिए विकल्पों में pituitary gland growth hormone से growth stimulate करती है। Board stem ‘all organs’ simplified है; actual tissue responses एवं अन्य hormones भी भूमिका रखते हैं।
hydra|7|Hydra budding से asexual reproduction करता है; parent body पर outgrowth mature होकर नया individual बनता है।
xylem|5|Xylem roots से water तथा dissolved minerals transport करता है। Phloem photosynthates का source–sink transfer करता है।
plastic|13|दिए examples में conventional plastic non-biodegradable है; persistent waste अलग collect/recycle करें। सभी types/material formulations की degradation समान नहीं होती।
halfR|11|Same material, area और temperature पर R=ρl/A। Length half होने पर resistance half, resistivity unchanged होती है।
volt|11|Potential difference की SI unit volt (V) है: 1 V=1 J/C। Current ampere और charge coulomb है।
attract|12|Unlike poles attract; like poles repel। समान strength के bar magnets होने से यह polarity rule बदलता नहीं।
lactic|2|Curd में मुख्य school-level characteristic acid lactic acid है। Lactic, tartaric, oxalic तथा methanoic acids अलग नाम/formulas रखते हैं।
copperheat|3|दिए copper,lead,mercury,zinc विकल्पों में copper heat का best conductor है। उत्तर source के विकल्पों के सापेक्ष है; silver को विकल्पों से बाहर जोड़कर चयन न करें।
ketone|4|Ketone का carbonyl group >C=O दो carbon-containing groups के बीच होता है। Aldehyde में –CHO और acid में –COOH है।
guard|5|Guard cells के turgor changes stomatal aperture खोलते/बंद करते हैं। Chloroplast, xylem और phloem को pore-control cells न कहें।
bisexual|7|जिस flower में stamen और pistil दोनों हों, वह bisexual flower है। Hibiscus और mustard standard examples हैं; bisexual होना self-pollination की guarantee नहीं।
xy|8|XX–XY school model में typical male sex chromosomes XY हैं। X/Y gametes से outcome probability समझते हैं; real biological variation को इस simplified answer में universal exclusion न मानें।
snell|9|Given sin i=a और sin r=b तो relative refractive index μ=a/b है, fixed media/wavelength और valid oblique incidence के लिए। Normal incidence के 0/0 को सीधे ratio न निकालें।
earlysun|10|Atmospheric refraction sun की apparent position ऊपर shift कर सकती है; sunrise advance और sunset delay visible होते हैं। यह reflection या scattering मात्र नहीं।
earth|12|Earth wire exposed metal body को protective low-resistance fault path देता है। Suitable protection fault पर disconnect कर सकती है; earth सामान्य working return current path नहीं।''')

answers('''mirrormag|9|Spherical mirror magnification m=hᵢ/hₒ=−v/u। New Cartesian signs लें; m<0 inverted और m>0 erect image दर्शाता है।
mirrorerect|9|Concave mirror object को pole और focus के बीच रखने पर erect, enlarged virtual image देता है। Convex mirror finite real object की erect लेकिन diminished image देता है।
currentformula|11|Current I=Q/t। Q coulomb और t second में लेने पर I ampere मिलता है; 1 A=1 C/s।
voltageformula|11|Potential difference V=W/Q। W joule और Q coulomb में होने पर V volt; 1 V=1 J/C।
insulin|6|Pancreas insulin देता है; blood glucose regulation तथा uptake/storage में सहायता करता है। इसकी deficiency diabetes mellitus से जुड़ सकती है। सभी diabetes के cases केवल पूर्ण insulin absence से नहीं होते।
fieldprops|12|Field lines closed loops: बाहर N→S, अंदर S→N। Tangent local direction, close spacing stronger field; lines intersect नहीं करतीं। Diagram arrows और poles दोनों label करें।
strength|2|Strong acid जल में अधिक/लगभग पूर्ण ionisation, weak acid आंशिक ionisation करता है। HCl strong और ethanoic acid weak उदाहरण हैं। Strength तथा concentration अलग धारणाएँ हैं।
graphRA|11|Same material, length और temperature पर R=ρl/A, इसलिए R∝1/A। R vertical और A horizontal पर decreasing hyperbola; R बनाम 1/A plot linear है। Axes labels जरूरी हैं।
thermalelectrical|1|Thermolysis heat से decomposition, जैसे CaCO₃→CaO+CO₂। Electrolysis electrical energy से decomposition, जैसे 2H₂O→2H₂+O₂। Energy source तथा उदाहरण तुलना-बिंदु हैं।
ovary|7|Female primary reproductive organs ovaries हैं; ova तथा reproductive hormones बनाती हैं। Oviduct transport/fertilisation और uterus implantation/development से जुड़े हैं।
dominance|8|TT×tt से F₁ Tt सभी tall: heterozygote में T expressed, t hidden है। F₁ selfing में phenotype 3:1। Mendel rules trait transmission की predictions और recessive allele के फिर प्रकट होने को समझाते हैं। Dominant का अर्थ श्रेष्ठ नहीं।
geneticdiversity|8|Same species के individuals/populations में hereditary genetic differences genetic diversity हैं। Alleles तथा genotypes में variation इसके आधार हैं; सभी differences केवल training से acquired नहीं।
headrear|9|School optics में headlight reflector concave, source near focus से roughly parallel beam देता है। Rear-view convex wide field तथा erect diminished virtual image देता है। Modern lamp designs अलग हो सकती हैं; उत्तर prescribed optical model का है।
methane|4|Marsh gas methane CH₄ है। Structural diagram में central C से चार H single bonds लगाएँ; electron-dot form में चार shared pairs। इसे CH₃ radical या ethene न लिखें।
magnesia|2|Milk of magnesia में magnesium hydroxide Mg(OH)₂ होता है। यह अतिरिक्त stomach acid neutralise करता है: Mg(OH)₂+2HCl→MgCl₂+2H₂O। यह chemical principle है, dose/self-treatment निर्देश नहीं।
excretiondef|5|Metabolic wastes को body से हटाना excretion है, जैसे nitrogenous wastes urine में। Undigested food का removal egestion है; waste की उत्पत्ति दोनों में अलग है।
fruit|7|Flower का ovary fertilisation के बाद सामान्यतः fruit में विकसित होता है; ovules seeds बनते हैं। Seedless/parthenocarpic examples के कारण ‘हर fruit में fertilisation अनिवार्य’ absolute न जोड़ें।
magnification|9|Linear magnification image height/object height, m=hᵢ/hₒ। Mirror में −v/u और lens में v/u। Magnitude relative size, sign orientation दर्शाता है।
positiveimage|9|Positive magnification का अर्थ erect image है। Standard concave-mirror real-object school case में ऐसी image virtual होती है और object P–F के बीच है। Positive का अर्थ अनिवार्य larger नहीं।
synapse|6|दो neurons का functional junction synapse है; chemical synapse में छोटा synaptic cleft और neurotransmitter-mediated signalling होती है। इसे axon के भीतर की लंबाई न कहें।
propaneB|4|Propane C₃H₈ में 8 C–H तथा 2 C–C single bonds, total 10 covalent bonds हैं। Atom count 11 होने से bond count 11 नहीं हो जाता।
no2|1|Lead nitrate thermal decomposition: 2Pb(NO₃)₂→2PbO+4NO₂+O₂। Nitrogen-containing brown gas NO₂ है, N₂ नहीं।
bromine|3|दिए sulfur,bromine,iodine में bromine room temperature पर liquid nonmetal है। Mercury liquid metal है; दोनों को न बदलें।
propyne|4|CH₃–C≡CH का नाम propyne/prop-1-yne है। तीन carbon और terminal triple bond; suffix -yne प्रयोग करें।
dwarf|8|TT×tt के F₁ selfing model में F₂ dwarf tt की expected proportion 1/4=25%। Actual small sample count ratio से भिन्न हो सकता है।
lensformula|9|Thin lens formula 1/f=1/v−1/u। Lens magnification v/u; mirror formula में plus और magnification में minus होता है।
consumer|13|Deer/grasshopper जैसे herbivores consumers हैं; plants producers। Consumer अन्य organisms/organic food पर निर्भर होता है, trophic position diet से बदल सकती है।
naturalforest|13|दिए garden,crop-field,aquarium,forest विकल्पों में forest natural ecosystem है। Other listed examples human-created/managed हैं; सभी forests आज बिना human influence हों, ऐसा दावा नहीं।
agclgas|1|2AgCl→2Ag+Cl₂ (sunlight)। Gas chlorine है; धूसर appearance silver बनने से है।
gastricpH|2|Source options में gastric juice का pH लगभग 1.2 है, यानी strongly acidic। यह school typical value है; actual physiological measurements vary कर सकती हैं।
aluminium|3|Al atomic number 13 के shell electrons 2,8,3; M shell में 3 हैं। Shell electron count को isotope mass number से न मिलाएँ।
butaneB|4|Butane C₄H₁₀ में 10 C–H तथा 3 C–C single bonds, total 13 covalent bonds हैं। Branching isomer में भी total single-bond count समान हो सकता है।
limestone|2|Limestone का प्रमुख school formula calcium carbonate CaCO₃ है। Quicklime CaO और slaked lime Ca(OH)₂ हैं।
feoxidecoef|1|3Fe+4H₂O→Fe₃O₄+4H₂। Fe₃O₄ coefficient 1, Fe coefficient 3 और H₂ coefficient 4 है। दिए compound को पहचानकर उत्तर दें।
nitricMg|3|दिए Ag,Mg,Au,Pt में Mg बहुत dilute HNO₃ से H₂ दे सकता है। Nitric acid सामान्यतः oxidising होने से सामान्य H₂ evolution rule की exception है; dilute condition अनिवार्य है।
activityMAF|3|Decreasing reactivity Mg > Al > Fe। केवल alphabetical order या atomic number से activity क्रम न निकालें।
aldehyde|4|Aldehyde group –CHO है: terminal carbonyl carbon से hydrogen जुड़ा है। Ketone >C=O और carboxylic acid –COOH अलग हैं।
nitrogen|3|Nitrogen atomic number 7 है, nucleus में सात protons। Neutral atom में electrons भी सात; mass number अलग quantity है।
plasma|5|Blood का fluid medium plasma है। इसमें blood cells suspended और dissolved substances transported होते हैं; RBC pigment haemoglobin plasma का नाम नहीं।
chromosomes|8|Typical human somatic cells में 23 chromosome pairs (46 total) होते हैं। Gametes में 23 single chromosomes होते हैं; pairs और total न मिलाएँ।
acetate|4|CH₃COOH के aqueous ionisation का anion CH₃COO⁻, acetate/ethanoate है। Acid weak होने से ionisation partial होता है; anion का charge −1।
tartaric|2|Tamarind का characteristic school-level acid tartaric acid है। Orange का citric और curd का lactic acid इससे अलग हैं।
gold|3|दिए mercury,lead,gold,sodium विकल्पों में gold अत्यंत ductile है। Ductility तार बनाने और malleability sheet बनाने का गुण है।
lungs|5|Lungs respiratory system के organs हैं; alveoli gas exchange देते हैं। Cellular respiration का पूरा chemical breakdown केवल lungs में नहीं होता।
redwavelength|10|दिए yellow,red,violet,green में red की wavelength सबसे अधिक है। Ordinary prism में red कम deviation और small-particle scattering भी comparatively कम करता है।
allotropes|4|Diamond और graphite carbon के crystalline allotropes हैं। Atomic element same, bonding/structure अलग; graphite conductor जबकि diamond सामान्यतः electrical insulator है।
segregation|8|Tt organism gamete बनाते समय allele pair अलग करता है, इसलिए gametes T या t हैं। Tt×Tt में TT:Tt:tt=1:2:1 expected। Dominant allele होने पर भी recessive allele gamete तक जा सकता है।
modernperiodic|0|पुराने पाठ्यक्रम का प्रश्न: elements के physical/chemical properties उनके atomic numbers की periodic function हैं। Atomic number arrangement का आधार है, atomic mass नहीं।
q300|11|Q=300 C; t=5 min=300 s। I=Q/t=300/300=1 A। Minute को second में बदले बिना 60 A निकालना गलत है।
lamps100|11|दोनों rated bulbs 220 V पर parallel: total P=60+40=100 W। I=P/V=100/220=5/11 A≈0.455 A। यह total current है, किसी एक bulb का नहीं।
bulbs11|11|School ideal rating: maximum power VI=220×5=1100 W। Each bulb 100 W, इसलिए 1100/100=11 bulbs। Real circuit design में safety margins/inrush/अन्य loads जाँचे जाते हैं; इसे installation instruction न मानें।
q025|11|I=0.25 A; t=20 min=1200 s। Q=It=0.25×1200=300 C। Electric charge unit coulomb है, ampere-hour को बिना conversion न लिखें।
iron840|11|P=840 W,V=220 V। I=P/V=42/11≈3.82 A। R=V²/P=48400/840=1210/21≈57.62 Ω। P=VI तथा V/I से दो checks करें।
bill576|11|P=600 W=0.6 kW; t=8×30=240 h। E=0.6×240=144 kWh। Rate ₹4/kWh पर charge ₹576; fixed fees/taxes शामिल नहीं।
power110|11|V=220 V,I=0.5 A। P=VI=110 W। यदि resistance भी चाहिए तो R=V/I=440 Ω।
q30|11|I=1 A,t=30 s। Q=It=30 C। Current प्रति second charge flow है; I तथा Q अलग quantities हैं।
power2|9|f=0.5 m। P=1/f=2 D; given positive focal length school model में +2 D। यदि lens type/sign न दी हो तो power sign के लिए convention स्पष्ट करें।
speed2|9|n=1.5,c=3×10⁸ m/s। v=c/n=2×10⁸ m/s। Refractive index dimensionless और speed की unit m/s है।
res4|11|दो readings: R=2/0.50=4 Ω और R=3/0.75=4 Ω। Constant V/I ohmic relation का support है, assuming temperature stable।
heat5184|11|V=12 V,R=25 Ω,t=15 min=900 s। H=V²t/R=144×900/25=5184 J। I=0.48 A लेकर I²Rt से भी यही result।
qsmall|11|4 mA=0.004 A,t=0.05 s। Q=It=0.0002 C=2×10⁻⁴ C। Milli-prefix तथा decimal दोनों सही convert करें।
heat4320|11|V=6 V,R=30 Ω,t=1 h=3600 s। H=V²t/R=36×3600/30=4320 J। Current 0.2 A है; hour को second में बदलें।
waterSpeed|9|n=1.33,c≈3×10⁸ m/s। v=c/n≈2.26×10⁸ m/s। Medium में speed कम है; n को c से multiply करना गलत।
half5|11|P resistance=5 Ω और Q resistivity=8×10⁻⁴ Ω·m। Length half, same A/material/temperature में P=2.5 Ω; Q unchanged 8×10⁻⁴ Ω·m।
double3|11|A=3 Ω resistance और B=7×10⁻⁵ Ω·m resistivity। Length double, area/material/temperature same: A=6 Ω, B unchanged। Units से quantities पहचानें।
plane6|9|Object mirror से 3 m, virtual image mirror के पीछे 3 m। Object–image separation=3+3=6 m। Mirror से image distance और object से image distance अलग हैं।
plane10|9|Object plane mirror से 5 m, image पीछे 5 m। Total object–image distance 10 m। Plane mirror magnification +1, size same है।
seriesR2|11|Source diagram में series total current 2 A और voltage 12 V: Rtotal=12/2=6 Ω। Known resistor 4 Ω हटाने पर unknown R=2 Ω।
voltage12|11|Work 24 J तथा charge 2 C। V=W/Q=24/2=12 V। Volt joule प्रति coulomb है।
forceup|12|Positive charge west velocity और north force के लिए B upward है: v×B दिशा north होनी चाहिए। Electron/negative charge हो तो force direction opposite होती।
propene|4|CH₃–CH=CH₂ अथवा CH₂=CH–CH₃ का IUPAC नाम propene है। तीन carbon, one double bond; suffix -ene।
energyunit|11|1 kWh=3.6×10⁶ J और यह electric energy की unit है। kW power, kWh energy; 1 hour=3600 seconds।
mechanics60|0|पुराने mechanics पाठ्यक्रम: W=ΔK=½m(v²−u²)=½×40×(4−1)=60 J। यह current 13-chapter core का topic नहीं; historical practice label रखें।
spring08|0|पुराना mechanics: x=2 cm=0.02 m। E=½kx²=½×4000×0.02²=0.8 J। Centimetre को metre में convert करना जरूरी है।
mechanics1500|0|पुराना mechanics: W=½×40×(10²−5²)=20×75=1500 J। Work–energy theorem उपयोग होता है, current core scope से अलग।
force20|0|पुराना mechanics: maximum aligned work W=Fs। F=200/10=20 N। Angle 0° होने की maximum-work condition महत्वपूर्ण है।''')

answers('''electronredox|1|Electron concept में oxidation electron loss, reduction electron gain है। Zn→Zn²⁺+2e⁻ तथा Cu²⁺+2e⁻→Cu; net Zn+Cu²⁺→Zn²⁺+Cu। दोनों half-reactions में electron संख्या समान रखकर जोड़ें।
bioenzyme|5|Salivary amylase starch को छोटे carbohydrate products में hydrolyse करना शुरू करता है। Enzyme biological catalyst है; reaction में rate बढ़ाता है और खुद स्थायी रूप से consumed नहीं होता।
poponly|2|Plaster of Paris calcium sulfate hemihydrate, CaSO₄·½H₂O है। Water मिलाने पर gypsum बनकर hardens, इसलिए casts/moulds में उपयोगी। Gypsum का formula CaSO₄·2H₂O अलग है।
seriesderive|11|Series में same I और V=V₁+V₂+V₃। Ohm law से V=I(R₁+R₂+R₃)=IRₛ, इसलिए Rₛ=R₁+R₂+R₃। Circuit में resistors एक successive path में दिखाएँ, branches नहीं।
cfc|13|CFC का full form chlorofluorocarbon है। इनमें carbon, chlorine और fluorine वाले compounds शामिल हैं; कुछ CFCs stratospheric ozone depletion में भूमिका निभाते हैं।
citric|2|Orange का characteristic school-level acid citric acid है। Tamarind tartaric और curd lactic acid examples हैं; fruit sample में कई acids मौजूद हो सकते हैं।
h2coef|1|Balanced reaction 3Fe+4H₂O(steam)→Fe₃O₄+4H₂। Asked H₂ coefficient 4 है; Fe coefficient 3 को answer न लिखें।
tallround|8|Mendel pea model में tall stem और round seed dominant traits हैं। Dwarf तथा wrinkled recessive; dominance heterozygote expression है, trait की श्रेष्ठता नहीं।
snellcd|9|Given sin i=c,sin r=d तो relative index μ=c/d। Fixed media/wavelength की Snell relation प्रयोग करें; c को यहाँ vacuum speed symbol न मानें क्योंकि source में यह sine value का label है।
foodweb|13|Branching/interconnected food chains का network food web है। One organism कई food sources/predators से जुड़ सकता है; arrows transfer source से recipient तक हों।
coilstrength|12|Same geometry/current में turns बढ़ने पर loop/coil का combined magnetic field बढ़ सकता है। Individual turns का field contribution add होता है; current, core और dimensions भी महत्त्वपूर्ण हैं।
voltmeter|11|Voltmeter potential difference मापता है और measured component के parallel लगता है। Ammeter current के लिए series है; instruments के connections swap न करें।
slakedlime|2|CaO+H₂O→Ca(OH)₂+heat। Product calcium hydroxide/slaked lime है। Quicklime CaO reactant है; lime water aqueous Ca(OH)₂ होता है।
acidconduct|2|Aqueous acids mobile ions बनाते हैं, जिनसे electrical conduction और bulb glow हो सकती है। H₃O⁺ तथा counter-anions charge ले जाते हैं; सभी H-containing molecules acids नहीं।
alimentary|5|Alimentary canal digestive system का भाग है: food passage, digestion और nutrient absorption से जुड़ा है। Excretory urinary tract से इसकी संरचना अलग है।
electromagnet|12|Current-carrying coil, प्रायः suitable soft-iron core सहित, temporary electromagnet बना सकती है। Current off/reverse से strength/polarity control हो सकती है। यह permanent bar magnet का identical construction नहीं।
fuse|12|Excess current से suitable fuse element heats और melts होकर circuit खोलता है। Correct current rating तथा live conductor placement जरूरी हैं; fuse को मोटे साधारण wire से replace न करें।
znredox|1|ZnO+C→Zn+CO में ZnO oxygen खोकर reduced और carbon oxygen पाकर oxidised होता है। ZnO oxidising agent, carbon reducing agent। दोनों transformations एक साथ होने से यह redox है।
enzymes|5|Salivary amylase starch breakdown, stomach pepsin protein digestion और pancreatic/intestinal enzymes आगे digestion करते हैं। Lipase fat breakdown करता है; bile emulsification करता है लेकिन enzyme नहीं। Enzymes reaction-specific biological catalysts हैं।
spheremirrors|9|Spherical mirror का reflecting surface sphere के भाग जैसा है। Concave inward surface, convex outward surface। Real image actual rays की intersection से screen पर मिलती है; virtual image backward extensions का apparent intersection है।''')

QUESTIONS=[]
def paper(paper_id,text):
    for line in text.strip().splitlines():
        ref,page,marks,key,prompt=line.split('|')
        assert key in ANSWERS,key
        QUESTIONS.append(dict(paper=paper_id,ref=ref,page=int(page),marks=marks,key=key,prompt=prompt))

# Prompts summarise the selected subquestion; the linked paper preserves exact wording.
paper('2014_main','''2|2|1|neutral|उदासीन विलयन का pH।
3|2|1|formic|चींटी के डंक का अम्ल।
4|3|1|multiple|Plasmodium का विखंडन।
5|3|1|ozonecause|ओजोन गिरावट का प्रमुख कारण।
7|3|1|overload|एक socket पर बहुत उपकरण।
9(a)|4|1|redox|एक redox उदाहरण।
9(b)|4|1|electrolysis|जल विद्युत-अपघटन का विन्यास।
11|4|2|photo|Photosynthesis के दो events।
13|4|2|vegetative|कायिक जनन और लाभ।
14(i)|4|1|darksky|Astronaut को dark sky क्यों?
14(ii)|4|1|iris|Pupil का नियंत्रण।
15(a)|5|1|zincalkali|Zn–NaOH गैस और समीकरण।
15(b)|5|2|saltsuses|चार दैनिक उपयोग के रसायन।
16(a)|5|1|displacement|विस्थापन की परिभाषा।
16(b)(i)|5|1|znso4|Zn–CuSO₄ में missing product।
16(b)(ii)|5|1|baso4|Na₂SO₄–BaCl₂ का precipitate।
18|6|3|dialysis|कृत्रिम वृक्क का उपयोग।
19|6|3|budding|Hydra budding की अवस्थाएँ।
21|7|3|threeR|पर्यावरण के तीन R।
22|7|3|focusmirror|Concave focus, convex उपयोग।
23|7|3|ohm|Ohm नियम तथा verification।
25(b)|8|2|amphoteric|Amphoteric oxide का उदाहरण।
25(c)|8|1|brass|Brass के घटक।
26|8|5|foodenergy|Food chain और energy flow।
28(a)|9|1|covalent|Covalent bond का अर्थ।
30(c)|11|1|normalincidence|Normal incidence में दिशा।
8|3|1|q300|300 C, 5 min: current।
24|7|3|lamps100|60 W+40 W, 220 V: total I।''')

paper('2015_main','''1|2|1|indicators|दो synthetic indicators।
2|2|1|placenta|Embryo nutrition का interface।
4|2|1|phcompare|दो जोड़ों का pH compare।
5|2|1|overload|Overload से दो बचाव।
8|3|1|accommodation|Eye focal adjustment का नाम।
9|3|2|combdecomp|Combination/decomposition के examples।
11(a)|3|1|uv|Ozone किस radiation से बचाती है?
14|3|2|sexdetermination|XX–XY determination schematic।
15(a)|4|1|stomachacid|Stomach acid का कार्य।
15(b)|4|2|nutrition|दो nutrition modes में अंतर।
16(b)|4|2|nervoushormonal|Nerve और hormone control।
17|4|3|redox|CuO–H₂ redox तथा दूसरा उदाहरण।
18|4|3|spheremirrors|Mirrors और image types तुलना।
19(b)|4|2|insulinthyroxine|Insulin/thyroxine के functions।
20|4|3|dispersion|White-light separation का कारण।
21|4|3|fragmentregbud|तीन asexual modes तुलना।
23|5|3|zincacid|Zn–acid गैस और test।
24|5|3|slab|Air–glass–air ray path।
25(a)|5|3|ecosystem|Ecosystem components।
26(a)|5|1|mercury|Room-temperature liquid metal।
26(b,c)|5|4|mgcl2|MgCl₂ का electron transfer।
27(a)|5|2|left|Conductor force direction rule।
28(b), प्रथम विकल्प|6|2|doublecirculation|Double circulation की आवश्यकता।
28(b,c), दूसरा विकल्प|6|3|salivabile|Fat digestion और saliva।
29(a), प्रथम विकल्प|6|2.5|resistivity|Wire resistance तथा resistivity।
30(a), प्रथम विकल्प|7|3|homology|Homologous series के तीन गुण।
7|3|1|bulbs11|5 A fuse, 100 W bulbs संख्या।
13|3|2|q025|0.25 A, 20 min: charge।
29(b), दूसरा विकल्प|7|2.5|iron840|840 W, 220 V: I,R।''')

paper('2016_main','''1|2|1|bakingpowder|Baking powder के दो घटक।
2|2|1|vegetative|Seed-loss plants का propagation।
5|2|1|uniformfield|Uniform magnetic field का चित्र।
7|2|1|eastwest|East→west wire के नीचे field।
9|3|2|combdecomp|Quicklime–water combination।
15(a)|4|2|photo|Photosynthesis equation तथा घटनाएँ।
17|4|3|znredox|ZnO–carbon redox analysis।
18(a)|4|1|mirrormag|Mirror magnification formula।
18(b)|4|1|mirrorerect|Erect enlarged mirror पहचान।
19|4|3|reflex|Reflex arc और response।
20(i)|5|0.5|currentformula|Current का सही formula।
20(ii)|5|0.5|voltageformula|Potential difference formula।
20(iii)|5|0.5|ohm|Ohm relation मिलान।
20(iv)|5|0.5|resistivity|Resistivity relation मिलान।
21|5|3|menstruation|Unfertilised egg के बाद प्रक्रिया।
23|5|3|toothpH|Mouth pH और tooth decay।
25|5|5|foodenergy|Grassland chain तथा energy।
24|5|3|bill576|600 W fridge, 30 दिन: bill।''')

paper('2017_main','''1|2|1|rust|Iron rust के दो बचाव।
2|2|1|mgo|Mg combustion product।
6|3|1|nearpoint|Normal adult near point।
9|4|2|calcroast|Roasting–calcination अंतर।
11|4|2|dihybrid|Tall/round cross, F₂ ratio।
12|5|2|sexdetermination|Human sex-determination आधार।
13(a)|5|1|rearview|Vehicle rear-view mirror।
14|5|2|parallel|Household parallel का कारण।
15(a)|5|1.5|rancidity|Fat food oxidation रोकना।
15(b)|5|1.5|redox|CuO–H₂ में oxidation/reduction।
17(a)|6|1|metalproperties|दो metal properties।
17(b)|6|1|alloy|Alloy definition और examples।
17(c)|6|1|oxides|Metal/nonmetal oxides की प्रकृति।
18(a)|6|2|enzymes|Digestion में enzymes।
19|7|3|insulin|Pancreatic hormone और deficiency।
21|7|3|placenta|Placenta damage का प्रभाव।
22(a)|7|2|defects|Near-object defect और correction।
22(b)|7|1|tyndall|Tyndall mechanism।
23, नियम भाग|8|1|ohm|Ohm statement।
25(ii)|8|2|acidwater|Dilution का सुरक्षित क्रम क्यों?
25(iv)|8|1|chloralkali|Chlor-alkali process।
27(b)|9|2|fieldprops|Field-line representation के गुण।
13(b)|5|1|power110|220 V, 0.5 A: power।
24|8|3|q30|1 A, 30 s: charge।
30, प्रथम विकल्प अंतिम भाग|11|1|power2|f=0.5 m: lens power।
30, दूसरे विकल्प अंतिम भाग|11|1|speed2|n=1.5: light speed।''')

paper('2017_supplementary','''1|2|1|brass|Copper–zinc alloy।
4|3|1|metalproperties|दो metal गुण।
5|3|1|bisexual|Bisexual flower का अर्थ।
6|3|1|dispersion|White light dispersion।
7|3|1|lenspower|P–f संबंध।
9|4|2|bleachpop|Bleaching powder और POP उपयोग।
13(a)|5|1|rearview|Rear-view mirror।
14|5|2|fieldprops|Bar-magnet lines के गुण।
15(b)|5|1|strength|Strong/weak acid का आधार।
15(c)|5|1|crystalwater|Crystal water क्या है?
18(a)|6|2|salivabile|Saliva और bile के काम।
19(a)|7|2|aba|Growth-inhibiting hormone का प्रभाव।
19(b)|7|1|cytokinin|Division-promoting hormone।
22|7|3|defects|दो defects और corrective lenses।''')

paper('2018_main','''1|3|1|amylase|Salivary gland का enzyme।
3|3|1|alkyne|Alkyne general formula।
11|4|1|graphRA|Equal-length wires का R–A graph।
17(b)|5|1|thermalelectrical|Thermal/electrical decomposition अंतर।
21|6|3|waste|Waste तथा management के उपाय।
23, cross भाग|7|3|backdominant|F₁ × dominant parent के ratios।
24(a), formula भाग|7|-|bleachpop|Bleaching powder formula।
28(a), प्रथम विकल्प|9|1|respiration|Respiration की परिभाषा।
28(a), दूसरा विकल्प|10|1|ovary|Female primary sex organ।
4|3|1|energyunit|kWh को joules में।
25(a)|8|2|res4|दो V–I readings से R।
25(b)|8|2|heat5184|12 V,25 Ω,15 min: heat।
26(a)|9|2|mechanics60|40 kg,1→2 m/s: work।
26(b)|9|2|spring08|k=4000, x=2 cm: energy।''')

paper('2018_supplementary','''11|4|1|insidefield|Bar magnet field की दिशा।
15(b)|5|1|rearview|Vehicle mirror selection।
17(a)|5|1|displacement|Displacement का उदाहरण।
17(b)|5|1|neutralisation|Neutralisation का example।
17(c)|5|1|redox|Redox का example।
21, परिभाषा भाग|7|1|biodegradable|Biodegradable waste का अर्थ।
23, dominance भाग|7|2|dominance|Dominance उदाहरण।
24(a)|7|2|arrhenius|Arrhenius acid/base examples।
20(b)|6|1|propene|CH₂=CH–CH₃ का नाम।
25(b)|8|2|qsmall|4 mA,0.05 s: charge।''')

paper('2019_main','''7|3|1|geneticdiversity|Genetic diversity का अर्थ।
11|4|1|ohm|V–I graph का आकार।
15(b)|5|2|headrear|Headlight/rear-view mirror चयन।
17(a)|6|1|combdecomp|Carbon combustion और water splitting।
17(b)|6|1|combdecomp|दो reactions की तुलना।
20(b)|7|1|methane|Marsh gas structure।
23|8|4|dominance|Mendel dominance और उपयोगिता।
24(a)(i)|8|1|magnesia|Milk of magnesia antacid क्यों?
28(a), प्रथम विकल्प|9|1|excretiondef|Excretion का अर्थ।''')

paper('2020_main','''3|3|1|carbonfeatures|Catenation का अर्थ।
11|4|1|insidefield|Bar-magnet field sketch।
17(b)|5|1|neutralisation|Neutralisation example।
21|7|3|waste|Agricultural waste और disposal।
22(a)|7|1|fruit|Fruit की परिभाषा।
23|7|4|backtest|Backcross तथा testcross।
24(a)|7|1|bleachpop|Bleaching powder name/formula।
24(b)|7|1|arrhenius|Aqueous acids/bases theory।
28(a), प्रथम विकल्प|9|1|respiration|Respiration का अर्थ।
28(a), दूसरा विकल्प|9|1|sexhormones|Male प्रमुख sex hormone।
30(a), प्रथम विकल्प|11|1|magnification|Magnification की परिभाषा।
30(c), प्रथम विकल्प|11|1|positiveimage|Positive m की image nature।
20(a)(ii)|6|1|propene|CH₃–CH=CH₂ का नाम।
25|8|4|power110|220 V,0.5 A: R और P।
26(a)|8|2|mechanics1500|40 kg,5→10 m/s: work।
26(b)|8|2|force20|200 J,10 m: force।''')

paper('2020_supplementary','''3|3|1|allotropes|दो crystalline carbon forms।
11|4|1|thumb|Current-wire field direction rule।
17(a)|5|2|electronredox|Electron transfer से redox।
17(b)|5|1|bioenzyme|एक enzyme-driven reaction।
20(a)(2)|6|1|propyne|HC≡C–CH₃ का नाम।
21, परिभाषा भाग|6|1|plastic|Non-biodegradable waste का अर्थ।
23|7|4|segregation|Mendel segregation और example।
24(a)|7|1|poponly|Fracture plaster का compound।
24(c)|7|2|zincacid|Zn–H₂SO₄ reaction का विन्यास।
25(a)|8|2|seriesderive|तीन series resistors का equivalent।
25(b)|8|2|heat4320|6 V,30 Ω,1 h: heat।
26(b)|8|2|energyunit|एक commercial unit की energy।''')

paper('2022_main','''1(i)|2|1|heart|Heart किस organ system में?
1(iii)|3|1|iodine|Thyroxine का आवश्यक element।
1(iv)|3|1|medulla|Involuntary functions का brain भाग।
1(v)|3|1|nocryswater|किस salt में crystal water नहीं?
1(vi)|4|1|zincacid|Zn–dilute acid की gas।
1(vii)|4|1|potassium|Soft, cold-water-reactive option।
1(viii)|5|1|reflectionall|Reflection laws किन mirrors पर?
1(ix)|5|1|waterSpeed|n=1.33: water में light speed।
1(x)|5|1|chargeunit|Charge का SI unit।
2(i)|7|1|feedback|Hormone amount/time regulation।
2(ii)|7|1|impulse|Nerve message का प्रकार।
2(iii)|7|1|energyloss|Trophic transfer में energy।
2(v)|7|1|magnification|Lens v/u का अर्थ।
2(vi)|7|1|tungsten|Bulb filament का material।
3(i)|7|1|neuron|Nervous tissue का network।
3(ii)|7|1|pituitary|Growth-regulating endocrine gland।
3(iii)|8|1|cfc|CFC का expansion।
3(v)|8|1|threeR|Recycling का अर्थ।
3(vi)|8|1|citric|Orange का acid।''')

paper('2023_main','''1(i)|2|1|aba|Growth-inhibiting hormone।
1(ii)|2|1|cerebellum|Posture/balance का brain भाग।
1(iii)|3|1|rryy|RrYy का pea phenotype।
1(vii)|5|1|iris|Iris muscles का काम।
1(viii)|5|1|energyunit|kWh किस quantity की unit?
1(x)|6|1|silvercorrosion|Silver का black coating process।
1(xi)|6|1|activityAl|Al/Fe/Zn ascending activity।
1(xii)|6|1|ester|Acid+ethanol का ester।
2(i)|7|1|amylase|Saliva enzyme का नाम।
2(ii)|7|1|clones|Vegetative offspring की similarity।
2(iii)|7|1|biodegradable|Biological breakdown वाला material।
2(iv)|7|1|repel|Like magnet poles का effect।
2(v)|7|1|vinegar|Vinegar acid का नाम।
3(i)|8|1|feedback|Hormone action regulation।
3(ii)|8|1|multiple|Multiple-fission organism।
3(iv)|8|1|abiotic|एक abiotic component।
3(v)|8|1|half5|5 Ω wire half length: R,ρ।
3(vi)|8|1|nolinescross|Field lines क्यों नहीं cross?
3(vii)|9|1|solenoid|Coil के भीतर-बाहर field।
3(viii)|9|1|neutralisation|Neutralisation definition।
3(x)|9|1|redox|CuO–H₂ में reduced reactant।''')

paper('2024_main','''1(i)|2|1|febalance|Fe–steam reaction का Fe coefficient।
1(ii)|3|1|lactic|Curd का acid।
1(iii)|3|1|copperheat|दिए metals में best heat conductor।
1(iv)|3|1|ketone|Ketone का functional group।
1(v)|4|1|heart|Heart का organ system।
1(vi)|4|1|guard|Leaf pore का नियंत्रण।
1(vii)|4|1|pituitary|Growth-stimulating endocrine gland।
1(viii)|4|1|bisexual|Stamen+pistil वाला flower।
1(ix)|5|1|xy|Male sex chromosomes।
1(x)|5|1|plane6|3 m mirror distance: image separation।
1(xi)|5|1|snell|sin i=a,sin r=b: μ।
1(xii)|6|1|earlysun|Advance sunrise का mechanism।
1(xiv)|7|1|earth|Earth-wire protection का उद्देश्य।
1(xv)|7|1|thumb|Right-hand thumb का संकेत।
2(i)|7|1|no2|Lead nitrate की nitrogen gas।
2(ii)|7|1|chloride|HCl का anion।
2(iii)|7|1|propaneB|C₃H₈ covalent-bond count।
2(iv)|8|1|dialysis|Artificial-kidney waste removal method।
2(v)|8|1|synapse|Two neurons का junction।
2(vi)|8|1|magnification|hᵢ/hₒ का नाम।
2(vii)|8|1|defects|Hypermetropia का corrective lens।
3(i)|8|1|brass|Brass में copper का साथी।
3(ii)|8|1|bromine|S,Br,I में liquid nonmetal।
3(iii)|8|1|propyne|CH₃–C≡CH का नाम।
3(v)|9|1|medulla|Blood-pressure/salivation control।
3(vii)|9|1|dwarf|Mendel F₂ dwarf percentage।
3(viii)|9|1|lensformula|u,v,f का lens relation।
3(ix)|9|1|iris|Pupil-control eye part।
3(x)|9|1|consumer|एक ecosystem consumer।''')

paper('2024_supplementary','''1(i)|2|1|h2coef|Fe–steam का H₂ coefficient।
1(ii)|2|1|tartaric|Tamarind acid।
1(iii)|2|1|gold|दिए metals में maximum ductility।
1(iv)|3|1|carboxyl|Carboxylic-acid functional group।
1(v)|3|1|lungs|Lungs का organ system।
1(vi)|3|1|mitochondria|Pyruvate breakdown का organelle।
1(vii)|3|1|thyroid|Growth-metabolism regulation gland।
1(viii)|4|1|hydra|Budding organism का चयन।
1(ix)|4|1|tallround|Dominant pea traits का जोड़ा।
1(x)|4|1|plane10|5 m mirror distance: separation।
1(xi)|4|1|snellcd|sin i=c,sin r=d: μ।
1(xii)|5|1|redwavelength|Visible options में longest wavelength।
1(xiv)|6|1|parallel|Domestic appliance connection।
1(xv)|6|1|left|Fleming thumb का अर्थ।
2(i)|7|1|electrolysis|Water anode की gas।''')

paper('2025_main','''1(i)|2|1|thyroid|Metabolism-for-growth gland।
1(ii)|2|1|planaria|Regeneration वाला organism।
1(iii)|2|1|excretion|Kidney का organ system।
1(iv)|3|1|cytokinin|Plant hormone का चयन।
1(v)|3|1|genotypic|Monohybrid F₂ genotype ratio।
1(vi)|3|1|producer|Solar energy fixing organisms।
1(vii)|4|1|radius|Mirror R–f relation।
1(viii)|4|1|redleast|Prism में least deviation।
1(x)|5|1|silverconduct|दिए metals में best conductor।
1(xi)|5|1|thumb|Right-hand thumb direction।
1(xiii)|6|1|zincacid|Zn–dilute H₂SO₄ की gas।
1(xiv)|6|1|neutral|Neutral solution का pH।
1(xv)|6|1|pbredox|PbO–carbon के true redox statements।
1(xvi)|7|1|phosphorus|Phosphorus M-shell electrons।
1(xvii)|7|1|ethane|दिए formula में saturated hydrocarbon।
1(xviii)|7|1|methanebonds|CH₄ का covalent-bond count।
2(i)|7|1|feedback|Hormone action regulation।
2(ii)|7|1|foodweb|Branching food-chain network।
2(iv)|8|1|coilstrength|Coil turns बढ़ाने का effect।
2(v)|8|1|mgo|Burning magnesium का compound।
2(vi)|8|1|gold|Gold/iron में अधिक ductile।
3(i)|8|1|respiration|Respiration का अर्थ।
3(ii)|8|1|cerebellum|Precise body movement का भाग।
3(iii)|8|1|bisexual|एक bisexual flower।
3(v)|9|1|rearview|Vehicle rear-view mirror।
3(vi)|9|1|defects|Myopia का अर्थ।
3(vii)|9|1|voltmeter|Voltage मापने का यंत्र।
3(ix)|9|1|slakedlime|CaO–water का product।
3(xi)|10|1|carboxyl|Acid functional-group formula।
3(xii)|10|1|acidconduct|Aqueous acid में bulb glow।''')

paper('2025_supplementary','''1(i)|2|1|insulin|Blood-sugar hormone।
1(ii)|2|1|multiple|Multiple-fission option।
1(iii)|2|1|alimentary|Alimentary canal का system।
1(iv)|3|1|cytokinin|Plant cell-division hormone।
1(v)|3|1|genotypic|Monohybrid F₂ genotype types।
1(vi)|3|1|naturalforest|Natural ecosystem का चयन।
1(vii)|4|1|mirrorerect|Concave enlarged virtual image: object site।
1(viii)|4|1|accommodation|Lens focal change कराने वाली muscles।
1(ix)|5|1|seriesR2|12 V,2 A,4 Ω: unknown R।
1(x)|5|1|voltage12|24 J/2 C: voltage।
1(xii)|6|1|forceup|West-moving positive charge, north force।
1(xiii)|6|1|agclgas|AgCl photodecomposition की gas।
1(xiv)|7|1|gastricpH|Gastric-juice pH का चयन।
1(xv)|7|1|redox|CuO–H₂ true redox statements।
1(xvi)|7|1|aluminium|Aluminium M-shell electrons।
1(xviii)|8|1|butaneB|Butane covalent-bond count।
2(i)|8|1|iodine|Thyroxine synthesis का element।
2(ii)|8|1|decomposer|Complex organic waste breakdown organisms।''')

paper('2026_main','''1(i)|2|1|pancreas|Sugar-regulating endocrine gland।
1(ii)|2|1|leishmania|Binary-fission option।
1(iii)|2|1|mitochondria|Aerobic pyruvate breakdown स्थल।
1(iv)|3|1|asexualone|Asexual reproduction का parent count।
1(v)|3|1|decomposer|Microbes का food-chain role।
1(vi)|3|1|biomag|Pesticide concentration का trophic increase।
1(vii)|3|1|dispersion|Prism से white-light separation।
1(viii)|4|1|twinkle|Star twinkling का mechanism।
1(ix)|4|1|double3|Wire length double: R,ρ।
1(x)|4|1|ampere|Current की SI unit।
1(xi)|5|1|insidefield|Magnet के अंदर field direction।
1(xii)|5|1|left|Fleming-rule fingers मिलान।
1(xiii)|5|1|quicklime|Quicklime का formula।
1(xiv)|6|1|febalance|Balanced Fe coefficient।
1(xv)|6|1|sodiumwater|Cold-water H₂ देने वाला option।
1(xvi)|6|1|activityMg|Mg/Zn/Fe descending activity।
1(xvii)|7|1|carboxyl|Carboxylic-acid group।
1(xviii)|7|1|atomicH|Hydrogen atomic number।
2(i)|7|1|lifeprocesses|Collective maintenance processes का नाम।
2(ii)|7|1|foodvacuole|Amoeba food enclosure।
2(iii)|8|1|mendel|Inheritance rules के वैज्ञानिक।
2(v)|8|1|chloride|HCl का aqueous anion।
2(vi)|8|1|formic|Nettle का school-level acid।
3(i)|8|1|medulla|Blood-pressure/salivation/vomiting का brain भाग।
3(ii)|8|1|cytokinin|Plant division-promoting hormone।
3(iii)|8|1|dihybrid|Independent dihybrid F₂ ratio।
3(v)|9|1|uv|Ozone layer की आवश्यकता।
3(vii)|9|1|lenspower|Lens power का अर्थ।
3(viii)|9|1|electromagnet|Electromagnet की परिभाषा।
3(ix)|9|1|fuse|Circuit fuse का काम।
3(x)|9|1|zincacid|Zn–H₂SO₄ balanced equation।''')

paper('2026_supplementary','''1(i)|3|1|pituitary|Growth-stimulating gland का चयन।
1(ii)|3|1|hydra|Budding से नया organism।
1(iii)|3|1|xylem|Xylem का transported पदार्थ।
1(v)|4|1|plastic|Non-biodegradable option।
1(vi)|4|1|uv|Ozone किस radiation को रोकती है?
1(vii)|4|1|iris|Pupil size का नियंत्रण।
1(viii)|5|1|redleast|Prism least bending colour।
1(ix)|5|1|halfR|Wire half length का R।
1(x)|5|1|volt|Potential difference unit।
1(xi)|5|1|attract|Unlike poles का effect।
1(xii)|6|1|left|Left-hand rule की तीन quantities।
1(xiii)|6|1|limestone|Limestone formula।
1(xiv)|6|1|feoxidecoef|Fe₃O₄ coefficient।
1(xv)|7|1|nitricMg|Very dilute HNO₃ में H₂ option।
1(xvi)|7|1|activityMAF|Mg/Al/Fe decreasing activity।
1(xvii)|7|1|aldehyde|Aldehyde functional group।
1(xviii)|7|1|nitrogen|Nitrogen atomic number।
2(i)|8|1|plasma|Blood का fluid medium।
2(iii)|8|1|dihybrid|Two-gene F₂ phenotype ratio।
2(iv)|8|1|chromosomes|Human chromosome pairs।
2(v)|8|1|acetate|Ethanoic-acid aqueous anion।
2(vi)|8|1|tartaric|Tamarind का sour acid।''')
