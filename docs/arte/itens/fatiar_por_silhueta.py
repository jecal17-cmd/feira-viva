"""Recorta figuras de uma grade em que elas passam do limite das células (ex.: personagens com chapéu).

Em vez de cortar a grade em células fixas, tira o fundo da imagem inteira, separa as figuras pela silhueta e
entrega a cada código todas as partes cujo centro cai na célula dele (um vendedor e o carrinho, a fumaça da panela…).

Uso:  python fatiar_por_silhueta.py GRADE.png COLUNAS LINHAS LOTE      (LOTE: chave de grades.json; "" = célula ignorada)
Grava docs/arte/<pasta>/<nome>.png (512 px, fundo transparente).
"""
import json, os, sys
import numpy as np
from PIL import Image
from scipy import ndimage
AQUI = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, AQUI)
import recortar_itens as R

grade, cols, rows, lote = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
codigos = json.load(open(os.path.join(AQUI, 'grades.json')))[lote]
img = Image.open(grade).convert('RGB'); W, H = img.size; cw, ch = W / cols, H / rows
a = R.mascara(img)
lab, n = ndimage.label(ndimage.binary_closing(a > 0.5, iterations=2))
centros = ndimage.center_of_mass(np.ones_like(lab), lab, range(1, n + 1))
areas = ndimage.sum(np.ones_like(lab), lab, range(1, n + 1))
dono = {}
for i, ((cy, cx), ar) in enumerate(zip(centros, areas), 1):
    if ar < W * H * 0.0004: continue                      # poeira
    k = int(cy // ch) * cols + int(cx // cw)
    dono.setdefault(k, []).append(i)
for k, cod in enumerate(codigos):
    if not cod or k not in dono: continue
    m = np.isin(lab, dono[k])
    alfa = np.where(ndimage.binary_dilation(m, iterations=3), a, 0)
    out = Image.fromarray(np.dstack([np.asarray(img), (alfa * 255).astype(np.uint8)]), 'RGBA')
    out = out.crop(out.getchannel('A').point(lambda v: 255 if v > 10 else 0).getbbox())
    s = round(max(out.size) * 1.08); q = Image.new('RGBA', (s, s), (0, 0, 0, 0)); q.paste(out, ((s - out.width) // 2, (s - out.height) // 2), out)
    pasta, nome = cod.split('/'); d = os.path.join(AQUI, '..', pasta); os.makedirs(d, exist_ok=True)
    q.resize((512, 512), Image.LANCZOS).save(os.path.join(d, nome + '.png'), optimize=True)
    print(cod, len(dono[k]), 'partes')
