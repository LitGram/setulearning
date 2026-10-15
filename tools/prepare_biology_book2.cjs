// Archive generated sources, compress app assets and produce review sheets.
const fs=require('fs'),path=require('path');
const sharp=require('C:/Users/rishi/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/sharp');
const root=path.resolve(__dirname,'..'),dir=path.join(root,'artifacts/biology_book2');
async function main(){
 fs.mkdirSync(path.join(dir,'source_images'),{recursive:true});
 const sources=JSON.parse(fs.readFileSync(path.join(dir,'raster_sources.json'),'utf8'));
 const briefs=JSON.parse(fs.readFileSync(path.join(root,'artifacts/biology_book2_figure_briefs.json'),'utf8'));
 const report=[];
 for(const s of sources){const archive=path.join(dir,'source_images',s.id+'.png');if(path.resolve(s.path)!==archive)fs.copyFileSync(s.path,archive);const dest=path.join(root,'assets/images','bio2_'+s.id+'.webp');await sharp(archive).resize({width:1600,height:1600,fit:'inside',withoutEnlargement:true}).webp({quality:85,effort:6}).toFile(dest);report.push({id:s.id,bytes:fs.statSync(dest).size});}
 const existing=briefs.filter(f=>f.kind==='existing');
 for(const f of existing){const dest=path.join(root,'assets/images','bio2_'+f.id+'.webp');await sharp(path.join(root,'assets/images',f.source)).resize({width:1600,height:1600,fit:'inside',withoutEnlargement:true}).webp({quality:85,effort:6}).toFile(dest);report.push({id:f.id,bytes:fs.statSync(dest).size});}
 fs.writeFileSync(path.join(dir,'raster_sizes.json'),JSON.stringify(report,null,2));
 for(let start=0;start<briefs.length;start+=12){const items=briefs.slice(start,start+12),tiles=[];for(let i=0;i<items.length;i++){const f=items[i],file=path.join(root,'assets/images','bio2_'+f.id+'.webp');if(!fs.existsSync(file))continue;const img=await sharp(file).resize(450,365,{fit:'contain',background:'white'}).png().toBuffer();tiles.push({input:img,left:(i%3)*450,top:Math.floor(i/3)*405});const label=Buffer.from(`<svg width="450" height="40"><rect width="450" height="40" fill="#edf6f2"/><text x="225" y="27" font-size="21" font-family="Arial" text-anchor="middle">${f.chapter} · ${f.id}</text></svg>`);tiles.push({input:label,left:(i%3)*450,top:Math.floor(i/3)*405+365});}await sharp({create:{width:1350,height:Math.ceil(items.length/3)*405,channels:3,background:'white'}}).composite(tiles).jpeg({quality:92}).toFile(path.join(dir,`contact_${Math.floor(start/12)+1}.jpg`));}
 console.log({rasterImages:report.length,rasterBytes:report.reduce((n,s)=>n+s.bytes,0)});
}
main().catch(e=>{console.error(e);process.exit(1)});
