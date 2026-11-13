"""Marca na lista de arte o que já tem imagem no jogo (✅) e o que falta (⬜).

Confere os arquivos de verdade em versao-b-quitanda-zen/ (mercados/*.webp, itens/*.webp, personagens/*.webp,
decoracao/*.webp), atualiza a coluna "Arte" das tabelas de lista-de-arte.md, a seção "Progresso" e a coluna
"status" de lista-de-arte.csv e gera falta-gerar.md (só o que falta, com prompts prontos). Rode de novo sempre que entrar arte nova:  python docs/arte/atualizar_status.py
"""
import csv, io, os, re

AQUI = os.path.dirname(os.path.abspath(__file__))
JOGO = os.path.normpath(os.path.join(AQUI, '..', '..', 'versao-b-quitanda-zen'))
MD, CSV = os.path.join(AQUI, 'lista-de-arte.md'), os.path.join(AQUI, 'lista-de-arte.csv')
FALTA = os.path.join(AQUI, 'falta-gerar.md')

# Arte que já está no jogo mas vale gerar de novo (código ou arquivo -> motivo). Apague a linha quando refizer.
REFAZER = {
    'itens/fr-8.png': 'o creme saiu marrom, com cara de chocolate; açaí é roxo-escuro (o prompt já pede "deep purple")',
    'mercados/03-feira-de-sao-joaquim-salvador.png': 'a faixa tem texto embaralhado; peça "no text, no signs"',
    'mercados/05-mercado-central-fortaleza.png': 'a fachada tem texto embaralhado; peça "no text, no signs"',
    'mercados/06-feira-central-campo-grande.png': 'toldos e placas com "SOBÁ" escrito à mão, letras tortas',
}

ROTA = os.path.normpath(os.path.join(AQUI, '..', '..', 'versao-a-rota-das-feiras'))
def tem(arquivo):                       # 'itens/fr-1.png' -> versao-b-quitanda-zen/itens/fr-1.webp; 'rota/itens/ac-1.png' -> versao-a-...
    base = os.path.splitext(arquivo)[0]; raiz = JOGO
    if base.startswith('rota/'): base, raiz = base[5:], ROTA
    return any(os.path.exists(os.path.join(raiz, base + ext)) for ext in ('.webp', '.png'))

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
        m = re.search(r'`((?:mercados|itens|rota/itens|personagens|decoracao)/[^`]+)`', ln)
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
nomes = {'mercado': 'Mercados', 'item': 'Itens do tabuleiro', 'item-rota': 'Itens da Rota das Feiras', 'personagem': 'Personagens', 'decoracao': 'Decoração da banca'}
p = ['## Progresso da arte', '', 'Atualizado por `atualizar_status.py`. ✅ = imagem já no jogo · ⬜ = falta gerar.', '',
     '| Grupo | Prontas | Faltam |', '|---|---|---|']
for t in ('mercado', 'item', 'item-rota', 'personagem', 'decoracao'):
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

# falta-gerar.md: lista de trabalho, só com o que falta
nomes_pl = {'mercado': 'Mercados', 'item': 'Itens do tabuleiro', 'item-rota': 'Itens da Rota das Feiras', 'personagem': 'Personagens', 'decoracao': 'Decoração da banca'}
f = ['# Feira Viva · Arte que falta gerar', '',
     'Gerado por `atualizar_status.py` a partir de `lista-de-arte.csv`; não edite à mão. Cada bloco traz o nome do arquivo e o prompt pronto para colar no gerador.', '',
     '## Como mandar', '',
     '- **Itens e decoração:** render 3D brilhante, fundo branco liso, quadrado. Os prompts já pedem pose compacta (itens compridos, como peixe e milho, ficam pequenos nas casas) e nenhum texto.',
     '- **Personagens:** ilustração pintada, busto, fundo liso claro.',
     '- Mande em lotes (uma linha de 8 itens é um bom tamanho) e diga o código de cada imagem quando não for óbvio, por exemplo "te-3 cebola".',
     '- O recorte, a troca no jogo e a atualização desta lista são feitos depois, com `itens/recortar_itens.py` e este script.', '',
     '| Grupo | Prontas | Faltam |', '|---|---|---|']
for t in ('mercado', 'item', 'item-rota', 'personagem', 'decoracao'):
    ok, tot, _ = grupos[t]; f.append(f'| {nomes_pl[t]} | {ok} de {tot} | {tot - ok} |')
ref = [r for r in rows if r['arquivo'] in REFAZER]
if ref:
    f += ['', '## Refazer (já está no jogo, mas vale gerar de novo)', '']
    for r in ref:
        f += [f'### `{r["arquivo"]}` · {r["nome_pt"]}', '', f'Motivo: {REFAZER[r["arquivo"]]}.', '', '```', r['prompt_en'], '```', '']
for t in ('item', 'item-rota', 'decoracao', 'personagem'):
    falta = grupos[t][2]
    if not falta: continue
    f += ['', f'## {nomes_pl[t]} ({len(falta)})', '']
    grupo_atual = None
    for r in falta:
        g = r['descricao_pt'].split(',')[0] if t in ('item', 'item-rota') else None
        if g and g != grupo_atual:
            grupo_atual = g; f += [f'### {g}', '']
        cod = os.path.splitext(os.path.basename(r['arquivo']))[0]
        titulo = f'**{cod}** · {r["nome_pt"]}' + (f' ({r["nome_en"]})' if r['nome_en'] != r['nome_pt'] else '')
        if t in ('item', 'item-rota'): titulo += ' · ' + r['descricao_pt'].split(', ')[-1]
        f += [titulo, '', '```', r['prompt_en'], '```', '']
open(FALTA, 'w', encoding='utf-8').write('\n'.join(f).rstrip() + '\n')
print('falta-gerar.md:', sum(len(grupos[t][2]) for t in grupos), 'imagens a gerar,', len(ref), 'a refazer')
