const {chromium}=require('playwright'); const fs=require('fs'), path=require('path');
const S=__dirname, [,,tipo,lang,modo]=process.argv; // modo: "previa" (só alguns quadros) ou "video"
(async()=>{ const b=await chromium.launch({args:['--autoplay-policy=no-user-gesture-required']}); const p=await b.newPage({viewport:{width:1080,height:1920}}); const errs=[];
 p.on('pageerror',e=>errs.push(e.message)); p.on('requestfailed',r=>errs.push('falhou '+r.url()));
 await p.goto(`file://${S}/reel.html?tipo=${tipo}&l=${lang}`); await p.waitForFunction(()=>document.body.dataset.pronto==='1',null,{timeout:30000});
 const dir=path.join(S,'frames',`${tipo}-${lang}`); fs.rmSync(dir,{recursive:true,force:true}); fs.mkdirSync(dir,{recursive:true});
 const FPS=30, N=15*FPS, ts=modo==='previa'?[0.3,0.9,2.0,3.6,5.5,9,11.9,12.6,14.5]:Array.from({length:N},(_,i)=>i/FPS);
 let k=0; for(const t of ts){ await p.evaluate(t=>window.setT(t),t); await p.screenshot({path:path.join(dir,String(k++).padStart(4,'0')+'.jpg'),type:'jpeg',quality:92}); }
 console.log(tipo,lang,k,'quadros', errs.join(' | ')||'sem erros'); await b.close(); })();
