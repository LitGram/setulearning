// Eight polished, source-aligned learning visuals that complete Book 6.
const fs = require('fs');
const path = require('path');
const sharp = require('C:/Users/rishi/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/sharp');
const root = path.resolve(__dirname, '..');
const out = path.join(root, 'artifacts/rassetu_series/svg');
fs.mkdirSync(out, { recursive: true });
const C = { ink:'#20352f', muted:'#526a61', green:'#2f8066', blue:'#3976a8', rust:'#bd7149', gold:'#b38a43', pale:'#f2f6f3', sky:'#eaf2f8', sand:'#f5ead8', line:'#bdcfc6', rose:'#f7ece8', white:'#fff', red:'#b94c43' };
const esc = s => String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
const tx = (x,y,s,size=24,color=C.ink,weight=400,anchor='middle') => `<text x="${x}" y="${y}" text-anchor="${anchor}" fill="${color}" font-family="Noto Sans Devanagari, Nirmala UI, Arial, sans-serif" font-size="${size}" font-weight="${weight}">${esc(s)}</text>`;
const lines = (x,y,list,size=23,color=C.ink,step=34,weight=400) => list.map((t,i)=>tx(x,y+i*step,t,size,color,weight)).join('');
const rect = (x,y,w,h,fill,rx=24,stroke=C.line,sw=2) => `<rect x="${x}" y="${y}" width="${w}" height="${h}" rx="${rx}" fill="${fill}" stroke="${stroke}" stroke-width="${sw}"/>`;
const circle = (x,y,r,fill,stroke='none',sw=0) => `<circle cx="${x}" cy="${y}" r="${r}" fill="${fill}" stroke="${stroke}" stroke-width="${sw}"/>`;
const arrow = (x1,y1,x2,y2,color=C.muted,width=4) => `<path d="M${x1} ${y1} L${x2} ${y2}" fill="none" stroke="${color}" stroke-width="${width}" marker-end="url(#arrow)"/>`;
function frame(title, body, note) {
  return `<svg xmlns="http://www.w3.org/2000/svg" width="1440" height="1080" viewBox="0 0 1440 1080"><defs>
    <marker id="arrow" markerWidth="14" markerHeight="14" refX="10" refY="5" orient="auto"><path d="M0 0 L10 5 L0 10Z" fill="${C.muted}"/></marker>
    <filter id="shadow" x="-20%" y="-20%" width="140%" height="150%"><feDropShadow dx="0" dy="5" stdDeviation="8" flood-color="#2a4638" flood-opacity=".12"/></filter>
    </defs><rect width="1440" height="1080" fill="#fbfcfa"/><path d="M0 0H1440V118Q1080 160 720 118T0 118Z" fill="#f0f5f1"/>
    ${tx(720,70,title,38,C.ink,700)}<path d="M65 130H1375" stroke="#dbe8e0" stroke-width="3"/>${body}
    <rect x="54" y="956" width="1332" height="94" rx="18" fill="#f6f4ef"/>
    ${tx(720,988,note,18,'#655b4c',600)}
    ${tx(720,1022,'प्रतिनिधि शैक्षिक चित्रण • आरेख सांकेतिक है; तथ्य/निर्देश के लिए अध्याय-पाठ देखें।',18,'#655b4c')}
    </svg>`;
}
const figs = [];
function add(id,title,body,note){figs.push({id,title,svg:frame(title,body,note)});}

