// Book 3 graphics continuation: verified vector teaching visuals + three generated scenes.
const fs = require('fs');
const path = require('path');
const crypto = require('crypto');
const sharp = require('C:/Users/rishi/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/sharp');

const root = path.resolve(__dirname, '..');
const bookPath = path.join(root, 'assets/content/rassetu/rassetu_book3.json');
const manifestPath = path.join(root, 'artifacts/rassetu_series/book3_completion_manifest.json');
const svgDir = path.join(root, 'artifacts/rassetu_series/svg');
const imageDir = path.join(root, 'assets/images');
const planPath = path.join(root, 'artifacts/rassetu_series/book3_graphics_plan.md');
const palette = { ink:'#213b36', muted:'#58716a', green:'#337c64', blue:'#3979a6', rust:'#b96446', gold:'#d6a342', pale:'#f2f6f2', sky:'#eaf3f8', sand:'#f3e8d0', line:'#b8ccc2', white:'#fffdf8', purple:'#796aa8' };
const sourceUrls = {
  harappan:'https://ncert.nic.in/textbook/pdf/lehs101.pdf',
  ancient:'https://ncert.nic.in/textbook/pdf/lehs102.pdf',
  thinkers:'https://ncert.nic.in/textbook/pdf/lehs104.pdf',
  vijayanagara:'https://www.ncert.nic.in/textbook/pdf/lehs203.pdf',
  mughal:'https://ncert.nic.in/textbook/pdf/lehs204.pdf',
  bhakti:'https://ncert.nic.in/textbook/pdf/gess106.pdf',
  trade:'https://www.ncert.nic.in/textbook/pdf/hess202.pdf',
  revolt:'https://www.ncert.nic.in/textbook/pdf/hess205.pdf',
  reforms:'https://www.ncert.nic.in/textbook/pdf/hess208.pdf',
  nationalism:'https://www.ncert.nic.in/textbook/pdf/hess209.pdf',
  peasant:'https://www.ncert.nic.in/textbook/pdf/hess203.pdf',
  cabinet:'https://www.nationalarchives.gov.uk/explore-the-collection/stories/indian-independence-part-two/',
  reorg:'https://www.indiacode.nic.in/bitstream/123456789/1680/1/a1956-37.pdf'
};
const generated = [
  { id:'rassetu_b3_harappan_scene', chapter:'ch01', anchor:'### 2. नगर नियोजन एवं वास्तुकला (Town Planning & Architecture)', file:'exec-e78113a5-b00a-4105-b203-526a1c54e175.png', caption:'हड़प्पाई नगर-जीवन का प्रतिनिधि पुनर्निर्माण', explanation:'ईंटों के घर, सड़क और जल-निकास पर आधारित प्रतिनिधि दृश्य। यह किसी एक उत्खनित नगर का हूबहू पुनर्निर्माण नहीं है; पुरातात्विक साक्ष्य से कुछ विवरण ही ज्ञात हैं।', prompt:'Use case: historical-scene. Asset type: wide educational textbook illustration. Primary request: representative archaeological reconstruction of an Indus urban street with planned street lines, brick houses, a household well and visible covered drain. Scene: generic Bronze Age city neighborhood, not a named site. Style: naturalistic editorial gouache, historically informed. Composition: landscape 3:2, street-level oblique view. Constraints: representative reconstruction only; no named person/site, no text, labels, signage, watermark, modern infrastructure, speculative dockyard or exact dimensions.' },
  { id:'rassetu_b3_chola_town_scene', chapter:'ch11', anchor:'### 1. संगम युग (300 ई.पू. - 300 ई.): राज्य, समाज एवं साहित्य', file:'exec-232c51a3-fe45-48e6-875f-502a5f68cf29.png', caption:'दक्षिण भारतीय मंदिर-नगर: प्रतिनिधि दृश्य', explanation:'मंदिर, शिल्प और नगर-जीवन से प्रेरित प्रतिनिधि चित्रण। किसी विशिष्ट चोल मंदिर, नगर, व्यक्ति या ऐतिहासिक घटना का सटीक दृश्य नहीं।', prompt:'Use case: historical-scene. Asset type: wide educational textbook illustration. Primary request: representative medieval South Indian temple-town scene connecting temple architecture, craft activity and community life. Scene: a generic Chola-period Tamil town; distant Dravidian-style stone tower, shaded market lane, artisans at work. Style: refined editorial gouache, historically informed. Composition: landscape 3:2. Constraints: representative only; no named temple/person, no exact inscription, no text, signage, watermark, modern objects or famous monument replica.' },
  { id:'rassetu_b3_revolt_1857_scene', chapter:'ch27', anchor:'### 2.1 1857 के महान विद्रोह के बहुआयामी एवं संचयी कारण', file:'exec-fac7f536-a02e-4ca8-bac4-0b135aaa4c84.png', caption:'1857 के उथल-पुथल का प्रतिनिधि दृश्य', explanation:'सिपाहियों और नागरिकों के विस्थापन से प्रेरित गैर-दस्तावेजी प्रतिनिधि दृश्य। यह किसी विशिष्ट नगर, युद्ध, व्यक्ति या दिन का चित्रण नहीं है।', prompt:'Use case: historical-scene. Asset type: wide educational textbook illustration. Primary request: representative, non-documentary scene evoking the upheaval of the 1857 uprising in north India without depicting a specific battle or named person. Scene: dusty town-edge road, small mixed group of Indian sepoys and civilians moving together, simple period settlement in the distance. Style: restrained realistic editorial gouache. Composition: landscape 3:2, no dramatic combat. Constraints: illustrative atmosphere only; no identifiable portraits, specific event/city, text, labels, signage, watermark, gore, graphic violence or modern objects.' }
];

const esc = s => String(s).replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&apos;'}[c]));
const t = (x,y,s,size=28,fill=palette.ink,weight=500,anchor='middle') => `<text x="${x}" y="${y}" text-anchor="${anchor}" fill="${fill}" font-size="${size}" font-weight="${weight}" font-family="Noto Sans Devanagari, Nirmala UI, sans-serif">${esc(s)}</text>`;
const line = (x1,y1,x2,y2,color=palette.line,width=4,dash='') => `<line x1="${x1}" y1="${y1}" x2="${x2}" y2="${y2}" stroke="${color}" stroke-width="${width}" ${dash?`stroke-dasharray="${dash}"`:''}/>`;
const rect = (x,y,w,h,fill=palette.white,stroke=palette.line,r=24) => `<rect x="${x}" y="${y}" width="${w}" height="${h}" rx="${r}" fill="${fill}" stroke="${stroke}" stroke-width="3"/>`;
const circle = (x,y,r,fill=palette.green,stroke='none',sw=0) => `<circle cx="${x}" cy="${y}" r="${r}" fill="${fill}" stroke="${stroke}" stroke-width="${sw}"/>`;
const arrow = (x1,y1,x2,y2,color=palette.green) => `<path d="M${x1} ${y1} L${x2} ${y2}" stroke="${color}" stroke-width="5" fill="none" marker-end="url(#arrow)"/>`;
function label(x,y,lines,color=palette.ink,size=24,anchor='middle',weight=600,gap=31){return lines.map((s,i)=>t(x,y+i*gap,s,size,color,weight,anchor)).join('');}
function base(id,title,subtitle,body,map=false,source='पाठ्यपुस्तक-आधारित शिक्षण-आरेख'){
 const footer=map?'रेखाचित्र सांकेतिक है — पैमाने पर नहीं':'अवधारणा-आरेख — ऐतिहासिक विवरण पाठ में देखें';
 const short=[...subtitle].length>112?[...subtitle].slice(0,109).join('')+'…':subtitle;
 return `<svg xmlns="http://www.w3.org/2000/svg" width="1800" height="1200" viewBox="0 0 1800 1200"><defs><marker id="arrow" markerWidth="12" markerHeight="12" refX="9" refY="6" orient="auto"><path d="M0 0 L12 6 L0 12 z" fill="${palette.green}"/></marker><linearGradient id="wash" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#f8f7ef"/><stop offset="1" stop-color="#eef5f1"/></linearGradient></defs><rect width="1800" height="1200" fill="url(#wash)"/>${t(900,66,title,43,palette.ink,750)}${t(900,112,short,22,palette.muted,500)}<path d="M70 142 H1730" stroke="${palette.line}" stroke-width="3"/>${body}<path d="M70 1120 H1730" stroke="${palette.line}" stroke-width="2"/>${t(900,1159,`${footer} · ${source}`,19,palette.muted,500)}</svg>`;
}
function plot(lon,lat){return [110+(lon-60)*45,1020-(lat-18)*52];}
function indiaShape(x=80,y=180,sx=1,sy=1){return `<path d="M${x+160*sx} ${y+0*sy} L${x+310*sx} ${y+18*sy} L${x+370*sx} ${y+100*sy} L${x+330*sx} ${y+170*sy} L${x+280*sx} ${y+220*sy} L${x+250*sx} ${y+320*sy} L${x+190*sx} ${y+415*sy} L${x+140*sx} ${y+340*sy} L${x+95*sx} ${y+245*sy} L${x+70*sx} ${y+150*sy} L${x+0*sx} ${y+105*sy} L${x+55*sx} ${y+40*sy} Z" fill="#e5ebda" stroke="${palette.green}" stroke-width="4"/>`;}
function siteDot(lon,lat,name,dx=15,dy=-13,anchor='start'){const [x,y]=plot(lon,lat);return `${circle(x,y,9,palette.rust)}${t(x+dx,y+dy,name,20,palette.ink,650,anchor)}`;}
function timeline(items,y=835,x0=150,x1=1650){const gap=(x1-x0)/(items.length-1);return line(x0,y,x1,y,palette.green,5)+items.map((it,i)=>{const x=x0+i*gap;return `${circle(x,y,13,it.color||palette.rust)}${line(x,y+(i%2?12:-12),x,y+(i%2?78:-76),palette.line,3)}${label(x,y+(i%2?116:-94),Array.isArray(it.label)?it.label:[it.label],palette.ink,20,'middle',600,28)}${t(x,y+26,it.date,18,palette.muted,600)}`;}).join('');}

