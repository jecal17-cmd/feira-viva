// Gera as capturas de tela (1080 x 1920) e o gráfico de destaque (1024 x 500) da página da Play Store.
// Uso, na raiz do repositório (precisa do Playwright com o Chromium):
//   node docs/loja-play/quitanda-zen/gerar-imagens.js
// O jogo é preparado em modo de publicação (sem Loja paga) por app-android/scripts/copy-web.js.
const { chromium } = require('playwright');
const fs = require('fs'), os = require('os'), path = require('path'), { execFileSync } = require('child_process');
const RAIZ = path.resolve(__dirname, '..', '..', '..');
const OUT = __dirname + '/';
const S = fs.mkdtempSync(path.join(os.tmpdir(), 'quitanda-capturas-')) + '/';
execFileSync('node', [path.join(RAIZ, 'app-android/scripts/copy-web.js')], { env: { ...process.env, PUBLICACAO: '1', VERSAO: '1.0.0' }, stdio: 'inherit' });
const JOGO = path.join(RAIZ, 'app-android/www/index.html');
const LANGS = ['pt', 'en'];
const URL = l => 'file://' + JOGO + '?intro=0&lang=' + l;
function setup(){
  const s=fresh(0), now=Date.now(); s.stop=4; s.level=14; s.xp=Math.round(need(14)*.62); s.coins=3280; s.served=24; s.goalSeen=true;
  s.tut=4; s.tutF=7; s.encHint=1; s.giftDay=today(); s.streak=4; s.decor=[0,1,2,3,4,5]; s.exp=1; s.cols=6; s.rows=8;
  s.up={far:3,cap:2,spd:2}; s.recipes=[0,1,2,3,4];
  CAST.forEach((c,i)=>{ if(i<14) s.friends[c.id]={h:6+i*3,lv:1+(i%4)}; });
  s.stats.merges=1840; s.stats.items=2310; s.stats.orders=420; s.stats.first=now-864e5*5;
  s.baskets={}; linesAt(4).forEach((k,i)=>s.baskets[k]={c:[8,5,10,6][i],t:now});
  S=s; S.orders=[]; S.board=Array(s.cols*s.rows).fill(null);
  while(S.orders.length<4) S.orders.push(newOrder());
  const ls=linesAt(4), cells=[...Array(S.board.length).keys()];
  // itens que atendem os dois primeiros pedidos (ficam com borda verde)
  const put=(it)=>{ const i=cells.splice(Math.floor(Math.random()*cells.length),1)[0]; S.board[i]=it; };
  S.orders.slice(0,2).forEach(o=>o.items.forEach(x=>put({l:x.l,n:x.n})));
  const lv=[1,1,1,2,2,2,3,3,3,4,4,5,5,6,2,3,1,4];
  for(let k=0;k<39-S.orders.slice(0,2).reduce((a,o)=>a+o.items.length,0);k++) put({l:ls[k%ls.length],n:lv[k%lv.length]});
  S.missions.forEach((m,i)=>{ if(m) m.p=Math.min(m.goal,Math.round(m.goal*[1,.6,.3][i])); }); homeOn=false; render(); fit(); return S.orders.map(o=>JSON.stringify(o.items));
}
const CAP={
 pt:[['1-tabuleiro','Junte itens iguais e atenda a freguesia'],['2-inicio','Sem derrota: jogue no seu ritmo'],['3-map','Viaje por 12 mercados do Brasil'],['3-turma','Faça amizade com a Turma da Feira'],['3-rec','Descubra receitas brasileiras'],['3-up','Melhore e decore a sua banca']],
 en:[['1-tabuleiro','Merge matching items and serve your customers'],['2-inicio','No losing: play at your own pace'],['3-map','Travel to 12 markets across Brazil'],['3-turma','Befriend the market crew'],['3-rec','Discover Brazilian recipes'],['3-up','Upgrade and decorate your stall']]};
const b64=f=>'data:image/png;base64,'+fs.readFileSync(f).toString('base64');
const font='<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Baloo+2:wght@800&family=Nunito:wght@800&display=swap">';

