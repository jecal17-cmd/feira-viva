"""Gera os prompts do Nano Banana 2 Lite para a identidade visual própria do Ler Brincando.

Uso:  python gerar_prompts.py CAMINHO/DO/LerBrincando/data.json
Saída (nesta pasta):
  prompt-nano-banana-ler-brincando.md  os prompts, grade por grade, com a tabela de cada casa
  grades.json                           lote -> lista de destinos, na ordem das casas (esquerda->direita, cima->baixo)
Rode de novo sempre que entrarem palavras novas no jogo: as grades de palavras são refeitas na ordem de ensino.
"""
import json, os, sys, unicodedata as U

AQUI = os.path.dirname(os.path.abspath(__file__))
D = json.load(open(sys.argv[1], encoding='utf-8'))

ESTILO = ("Style for every object: glossy stylized 3D render matching the attached owl mascot image (Lili): the same soft, "
          "chunky rounded shapes, smooth glossy material with gentle highlights and a soft warm glow, warm golden and creamy "
          "tones mixed with bright friendly colors (sky blue, leaf green, coral red, sunny yellow), soft studio lighting. "
          "Cute and friendly for children aged 5 to 7: simple bold silhouettes that are easy to recognize even when tiny, "
          "big rounded forms, no small clutter, no scary details. Each object compact and fully inside its cell, centered, "
          "no shadows on the ground. Plain pure white background everywhere. Absolutely no text, no letters, no numbers, "
          "no labels, no watermark, no borders, no grid lines.")
REF = ("Use the attached image of the golden owl Lili only as the style reference (material, lighting, colors, level of detail). "
       "Do not draw the owl unless a cell asks for her.")

def grade(n, cols, rows, itens, extra='', ref=REF):
    tam = '2048 x 2048 pixels, square 1:1'
    linhas = [f"A sprite sheet of {n} separate game icons arranged in a strict grid of {cols} columns by {rows} rows, "
              f"read left to right, top to bottom. Every cell is the same size, with generous empty space between cells, "
              f"and contains exactly one subject, centered. {tam}. {ref}{extra}", '']
    for k, desc in enumerate(itens):
        linhas.append(f"{k+1}. Row {k//cols+1}, column {k%cols+1}: {desc}")
    linhas += ['', ESTILO]
    return '\n'.join(linhas)

