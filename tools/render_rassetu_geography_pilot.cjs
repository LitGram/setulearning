// Editable SVG masters and compact WebP outputs for the RASSetu Book 2 pilot.
const fs = require('fs');
const path = require('path');
const sharp = require('C:/Users/rishi/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/sharp');

const root = path.resolve(__dirname, '..');
const out = path.join(root, 'artifacts/rassetu_geography_pilot/svg');
fs.mkdirSync(out, {recursive: true});
const C = {ink:'#20352f', muted:'#526a61', green:'#2f8066', blue:'#3976a8', rust:'#bd7149', sand:'#eedbb9', pale:'#f2f6f3', sky:'#eaf2f8', line:'#bdd0c6'};
const esc = s => String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
function text(x,y,s,size=26,anchor='middle',color=C.ink,bold=false){return `<text x="${x}" y="${y}" text-anchor="${anchor}" fill="${color}" font-size="${size}" font-weight="${bold?'700':'400'}" font-family="Noto Sans Devanagari, Nirmala UI, Arial, sans-serif">${esc(s)}</text>`;}
function wrap(x,y,lines,size=24,color=C.ink){return lines.map((s,i)=>text(x,y+i*(size+9),s,size,'middle',color)).join('');}
function box(x,y,w,h,label,fill=C.pale,size=23){return `<rect x="${x}" y="${y}" width="${w}" height="${h}" rx="20" fill="${fill}" stroke="${C.line}" stroke-width="2"/>`+wrap(x+w/2,y+h/2-(label.length>24?5:0),Array.isArray(label)?label:[label],size);}
function arrow(x,y,xx,yy,color=C.muted){return `<path d="M${x} ${y} L${xx} ${yy}" fill="none" stroke="${color}" stroke-width="4" marker-end="url(#arr)"/>`;}
function base(title,footer='सांकेतिक चित्र — स्थानिक आकृतियां प्रतिनिधि हैं; मानचित्र पैमाने पर नहीं।'){
  return `<svg xmlns="http://www.w3.org/2000/svg" width="1440" height="1080" viewBox="0 0 1440 1080"><defs><marker id="arr" markerWidth="12" markerHeight="12" refX="9" refY="4" orient="auto"><path d="M0 0 L9 4 L0 8 Z" fill="${C.muted}"/></marker></defs><rect width="1440" height="1080" fill="#fff"/><text x="720" y="66" text-anchor="middle" fill="${C.ink}" font-size="38" font-weight="700" font-family="Noto Sans Devanagari, Nirmala UI, Arial, sans-serif">${esc(title)}</text><path d="M64 92 H1376" stroke="#dbe8e0" stroke-width="3"/>`;
}
function disclaimer(){return `<rect x="56" y="978" width="1328" height="76" rx="14" fill="#f6f4ef"/><text x="720" y="1007" text-anchor="middle" fill="#655b4c" font-size="19" font-family="Noto Sans Devanagari, Nirmala UI, Arial, sans-serif">प्रतिनिधि चित्रण — केवल शैक्षिक समझ हेतु; वास्तविक भू-दृश्य का हूबहू चित्र नहीं।</text><text x="720" y="1036" text-anchor="middle" fill="#655b4c" font-size="18" font-family="Arial, sans-serif">Representative illustration — for learning purposes; not a literal depiction. Schematic / not to scale.</text></svg>`;}
function mapPanel(){return `<path d="M290 155 L418 128 L540 163 L667 144 L791 184 L918 175 L1034 216 L1155 224 L1192 282 L1159 337 L1098 366 L1054 421 L958 447 L886 504 L786 513 L718 477 L638 491 L572 451 L499 454 L440 403 L367 394 L343 337 L298 306 Z" fill="#f3e6ce" stroke="#9f8061" stroke-width="4"/>`+`<path d="M416 127 Q515 200 566 300 T714 469 Q772 368 869 277 T1034 215" fill="none" stroke="${C.rust}" stroke-width="16" stroke-linecap="round"/>`+text(719,302,'अरावली पर्वतमाला',24,'middle',C.rust,true);}
const figures = [
 {id:'rassetu_b2_watershed',title:'अरावली: जल-विभाजक का सांकेतिक मॉडल',draw:()=>mapPanel()+arrow(585,283,455,225,C.blue)+arrow(600,315,450,378,C.blue)+arrow(855,305,1040,250,C.blue)+arrow(840,335,1022,414,C.blue)+text(392,211,'पश्चिमी अपवाह',22,'middle',C.blue)+text(1054,450,'पूर्वी अपवाह',22,'middle',C.blue)+text(720,586,'अरावली के दोनों ओर बहाव की दिशा बदलती है',25)+box(280,670,880,120,['रेखाएं नदी मार्ग या जिला सीमा नहीं दिखातीं।','केवल जल-विभाजक की अवधारणा समझाती हैं।'], '#f2f6f3',23)},
 {id:'rassetu_b2_drainage',title:'राजस्थान अपवाह: नदी-बेसिन संबंध',draw:()=>{
   let s=box(470,132,500,90,'राजस्थान की प्रमुख अपवाह प्रणालियां','#f5ead8',27);
   s+=box(62,340,390,130,['बंगाल की खाड़ी तंत्र','चंबल • बनास • बाणगंगा'],'#eaf2f8',23);
   s+=box(525,340,390,130,['अरब सागर तंत्र','माही • साबरमती'],'#e7f2ef',23);
   s+=box(988,340,390,130,['आंतरिक अपवाह','लूणी • सांभर बेसिन'],'#f8eee7',23);
   s+=arrow(600,226,260,328,C.blue)+arrow(720,226,720,328,C.green)+arrow(840,226,1178,328,C.rust);
   s+=text(720,580,'अरावली महत्वपूर्ण जल-विभाजक है; नदी-बेसिनों की सीमाएं इससे अधिक जटिल हैं।',23);
   s+=box(210,665,1020,118,['कुछ प्रतिनिधि उदाहरण; दिशात्मक तीर व स्थान सांकेतिक।','पूरा जल-निकास मानचित्र या प्रत्येक नदी का स्रोत/मार्ग नहीं।'],'#f2f6f3',22); return s;
 }},
 {id:'rassetu_b2_monsoon',title:'मानसून, अरावली और वर्षा-छाया',draw:()=>{
   let s=box(95,205,320,110,['अरब सागर से','नमी वाली हवाएं'],'#eaf2f8',25);
   s+=box(560,180,320,160,['अरावली की दिशा','दक्षिण-पश्चिम ↗ उत्तर-पूर्व'],'#f5ead8',24);
   s+=box(1030,205,320,110,['पूर्वी राजस्थान','अपेक्षाकृत अधिक वर्षा'],'#e7f2ef',24);
   s+=arrow(420,255,545,255,C.blue)+arrow(888,255,1015,255,C.blue);
   s+=text(720,440,'अरब सागरीय शाखा के लिए पर्वत दिशा काफी हद तक समानांतर',22);
   s+=`<path d="M850 560 C970 520 1070 540 1240 610" fill="none" stroke="${C.blue}" stroke-width="8" stroke-dasharray="14 12"/>`;
   s+=box(995,630,340,105,['पश्चिमी भाग','शुष्कता अधिक'],'#f8eee7',24);
   s+=text(390,610,'वर्षा में क्षेत्रीय अंतर कई कारकों से बनता है',23);
   s+=box(130,805,1180,58,['सरलीकृत व्याख्या; वास्तविक मानसून और वर्षा-वितरण अधिक जटिल हैं।'],'#f2f6f3',20); return s;
 }},
 {id:'rassetu_b2_crop_belts',title:'राजस्थान: फसल–जलवायु संबंध (सांकेतिक क्षेत्र)',draw:()=>{
   let s=box(175,190,500,160,['वर्षा की उपलब्धता','कम / अनिश्चित'],'#f8eee7',26);
   s+=box(765,190,500,160,['फसल चयन','सूखा-सहिष्णु फसलें'],'#eef3df',26);
   s+=arrow(690,270,750,270,C.muted);
   s+=box(175,440,500,160,['सिंचाई व मिट्टी','स्थानीय परिस्थितियां'],'#eaf2f8',25);
   s+=box(765,440,500,160,['फसल चयन','क्षेत्रानुसार विविध'],'#e7f2ef',26);
   s+=arrow(690,520,750,520,C.muted);
   s+=text(720,700,'राजस्थान की कृषि जलवायु और उपलब्ध संसाधनों से प्रभावित होती है',24,'middle',C.ink,true);
   s+=box(220,750,1000,80,['अवधारणात्मक तुलना; किसी निश्चित क्षेत्र या उत्पादन मात्रा का दावा नहीं।'],'#f2f6f3',21); return s;
 }},
 {id:'rassetu_b2_water_harvesting',title:'पारंपरिक जल-संचयन: रूप और काम',draw:()=>{
   const xs=[95,505,915];
   const titles=[['टांका','भूमिगत वर्षाजल','संग्रह'],['जोहड़','बहाव रोककर','स्थानीय संचयन'],['खडीन','ढाल से बहाव','खेत में रोकना']];
   let s='';
   xs.forEach((x,i)=>{
     s+=`<rect x="${x}" y="200" width="350" height="540" rx="24" fill="#fbfcfb" stroke="${C.line}" stroke-width="2"/>`;
     s+=text(x+175,250,titles[i][0],30,'middle',C.ink,true);
     if(i===0){s+=`<path d="M${x+45} 410 Q${x+175} 350 ${x+305} 410 L${x+305} 635 L${x+45} 635 Z" fill="#eedbb9" stroke="#9f8061" stroke-width="3"/>`;s+=`<rect x="${x+105}" y="444" width="140" height="160" rx="6" fill="#cce2eb" stroke="#3976a8" stroke-width="3"/>`;s+=text(x+175,665,'ढका जल-भंडार',21);}
     else if(i===1){s+=`<path d="M${x+42} 410 Q${x+170} 360 ${x+308} 410 L${x+308} 600 L${x+42} 600 Z" fill="#eedbb9" stroke="#9f8061" stroke-width="3"/>`;s+=`<path d="M${x+54} 510 Q${x+175} 470 ${x+296} 510 L${x+296} 590 L${x+54} 590 Z" fill="#cce2eb"/>`;s+=`<path d="M${x+65} 615 L${x+285} 615" stroke="#80654d" stroke-width="20"/>`;s+=text(x+175,667,'छोटा बांध / पाल',21);}
     else{s+=`<path d="M${x+40} 410 L${x+310} 520 L${x+310} 610 L${x+40} 610 Z" fill="#eedbb9" stroke="#9f8061" stroke-width="3"/>`;s+=`<path d="M${x+76} 505 L${x+280} 573 L${x+280} 598 L${x+76} 598 Z" fill="#cce2eb"/>`;s+=`<path d="M${x+42} 630 L${x+310} 630" stroke="#80654d" stroke-width="20"/>`;s+=text(x+175,680,'मेड़ से रोका बहाव',21);}
     s+=wrap(x+175,785,titles[i].slice(1),22);
   });
   return s;
 }}
];

async function main(){
 const report=[];
 for(const f of figures){
   const svg=base(f.title)+f.draw()+disclaimer();
   const src=path.join(out,`${f.id}.svg`),dest=path.join(root,'assets/images',`${f.id}.webp`);
   fs.writeFileSync(src,svg);
   await sharp(Buffer.from(svg)).webp({quality:88,effort:6}).toFile(dest);
   report.push({id:f.id,source:`artifacts/rassetu_geography_pilot/svg/${f.id}.svg`,file:`assets/images/${f.id}.webp`,bytes:fs.statSync(dest).size});
 }
 fs.writeFileSync(path.join(root,'artifacts/rassetu_geography_pilot/assets.json'),JSON.stringify(report,null,2)+'\n');
 console.log(JSON.stringify({count:report.length,totalBytes:report.reduce((s,x)=>s+x.bytes,0),assets:report},null,2));
}
main().catch(e=>{console.error(e);process.exit(1)});