(async () => {
  const b = await chromium.launch();
  for (const lang of LANGS) {
    const p = await b.newPage({viewport:{width:360,height:640},deviceScaleFactor:3});
    p.on('pageerror',e=>console.log('ERR',e.message));
    await p.goto(URL(lang)); await p.waitForTimeout(1200);
    await p.evaluate(`(${setup})()`); await p.waitForTimeout(500);
    const shot=async n=>{ await p.waitForTimeout(400); await p.screenshot({path:S+`${lang}-${n}.png`}); };
    await shot('1-tabuleiro');
    await p.evaluate(()=>{ homeOn=true; render(); }); await shot('2-inicio');
    await p.evaluate(()=>{ homeOn=false; render(); });
    for (const n of ['map','turma','rec','up','miss']) {
      await p.evaluate(n=>{ sheetName=n; document.getElementById('sheet').hidden=false; renderSheet(); document.getElementById('sheet').scrollTop=0; }, n);
      await shot('3-'+n);
      await p.evaluate(()=>{ document.getElementById('sheet').hidden=true; sheetName=null; });
    }
    await p.close();
  }
  const p=await b.newPage({viewport:{width:1080,height:1920},deviceScaleFactor:1});
  for(const [lang,dir] of [['pt','pt-BR'],['en','en-US']]){
    for(const [i,[n,cap]] of CAP[lang].entries()){
      await p.setContent(`<html><head>${font}<style>
        body{margin:0;width:1080px;height:1920px;background:linear-gradient(170deg,#3E9B5F,#1F6E4C);font-family:'Baloo 2',sans-serif;overflow:hidden;position:relative}
        .aw{position:absolute;top:0;left:0;right:0;height:70px;background:repeating-linear-gradient(90deg,#E4573D 0 90px,#FFF6E6 90px 180px);border-radius:0 0 36px 36px}
        h1{position:absolute;top:110px;left:70px;right:70px;margin:0;color:#fff;font-size:82px;line-height:1.02;text-align:center;text-shadow:0 4px 0 rgba(0,0,0,.18)}
        img{position:absolute;left:50%;transform:translateX(-50%);top:390px;width:840px;border-radius:44px;box-shadow:0 30px 70px rgba(0,0,0,.35);border:10px solid #10342A}
      </style></head><body><div class="aw"></div><h1>${cap}</h1><img src="${b64(S+lang+'-'+n+'.png')}"></body></html>`,{waitUntil:'networkidle'});
      await p.waitForTimeout(300);
      await p.screenshot({path:`${OUT}${dir}/capturas/${i+1}-${n.replace(/^\d-/,'')}.png`});
    }
  }
  // Gráfico de destaque 1024x500
  await p.setViewportSize({width:1024,height:500});
  for(const [lang,dir,t1,t2] of [['pt','pt-BR','Quitanda Zen','Junte, entregue e viaje pelas feiras do Brasil'],['en','en-US','Quitanda','Merge Across Brazil']]){
    await p.setContent(`<html><head>${font}<style>
      body{margin:0;width:1024px;height:500px;overflow:hidden;position:relative;background:radial-gradient(circle at 75% 40%,#5DBB7E,#2A8F63 55%,#1A5E42)}
      .aw{position:absolute;top:0;left:0;right:0;height:46px;background:repeating-linear-gradient(90deg,#E4573D 0 64px,#FFF6E6 64px 128px);border-radius:0 0 26px 26px}
      .ic{position:absolute;right:56px;top:86px;width:360px;height:360px;border-radius:72px;box-shadow:0 20px 50px rgba(0,0,0,.35);transform:rotate(4deg)}
      .tx{position:absolute;left:60px;top:110px;width:540px;color:#fff}
      h1{font-family:'Baloo 2';font-size:${lang==='pt'?100:112}px;line-height:.95;margin:0;text-shadow:0 5px 0 rgba(0,0,0,.2)}
      p{font-family:'Nunito';font-size:${lang==='pt'?34:44}px;line-height:1.15;margin:18px 0 0;color:#FFF6D9}
      .em{font-size:44px;margin-top:26px;letter-spacing:6px}
    </style></head><body><div class="aw"></div><img class="ic" src="${b64(path.join(RAIZ,'docs/arte/icones/quitanda-512.png'))}">
    <div class="tx"><h1>${t1}</h1><p>${t2}</p><div class="em">🍊🥥🦐🌽🍫</div></div></body></html>`,{waitUntil:'networkidle'});
    await p.waitForTimeout(300);
    await p.screenshot({path:`${OUT}${dir}/grafico-destaque-1024x500.png`});
  }
  await b.close();
  execFileSync('node', [path.join(RAIZ, 'app-android/scripts/copy-web.js')], { stdio: 'inherit' });   // volta o www ao normal
})();