# ---------- descrições das palavras ----------
# Nome Unicode do emoji (inglês) serve na maioria; aqui o que precisa de ajuste para a palavra em português.
FIX = {
 'MAMÃE': 'a smiling mother hugging her small child', 'PAPAI': 'a smiling father', 'TIA': 'a smiling young aunt waving',
 'VOVÓ': 'a sweet grandmother with white hair in a bun and glasses', 'VOVÔ': 'a kind grandfather with white hair and glasses',
 'MENINA': 'a smiling little girl', 'MENINO': 'a smiling little boy', 'BEBÊ': 'a happy baby in a diaper',
 'FILA': 'three children standing one behind the other in a line', 'VILA': 'a small village of three colorful houses',
 'NEVE': 'a snowy mound with snowflakes falling', 'LUA': 'a smiling crescent moon', 'DIA': 'a bright sunny sky with the sun and one small cloud',
 'SOL': 'a bright round smiling sun with rays', 'MAR': 'a big blue sea wave', 'RIO': 'a winding blue river between green banks',
 'BAÚ': 'a wooden treasure chest with golden trim, lid slightly open', 'COLA': 'a white bottle of school glue with an orange cap',
 'GOLA': 'a shirt collar', 'ÁGUA': 'a clear glass of water', 'SETA': 'a big curved arrow pointing right', 'VOTO': 'a ballot box with a paper being dropped in',
 'QUEIXO': 'a cartoon face seen from the side with a finger pointing to the chin', 'RAINHA': 'a queen with a crown and a long dress',
 'REI': 'a king with a crown and a red cape', 'BRUXA': 'a friendly cartoon witch with a pointed hat and a broom',
 'ROÇA': 'a small farm field with a little barn and rows of crops', 'CAÇA': 'a bow and arrow', 'CALO': 'a foot with an adhesive bandage on the toe',
 'CHATO': 'a bored cartoon face with half-closed eyes', 'PATA': 'a female duck', 'PAU': 'a wooden stick', 'BOTÃO': 'a round sewing button with four holes',
 'CABELO': 'a cartoon head with big curly hair', 'BONECA': 'a rag doll with braids and a dress', 'PENTE': 'a hair comb',
 'GARFO': 'a fork', 'PRATO': 'an empty round plate', 'FACA': 'a kitchen knife with a rounded tip', 'DEDO': 'a hand with the index finger pointing up',
 'JOGO': 'a board game with colored pieces', 'PICO': 'a pointed snowy mountain peak', 'OCA': 'a Brazilian indigenous oca: a round thatched straw hut',
 'PANELA': 'a cooking pot with a lid', 'SOFÁ': 'a comfy sofa', 'LOJA': 'a small shop with a striped awning', 'LUPA': 'a magnifying glass',
 'MAPA': 'a folded treasure map', 'PIANO': 'a piano', 'PÉ': 'a bare foot', 'BOTA': 'a rain boot', 'BOTE': 'a small rowing boat',
 'FOTO': 'a printed photo of a landscape', 'JATO': 'a jet airplane', 'NOTA': 'a single musical note', 'SAPATO': 'a shoe',
 'TELEFONE': 'an old telephone with a curly cord', 'COPO': 'a drinking glass', 'SUCO': 'a glass of orange juice with a straw',
 'PETECA': 'a peteca: a Brazilian hand shuttlecock with colorful feathers', 'GADO': 'a group of two cattle', 'GATO': 'a cat',
 'MÚSICA': 'musical notes floating', 'VASO': 'a flower vase with flowers', 'TESOURA': 'a pair of children safety scissors',
 'ESPADA': 'a toy sword', 'MÁSCARA': 'a carnival mask', 'TÊNIS': 'a sneaker', 'CARTA': 'a letter in an envelope with a heart seal',
 'CORDA': 'a coiled rope', 'GOL': 'a soccer goal with a ball in the net', 'PAPEL': 'a sheet of paper', 'SAL': 'a salt shaker',
 'ANJO': 'a little angel with wings and a halo', 'BANDEIRA': 'a little flag on a pole', 'LARANJA': 'an orange', 'LÍNGUA': 'a cartoon face sticking out the tongue',
 'NINJA': 'a cute cartoon ninja', 'POMBO': 'a gray pigeon', 'PONTE': 'a bridge over water', 'SEMENTE': 'a seed sprouting a tiny plant',
 'VAMPIRO': 'a friendly cartoon vampire', 'ZUMBI': 'a silly friendly cartoon zombie, not scary', 'MÃO': 'an open hand',
 'FLOR': 'a colorful flower', 'GLOBO': 'a world globe on a stand', 'PRAIA': 'a beach with a sun umbrella', 'PRESENTE': 'a wrapped gift box with a bow',
 'TECLADO': 'a computer keyboard', 'CHAPÉU': 'a hat', 'CHÁ': 'a cup of tea', 'MOCHILA': 'a school backpack', 'BOLHA': 'soap bubbles',
 'GARRAFA': 'a bottle', 'RAIO': 'a lightning bolt from a cloud', 'RODA': 'a wheel', 'TERRA': 'the planet Earth', 'BRAÇO': 'a strong flexed arm',
 'CALÇA': 'a pair of trousers', 'CORAÇÃO': 'a red heart', 'DINOSSAURO': 'a friendly long-necked dinosaur', 'LAÇO': 'a ribbon bow',
 'ONÇA': 'a jaguar (onça-pintada) with spots', 'PALHAÇO': 'a clown with a red nose', 'QUADRO': 'a picture frame with a painting',
 'GÊNIO': 'a friendly genie coming out of a lamp', 'RELÓGIO': 'an alarm clock', 'ESQUILO': 'a squirrel', 'GALINHA': 'a hen',
 'COELHO': 'a rabbit', 'ILHA': 'a small island with a palm tree', 'OLHO': 'a big cartoon eye', 'ORELHA': 'an ear', 'FOLHA': 'a green leaf',
 'MEDALHA': 'a gold medal with a ribbon', 'CACHORRO': 'a dog', 'RATO': 'a mouse', 'RAPOSA': 'a fox', 'ROBÔ': 'a friendly robot',
 'CESTA': 'a basket', 'CIRCO': 'a circus tent', 'MORCEGO': 'a cute bat', 'ESCUDO': 'a shield', 'FÁBRICA': 'a factory with a chimney',
 'TREM': 'a train', 'METRÔ': 'a subway train', 'PEDRA': 'a rock', 'LIXO': 'a trash can', 'POTE': 'a jar with a lid',
 'UVA': 'a bunch of purple grapes', 'MEIA': 'a pair of striped socks', 'LUVA': 'a pair of gloves', 'MALA': 'a suitcase',
 'BALA': 'a wrapped candy', 'SOPA': 'a bowl of soup', 'CAFÉ': 'a cup of coffee', 'CAIXA': 'a cardboard box', 'PIPOCA': 'a bag of popcorn',
 'SEREIA': 'a mermaid', 'CASTELO': 'a castle', 'ÓCULOS': 'a pair of glasses', 'UNICÓRNIO': 'a unicorn', 'AMENDOIM': 'a few peanuts in the shell',
 'FEIJÃO': 'a bowl of beans', 'PUDIM': 'a caramel flan pudding', 'ESTRELA': 'a star', 'ALHO': 'a garlic bulb', 'ARROZ': 'a bowl of white rice',
 'MACARRÃO': 'a plate of spaghetti', 'BALANÇA': 'a balance scale', 'CEREJA': 'two cherries', 'PANQUECA': 'a stack of pancakes',
 'ÁRVORE': 'a tree', 'LANTERNA': 'a flashlight', 'CARNE': 'a piece of meat', 'BONÉ': 'a baseball cap', 'MILHO': 'an ear of corn',
 'JOANINHA': 'a ladybug', 'CARRO': 'a car', 'COMPUTADOR': 'a computer', 'BICO': 'a little bird showing its beak',
 'MOTO': 'a motorcycle', 'CANETA': 'a pen', 'GOTA': 'a water drop', 'CHUVA': 'a cloud with rain', 'BULE': 'a teapot',
}
ANIMAL_FACE = (' face',)

