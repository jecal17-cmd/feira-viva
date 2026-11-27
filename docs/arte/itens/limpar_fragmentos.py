"""Tira pedacinhos soltos que vieram da casa vizinha da grade (ex.: a ponta de um limão embaixo de uma garrafa).

Uso:  python limpar_fragmentos.py CODIGO [CODIGO...]      ex.: python limpar_fragmentos.py rota/qc-2 rota/qc-4
Lê a matriz de 512 px (docs/arte/itens/[rota/]CODIGO.png), apaga as partes soltas menores que a principal com o centro
na faixa da borda (vieram da casa vizinha) ou que têm menos de MINIMO da área da maior, grava a matriz de volta e refaz o WebP do jogo (como o fatiar_grade.py).
"""
import os, sys
import numpy as np
from PIL import Image
from scipy import ndimage
AQUI = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, AQUI)
import recortar_itens as R

RAIZ = os.path.normpath(os.path.join(AQUI, '..', '..', '..'))
MINIMO = 0.06

for cod in sys.argv[1:]:
    rota = cod.startswith('rota/'); nome = cod.split('/')[-1]
    arq = os.path.join(AQUI, 'rota' if rota else '', nome + '.png')
    im = Image.open(arq).convert('RGBA'); a = np.array(im)
    rot, n = ndimage.label(a[..., 3] > 24)
    if n > 1:
        areas = ndimage.sum(np.ones_like(rot), rot, range(1, n + 1))
        H, W = rot.shape; cm = ndimage.center_of_mass(np.ones_like(rot), rot, range(1, n + 1))
        naborda = lambda y, x: y < .12 * H or y > .88 * H or x < .12 * W or x > .88 * W        # centro na faixa de fora
        fora = [k + 1 for k, t in enumerate(areas) if t < areas.max() and (t < MINIMO * areas.max() or naborda(*cm[k]))]
        a[np.isin(ndimage.binary_dilation(np.isin(rot, fora), iterations=2) * rot, fora) | np.isin(rot, fora), 3] = 0
    q = Image.fromarray(a, 'RGBA'); q = q.crop(q.getbbox())
    lado = max(q.size); quad = Image.new('RGBA', (lado, lado)); quad.paste(q, ((lado - q.width) // 2, (lado - q.height) // 2))
    quad.resize((512, 512), Image.LANCZOS).save(arq, optimize=True)
    jogo = os.path.join(RAIZ, 'versao-a-rota-das-feiras' if rota else 'versao-b-quitanda-zen', 'itens', nome + '.webp')
    R.normalizar(quad, nome).resize((256, 256), Image.LANCZOS).save(jogo, quality=88, method=6)
    print(cod, f'{n - 1} parte(s) solta(s) avaliada(s)')
