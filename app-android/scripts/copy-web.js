// Copia o jogo (um único HTML) para a pasta www, que o Capacitor empacota no app.
//
// Versão de publicação (AAB da Play Store): rode com PUBLICACAO=1. Aí o script
//  - esconde a Loja com dinheiro real (ainda não há Google Play Billing) e as ferramentas de teste;
//  - troca o texto "protótipo" pela versão (VERSAO, padrão: versionName do package.json);
//  - usa os blocos de anúncio reais do AdMob, se ADMOB_REWARDED_ID e ADMOB_INTERSTITIAL_ID existirem.
const fs = require('fs'), path = require('path');
const src = path.join(__dirname, '..', '..', 'versao-b-quitanda-zen', 'index.html');
const dst = path.join(__dirname, '..', 'www');
fs.mkdirSync(dst, { recursive: true });
let html = fs.readFileSync(src, 'utf8');

function trocar(regex, novo, nome) {
  if (!regex.test(html)) { console.error(`Não achei ${nome} no index.html`); process.exit(1); }
  html = html.replace(regex, novo);
}

if (process.env.PUBLICACAO === '1') {
  const versao = process.env.VERSAO || require('../package.json').version;
  trocar(/const PUB=\{loja:true,dev:true,ver:'',/, `const PUB={loja:false,dev:false,ver:'v${versao}',`, 'a constante PUB');
  const rew = process.env.ADMOB_REWARDED_ID, int = process.env.ADMOB_INTERSTITIAL_ID;
  if (rew && int) {
    trocar(/const ADMOB=\{[^}]*\};/, `const ADMOB={test:false,rew:'${rew}',int:'${int}'};`, 'a constante ADMOB');
    console.log('Anúncios: blocos reais do AdMob');
  } else {
    console.warn('AVISO: ADMOB_REWARDED_ID e ADMOB_INTERSTITIAL_ID não definidos; o app sai com anúncios de TESTE (sem receita).');
  }
  console.log(`Versão de publicação v${versao}: loja paga e ferramentas de teste escondidas`);
}

fs.writeFileSync(path.join(dst, 'index.html'), html);
const icone = path.join(path.dirname(src), 'icone-192.png');
if (fs.existsSync(icone)) fs.copyFileSync(icone, path.join(dst, 'icone-192.png'));
// Arte dos mercados (mapa, tela inicial e viagens) e dos itens do tabuleiro
for (const pasta of ['mercados', 'itens']) {
  const arte = path.join(path.dirname(src), pasta);
  if (fs.existsSync(arte)) fs.cpSync(arte, path.join(dst, pasta), { recursive: true });
}
console.log('Jogo copiado para www/index.html');