def desc_palavra(p):
    if p['p'] in FIX: return FIX[p['p']]
    nomes = [U.name(c).lower() for c in p['e'] if ord(c) not in (0xFE0F, 0x200D) and not 0x1F3FB <= ord(c) <= 0x1F3FF]
    n = ' and '.join(nomes)
    for a, b in (('black ', ''), ('white ', ''), ('heavy ', ''), ('left-pointing ', ''), ('lower left ', ''), ('mans ', ''), ('womans ', '')):
        n = n.replace(a, b)
    if n.endswith(' face') and n not in ('clown face', 'robot face'): n = n[:-5]
    return ('an ' if n[0] in 'aeiou' else 'a ') + n

# ---------- lotes fixos ----------
LOTES = []   # (chave, título, cols, rows, [(destino, rótulo pt, descrição en)], extra[, referência])

LILI = 'Lili'
REF_LILI = ("The attached image shows Lili, the owl mascot of the game. Draw her in every cell, full body, keeping her design exactly: "
            "golden glossy body, pointed ear tufts, big round eyes with brown irises, small diamond-shaped beak, cream belly with "
            "scale-like feathers, small side wings, no eggshell, no picture frame. Same character, proportions and colors in all 9 cells; "
            "only her pose and expression change.")
LOTES.append(('lili', 'Lili: expressões e poses', 3, 3, [
 ('lili/oi', 'Acenando (boas-vindas)', f'{LILI}, waving hello with one wing, big smile'),
 ('lili/fala', 'Falando (instruções)', f'{LILI}, beak open as if talking, one wing raised explaining'),
 ('lili/feliz', 'Feliz (olhos fechados)', f'{LILI}, eyes closed in happy upside-down crescents, cheerful smile'),
 ('lili/festa', 'Comemorando (acerto)', f'{LILI}, jumping with both wings up, sparkles around her'),
 ('lili/dica', 'Pensando (dica)', f'{LILI}, wing on her chin, thinking, a small glowing light bulb above her head'),
 ('lili/calma', 'Encorajando (errou)', f'{LILI}, gentle kind smile, head tilted, one wing on her chest, calm and reassuring'),
 ('lili/aponta', 'Apontando para o lado', f'{LILI}, pointing to the right with one wing, curious look'),
 ('lili/le', 'Lendo um livro', f'{LILI}, sitting and reading an open book held in her wings'),
 ('lili/dorme', 'Dormindo (pausa)', f'{LILI}, sleeping peacefully with eyes closed, sitting curled up, a tiny night cap'),
], '', REF_LILI))

AV = [('raposa', 'a fox'), ('panda', 'a panda'), ('tigre', 'a tiger'), ('sapo', 'a frog'), ('unicornio', 'a unicorn'), ('polvo', 'an octopus'),
      ('macaco', 'a monkey'), ('coelho', 'a rabbit'), ('urso', 'a bear'), ('coala', 'a koala'), ('leao', 'a lion'), ('pinguim', 'a penguin')]
LOTES.append(('avatares', 'Avatares de perfil (mesma ordem de `avatares` no data.json)', 4, 3,
 [(f'avatares/{a}', a, f'the head and shoulders of {d}, front view, big friendly eyes, happy smile') for a, d in AV],
 ' All 12 portraits have the same size, framing and cute style, like a matching set of profile pictures.'))

