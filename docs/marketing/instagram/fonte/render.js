const {chromium}=require('playwright'); const path=require('path'), fs=require('fs');
const S=__dirname, [,,out,...lista]=process.argv;
(async()=>{ const b=await chromium.launch(); const p=await b.newPage({viewport:{width:1080,height:1920},deviceScaleFactor:1}); const errs=[];
 p.on('pageerror',e=>errs.push(e.message)); p.on('requestfailed',r=>errs.push('falhou '+r.url()));
 for(const it of lista){ const [peca,lang]=it.split(':');
   await p.goto(`file://${S}/pecas.html?p=${peca}&l=${lang}`); await p.waitForFunction(()=>document.body.dataset.pronto==='1',null,{timeout:20000}); await p.waitForTimeout(150);
   const dir=path.join(out,lang==='en'?'en-US':'pt-BR'); fs.mkdirSync(dir,{recursive:true});
   await (await p.$('#peca')).screenshot({path:path.join(dir,peca+'.png')}); }
 console.log(errs.join('\n')||'ok'); await b.close(); })();
