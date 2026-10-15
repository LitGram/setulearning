// Continue Book 2 graphics with topic-specific SVG masters and reader placements.
const fs = require('fs');
const path = require('path');
const crypto = require('crypto');
const sharp = require('C:/Users/rishi/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/sharp');

const root = path.resolve(__dirname, '..');
const bookPath = path.join(root, 'assets/content/rassetu/rassetu_book2.json');
const manifestPath = path.join(root, 'artifacts/rassetu_geography_pilot/book2_continuation_manifest.json');
const svgDir = path.join(root, 'artifacts/rassetu_geography_pilot/svg');
const imgDir = path.join(root, 'assets/images');
const C = { ink:'#20352f', muted:'#526a61', green:'#2f8066', blue:'#3976a8', rust:'#bd7149', sand:'#eedbb9', pale:'#f2f6f3', sky:'#eaf2f8', line:'#bdd0c6', gold:'#d5a23d' };
const font = 'Noto Sans Devanagari, Nirmala UI, Arial, sans-serif';
const esc = s => String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
function txt(x,y,s,size=25,anchor='middle',color=C.ink,bold=false){return `<text x="${x}" y="${y}" text-anchor="${anchor}" fill="${color}" font-size="${size}" font-weight="${bold?700:400}" font-family="${font}">${esc(s)}</text>`;}
function lines(x,y,arr,size=22,color=C.ink,step=size+9){return arr.map((s,i)=>txt(x,y+i*step,s,size,'middle',color)).join('');}
function arrow(x,y,X,Y,color=C.muted,width=4){return `<path d="M${x} ${y} L${X} ${Y}" fill="none" stroke="${color}" stroke-width="${width}" marker-end="url(#arrow)"/>`;}
function box(x,y,w,h,label,fill=C.pale,size=23){const a=Array.isArray(label)?label:[label];return `<rect x="${x}" y="${y}" width="${w}" height="${h}" rx="18" fill="${fill}" stroke="${C.line}" stroke-width="2"/>`+lines(x+w/2,y+h/2-(a.length-1)*(size+9)/2+size*.34,a,size);}
function base(title){return `<svg xmlns="http://www.w3.org/2000/svg" width="1440" height="1080" viewBox="0 0 1440 1080"><defs><marker id="arrow" markerWidth="12" markerHeight="12" refX="9" refY="4" orient="auto"><path d="M0 0 L9 4 L0 8 Z" fill="${C.muted}"/></marker><pattern id="soil" width="14" height="14" patternUnits="userSpaceOnUse"><circle cx="3" cy="4" r="1.5" fill="#9f8061"/><circle cx="10" cy="10" r="1" fill="#9f8061"/></pattern></defs><rect width="1440" height="1080" fill="#fff"/>${txt(720,62,title,38,'middle',C.ink,true)}<path d="M64 91 H1376" stroke="#dbe8e0" stroke-width="3"/>`}
function footer(note='सांकेतिक आरेख — आकृतियां और तीर अवधारणा समझाने हेतु; पैमाने पर नहीं।  /  Schematic / not to scale.'){return `<rect x="55" y="987" width="1330" height="58" rx="12" fill="#f6f4ef"/>${txt(720,1023,note,18,'middle','#655b4c')}`}
function svg(title,body,note){return base(title)+body+footer(note)+'</svg>';}

