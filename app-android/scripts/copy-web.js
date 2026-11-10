// Copia o jogo (um único HTML) para a pasta www, que o Capacitor empacota no app.
const fs = require('fs'), path = require('path');
const src = path.join(__dirname, '..', '..', 'versao-b-quitanda-zen', 'index.html');
const dst = path.join(__dirname, '..', 'www');
fs.mkdirSync(dst, { recursive: true });
fs.copyFileSync(src, path.join(dst, 'index.html'));
console.log('Jogo copiado para www/index.html');
