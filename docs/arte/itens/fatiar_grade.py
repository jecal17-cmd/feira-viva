"""Fatia uma grade de itens gerada de uma vez (ver docs/arte/prompt-nano-banana.md) e põe cada item no jogo.

Uso:  python fatiar_grade.py GRADE.png COLUNAS LINHAS LOTE
  LOTE  chave de grades.json: "todos" (8 x 8), "1".."4" (4 x 4), "extra" (5 x 4: refações e decoração) ou "personagens" (6 x 5)
Cada célula vira um item: o fundo é tirado (rembg), a matriz de 512 px vai para docs/arte/itens/ (ou docs/arte/itens/rota/)
e o WebP normalizado vai para o jogo certo (Quitanda ou, com o prefixo rota/, Rota das Feiras).
Depois, acrescente os códigos em ITEM_ART no index.html de cada jogo e rode docs/arte/atualizar_status.py.
"""
import json, os, sys
from PIL import Image
AQUI = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, AQUI)
import recortar_itens as R

RAIZ = os.path.normpath(os.path.join(AQUI, '..', '..', '..'))
grade, cols, rows, lote = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
codigos = json.load(open(os.path.join(AQUI, 'grades.json')))[lote]
im = Image.open(grade).convert('RGB'); W, H = im.size; cw, ch = W / cols, H / rows
tmp = os.path.join(AQUI, '_celulas'); os.makedirs(tmp, exist_ok=True)
def salvar(cod, q):
    if cod.startswith(('decoracao/', 'personagens/')):          # ainda não aparecem no jogo: só a matriz em docs/arte/
        pasta, nome = cod.split('/'); d = os.path.join(AQUI, '..', pasta); os.makedirs(d, exist_ok=True)
        q.resize((512, 512), Image.LANCZOS).save(os.path.join(d, nome + '.png'), optimize=True); return
    rota = cod.startswith('rota/'); nome = cod.split('/')[-1]
    mdir = os.path.join(AQUI, 'rota') if rota else AQUI; os.makedirs(mdir, exist_ok=True)
    q.resize((512, 512), Image.LANCZOS).save(os.path.join(mdir, nome + '.png'), optimize=True)
    jogo = os.path.join(RAIZ, 'versao-a-rota-das-feiras' if rota else 'versao-b-quitanda-zen', 'itens'); os.makedirs(jogo, exist_ok=True)
    R.normalizar(q.convert('RGBA'), nome).resize((256, 256), Image.LANCZOS).save(os.path.join(jogo, nome + '.webp'), quality=88, method=6)

for k, cod in enumerate(codigos):          # "a+b": a mesma célula serve aos dois destinos
    if not cod: continue                     # célula ignorada (veio errada)
    x, y = k % cols, k // cols
    cel = im.crop((round(x * cw), round(y * ch), round((x + 1) * cw), round((y + 1) * ch)))
    arq = os.path.join(tmp, cod.replace('/', '_').replace('+', '_') + '.png'); cel.save(arq)
    q = R.recortar(arq)
    for c in cod.split('+'): salvar(c, q)
    print(cod, 'ok')