const graphics = [
 {id:'rassetu_b2_dune_formation', title:'थार मरुस्थल: वायु और बालुका स्तूप', chapter:'ch01', anchor:'### 2.2 थार मरुस्थल की उत्पत्ति एवं वायुगतिकीय बालुका स्तूप निर्माण (Aerodynamic Sand Dynamics)', caption:'बालुका स्तूपों की आकृति और पवन', explanation:'बरखान में एक मुख्य पवन-दिशा, पैरॉबोलिक स्तूप में वनस्पति से रुका मध्य भाग, और तारा स्तूप में बदलती पवन-दिशाएं दिखाने वाला सांकेतिक मॉडल। आकृतियां पैमाने पर नहीं हैं।',
  body:()=>{
   let s=txt(720,137,'तीन आकृतियां — अलग पवन और सतही दशाएं',24,'middle',C.muted,true);
   const panels=[{x:60,title:'बरखान',sub:'एक मुख्य पवन-दिशा',fill:'#f7e8ca'},{x:510,title:'पैरॉबोलिक',sub:'वनस्पति केंद्र को थामती है',fill:'#edf3df'},{x:960,title:'तारा स्तूप',sub:'पवन-दिशाएं बदलती हैं',fill:'#f4eadf'}];
   for(const p of panels){s+=`<rect x="${p.x}" y="185" width="420" height="650" rx="24" fill="#fbfcfb" stroke="${C.line}" stroke-width="2"/>`+txt(p.x+210,236,p.title,31,'middle',C.ink,true)+txt(p.x+210,275,p.sub,20,'middle',C.muted);}
   // Barchan plan-like silhouette, horns advance with the wind.
   s+=`<path d="M430 450 Q360 448 318 473 Q255 505 220 540 Q255 575 318 602 Q360 627 430 625 Q365 586 365 540 Q365 492 430 450Z" fill="#eacb91" stroke="#b98b4e" stroke-width="4"/>`;
   s+=arrow(130,365,390,365,C.blue,5)+txt(260,344,'पवन',20,'middle',C.blue,true)+txt(275,675,'दोनों सींग नीचे-पवन दिशा में',20);
   // Parabolic U-shaped form with stabilized center.
   s+=`<path d="M560 445 Q625 555 715 575 Q805 555 870 445 L838 468 Q785 535 715 540 Q645 535 592 468Z" fill="#eacb91" stroke="#b98b4e" stroke-width="4"/>`;
   s+=`<path d="M715 445 V540" stroke="${C.green}" stroke-width="7" stroke-dasharray="12 9"/>`+txt(715,420,'झाड़ी / वनस्पति',19,'middle',C.green,true)+arrow(585,365,675,365,C.blue,5)+arrow(760,365,850,365,C.blue,5)+txt(715,643,'वनस्पति से थमा मध्य भाग; किनारे आगे',20);
   // Multi-direction star dunes: central mound with radiating ridges.
   s+=`<path d="M1170 515 L1040 405 L1160 458 L1205 322 L1228 458 L1360 387 L1278 505 L1350 610 L1230 560 L1185 695 L1168 557 L1042 630Z" fill="#eacb91" stroke="#b98b4e" stroke-width="4"/>`;
   s+=arrow(1050,345,1125,405,C.blue,4)+arrow(1320,345,1260,420,C.rust,4)+arrow(1090,710,1150,635,C.green,4)+txt(1170,760,'बहुदिशीय पवन-रिज',20);
   return s;
  }},
 {id:'rassetu_b2_chambal_ravines', title:'चंबल बीहड़: बहते जल से अवनालिका तक', chapter:'ch01', anchor:'### 2.4 चंबल बेसिन में उत्खात स्थलाकृति (Badland Topography) का भू-आकृतिक विज्ञान', caption:'बीहड़ बनने की प्रक्रिया', explanation:'ढाल पर बहता वर्षाजल पहले छोटी नालियां काटता है; उनका विस्तार गहरी अवनालिकाओं और बीहड़ भू-आकृति में होता है। यह स्थलरूप का सांकेतिक अनुप्रस्थ दृश्य है।',
  body:()=>{
   const stages=[['1','ढाल पर बहाव','वर्षा का जल ढलान पर'],['2','छोटी नालियां','मिट्टी का बहाव'],['3','गहरी अवनालिका','कटाव की शाखाएं'],['4','बीहड़','खंडित, दुर्गम सतह']];
   let s=''; stages.forEach((a,i)=>{const x=55+i*345;s+=box(x,150,300,108,[a[0]+'  '+a[1],a[2]],i<2?'#eaf2f8':'#f8eee7',21);if(i<3)s+=arrow(x+302,205,x+338,205,C.muted,4);});
   s+=`<path d="M70 440 L280 330 L460 404 L610 338 L750 435 L890 361 L1045 480 L1190 380 L1370 465 L1370 850 L70 850Z" fill="#eedbb9" stroke="#9f8061" stroke-width="4"/>`;
   s+=`<path d="M400 380 Q420 500 444 830 M610 355 Q630 470 655 825 M820 415 Q845 545 872 845 M1010 440 Q1025 545 1058 840 M1180 400 Q1190 520 1220 835" fill="none" stroke="#a85e42" stroke-width="18"/>`;
   s+=`<path d="M360 374 Q470 425 550 365 M585 405 Q690 465 760 410 M825 446 Q925 485 1005 440 M1020 470 Q1120 510 1174 455" fill="none" stroke="#c8815a" stroke-width="8"/>`;
   s+=arrow(140,286,380,390,C.blue,5)+arrow(520,300,620,420,C.blue,5)+arrow(890,300,1035,490,C.blue,5);
   s+=txt(720,558,'गहरी कटान और शाखित नालियां',23,'middle',C.rust,true)+txt(720,920,'मानसून का बहाव नरम जलोढ़ सतह को काटकर खंडित करता है',24);
   return s;
  }},
 {id:'rassetu_b2_luni_salinity', title:'लूणी: बालोतरा के बाद बढ़ती लवणता', chapter:'ch03', anchor:"### 2.2 लूणी नदी का बालोतरा के बाद लवणीय होने का भू-रासायनिक कारण (Geochemistry of Luni's Salinity)", caption:'लूणी नदी के जल में लवणता का क्रम', explanation:'पुस्तक में दिए गए कारणों का सांकेतिक क्रम: ऊपरी प्रवाह में सामान्य खनिज मात्रा, फिर शुष्क पश्चिमी बेसिन में मिट्टी और लवणीय धूल से घुले लवणों का नदी में मिलना। स्थान और प्रवाह पैमाने पर नहीं हैं।',
  body:()=>{
   let s=box(100,190,355,158,['अरावली का उद्गम क्षेत्र','ग्रेनाइट / नीस','सामान्य घुलित खनिज'],'#eaf2f8',22);
   s+=box(985,190,355,158,['पश्चिमी शुष्क बेसिन','लवणीय निक्षेप और धूल','वर्षा से लवण घुलते हैं'],'#f8eee7',22);
   s+=`<path d="M240 485 C390 435 520 530 660 485 S950 435 1120 485" fill="none" stroke="#3976a8" stroke-width="24" stroke-linecap="round"/>`;
   s+=arrow(300,440,505,478,C.blue,5)+arrow(760,478,980,478,C.blue,5);
   s+=txt(270,535,'नाग पहाड़',22,'middle',C.ink,true)+txt(720,535,'बालोतरा',22,'middle',C.rust,true)+txt(1130,535,'आगे पश्चिम की ओर',21,'middle',C.ink,true);
   s+=`<path d="M635 505 V660" stroke="${C.rust}" stroke-width="4" stroke-dasharray="9 8"/>`;
   s+=box(115,690,510,170,['ऊपरी प्रवाह','लवणता अपेक्षाकृत कम'],'#e7f2ef',25)+box(815,690,510,170,['बालोतरा के बाद','घुले लवण बढ़ते हैं'],'#f8eee7',25);
   s+=txt(720,925,'स्रोत-पाठ पर आधारित प्रक्रिया-रेखा; नदी-मानचित्र नहीं',21,'middle',C.muted);
   return s;
  }},
 {id:'rassetu_b2_sambhar_salt_basin', title:'सांभर: बंद बेसिन से नमक तक', chapter:'ch03', anchor:'### 2.3 सांभर झील बेसिन में अंतःस्थलीय अपवाह एवं नमक निर्माण की प्रक्रिया', caption:'सांभर बेसिन और नमक बनने का मॉडल', explanation:'चारों ओर से आने वाला अपवाह घुले लवण बंद बेसिन में पहुंचाता है। वाष्पीकरण से नमकीन जल सघन होता है; क्यारों में नमक प्राप्त किया जाता है। सांकेतिक अनुप्रस्थ दृश्य, पैमाने पर नहीं।',
  body:()=>{
   let s=`<path d="M85 335 L420 575 L1020 575 L1355 335" fill="none" stroke="#9f8061" stroke-width="22" stroke-linejoin="round"/>`;
   s+=`<path d="M460 550 Q720 510 980 550 L960 655 Q720 690 480 655Z" fill="#b9d8e6" stroke="#3976a8" stroke-width="4"/>`;
   s+=arrow(180,320,470,525,C.blue,5)+arrow(1260,320,970,525,C.blue,5)+arrow(450,460,550,530,C.blue,4)+arrow(995,455,900,530,C.blue,4);
   s+=txt(170,270,'मेन्था',21,'middle',C.blue,true)+txt(1270,270,'रूपनगढ़',21,'middle',C.blue,true)+txt(445,415,'खारी',20,'middle',C.blue)+txt(1000,410,'खंडेला',20,'middle',C.blue);
   s+=txt(720,620,'बंद झील-बेसिन',26,'middle',C.ink,true)+txt(720,725,'घुले लवण जमा',22,'middle',C.muted);
   s+=arrow(720,495,720,385,C.rust,5)+`<path d="M670 365 Q720 332 770 365 M680 340 Q720 310 760 340" fill="none" stroke="${C.rust}" stroke-width="4"/>`+txt(720,290,'वाष्पीकरण',21,'middle',C.rust,true);
   s+=box(160,790,455,116,['सघन खारा घोल','ब्राइन'],'#eaf2f8',23)+arrow(625,850,815,850,C.muted,4)+box(825,790,455,116,['क्यारों में','नमक के क्रिस्टल'],'#f5ead8',23);
   return s;
  }},
 {id:'rassetu_b2_india_plate_tectonics', title:'भारतीय प्लेट: टक्कर से हिमालय तक', chapter:'ch27', anchor:'### 2.1 भारत की भूगर्भिक संरचना एवं प्लेट विवर्तनिकी (Plate Tectonics)', caption:'भारतीय प्लेट और हिमालय का निर्माण', explanation:'तीन चरणों का सांकेतिक मॉडल: भारतीय प्लेट का उत्तर की ओर बढ़ना, यूरेशियन प्लेट से अभिसरण और टेथिस क्षेत्र के अवसादों का वलन; आगे अग्रगर्त में नदी-निक्षेप से उत्तरी मैदान बनना। आकृतियां पैमाने पर नहीं हैं।',
  body:()=>{
   const xs=[60,510,960], titles=['1  उत्तरगामी गति','2  अभिसरण और वलन','3  निक्षेप और मैदान'];let s='';
   for(let i=0;i<3;i++)s+=`<rect x="${xs[i]}" y="155" width="420" height="690" rx="22" fill="#fbfcfb" stroke="${C.line}" stroke-width="2"/>`+txt(xs[i]+210,210,titles[i],26,'middle',C.ink,true);
   // Panels use a shared lower edge; India/Asia are schematic blocks.
   s+=`<path d="M95 540 H445 V700 H95Z" fill="#eacb91" stroke="#9f8061" stroke-width="3"/>`+txt(270,625,'भारतीय प्लेट',24,'middle',C.ink,true)+arrow(140,490,385,490,C.blue,5)+txt(265,460,'उत्तर',20,'middle',C.blue,true)+txt(270,760,'टेथिस क्षेत्र',20,'middle',C.muted);
   s+=`<path d="M555 545 H875 V700 H555Z" fill="#eacb91" stroke="#9f8061" stroke-width="3"/><path d="M555 545 Q600 470 645 545 T735 545 T825 545 T875 545 V420 H555Z" fill="#d8e5dc" stroke="#829b8b" stroke-width="3"/>`;
   s+=txt(715,460,'यूरेशियन प्लेट',22,'middle',C.ink,true)+txt(715,625,'भारतीय प्लेट',22,'middle',C.ink,true)+arrow(590,505,690,505,C.blue,4)+arrow(840,505,740,505,C.rust,4)+txt(715,760,'अवसादों में संपीडन और वलन',19);
   s+=`<path d="M1005 560 H1335 V700 H1005Z" fill="#eacb91" stroke="#9f8061" stroke-width="3"/><path d="M1005 540 Q1040 450 1075 535 Q1115 390 1150 530 Q1190 430 1230 530 Q1270 455 1305 540 L1335 560 V590 H1005Z" fill="#d8e5dc" stroke="#829b8b" stroke-width="3"/>`;
   s+=txt(1170,420,'हिमालय',22,'middle',C.ink,true)+`<path d="M1015 565 Q1170 580 1325 565 V620 H1015Z" fill="#dcebf2"/>`+txt(1170,650,'अग्रगर्त में निक्षेप',19,'middle',C.blue)+txt(1170,760,'नदी-अवसाद से उत्तरी मैदान',19);
   s+=arrow(470,470,500,470,C.muted,4)+arrow(920,470,950,470,C.muted,4)+txt(720,920,'भूगर्भिक प्रक्रिया का आरेख; सीमाएं, दूरी और ऊंचाई पैमाने पर नहीं',21,'middle',C.muted);
   return s;
  }},
 {id:"rassetu_b2_rajasthan_physiography",title:"राजस्थान के चार भौतिक प्रदेश",chapter:"ch01",anchor:"### 3.3 चारों भौतिक विभागों का प्रामाणिक तुलनात्मक पदानुक्रम",caption:"राजस्थान के भू-आकृतिक प्रदेश",explanation:"थार मरुस्थलीय प्रदेश, अरावली पर्वतीय प्रदेश, पूर्वी मैदान और हाड़ौती पठार का सांकेतिक क्षेत्र-क्रम। जिला-सीमा मानचित्र नहीं; पैमाने पर नहीं।",
  body:()=>txt(720,150,"पश्चिम से पूर्व / दक्षिण-पूर्व तक",24,"middle",C.muted,true)
   +'<path d="M70 665 Q165 610 270 635 L380 630 Q470 565 555 610 Q630 635 720 495 Q790 600 875 630 L1010 625 Q1115 585 1185 500 Q1280 470 1370 550 L1370 810 L70 810Z" fill="#eedbb9" stroke="#9f8061" stroke-width="4"/>'
   +'<path d="M400 610 Q455 490 505 545 Q555 410 600 545 Q650 480 720 495 Q770 570 810 615" fill="#d8e5dc" stroke="#829b8b" stroke-width="5"/>'
   +'<path d="M1070 600 L1145 495 L1220 600Z M1200 600 L1270 470 L1350 600Z" fill="#d9c49e" stroke="#9f8061" stroke-width="4"/>'
   +lines(190,285,["थार मरुस्थलीय","प्रदेश"],24,C.ink,32)+lines(590,285,["अरावली","पर्वतीय प्रदेश"],24,C.ink,32)
   +txt(930,300,"पूर्वी मैदान",24,"middle",C.ink,true)+lines(1220,285,["हाड़ौती","का पठार"],24,C.ink,32)
   +txt(720,900,"भू-आकृतिक अनुक्रम का सांकेतिक चित्र — पैमाने पर नहीं",20,"middle",C.muted)},
 {id:"rassetu_b2_forest_ecology",title:"राजस्थान के वन: जलवायु और वन-रूप",chapter:"ch07",anchor:"### 2.1 चैंपियन एवं सेठ के अनुसार राजस्थान के वन प्रारूप (Forest Ecology & Dynamics)",caption:"वन-रूपों में पर्यावरणीय अंतर",explanation:"पुस्तक में दिए पांच वन-समूह और उनकी मुख्य पारिस्थितिक दशाएं। क्षेत्र-वितरण व्यापक संकेत है; वर्तमान वनावरण प्रतिशत या जिला-सीमा नहीं।",
  body:()=>{let s="";const xs=[48,324,600,876,1152],ns=["शुष्क सागवान","शुष्क मिश्रित","धोकड़ा वन","कंटीले मरुद्भिद","उपोष्ण सदाबहार"],ds=["दक्षिणी क्षेत्र","अरावली ढाल","अरावली • विंध्य","पश्चिमी शुष्क क्षेत्र","माउंट आबू ऊंचाई"],sp=["सागवान","सालर • खैर","धोकड़ा","खेजड़ी • रोहिड़ा","जामुन • गूलर"],cl=["गहरी मिट्टी","पर्णपाती","सूखा-सहिष्णु","कांटे • गहरी जड़ें","ठंडा • नम"];for(let i=0;i<5;i++){let x=xs[i],cx=x+115;s+='<rect x="'+x+'" y="180" width="238" height="620" rx="18" fill="#fbfcfb" stroke="'+C.line+'" stroke-width="2"/>'+txt(cx,230,ns[i],21,"middle",C.ink,true)+txt(cx,270,ds[i],17,"middle",C.muted);s+='<path d="M'+cx+' 555 V370 M'+cx+' 420 Q'+(cx-70)+' 390 '+(cx-58)+' 342 Q'+(cx-12)+' 330 '+cx+' 397 Q'+(cx+12)+' 330 '+(cx+58)+' 342 Q'+(cx+70)+' 390 '+cx+' 420Z" fill="'+["#6f9a60","#81a66f","#769653","#9eaa56","#5f9277"][i]+'" stroke="#487449" stroke-width="4"/>';if(i===3)s+='<path d="M'+(cx-20)+' 470 L'+(cx-42)+' 440 M'+(cx+20)+' 470 L'+(cx+42)+' 440 M'+cx+' 470 L'+cx+' 435" stroke="#687d3c" stroke-width="6"/>';s+=txt(cx,640,sp[i],18,"middle",C.ink,true)+txt(cx,700,cl[i],17,"middle",C.muted);}return s+txt(720,890,"वन-प्रकारों का पर्यावरणीय तुलनात्मक चित्र; संख्यात्मक वनावरण नहीं",20,"middle",C.muted);}},
 {id:"rassetu_b2_soil_parent_material",title:"मूल पदार्थ से मृदा-गुण तक",chapter:"ch09",anchor:"### 2.1 पैतृक शैल (Parent Rock) एवं राजस्थान की मृदा उत्पत्ति का संबंध",caption:"पैतृक पदार्थ और मृदा का संबंध",explanation:"पुस्तक में दिए उदाहरण: बेसाल्ट, नदीय जलोढ़, नाइस/शिस्ट और क्वार्ट्ज बालू से बनने वाले मृदा-समूह। कारण-संबंध का सांकेतिक चित्र, मृदा-सीमा मानचित्र नहीं।",
  body:()=>{const rows=[["बेसाल्ट लावा","अपक्षय","मध्यम काली मृदा","जल धारण • दरारें"],["नदीय जलोढ़","निक्षेप","दोमट जलोढ़ मृदा","उपजाऊ निक्षेप"],["नाइस / शिस्ट","अपक्षय","लाल-लोमी मृदा","लौह-अंश • लाल रंग"],["क्वार्ट्ज बालू","पवन-अपक्षय","रेतीली शुष्क मृदा","कम लीचिंग"]];let s="";rows.forEach((r,i)=>{let y=145+i*195;s+='<rect x="70" y="'+y+'" width="1300" height="160" rx="16" fill="'+(i%2?"#fbfcfb":"#f6f8f5")+'" stroke="'+C.line+'" stroke-width="2"/>'+txt(245,y+66,r[0],22,"middle",C.ink,true)+arrow(395,y+80,500,y+80,C.rust,4)+txt(448,y+48,r[1],17,"middle",C.rust)+ '<path d="M545 '+(y+105)+' L580 '+(y+47)+' L615 '+(y+105)+'Z" fill="#d8c39e" stroke="#9f8061" stroke-width="3"/>'+txt(825,y+65,r[2],23,"middle",C.ink,true)+txt(825,y+108,r[3],18,"middle",C.muted);});return s;}},
 {id:"rassetu_b2_water_stress",title:"राजस्थान में जल-संकट: कारणों का तंत्र",chapter:"ch15",anchor:"### 2.1 राजस्थान में जल संकट: भौतिक पृष्ठभूमि एवं सांख्यिकीय वास्तविकता",caption:"जल की उपलब्धता पर भौतिक दबाव",explanation:"कम और अनिश्चित वर्षा, उच्च वाष्पीकरण, सीमित स्थानीय सतही जल और भूजल पर निर्भरता से बनने वाले जल-दबाव का सांकेतिक मॉडल। बदलते आंकड़े, ब्लॉक-गणना और परियोजना क्षमता शामिल नहीं।",
  body:()=>{let s=box(75,210,370,150,["कम / अनिश्चित वर्षा","समय और मात्रा बदलते हैं"],"#eaf2f8",22)+box(535,210,370,150,["उच्च वाष्पीकरण","खुला जल तेजी से घटता है"],"#f8eee7",22)+box(995,210,370,150,["सीमित सतही प्रवाह","स्थानीय उपलब्धता असमान"],"#e7f2ef",22);s+=arrow(260,390,545,530,C.blue,4)+arrow(720,390,720,530,C.rust,4)+arrow(1180,390,895,530,C.green,4);s+='<path d="M100 630 Q260 570 420 630 T720 630 T1020 630 T1340 630 V770 H100Z" fill="#eedbb9" stroke="#9f8061" stroke-width="3"/><path d="M250 675 V745 M430 675 V745 M610 675 V745 M790 675 V745 M970 675 V745 M1150 675 V745" stroke="#9f8061" stroke-width="3" stroke-dasharray="7 7"/><path d="M190 835 Q720 785 1250 835" fill="none" stroke="#3976a8" stroke-width="20" stroke-linecap="round"/>';return s+txt(720,910,"भूजल पर निर्भरता से दीर्घकालीन दबाव का जोखिम",22,"middle",C.ink,true);}},
 {id:"rassetu_b2_india_physiography",title:"भारत: प्रमुख भौतिक प्रदेश",chapter:"ch27",anchor:"### 2.6 तटीय मैदान एवं द्वीप समूह",caption:"भारत के प्रमुख भू-आकृतिक विभाग",explanation:"हिमालय, उत्तरी मैदान, प्रायद्वीपीय पठार, तटीय मैदान और द्वीप समूह को एक सांकेतिक प्रोफाइल में दिखाया गया है। यह मानचित्र नहीं; आकृतियां और दूरी पैमाने पर नहीं।",
  body:()=>{let s='<path d="M65 650 L135 520 L200 565 L265 405 L330 590 L395 650 L520 630 L640 635 L745 625 L875 655 L980 615 L1090 650 L1250 625 L1370 650 V810 H65Z" fill="#eedbb9" stroke="#9f8061" stroke-width="4"/><path d="M95 620 L135 520 L200 565 L265 405 L330 590 L395 650Z" fill="#d8e5dc" stroke="#829b8b" stroke-width="3"/><path d="M390 650 Q470 615 550 640 T710 635 T875 655 V810 H390Z" fill="#e8d5ad" stroke="#b89d70" stroke-width="3"/><path d="M875 655 Q980 590 1090 650 V810 H875Z" fill="#d4c096" stroke="#9f8061" stroke-width="3"/><path d="M1090 650 Q1240 615 1370 650 V810 H1090Z" fill="#d9e8ee" stroke="#3976a8" stroke-width="3"/>';s+=txt(240,330,"हिमालय",24,"middle",C.ink,true)+txt(600,590,"उत्तरी मैदान",23,"middle",C.ink,true)+txt(980,570,"प्रायद्वीपीय पठार",22,"middle",C.ink,true)+txt(1240,610,"तटीय मैदान",19,"middle",C.blue,true);s+=lines(500,285,["भारतीय मरुस्थल","(उत्तर-पश्चिम)"],18,C.rust,25);s+='<ellipse cx="1220" cy="330" rx="120" ry="50" fill="#eaf2f8" stroke="'+C.line+'" stroke-width="2"/>';s+=txt(1220,325,"द्वीप समूह",19,"middle",C.ink,true)+txt(1220,352,"अलग स्थानों पर",16,"middle",C.muted);return s+txt(720,900,"सांकेतिक भौतिक प्रोफाइल — मानचित्र नहीं; पैमाने पर नहीं",20,"middle",C.muted);}},
 {id:"rassetu_b2_india_monsoon_mechanism",title:"भारतीय ग्रीष्म मानसून: पवन और वर्षा",chapter:"ch29",anchor:"### 2.2 मानसून उत्पत्ति के शास्त्रीय एवं आधुनिक वैज्ञानिक सिद्धांत",caption:"मौसमी दाब-ढाल और नमी-युक्त पवन",explanation:"सरलीकृत तंत्र: मौसमी तापीय अंतर और निम्न-दाब क्षेत्र की ओर नमी-युक्त पवन का प्रवाह; भूमध्य रेखा पार करती पवनें दक्षिण-पश्चिम दिशा से भारत में प्रवेश करती हैं। यह मौसम-पूर्वानुमान या वर्तमान मानसून स्थिति नहीं।",
  body:()=>{let s='<circle cx="220" cy="250" r="70" fill="#f3d889" stroke="#d5a23d" stroke-width="4"/>'+txt(220,258,"सूर्य",22,"middle",C.ink,true)+'<path d="M360 280 Q650 370 950 280" fill="none" stroke="#d5a23d" stroke-width="3" stroke-dasharray="10 9"/>';s+=txt(650,390,"ऋतु के साथ ताप-वितरण बदलता है",20,"middle",C.muted);s+='<path d="M65 705 Q380 655 700 700 T1375 690 V865 H65Z" fill="#d9e8ee" stroke="#3976a8" stroke-width="3"/><path d="M65 640 Q330 600 570 630 L590 785 H65Z" fill="#eedbb9" stroke="#9f8061" stroke-width="3"/><path d="M1015 625 L1080 525 L1135 625 L1190 500 L1240 625 L1320 555 L1375 640 V790 H1015Z" fill="#d8e5dc" stroke="#829b8b" stroke-width="3"/>';s+=txt(1190,480,"हिमालय",21,"middle",C.ink,true)+box(425,465,430,110,["स्थल पर उष्ण निम्न-दाब","मौसमी मानसून द्रोणी"],"#f8eee7",21)+arrow(250,675,485,600,C.blue,6)+arrow(620,680,710,600,C.blue,6)+arrow(785,600,1040,670,C.blue,6);s+=txt(325,745,"दक्षिण-पश्चिम पवन",20,"middle",C.blue,true)+txt(1130,420,"नमी ऊपर उठती है",18,"middle",C.blue,true);return s+txt(720,930,"सरलीकृत परिपथ; वास्तविक मानसून अनेक कारकों से प्रभावित",20,"middle",C.muted);}},
 {id:"rassetu_b2_india_drainage_compare",title:"भारत के नदी-तंत्र: हिमालयी और प्रायद्वीपीय",chapter:"ch31",anchor:"### 2.1 भारतीय अपवाह तंत्र का वर्गीकरण",caption:"दो बड़े नदी-तंत्रों की तुलना",explanation:"हिमालयी नदियों को हिम-पिघलन और वर्षा से जल मिलता है; प्रायद्वीपीय नदियां मुख्यतः वर्षा-आधारित हैं। घाटियां सांकेतिक हैं; किसी नदी का मापित मार्ग नहीं।",
  body:()=>{let s='<rect x="65" y="155" width="625" height="660" rx="22" fill="#f8fbfd" stroke="'+C.line+'" stroke-width="2"/><rect x="750" y="155" width="625" height="660" rx="22" fill="#fbfcfb" stroke="'+C.line+'" stroke-width="2"/>';s+=txt(377,215,"हिमालयी अपवाह",29,"middle",C.ink,true)+txt(1062,215,"प्रायद्वीपीय अपवाह",29,"middle",C.ink,true);s+='<path d="M120 405 L210 280 L300 400 L365 295 L430 405 L520 310 L635 420" fill="none" stroke="#829b8b" stroke-width="34" stroke-linejoin="round"/><path d="M210 395 Q230 480 305 510 T435 630 Q520 690 625 725" fill="none" stroke="#3976a8" stroke-width="17" stroke-linecap="round"/><path d="M155 410 Q220 485 305 510 M355 380 Q365 455 435 500 M520 400 Q495 520 435 630" fill="none" stroke="#75a9c6" stroke-width="9"/>';s+=txt(370,755,"हिम-पिघलन + वर्षा • नित्यवाही",19,"middle",C.blue,true);s+='<path d="M810 690 Q910 660 1005 690 T1200 680 T1340 690" fill="none" stroke="#c6ad78" stroke-width="20"/><path d="M900 400 Q990 440 1050 520 Q1110 585 1260 620" fill="none" stroke="#3976a8" stroke-width="15" stroke-linecap="round"/><path d="M1090 410 Q1080 500 1050 520 M1195 390 Q1190 505 1260 620" fill="none" stroke="#75a9c6" stroke-width="8"/>';s+=txt(1060,755,"वर्षा-आधारित • अधिकतर ऋतुनिष्ठ",19,"middle",C.blue,true);return s+txt(720,885,"सरलीकृत तुलना; घाटियां, प्रवाह और ऋतुएं क्षेत्रानुसार बदलती हैं",20,"middle",C.muted);}},
 {id:"rassetu_b2_whittlesey_framework",title:"विश्व कृषि प्रदेश: व्हिटलसी के पांच मानदंड",chapter:"ch45",anchor:"### 2.1 डी. व्हिटलसी का विश्व कृषि वर्गीकरण (Derwent Whittlesey's Classification - 1936)",caption:"कृषि प्रदेश पहचानने के पांच मानदंड",explanation:"1936 के व्हिटलसी वर्गीकरण में कृषि प्रदेशों की पहचान के पांच कार्यात्मक मानदंड दिखाए गए हैं। यह वर्गीकरण-ढांचा है, वर्तमान उत्पादन या देश-सीमा मानचित्र नहीं।",
  body:()=>{let s='<circle cx="720" cy="540" r="145" fill="#e7f2ef" stroke="'+C.green+'" stroke-width="4"/>'+txt(720,530,"कृषि प्रदेश",29,"middle",C.ink,true)+txt(720,570,"समग्र रूप",20,"middle",C.muted);const pts=[[720,235,"1","फसल और पशु","साहचर्य"],[1100,410,"2","उत्पादन की","विधियां"],[960,805,"3","श्रम, पूंजी और","प्रबंधन"],[480,805,"4","निर्वाह या","व्यापार"],[340,410,"5","संरचनाएं और","औजार"]];pts.forEach((p,i)=>{s+=arrow(720+(p[0]-720)*.58,540+(p[1]-540)*.58,p[0],p[1],C.muted,4);s+='<circle cx="'+p[0]+'" cy="'+p[1]+'" r="92" fill="'+(i%2?"#f8eee7":"#eaf2f8")+'" stroke="'+C.line+'" stroke-width="3"/>'+txt(p[0],p[1]-18,p[2],24,"middle",C.rust,true)+txt(p[0],p[1]+18,p[3],18,"middle",C.ink,true)+txt(p[0],p[1]+44,p[4],18,"middle",C.ink,true);});return s+txt(720,955,"पांच पहलुओं का संयुक्त रूप कृषि-क्षेत्र की पहचान बनाता है",20,"middle",C.muted);}},
];

