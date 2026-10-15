const fs = require('fs');
const path = require('path');
const sharp = require('C:/Users/rishi/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/sharp');
async function main() {
 const dir='artifacts/biology_book1'; fs.mkdirSync(`${dir}/source_images`,{recursive:true});
 const sources=JSON.parse(fs.readFileSync(`${dir}/raster_sources.json`));
 sources.push({id:'cells',path:`${dir}/source_images/cells.png`},{id:'mitosis',path:`${dir}/source_images/mitosis.png`});
 const report=[];
 for(const s of sources){
  if(path.resolve(s.path)!==path.resolve(`${dir}/source_images/${s.id}.png`))fs.copyFileSync(s.path,`${dir}/source_images/${s.id}.png`);
  const out=`assets/images/bio1_${s.id}.webp`;
  await sharp(s.path).resize({width:1440,height:1440,fit:'inside',withoutEnlargement:true}).webp({quality:82,effort:6}).toFile(out);
  report.push({id:s.id,bytes:fs.statSync(out).size});
 }
 fs.writeFileSync(`${dir}/raster_sizes.json`,JSON.stringify(report,null,2));
 const groups=[sources.map(s=>({id:s.id,file:`assets/images/bio1_${s.id}.webp`})),JSON.parse(fs.readFileSync(`${dir}/vector_sizes.json`)).map(s=>({id:s.id,file:`assets/images/bio1_${s.id}.webp`}))];
 for(let g=0;g<groups.length;g++){
  const items=groups[g];const tiles=[];let i=0;
  for(const s of items){const tile=await sharp(s.file).resize(400,320,{fit:'contain',background:'white'}).png().toBuffer();tiles.push({input:tile,left:(i%4)*400,top:Math.floor(i/4)*350});i++;}
  await sharp({create:{width:1600,height:Math.ceil(i/4)*350,channels:3,background:'white'}}).composite(tiles).jpeg({quality:90}).toFile(`${dir}/contact_${g}.jpg`);
 }
 console.log(report.reduce((n,s)=>n+s.bytes,0));
}
main().catch(e=>{console.error(e);process.exit(1)});
