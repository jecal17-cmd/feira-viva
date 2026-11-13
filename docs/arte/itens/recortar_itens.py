"""Recorta a arte dos itens do tabuleiro: tira o fundo branco, apaga textos soltos e deixa a peça quadrada.

Uso:  python recortar_itens.py CODIGO=IMAGEM.png [CODIGO=IMAGEM.png ...]
  CODIGO  código do item na lista de arte (fr-1 = Frutas nível 1)
Gera docs/arte/itens/CODIGO.png (512 px, fundo transparente) e versao-b-quitanda-zen/itens/CODIGO.webp (256 px, usado no jogo).
Precisa de Pillow, numpy, scipy e rembg (pip install "rembg[cpu]" scipy).
"""
import os, sys
import numpy as np
from PIL import Image
from scipy import ndimage

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.normpath(os.path.join(AQUI, '..', '..', '..'))
JOGO = os.path.join(RAIZ, 'versao-b-quitanda-zen', 'itens')

_sessao = None
def mascara(img):
    """Alfa da peça pelo removedor de fundo rembg (modelo isnet-general-use, baixado na 1ª vez)."""
    global _sessao
    from rembg import new_session, remove
    if _sessao is None: _sessao = new_session('isnet-general-use')
    return np.asarray(remove(img, session=_sessao, only_mask=True), dtype=np.float32) / 255

def recortar(caminho):
    img = Image.open(caminho).convert('RGB')
    im = np.asarray(img).astype(np.float32)
    alfa = mascara(img)
    # fica com a peça principal e partes grandes (ex.: duas frutas); some com textos e respingos
    rot, n = ndimage.label(alfa > 0.5)
    if n == 0: raise SystemExit(f'nada encontrado em {caminho}')
    tam = ndimage.sum(np.ones_like(alfa), rot, range(1, n + 1))
    manter = np.isin(rot, [i + 1 for i, t in enumerate(tam) if t >= tam.max() * 0.08])
    alfa = np.where(ndimage.binary_dilation(manter, iterations=4), alfa, 0)
    alfa = np.where(alfa < 0.04, 0, alfa)
    # tira o halo branco das bordas semitransparentes
    k = np.maximum(alfa, 1e-3)[..., None]
    cor = np.where(k > 0.98, im, np.clip((im - 255 * (1 - k)) / k, 0, 255))
    out = Image.fromarray(np.dstack([cor, alfa * 255]).astype(np.uint8), 'RGBA')
    out = out.crop(out.getchannel('A').point(lambda v: 255 if v > 10 else 0).getbbox())
    lado = round(max(out.size) * 1.08)
    q = Image.new('RGBA', (lado, lado), (0, 0, 0, 0))
    q.paste(out, ((lado - out.width) // 2, (lado - out.height) // 2))
    return q

for arg in sys.argv[1:]:
    cod, caminho = arg.split('=', 1)
    q = recortar(caminho)
    q.resize((512, 512), Image.LANCZOS).save(os.path.join(AQUI, cod + '.png'), optimize=True)
    os.makedirs(JOGO, exist_ok=True)
    q.resize((256, 256), Image.LANCZOS).save(os.path.join(JOGO, cod + '.webp'), quality=88, method=6)
    print(cod, 'ok')