graphics.find(g=>g.id==='rassetu_b2_india_physiography').sourceReferences=['https://www.ncert.nic.in/textbook/pdf/iess102.pdf'];
graphics.find(g=>g.id==='rassetu_b2_india_monsoon_mechanism').sourceReferences=['https://mausamjournal.imd.gov.in/index.php/MAUSAM/article/view/913'];

const scenes = [{id:'rassetu_b2_thar_dunes_scene', chapter:'ch01', anchor:graphics[0].anchor,afterOffset:3,
 caption:'थार के बालुका स्तूप: प्रतिनिधि दृश्य', explanation:'पवन से बने बालुका स्तूपों और विरल मरुस्थलीय वनस्पति का प्रतिनिधि चित्रण — केवल शैक्षिक समझ हेतु; किसी नामित स्थान का वास्तविक दृश्य नहीं।',
 generationPrompt:'Use case: educational textbook image for Rajasthan geography. Asset type: wide representative scene illustration. Scene: Thar Desert in western Rajasthan, sweeping wind-shaped crescent dunes with sparse hardy desert grasses and a few khejri-like trees at the far edge, warm late-afternoon light, natural ochre and muted green palette. Style: polished, realistic gouache-meets-editorial illustration, clear landforms and restrained detail, suitable for a high-school geography reader on a phone. Composition: landscape 3:2, broad dune forms readable at small size, no people or buildings, no labels or text. Constraints: representative atmosphere only, not a literal depiction of a named place or exact topographic map; no signage, no watermark, no text.',sourceEnv:'RASSETU_SCENE_SOURCE',sourceReferences:['https://pubs.usgs.gov/gip/deserts/dunes/','https://www.doi.gov/sites/default/files/usgs-dune-models.508.pdf']},
 {id:'rassetu_b2_woodland_scene',chapter:'ch07',anchor:'### 2.3 गोडावण (Great Indian Bustard) के संकट एवं प्रजनन परियोजनाएं (Project Godawan)',caption:'शुष्क वन और घासभूमि: प्रतिनिधि दृश्य',explanation:'शुष्क झाड़ीदार वनस्पति और घासभूमि का प्रतिनिधि चित्रण — केवल शैक्षिक समझ हेतु; किसी नामित वन, अभयारण्य या सटीक प्रजाति-सूची का चित्र नहीं।',assetType:'generated-representative-image',sourceEnv:'RASSETU_WOODLAND_SCENE_SOURCE',generationPrompt:'Use case: high-school Rajasthan geography textbook scene. Asset type: wide representative ecosystem illustration. Scene: semi-arid woodland and grassland in Rajasthan, low native grasses and thorny scrub, a few broad-canopy dhok and khejri-like trees, open dry-season landscape with distant low hills, warm clear light and restrained earth-green palette. Style: polished realistic editorial gouache illustration, scientifically plausible plants, clear layered habitat, calm documentary composition. Landscape 3:2. No people, buildings, fences, roads, power lines, labels, text, watermark, or dramatic fantasy wildlife. Representative atmosphere only; not a literal depiction of a named reserve or exact species inventory.',sourceReferences:['assets/content/rassetu/rassetu_book2.json#ch07/2.1']},
 {id:'rassetu_b2_pastoral_scene',chapter:'ch13',anchor:'### 2.1 थार मरुस्थल में पशुपालन का पारिस्थितिकीय महत्व (Ecological Resilience)',caption:'थार में पशुधन और चरागाह: प्रतिनिधि दृश्य',explanation:'ऊंट, भेड़ और बकरियों के साथ शुष्क चरागाह का प्रतिनिधि चित्रण — केवल शैक्षिक समझ हेतु; पशु किसी विशिष्ट नस्ल के सटीक चित्र नहीं हैं।',assetType:'generated-representative-image',sourceEnv:'RASSETU_PASTORAL_SCENE_SOURCE',generationPrompt:'Use case: high-school Rajasthan geography textbook scene. Asset type: wide representative pastoral ecology illustration. Scene: open Thar Desert rangeland in western Rajasthan, a small mixed herd of hardy local-style sheep and goats grazing sparse dry grasses, one camel in the background, a distant khejri tree, soft evening light, natural ochre and muted olive palette. Style: polished realistic gouache-meets-editorial illustration, respectful and educational, animals anatomically plausible and not identifiable as specific registered breeds. Landscape 3:2, clear foreground animals, uncluttered. No people, buildings, text, signage, watermark, or specific location. Representative illustration only, not a literal depiction.',sourceReferences:['assets/content/rassetu/rassetu_book2.json#ch13/2.1']}];

