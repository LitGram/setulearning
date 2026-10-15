const fs = require('fs');
const path = require('path');
const sharp = require('sharp');
const root = path.resolve(__dirname, '..');
const out = path.join(root, 'assets/images');
const W = 1600, H = 1000;
const C = { ink:'#263746', muted:'#61727b', paper:'#fffdf8', line:'#d9dfd8', rust:'#a7422c', gold:'#c38d2f', green:'#3d7666', blue:'#477c9a', sky:'#e6f1f5', sand:'#f5ecd8', mint:'#e7f1e9', rose:'#f4e5df', white:'#ffffff' };
const esc = s => String(s).replaceAll('&','&amp;').replaceAll('<','&lt;').replaceAll('>','&gt;');
const tx = (x,y,s,size=30,fill=C.ink,weight=500,anchor='middle') => `<text x="${x}" y="${y}" text-anchor="${anchor}" font-family="Noto Sans Devanagari, Nirmala UI, sans-serif" font-size="${size}" font-weight="${weight}" fill="${fill}">${esc(s)}</text>`;
const lines = (x,y,ss,size=27,fill=C.ink,weight=500,lh=42,anchor='middle') => ss.map((s,i)=>tx(x,y+i*lh,s,size,fill,weight,anchor)).join('');
const rect=(x,y,w,h,fill,rx=26,stroke=C.line,sw=2)=>`<rect x="${x}" y="${y}" width="${w}" height="${h}" rx="${rx}" fill="${fill}" stroke="${stroke}" stroke-width="${sw}"/>`;
const circle=(x,y,r,fill,stroke=C.white,sw=5)=>`<circle cx="${x}" cy="${y}" r="${r}" fill="${fill}" stroke="${stroke}" stroke-width="${sw}"/>`;
const pathSvg=(d,stroke=C.ink,sw=6,fill='none')=>`<path d="${d}" fill="${fill}" stroke="${stroke}" stroke-width="${sw}" stroke-linecap="round" stroke-linejoin="round"/>`;
const base=(title,sub,content,foot='')=>`<svg xmlns="http://www.w3.org/2000/svg" width="${W}" height="${H}" viewBox="0 0 ${W} ${H}"><rect width="100%" height="100%" fill="${C.paper}"/><path d="M68 110 H1532" stroke="${C.line}" stroke-width="2"/>${tx(800,67,title,40,C.ink,700)}${tx(800,151,sub,24,C.muted,500)}${content}<rect x="60" y="920" width="1480" height="48" rx="14" fill="#f2efe7"/>${tx(800,952,foot,19,C.muted,500)}</svg>`;
const files=[];
function save(id,title,sub,body,foot='') { files.push([`rassetu_b1x_${id}`,base(title,sub,body,foot)]); }
function arrow(x1,y1,x2,y2,color=C.muted){return `<path d="M${x1} ${y1} L${x2} ${y2}" stroke="${color}" stroke-width="5" marker-end="url(#arrow)"/>`}
const defs='<defs><marker id="arrow" markerWidth="12" markerHeight="12" refX="9" refY="6" orient="auto"><path d="M0 0 L12 6 L0 12 z" fill="#61727b"/></marker></defs>';

