// Copia o jogo da Versão A (um único HTML) para a pasta www, que o Capacitor empacota no app.
const fs = require('fs'), path = require('path');
const src = path.join(__dirname, '..', '..', 'versao-a-rota-das-feiras', 'index.html');
const dst = path.join(__dirname, '..', 'www');
fs.mkdirSync(dst, { recursive: true });
fs.copyFileSync(src, path.join(dst, 'index.html'));
const icone = path.join(path.dirname(src), 'icone-192.png');
if (fs.existsSync(icone)) fs.copyFileSync(icone, path.join(dst, 'icone-192.png'));
// Arte dos mercados e dos itens
for (const pasta of ['mercados', 'itens']) {
  const arte = path.join(path.dirname(src), pasta);
  if (fs.existsSync(arte)) fs.cpSync(arte, path.join(dst, pasta), { recursive: true });
}
console.log('Jogo copiado para www/index.html');