MUNDO_EN = {1: 'a small round tropical island with sand, a palm tree, a seashell and a crab, surrounded by blue water',
            2: 'a round flowery green valley with daisies, tulips, sunflowers, a butterfly and a bee',
            3: 'a round piece of whispering forest with tall trees, red mushrooms and a squirrel',
            4: 'a round snowy mountain with two twin peaks, a mountain goat and an eagle',
            5: 'a round river landscape with a little steam train crossing a bridge and a canoe on the water',
            6: 'a round crystal cave with glowing purple and blue crystals and a cute bat',
            7: 'a round fairy-tale castle on a hill with flags, a shield and a friendly little dragon',
            8: 'a round enchanted library with stacked books, a glowing open book and a candle'}
LOTES.append(('mundos', 'Emblemas dos 8 mundos (abas e cartões do mapa)', 3, 3,
 [(f"mundos/{m['id']}", m['nome'], f"{MUNDO_EN[m['id']]}, as a small floating 3D diorama badge, main colors {m['cor1']} and {m['cor2']}")
  for m in D['mundos']] + [('mapa/presente', 'Presente do mapa (🎁)', 'a gift box with a golden bow, glowing softly')],
 ' The 8 world badges are a matching set: same size, same round floating-island shape, each with its own colors.'))

ENF = {'casca': 'the bottom half of a cracked white eggshell with a zigzag edge', 'broto': 'a tiny green sprout with two leaves',
       'flor': 'a small pink flower to wear on the head', 'chapeuExplorador': 'a khaki explorer safari hat',
       'mochila': 'a small adventure backpack', 'lupa': 'a golden magnifying glass', 'capelo': 'a graduation cap with a golden tassel',
       'capa': 'a red superhero cape'}
LOJA_EN = {'laco': 'a red ribbon bow for the head', 'oculos': 'round cute glasses', 'cachecol': 'a striped knitted scarf',
           'chapeu': 'a black top hat with a ribbon', 'coroa': 'a small golden crown with gems',
           'mapaPorDoSol': 'a round sunset scene over the sea, orange and pink sky', 'mapaOceano': 'a round deep blue ocean scene with a wave',
           'mapaDoce': 'a round candy land scene with lollipops and pastel colors'}
loja = []
for x in D['loja']:
    if x['tipo'] == 'cor': continue
    chave = {'🌅': 'mapaPorDoSol', '🌊': 'mapaOceano', '🍭': 'mapaDoce'}.get(x['emoji'], x['id'])
    loja.append((f'loja/{chave}', x['nome'], LOJA_EN[chave]))
LOTES.append(('enfeites', 'Enfeites de nível e Lojinha', 4, 4,
 [(f"enfeites/{n['enfeite']}", f"{n['nome']} ({n['enfeite']})", ENF[n['enfeite']]) for n in D['niveis']] + loja,
 ' The first 13 cells are accessories that will be placed on the owl later, so draw them alone, without any character.'))

MED_EN = {'ouvidoOuro': 'a golden ear', 'contador': 'a stack of colorful books', 'persistente': 'a strong flexed arm',
          'escritor': 'a magic pencil leaving a sparkle trail', 'leitor': 'a pair of big curious eyes', 'estrelas': 'a shower of stars',
          'colecionador': 'a sticker album', 'voz': 'a microphone', 'tracos': 'a magic wand with sparkles', 'mundo1': 'a tiny island with a palm tree',
          'mundo4': 'a snowy mountain with a little flag on top', 'superLeitor': 'a red cape and an open book'}
med = []
for x in D['medalhas']:
    en = MED_EN.get(x['id']) or f"the symbol {x['emoji']}"
    med.append((f"medalhas/{x['id']}", x['nome'], f'a round gold medal with a ribbon, with {en} in relief in the center'))
LOTES.append(('medalhas', 'Medalhas', 4, 3, med, ' All 12 medals share the same round shape and ribbon; only the center symbol changes.'))

