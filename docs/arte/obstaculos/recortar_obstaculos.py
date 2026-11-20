"""Recorta as tiras de 5 quadros do mofo e da caixa (fundo branco) em WebP transparentes.

Uso: python docs/arte/obstaculos/recortar_obstaculos.py
Entrada: docs/arte/obstaculos/{mofo,caixa}-original.jpg (2320x464, 5 quadros de 464 px)
Saída:   versao-a-rota-das-feiras/obstaculos/{mofo,caixa}-1..5.webp (192 px)

O fundo é o branco ligado à borda (preenchimento a partir das bordas). Nessa região,
o branco vira transparência suave (espuma, poeira e nuvens claras ficam translúcidas);
o que está dentro dos contornos continua opaco. Miolos brancos grandes (o vão da
caixa quebrada) também viram fundo.
"""
from pathlib import Path
import numpy as np
from PIL import Image
from scipy import ndimage

AQUI = Path(__file__).parent
SAIDA = AQUI.parents[2] / 'versao-a-rota-das-feiras' / 'obstaculos'
LADO, TAM = 464, 192

def recortar(quadro):
    a = np.asarray(quadro.convert('RGB')).astype(float)
    claro = a.min(2) > 175                       # candidatos a fundo
    rot, _ = ndimage.label(claro)
    borda = set(np.unique(np.concatenate([rot[0], rot[-1], rot[:, 0], rot[:, -1]]))) - {0}
    fundo = np.isin(rot, list(borda))
    # miolos brancos fechados (o vão da caixa quebrada) também são fundo
    branco = a.min(2) > 232
    rb, n = ndimage.label(branco)
    tam = ndimage.sum(branco, rb, range(1, n + 1))
    grandes = [k + 1 for k, t in enumerate(tam) if t > 300]
    fundo |= ndimage.binary_dilation(np.isin(rb, grandes), iterations=2) & claro
    # branco -> transparência (como "cor para alfa" do GIMP)
    alfa = np.clip((255 - a).max(2) / 255 * 1.6, 0, 1)
    alfa[alfa < .06] = 0
    alfa = np.where(fundo, alfa, 1.0)
    cor = np.where(fundo[..., None] & (alfa[..., None] > 0),
                   255 - (255 - a) / np.maximum(alfa[..., None], 1e-3), a)
    rgba = np.dstack([np.clip(cor, 0, 255), alfa * 255]).astype(np.uint8)
    return Image.fromarray(rgba, 'RGBA')

SAIDA.mkdir(parents=True, exist_ok=True)
for nome in ('mofo', 'caixa'):
    tira = Image.open(AQUI / f'{nome}-original.jpg')
    for k in range(5):
        q = recortar(tira.crop((k * LADO, 0, (k + 1) * LADO, LADO)))
        q.resize((TAM, TAM), Image.LANCZOS).save(SAIDA / f'{nome}-{k + 1}.webp', quality=88, method=6)
        print(f'{nome}-{k + 1}.webp')