const graphics = [
 {id:'rassetu_b3_harappan_sites_planning',chapter:'ch01',anchor:'### 3. प्रमुख पुरातात्विक स्थल एवं उनके विशिष्ट साक्ष्य',caption:'हड़प्पाई स्थल और नगर-योजना का पुरातात्विक साक्ष्य',explanation:'मुख्य स्थलों को नदी-मैदानों और तटीय क्षेत्रों के सापेक्ष रखें। मोहेंजोदड़ो का रेखाचित्र केवल सड़क-जाल, ऊंचे भाग/निचले नगर और नालियों के साक्ष्य को समझाता है; यह किसी पूरी बस्ती का मापित नक्शा नहीं।',sourceRefs:['assets/content/rassetu/rassetu_book3.json#ch01/### 3. प्रमुख पुरातात्विक स्थल एवं उनके विशिष्ट साक्ष्य',sourceUrls.harappan],map:true,body:()=>{
   let s=rect(65,175,1020,875,palette.white,palette.line,28)+rect(1110,175,625,875,'#fbf8ef',palette.line,28);
   s+=t(575,220,'परिपक्व हड़प्पाई स्थलों के सापेक्ष स्थान',28,palette.ink,700)+`<path d="M210 285 C330 365 340 460 395 555 S500 740 525 920" fill="none" stroke="#6e9ec0" stroke-width="9"/><path d="M635 305 C635 430 700 470 675 600 S650 770 630 900" fill="none" stroke="#91b59d" stroke-width="6" stroke-dasharray="14 10"/>`;
   s+=t(250,370,'सिंधु',18,'#3979a6',600)+t(690,393,'घग्गर-हकरा क्षेत्र',18,'#4c8b6b',600);
   s+=siteDot(72.9,30.6,'हड़प्पा',15,-12)+siteDot(68.1,27.3,'मोहनजोदड़ो',15,-12)+siteDot(76.1,29.3,'राखीगढ़ी',62,-21)+siteDot(74.1,29.5,'कालीबंगन',-88,48,'end')+siteDot(70.2,23.9,'धोलावीरा',-16,-15,'end')+siteDot(72.3,22.5,'लोथल',18,25)+siteDot(75.4,29.6,'बनावली',60,47)+siteDot(76.2,32.8,'मांडा',16,-10);
   s+=t(1420,230,'मोहनजोदड़ो का साक्ष्य-आधारित संकेत',25,palette.ink,700);
   s+=`<path d="M1185 345 H1665 M1185 465 H1665 M1185 585 H1665 M1185 705 H1665 M1185 825 H1665" stroke="#bdcfc4" stroke-width="2"/>`;
   s+=label(1200,330,['ग्रिड-जैसी सड़कें','लगभग समकोण पर मिलती गलियां'],palette.ink,22,'start',600,31);
   s+=label(1200,450,['ऊंचा भाग और निचला नगर','दोनों में नियोजित निर्माण के संकेत'],palette.ink,22,'start',600,31);
   s+=label(1200,570,['घर से गली-नाली तक','निकास और ढके नालों के अवशेष'],palette.ink,22,'start',600,31);
   s+=label(1200,690,['आंगन और कुएं','घरेलू वास्तु के विविध उदाहरण'],palette.ink,22,'start',600,31);
   s+=label(1200,810,['भिन्न स्थल, भिन्न रूप','धोलावीरा/लोथल में स्थानीय विविधता'],palette.ink,22,'start',600,31);
   s+=t(1420,960,'किसी विवादित “गोदी” का दावा शामिल नहीं',20,palette.rust,700);
   return s;
 }},
 {id:'rassetu_b3_vedic_geography_shift',chapter:'ch03',anchor:'### 1. ऋग्वैदिक काल (1500 - 1000 ई.पू.): कबीलाई जनतंत्र एवं संस्थाएं',caption:'वैदिक काल: क्षेत्रीय विस्तार का सांकेतिक मॉडल',explanation:'पाठ के अनुसार ऋग्वैदिक संदर्भ उत्तर-पश्चिमी नदी-क्षेत्र से जुड़ते हैं और उत्तर-वैदिक संदर्भ गंगा-यमुना क्षेत्र की ओर अधिक फैलते हैं। सीमाएं सांकेतिक हैं, न कि निश्चित राजनीतिक सरहदें।',sourceRefs:['assets/content/rassetu/rassetu_book3.json#ch03/ऋग्वैदिक काल',sourceUrls.ancient],map:true,body:()=>{
   let s=rect(75,190,780,770,palette.white,palette.line,30)+rect(945,190,780,770,palette.white,palette.line,30);
   s+=t(465,250,'ऋग्वैदिक संदर्भ',30,palette.ink,700)+t(1335,250,'उत्तर-वैदिक संदर्भ',30,palette.ink,700);
   s+=`<path d="M160 365 C270 330 355 390 445 455 S620 565 765 705" fill="none" stroke="#76a2bd" stroke-width="12"/><path d="M1030 375 C1120 430 1165 520 1225 655 S1420 735 1640 830" fill="none" stroke="#76a2bd" stroke-width="12"/><path d="M1065 340 C1145 445 1260 520 1375 685" fill="none" stroke="#9bc4ab" stroke-width="8"/>`;
   s+=label(280,360,['सिंधु-क्षेत्र'],palette.blue,24,'middle',700)+label(515,500,['सरस्वती','संदर्भ'],palette.green,21,'middle',700,26)+label(1210,490,['यमुना'],palette.blue,23,'middle',700)+label(1490,625,['गंगा'],palette.green,23,'middle',700);
   s+=`<ellipse cx="430" cy="580" rx="245" ry="170" fill="none" stroke="${palette.rust}" stroke-width="5" stroke-dasharray="16 12"/><ellipse cx="1350" cy="620" rx="275" ry="210" fill="none" stroke="${palette.rust}" stroke-width="5" stroke-dasharray="16 12"/>`;
   s+=t(465,835,'आरंभिक वैदिक पाठ में प्रमुख',20,palette.muted,600)+t(1335,885,'बाद के पाठों में पूर्व की ओर बढ़ता संदर्भ',20,palette.muted,600);
   s+=arrow(790,565,1000,565,palette.rust)+t(895,535,'पूर्व की ओर',20,palette.rust,700);
   return s;
 }},
 {id:'rassetu_b3_mahajanapada_magadh',chapter:'ch05',anchor:'### 1. द्वितीय नगरीकरण एवं 16 महाजनपदों की राजनीतिक व्यवस्था',caption:'16 महाजनपद और मगध के उत्कर्ष का स्थानिक संदर्भ',explanation:'नाम और स्थान का सामान्यीकृत अध्ययन-मानचित्र। अलग-अलग महाजनपदों की वास्तविक सीमाएं आधुनिक राज्य-सीमाओं जैसी स्थिर रेखाएं नहीं थीं। मगध के उत्कर्ष के कारण अध्याय में दिए गए भूगोल, संसाधन और राजनीतिक संदर्भ के साथ पढ़ें।',sourceRefs:['assets/content/rassetu/rassetu_book3.json#ch05/महाजनपद',sourceUrls.ancient],map:true,body:()=>{
   let s=rect(60,175,1150,890,palette.white,palette.line,28)+rect(1240,175,495,890,'#faf7ee',palette.line,28);
   s+=`<path d="M180 370 C360 470 550 490 780 560 S1020 700 1125 820" fill="none" stroke="#73a2bd" stroke-width="9"/><path d="M230 680 C425 620 615 675 790 745" fill="none" stroke="#92b69f" stroke-width="7"/>`;
   s+=t(650,230,'उत्तर भारत के जनपदों का स्थानिक अनुमान',25,palette.ink,700);
   const dots=[['कम्बोज',68,34],['गांधार',72,34],['कुरु',77,29],['पांचाल',79,28.5],['मत्स्य',76.3,27],['शूरसेन',78.1,27],['वत्स',81,25.5],['अवंति',76,23],['चेदि',80,24],['काशी',83,25],['कोसल',82,26.8],['मल्ल',83.5,26.4],['वज्जि',85,26.2],['अंग',87,25],['मगध',85.5,24.5],['अश्मक',78,19.5]];
   dots.forEach(([n,lon,lat],i)=>{const x=145+(lon-67)*42,y=860-(lat-19)*36;s+=circle(x,y,10,i===14?palette.rust:palette.green)+t(x+(i%2?15:-12),y+(i%3===0?-12:25),`${i+1}`,18,palette.ink,700,i%2?'start':'end');});
   s+=t(1475,230,'मानचित्र की कुंजी',27,palette.ink,700);
   for(let i=0;i<dots.length;i++){const col=i<8?0:1,row=i<8?i:i-8;const x=1275+col*220,y=300+row*68;s+=circle(x,y-8,9,i===14?palette.rust:palette.green)+t(x+20,y,dots[i][0],19,palette.ink,600,'start');}
   s+=t(1490,930,'मगध का उत्कर्ष',23,palette.rust,700)+label(1490,970,['हर्यक → शिशुनाग → नंद','राजवंश-क्रम पाठानुसार'],palette.ink,18,'middle',600,28);
   return s;
 }},
 {id:'rassetu_b3_buddhism_jainism_compare',chapter:'ch05',anchor:'### 3. बौद्ध धर्म: दर्शन, आचार संहिता एवं संगीतियां',caption:'बौद्ध और जैन शिक्षाएं: तुलना और साधना-पथ',explanation:'दोनों श्रमण परंपराओं के अपने सिद्धांत और आचार हैं। बौद्ध चार आर्य सत्य/अष्टांगिक मार्ग तथा जैन त्रिरत्न/महाव्रत को अलग-अलग रखें; यह संक्षिप्त तुलना है, पूर्ण दर्शन-सार नहीं।',sourceRefs:['assets/content/rassetu/rassetu_book3.json#ch05/बौद्ध धर्म और जैन धर्म',sourceUrls.thinkers],map:false,body:()=>{
   let s=rect(70,190,790,820,'#edf4f8','#8caec0',36)+rect(940,190,790,820,'#f5f0e6','#d5b36a',36);
   s+=t(465,258,'बौद्ध परंपरा',32,palette.blue,750)+t(1335,258,'जैन परंपरा',32,palette.rust,750);
   s+=circle(465,390,74,'#dcecf4',palette.blue,4)+t(465,380,'दुःख',22,palette.ink,700)+t(465,412,'और निरोध',20,palette.ink,600);
   const truths=['दुःख','समुदय','निरोध','मार्ग'];truths.forEach((v,i)=>{const x=210+i*170;s+=circle(x,545,42,[palette.blue,palette.rust,palette.green,palette.gold][i])+t(x,553,v,19,'white',700);if(i<truths.length-1)s+=arrow(x+49,545,x+120,545,palette.blue);});
   s+=t(465,660,'अष्टांगिक मार्ग',27,palette.ink,700);
   s+=label(465,710,['सम्यक् दृष्टि · संकल्प · वाक् · कर्म','आजीविका · प्रयास · स्मृति · समाधि'],palette.ink,20,'middle',600,32);
   s+=circle(1335,390,74,'#f5e9cc',palette.rust,4)+t(1335,380,'आत्म-संयम',22,palette.ink,700)+t(1335,412,'और मुक्ति',20,palette.ink,600);
   s+=circle(1335,548,62,'#f1d9aa',palette.gold,4)+t(1335,556,'त्रिरत्न',23,palette.ink,700);
   const jewels=['सम्यक् दर्शन','सम्यक् ज्ञान','सम्यक् चरित्र'];jewels.forEach((v,i)=>{const x=1100+i*235;s+=circle(x,690,30,[palette.green,palette.blue,palette.rust][i])+t(x,746,v,19,palette.ink,600);});
   s+=line(1075,815,1595,815,palette.line,4)+t(1335,865,'पंच महाव्रत',25,palette.ink,700)+label(1335,910,['अहिंसा · सत्य · अस्तेय','अपरिग्रह · ब्रह्मचर्य'],palette.ink,20,'middle',600,32);
   return s;
 }},
 {id:'rassetu_b3_maurya_saptanga_edicts',chapter:'ch07',anchor:'### 2. कौटिल्य का अर्थशास्त्र एवं मौर्य प्रशासनिक ढांचा',caption:'मौर्यकालीन राज्य-विचार: सप्तांग सिद्धांत',explanation:'अर्थशास्त्र का सप्तांग राज्य-विचार सात परस्पर जुड़े घटक बताता है। यह प्रशासनिक पदक्रम नहीं है; धम्म और अभिलेखों के लिए आगे के अनुभाग देखें।',sourceRefs:['assets/content/rassetu/rassetu_book3.json#ch07/मौर्य प्रशासन',sourceUrls.ancient],map:false,body:()=>{
   const cx=900,cy=620,r=300;let s=`<circle cx="${cx}" cy="${cy}" r="${r}" fill="none" stroke="${palette.line}" stroke-width="10"/>`;
   const parts=[['स्वामी',-90],['अमात्य',-38],['जनपद',14],['दुर्ग',66],['कोष',118],['दण्ड',170],['मित्र',222]];
   for(const [n,d] of parts){const a=d*Math.PI/180,x=cx+Math.cos(a)*r,y=cy+Math.sin(a)*r;s+=line(cx+Math.cos(a)*85,cy+Math.sin(a)*85,x,y,palette.green,4)+circle(x,y,54,n==='स्वामी'?palette.rust:'#e5f0e9',n==='स्वामी'?palette.rust:palette.green,4)+t(x,y+8,n,23,n==='स्वामी'?'white':palette.ink,700);}
   s+=circle(cx,cy,95,'#f1e6c9',palette.gold,5)+label(cx,cy-8,['राज्य','सात अंगों का','परस्पर संबंध'],palette.ink,23,'middle',700,31);
   s+=label(900,1040,['राज्य-विचार: सात घटक साथ मिलकर राजनीतिक क्षमता बनाते हैं','प्रत्येक अंग का अर्थ और उदाहरण पाठ के साथ पढ़ें'],palette.muted,21,'middle',600,31);
   return s;
 }},
 {id:'rassetu_b3_gupta_harsha_knowledge',chapter:'ch09',anchor:'### 3. प्राचीन भारत की वैज्ञानिक एवं बौद्धिक परंपराएं',caption:'गुप्त और गुप्तोत्तर काल: ज्ञान-परंपरा के कुछ पड़ाव',explanation:'गुप्त काल और हर्ष के समय की चुनी हुई साहित्यिक, वैज्ञानिक और शिक्षण परंपराएं। काल-रेखाएं व्यापक हैं; व्यक्तियों/रचनाओं का सटीक काल और संबद्धता पाठ में जांचें।',sourceRefs:['assets/content/rassetu/rassetu_book3.json#ch09/वैज्ञानिक और बौद्धिक परंपराएं',sourceUrls.ancient,sourceUrls.thinkers],map:false,body:()=>{
   let s=line(160,640,1640,640,palette.green,7);
   const eras=[{x:280,top:'गुप्त काल',dates:'लगभग चौथी–छठी शताब्दी',items:['आर्यभट — गणित/खगोल','कालिदास — साहित्य']},{x:760,top:'ज्ञान और संस्थान',dates:'कालगत विविधता',items:['नालंदा — शिक्षण केंद्र','कला/मूर्तिकला की परंपराएं']},{x:1260,top:'हर्ष का काल',dates:'सातवीं शताब्दी',items:['हर्ष — उत्तर भारत का शासक','बाणभट्ट — साहित्यिक स्रोत']}];
   eras.forEach((e,i)=>{s+=circle(e.x,640,18,[palette.rust,palette.blue,palette.green][i])+line(e.x,620,e.x,380,palette.line,4)+line(e.x,660,e.x,845,palette.line,4)+t(e.x,305,e.top,29,palette.ink,750)+t(e.x,352,e.dates,20,palette.muted,600)+label(e.x,415,e.items,palette.ink,21,'middle',600,34)+circle(e.x,875,32,[palette.rust,palette.blue,palette.green][i])+t(e.x,925,'चयनित उदाहरण',17,palette.muted,600);});
   s+=t(900,1035,'“स्वर्ण युग” एक मूल्यांकन-विषय है; इसे निर्विवाद सार्वभौमिक तथ्य न मानें',20,palette.rust,650);
   return s;
 }},
 {id:'rassetu_b3_south_india_governance',chapter:'ch11',anchor:'### 5. चोल प्रशासन एवं स्थानीय स्वशासन की प्रणाली',caption:'दक्षिण भारत के प्रमुख सत्ता-केंद्र और चोल स्थानीय संस्थाएं',explanation:'सत्ता-केंद्रों की अवस्थिति सांकेतिक है। चोल-कालीन स्थानीय संस्थाओं के नाम और कार्य अध्याय से पढ़ें; यह आधुनिक पंचायत व्यवस्था के समान नहीं है।',sourceRefs:['assets/content/rassetu/rassetu_book3.json#ch11/चोल प्रशासन और स्थानीय स्वशासन',sourceUrls.vijayanagara],map:true,body:()=>{
   let s=rect(65,180,820,850,palette.white,palette.line,28)+rect(930,180,805,850,'#f9f7ef',palette.line,28);
   s+=t(475,235,'दक्षिण भारत: सत्ता-केंद्र (सांकेतिक)',25,palette.ink,700);
   s+=`<path d="M220 345 C440 300 685 365 765 530 S650 800 430 890" fill="none" stroke="#6f9fc0" stroke-width="8"/><path d="M190 780 C360 710 520 690 750 655" fill="none" stroke="#99b9a3" stroke-width="5" stroke-dasharray="12 9"/>`;
   const points=[['कांची',80,13,14,-12],['बादामी',76,16,14,-12],['तंजावुर',79,11,15,30],['गंगैकोंडचोलपुरम्',79.5,12,15,-20],['मदुरै',78,9,15,28]];
   points.forEach(([n,lon,lat,dx,dy])=>{const x=140+(lon-74)*95,y=890-(lat-8)*85;s+=circle(x,y,10,palette.rust)+t(x+dx,y+dy,n,18,palette.ink,600,'start');});
   s+=t(1330,235,'स्थानीय संस्थाएं — भिन्न भूमिकाएं',27,palette.ink,700);
   s+=circle(1330,390,72,'#dcece3',palette.green,4)+t(1330,398,'ग्राम',24,palette.ink,700);
   s+=line(1120,510,1540,510,palette.green,5)+circle(1120,510,14,palette.rust)+circle(1330,510,14,palette.blue)+circle(1540,510,14,palette.gold);
   s+=t(1120,558,'ऊर',23,palette.ink,700)+t(1330,558,'सभा',23,palette.ink,700)+t(1540,558,'नगरम्',23,palette.ink,700);
   s+=label(1120,610,['सामान्य ग्राम','स्थानीय निकाय'],palette.muted,18,'middle',500,27)+label(1330,610,['ब्राह्मदेय ग्राम','सभा'],palette.muted,18,'middle',500,27)+label(1540,610,['व्यापारी/नगर','संबद्ध निकाय'],palette.muted,18,'middle',500,27);
   s+=arrow(1330,690,1330,775,palette.green)+t(1330,830,'समितियां (वरियम)',23,palette.green,700)+label(1330,875,['विशिष्ट कार्य-विभाजन','और स्थानीय भागीदारी'],palette.ink,19,'middle',600,30);
   return s;
 }},
 {id:'rassetu_b3_delhi_sultanate_system',chapter:'ch13',anchor:'### 2. खिलजी क्रांति एवं अलाउद्दीन खिलजी के सुधार (1290-1320 ई.)',caption:'दिल्ली सल्तनत: राजवंश-क्रम और खिलजी बाजार-नियमन',explanation:'राजवंश-क्रम के साथ बाजार-नियमन का कारण-प्रक्रिया मॉडल। इसे पूरे सल्तनत काल में समान रूप से लागू व्यवस्था न मानें; विशेष विवरण अलाउद्दीन खिलजी के शासन से जुड़ा है।',sourceRefs:['assets/content/rassetu/rassetu_book3.json#ch13/दिल्ली सल्तनत',sourceUrls.ancient],map:false,body:()=>{
   const dyn=[['गुलाम','1206–1290'],['खिलजी','1290–1320'],['तुगलक','1320–1414'],['सैयद','1414–1451'],['लोदी','1451–1526']];let s=line(155,375,1645,375,palette.green,7);
   dyn.forEach((d,i)=>{const x=180+i*360;s+=circle(x,375,17,i===1?palette.rust:palette.green)+t(x,300,d[0],27,palette.ink,700)+t(x,335,d[1],19,palette.muted,600);});
   s+=rect(110,515,1580,480,'#f7f9f5',palette.line,28)+t(900,575,'अलाउद्दीन खिलजी: बाजार-नियमन का कारण-कार्य मॉडल',27,palette.ink,700);
   const steps=[['राज्य का लक्ष्य','सैन्य खर्च के बीच','सामान्य दरें बनाए रखना'],['बाजार निगरानी','दर/माप और आपूर्ति पर','अधिकारी नजर रखते'],['नियंत्रित खरीद','अनाज और वस्तुओं का','नियंत्रित वितरण'],['परीक्षा-बिंदु','व्यवस्था के नियम और','प्रभाव अलग-अलग पढ़ें']];
   steps.forEach((a,i)=>{const x=265+i*420;s+=circle(x,730,46,[palette.blue,palette.rust,palette.gold,palette.green][i])+t(x,739,String(i+1),26,'white',750)+label(x,830,a,palette.ink,20,'middle',650,31);if(i<3)s+=arrow(x+54,730,x+350,730,palette.green);});
   return s;
 }},
 {id:'rassetu_b3_vijayanagara_bahmani_1565',chapter:'ch15',anchor:"### 2. तालीकोटा का युद्ध (23 जनवरी 1565 ई.) — 'राक्षस-तंगड़ी का युद्ध'",caption:'विजयनगर और दक्कन: 1565 का स्थानिक संदर्भ',explanation:'1565 के संदर्भ में दक्षिणी दक्कन के शक्ति-केंद्रों का सांकेतिक स्थान-चित्र। यह राजनीतिक सीमाओं का सटीक मानचित्र नहीं है; राक्षस-तंगड़ी/तालीकोटा का युद्ध-बिंदु अनुमानित क्षेत्र के रूप में दिखाया गया है।',sourceRefs:['assets/content/rassetu/rassetu_book3.json#ch15/तालीकोटा का युद्ध',sourceUrls.vijayanagara],map:true,body:()=>{
   let s=rect(65,180,1060,850,palette.white,palette.line,28)+rect(1170,180,565,850,'#faf7ef',palette.line,28);
   s+=t(595,235,'दक्कन के शक्ति-केंद्र — 1565',27,palette.ink,700)+`<path d="M190 400 C365 345 555 390 780 465 S980 615 1050 790" fill="none" stroke="#6d9ec0" stroke-width="9"/><path d="M235 780 C445 710 620 690 875 755" fill="none" stroke="#9ab89f" stroke-width="5" stroke-dasharray="12 10"/>`;
   const pts=[['विजयनगर / हम्पी',76.5,15.3],['बहमनी उत्तराधिकार',76.3,17.9],['बीजापुर',75.7,16.8],['गोलकुंडा',78.5,17.4],['अहमदनगर',74.7,19.1],['तालीकोटा क्षेत्र',76,16.5]];
   pts.forEach((p,i)=>{const x=160+(p[1]-72)*112,y=880-(p[2]-13)*110;s+=circle(x,y, i===5?14:10,i===0?palette.green:i===5?palette.rust:palette.blue)+t(x+(i%2?16:-14),y+(i%2?27:-15),p[0],19,palette.ink,650,i%2?'start':'end');});
   s+=line(1240,290,1240,890,palette.line,5)+t(1450,245,'पढ़ने का ढांचा',26,palette.ink,700);
   s+=circle(1240,360,20,palette.green)+label(1490,350,['विजयनगर का दक्षिणी','साम्राज्यिक केंद्र'],palette.ink,20,'start',600,30);
   s+=circle(1240,520,20,palette.blue)+label(1490,510,['दक्कन की सल्तनतें','अलग सत्ता-केंद्र'],palette.ink,20,'start',600,30);
   s+=circle(1240,680,20,palette.rust)+label(1490,670,['राक्षस-तंगड़ी','युद्ध-संदर्भ: 1565'],palette.ink,20,'start',600,30);
   s+=label(1450,835,['क्षेत्रीय अवस्थिति','सीमा-रेखाएं नहीं'],palette.muted,19,'middle',600,30);
   return s;
 }},
 {id:'rassetu_b3_mughal_mansabdari_dahsala',chapter:'ch17',anchor:'### 3. अकबर की प्रशासनिक संस्थाएं: मनसबदारी एवं दहसाला व्यवस्था',caption:'मुगल प्रशासन: मनसब और दहसाला के अलग तंत्र',explanation:'मनसब में जात व्यक्तिगत पद/रैंक और सवार घुड़सवार दायित्व बताता है। दहसाला भूमि-राजस्व आकलन से जुड़ी व्यवस्था है। दोनों को एक ही प्रशासनिक प्रणाली न समझें।',sourceRefs:['assets/content/rassetu/rassetu_book3.json#ch17/मनसबदारी और दहसाला',sourceUrls.mughal],map:false,body:()=>{
   let s=rect(65,190,810,820,'#eef4f7','#91adbb',30)+rect(925,190,810,820,'#f7f2e6','#cfb26e',30);
   s+=t(470,255,'मनसबदारी: पद और दायित्व',30,palette.blue,750)+t(1330,255,'दहसाला: राजस्व आकलन',30,palette.rust,750);
   s+=circle(470,405,92,'#deedf3',palette.blue,5)+t(470,398,'मनसब',28,palette.ink,700)+t(470,435,'पद-रैंक',20,palette.muted,600);
   s+=line(470,500,470,570,palette.blue,5)+line(245,570,695,570,palette.blue,5)+circle(245,570,14,palette.blue)+circle(695,570,14,palette.rust);
   s+=t(245,625,'जात',25,palette.ink,700)+t(245,665,'व्यक्तिगत पद',19,palette.muted,600)+t(695,625,'सवार',25,palette.ink,700)+t(695,665,'घुड़सवार दायित्व',19,palette.muted,600);
   s+=label(470,775,['रैंक + नियुक्ति संबंध','सेवा-दायित्व पाठानुसार'],palette.ink,20,'middle',600,32);
   const st=[['भूमि','मापन/वर्गीकरण'],['उपज','क्षेत्रीय औसत'],['दर','मूल्य का संदर्भ'],['आकलन','राजस्व मांग']];st.forEach((a,i)=>{const x=1030+i*210;s+=circle(x,470,42,[palette.green,palette.gold,palette.blue,palette.rust][i])+t(x,478,String(i+1),24,'white',700)+label(x,550,a,palette.ink,18,'middle',650,28);if(i<3)s+=arrow(x+48,470,x+160,470,palette.rust);});
   s+=t(1330,710,'औसत उपज/मूल्य की गणना',22,palette.ink,700)+t(1330,755,'दस-वर्षीय संदर्भ (दहसाला)',21,palette.rust,700)+label(1330,835,['भूमि-राजस्व आकलन का प्रवाह','विवरण और क्षेत्रीय लागूकरण पाठ देखें'],palette.muted,19,'middle',600,30);
   return s;
 }},
 {id:'rassetu_b3_bhakti_sufi_network',chapter:'ch21',anchor:'### 2.2 भक्ति संप्रदाय: दार्शनिक मत एवं आचार्य परंपरा',caption:'भक्ति और सूफी परंपराएं: विविध पथ, अलग संस्थाएं',explanation:'भक्ति और सूफी धाराएं अनेक थीं। आचार्य, संत, सिलसिले और क्षेत्र अध्याय में दिए चयनित उदाहरण हैं; आरेख किसी एकीकृत या एकरेखीय आंदोलन का दावा नहीं करता।',sourceRefs:['assets/content/rassetu/rassetu_book3.json#ch21/भक्ति और सूफी परंपराएं',sourceUrls.bhakti],map:false,body:()=>{
   let s=rect(70,185,790,835,'#eef5f1','#8eb5a1',36)+rect(940,185,790,835,'#f5f1e8','#c7ad75',36);
   s+=t(465,250,'भक्ति परंपराएं',31,palette.green,750)+t(1335,250,'सूफी परंपराएं',31,palette.rust,750);
   s+=`<path d="M465 345 C350 420 300 505 245 620 M465 345 C465 450 465 500 465 620 M465 345 C580 420 630 505 685 620" fill="none" stroke="${palette.green}" stroke-width="5"/>`;
   s+=circle(465,345,66,'#d8eadf',palette.green,4)+t(465,353,'भक्ति',24,palette.ink,700);
   [['सगुण',245],['निर्गुण',465],['आचार्य परंपरा',685]].forEach((v,i)=>{s+=circle(v[1],620,54,[palette.blue,palette.gold,palette.rust][i])+t(v[1],628,v[0],19,'white',700);});
   s+=label(465,770,['चयनित भाषाएं, संत और क्षेत्र','अनेक मत और सामाजिक संदर्भ'],palette.ink,20,'middle',600,32);
   s+=circle(1335,350,64,'#f0dfba',palette.rust,4)+t(1335,358,'सिलसिला',22,palette.ink,700);
   s+=line(1110,500,1560,500,palette.rust,5)+circle(1110,500,18,palette.blue)+circle(1335,500,18,palette.rust)+circle(1560,500,18,palette.gold);
   s+=t(1110,545,'पीर',20,palette.ink,650)+t(1335,545,'खानकाह',20,palette.ink,650)+t(1560,545,'मुरीद',20,palette.ink,650);
   s+=arrow(1125,630,1545,630,palette.rust)+t(1335,690,'शिक्षा और आध्यात्मिक संबंध',20,palette.muted,600);
   s+=label(1335,780,['चिश्ती/सुहरावर्दी जैसे चयनित सिलसिले','समा और स्थानीय संदर्भ पाठानुसार'],palette.ink,19,'middle',600,31);
   s+=t(900,1080,'साझा भक्ति-भाषा का अर्थ समान दर्शन या समान संगठन नहीं',20,palette.purple,700);
   return s;
 }},
 {id:'rassetu_b3_european_expansion',chapter:'ch23',anchor:'### 2.1 यूरोपीय व्यापारिक कंपनियों का आगमन एवं नौसैनिक प्रभुत्व का संघर्ष',caption:'यूरोपीय व्यापार से औपनिवेशिक सत्ता तक: चुने हुए पड़ाव',explanation:'व्यापारिक उपस्थिति और क्षेत्रीय राजनीतिक सत्ता अलग चरण थे। यह सामान्यीकृत तटीय स्थान-चित्र और चुनी हुई तिथियां दिखाता है; आधुनिक राजनीतिक सीमाएं लागू नहीं की गई हैं।',sourceRefs:['assets/content/rassetu/rassetu_book3.json#ch23/यूरोपीय व्यापारिक कंपनियां',sourceUrls.trade],map:true,body:()=>{
   let s=rect(65,180,835,845,palette.white,palette.line,28)+rect(950,180,785,845,'#faf7ef',palette.line,28);
   s+=t(480,235,'तटीय व्यापारिक केंद्र (सांकेतिक)',25,palette.ink,700)+indiaShape(300,310,1.4,1.45);
   const coastal=[['सूरत',72.8,21.2],['गोवा',73.8,15.5],['कोच्चि',76.3,10],['मद्रास',80.3,13.1],['कलकत्ता',88.4,22.6]];
   coastal.forEach(([n,lon,lat],i)=>{const x=185+(lon-68)*27,y=860-(lat-8)*28;s+=circle(x,y,9,palette.rust)+t(x+(i%2?13:-13),y+(i%2?23:-13),n,17,palette.ink,600,i%2?'start':'end');});
   s+=t(1340,235,'व्यापार से सत्ता: अलग-अलग चरण',27,palette.ink,700);
   const steps=[['1498','पुर्तगाली समुद्री मार्ग'],['1600','ईस्ट इंडिया कंपनी'],['1757','प्लासी के बाद राजनीतिक प्रभाव'],['1764','बक्सर'],['1765','दीवानी अधिकार']];
   s+=line(1060,330,1060,860,palette.green,6);
   steps.forEach((a,i)=>{const y=345+i*122;s+=circle(1060,y,17,i>1?palette.rust:palette.blue)+t(1110,y+8,a[0],22,palette.rust,750,'start')+t(1245,y+8,a[1],20,palette.ink,600,'start');});
   s+=t(1340,970,'प्रवेश ≠ तत्काल भू-राजनीतिक नियंत्रण',20,palette.muted,700);
   return s;
 }},
 {id:'rassetu_b3_revolt_1857_centres',chapter:'ch27',anchor:'### 2.2 विद्रोह का प्रसार एवं प्रमुख केंद्र: विस्तृत सामरिक इतिहास',caption:'1857–58: विद्रोह के प्रमुख केंद्र और नेता',explanation:'मुख्य केंद्रों और अध्याय में उल्लिखित नेताओं का योजनात्मक स्थान-चित्र। यह विद्रोह के पूरे प्रसार या राजनीतिक सीमाओं का मानचित्र नहीं है।',sourceRefs:['assets/content/rassetu/rassetu_book3.json#ch27/1857 के प्रमुख केंद्र',sourceUrls.revolt],map:true,body:()=>{
   let s=rect(65,180,1030,850,palette.white,palette.line,28)+rect(1145,180,590,850,'#faf7ef',palette.line,28);
   s+=t(580,230,'उत्तर भारत के प्रमुख केंद्र · 1857–58',25,palette.ink,700)+indiaShape(330,310,1.35,1.4);
   const pts=[['बैरकपुर',88.4,22.8],['मेरठ',77.7,28.9],['दिल्ली',77.2,28.6],['कानपुर',80.3,26.5],['लखनऊ',80.9,26.8],['झांसी',78.6,25.4],['ग्वालियर',78.2,26.2],['जगदीशपुर',84.4,25.5]];
   pts.forEach(([n,lon,lat],i)=>{const x=180+(lon-70)*28,y=850-(lat-20)*30;s+=circle(x,y,11,palette.rust)+t(x,y+6,String(i+1),14,'white',750);});
   s+=t(1435,230,'चयनित नेतृत्व',27,palette.ink,700);
   const leaders=[['बैरकपुर','मंगल पांडे'],['मेरठ','सैनिक विद्रोह'],['दिल्ली','बहादुर शाह ज़फर'],['कानपुर','नाना साहब / तात्या टोपे'],['लखनऊ','बेगम हज़रत महल'],['झांसी','रानी लक्ष्मीबाई'],['ग्वालियर','रानी लक्ष्मीबाई'],['जगदीशपुर','कुँवर सिंह']];
   leaders.forEach((x,i)=>{const y=290+i*82;s+=circle(1197,y-7,13,[palette.blue,palette.rust,palette.green][i%3])+t(1197,y-2,String(i+1),12,'white',750)+t(1224,y,x[0],17,palette.rust,700,'start')+t(1224,y+27,x[1],17,palette.ink,600,'start');});
   return s;
 }},
 {id:'rassetu_b3_reform_movements',chapter:'ch29',anchor:'### 2.5 अन्य प्रमुख सामाजिक-धार्मिक सुधार आंदोलन',caption:'उन्नीसवीं सदी के सुधार आंदोलन: क्षेत्र और अलग प्राथमिकताएं',explanation:'सुधारकों/संस्थाओं के क्षेत्र, काल और विचार अलग थे। तिथियां अध्याय के अनुसार चुनी गई हैं; यह संपूर्ण सूची या एक साझा विचारधारा का दावा नहीं है।',sourceRefs:['assets/content/rassetu/rassetu_book3.json#ch29/सामाजिक-धार्मिक सुधार आंदोलन',sourceUrls.reforms],map:false,body:()=>{
   let s=line(200,970,1600,970,palette.line,3);
   const nodes=[['ब्रह्म समाज','बंगाल','1828',250,palette.blue],['प्रार्थना समाज','बंबई','1867',480,palette.green],['सत्यशोधक समाज','महाराष्ट्र','1873',710,palette.rust],['आर्य समाज','उत्तर भारत','1875',940,palette.gold],['अलीगढ़ आंदोलन','उत्तर भारत','1875+',1170,palette.purple],['रामकृष्ण मिशन','बंगाल','1897',1400,palette.blue],['थियोसोफिकल सोसाइटी','मद्रास केंद्र','1882+',1610,palette.green]];
   nodes.forEach((n,i)=>{const x=n[3],y=500+(i%2?70:-55);s+=line(x,y+60,x,970,n[4],4)+circle(x,y,52,n[4])+t(x,y+8,String(i+1),23,'white',750)+t(x,y-80,n[2],19,n[4],700)+label(x,y+110,[n[0],n[1]],palette.ink,18,'middle',650,28);});
   s+=t(900,260,'विभिन्न प्रतिक्रियाएं — शिक्षा, जाति, धर्म और सामाजिक सुधार',27,palette.ink,700);
   s+=`<path d="M160 400 C390 330 590 450 820 380 S1240 335 1640 405" fill="none" stroke="#d6e0d8" stroke-width="5"/>`;
   return s;
 }},
 {id:'rassetu_b3_early_nationalism',chapter:'ch31',anchor:'## 16.5 बंगाल विभाजन (1905 AD) — कारण, योजना एवं प्रतिक्रिया',caption:'कांग्रेस से स्वदेशी तक: आरंभिक राष्ट्रवाद के पड़ाव',explanation:'कांग्रेस के गठन से बंगाल विभाजन, स्वदेशी और सूरत-विभाजन तक चुने हुए पड़ाव। यह आरंभिक राष्ट्रवाद का संक्षिप्त कालक्रम है; बाद के आंदोलनों के लिए राष्ट्रीय आंदोलन के व्यापक चित्र को देखें।',sourceRefs:['assets/content/rassetu/rassetu_book3.json#ch31/प्रारंभिक राष्ट्रीय आंदोलन',sourceUrls.nationalism],map:false,body:()=>{
   const ev=[['1885','कांग्रेस की स्थापना'],['1905','बंगाल विभाजन · स्वदेशी'],['1906','कलकत्ता अधिवेशन'],['1907','सूरत विभाजन'],['1911','बंगाल विभाजन रद्द']];
   let s=line(180,600,1620,600,palette.green,8);
   ev.forEach((e,i)=>{const x=190+i*355;s+=circle(x,600,18,[palette.blue,palette.rust,palette.gold,palette.purple,palette.green][i])+line(x,578,x,420,palette.line,4)+line(x,622,x,785,palette.line,4)+t(x,360,e[0],29,palette.rust,750)+label(x,455,e[1].split(' · '),palette.ink,21,'middle',650,31)+label(x,850,[['संगठन','और याचिका'],['बहिष्कार','स्वदेशी'],['स्वराज','राजनीति'],['उदार/उग्र','मतभेद'],['औपनिवेशिक','निर्णय बदला']][i],palette.muted,18,'middle',550,28);});
   s+=t(900,1030,'समय-क्रम में संगठन, नीति और जन-आंदोलन की कड़ियां',21,palette.ink,650);
   return s;
 }},
 {id:'rassetu_b3_revolutionary_networks',chapter:'ch33',anchor:'## 17.3 क्रांतिकारी आंदोलन का प्रथम चरण (1897–1917 AD)',caption:'क्रांतिकारी गतिविधियां: क्षेत्रीय केंद्र और चरण',explanation:'अध्याय में उल्लिखित गतिविधियों के कुछ स्थान और दो व्यापक चरण। एक ही संगठन/रणनीति सभी क्षेत्रों में समान नहीं थी; स्थान-रेखाएं योजनात्मक हैं।',sourceRefs:['assets/content/rassetu/rassetu_book3.json#ch33/क्रांतिकारी आंदोलन',sourceUrls.nationalism],map:true,body:()=>{
   let s=rect(65,180,850,830,palette.white,palette.line,28)+rect(965,180,770,830,'#faf7ef',palette.line,28);
   s+=t(490,235,'क्षेत्रीय गतिविधि केंद्र (सांकेतिक)',25,palette.ink,700)+indiaShape(300,300,1.4,1.55);
   const pts=[['पुणे',73.9,18.5],['कोलकाता',88.4,22.6],['दिल्ली',77.2,28.6],['लाहौर',74.3,31.5],['चटगांव',91.8,22.4]];
   pts.forEach(([n,lon,lat],i)=>{const x=160+(lon-70)*32,y=855-(lat-15)*34;s+=circle(x,y,11,[palette.blue,palette.rust,palette.green][i%3])+t(x,y+5,String(i+1),13,'white',750);});
   s+=t(1350,235,'स्थान-संकेत',25,palette.ink,700);
   const placeKeys=['पुणे','दिल्ली','लाहौर','कोलकाता','चटगांव'];placeKeys.forEach((n,i)=>{const y=300+i*49;s+=circle(1060,y-6,12,[palette.blue,palette.rust,palette.green][i%3])+t(1060,y-1,String(i+1),12,'white',750)+t(1090,y,n,18,palette.ink,650,'start');});
   s+=line(1030,565,1680,565,palette.line,3)+circle(1085,665,34,palette.blue)+t(1085,673,'I',22,'white',750)+label(1400,650,['प्रथम चरण · 1897–1917','क्षेत्रीय गुप्त संगठन'],palette.ink,19,'middle',650,31);
   s+=circle(1085,830,34,palette.rust)+t(1085,838,'II',18,'white',750)+label(1400,815,['द्वितीय चरण · 1924–1934','HSRA · चटगांव'],palette.ink,19,'middle',650,31);
   return s;
 }},
 {id:'rassetu_b3_peasant_tribal_movements',chapter:'ch37',anchor:'## 19.2 19वीं एवं 20वीं शताब्दी के प्रमुख भारतीय किसान आंदोलन',caption:'किसान और जनजातीय आंदोलनों के चयनित क्षेत्र',explanation:'चयनित आंदोलनों को क्षेत्र और समय के साथ दिखाया गया है। यह सम्पूर्ण सूची नहीं; किसान, जनजातीय और देसी-रियासत आंदोलनों को अलग श्रेणियों में रखें।',sourceRefs:['assets/content/rassetu/rassetu_book3.json#ch37/किसान और जनजातीय आंदोलन',sourceUrls.peasant],map:true,body:()=>{
   let s=rect(65,180,895,850,palette.white,palette.line,28)+rect(1005,180,730,850,'#faf7ef',palette.line,28);
   s+=t(510,235,'स्थानिक संकेत (सांकेतिक)',25,palette.ink,700)+indiaShape(290,290,1.5,1.6);
   const zones=[['बंगाल',88,23],['बिहार',85,25],['अवध',81,27],['दक्कन',76,19],['गुजरात',72,22],['मालाबार',76,11],['तेलंगाना',79,17],['छोटानागपुर',85,23]];
   zones.forEach((p,i)=>{const x=155+(p[1]-69)*32,y=850-(p[2]-9)*28;s+=circle(x,y,11,i%2?palette.rust:palette.green)+t(x,y+5,String(i+1),13,'white',750);});
   s+=t(1370,235,'आंदोलन · क्षेत्र · समय',27,palette.ink,700);
   const rows=[['1 बंगाल · नील / पाबना / तेभागा','1859–60 · 1873–76 · 1946–47'],['4 महाराष्ट्र · दक्कन दंगे','1875'],['2/5 बिहार–गुजरात · चंपारण / खेड़ा / बारदोली','1917–28'],['6 मालाबार · मोपला','1921'],['8 पूर्वी भारत · संथाल / मुंडा','1855–56 · 1899–1900'],['7 हैदराबाद · तेलंगाना संघर्ष','1946–51'],['3 अवध · एका आंदोलन','1921–22']];
   rows.forEach((r,i)=>{const y=300+i*91;s+=circle(1060,y-5,8,i%2?palette.blue:palette.rust)+t(1090,y,r[0],16,palette.ink,650,'start')+t(1675,y+29,r[1],15,palette.rust,650,'end')+line(1050,y+48,1680,y+48,palette.line,2);});
   return s;
 }},
 {id:'rassetu_b3_transfer_of_power',chapter:'ch39',anchor:'## 20.4 कैबिनेट मिशन एवं अंतरिम सरकार (1946 AD)',caption:'कैबिनेट मिशन से स्वतंत्रता तक: संवैधानिक पड़ाव',explanation:'1946–47 की घटनाओं का संक्षिप्त क्रम। कैबिनेट मिशन की योजना, समूह और प्रस्ताव अलग-अलग चरण थे; बाद की घटनाओं को उसी योजना का स्वतः लागू परिणाम न समझें।',sourceRefs:['assets/content/rassetu/rassetu_book3.json#ch39/कैबिनेट मिशन और अंतरिम सरकार',sourceUrls.cabinet],map:false,body:()=>{
   const items=[['19 फ़रवरी 1946','मिशन की घोषणा'],['16 मई 1946','योजना प्रकाशित'],['दिसंबर 1946','संविधान सभा की बैठक'],['3 जून 1947','माउंटबेटन योजना'],['15 अगस्त 1947','स्वतंत्रता']];
   let s=line(170,600,1630,600,palette.green,8);
   items.forEach((v,i)=>{const x=190+i*360;s+=circle(x,600,18,[palette.blue,palette.rust,palette.gold,palette.purple,palette.green][i])+line(x,578,x,430,palette.line,4)+line(x,622,x,790,palette.line,4)+t(x,360,v[0],23,palette.rust,750)+label(x,462,v[1].split(' '),palette.ink,20,'middle',650,30);});
   s+=rect(310,870,1180,135,'#eef4f7','#b3c6ce',25)+t(900,925,'मुख्य संवैधानिक प्रश्न',23,palette.blue,700)+t(900,973,'संघ की शक्तियां · प्रांतीय समूह · संविधान सभा · सत्ता हस्तांतरण',21,palette.ink,600);
   return s;
 }},
 {id:'rassetu_b3_princely_integration_reorg',chapter:'ch41',anchor:'## 21.2 देशी रियासतों का ऐतिहासिक एकीकरण (Integration of Princely States)',caption:'रियासतों का एकीकरण और 1956 का राज्यों का पुनर्गठन',explanation:'1947–49 के विलय और 1956 के राज्य-पुनर्गठन को अलग ऐतिहासिक चरणों के रूप में दिखाया गया है। 1956 का कानूनी पुनर्गठन 1 नवम्बर 1956 से प्रभावी था; चित्र आधुनिक सीमाओं का मानचित्र नहीं है।',sourceRefs:['assets/content/rassetu/rassetu_book3.json#ch41/देशी रियासतों का एकीकरण',sourceUrls.reorg],map:false,body:()=>{
   let s=t(900,230,'एकीकरण के औजार और चुनिंदा मामले',28,palette.ink,700);
   s+=circle(900,410,90,'#e5efe7',palette.green,5)+t(900,402,'भारत संघ',28,palette.ink,700)+t(900,442,'1947–49',20,palette.muted,600);
   const cases=[['जूनागढ़','जनमत-संग्रह'],['हैदराबाद','पोलो · 1948'],['जम्मू-कश्मीर','विलय-पत्र · 1947']];
   cases.forEach((c,i)=>{const x=310+i*590;s+=line(900,505,x,650,palette.line,5)+circle(x,670,17,[palette.blue,palette.rust,palette.gold][i])+t(x,730,c[0],24,palette.ink,700)+t(x,772,c[1],20,palette.muted,600);});
   s+=rect(250,845,1300,175,'#f7f1e4','#d5bc7d',26)+t(900,895,'अलग चरण: राज्य पुनर्गठन अधिनियम',24,palette.rust,700)+t(900,942,'31 अगस्त 1956 अधिनियम · प्रभावी तिथि 1 नवम्बर 1956',21,palette.ink,650)+t(900,982,'भाषायी/प्रशासनिक पुनर्गठन — ऐतिहासिक तिथि, वर्तमान सीमा-चित्र नहीं',19,palette.muted,550);
   return s;
 }}
];