function sha(buf){return crypto.createHash('sha256').update(buf).digest('hex');}
function digest(v){return sha(Buffer.from(JSON.stringify(v,Object.keys(v).sort())));}
function canonical(value){if(Array.isArray(value))return value.map(canonical);if(value&&typeof value==='object')return Object.fromEntries(Object.keys(value).sort().map(k=>[k,canonical(value[k])]));return value;}
function stableHash(v){return sha(Buffer.from(JSON.stringify(canonical(v))));}
function sourceSnapshot(ch){
 const content=ch.content,remove=new Set();
 content.forEach((b,i)=>{if(b?.type!=='image')return;remove.add(i);for(const j of [i+1,i-1])if(j>=0&&j<content.length&&content[j]?.type==='callout'&&String(content[j].value||'').startsWith('**चित्र से सीखें')){remove.add(j);break;}});
 return {...ch,content:content.filter((_,i)=>!remove.has(i))};
}
function findAnchor(ch,anchor){const matches=[];ch.content.forEach((b,i)=>{if(b.type==='text'&&b.value.startsWith(anchor))matches.push(i);});if(matches.length!==1)throw new Error(`${ch.id}: expected one exact anchor ${anchor}; found ${matches.length}`);return matches[0];}

async function main(){
 fs.mkdirSync(svgDir,{recursive:true});
 const book=JSON.parse(fs.readFileSync(bookPath,'utf8'));
 const placements=[];
 for(const g of graphics){
  const svgText=svg(g.title,g.body()); const svgPath=path.join(svgDir,g.id+'.svg'); const imageName=g.id+'.webp'; const imagePath=path.join(imgDir,imageName);
  fs.writeFileSync(svgPath,svgText); await sharp(Buffer.from(svgText)).webp({quality:88,effort:6}).toFile(imagePath);
  const ch=book.chapters.find(c=>c.id===g.chapter); if(!ch)throw new Error('Missing chapter '+g.chapter);
  const imageIndex=ch.content.findIndex(b=>b.type==='image'&&b.value===imageName);
  if(imageIndex<0){const idx=findAnchor(ch,g.anchor);ch.content.splice(idx+1,0,{type:'image',value:imageName,caption:g.caption},{type:'callout',value:'**चित्र से सीखें — सांकेतिक प्रक्रिया-आरेख**\n\n'+g.explanation});}
  else if(ch.content[imageIndex+1]?.type==='callout'){ch.content[imageIndex+1].value='**चित्र से सीखें — सांकेतिक प्रक्रिया-आरेख**\n\n'+g.explanation;}
  const source=sourceSnapshot(ch); placements.push({book:2,chapter:g.chapter,originalChapterSha256:stableHash(source),sourceContentSha256:stableHash(source.content),anchor:g.anchor,image:imageName,assetSha256:sha(fs.readFileSync(imagePath)),caption:g.caption,explanation:g.explanation,assetType:'editable-vector-diagram',sourceReferences:g.sourceReferences||['assets/content/rassetu/rassetu_book2.json#'+g.chapter+'/'+g.anchor]});
 }
 for(const scene of scenes){
  const srcScene=process.env[scene.sourceEnv],scenePath=path.join(imgDir,scene.id+'.webp');
  if(!fs.existsSync(scenePath)){if(!srcScene||!fs.existsSync(srcScene))throw new Error('Missing generated scene input for '+scene.id);await sharp(srcScene).resize({width:1440,withoutEnlargement:true}).webp({quality:88,effort:6}).toFile(scenePath);}
  const ch=book.chapters.find(c=>c.id===scene.chapter);const imageName=scene.id+'.webp';
  const imageIndex=ch.content.findIndex(b=>b.type==='image'&&b.value===imageName);
  if(imageIndex<0){const idx=findAnchor(ch,scene.anchor);ch.content.splice(idx+(scene.afterOffset||1),0,{type:'image',value:imageName,caption:scene.caption},{type:'callout',value:'**चित्र से सीखें — प्रतिनिधि चित्रण**\n\n'+scene.explanation});}
  else if(ch.content[imageIndex+1]?.type==='callout'){ch.content[imageIndex+1].value='**चित्र से सीखें — प्रतिनिधि चित्रण**\n\n'+scene.explanation;}
  const source=sourceSnapshot(ch);
  placements.push({book:2,chapter:scene.chapter,originalChapterSha256:stableHash(source),sourceContentSha256:stableHash(source.content),anchor:scene.anchor,image:imageName,assetSha256:sha(fs.readFileSync(scenePath)),caption:scene.caption,explanation:scene.explanation,assetType:'generated-representative-image',generationPrompt:scene.generationPrompt,sourceReferences:scene.sourceReferences});
 }
 fs.writeFileSync(bookPath,JSON.stringify(book,null,2)+'\n','utf8');
 fs.writeFileSync(manifestPath,JSON.stringify({version:1,batch:'Book 2 continuation — uncovered geography topics',asset:'assets/content/rassetu/rassetu_book2.json',chapters:placements},null,2)+'\n','utf8');
 console.log('Integrated '+placements.length+' Book 2 continuation entries ('+graphics.length+' vector diagrams and '+scenes.length+' representative scenes).');
}
main().catch(e=>{console.error(e);process.exit(1)});
