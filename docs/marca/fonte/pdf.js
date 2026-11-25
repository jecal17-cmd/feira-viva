const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage();
for(const id of process.argv.slice(2)){await p.goto('file://'+__dirname+'/guias/'+id+'.html');await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(300);
 await p.pdf({path:__dirname+'/guias/identidade-visual-'+id+'.pdf',format:'A4',printBackground:true,preferCSSPageSize:true});}
await b.close();console.log('ok')})();
