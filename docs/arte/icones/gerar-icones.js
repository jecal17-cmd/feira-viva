// ANTIGO: ícones desenhados em SVG (v0.4). Desde a v0.5 os ícones vêm das artes quitanda-arte.png e rota-arte.png,
// geradas com gerar_icones_arte.py (veja CONTEXTO.md). Rodar este script sobrescreve os ícones novos.
// Gera os ícones e as telas de abertura dos apps Android a partir dos desenhos em SVG abaixo.
// Uso (na raiz do repositório): node docs/arte/icones/gerar-icones.js   (precisa do Playwright)
const { chromium } = require('playwright');
const fs = require('fs'), path = require('path');

// Arte em 108×108 (grade do ícone adaptativo do Android); o conteúdo fica na área segura central (21 a 87).
const ART = {
  quitanda: { bg: '#2A8F63', svg: `
    <g>
      <rect x="29" y="44" width="3.5" height="20" rx="1.5" fill="#7A4E2A"/><rect x="75.5" y="44" width="3.5" height="20" rx="1.5" fill="#7A4E2A"/>
      <rect x="24" y="29" width="60" height="15" rx="3" fill="#FFF6E8"/>
      ${[0,2,4].map(k=>`<rect x="${24+k*10}" y="29" width="10" height="15" fill="#E4573D"${k===0?' rx="3"':''}/>`).join('')}
      <path d="M74 29h7a3 3 0 0 1 3 3v12h-10z" fill="#FFF6E8"/>
      ${[0,1,2,3,4,5].map(k=>`<circle cx="${29+k*10}" cy="44" r="5" fill="${k%2?'#FFF6E8':'#E4573D'}"/>`).join('')}
      <circle cx="42" cy="57.5" r="7.5" fill="#F39A2B"/><path d="M42 50.5q3-4 6-2q-3 3-6 2z" fill="#3E9B5F"/>
      <circle cx="56" cy="56.5" r="8" fill="#8CC63F"/><circle cx="53.5" cy="54" r="2" fill="#C8E68C"/>
      <circle cx="69" cy="57.5" r="7" fill="#E4573D"/><path d="M69 50.5q1-3 3-3.5" stroke="#5A3A1E" stroke-width="1.6" fill="none" stroke-linecap="round"/>
      <rect x="27" y="62" width="54" height="18" rx="3.5" fill="#B5763E"/>
      <rect x="27" y="62" width="54" height="4.5" rx="2" fill="#C98A50"/>
      <path d="M31 72h46" stroke="#8E5A2C" stroke-width="1.6" stroke-linecap="round"/>
    </g>` },
  rota: { bg: '#0F7A73', svg: `
    <g>
      <path d="M27 81 C40 82 36 66 48 64 S60 66 62 60" stroke="#FFF6D9" stroke-width="4" stroke-linecap="round" stroke-dasharray=".1 8" fill="none"/>
      <circle cx="27" cy="81" r="4.5" fill="#FFF6D9"/>
      <path d="M66 70 C58 60 50 52 50 42 a16 16 0 0 1 32 0 C82 52 74 60 66 70z" fill="#F2B33D"/>
      <path d="M66 70 C58 60 50 52 50 42 a16 16 0 0 1 16-16" fill="none" stroke="#FFD675" stroke-width="2" stroke-linecap="round" opacity=".7"/>
      <circle cx="66" cy="42" r="11" fill="#FFF6D9"/>
      <circle cx="62" cy="44.5" r="4.6" fill="#5B2A86"/><circle cx="70" cy="44.5" r="4.6" fill="#5B2A86"/><circle cx="66" cy="38" r="4.6" fill="#6E3AA0"/>
      <circle cx="60.6" cy="43" r="1.2" fill="#fff" opacity=".8"/><circle cx="68.6" cy="43" r="1.2" fill="#fff" opacity=".8"/><circle cx="64.6" cy="36.5" r="1.2" fill="#fff" opacity=".8"/>
    </g>` }
};
const svg = (a, { size, bg, shape, scale = 1 }) => {
  const s = 108, t = `translate(${s/2} ${s/2}) scale(${scale}) translate(${-s/2} ${-s/2})`;
  const back = !bg ? '' : shape === 'circle' ? `<circle cx="54" cy="54" r="54" fill="${a.bg}"/>` : shape === 'round' ? `<rect width="108" height="108" rx="22" fill="${a.bg}"/>` : `<rect width="108" height="108" fill="${a.bg}"/>`;
  return `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 108 108" width="${size}" height="${size}">${back}<g transform="${t}">${a.svg}</g></svg>`;
};
const DENS = { mdpi: 1, hdpi: 1.5, xhdpi: 2, xxhdpi: 3, xxxhdpi: 4 };
(async () => {
  const b = await chromium.launch(), p = await b.newPage();
  const shot = async (html, w, h, file, transparent) => {
    await p.setViewportSize({ width: w, height: h });
    await p.setContent(`<html><body style="margin:0;background:transparent">${html}</body></html>`);
    fs.mkdirSync(path.dirname(file), { recursive: true });
    await p.screenshot({ path: file, omitBackground: !!transparent, clip: { x: 0, y: 0, width: w, height: h } });
  };
  for (const [key, dir] of [['quitanda', 'app-android'], ['rota', 'app-android-rota']]) {
    const a = ART[key], res = `${dir}/android/app/src/main/res`;
    for (const [d, k] of Object.entries(DENS)) {
      // No ícone adaptativo, a arte fica dentro do círculo seguro de 66dp, para não ser cortada em nenhum formato de máscara.
      await shot(svg(a, { size: 108 * k, scale: .82 }), 108 * k, 108 * k, `${res}/mipmap-${d}/ic_launcher_foreground.png`, true);
      await shot(svg(a, { size: 48 * k, bg: 1, shape: 'round', scale: 1.3 }), 48 * k, 48 * k, `${res}/mipmap-${d}/ic_launcher.png`, true);
      await shot(svg(a, { size: 48 * k, bg: 1, shape: 'circle', scale: 1.25 }), 48 * k, 48 * k, `${res}/mipmap-${d}/ic_launcher_round.png`, true);
    }
    fs.writeFileSync(`${res}/values/ic_launcher_background.xml`, `<?xml version="1.0" encoding="utf-8"?>\n<resources>\n    <color name="ic_launcher_background">${a.bg}</color>\n</resources>\n`);
    // Telas de abertura: a arte no centro, sobre a cor do ícone, em todos os tamanhos que o Capacitor criou.
    for (const f of fs.readdirSync(res).filter(x => x.startsWith('drawable')).map(x => `${res}/${x}/splash.png`).filter(fs.existsSync)) {
      const { w, h } = await p.evaluate(async src => { const i = new Image(); i.src = src; await i.decode(); return { w: i.width, h: i.height }; }, 'data:image/png;base64,' + fs.readFileSync(f).toString('base64'));
      const z = Math.round(Math.min(w, h) * .8);
      await shot(`<div style="width:${w}px;height:${h}px;background:${a.bg};display:grid;place-items:center">${svg(a, { size: z, scale: 1.25 })}</div>`, w, h, f);
    }
    // Ícone da loja (512×512) e prévia
    await shot(svg(a, { size: 512, bg: 1, scale: 1.3 }), 512, 512, `docs/arte/icones/${key}-512.png`);
    fs.writeFileSync(`docs/arte/icones/${key}.svg`, svg(a, { size: 512, bg: 1, shape: 'round', scale: 1.3 }));
  }
  await b.close(); console.log('ícones gerados');
})();