// 1. Schematic locator: directional zones and anchors are intentionally non-cartographic.
{
 let s=defs+`<path d="M510 220 L690 195 820 235 880 345 850 460 920 570 835 700 760 825 615 795 525 690 420 635 375 520 410 405 390 300 Z" fill="#f5ecd8" stroke="#c38d2f" stroke-width="6"/>`;
 s+=pathSvg('M430 425 C520 390 570 340 650 320 S760 350 820 320', '#76a9b7',12)+pathSvg('M470 565 C550 520 610 530 675 575 S760 640 835 620','#76a9b7',12);
 const pts=[['कालीबंगा','उत्तर-पश्चिम',610,285,C.rust],['गणेश्वर','उत्तर-पूर्व',790,360,C.gold],['बागोर','मध्य',630,500,C.green],['आहड़–बालाथल','दक्षिण',650,680,C.blue],['बैराठ','उत्तर-पूर्व',790,440,C.rust],['नगरी','दक्षिण-पूर्व',760,590,C.green],['रैढ़','पूर्व-मध्य',740,520,C.gold]];
 for(const [a,b,x,y,col] of pts){s+=circle(x,y,14,col); s+=tx(x+25,y-9,a,25,C.ink,700,'start'); s+=tx(x+25,y+21,b,18,C.muted,500,'start');}
 s+=tx(460,270,'पश्चिम',21,C.muted)+tx(820,760,'पूर्व',21,C.muted)+tx(1040,330,'नदी-घाटी संकेत',22,C.blue,700,'start')+pathSvg('M1015 350 H1115', '#76a9b7',10);
 s+=rect(1050,440,420,205,C.white,24)+lines(1260,490,['स्थल पहचान के लिए','क्षेत्र + नदी + संस्कृति','को साथ पढ़ें'],25,C.ink,600,44);
 save('archaeology_locator','राजस्थान के पुरातात्विक स्थल','दिशात्मक स्थान-स्मरण मॉडल • सीमाएं और दूरियां नहीं दर्शाई गईं',s,'योजना-आधारित schematic; पैमाने पर नहीं। नदी-रेखाएं केवल संकेत हैं।');
}
// 2. Chronological progression with small artifact motifs.
{
 let s=defs+pathSvg('M155 495 H1440', '#aab8b1',10);
 const stages=[['पुरापाषाण','कोर–फ्लेक औजार','शिकार • संग्रह',C.rust],['मध्यपाषाण','सूक्ष्म पाषाण','बागोर • तिलवाड़ा',C.green],['नवपाषाण','कृषि • स्थायी बसावट','चाक के मृद्भांड',C.blue],['ताम्रपाषाण','तांबा + मृद्भांड','आहड़ • गणेश्वर',C.gold],['कांस्य युग','नियोजित नगर','कालीबंगा',C.rust],['लौह युग','लौह उपकरण','बैराठ • नगरी',C.green]];
 stages.forEach((a,i)=>{let x=145+i*262; s+=circle(x,495,22,a[3]); s+=rect(x-111,260,222,165,[C.rose,C.mint,C.sky,C.sand,C.rose,C.mint][i],22); s+=tx(x,310,a[0],25,a[3],700); s+=lines(x,355,[a[1],a[2]],20,C.ink,500,36); s+=pathSvg(`M${x} 390 V465`,a[3],4);});
 s+=tx(800,610,'उपकरण और बसावट के संकेत समय के साथ बदलते हैं',27,C.ink,600);
 // tool, microlith, pot, city, iron blade icons
 s+=pathSvg('M125 760 L205 700 250 745 170 805 Z',C.rust,7,C.sand)+pathSvg('M125 760 L170 805',C.rust,5);
 s+=pathSvg('M420 770 L470 720 500 750 450 800 Z',C.green,6,C.mint)+pathSvg('M475 720 L500 750',C.green,5);
 s+=`<path d="M715 700 Q800 740 885 700 L865 815 Q800 850 735 815 Z" fill="${C.sand}" stroke="${C.gold}" stroke-width="6"/>`;
 s+=pathSvg('M1020 800 V710 H1170 V800 M1040 710 V680 H1150 V710 M1045 745 H1090 V800 M1110 745 H1150 V800',C.blue,6,'#e6f1f5');
 s+=pathSvg('M1370 700 L1410 790 1370 840 1330 790 Z',C.ink,6,C.sky)+pathSvg('M1370 840 V865',C.ink,6);
 s+=tx(800,890,'प्रतिनिधि वस्तु-चिह्न • किसी विशिष्ट खुदाई की वस्तु का चित्र नहीं',19,C.muted);
 save('prehistoric_sequence','राजस्थान: सांस्कृतिक क्रम','युगों का क्रम और अध्याय में दिए गए पहचान-संकेत',s,'यह वैचारिक कालक्रम है; सीमांत तिथियां/अवधियां सभी स्थलों पर समान नहीं।');
}
// 3. Distinguishing features, not an undifferentiated table.
{
 let s=defs+rect(90,220,680,625,C.sky,34,'#b8d4df',3)+rect(830,220,680,625,C.sand,34,'#e1cc9e',3);
 s+=tx(430,285,'कालीबंगा',36,C.blue,700)+tx(1170,285,'आहड़–बनास',36,C.rust,700);
 s+=tx(430,330,'घग्घर क्षेत्र • हड़प्पाई नगर',22,C.muted)+tx(1170,330,'आयड़/बनास घाटियां • ताम्रपाषाण',22,C.muted);
 // ploughed furrow and planned town icon
 s+=pathSvg('M190 435 H660 M190 470 H660 M190 505 H660 M250 415 V525 M330 415 V525 M410 415 V525 M490 415 V525 M570 415 V525',C.blue,5);
 s+=lines(430,585,['जुते खेत का साक्ष्य','दुर्गीकृत नगर-खंड','अग्निवेदियों के उदाहरण'],26,C.ink,600,50);
 // pottery + copper icon
 s+=`<path d="M1000 410 Q1170 455 1340 410 L1300 540 Q1170 590 1040 540 Z" fill="#a94e36" stroke="#783522" stroke-width="7"/><path d="M1030 455 Q1170 500 1310 455 M1050 495 Q1170 535 1290 495" fill="none" stroke="#f5d79a" stroke-width="8"/>`;
 s+=pathSvg('M1400 420 L1450 530 1400 595 1350 530 Z',C.gold,7,'#efd49a');
 s+=lines(1170,655,['काले-लाल मृद्भांड','ताम्र औजार और धातुकर्म','गांवों/क्षेत्रीय केंद्रों का समूह'],26,C.ink,600,50);
 s+=rect(150,745,560,65,C.white,18)+rect(890,745,560,65,C.white,18)+tx(430,789,'पहचान: नगर-योजना + खेत/अग्नि-साक्ष्य',20,C.blue,700)+tx(1170,789,'पहचान: तांबा + विशिष्ट मृद्भांड',20,C.rust,700);
 save('kalibanga_ahar_compare','कालीबंगा और आहड़–बनास','स्थल-लक्षणों का तुलना-पटल • उदाहरण अध्याय के वर्णन पर आधारित',s,'स्थल-लक्षणों का संक्षेप; सभी काल/उत्खनन स्तरों का पूर्ण विवरण नहीं।');
}
// 4. A clean parallel timeline of dynastic chapters, avoiding unsupported exact borders.
{
 let s=defs+tx(220,245,'आरंभिक / मध्यकाल',23,C.muted,700,'start')+tx(1380,245,'उत्तर-मध्यकाल',23,C.muted,700,'end');
 const rows=[['गुहिल–सिसोदिया','मेवाड़',C.green,300],['गुर्जर–प्रतिहार','मंडोर • भीनमाल',C.rust,405],['चौहान','शाकंभरी • अजमेर • शाखाएं',C.blue,510],['राठौड़','मारवाड़ • बीकानेर • किशनगढ़',C.gold,615],['कछवाहा','ढूंढाड़ • आमेर • जयपुर',C.green,720],['क्षेत्रीय राजवंश','भाटी • हाड़ा • जाट • यादव • परमार',C.rust,825]];
 rows.forEach((r,i)=>{let x=245, y=r[3]; s+=tx(x,y+8,r[0],26,C.ink,700,'start'); s+=pathSvg(`M620 ${y} H1390`,C.line,11); s+=pathSvg(`M650 ${y} H${690+i*31}`,r[2],11); s+=circle(690+i*31,y,16,r[2]); s+=tx(1430,y+7,r[1],22,C.muted,600,'end');});
 s+=tx(800,190,'राजस्थान के प्रमुख राजवंश • विषय-समूहों का समानांतर अवलोकन',25,C.ink,600);
 save('dynasty_parallel_timeline','राजस्थान के राजवंश: समानांतर काल-रेखाएं','अध्यायों में वर्णित वंशों और उनसे जुड़े क्षेत्रीय केंद्रों का अवलोकन',s,'क्षैतिज पट्टियां क्रमिक पाठ-विषयों को दिखाती हैं; लंबाई/सीमाएं पैमाने या समान शासन-अवधि का दावा नहीं।');
}
// 5. Schematic regional locator using labels, not a political map.
{
 let s=defs+`<path d="M520 210 L720 190 865 250 920 370 880 485 930 610 840 770 690 825 540 780 430 675 380 545 410 395 390 285 Z" fill="#f6f0e3" stroke="#c9b991" stroke-width="6"/>`;
 const loc=[['जैसलमेर','भाटी',470,355,C.gold],['मारवाड़','राठौड़',600,420,C.rust],['मेवाड़','गुहिल–सिसोदिया',620,600,C.green],['ढूंढाड़ / आमेर','कछवाहा',760,390,C.blue],['अजमेर–शाकंभरी','चौहान',670,485,C.rust],['हाड़ौती','हाड़ा',800,625,C.gold],['भरतपुर–धौलपुर','जाट',830,330,C.green],['करौली','यादव',850,535,C.blue]];
 loc.forEach((a,i)=>{s+=circle(a[2],a[3],14,a[4]); s+=rect(970+(i%2)*285,240+Math.floor(i/2)*145,255,110,[C.sand,C.rose,C.mint,C.sky][i%4],18); s+=tx(1097+(i%2)*285,282+Math.floor(i/2)*145,a[0],23,C.ink,700); s+=tx(1097+(i%2)*285,321+Math.floor(i/2)*145,a[1],20,a[4],600);});
 s+=tx(685,875,'क्षेत्र-संबंधी स्थान-स्मरण • आधुनिक सीमा-रेखा नहीं',23,C.muted,600);
 save('kingdoms_schematic_locator','क्षेत्रीय राजवंश: स्थान और पहचान','राजस्थान के भीतर दिशात्मक संबंध • नामित क्षेत्रों का schematic',s,'स्थान संकेतात्मक हैं; यह प्रशासनिक मानचित्र नहीं और पैमाने पर नहीं।');
}
// 6. Mewar capital and branch sequence based on the chapter narrative.
{
 let s=defs+pathSvg('M170 520 C420 390 600 650 820 520 S1190 390 1430 520', '#a6b5ae',12);
 const stops=[['नागदा','प्रारंभिक केंद्र',245,C.green],['चित्तौड़','रावल शाखा',540,C.rust],['चित्तौड़','राणा शाखा का उदय',835,C.blue],['उदयपुर','उत्तर-मध्यकालीन राजधानी',1130,C.gold],['चावंड','प्रताप का अंतिम चरण',1400,C.green]];
 stops.forEach((a,i)=>{let x=a[2],y=i%2?650:390;s+=pathSvg(`M${x} ${i%2?535:505} V${i%2?615:430}`,a[3],4);s+=circle(x,520,20,a[3]);s+=rect(x-115,y-65,230,120,[C.mint,C.rose,C.sky,C.sand,C.mint][i],20);s+=tx(x,y-20,a[0],27,a[3],700);s+=tx(x,y+18,a[1],19,C.ink,500);});
 s+=tx(800,780,'राजधानी / सत्ता-केंद्र का परिवर्तन',27,C.ink,700)+tx(800,830,'शाखा-परिवर्तन और राजनीतिक परिस्थितियों को साथ पढ़ें',21,C.muted);
 save('mewar_capital_sequence','मेवाड़: सत्ता-केंद्र और शाखा क्रम','वंश-वृत्तांत में वर्णित प्रमुख पड़ाव',s,'सरलीकृत क्रम; सह-राजधानियों और अल्पकालीन केंद्रों का पूरा इतिहास नहीं।');
}
// 7. Fort and capital locator with a clear schematic warning.
{
 let s=defs+`<path d="M320 260 C470 210 595 265 700 325 S920 390 1030 325 S1260 240 1380 320" fill="none" stroke="#93b9c5" stroke-width="18" stroke-linecap="round"/>`;
 const places=[['जैसलमेर','मरुस्थली दुर्ग',360,365,C.gold],['जोधपुर','मेहरानगढ़',570,470,C.rust],['चित्तौड़','पर्वतीय दुर्ग',810,620,C.green],['आमेर','पहाड़ी दुर्ग',1050,420,C.blue],['रणथंभौर','वन-पहाड़ी दुर्ग',1270,600,C.rust]];
 places.forEach((a,i)=>{const [name,kind,x,y,col]=a;s+=circle(x,y,20,col);s+=rect(x-105,y-135,210,80,[C.sand,C.rose,C.mint,C.sky,C.rose][i],16);s+=tx(x,y-87,name,25,col,700);s+=tx(x,y-55,kind,18,C.ink,500);s+=pathSvg(`M${x} ${y-50} V${y-24}`,col,3);s+=`<path d="M${x-28} ${y+30} V${y-5} L${x} ${y-25} L${x+28} ${y-5} V${y+30} Z" fill="${[C.sand,C.rose,C.mint,C.sky,C.rose][i]}" stroke="${col}" stroke-width="4"/>`;});
 s+=tx(800,790,'उदाहरण: भू-आकृति और दुर्ग-प्रकार का संबंध',26,C.ink,700)+tx(800,845,'मार्ग, दूरी, नदी-प्रवाह और आधुनिक सीमाएं नहीं दिखाई गईं',21,C.muted);
 save('fort_capital_schematic','दुर्ग और क्षेत्रीय केंद्र','पुस्तक में वर्णित प्रमुख दुर्गों का संबंध-मॉडल',s,'स्थान और बीच की रेखाएं संकेतात्मक हैं; यह मानचित्र नहीं और पैमाने पर नहीं।');
}
// 8. Movements as a time-and-region sequence; no exact geographic claims.
{
 let s=defs+pathSvg('M135 500 H1465','#9cb1aa',10);
 const ev=[['1897–1941','बिजौलिया','किसान सत्याग्रह',C.rust],['1913','मानगढ़','भगत आंदोलन',C.green],['1921–22','एकी • नीमड़ा','तेजावत आंदोलन',C.gold],['1923','बेगू • बूंदी','किसान आंदोलन',C.blue],['1925','नीमूचाणा','अलवर किसान आंदोलन',C.rust],['1934–35','कटराथल • कूदन','शेखावाटी आंदोलन',C.green]];
 ev.forEach((a,i)=>{let x=145+i*264;s+=circle(x,500,20,a[3]);let up=i%2===0, top=up?310:610;s+=pathSvg(`M${x} ${up?478:522} V${up?390:590}`,a[3],4);s+=rect(x-120,top-55,240,145,[C.rose,C.mint,C.sand,C.sky,C.rose,C.mint][i],22);s+=tx(x,top-12,a[0],22,a[3],700);s+=tx(x,top+27,a[1],22,C.ink,700);s+=tx(x,top+63,a[2],17,C.muted,500);});
 s+=tx(800,790,'स्थान + आंदोलन + काल: तीनों संकेतों से पहचानें',26,C.ink,700);
 save('people_movements_timeline','किसान और जनजातीय आंदोलनों के पड़ाव','समय-रेखा • स्रोत अध्याय में दिए उदाहरणों का चयन',s,'साल/दशक और स्थान अध्याय के संक्षेप हैं; यह पूर्ण सूची या मानचित्र नहीं।');
}
// 9. Seven-stage integration as a branching political-process diagram.
{
 let s=defs+tx(800,225,'रियासतों का क्रमिक एकीकरण',30,C.ink,700);
 const nodes=[['I','मत्स्य संघ','18 मार्च 1948'],['II','पूर्व राजस्थान संघ','25 मार्च 1948'],['III','संयुक्त राजस्थान','18 अप्रैल 1948'],['IV','वृहत् राजस्थान','30 मार्च 1949'],['V','संयुक्त वृहत् राजस्थान','15 मई 1949'],['VI','राजस्थान संघ','26 जनवरी 1950'],['VII','पुनर्गठित राजस्थान','1 नवंबर 1956']];
 nodes.forEach((a,i)=>{let x=135+i*222,y=i%2?565:380;s+=circle(x,y,45,[C.rust,C.gold,C.green,C.blue][i%4]);s+=tx(x,y+10,a[0],23,C.white,700);s+=rect(x-98,y+72,196,128,[C.rose,C.sand,C.mint,C.sky][i%4],18);s+=lines(x,y+109,[a[1],a[2]],17,C.ink,700,34);if(i<nodes.length-1){let nx=135+(i+1)*222,ny=(i+1)%2?565:380;s+=`<path d="M${x+47} ${y} C${x+105} ${y} ${nx-105} ${ny} ${nx-48} ${ny}" fill="none" stroke="#91a59d" stroke-width="6" marker-end="url(#arrow)"/>`;}});
 s+=tx(800,800,'प्रत्येक चरण में शामिल रियासतों और नेतृत्व को अध्याय की सूची से जोड़ें',22,C.muted);
 save('integration_seven_stages','राजस्थान एकीकरण: सात चरण','प्रक्रिया-रेखा • अध्याय में दिए चरण-नामों का स्मरण',s,'सार-रेखा; प्रत्येक चरण की आधिकारिक तिथि और सहभागी इकाइयां अध्याय में देखें।');
}
// 10. Craft techniques as visual process chains.
{
 let s=defs;
 const cols=[['मृण्मय','मिट्टी','आकार देना','पकाना','मोलेला टेराकोटा',C.rust],['धातु','धातु-पत्र','उभार / जड़ाई','सजावटी रूप','थेवा • मीनाकारी',C.gold],['वस्त्र','कपड़ा','बंधेज / छपाई','रंग-प्रतिरूप','लहरिया • ब्लॉक प्रिंट',C.blue],['काष्ठ / चमड़ा','लकड़ी / चमड़ा','नक्काशी / कढ़ाई','उपयोगी वस्तु','बस्सी • उस्ता',C.green]];
 cols.forEach((a,i)=>{let x=205+i*395;s+=tx(x,260,a[0],30,a[5],700);s+=circle(x,370,62,[C.rose,C.sand,C.sky,C.mint][i],a[5],5);
 if(i===0)s+=`<path d="M${x-35} 350 Q${x} 370 ${x+35} 350 L${x+27} 402 Q${x} 420 ${x-27} 402 Z" fill="#c87855" stroke="#81432e" stroke-width="4"/>`;
 if(i===1)s+=pathSvg(`M${x} 320 L${x+38} 370 L${x} 420 L${x-38} 370 Z`,a[5],5,'#eed48f');
 if(i===2)s+=pathSvg(`M${x-34} 340 Q${x} 370 ${x+34} 340 M${x-34} 365 Q${x} 395 ${x+34} 365 M${x-34} 390 Q${x} 420 ${x+34} 390`,a[5],5);
 if(i===3)s+=pathSvg(`M${x-35} 405 V340 L${x} 320 L${x+35} 340 V405 M${x-35} 355 H${x+35}`,a[5],5,'#e6cda2');
 s+=lines(x,500,[a[1],a[2],a[3]],22,C.ink,600,42);s+=pathSvg(`M${x} 585 V650`,a[5],4);s+=rect(x-150,660,300,92,[C.rose,C.sand,C.sky,C.mint][i],18);s+=tx(x,718,a[4],21,C.ink,700);});
 s+=tx(800,835,'सामग्री → तकनीक → पहचानने योग्य उत्पाद',26,C.ink,700);
 save('craft_material_process','राजस्थानी शिल्प: सामग्री से पहचान','शिल्प-प्रक्रिया और अध्याय में दिए उदाहरण',s,'उत्पाद-चिह्न रूपक हैं; किसी विशिष्ट कलाकार/वस्तु का चित्र नहीं।');
}
// 11. Annual festival cycle as a sequence of lunar-month windows, no fixed Gregorian dates.
{
 let s=defs+`<circle cx="800" cy="520" r="260" fill="none" stroke="#e5ddcb" stroke-width="76"/>`;
 const months=['चैत्र','वैशाख','ज्येष्ठ','आषाढ़','श्रावण','भाद्रपद','आश्विन','कार्तिक','अगहन','पौष','माघ','फाल्गुन'];
 months.forEach((m,i)=>{let a=(-90+i*30)*Math.PI/180, x=800+260*Math.cos(a), y=520+260*Math.sin(a);s+=circle(x,y,34,[C.rust,C.gold,C.green,C.blue][i%4]);s+=tx(x,y+8,m,18,C.white,700);});
 const fests=[['तीज','श्रावण',580,330,C.rust],['गणगौर','चैत्र',610,700,C.green],['पुष्कर मेला','कार्तिक',1120,340,C.blue],['बेणेश्वर','माघ',1070,710,C.gold]];
 fests.forEach((a,i)=>{s+=rect(a[2]-120,a[3]-42,240,84,[C.rose,C.mint,C.sky,C.sand][i],18);s+=tx(a[2],a[3]-4,a[0],23,a[4],700);s+=tx(a[2],a[3]+25,a[1],16,C.muted,500);});
 s+=tx(800,250,'विक्रम संवत के मासों के साथ सांस्कृतिक चक्र',23,C.ink,600)+tx(800,865,'स्थिर अंग्रेज़ी तारीख नहीं: तिथि/मेला-विवरण अध्याय से मिलाएं',21,C.muted);
 save('festival_month_cycle','राजस्थान: त्योहार और मेले का वार्षिक चक्र','मास-आधारित स्मरण • प्रमुख उदाहरण, पूर्ण कैलेंडर नहीं',s,'चंद्र पंचांग की तिथियां हर वर्ष बदलती हैं; यह Gregorian तारीख-सारणी नहीं।');
}
// 12. Cross-topic concept web.
{
 let s=defs+circle(800,520,140,C.rust)+tx(800,510,'राजस्थान की',29,C.white,700)+tx(800,555,'विरासत',36,C.white,700);
 const nodes=[['इतिहास',390,290,C.rose],['पुरातत्व',800,245,C.sand],['दुर्ग–स्थापत्य',1210,290,C.sky],['चित्रकला',1320,520,C.mint],['लोक-प्रदर्शन',1210,750,C.rose],['शिल्प',800,805,C.sky],['भाषा–साहित्य',390,750,C.sand],['आस्था–परंपरा',280,520,C.mint]];
 nodes.forEach((a,i)=>{s+=pathSvg(`M800 520 Q${(800+a[1])/2} ${(520+a[2])/2-30} ${a[1]} ${a[2]}`,C.line,6);s+=circle(a[1],a[2],82,a[3],C.white,4);s+=tx(a[1],a[2]+8,a[0],22,C.ink,700);});
 s+=tx(800,925,'हर विषय को स्थल, काल, समुदाय और साक्ष्य से जोड़कर पुनः देखें',21,C.muted);
 save('heritage_concept_web','राजस्थान विरासत: पुनरावृत्ति संकल्पना-जाल','इतिहास, कला और सांस्कृतिक परंपराओं के बीच संबंध',s,'अध्ययन-संगठन मॉडल; नोड का आकार महत्व या अनुपात नहीं दर्शाता।');
}
// 13. A visual matching grid with reusable question-solving flow.
{
 let s=defs+tx(800,220,'चार स्तंभों में स्मरण-संकेत जोड़ें',28,C.ink,700);
 const headers=['स्थल / व्यक्तित्व','काल / राजवंश','पहचान-संकेत','स्रोत / परंपरा'];
 const rows=[['कालीबंगा','कांस्य युग','जुता खेत','पुरातात्विक'],['मेहरानगढ़','मध्यकाल','पर्वतीय दुर्ग','स्थापत्य'],['बणी-ठणी','किशनगढ़','चित्रशैली','चित्रकला'],['गैर','मेवाड़ क्षेत्र','सामूहिक नृत्य','लोक-प्रदर्शन']];
 headers.forEach((h,i)=>{let x=95+i*355;s+=rect(x,275,330,72,[C.rust,C.green,C.blue,C.gold][i],16,'none',0);s+=tx(x+165,321,h,21,C.white,700);});
 rows.forEach((row,r)=>row.forEach((v,c)=>{let x=95+c*355,y=370+r*105;s+=rect(x,y,330,78,r%2?C.white:'#f4f2ec',12,C.line,2);s+=tx(x+165,y+50,v,21,C.ink,600);}));
 s+=pathSvg('M270 810 H1320','#aab8b1',5);s+=tx(800,860,'ढकें → याद करें → कारण बताएं → अध्याय में सत्यापित करें',23,C.ink,700);
 save('heritage_recall_grid','विरासत पुनरावृत्ति: मिलान-अभ्यास','एक नमूना retrieval grid • अपनी पंक्तियां जोड़कर अभ्यास करें',s,'उदाहरण स्मरण-अभ्यास हैं; प्रत्येक संबंध की पुष्टि अध्याय के मूल पाठ से करें।');
}

(async()=>{for(const [id,svg] of files){const target=path.join(out,id+'.webp');await sharp(Buffer.from(svg)).webp({quality:90,effort:6}).toFile(target);fs.writeFileSync(path.join(root,'artifacts/rassetu_series/svg',id+'.svg'),svg)} console.log(`Rendered ${files.length} Book 1 graphics`);})().catch(e=>{console.error(e);process.exit(1)});