LOTES.append(('interface', 'Ícones da interface', 4, 4, [
 ('ui/som', 'Ouvir (🔊)', 'a speaker with sound waves'), ('ui/devagar', 'Devagar (🐢)', 'a cute green turtle'),
 ('ui/cadeado', 'Fase trancada (🔒)', 'a golden padlock'), ('ui/estrela', 'Estrela', 'a shiny golden star'),
 ('ui/moeda', 'Moeda', 'a shiny gold coin with a star embossed'), ('ui/presente', 'Presente (🎁)', 'a gift box with a ribbon'),
 ('ui/ajuda', 'Ajuda (🛟)', 'a red and white lifebuoy ring'), ('ui/adiantar', 'Adiantar fala (⏩)', 'a fast-forward symbol made of two rounded triangles'),
 ('ui/tambor', 'Tambor (palmas)', 'a toy drum with two drumsticks'), ('ui/pronto', 'Pronto (✔)', 'a big green check mark'),
 ('ui/microfone', 'Microfone', 'a microphone'), ('ui/mapa', 'Mapa (🗺️)', 'a folded paper map with a dotted path'),
 ('ui/livro', 'História (📖)', 'an open storybook'), ('ui/trofeu', 'Troféu', 'a golden trophy cup'),
 ('ui/lampada', 'Dica (💡)', 'a glowing light bulb'), ('ui/casa', 'Início', 'a small cozy house')], ''))

# ---------- palavras, na ordem de ensino ----------
pals = sorted(D['palavras'], key=lambda p: (p['faseMin'], p['p']))
for i in range(0, len(pals), 16):
    bloco = pals[i:i+16]; n = i // 16 + 1
    mundos = sorted({p['mundo'] for p in bloco})
    LOTES.append((f'palavras-{n}', f"Palavras {n} (mundo{'s' if len(mundos) > 1 else ''} {', '.join(map(str, mundos))})", 4, 4,
                  [(f"imagens/{p['om']}", p['p'], desc_palavra(p)) for p in bloco],
                  ' Every picture illustrates a simple word for a child learning to read, so show the thing itself in the clearest way.'))

# ---------- saída ----------
md = ['# Prompt para o Nano Banana 2 Lite · identidade visual própria do Ler Brincando', '',
 'Troca as figuras do OpenMoji por arte própria, no estilo da Lili do ícone (dourada, brilhante, formas redondas). '
 'Gerado por `gerar_prompts.py` a partir do `data.json` do Ler Brincando (versão ' + D['versao'] + ').', '',
 '## Como usar', '',
 '- **Anexe sempre a imagem de referência** `referencia-lili.png` (a arte do ícone) junto com o prompt. Ela fixa o material, a luz e as cores.',
 '- Peça **2048 × 2048** e **baixe/envie como arquivo** (documento), não como foto, para o app não comprimir.',
 '- Um prompt por vez; cada um gera **uma imagem com várias figuras** em grade. A ordem das casas é a da tabela abaixo de cada prompt.',
 '- Se uma casa vier errada, gere de novo só aquela grade ou me diga qual casa ignorar (fica vazia no `grades.json`).',
 f'- São **{len(LOTES)} grades**: 6 de identidade (Lili, avatares, mundos, enfeites e loja, medalhas, interface) e '
 f'{len(LOTES)-6} de palavras ({len(pals)} palavras, na ordem em que o jogo ensina).',
 '- **Ordem sugerida:** Lili → avatares → interface → mundos → palavras 1 a 3 (mundos 1 a 3, os grátis e os primeiros que a criança vê) → o resto.', '',
 '---', '']
mapa = {}
for chave, titulo, cols, rows, itens, extra, *ref in LOTES:
    mapa[chave] = [d for d, _, _ in itens]
    md += [f'## {titulo} · lote `{chave}` ({cols} × {rows})', '', '```', grade(len(itens), cols, rows, [e for _, _, e in itens], extra, *ref), '```', '',
           '| Casa | Destino | Figura |', '|---|---|---|']
    md += [f'| linha {k//cols+1}, col. {k%cols+1} | `{d}` | {r} |' for k, (d, r, _) in enumerate(itens)]
    md += ['']
md += ['---', '', '## Depois de gerar', '',
 'Mande as imagens dizendo o lote de cada uma. Eu fatio com o `fatiar_grade.py` (mesmo processo da Quitanda), tiro o fundo, '
 'gero os WebP e troco no Ler Brincando: as palavras substituem `imagens/<código>.svg` (o jogo passa a carregar o WebP próprio e '
 'mantém o OpenMoji como reserva), e a Lili, os avatares, os mundos, a lojinha, as medalhas e os ícones entram nas telas. '
 'Os créditos do OpenMoji saem da tela Sobre quando todas as figuras forem próprias.', '']
open(os.path.join(AQUI, 'prompt-nano-banana-ler-brincando.md'), 'w', encoding='utf-8').write('\n'.join(md))
json.dump(mapa, open(os.path.join(AQUI, 'grades.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(LOTES), 'grades;', sum(len(v) for v in mapa.values()), 'figuras')
