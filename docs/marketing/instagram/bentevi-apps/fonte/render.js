// uso: node render.js arquivo.html saida largura altura escala  "q1=a" ...
const {chromium}=require('playwright');const [,,html,out,w,h,s,...qs]=process.argv;
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:+w,height:+h},deviceScaleFactor:+s});const errs=[];
p.on('pageerror',e=>errs.push(e.message));p.on('requestfailed',r=>errs.push('falhou '+r.url()));
for(const q of qs){const i=q.indexOf('='),nome=q.slice(0,i),query=q.slice(i+1);await p.goto('file://'+require('path').resolve(html)+'?'+query);
 await p.waitForFunction(()=>document.body.dataset.pronto==='1',null,{timeout:20000});await p.waitForTimeout(200);
 const e=await p.$('#peca');await (e||p).screenshot({path:out+'/'+nome+'.png'});}
console.log(errs.join('\n')||'ok');await b.close();})();