function snapshot(ch){const content=ch.content,remove=new Set();content.forEach((b,i)=>{if(b?.type!=='image')return;remove.add(i);for(const j of [i+1,i-1])if(j>=0&&j<content.length&&content[j]?.type==='callout'&&String(content[j].value||'').startsWith('**चित्र से सीखें')){remove.add(j);break;}});return {...ch,content:content.filter((_,i)=>!remove.has(i))};}
function stable(value){const sort=v=>Array.isArray(v)?v.map(sort):v&&typeof v==='object'?Object.fromEntries(Object.keys(v).sort().map(k=>[k,sort(v[k])])):v;return crypto.createHash('sha256').update(JSON.stringify(sort(value))).digest('hex');}
function findAnchor(ch,anchor){const matches=[];ch.content.forEach((b,i)=>{if(b.type==='text'&&b.value.startsWith(anchor))matches.push(i);});if(matches.length!==1)throw new Error(`${ch.id}: expected one anchor ${anchor}, found ${matches.length}`);return matches[0];}
function place(ch,anchor,image,explanation,representative=false){if(ch.content.some(b=>b.type==='image'&&b.value===image))return;const at=findAnchor(ch,anchor);const label=representative?'प्रतिनिधि चित्रण':'सांकेतिक शिक्षण-आरेख';ch.content.splice(at+1,0,{type:'image',value:image,caption:explanation.caption},{type:'callout',value:`**चित्र से सीखें — ${label}**\n\n${explanation.text}`});}
const pairedChapter=id=>'ch'+String(Number(id.slice(2))+1).padStart(2,'0');
async function main(){
 fs.mkdirSync(svgDir,{recursive:true});fs.mkdirSync(imageDir,{recursive:true});
 const book=JSON.parse(fs.readFileSync(bookPath,'utf8'));
 const before=new Map(book.chapters.map(c=>[c.id,stable(c)]));
 const entries=[];
 for(const g of graphics){
  const svgText=base(g.id,g.caption,g.explanation,g.body(),g.map,g.sourceRefs[1]?.startsWith('http')?'Source verified 2026-10-08':`Book 3 source · verified 2026-10-08`);
  const svgPath=path.join(svgDir,g.id+'.svg'),imageName=g.id+'.webp',imagePath=path.join(imageDir,imageName);
  fs.writeFileSync(svgPath,svgText,'utf8');await sharp(Buffer.from(svgText)).webp({quality:90,effort:6}).toFile(imagePath);
  for(const cid of [g.chapter,pairedChapter(g.chapter)]){
   const ch=book.chapters.find(c=>c.id===cid);if(!ch)throw new Error('Missing paired chapter '+cid);
   const original=snapshot(ch);place(ch,g.anchor,imageName,{caption:g.caption,text:g.explanation});
   entries.push({book:3,chapter:cid,topicId:g.id,originalChapterSha256:stable(original),sourceContentSha256:stable(original.content),anchor:g.anchor,image:imageName,assetSha256:crypto.createHash('sha256').update(fs.readFileSync(imagePath)).digest('hex'),caption:g.caption,explanation:g.explanation,assetType:'editable-vector-diagram',sourceReferences:[`assets/content/rassetu/rassetu_book3.json#${cid}/${g.anchor}`,...g.sourceRefs.filter(x=>x.startsWith('http'))],asOfDate:'2026-10-08'});
  }
 }
 for(const scene of generated){
  const src=path.join('C:/Users/rishi/.codex/generated_images/01a1199b-5fd6-7281-bca2-20f5e9c6b861',scene.file);
  const imageName=scene.id+'.webp',imagePath=path.join(imageDir,imageName);
  if(!fs.existsSync(src))throw new Error('Missing generated source '+src);
  await sharp(src).resize({width:1440,withoutEnlargement:true}).webp({quality:88,effort:6}).toFile(imagePath);
  const sourceHash=crypto.createHash('sha256').update(fs.readFileSync(src)).digest('hex');
  for(const cid of [scene.chapter,pairedChapter(scene.chapter)]){
   const ch=book.chapters.find(c=>c.id===cid);if(!ch)throw new Error('Missing paired chapter '+cid);
   const original=snapshot(ch);place(ch,scene.anchor,imageName,{caption:scene.caption,text:scene.explanation},true);
   entries.push({book:3,chapter:cid,topicId:scene.id,originalChapterSha256:stable(original),sourceContentSha256:stable(original.content),anchor:scene.anchor,image:imageName,assetSha256:crypto.createHash('sha256').update(fs.readFileSync(imagePath)).digest('hex'),caption:scene.caption,explanation:scene.explanation,assetType:'generated-representative-image',generationTool:'built-in image_gen',generationPrompt:scene.prompt,generatedSourceSha256:sourceHash,sourceReferences:[`assets/content/rassetu/rassetu_book3.json#${cid}/${scene.anchor}`],asOfDate:'2026-10-08'});
  }
 }
 fs.writeFileSync(bookPath,JSON.stringify(book,null,2)+'\n','utf8');
 // Carry forward the two visuals already integrated in Book 3 so this completion
 // manifest describes the entire book, not only this production batch.
 const existing=[];
 for(const [batchFile,kind] of [['batch6_manifest.json','editable-vector-timeline'],['batch10_manifest.json','generated-representative-image']]){
  const prior=JSON.parse(fs.readFileSync(path.join(root,'artifacts/rassetu_series',batchFile),'utf8'));
  for(const p of prior.placements.filter(p=>p.book===3||p.chapter==='ch35'||p.chapter==='ch36')){
   if(!['ch35','ch36'].includes(p.chapter)||!p.image.startsWith('rassetu_b3_'))continue;
   const ch=book.chapters.find(c=>c.id===p.chapter), imagePath=path.join(imageDir,p.image);
   if(!fs.existsSync(imagePath))throw new Error('Missing existing Book 3 asset '+imagePath);
   existing.push({book:3,chapter:p.chapter,topicId:p.image.replace(/\.webp$/,''),originalChapterSha256:stable(snapshot(ch)),sourceContentSha256:stable(snapshot(ch).content),anchor:p.anchor,image:p.image,assetSha256:crypto.createHash('sha256').update(fs.readFileSync(imagePath)).digest('hex'),caption:p.caption,explanation:p.explanation,assetType:kind,sourceReferences:[`assets/content/rassetu/rassetu_book3.json#${p.chapter}/${p.anchor}`,`artifacts/rassetu_series/${batchFile}`]});
  }
 }
 const all=[...entries,...existing];
 const manifest={version:1,batch:'Book 3 completion — 19 vector diagrams/maps and 3 representative scenes, plus 2 previously integrated visuals',asset:'assets/content/rassetu/rassetu_book3.json',date:'2026-10-08',vectorAssets:graphics.length+1,generatedSceneAssets:generated.length+1,newVectorAssets:graphics.length,newGeneratedSceneAssets:generated.length,newPlacementCount:entries.length,placementCount:all.length,distinctNewAssets:graphics.length+generated.length,distinctVisualAssets:graphics.length+generated.length+2,chapters:all};
 fs.writeFileSync(manifestPath,JSON.stringify(manifest,null,2)+'\n','utf8');
 const assetsPath=path.join(root,'artifacts/rassetu_series/assets.json');const registry=JSON.parse(fs.readFileSync(assetsPath,'utf8'));
 const additions=[...graphics.map(g=>({book:3,id:g.id,file:`assets/images/${g.id}.webp`,source:`artifacts/rassetu_series/svg/${g.id}.svg`,bytes:fs.statSync(path.join(imageDir,g.id+'.webp')).size,title:g.caption})),...generated.map(g=>({book:3,id:g.id,file:`assets/images/${g.id}.webp`,source:'generated representative image',bytes:fs.statSync(path.join(imageDir,g.id+'.webp')).size,title:g.caption}))];
 for(const a of additions)if(!registry.some(x=>x.id===a.id))registry.push(a);
 fs.writeFileSync(assetsPath,JSON.stringify(registry,null,2)+'\n','utf8');
 fs.writeFileSync(path.join(root,'artifacts/rassetu_series/book3_generation_prompts.md'),generated.map((g,i)=>`## ${g.id}\n\n${g.prompt}\n\nSaved as: \`assets/images/${g.id}.webp\`\n`).join('\n'),'utf8');
 console.log(`Integrated ${all.length} Book 3 image placements: ${graphics.length} vector assets and ${generated.length} generated scenes.`);
}
main().catch(e=>{console.error(e);process.exit(1)});
