/* Vinheta Bentevi Apps: o bem-te-vi chega voando batendo as asas, freia, pousa no galho e canta o próprio nome.
   Arte do Nano Banana (docs/arte/vinheta/), recortada e embutida em VINHETA_IMG. Toda a animação sai de vinheta.quadro(t),
   com t em segundos desde o início: 0 a 1,42 s voo, até 1,86 s freada, 2,05 s canto (sílabas no tempo do CALL), 3,8 s "apps".
   Uso: vinheta.montar(palco, raiz) uma vez; depois vinheta.quadro(t) a cada quadro (requestAnimationFrame). */
const vinheta=(()=>{
  const W=300, SB=150/427, SG=290/820, KC=SB*1.08, KP=SB*1.22;      // escalas: pousado, galho, voo e freada (px de tela por px da arte)
  const TAM={galho:[820,850],pousado:[350,427],cantando:[304,422],v2_corpo:[438,313],v2_asacima:[297,387],v2_asabaixo:[426,347],v2_pouso:[439,467]};
  const PE={x:194,y:378}, PEC={x:204,y:262}, PEF={x:277,y:432};      // pés: pousado, corpo em voo, freada
  const OMB={x:185,y:100}, PC={x:268,y:322}, PB={x:345,y:45};        // ombro no corpo; ombro nas asas de cima e de baixo
  const ALVO={x:530*SG,y:567*SG}, CANTO=2.05, TF=1.42, TP=1.86, FLAP=7/1.42;
  const SILABAS=[[.03,.1],[.34,.13],[.565,.21]];                     // mesmo tempo do canto gravado (CALL)
  const cl=(v,a=0,b=1)=>Math.min(b,Math.max(a,v)), lerp=(a,b,k)=>a+(b-a)*k, seg=(t,a,b)=>cl((t-a)/(b-a)), sm=x=>x*x*(3-2*x);
  const bez=(x1,y1,x2,y2)=>t=>{ let u=t; for(let i=0;i<8;i++){ const x=3*(1-u)**2*u*x1+3*(1-u)*u*u*x2+u**3-t, d=3*(1-u)**2*x1+6*(1-u)*u*(x2-x1)+3*u*u*(1-x2); if(Math.abs(d)<1e-6) break; u=cl(u-x/d); } return 3*(1-u)**2*u*y1+3*(1-u)*u*u*y2+u**3; };
  const eOut=bez(0,0,.58,1), back=bez(.3,1.5,.5,1), eV=bez(.32,.1,.25,1);
  const cub=(a,b,c,d,u)=>(1-u)**3*a+3*(1-u)**2*u*b+3*(1-u)*u*u*c+u**3*d;
  const PATH=[[-300,-260],[-200,10],[-90,-10],[0,0]];
  const pos=k=>{ const u=eV(cl(k)); return [ALVO.x+cub(...PATH.map(p=>p[0]),u), ALVO.y+cub(...PATH.map(p=>p[1]),u)]; };
  let E=null;
  function img(n,k,extra){ const i=document.createElement('img'); i.src=VINHETA_IMG[n]; i.alt=''; i.draggable=false;
    i.style.cssText=`position:absolute;left:0;top:0;width:${TAM[n][0]*k}px;height:${TAM[n][1]*k}px;max-width:none;will-change:transform,opacity;${extra||''}`; return i; }
  function caixa(){ const d=document.createElement('div'); d.style.cssText='position:absolute;left:0;top:0;will-change:transform,opacity'; return d; }
  function montar(palco,raiz){
    palco.textContent=''; palco.style.cssText=`position:relative;width:${W}px;height:${W}px;flex:none`;
    const galho=caixa(); galho.style.width=galho.style.height=W+'px'; galho.style.transformOrigin='14px 297px';
    galho.append(img('galho',SG));
    const voo=caixa(), esc='filter:brightness(.72) saturate(.9)';
    const a2c=img('v2_asacima',KC,esc), a2b=img('v2_asabaixo',KC,esc), corpo=img('v2_corpo',KC), a1c=img('v2_asacima',KC), a1b=img('v2_asabaixo',KC);
    voo.append(a2c,a2b,corpo,a1c,a1b);
    const freio=caixa(); freio.append(img('v2_pouso',KP));
    const pouso=caixa(), parado=img('pousado',SB), canta=img('cantando',SB,`left:${9*SB}px;top:${4*SB}px;opacity:0`);
    pouso.append(parado,canta);
    galho.append(voo,freio,pouso); palco.append(galho);
    const wm=raiz.querySelector('.wm,.vn-wm');
    E={raiz,galho,voo,a1c,a1b,a2c,a2b,freio,pouso,parado,canta,sil:wm?[...wm.querySelectorAll('span')]:[],sub:wm&&wm.querySelector('i'),ws:raiz.querySelector('.wsub,.vn-sub')};
    a1c.style.transformOrigin=a2c.style.transformOrigin=`${PC.x*KC}px ${PC.y*KC}px`;
    a1b.style.transformOrigin=a2b.style.transformOrigin=`${PB.x*KC}px ${PB.y*KC}px`;
    voo.style.transformOrigin=`${PEC.x*KC}px ${PEC.y*KC}px`; freio.style.transformOrigin=`${PEF.x*KP}px ${PEF.y*KP}px`; pouso.style.transformOrigin=`${PE.x*SB}px ${PE.y*SB}px`;
    const larg=Math.min(window.innerWidth||360,560); palco.style.zoom='';                 // cabe em telas estreitas
    palco.style.transform=larg<W/.86?`scale(${larg*.86/W})`:''; palco.style.transformOrigin='50% 100%';
    quadro(0);
  }
  function asa(c,b,p,ox,oy,e){                     // p: 0 = asa no alto, 1 = asa embaixo
    const mix=sm(seg(p,.42,.58)), rc=lerp(0,-42,sm(cl(p/.6))), sc=lerp(1,.8,cl(p/.6)), rb=lerp(32,0,sm(seg(p,.4,1))), sb=lerp(.8,1,seg(p,.4,1));
    c.style.transform=`translate(${ox-PC.x*KC}px,${oy-PC.y*KC}px) rotate(${rc}deg) scale(${e},${sc*e})`;
    b.style.transform=`translate(${ox-PB.x*KC}px,${oy-PB.y*KC}px) rotate(${rb}deg) scale(${e},${sb*e})`;
    c.style.opacity=1-mix; b.style.opacity=mix;
  }
  const bate=c=>c<.42?sm(c/.42):1-sm((c-.42)/.58);   // a asa desce mais rápido do que sobe
  function quadro(t){
    if(!E) return;
    const z=eOut(seg(t,0,6)); E.raiz.style.transform=`scale(${1+.035*z})`;
    // voo
    const [fx,fy]=pos(seg(t,0,TP)), [fx2,fy2]=pos(seg(t,0,TP)+.004);
    const ang=cl(Math.atan2(fy2-fy,fx2-fx)*90/Math.PI,-20,20);
    const amt=1-sm(seg(t,TF-.12,TF)), c=(FLAP*t)%1, bob=-Math.sin(2*Math.PI*(c-.1))*3*amt;
    E.voo.style.transform=`translate(${fx-PEC.x*KC}px,${fy-PEC.y*KC+bob}px) rotate(${ang}deg)`;
    asa(E.a1c,E.a1b,bate(c)*amt,OMB.x*KC,OMB.y*KC,1);
    asa(E.a2c,E.a2b,bate((c+.94)%1)*amt,(OMB.x+16)*KC,(OMB.y-8)*KC,.9);
    const tf=sm(seg(t,TF-.05,TF+.07)), troca=seg(t,TP-.02,TP+.03);
    E.voo.style.opacity=Math.min(seg(t,0,.2),1-tf);
    // freada
    const fk=seg(t,TF-.05,TP), tremor=Math.sin(t*2*Math.PI*9)*1.2*(1-fk);
    E.freio.style.transform=`translate(${fx-PEF.x*KP}px,${fy-PEF.y*KP}px) rotate(${lerp(ang,-4,sm(fk))+tremor}deg) scale(${1+.03*Math.sin(Math.PI*fk)})`;
    E.freio.style.opacity=Math.min(tf,1-troca);
    // pousado: amortece, respira e canta
    const q=seg(t,TP,TP+.5);
    const sy0=q<.3?lerp(1,.93,eOut(q/.3)):q<.65?lerp(.93,1.025,eOut((q-.3)/.35)):lerp(1.025,1,eOut((q-.65)/.35));
    const resp=1+.007*Math.sin(2*Math.PI*1.1*(t-TP))*seg(t,TP+.4,TP+.8);
    let lift=0, aberto=false;
    SILABAS.forEach(([at,du],i)=>{ const t0=CANTO+at, k=seg(t,t0-.04,t0+du+.12); if(k>0&&k<1) lift+=Math.sin(Math.PI*k); if(t>=t0&&t<t0+du*.8) aberto=true;
      const s=E.sil[i]; if(s){ const m=back(seg(t,t0,t0+.4)); s.style.opacity=seg(t,t0,t0+.25); s.style.transform=`translateY(${lerp(12,0,m)}px) scale(${lerp(.88,1,m)})`; } });
    const sy=sy0*resp*(1+.012*lift), sx=(1+(1-sy0)*.6)/(1+.004*lift);
    E.pouso.style.transform=`translate(${ALVO.x-PE.x*SB}px,${ALVO.y-PE.y*SB-1.5*lift}px) rotate(${-2.2*lift}deg) scale(${sx},${sy})`;
    E.pouso.style.opacity=troca;
    E.canta.style.opacity=aberto?1:0; E.parado.style.opacity=aberto?0:1;
    // o galho balança com o peso
    const d=seg(t,TP-.02,TP+1.2);
    E.galho.style.transform=`rotate(${d>0&&d<1?3.4*Math.exp(-3.2*d)*Math.sin(d*Math.PI*2.6)*(1-d):0}deg)`;
    // sublinhado e "apps"
    const ws=eOut(seg(t,CANTO+1.75,CANTO+2.3));
    if(E.sub) E.sub.style.transform=`scaleX(${ws})`;
    if(E.ws){ E.ws.style.opacity=ws; E.ws.style.transform=`translateY(${6*(1-ws)}px)`; }
  }
  return {montar,quadro,FIM:5.35,CANTO,FINAL:4.6};
})();