// 1. Three explicit elimination checks from the chapter’s 30-second filter.
{
  let s = '';
  const qs = [
    ['01','क्या कदम समस्या को','हल या कम करता है?'],
    ['02','क्या कदम अत्यधिक कठोर,','गैर-कानूनी या अव्यावहारिक है?'],
    ['03','क्या कदम इससे भी बड़ा','नया संकट पैदा करेगा?'],
  ];
  qs.forEach((q,i)=>{
    const x=90+i*445, cy=335;
    s += rect(x,225,355,205,[C.sky,C.sand,C.pale][i],28,C.line,2);
    s += circle(x+46,268,26,[C.blue,C.gold,C.green][i])+tx(x+46,276,q[0],16,C.white,700);
    s += lines(x+195,318,q.slice(1),21,C.ink,34,600);
    const pathText=[['हाँ → आगे','नहीं → हटाएं'],['नहीं → आगे','हाँ → हटाएं'],['नहीं → उचित विकल्प','हाँ → हटाएं']][i];
    s += tx(x+177,468,pathText[0],17,C.green,650);
    s += tx(x+177,497,pathText[1],17,C.red,650);
    if(i<2){
      s+=arrow(x+358,cy,x+430,cy,C.green,4);
      s+=tx(x+394,cy-16,i===0?'हाँ':'नहीं',16,C.green,650);
    }
  });
  s += rect(125,605,550,118,'#e8f4ed',26,'#a8cdb8',2)+tx(400,654,'तीनों कसौटियां पास',22,C.green,700)+tx(400,693,'उचित विकल्प पर विचार करें',23,C.ink,600);
  s += rect(765,605,550,118,'#faece9',26,'#e3b6af',2)+tx(1040,654,'किसी कसौटी पर विफल',22,C.red,700)+tx(1040,693,'विकल्प हटाएं',23,C.ink,600);
  s += tx(720,805,'Q1: समस्या को हल/कम करना चाहिए  •  Q2: कठोर/गैर-कानूनी/अव्यावहारिक न हो  •  Q3: बड़ा नया संकट न बनाए',18,C.muted,500);
  add('course_of_action_filter','उचित कार्यवाही: तीन प्रश्नों की निर्णय-कसौटी',s,'30-सेकंड फिल्टर अध्याय में दिए गए तीन प्रश्नों का संक्षिप्त दृश्य-सार है।');
}
// 2. Claim / evidence / alternative cause, without asserting a real-world result.
{
  let s='';
  s += rect(95,210,495,160,C.sky,28)+circle(150,290,34,C.blue)+tx(150,300,'दावा',20,C.white,700)+lines(365,277,['कारण X से','परिणाम Y'],25,C.ink,38,700);
  s += rect(850,210,495,160,C.sand,28)+circle(905,290,34,C.gold)+tx(905,300,'Y',22,C.white,700)+lines(1110,277,['देखा गया','परिणाम'],25,C.ink,38,700);
  s += arrow(600,290,830,290,C.green,7);
  s += rect(250,470,410,175,C.pale,28)+circle(310,525,31,C.green)+tx(310,533,'✓',25,C.white,700)+lines(468,525,['साक्ष्य','X वास्तव में Y को','बढ़ाता है?'],22,C.ink,33,600);
  s += rect(780,470,410,175,C.rose,28)+circle(840,525,31,C.rust)+tx(840,533,'?',25,C.white,700)+lines(998,525,['वैकल्पिक कारण','क्या कोई तीसरा कारक','Y समझा सकता है?'],22,C.ink,33,600);
  s += arrow(485,375,455,455,C.muted,4)+arrow(955,375,985,455,C.muted,4);
  s += `<path d="M985 658 C985 760 720 770 720 823" fill="none" stroke="${C.rust}" stroke-width="4" marker-end="url(#arrow)"/>`;
  s += rect(330,805,780,86,'#fff',22,'#a8cdb8',3)+tx(720,859,'निष्कर्ष: दावे की कड़ी को समर्थन या चुनौती दें',23,C.ink,650);
  add('argument_cause_effect','कारण–प्रभाव तर्क: दावे की कड़ी परखें',s,'सांकेतिक तर्क-मॉडल; X और Y किसी वास्तविक घटना या प्रमाण का दावा नहीं हैं।');
}
// 3. Accurate letter positions, opposite pairs, and a cyclic shift example.
{
  let s='';
  s += tx(720,205,'अक्षर-स्थान',24,C.muted,600);
  const alpha='ABCDEFGHIJKLMNOPQRSTUVWXYZ'.split('');
  alpha.forEach((ch,i)=>{
    const x=100+i*49.5;
    s += circle(x,270,18,i<13?C.sky:C.sand,C.line,1.5)+tx(x,278,ch,16,C.ink,700);
    if([0,4,8,12,16,20,25].includes(i)) s+=tx(x,318,String(i+1),15,C.muted,400);
  });
  s += rect(100,370,1240,172,'#fff',24,'#d9e5dd',2)+tx(720,412,'विपरीत अक्षर-युग्म: दोनों स्थानों का योग 27',22,C.ink,700);
  const pairs=[['A','Z'],['B','Y'],['C','X'],['…','…']];
  pairs.forEach((p,i)=>{const x=250+i*300;s+=circle(x,473,29,i===3?C.pale:C.sky,C.line,2)+tx(x,481,p[0],19,C.blue,700);s+=arrow(x+44,473,x+102,473,C.gold,3);s+=circle(x+136,473,29,i===3?C.pale:C.sand,C.line,2)+tx(x+136,481,p[1],19,C.rust,700);});
  s += rect(150,610,1140,225,C.pale,30,'#d9e5dd',2)+tx(720,660,'चक्रीय शिफ्ट +2: हर अक्षर को दो स्थान आगे पढ़ें',23,C.green,700);
  const ex=[['मूल','C','A','T'],['स्थान +2','E','C','V']];
  ex.forEach((row,r)=>{const y=715+r*69;s+=tx(350,y,row[0],20,C.muted,600,'end');row.slice(1).forEach((ch,i)=>{const x=485+i*162;s+=rect(x,y-36,115,49,r?C.sand:C.sky,13,C.line,1.5)+tx(x+57,y-2,ch,23,C.ink,700);});});
  add('coding_alphabet_map','कोडिंग–डिकोडिंग: वर्णमाला और चक्रीय शिफ्ट',s,'उदाहरण में +2 शिफ्ट चक्रीय है: Y→A और Z→B; नियम प्रश्न के अनुसार बदल सकता है।');
}
// 4. Fictional chart data shown only as a reading-practice model.
{
  let s='';
  s += rect(140,190,1160,112,'#fff',24,'#d9e5dd',2)+tx(720,236,'अभ्यास डेटा: A = 20 इकाई  •  B = 40 इकाई',23,C.ink,650)+tx(720,273,'काल्पनिक उदाहरण — किसी जिले/वर्ष का वास्तविक आंकड़ा नहीं',17,C.rust,600);
  const baseY=690, x0=420, scale=5;
  s += rect(495,330,450,54,'#fff',18,'#d9e5dd',1.5)+tx(720,365,'अंतर = 40 − 20 = 20 इकाई',18,C.rust,650);
  s += `<path d="M${x0-35} 410 V${baseY} H1030" stroke="${C.muted}" stroke-width="4" fill="none"/>`;
  [0,10,20,30,40].forEach(v=>{const y=baseY-v*scale;s+=`<path d="M${x0-30} ${y} H1030" stroke="#e2ebe5" stroke-width="2"/>${tx(x0-52,y+6,String(v),16,C.muted,400,'end')}`;});
  [[560,20,C.blue,'A'],[850,40,C.gold,'B']].forEach(([x,v,col,label])=>{
    const y=baseY-v*scale,h=v*scale;
    s+=`<rect x="${x}" y="${y}" width="150" height="${h}" rx="16" fill="${col}" opacity=".88"/>`;
    s+=tx(Number(x)+75,y-16,`${v}`,22,C.ink,700)+tx(Number(x)+75,baseY+38,label,20,C.muted,600);
  });
  s += rect(215,788,1010,94,C.sky,24,'#c5d8e7',2)+tx(720,827,'पहले शीर्षक/इकाई पढ़ें  →  फिर तुलना करें  →  गणना सहित उत्तर लिखें',21,C.ink,600);
  add('data_interpretation_reading','आंकड़ा व्याख्या: चार कदम में चार्ट पढ़ें',s,'चार्ट के सभी मान काल्पनिक अभ्यास-मान हैं; आधिकारिक/राजस्थान डेटा के रूप में उपयोग न करें।');
}
// 5. One selection set, then the ordered permutations of those selections.
{
  let s='';
  const people=[['A',300,C.blue],['B',720,C.green],['C',1140,C.rust]];
  people.forEach(([n,x,col],i)=>{
    s+=circle(x,260,76,'#fff',col,5)+circle(x,232,23,col)+`<path d="M${x-45} 318 Q${x} 265 ${x+45} 318" fill="${col}" opacity=".75"/>`+tx(x,372,`व्यक्ति ${n}`,20,C.ink,600);
  });
  s += tx(720,455,'2 लोगों का चयन: क्रम मायने नहीं रखता',22,C.green,700);
  const combos=[['AB',420],['AC',720],['BC',1020]];
  combos.forEach(([t,x])=>{s+=rect(x-88,490,176,70,C.pale,20,'#b9d4c5',2)+tx(x,535,t,24,C.ink,700);});
  s += tx(720,601,'C(3,2) = 3 चयन',21,C.green,700);
  s += `<path d="M150 645 H1290" stroke="#d9e5dd" stroke-width="3"/>`;
  s += tx(720,703,'दो स्थानों पर क्रमबद्ध व्यवस्था: क्रम मायने रखता है',22,C.blue,700);
  [['AB','BA'],['AC','CA'],['BC','CB']].forEach((p,i)=>{
    const x=295+i*425;
    s+=rect(x-115,738,230,75,C.sky,20,'#c5d8e7',2)+tx(x,786,`${p[0]}   ${p[1]}`,22,C.ink,700);
  });
  s += tx(720,858,'P(3,2) = 6 व्यवस्थाएं',21,C.blue,700);
  add('permutation_combination','क्रमचय और संचय: व्यवस्था बनाम चयन',s,'तीन अलग व्यक्तियों में से दो का चयन/क्रम: C(3,2)=3 और P(3,2)=6।');
}
// 6. Timeless current-affairs verification path; no time-sensitive facts.
{
  let s='';
  const nodes=[
    ['01','दावा / घटना','किस बात की चर्चा?'],
    ['02','स्रोत + तिथि','आधिकारिक मूल स्रोत?'],
    ['03','निर्णयकर्ता','कौन-सी संस्था?'],
    ['04','कार्रवाई','नीति / क्रियान्वयन'],
    ['05','प्रभाव','क्या प्रमाणित है?'],
    ['06','परीक्षा-संबंध','क्यों महत्वपूर्ण?'],
  ];
  nodes.forEach((n,i)=>{
    const x=74+i*216, y=360+(i%2?105:0), col=[C.sky,C.sand,C.pale,C.rose][i%4];
    s+=circle(x+76,y-35,27,[C.blue,C.gold,C.green,C.rust][i%4])+tx(x+76,y-28,n[0],16,C.white,700);
    s+=rect(x,y,164,142,col,25,C.line,2)+tx(x+82,y+46,n[1],20,C.ink,700)+lines(x+82,y+83,[n[2]],16,C.muted,24,500);
    if(i<nodes.length-1) s+=arrow(x+166,y+72,x+204,y+72,C.muted,3);
  });
  s += rect(210,690,1020,118,'#fff',26,'#d9e5dd',2)+tx(720,737,'हर तथ्य की तिथि और मूल स्रोत फिर से जांचें',23,C.green,700)+tx(720,779,'यह जांच-ढांचा है; इसमें कोई 2026 घटना/आंकड़ा दर्ज नहीं है।',18,C.muted,500);
  add('current_affairs_verification','समसामयिकी: स्रोत से परीक्षा-संबंध तक',s,'स्रोत-सत्यापन का स्थिर ढांचा; आरेख में समय-संवेदी समाचार या तथ्य नहीं हैं।');
}
// 7. Safe OMR workflow, with changing exam instructions explicitly deferred to official notices.
{
  let s='';
  s+=circle(720,255,76,C.sky,C.blue,4)+tx(720,266,'प्रश्न',26,C.blue,700);
  s+=arrow(680,330,440,430,C.muted,4)+arrow(760,330,1000,430,C.muted,4);
  s+=rect(130,425,510,150,'#eaf4ed',28,'#b7d7c3',2)+circle(205,500,34,C.green)+tx(205,510,'✓',24,C.white,700)+lines(430,488,['उत्तर सुनिश्चित?','उचित A/B/C/D गोला','निर्देशानुसार भरें'],22,C.ink,32,600);
  s+=rect(800,425,510,150,C.sand,28,'#dec99e',2)+circle(875,500,34,C.gold)+tx(875,510,'?',24,C.white,700)+lines(1100,488,['अनुत्तरित रखना है?','पांचवां विकल्प / E','यदि आधिकारिक निर्देश कहें'],21,C.ink,32,600);
  s+=arrow(385,585,540,690,C.green,4)+arrow(1055,585,900,690,C.gold,4);
  s+=rect(250,690,940,118,C.pale,28,'#b9d4c5',2)+tx(720,737,'अंतिम जांच: हर प्रश्न की OMR स्थिति पूरी है?',23,C.ink,700)+tx(720,779,'विकल्प, कटौती और अतिरिक्त समय की शर्तें अधिसूचना से मिलाएं।',19,C.rust,600);
  add('omr_fifth_option_workflow','पांचवां विकल्प: OMR भरने की सुरक्षित जांच',s,'परीक्षा-निर्देश बदल सकते हैं; विकल्प, दंड और समय के लिए वर्तमान आधिकारिक अधिसूचना मानें।');
}
// 8. Practice / feedback / error-tagging loop for the question-bank lesson.
{
  let s='';
  const steps=[['01','प्रश्न हल करें','समय सीमा रखें'],['02','उत्तर-कुंजी देखें','सही विकल्प पहचानें'],['03','व्याख्या पढ़ें','तर्क / गणना समझें'],['04','गलती का प्रकार','अवधारणा • गणना • जल्दबाजी'],['05','दोबारा प्रयास','सीख को जांचें']];
  const pts=[[230,365],[525,245],[905,245],[1210,365],[720,665]];
  const cols=[C.sky,C.sand,C.pale,C.rose,'#e8f4ed'];
  pts.forEach(([x,y],i)=>{
    s+=circle(x,y,94,cols[i],C.line,3)+circle(x,y-58,24,[C.blue,C.gold,C.green,C.rust,C.green][i])+tx(x,y-51,steps[i][0],15,C.white,700);
    s+=tx(x,y+3,steps[i][1],19,C.ink,700)+lines(x,y+35,[steps[i][2]],15,C.muted,21,500);
  });
  for(let i=0;i<4;i++){const [x1,y1]=pts[i],[x2,y2]=pts[i+1];s+=arrow(x1+(x2>x1?92:-92),y1+(y2>y1?32:-25),x2-(x2>x1?92:-92),y2-(y2>y1?32:-25),C.muted,4);}
  s+=`<path d="M${pts[4][0]-95} ${pts[4][1]+8} C350 890 130 830 155 505" fill="none" stroke="${C.green}" stroke-width="4" stroke-dasharray="10 8" marker-end="url(#arrow)"/>`;
  s+=rect(385,805,670,75,'#fff',22,'#d9e5dd',2)+tx(720,852,'अंक से आगे बढ़ें: हर गलती को सीख में बदलें',21,C.green,650);
  add('question_bank_review_loop','मास्टर प्रश्न बैंक: हल करें, जांचें, सुधारें',s,'अभ्यास-चक्र प्रतिनिधि है; प्रश्नों/विकल्पों के उत्तर अध्याय की कुंजी से जांचें।');
}

