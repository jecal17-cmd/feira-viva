const {chromium}=require('playwright');
const lang=process.argv[2]||'pt';
(async()=>{ const b=await chromium.launch();
 const ctx=await b.newContext({viewport:{width:1080,height:1920},deviceScaleFactor:1,recordVideo:{dir:'video/raw-'+lang,size:{width:1080,height:1920}}});
 await ctx.addInitScript(()=>{ try{localStorage.clear()}catch(e){} document.addEventListener('DOMContentLoaded',()=>{ document.documentElement.style.zoom='3'; }); });
 const p=await ctx.newPage(); const errs=[]; p.on('pageerror',e=>errs.push(e.message));
 await p.goto(`file:///home/user/feira-viva/versao-b-quitanda-zen/index.html?intro=0&lang=${lang}`); await p.waitForTimeout(500);
 await p.evaluate(()=>{ S.tut=9; S.level=6; S.coins=1240; S.stop=0; S.served=18; S.goalSeen=true; S.giftDay=today(); maybeInter=()=>{}; homeOn=false;
   const L=['fr','pe','te','be']; const pat=[[0,1],[0,1],[1,2],[1,2],[2,2],[2,2],[3,1],[3,1],[0,3],[0,3],[1,1],[1,1],[2,3],[3,2],[3,2],[0,2],[0,2],[1,3],[2,1],[2,1],[3,3],[3,3],[0,4],[1,4],[2,4],[3,4]];
   S.board=S.board.map((x,i)=>i<pat.length?{l:L[pat[i][0]],n:pat[i][1]}:null); S.board.sort(()=>Math.random()-.5);
   S.orders.forEach((o,k)=>{ o.rush=k===1?Date.now()+70000:0; o.rec=null; });
   S.orders[0].items=[{l:'fr',n:2,done:false}]; S.orders[1].items=[{l:'pe',n:3,done:false},{l:'te',n:2,done:false}]; S.orders[2].items=[{l:'be',n:2,done:false}]; S.orders[3].items=[{l:'fr',n:4,done:false}];
   render(); });
 await p.waitForTimeout(900);
 const center=async i=>{ const r=await p.evaluate(i=>{ const c=document.querySelector(`[data-cell="${i}"]`).getBoundingClientRect(); return [c.x+c.width/2,c.y+c.height/2]; },i); return r; };
 const drag=async(a,c)=>{ const A=await center(a), C=await center(c); await p.mouse.move(A[0],A[1]); await p.mouse.down(); for(let k=1;k<=14;k++){ await p.mouse.move(A[0]+(C[0]-A[0])*k/14,A[1]+(C[1]-A[1])*k/14); await p.waitForTimeout(16); } await p.mouse.up(); await p.waitForTimeout(520); };
 for(let k=0;k<7;k++){ const pr=await p.evaluate(()=>findPair()); if(!pr) break; await drag(pr[0],pr[1]);
   const rd=await p.evaluate(()=>{ const o=document.querySelector('.order.ready'); return o?o.dataset.order:null; });
   if(rd&&k%2===1){ await p.click(`[data-order="${rd}"]`); await p.waitForTimeout(700); } }
 for(let k=0;k<2;k++){ const bk=await p.$('.basket[data-act^="basket:"]'); if(bk){ await bk.click(); await p.waitForTimeout(450);} }
 for(let k=0;k<3;k++){ const pr=await p.evaluate(()=>findPair()); if(!pr) break; await drag(pr[0],pr[1]); }
 await p.waitForTimeout(600); const v=p.video(); await ctx.close(); console.log(await v.path()); console.log(errs.join('\n')||'sem erros'); await b.close(); })();
