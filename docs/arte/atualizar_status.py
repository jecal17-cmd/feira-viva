"""Marca na lista de arte o que já tem imagem no jogo (✅) e o que falta (⬜).

Confere os arquivos de verdade em versao-b-quitanda-zen/ (mercados/*.webp, itens/*.webp, personagens/*.webp,
decoracao/*.webp), atualiza a coluna "Arte" das tabelas de lista-de-arte.md, a seção "Progresso" e a coluna
"status" de lista-de-arte.csv. Rode de novo sempre que entrar arte nova:  python docs/arte/atualizar_status.py
"""
import csv, io, os, re

AQUI = os.path.dirname(os.path.abspath(__file__))
JOGO = os.path.normpath(os.path.join(AQUI, '..', '..', 'versao-b-quitanda-zen'))
MD, CSV = os.path.join(AQUI, 'lista-de-arte.md'), os.path.join(AQUI, 'lista-de-arte.csv')

def tem(arquivo):                       # 'itens/fr-1.png' -> existe versao-b-quitanda-zen/itens/fr-1.webp?
    base = os.path.splitext(arquivo)[0]
    return any(os.path.exists(os.path.join(JOGO, base + ext)) for ext in ('.webp', '.png'))

# CSV
with open(CSV, encoding='utf-8-sig', newline='') as f: rows = list(csv.DictReader(f))
campos = [c for c in rows[0] if c != 'status']; campos.insert(2, 'status')
grupos = {}
for r in rows:
    r['status'] = 'carregada' if tem(r['arquivo']) else 'faltando'
    g = grupos.setdefault(r['tipo'], [0, 0, []]); g[1] += 1
    if r['status'] == 'carregada': g[0] += 1
    else: g[2].append(r)
o = io.StringIO(); w = csv.DictWriter(o, fieldnames=campos, quoting=csv.QUOTE_ALL, lineterminator='\n')
w.writeheader(); w.writerows({k: r[k] for k in campos} for r in rows)
open(CSV, 'w', encoding='utf-8-sig', newline='').write(o.getvalue())

# MD: coluna Arte
linhas, out, na_tabela = open(MD, encoding='utf-8').read().split('\n'), [], False
for n, ln in enumerate(linhas):
    if ln.startswith('|') and 'Arquivo' in ln and not ln.startswith('| `') and 'referencias/' not in ''.join(linhas[n + 2:n + 3]):
        na_tabela = True
        ln = ln if ln.rstrip().endswith('| Arte |') else ln.rstrip() + ' Arte |'
    elif na_tabela and re.match(r'^\|[-| ]+\|$', ln.strip()):
        cols = ln.strip().count('|') - 1
        hdr = out[-1].count('|') - 1
        ln = ln.strip() + ('---|' if cols < hdr else '')
    elif na_tabela and ln.startswith('|'):
        m = re.search(r'`((?:mercados|itens|personagens|decoracao)/[^`]+)`', ln)
        marca = ('✅' if m and tem(m.group(1)) else '⬜')
        cel = ln.rstrip().split('|')[1:-1]
        ncols = next(l for l in reversed(out) if 'Arquivo' in l).count('|') - 1
        if len(cel) == ncols: cel[-1] = f' {marca} '
        else: cel.append(f' {marca} ')
        ln = '|' + '|'.join(cel) + '|'
    else:
        na_tabela = na_tabela and ln.startswith('|')
    out.append(ln)
md = '\n'.join(out)

# MD: seção Progresso
nomes = {'mercado': 'Mercados', 'item': 'Itens do tabuleiro', 'personagem': 'Personagens', 'decoracao': 'Decoração da banca'}
p = ['## Progresso da arte', '', 'Atualizado por `atualizar_status.py`. ✅ = imagem já no jogo · ⬜ = falta gerar.', '',
     '| Grupo | Prontas | Faltam |', '|---|---|---|']
for t in ('mercado', 'item', 'personagem', 'decoracao'):
    ok, tot, falta = grupos[t]; p.append(f'| {nomes[t]} | {ok} de {tot} | {tot - ok} |')
falta_it = grupos['item'][2]
if falta_it:
    por = {}
    for r in falta_it: por.setdefault(r['descricao_pt'].split(',')[0], []).append(r['nome_pt'])
    p += ['', '**Itens que faltam, por linha:**', '']
    p += [f'- {k} ({len(v)}): {", ".join(v)}' for k, v in por.items()]
bloco = '\n'.join(p) + '\n\n'
if '## Progresso da arte' in md:
    i = md.index('## Progresso da arte'); j = md.index('\n## ', i + 5) + 1
    md = md[:i] + bloco + md[j:]
else:
    i = md.index('## Como gerar'); md = md[:i] + bloco + md[i:]
open(MD, 'w', encoding='utf-8').write(md)
print({nomes[t]: f'{g[0]}/{g[1]}' for t, g in grupos.items()})
