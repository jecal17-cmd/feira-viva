"""Recorta a arte dos itens do tabuleiro: tira o fundo branco, apaga textos soltos e deixa a peça quadrada.

Uso:  python recortar_itens.py CODIGO=IMAGEM.png [CODIGO=IMAGEM.png ...]
      python recortar_itens.py --todos      (refaz os WebP do jogo a partir das matrizes, sem recortar de novo)
  CODIGO  código do item na lista de arte (fr-1 = Frutas nível 1)
Gera docs/arte/itens/CODIGO.png (matriz: recorte de 512 px, fundo transparente, sem girar) e
versao-b-quitanda-zen/itens/CODIGO.webp (256 px, usado no jogo, já normalizado).

Normalização (para todos os itens parecerem do mesmo tamanho na casa do tabuleiro):
  - item bem comprido e deitado (peixe, milho, pimenta...) é girado para a diagonal, o maior espaço do quadrado,
    subindo pela ponta esquerda (ou pela direita, se estiver em GIRO); o que está em pé não gira;
  - a escala é escolhida para a parte visível ocupar AREA_ALVO do quadrado, sem passar de LADO_MAX.
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

AREA_ALVO, LADO_MAX = 0.36, 0.94
# Itens deitados sobem pela ponta esquerda; aqui ficam os que têm a "cabeça" à direita (sobem pela direita).
GIRO = {'pe-5': -45}

def normalizar(im, cod='', lado=512):
    a = np.asarray(im.getchannel('A')).astype(np.float64) / 255
    ys, xs = np.nonzero(a > 0.5)
    pts = np.vstack([xs - xs.mean(), ys - ys.mean()])
    ev, vec = np.linalg.eigh(np.cov(pts))
    along = (ev[1] / max(ev[0], 1e-9)) ** .5
    v = vec[:, 1]; ang = (np.degrees(np.arctan2(v[1], v[0])) + 90) % 180 - 90   # eixo maior, entre -90 e 90 (y para baixo)
    gira = along >= 2.5 and abs(ang) <= 70      # só os bem compridos; o que está em pé (garrafa, boneco) fica em pé
    if gira:
        if abs(abs(ang) - 45) <= 25: alvo = 45 if ang > 0 else -45     # já está quase na diagonal: só acerta
        else: alvo = GIRO.get(cod, 45)                                  # deitado: sobe pela ponta esquerda (45) ou direita (-45)
        im = im.rotate(-(alvo - ang), resample=Image.BICUBIC, expand=True)
    im = im.crop(im.getchannel('A').point(lambda v: 255 if v > 10 else 0).getbbox())
    area = (np.asarray(im.getchannel('A')).astype(np.float64) / 255).sum()
    esc = min((AREA_ALVO * lado * lado / area) ** .5, LADO_MAX * lado / max(im.size))
    im = im.resize((max(1, round(im.width * esc)), max(1, round(im.height * esc))), Image.LANCZOS)
    q = Image.new('RGBA', (lado, lado), (0, 0, 0, 0))
    q.paste(im, ((lado - im.width) // 2, (lado - im.height) // 2), im)
    return q

def para_jogo(cod):
    q = normalizar(Image.open(os.path.join(AQUI, cod + '.png')).convert('RGBA'), cod)
    os.makedirs(JOGO, exist_ok=True)
    q.resize((256, 256), Image.LANCZOS).save(os.path.join(JOGO, cod + '.webp'), quality=88, method=6)

if sys.argv[1:] == ['--todos']:
    import glob
    for f in sorted(glob.glob(os.path.join(AQUI, '[a-z][a-z]-[0-9].png'))):
        para_jogo(os.path.basename(f)[:-4]); print(os.path.basename(f)[:-4], 'ok')
    sys.exit()

for arg in sys.argv[1:]:
    cod, caminho = arg.split('=', 1)
    q = recortar(caminho)
    q.resize((512, 512), Image.LANCZOS).save(os.path.join(AQUI, cod + '.png'), optimize=True)
    para_jogo(cod)
    print(cod, 'ok')