async function main(){
  const report=[];
  for(const f of figs){
    const id=`rassetu_b6_${f.id}`;
    const source=`artifacts/rassetu_series/svg/${id}.svg`;
    const file=`assets/images/${id}.webp`;
    fs.writeFileSync(path.join(root,source),f.svg);
    await sharp(Buffer.from(f.svg)).webp({quality:91,effort:6}).toFile(path.join(root,file));
    report.push({book:6,id,file,source,bytes:fs.statSync(path.join(root,file)).size,title:f.title});
  }
  const thumbW=360,thumbH=270,gap=18,cols=2,rows=Math.ceil(figs.length/cols);
  const thumbs=[];
  for(let i=0;i<figs.length;i++){
    const buf=await sharp(Buffer.from(figs[i].svg)).resize(thumbW,thumbH).png().toBuffer();
    thumbs.push({input:buf,left:gap+(i%cols)*(thumbW+gap),top:gap+Math.floor(i/cols)*(thumbH+gap)});
  }
  await sharp({create:{width:gap+cols*(thumbW+gap),height:gap+rows*(thumbH+gap),channels:3,background:'#eef2ee'}}).composite(thumbs).jpeg({quality:85}).toFile(path.join(root,'artifacts/rassetu_series/book6_completion_contact.jpg'));
  fs.writeFileSync(path.join(root,'artifacts/rassetu_series/book6_completion_assets.json'),JSON.stringify(report,null,2)+'\n');
  console.log(JSON.stringify({count:report.length,bytes:report.reduce((a,x)=>a+x.bytes,0),contact:'artifacts/rassetu_series/book6_completion_contact.jpg'},null,2));
}
main().catch(e=>{console.error(e);process.exit(1)});
