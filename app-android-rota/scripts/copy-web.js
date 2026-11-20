// Copia o jogo da Versão A (um único HTML) para a pasta www, que o Capacitor empacota no app.
const fs = require('fs'), path = require('path');
const src = path.join(__dirname, '..', '..', 'versao-a-rota-das-feiras', 'index.html');
const dst = path.join(__dirname, '..', 'www');
fs.mkdirSync(dst, { recursive: true });
let html = fs.readFileSync(src, 'utf8');
// COMPRAS=play liga as compras de verdade pela Google Play (plugin Compras); sem isso, são simuladas.
// Só funcionam no app baixado da Play Store, com os produtos criados na Play Console.
if (process.env.COMPRAS === 'play') {
  if (!/const PAGAMENTO='simulado';/.test(html)) { console.error('Não achei a constante PAGAMENTO no index.html'); process.exit(1); }
  html = html.replace(/const PAGAMENTO='simulado';/, "const PAGAMENTO='play';");
  console.log('Compras: Google Play (dinheiro real)');
}
fs.writeFileSync(path.join(dst, 'index.html'), html);
const icone = path.join(path.dirname(src), 'icone-192.png');
if (fs.existsSync(icone)) fs.copyFileSync(icone, path.join(dst, 'icone-192.png'));
// Arte dos mercados, dos itens, dos personagens e dos obstáculos (caixote e mofo); trilhas dos mercados
for (const pasta of ['mercados', 'itens', 'personagens', 'musica', 'obstaculos']) {
  const arte = path.join(path.dirname(src), pasta);
  if (fs.existsSync(arte)) fs.cpSync(arte, path.join(dst, pasta), { recursive: true });
}
console.log('Jogo copiado para www/index.html');
