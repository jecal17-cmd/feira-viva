# Prompt para o Nano Banana 2 Lite · identidade visual própria do Ler Brincando

Troca as figuras do OpenMoji por arte própria, no estilo da Lili do ícone (dourada, brilhante, formas redondas). Gerado por `gerar_prompts.py` a partir do `data.json` do Ler Brincando (versão 1.4.1).

## Como usar

- **Anexe sempre a imagem de referência** `referencia-lili.png` (a arte do ícone) junto com o prompt. Ela fixa o material, a luz e as cores.
- Peça **2048 × 2048** e **baixe/envie como arquivo** (documento), não como foto, para o app não comprimir.
- Um prompt por vez; cada um gera **uma imagem com várias figuras** em grade. A ordem das casas é a da tabela abaixo de cada prompt.
- Se uma casa vier errada, gere de novo só aquela grade ou me diga qual casa ignorar (fica vazia no `grades.json`).
- São **29 grades**: 6 de identidade (Lili, avatares, mundos, enfeites e loja, medalhas, interface) e 23 de palavras (363 palavras, na ordem em que o jogo ensina).
- **Ordem sugerida:** Lili → avatares → interface → mundos → palavras 1 a 3 (mundos 1 a 3, os grátis e os primeiros que a criança vê) → o resto.

---

## Lili: expressões e poses · lote `lili` (3 × 3)

```
A sprite sheet of 9 separate game icons arranged in a strict grid of 3 columns by 3 rows, read left to right, top to bottom. Every cell is the same size, with generous empty space between cells, and contains exactly one subject, centered. 2048 x 2048 pixels, square 1:1. The attached image shows Lili, the owl mascot of the game. Draw her in every cell, full body, keeping her design exactly: golden glossy body, pointed ear tufts, big round eyes with brown irises, small diamond-shaped beak, cream belly with scale-like feathers, small side wings, no eggshell, no picture frame. Same character, proportions and colors in all 9 cells; only her pose and expression change.

1. Row 1, column 1: Lili, waving hello with one wing, big smile
2. Row 1, column 2: Lili, beak open as if talking, one wing raised explaining
3. Row 1, column 3: Lili, eyes closed in happy upside-down crescents, cheerful smile
4. Row 2, column 1: Lili, jumping with both wings up, sparkles around her
5. Row 2, column 2: Lili, wing on her chin, thinking, a small glowing light bulb above her head
6. Row 2, column 3: Lili, gentle kind smile, head tilted, one wing on her chest, calm and reassuring
7. Row 3, column 1: Lili, pointing to the right with one wing, curious look
8. Row 3, column 2: Lili, sitting and reading an open book held in her wings
9. Row 3, column 3: Lili, sleeping peacefully with eyes closed, sitting curled up, a tiny night cap

Style for every object: glossy stylized 3D render matching the attached owl mascot image (Lili): the same soft, chunky rounded shapes, smooth glossy material with gentle highlights and a soft warm glow, warm golden and creamy tones mixed with bright friendly colors (sky blue, leaf green, coral red, sunny yellow), soft studio lighting. Cute and friendly for children aged 5 to 7: simple bold silhouettes that are easy to recognize even when tiny, big rounded forms, no small clutter, no scary details. Each object compact and fully inside its cell, centered, no shadows on the ground. Plain pure white background everywhere. Absolutely no text, no letters, no numbers, no labels, no watermark, no borders, no grid lines.
```

| Casa | Destino | Figura |
|---|---|---|
| linha 1, col. 1 | `lili/oi` | Acenando (boas-vindas) |
| linha 1, col. 2 | `lili/fala` | Falando (instruções) |
| linha 1, col. 3 | `lili/feliz` | Feliz (olhos fechados) |
| linha 2, col. 1 | `lili/festa` | Comemorando (acerto) |
| linha 2, col. 2 | `lili/dica` | Pensando (dica) |
| linha 2, col. 3 | `lili/calma` | Encorajando (errou) |
| linha 3, col. 1 | `lili/aponta` | Apontando para o lado |
| linha 3, col. 2 | `lili/le` | Lendo um livro |
| linha 3, col. 3 | `lili/dorme` | Dormindo (pausa) |

## Avatares de perfil (mesma ordem de `avatares` no data.json) · lote `avatares` (4 × 3)

```
A sprite sheet of 12 separate game icons arranged in a strict grid of 4 columns by 3 rows, read left to right, top to bottom. Every cell is the same size, with generous empty space between cells, and contains exactly one subject, centered. 2048 x 2048 pixels, square 1:1. Use the attached image of the golden owl Lili only as the style reference (material, lighting, colors, level of detail). Do not draw the owl unless a cell asks for her. All 12 portraits have the same size, framing and cute style, like a matching set of profile pictures.

1. Row 1, column 1: the head and shoulders of a fox, front view, big friendly eyes, happy smile
2. Row 1, column 2: the head and shoulders of a panda, front view, big friendly eyes, happy smile
3. Row 1, column 3: the head and shoulders of a tiger, front view, big friendly eyes, happy smile
4. Row 1, column 4: the head and shoulders of a frog, front view, big friendly eyes, happy smile
5. Row 2, column 1: the head and shoulders of a unicorn, front view, big friendly eyes, happy smile
6. Row 2, column 2: the head and shoulders of an octopus, front view, big friendly eyes, happy smile
7. Row 2, column 3: the head and shoulders of a monkey, front view, big friendly eyes, happy smile
8. Row 2, column 4: the head and shoulders of a rabbit, front view, big friendly eyes, happy smile
9. Row 3, column 1: the head and shoulders of a bear, front view, big friendly eyes, happy smile
10. Row 3, column 2: the head and shoulders of a koala, front view, big friendly eyes, happy smile
11. Row 3, column 3: the head and shoulders of a lion, front view, big friendly eyes, happy smile
12. Row 3, column 4: the head and shoulders of a penguin, front view, big friendly eyes, happy smile

Style for every object: glossy stylized 3D render matching the attached owl mascot image (Lili): the same soft, chunky rounded shapes, smooth glossy material with gentle highlights and a soft warm glow, warm golden and creamy tones mixed with bright friendly colors (sky blue, leaf green, coral red, sunny yellow), soft studio lighting. Cute and friendly for children aged 5 to 7: simple bold silhouettes that are easy to recognize even when tiny, big rounded forms, no small clutter, no scary details. Each object compact and fully inside its cell, centered, no shadows on the ground. Plain pure white background everywhere. Absolutely no text, no letters, no numbers, no labels, no watermark, no borders, no grid lines.
```

| Casa | Destino | Figura |
|---|---|---|
| linha 1, col. 1 | `avatares/raposa` | raposa |
| linha 1, col. 2 | `avatares/panda` | panda |
| linha 1, col. 3 | `avatares/tigre` | tigre |
| linha 1, col. 4 | `avatares/sapo` | sapo |
| linha 2, col. 1 | `avatares/unicornio` | unicornio |
| linha 2, col. 2 | `avatares/polvo` | polvo |
| linha 2, col. 3 | `avatares/macaco` | macaco |
| linha 2, col. 4 | `avatares/coelho` | coelho |
| linha 3, col. 1 | `avatares/urso` | urso |
| linha 3, col. 2 | `avatares/coala` | coala |
| linha 3, col. 3 | `avatares/leao` | leao |
| linha 3, col. 4 | `avatares/pinguim` | pinguim |

## Emblemas dos 8 mundos (abas e cartões do mapa) · lote `mundos` (3 × 3)

```
A sprite sheet of 9 separate game icons arranged in a strict grid of 3 columns by 3 rows, read left to right, top to bottom. Every cell is the same size, with generous empty space between cells, and contains exactly one subject, centered. 2048 x 2048 pixels, square 1:1. Use the attached image of the golden owl Lili only as the style reference (material, lighting, colors, level of detail). Do not draw the owl unless a cell asks for her. The 8 world badges are a matching set: same size, same round floating-island shape, each with its own colors.

1. Row 1, column 1: a small round tropical island with sand, a palm tree, a seashell and a crab, surrounded by blue water, as a small floating 3D diorama badge, main colors #7fd6f5 and #ffe8a3
2. Row 1, column 2: a round flowery green valley with daisies, tulips, sunflowers, a butterfly and a bee, as a small floating 3D diorama badge, main colors #b8f0a8 and #fff5c2
3. Row 1, column 3: a round piece of whispering forest with tall trees, red mushrooms and a squirrel, as a small floating 3D diorama badge, main colors #7cc489 and #d8f3c9
4. Row 2, column 1: a round snowy mountain with two twin peaks, a mountain goat and an eagle, as a small floating 3D diorama badge, main colors #a9b8e8 and #eef1ff
5. Row 2, column 2: a round river landscape with a little steam train crossing a bridge and a canoe on the water, as a small floating 3D diorama badge, main colors #79c7e8 and #d6f6ff
6. Row 2, column 3: a round crystal cave with glowing purple and blue crystals and a cute bat, as a small floating 3D diorama badge, main colors #b49be0 and #efe6ff
7. Row 3, column 1: a round fairy-tale castle on a hill with flags, a shield and a friendly little dragon, as a small floating 3D diorama badge, main colors #f2a7a7 and #fff0e6
8. Row 3, column 2: a round enchanted library with stacked books, a glowing open book and a candle, as a small floating 3D diorama badge, main colors #e8c07a and #fff6e0
9. Row 3, column 3: a gift box with a golden bow, glowing softly

Style for every object: glossy stylized 3D render matching the attached owl mascot image (Lili): the same soft, chunky rounded shapes, smooth glossy material with gentle highlights and a soft warm glow, warm golden and creamy tones mixed with bright friendly colors (sky blue, leaf green, coral red, sunny yellow), soft studio lighting. Cute and friendly for children aged 5 to 7: simple bold silhouettes that are easy to recognize even when tiny, big rounded forms, no small clutter, no scary details. Each object compact and fully inside its cell, centered, no shadows on the ground. Plain pure white background everywhere. Absolutely no text, no letters, no numbers, no labels, no watermark, no borders, no grid lines.
```

| Casa | Destino | Figura |
|---|---|---|
| linha 1, col. 1 | `mundos/1` | Ilha dos Sons |
| linha 1, col. 2 | `mundos/2` | Vale das Vogais |
| linha 1, col. 3 | `mundos/3` | Floresta Sussurrante |
| linha 2, col. 1 | `mundos/4` | Montanha dos Gêmeos |
| linha 2, col. 2 | `mundos/5` | Rio das Palavras |
| linha 2, col. 3 | `mundos/6` | Caverna dos Cristais |
| linha 3, col. 1 | `mundos/7` | Castelo das Regras |
| linha 3, col. 2 | `mundos/8` | Biblioteca Encantada |
| linha 3, col. 3 | `mapa/presente` | Presente do mapa (🎁) |

## Enfeites de nível e Lojinha · lote `enfeites` (4 × 4)

```
A sprite sheet of 16 separate game icons arranged in a strict grid of 4 columns by 4 rows, read left to right, top to bottom. Every cell is the same size, with generous empty space between cells, and contains exactly one subject, centered. 2048 x 2048 pixels, square 1:1. Use the attached image of the golden owl Lili only as the style reference (material, lighting, colors, level of detail). Do not draw the owl unless a cell asks for her. The first 13 cells are accessories that will be placed on the owl later, so draw them alone, without any character.

1. Row 1, column 1: the bottom half of a cracked white eggshell with a zigzag edge
2. Row 1, column 2: a tiny green sprout with two leaves
3. Row 1, column 3: a small pink flower to wear on the head
4. Row 1, column 4: a khaki explorer safari hat
5. Row 2, column 1: a small adventure backpack
6. Row 2, column 2: a golden magnifying glass
7. Row 2, column 3: a graduation cap with a golden tassel
8. Row 2, column 4: a red superhero cape
9. Row 3, column 1: a red ribbon bow for the head
10. Row 3, column 2: round cute glasses
11. Row 3, column 3: a striped knitted scarf
12. Row 3, column 4: a black top hat with a ribbon
13. Row 4, column 1: a small golden crown with gems
14. Row 4, column 2: a round sunset scene over the sea, orange and pink sky
15. Row 4, column 3: a round deep blue ocean scene with a wave
16. Row 4, column 4: a round candy land scene with lollipops and pastel colors

Style for every object: glossy stylized 3D render matching the attached owl mascot image (Lili): the same soft, chunky rounded shapes, smooth glossy material with gentle highlights and a soft warm glow, warm golden and creamy tones mixed with bright friendly colors (sky blue, leaf green, coral red, sunny yellow), soft studio lighting. Cute and friendly for children aged 5 to 7: simple bold silhouettes that are easy to recognize even when tiny, big rounded forms, no small clutter, no scary details. Each object compact and fully inside its cell, centered, no shadows on the ground. Plain pure white background everywhere. Absolutely no text, no letters, no numbers, no labels, no watermark, no borders, no grid lines.
```

| Casa | Destino | Figura |
|---|---|---|
| linha 1, col. 1 | `enfeites/casca` | Semente (casca) |
| linha 1, col. 2 | `enfeites/broto` | Broto (broto) |
| linha 1, col. 3 | `enfeites/flor` | Florzinha (flor) |
| linha 1, col. 4 | `enfeites/chapeuExplorador` | Explorador(a) (chapeuExplorador) |
| linha 2, col. 1 | `enfeites/mochila` | Aventureiro(a) (mochila) |
| linha 2, col. 2 | `enfeites/lupa` | Detetive das Letras (lupa) |
| linha 2, col. 3 | `enfeites/capelo` | Mestre das Sílabas (capelo) |
| linha 2, col. 4 | `enfeites/capa` | Super Leitor(a) (capa) |
| linha 3, col. 1 | `loja/laco` | Laço |
| linha 3, col. 2 | `loja/oculos` | Óculos |
| linha 3, col. 3 | `loja/cachecol` | Cachecol |
| linha 3, col. 4 | `loja/chapeu` | Chapéu |
| linha 4, col. 1 | `loja/coroa` | Coroa |
| linha 4, col. 2 | `loja/mapaPorDoSol` | Mapa pôr do sol |
| linha 4, col. 3 | `loja/mapaOceano` | Mapa oceano |
| linha 4, col. 4 | `loja/mapaDoce` | Mapa doce |

## Medalhas · lote `medalhas` (4 × 3)

```
A sprite sheet of 12 separate game icons arranged in a strict grid of 4 columns by 3 rows, read left to right, top to bottom. Every cell is the same size, with generous empty space between cells, and contains exactly one subject, centered. 2048 x 2048 pixels, square 1:1. Use the attached image of the golden owl Lili only as the style reference (material, lighting, colors, level of detail). Do not draw the owl unless a cell asks for her. All 12 medals share the same round shape and ribbon; only the center symbol changes.

1. Row 1, column 1: a round gold medal with a ribbon, with a golden ear in relief in the center
2. Row 1, column 2: a round gold medal with a ribbon, with a stack of colorful books in relief in the center
3. Row 1, column 3: a round gold medal with a ribbon, with a strong flexed arm in relief in the center
4. Row 1, column 4: a round gold medal with a ribbon, with a magic pencil leaving a sparkle trail in relief in the center
5. Row 2, column 1: a round gold medal with a ribbon, with a pair of big curious eyes in relief in the center
6. Row 2, column 2: a round gold medal with a ribbon, with a shower of stars in relief in the center
7. Row 2, column 3: a round gold medal with a ribbon, with a sticker album in relief in the center
8. Row 2, column 4: a round gold medal with a ribbon, with a microphone in relief in the center
9. Row 3, column 1: a round gold medal with a ribbon, with a magic wand with sparkles in relief in the center
10. Row 3, column 2: a round gold medal with a ribbon, with a tiny island with a palm tree in relief in the center
11. Row 3, column 3: a round gold medal with a ribbon, with a snowy mountain with a little flag on top in relief in the center
12. Row 3, column 4: a round gold medal with a ribbon, with a red cape and an open book in relief in the center

Style for every object: glossy stylized 3D render matching the attached owl mascot image (Lili): the same soft, chunky rounded shapes, smooth glossy material with gentle highlights and a soft warm glow, warm golden and creamy tones mixed with bright friendly colors (sky blue, leaf green, coral red, sunny yellow), soft studio lighting. Cute and friendly for children aged 5 to 7: simple bold silhouettes that are easy to recognize even when tiny, big rounded forms, no small clutter, no scary details. Each object compact and fully inside its cell, centered, no shadows on the ground. Plain pure white background everywhere. Absolutely no text, no letters, no numbers, no labels, no watermark, no borders, no grid lines.
```

| Casa | Destino | Figura |
|---|---|---|
| linha 1, col. 1 | `medalhas/ouvidoOuro` | Ouvido de Ouro |
| linha 1, col. 2 | `medalhas/contador` | Contador de Histórias |
| linha 1, col. 3 | `medalhas/persistente` | Não Desisto! |
| linha 1, col. 4 | `medalhas/escritor` | Escritor Mágico |
| linha 2, col. 1 | `medalhas/leitor` | Olho de Leitor |
| linha 2, col. 2 | `medalhas/estrelas` | Chuva de Estrelas |
| linha 2, col. 3 | `medalhas/colecionador` | Colecionador |
| linha 2, col. 4 | `medalhas/voz` | Voz de Leitor |
| linha 3, col. 1 | `medalhas/tracos` | Mão Mágica |
| linha 3, col. 2 | `medalhas/mundo1` | Rei da Ilha |
| linha 3, col. 3 | `medalhas/mundo4` | Alpinista |
| linha 3, col. 4 | `medalhas/superLeitor` | Super Leitor |

## Ícones da interface · lote `interface` (4 × 4)

```
A sprite sheet of 16 separate game icons arranged in a strict grid of 4 columns by 4 rows, read left to right, top to bottom. Every cell is the same size, with generous empty space between cells, and contains exactly one subject, centered. 2048 x 2048 pixels, square 1:1. Use the attached image of the golden owl Lili only as the style reference (material, lighting, colors, level of detail). Do not draw the owl unless a cell asks for her.

1. Row 1, column 1: a speaker with sound waves
2. Row 1, column 2: a cute green turtle
3. Row 1, column 3: a golden padlock
4. Row 1, column 4: a shiny golden star
5. Row 2, column 1: a shiny gold coin with a star embossed
6. Row 2, column 2: a gift box with a ribbon
7. Row 2, column 3: a red and white lifebuoy ring
8. Row 2, column 4: a fast-forward symbol made of two rounded triangles
9. Row 3, column 1: a toy drum with two drumsticks
10. Row 3, column 2: a big green check mark
11. Row 3, column 3: a microphone
12. Row 3, column 4: a folded paper map with a dotted path
13. Row 4, column 1: an open storybook
14. Row 4, column 2: a golden trophy cup
15. Row 4, column 3: a glowing light bulb
16. Row 4, column 4: a small cozy house

Style for every object: glossy stylized 3D render matching the attached owl mascot image (Lili): the same soft, chunky rounded shapes, smooth glossy material with gentle highlights and a soft warm glow, warm golden and creamy tones mixed with bright friendly colors (sky blue, leaf green, coral red, sunny yellow), soft studio lighting. Cute and friendly for children aged 5 to 7: simple bold silhouettes that are easy to recognize even when tiny, big rounded forms, no small clutter, no scary details. Each object compact and fully inside its cell, centered, no shadows on the ground. Plain pure white background everywhere. Absolutely no text, no letters, no numbers, no labels, no watermark, no borders, no grid lines.
```

| Casa | Destino | Figura |
|---|---|---|
| linha 1, col. 1 | `ui/som` | Ouvir (🔊) |
| linha 1, col. 2 | `ui/devagar` | Devagar (🐢) |
| linha 1, col. 3 | `ui/cadeado` | Fase trancada (🔒) |
| linha 1, col. 4 | `ui/estrela` | Estrela |
| linha 2, col. 1 | `ui/moeda` | Moeda |
| linha 2, col. 2 | `ui/presente` | Presente (🎁) |
| linha 2, col. 3 | `ui/ajuda` | Ajuda (🛟) |
| linha 2, col. 4 | `ui/adiantar` | Adiantar fala (⏩) |
| linha 3, col. 1 | `ui/tambor` | Tambor (palmas) |
| linha 3, col. 2 | `ui/pronto` | Pronto (✔) |
| linha 3, col. 3 | `ui/microfone` | Microfone |
| linha 3, col. 4 | `ui/mapa` | Mapa (🗺️) |
| linha 4, col. 1 | `ui/livro` | História (📖) |
| linha 4, col. 2 | `ui/trofeu` | Troféu |
| linha 4, col. 3 | `ui/lampada` | Dica (💡) |
| linha 4, col. 4 | `ui/casa` | Início |

## Palavras 1 (mundos 2, 3) · lote `palavras-1` (4 × 4)

```
A sprite sheet of 16 separate game icons arranged in a strict grid of 4 columns by 4 rows, read left to right, top to bottom. Every cell is the same size, with generous empty space between cells, and contains exactly one subject, centered. 2048 x 2048 pixels, square 1:1. Use the attached image of the golden owl Lili only as the style reference (material, lighting, colors, level of detail). Do not draw the owl unless a cell asks for her. Every picture illustrates a simple word for a child learning to read, so show the thing itself in the clearest way.

1. Row 1, column 1: a yo-yo
2. Row 1, column 2: a bird
3. Row 1, column 3: an egg
4. Row 1, column 4: a bunch of purple grapes
5. Row 2, column 1: a sweet grandmother with white hair in a bun and glasses
6. Row 2, column 2: a kind grandfather with white hair and glasses
7. Row 2, column 3: a smiling mother hugging her small child
8. Row 2, column 4: a pair of striped socks
9. Row 3, column 1: a magnet
10. Row 3, column 2: a smiling little girl
11. Row 3, column 3: a smiling little boy
12. Row 3, column 4: a ship
13. Row 4, column 1: a snowy mound with snowflakes falling
14. Row 4, column 2: three children standing one behind the other in a line
15. Row 4, column 3: a smiling crescent moon
16. Row 4, column 4: a squid

Style for every object: glossy stylized 3D render matching the attached owl mascot image (Lili): the same soft, chunky rounded shapes, smooth glossy material with gentle highlights and a soft warm glow, warm golden and creamy tones mixed with bright friendly colors (sky blue, leaf green, coral red, sunny yellow), soft studio lighting. Cute and friendly for children aged 5 to 7: simple bold silhouettes that are easy to recognize even when tiny, big rounded forms, no small clutter, no scary details. Each object compact and fully inside its cell, centered, no shadows on the ground. Plain pure white background everywhere. Absolutely no text, no letters, no numbers, no labels, no watermark, no borders, no grid lines.
```

| Casa | Destino | Figura |
|---|---|---|
| linha 1, col. 1 | `imagens/1FA80` | IOIÔ |
| linha 1, col. 2 | `imagens/1F426` | AVE |
| linha 1, col. 3 | `imagens/1F95A` | OVO |
| linha 1, col. 4 | `imagens/1F347` | UVA |
| linha 2, col. 1 | `imagens/1F475` | VOVÓ |
| linha 2, col. 2 | `imagens/1F474` | VOVÔ |
| linha 2, col. 3 | `imagens/1F931` | MAMÃE |
| linha 2, col. 4 | `imagens/1F9E6` | MEIA |
| linha 3, col. 1 | `imagens/1F9F2` | ÍMÃ |
| linha 3, col. 2 | `imagens/1F467` | MENINA |
| linha 3, col. 3 | `imagens/1F466` | MENINO |
| linha 3, col. 4 | `imagens/1F6A2` | NAVIO |
| linha 4, col. 1 | `imagens/2744` | NEVE |
| linha 4, col. 2 | `imagens/1F9CD` | FILA |
| linha 4, col. 3 | `imagens/1F319` | LUA |
| linha 4, col. 4 | `imagens/1F991` | LULA |

## Palavras 2 (mundos 3, 4) · lote `palavras-2` (4 × 4)

```
A sprite sheet of 16 separate game icons arranged in a strict grid of 4 columns by 4 rows, read left to right, top to bottom. Every cell is the same size, with generous empty space between cells, and contains exactly one subject, centered. 2048 x 2048 pixels, square 1:1. Use the attached image of the golden owl Lili only as the style reference (material, lighting, colors, level of detail). Do not draw the owl unless a cell asks for her. Every picture illustrates a simple word for a child learning to read, so show the thing itself in the clearest way.

1. Row 1, column 1: a pair of gloves
2. Row 1, column 2: a suitcase
3. Row 1, column 3: a donkey
4. Row 1, column 4: a ball of yarn
5. Row 2, column 1: a candle
6. Row 2, column 2: a small village of three colorful houses
7. Row 2, column 3: a bell
8. Row 2, column 4: a comfy sofa
9. Row 3, column 1: a window
10. Row 3, column 2: a boar
11. Row 3, column 3: a trash can
12. Row 3, column 4: a small shop with a striped awning
13. Row 4, column 1: a magnifying glass
14. Row 4, column 2: a folded treasure map
15. Row 4, column 3: a cooking pot with a lid
16. Row 4, column 4: a smiling father

Style for every object: glossy stylized 3D render matching the attached owl mascot image (Lili): the same soft, chunky rounded shapes, smooth glossy material with gentle highlights and a soft warm glow, warm golden and creamy tones mixed with bright friendly colors (sky blue, leaf green, coral red, sunny yellow), soft studio lighting. Cute and friendly for children aged 5 to 7: simple bold silhouettes that are easy to recognize even when tiny, big rounded forms, no small clutter, no scary details. Each object compact and fully inside its cell, centered, no shadows on the ground. Plain pure white background everywhere. Absolutely no text, no letters, no numbers, no labels, no watermark, no borders, no grid lines.
```

| Casa | Destino | Figura |
|---|---|---|
| linha 1, col. 1 | `imagens/1F9E4` | LUVA |
| linha 1, col. 2 | `imagens/1F9F3` | MALA |
| linha 1, col. 3 | `imagens/1FACF` | MULA |
| linha 1, col. 4 | `imagens/1F9F6` | NOVELO |
| linha 2, col. 1 | `imagens/1F56F` | VELA |
| linha 2, col. 2 | `imagens/1F3D8` | VILA |
| linha 2, col. 3 | `imagens/1F514` | SINO |
| linha 2, col. 4 | `imagens/1F6CB` | SOFÁ |
| linha 3, col. 1 | `imagens/1FA9F` | JANELA |
| linha 3, col. 2 | `imagens/1F417` | JAVALI |
| linha 3, col. 3 | `imagens/1F5D1` | LIXO |
| linha 3, col. 4 | `imagens/1F3EC` | LOJA |
| linha 4, col. 1 | `imagens/1F50D` | LUPA |
| linha 4, col. 2 | `imagens/1F5FA` | MAPA |
| linha 4, col. 3 | `imagens/1F373` | PANELA |
| linha 4, col. 4 | `imagens/1F468` | PAPAI |

## Palavras 3 (mundo 4) · lote `palavras-3` (4 × 4)

```
A sprite sheet of 16 separate game icons arranged in a strict grid of 4 columns by 4 rows, read left to right, top to bottom. Every cell is the same size, with generous empty space between cells, and contains exactly one subject, centered. 2048 x 2048 pixels, square 1:1. Use the attached image of the golden owl Lili only as the style reference (material, lighting, colors, level of detail). Do not draw the owl unless a cell asks for her. Every picture illustrates a simple word for a child learning to read, so show the thing itself in the clearest way.

1. Row 1, column 1: a wooden stick
2. Row 1, column 2: a fish
3. Row 1, column 3: a feather
4. Row 1, column 4: a cucumber
5. Row 2, column 1: a piano
6. Row 2, column 2: a kite
7. Row 2, column 3: a bare foot
8. Row 2, column 4: a frog
9. Row 3, column 1: a bowl of soup
10. Row 3, column 2: a wrapped candy
11. Row 3, column 3: a whale
12. Row 3, column 4: a banana
13. Row 4, column 1: a wooden treasure chest with golden trim, lid slightly open
14. Row 4, column 2: a happy baby in a diaper
15. Row 4, column 3: an ox
16. Row 4, column 4: a soccer ball

Style for every object: glossy stylized 3D render matching the attached owl mascot image (Lili): the same soft, chunky rounded shapes, smooth glossy material with gentle highlights and a soft warm glow, warm golden and creamy tones mixed with bright friendly colors (sky blue, leaf green, coral red, sunny yellow), soft studio lighting. Cute and friendly for children aged 5 to 7: simple bold silhouettes that are easy to recognize even when tiny, big rounded forms, no small clutter, no scary details. Each object compact and fully inside its cell, centered, no shadows on the ground. Plain pure white background everywhere. Absolutely no text, no letters, no numbers, no labels, no watermark, no borders, no grid lines.
```

| Casa | Destino | Figura |
|---|---|---|
| linha 1, col. 1 | `imagens/1FAB5` | PAU |
| linha 1, col. 2 | `imagens/1F41F` | PEIXE |
| linha 1, col. 3 | `imagens/1FAB6` | PENA |
| linha 1, col. 4 | `imagens/1F952` | PEPINO |
| linha 2, col. 1 | `imagens/1F3B9` | PIANO |
| linha 2, col. 2 | `imagens/1FA81` | PIPA |
| linha 2, col. 3 | `imagens/1F9B6` | PÉ |
| linha 2, col. 4 | `imagens/1F438` | SAPO |
| linha 3, col. 1 | `imagens/1F372` | SOPA |
| linha 3, col. 2 | `imagens/1F36C` | BALA |
| linha 3, col. 3 | `imagens/1F40B` | BALEIA |
| linha 3, col. 4 | `imagens/1F34C` | BANANA |
| linha 4, col. 1 | `imagens/1F9F0` | BAÚ |
| linha 4, col. 2 | `imagens/1F476` | BEBÊ |
| linha 4, col. 3 | `imagens/1F402` | BOI |
| linha 4, col. 4 | `imagens/26BD` | BOLA |

## Palavras 4 (mundo 4) · lote `palavras-4` (4 × 4)

```
A sprite sheet of 16 separate game icons arranged in a strict grid of 4 columns by 4 rows, read left to right, top to bottom. Every cell is the same size, with generous empty space between cells, and contains exactly one subject, centered. 2048 x 2048 pixels, square 1:1. Use the attached image of the golden owl Lili only as the style reference (material, lighting, colors, level of detail). Do not draw the owl unless a cell asks for her. Every picture illustrates a simple word for a child learning to read, so show the thing itself in the clearest way.

1. Row 1, column 1: a birthday cake
2. Row 1, column 2: a baseball cap
3. Row 1, column 3: a teapot
4. Row 1, column 4: a wolf
5. Row 2, column 1: an olive
6. Row 2, column 2: a potato
7. Row 2, column 3: a rain boot
8. Row 2, column 4: a small rowing boat
9. Row 3, column 1: a printed photo of a landscape
10. Row 3, column 2: a jet airplane
11. Row 3, column 3: a glass of milk
12. Row 3, column 4: a mammoth
13. Row 4, column 1: a motorcycle
14. Row 4, column 2: a single musical note
15. Row 4, column 3: a female duck
16. Row 4, column 4: a scooter

Style for every object: glossy stylized 3D render matching the attached owl mascot image (Lili): the same soft, chunky rounded shapes, smooth glossy material with gentle highlights and a soft warm glow, warm golden and creamy tones mixed with bright friendly colors (sky blue, leaf green, coral red, sunny yellow), soft studio lighting. Cute and friendly for children aged 5 to 7: simple bold silhouettes that are easy to recognize even when tiny, big rounded forms, no small clutter, no scary details. Each object compact and fully inside its cell, centered, no shadows on the ground. Plain pure white background everywhere. Absolutely no text, no letters, no numbers, no labels, no watermark, no borders, no grid lines.
```

| Casa | Destino | Figura |
|---|---|---|
| linha 1, col. 1 | `imagens/1F382` | BOLO |
| linha 1, col. 2 | `imagens/1F9E2` | BONÉ |
| linha 1, col. 3 | `imagens/1FAD6` | BULE |
| linha 1, col. 4 | `imagens/1F43A` | LOBO |
| linha 2, col. 1 | `imagens/1FAD2` | AZEITONA |
| linha 2, col. 2 | `imagens/1F954` | BATATA |
| linha 2, col. 3 | `imagens/1F462` | BOTA |
| linha 2, col. 4 | `imagens/1F6F6` | BOTE |
| linha 3, col. 1 | `imagens/1F4F7` | FOTO |
| linha 3, col. 2 | `imagens/1F6E9` | JATO |
| linha 3, col. 3 | `imagens/1F95B` | LEITE |
| linha 3, col. 4 | `imagens/1F9A3` | MAMUTE |
| linha 4, col. 1 | `imagens/1F3CD` | MOTO |
| linha 4, col. 2 | `imagens/1F3B5` | NOTA |
| linha 4, col. 3 | `imagens/1F43E` | PATA |
| linha 4, col. 4 | `imagens/1F6F4` | PATINETE |

## Palavras 5 (mundo 4) · lote `palavras-5` (4 × 4)

```
A sprite sheet of 16 separate game icons arranged in a strict grid of 4 columns by 4 rows, read left to right, top to bottom. Every cell is the same size, with generous empty space between cells, and contains exactly one subject, centered. 2048 x 2048 pixels, square 1:1. Use the attached image of the golden owl Lili only as the style reference (material, lighting, colors, level of detail). Do not draw the owl unless a cell asks for her. Every picture illustrates a simple word for a child learning to read, so show the thing itself in the clearest way.

1. Row 1, column 1: a duck
2. Row 1, column 2: a jar with a lid
3. Row 1, column 3: a bar of soap
4. Row 1, column 4: a shoe
5. Row 2, column 1: a big curved arrow pointing right
6. Row 2, column 2: an old telephone with a curly cord
7. Row 2, column 3: a smiling young aunt waving
8. Row 2, column 4: a brick
9. Row 3, column 1: a tomato
10. Row 3, column 2: a tulip
11. Row 3, column 3: a ballot box with a paper being dropped in
12. Row 3, column 4: a goat
13. Row 4, column 1: a game die
14. Row 4, column 2: a hand with the index finger pointing up
15. Row 4, column 3: a bright sunny sky with the sun and one small cloud
16. Row 4, column 4: a fairy

Style for every object: glossy stylized 3D render matching the attached owl mascot image (Lili): the same soft, chunky rounded shapes, smooth glossy material with gentle highlights and a soft warm glow, warm golden and creamy tones mixed with bright friendly colors (sky blue, leaf green, coral red, sunny yellow), soft studio lighting. Cute and friendly for children aged 5 to 7: simple bold silhouettes that are easy to recognize even when tiny, big rounded forms, no small clutter, no scary details. Each object compact and fully inside its cell, centered, no shadows on the ground. Plain pure white background everywhere. Absolutely no text, no letters, no numbers, no labels, no watermark, no borders, no grid lines.
```

| Casa | Destino | Figura |
|---|---|---|
| linha 1, col. 1 | `imagens/1F986` | PATO |
| linha 1, col. 2 | `imagens/1FAD9` | POTE |
| linha 1, col. 3 | `imagens/1F9FC` | SABONETE |
| linha 1, col. 4 | `imagens/1F45E` | SAPATO |
| linha 2, col. 1 | `imagens/27A1` | SETA |
| linha 2, col. 2 | `imagens/260E` | TELEFONE |
| linha 2, col. 3 | `imagens/1F469` | TIA |
| linha 2, col. 4 | `imagens/1F9F1` | TIJOLO |
| linha 3, col. 1 | `imagens/1F345` | TOMATE |
| linha 3, col. 2 | `imagens/1F337` | TULIPA |
| linha 3, col. 3 | `imagens/1F5F3` | VOTO |
| linha 3, col. 4 | `imagens/1F410` | BODE |
| linha 4, col. 1 | `imagens/1F3B2` | DADO |
| linha 4, col. 2 | `imagens/261D` | DEDO |
| linha 4, col. 3 | `imagens/1F31E` | DIA |
| linha 4, col. 4 | `imagens/1F9DA` | FADA |

## Palavras 6 (mundo 4) · lote `palavras-6` (4 × 4)

```
A sprite sheet of 16 separate game icons arranged in a strict grid of 4 columns by 4 rows, read left to right, top to bottom. Every cell is the same size, with generous empty space between cells, and contains exactly one subject, centered. 2048 x 2048 pixels, square 1:1. Use the attached image of the golden owl Lili only as the style reference (material, lighting, colors, level of detail). Do not draw the owl unless a cell asks for her. Every picture illustrates a simple word for a child learning to read, so show the thing itself in the clearest way.

1. Row 1, column 1: a coin
2. Row 1, column 2: a green salad
3. Row 1, column 3: an electric plug
4. Row 1, column 4: a deer
5. Row 2, column 1: an avocado
6. Row 2, column 2: a pineapple
7. Row 2, column 3: a little bird showing its beak
8. Row 2, column 4: a mouth
9. Row 3, column 1: a rag doll with braids and a dress
10. Row 3, column 2: a cartoon head with big curly hair
11. Row 3, column 3: a lock
12. Row 3, column 4: a cup of coffee
13. Row 4, column 1: a cardboard box
14. Row 4, column 2: a foot with an adhesive bandage on the toe
15. Row 4, column 3: a bed
16. Row 4, column 4: a bactrian camel

Style for every object: glossy stylized 3D render matching the attached owl mascot image (Lili): the same soft, chunky rounded shapes, smooth glossy material with gentle highlights and a soft warm glow, warm golden and creamy tones mixed with bright friendly colors (sky blue, leaf green, coral red, sunny yellow), soft studio lighting. Cute and friendly for children aged 5 to 7: simple bold silhouettes that are easy to recognize even when tiny, big rounded forms, no small clutter, no scary details. Each object compact and fully inside its cell, centered, no shadows on the ground. Plain pure white background everywhere. Absolutely no text, no letters, no numbers, no labels, no watermark, no borders, no grid lines.
```

| Casa | Destino | Figura |
|---|---|---|
| linha 1, col. 1 | `imagens/1FA99` | MOEDA |
| linha 1, col. 2 | `imagens/1F957` | SALADA |
| linha 1, col. 3 | `imagens/1F50C` | TOMADA |
| linha 1, col. 4 | `imagens/1F98C` | VEADO |
| linha 2, col. 1 | `imagens/1F951` | ABACATE |
| linha 2, col. 2 | `imagens/1F34D` | ABACAXI |
| linha 2, col. 3 | `imagens/1F425` | BICO |
| linha 2, col. 4 | `imagens/1F444` | BOCA |
| linha 3, col. 1 | `imagens/1FA86` | BONECA |
| linha 3, col. 2 | `imagens/1F487` | CABELO |
| linha 3, col. 3 | `imagens/1F512` | CADEADO |
| linha 3, col. 4 | `imagens/2615` | CAFÉ |
| linha 4, col. 1 | `imagens/1F4E6` | CAIXA |
| linha 4, col. 2 | `imagens/1FA79` | CALO |
| linha 4, col. 3 | `imagens/1F6CF` | CAMA |
| linha 4, col. 4 | `imagens/1F42B` | CAMELO |

## Palavras 7 (mundo 4) · lote `palavras-7` (4 × 4)

```
A sprite sheet of 16 separate game icons arranged in a strict grid of 4 columns by 4 rows, read left to right, top to bottom. Every cell is the same size, with generous empty space between cells, and contains exactly one subject, centered. 2048 x 2048 pixels, square 1:1. Use the attached image of the golden owl Lili only as the style reference (material, lighting, colors, level of detail). Do not draw the owl unless a cell asks for her. Every picture illustrates a simple word for a child learning to read, so show the thing itself in the clearest way.

1. Row 1, column 1: a pen
2. Row 1, column 2: a horse
3. Row 1, column 3: a koala
4. Row 1, column 4: a coconut
5. Row 2, column 1: a white bottle of school glue with an orange cap
6. Row 2, column 2: a comet
7. Row 2, column 3: a drinking glass
8. Row 2, column 4: a kitchen knife with a rounded tip
9. Row 3, column 1: a seal
10. Row 3, column 2: a monkey
11. Row 3, column 3: a Brazilian indigenous oca: a round thatched straw hut
12. Row 3, column 4: a peteca: a Brazilian hand shuttlecock with colorful feathers
13. Row 4, column 1: a pointed snowy mountain peak
14. Row 4, column 2: a bag of popcorn
15. Row 4, column 3: a glass of orange juice with a straw
16. Row 4, column 4: a cow

Style for every object: glossy stylized 3D render matching the attached owl mascot image (Lili): the same soft, chunky rounded shapes, smooth glossy material with gentle highlights and a soft warm glow, warm golden and creamy tones mixed with bright friendly colors (sky blue, leaf green, coral red, sunny yellow), soft studio lighting. Cute and friendly for children aged 5 to 7: simple bold silhouettes that are easy to recognize even when tiny, big rounded forms, no small clutter, no scary details. Each object compact and fully inside its cell, centered, no shadows on the ground. Plain pure white background everywhere. Absolutely no text, no letters, no numbers, no labels, no watermark, no borders, no grid lines.
```

| Casa | Destino | Figura |
|---|---|---|
| linha 1, col. 1 | `imagens/1F58A` | CANETA |
| linha 1, col. 2 | `imagens/1F434` | CAVALO |
| linha 1, col. 3 | `imagens/1F428` | COALA |
| linha 1, col. 4 | `imagens/1F965` | COCO |
| linha 2, col. 1 | `imagens/1F9F4` | COLA |
| linha 2, col. 2 | `imagens/2604` | COMETA |
| linha 2, col. 3 | `imagens/1F964` | COPO |
| linha 2, col. 4 | `imagens/1F52A` | FACA |
| linha 3, col. 1 | `imagens/1F9AD` | FOCA |
| linha 3, col. 2 | `imagens/1F412` | MACACO |
| linha 3, col. 3 | `imagens/1F6D6` | OCA |
| linha 3, col. 4 | `imagens/1F3F8` | PETECA |
| linha 4, col. 1 | `imagens/1F3D4` | PICO |
| linha 4, col. 2 | `imagens/1F37F` | PIPOCA |
| linha 4, col. 3 | `imagens/1F9C3` | SUCO |
| linha 4, col. 4 | `imagens/1F404` | VACA |

## Palavras 8 (mundos 4, 5, 6) · lote `palavras-8` (4 × 4)

```
A sprite sheet of 16 separate game icons arranged in a strict grid of 4 columns by 4 rows, read left to right, top to bottom. Every cell is the same size, with generous empty space between cells, and contains exactly one subject, centered. 2048 x 2048 pixels, square 1:1. Use the attached image of the golden owl Lili only as the style reference (material, lighting, colors, level of detail). Do not draw the owl unless a cell asks for her. Every picture illustrates a simple word for a child learning to read, so show the thing itself in the clearest way.

1. Row 1, column 1: a mushroom
2. Row 1, column 2: a fire
3. Row 1, column 3: a group of two cattle
4. Row 1, column 4: a rooster
5. Row 2, column 1: a cat
6. Row 2, column 2: a shirt collar
7. Row 2, column 3: a water drop
8. Row 2, column 4: a board game with colored pieces
9. Row 3, column 1: a parrot
10. Row 3, column 2: a clear glass of water
11. Row 3, column 3: a t-shirt
12. Row 3, column 4: a house building
13. Row 4, column 1: a jellyfish
14. Row 4, column 2: musical notes floating
15. Row 4, column 3: a flower vase with flowers
16. Row 4, column 4: a cockroach

Style for every object: glossy stylized 3D render matching the attached owl mascot image (Lili): the same soft, chunky rounded shapes, smooth glossy material with gentle highlights and a soft warm glow, warm golden and creamy tones mixed with bright friendly colors (sky blue, leaf green, coral red, sunny yellow), soft studio lighting. Cute and friendly for children aged 5 to 7: simple bold silhouettes that are easy to recognize even when tiny, big rounded forms, no small clutter, no scary details. Each object compact and fully inside its cell, centered, no shadows on the ground. Plain pure white background everywhere. Absolutely no text, no letters, no numbers, no labels, no watermark, no borders, no grid lines.
```

| Casa | Destino | Figura |
|---|---|---|
| linha 1, col. 1 | `imagens/1F344` | COGUMELO |
| linha 1, col. 2 | `imagens/1F525` | FOGO |
| linha 1, col. 3 | `imagens/1F403` | GADO |
| linha 1, col. 4 | `imagens/1F413` | GALO |
| linha 2, col. 1 | `imagens/1F431` | GATO |
| linha 2, col. 2 | `imagens/1F454` | GOLA |
| linha 2, col. 3 | `imagens/1F4A7` | GOTA |
| linha 2, col. 4 | `imagens/1F3AE` | JOGO |
| linha 3, col. 1 | `imagens/1F99C` | PAPAGAIO |
| linha 3, col. 2 | `imagens/1F6B0` | ÁGUA |
| linha 3, col. 3 | `imagens/1F455` | CAMISA |
| linha 3, col. 4 | `imagens/1F3E0` | CASA |
| linha 4, col. 1 | `imagens/1FABC` | MEDUSA |
| linha 4, col. 2 | `imagens/1F3B6` | MÚSICA |
| linha 4, col. 3 | `imagens/1FAB4` | VASO |
| linha 4, col. 4 | `imagens/1FAB3` | BARATA |

## Palavras 9 (mundo 6) · lote `palavras-9` (4 × 4)

```
A sprite sheet of 16 separate game icons arranged in a strict grid of 4 columns by 4 rows, read left to right, top to bottom. Every cell is the same size, with generous empty space between cells, and contains exactly one subject, centered. 2048 x 2048 pixels, square 1:1. Use the attached image of the golden owl Lili only as the style reference (material, lighting, colors, level of detail). Do not draw the owl unless a cell asks for her. Every picture illustrates a simple word for a child learning to read, so show the thing itself in the clearest way.

1. Row 1, column 1: a beetle
2. Row 1, column 2: a chair
3. Row 1, column 3: a crown
4. Row 1, column 4: an owl
5. Row 2, column 1: a gorilla
6. Row 2, column 2: a crocodile
7. Row 2, column 3: a pear
8. Row 2, column 4: a turkey
9. Row 3, column 1: a lollipop
10. Row 3, column 2: a mermaid
11. Row 3, column 3: a pair of children safety scissors
12. Row 3, column 4: a cookie
13. Row 4, column 1: a castle
14. Row 4, column 2: a ladder
15. Row 4, column 3: a school
16. Row 4, column 4: a toothbrush

Style for every object: glossy stylized 3D render matching the attached owl mascot image (Lili): the same soft, chunky rounded shapes, smooth glossy material with gentle highlights and a soft warm glow, warm golden and creamy tones mixed with bright friendly colors (sky blue, leaf green, coral red, sunny yellow), soft studio lighting. Cute and friendly for children aged 5 to 7: simple bold silhouettes that are easy to recognize even when tiny, big rounded forms, no small clutter, no scary details. Each object compact and fully inside its cell, centered, no shadows on the ground. Plain pure white background everywhere. Absolutely no text, no letters, no numbers, no labels, no watermark, no borders, no grid lines.
```

| Casa | Destino | Figura |
|---|---|---|
| linha 1, col. 1 | `imagens/1FAB2` | BESOURO |
| linha 1, col. 2 | `imagens/1FA91` | CADEIRA |
| linha 1, col. 3 | `imagens/1F451` | COROA |
| linha 1, col. 4 | `imagens/1F989` | CORUJA |
| linha 2, col. 1 | `imagens/1F98D` | GORILA |
| linha 2, col. 2 | `imagens/1F40A` | JACARÉ |
| linha 2, col. 3 | `imagens/1F350` | PERA |
| linha 2, col. 4 | `imagens/1F983` | PERU |
| linha 3, col. 1 | `imagens/1F36D` | PIRULITO |
| linha 3, col. 2 | `imagens/1F9DC` | SEREIA |
| linha 3, col. 3 | `imagens/2702` | TESOURA |
| linha 3, col. 4 | `imagens/1F36A` | BISCOITO |
| linha 4, col. 1 | `imagens/1F3F0` | CASTELO |
| linha 4, col. 2 | `imagens/1FA9C` | ESCADA |
| linha 4, col. 3 | `imagens/1F3EB` | ESCOLA |
| linha 4, col. 4 | `imagens/1FAA5` | ESCOVA |

## Palavras 10 (mundo 6) · lote `palavras-10` (4 × 4)

```
A sprite sheet of 16 separate game icons arranged in a strict grid of 4 columns by 4 rows, read left to right, top to bottom. Every cell is the same size, with generous empty space between cells, and contains exactly one subject, centered. 2048 x 2048 pixels, square 1:1. Use the attached image of the golden owl Lili only as the style reference (material, lighting, colors, level of detail). Do not draw the owl unless a cell asks for her. Every picture illustrates a simple word for a child learning to read, so show the thing itself in the clearest way.

1. Row 1, column 1: a shield
2. Row 1, column 2: a toy sword
3. Row 1, column 3: a pencil
4. Row 1, column 4: a fly
5. Row 2, column 1: a carnival mask
6. Row 2, column 2: a nose
7. Row 2, column 3: a sneaker
8. Row 2, column 4: a dress
9. Row 3, column 1: a pair of glasses
10. Row 3, column 2: a bus
11. Row 3, column 3: a sailboat
12. Row 3, column 4: a butterfly
13. Row 4, column 1: a piece of meat
14. Row 4, column 2: a letter in an envelope with a heart seal
15. Row 4, column 3: a beaver
16. Row 4, column 4: a coiled rope

Style for every object: glossy stylized 3D render matching the attached owl mascot image (Lili): the same soft, chunky rounded shapes, smooth glossy material with gentle highlights and a soft warm glow, warm golden and creamy tones mixed with bright friendly colors (sky blue, leaf green, coral red, sunny yellow), soft studio lighting. Cute and friendly for children aged 5 to 7: simple bold silhouettes that are easy to recognize even when tiny, big rounded forms, no small clutter, no scary details. Each object compact and fully inside its cell, centered, no shadows on the ground. Plain pure white background everywhere. Absolutely no text, no letters, no numbers, no labels, no watermark, no borders, no grid lines.
```

| Casa | Destino | Figura |
|---|---|---|
| linha 1, col. 1 | `imagens/1F6E1` | ESCUDO |
| linha 1, col. 2 | `imagens/1F5E1` | ESPADA |
| linha 1, col. 3 | `imagens/270F` | LÁPIS |
| linha 1, col. 4 | `imagens/1FAB0` | MOSCA |
| linha 2, col. 1 | `imagens/1F3AD` | MÁSCARA |
| linha 2, col. 2 | `imagens/1F443` | NARIZ |
| linha 2, col. 3 | `imagens/1F45F` | TÊNIS |
| linha 2, col. 4 | `imagens/1F457` | VESTIDO |
| linha 3, col. 1 | `imagens/1F453` | ÓCULOS |
| linha 3, col. 2 | `imagens/1F68C` | ÔNIBUS |
| linha 3, col. 3 | `imagens/26F5` | BARCO |
| linha 3, col. 4 | `imagens/1F98B` | BORBOLETA |
| linha 4, col. 1 | `imagens/1F969` | CARNE |
| linha 4, col. 2 | `imagens/1F48C` | CARTA |
| linha 4, col. 3 | `imagens/1F9AB` | CASTOR |
| linha 4, col. 4 | `imagens/1FAA2` | CORDA |

## Palavras 11 (mundo 6) · lote `palavras-11` (4 × 4)

```
A sprite sheet of 16 separate game icons arranged in a strict grid of 4 columns by 4 rows, read left to right, top to bottom. Every cell is the same size, with generous empty space between cells, and contains exactly one subject, centered. 2048 x 2048 pixels, square 1:1. Use the attached image of the golden owl Lili only as the style reference (material, lighting, colors, level of detail). Do not draw the owl unless a cell asks for her. Every picture illustrates a simple word for a child learning to read, so show the thing itself in the clearest way.

1. Row 1, column 1: an ant
2. Row 1, column 2: a fork
3. Row 1, column 3: a lizard
4. Row 1, column 4: a big blue sea wave
5. Row 2, column 1: a hammer
6. Row 2, column 2: a leg
7. Row 2, column 3: a pig
8. Row 2, column 4: a door
9. Row 3, column 1: a soft ice cream
10. Row 3, column 2: a turtle
11. Row 3, column 3: a pie
12. Row 3, column 4: a unicorn
13. Row 4, column 1: a bear
14. Row 4, column 2: a tree
15. Row 4, column 3: a ring
16. Row 4, column 4: a bucket

Style for every object: glossy stylized 3D render matching the attached owl mascot image (Lili): the same soft, chunky rounded shapes, smooth glossy material with gentle highlights and a soft warm glow, warm golden and creamy tones mixed with bright friendly colors (sky blue, leaf green, coral red, sunny yellow), soft studio lighting. Cute and friendly for children aged 5 to 7: simple bold silhouettes that are easy to recognize even when tiny, big rounded forms, no small clutter, no scary details. Each object compact and fully inside its cell, centered, no shadows on the ground. Plain pure white background everywhere. Absolutely no text, no letters, no numbers, no labels, no watermark, no borders, no grid lines.
```

| Casa | Destino | Figura |
|---|---|---|
| linha 1, col. 1 | `imagens/1F41C` | FORMIGA |
| linha 1, col. 2 | `imagens/1F374` | GARFO |
| linha 1, col. 3 | `imagens/1F98E` | LAGARTO |
| linha 1, col. 4 | `imagens/1F30A` | MAR |
| linha 2, col. 1 | `imagens/1F528` | MARTELO |
| linha 2, col. 2 | `imagens/1F9B5` | PERNA |
| linha 2, col. 3 | `imagens/1F437` | PORCO |
| linha 2, col. 4 | `imagens/1F6AA` | PORTA |
| linha 3, col. 1 | `imagens/1F366` | SORVETE |
| linha 3, col. 2 | `imagens/1F422` | TARTARUGA |
| linha 3, col. 3 | `imagens/1F967` | TORTA |
| linha 3, col. 4 | `imagens/1F984` | UNICÓRNIO |
| linha 4, col. 1 | `imagens/1F43B` | URSO |
| linha 4, col. 2 | `imagens/1F333` | ÁRVORE |
| linha 4, col. 3 | `imagens/1F48D` | ANEL |
| linha 4, col. 4 | `imagens/1FAA3` | BALDE |

## Palavras 12 (mundo 6) · lote `palavras-12` (4 × 4)

```
A sprite sheet of 16 separate game icons arranged in a strict grid of 4 columns by 4 rows, read left to right, top to bottom. Every cell is the same size, with generous empty space between cells, and contains exactly one subject, centered. 2048 x 2048 pixels, square 1:1. Use the attached image of the golden owl Lili only as the style reference (material, lighting, colors, level of detail). Do not draw the owl unless a cell asks for her. Every picture illustrates a simple word for a child learning to read, so show the thing itself in the clearest way.

1. Row 1, column 1: a handbag
2. Row 1, column 2: a snail
3. Row 1, column 3: a soccer goal with a ball in the net
4. Row 1, column 4: a newspaper
5. Row 2, column 1: a honey pot
6. Row 2, column 2: a palm tree
7. Row 2, column 3: a sheet of paper
8. Row 2, column 4: an octopus
9. Row 3, column 1: a salt shaker
10. Row 3, column 2: a bright round smiling sun with rays
11. Row 3, column 3: a few peanuts in the shell
12. Row 3, column 4: a little angel with wings and a halo
13. Row 4, column 1: a little flag on a pole
14. Row 4, column 2: a kangaroo
15. Row 4, column 3: a computer
16. Row 4, column 4: a tooth

Style for every object: glossy stylized 3D render matching the attached owl mascot image (Lili): the same soft, chunky rounded shapes, smooth glossy material with gentle highlights and a soft warm glow, warm golden and creamy tones mixed with bright friendly colors (sky blue, leaf green, coral red, sunny yellow), soft studio lighting. Cute and friendly for children aged 5 to 7: simple bold silhouettes that are easy to recognize even when tiny, big rounded forms, no small clutter, no scary details. Each object compact and fully inside its cell, centered, no shadows on the ground. Plain pure white background everywhere. Absolutely no text, no letters, no numbers, no labels, no watermark, no borders, no grid lines.
```

| Casa | Destino | Figura |
|---|---|---|
| linha 1, col. 1 | `imagens/1F45C` | BOLSA |
| linha 1, col. 2 | `imagens/1F40C` | CARACOL |
| linha 1, col. 3 | `imagens/1F945` | GOL |
| linha 1, col. 4 | `imagens/1F4F0` | JORNAL |
| linha 2, col. 1 | `imagens/1F36F` | MEL |
| linha 2, col. 2 | `imagens/1F334` | PALMEIRA |
| linha 2, col. 3 | `imagens/1F4C4` | PAPEL |
| linha 2, col. 4 | `imagens/1F419` | POLVO |
| linha 3, col. 1 | `imagens/1F9C2` | SAL |
| linha 3, col. 2 | `imagens/2600` | SOL |
| linha 3, col. 3 | `imagens/1F95C` | AMENDOIM |
| linha 3, col. 4 | `imagens/1F47C` | ANJO |
| linha 4, col. 1 | `imagens/1F6A9` | BANDEIRA |
| linha 4, col. 2 | `imagens/1F998` | CANGURU |
| linha 4, col. 3 | `imagens/1F4BB` | COMPUTADOR |
| linha 4, col. 4 | `imagens/1F9B7` | DENTE |

## Palavras 13 (mundo 6) · lote `palavras-13` (4 × 4)

```
A sprite sheet of 16 separate game icons arranged in a strict grid of 4 columns by 4 rows, read left to right, top to bottom. Every cell is the same size, with generous empty space between cells, and contains exactly one subject, centered. 2048 x 2048 pixels, square 1:1. Use the attached image of the golden owl Lili only as the style reference (material, lighting, colors, level of detail). Do not draw the owl unless a cell asks for her. Every picture illustrates a simple word for a child learning to read, so show the thing itself in the clearest way.

1. Row 1, column 1: an elephant
2. Row 1, column 2: an envelope
3. Row 1, column 3: a sponge
4. Row 1, column 4: a ghost
5. Row 2, column 1: a goose
6. Row 2, column 2: a raccoon
7. Row 2, column 3: a flashlight
8. Row 2, column 4: an orange
9. Row 3, column 1: an electric light bulb
10. Row 3, column 2: a cartoon face sticking out the tongue
11. Row 3, column 3: a mango
12. Row 3, column 4: a strawberry
13. Row 4, column 1: a cute cartoon ninja
14. Row 4, column 2: a cloud
15. Row 4, column 3: a panda
16. Row 4, column 4: a roller skate

Style for every object: glossy stylized 3D render matching the attached owl mascot image (Lili): the same soft, chunky rounded shapes, smooth glossy material with gentle highlights and a soft warm glow, warm golden and creamy tones mixed with bright friendly colors (sky blue, leaf green, coral red, sunny yellow), soft studio lighting. Cute and friendly for children aged 5 to 7: simple bold silhouettes that are easy to recognize even when tiny, big rounded forms, no small clutter, no scary details. Each object compact and fully inside its cell, centered, no shadows on the ground. Plain pure white background everywhere. Absolutely no text, no letters, no numbers, no labels, no watermark, no borders, no grid lines.
```

| Casa | Destino | Figura |
|---|---|---|
| linha 1, col. 1 | `imagens/1F418` | ELEFANTE |
| linha 1, col. 2 | `imagens/2709` | ENVELOPE |
| linha 1, col. 3 | `imagens/1F9FD` | ESPONJA |
| linha 1, col. 4 | `imagens/1F47B` | FANTASMA |
| linha 2, col. 1 | `imagens/1FABF` | GANSO |
| linha 2, col. 2 | `imagens/1F99D` | GUAXINIM |
| linha 2, col. 3 | `imagens/1F526` | LANTERNA |
| linha 2, col. 4 | `imagens/1F34A` | LARANJA |
| linha 3, col. 1 | `imagens/1F4A1` | LÂMPADA |
| linha 3, col. 2 | `imagens/1F445` | LÍNGUA |
| linha 3, col. 3 | `imagens/1F96D` | MANGA |
| linha 3, col. 4 | `imagens/1F353` | MORANGO |
| linha 4, col. 1 | `imagens/1F977` | NINJA |
| linha 4, col. 2 | `imagens/2601` | NUVEM |
| linha 4, col. 3 | `imagens/1F43C` | PANDA |
| linha 4, col. 4 | `imagens/1F6FC` | PATINS |

## Palavras 14 (mundo 6) · lote `palavras-14` (4 × 4)

```
A sprite sheet of 16 separate game icons arranged in a strict grid of 4 columns by 4 rows, read left to right, top to bottom. Every cell is the same size, with generous empty space between cells, and contains exactly one subject, centered. 2048 x 2048 pixels, square 1:1. Use the attached image of the golden owl Lili only as the style reference (material, lighting, colors, level of detail). Do not draw the owl unless a cell asks for her. Every picture illustrates a simple word for a child learning to read, so show the thing itself in the clearest way.

1. Row 1, column 1: a hair comb
2. Row 1, column 2: a hot pepper
3. Row 1, column 3: a gray pigeon
4. Row 1, column 4: a bridge over water
5. Row 2, column 1: a caramel flan pudding
6. Row 2, column 2: a seed sprouting a tiny plant
7. Row 2, column 3: a drum with drumsticks
8. Row 2, column 4: a friendly cartoon vampire
9. Row 3, column 1: a silly friendly cartoon zombie, not scary
10. Row 3, column 2: an airplane
11. Row 3, column 3: a balloon
12. Row 3, column 4: a round sewing button with four holes
13. Row 4, column 1: a shrimp
14. Row 4, column 2: a scorpion
15. Row 4, column 3: a bowl of beans
16. Row 4, column 4: a lion

Style for every object: glossy stylized 3D render matching the attached owl mascot image (Lili): the same soft, chunky rounded shapes, smooth glossy material with gentle highlights and a soft warm glow, warm golden and creamy tones mixed with bright friendly colors (sky blue, leaf green, coral red, sunny yellow), soft studio lighting. Cute and friendly for children aged 5 to 7: simple bold silhouettes that are easy to recognize even when tiny, big rounded forms, no small clutter, no scary details. Each object compact and fully inside its cell, centered, no shadows on the ground. Plain pure white background everywhere. Absolutely no text, no letters, no numbers, no labels, no watermark, no borders, no grid lines.
```

| Casa | Destino | Figura |
|---|---|---|
| linha 1, col. 1 | `imagens/1FAAE` | PENTE |
| linha 1, col. 2 | `imagens/1F336` | PIMENTA |
| linha 1, col. 3 | `imagens/1F54A` | POMBO |
| linha 1, col. 4 | `imagens/1F309` | PONTE |
| linha 2, col. 1 | `imagens/1F36E` | PUDIM |
| linha 2, col. 2 | `imagens/1F331` | SEMENTE |
| linha 2, col. 3 | `imagens/1F941` | TAMBOR |
| linha 2, col. 4 | `imagens/1F9DB` | VAMPIRO |
| linha 3, col. 1 | `imagens/1F9DF` | ZUMBI |
| linha 3, col. 2 | `imagens/2708` | AVIÃO |
| linha 3, col. 3 | `imagens/1F388` | BALÃO |
| linha 3, col. 4 | `imagens/1F518` | BOTÃO |
| linha 4, col. 1 | `imagens/1F990` | CAMARÃO |
| linha 4, col. 2 | `imagens/1F982` | ESCORPIÃO |
| linha 4, col. 3 | `imagens/1FAD8` | FEIJÃO |
| linha 4, col. 4 | `imagens/1F981` | LEÃO |

## Palavras 15 (mundo 6) · lote `palavras-15` (4 × 4)

```
A sprite sheet of 16 separate game icons arranged in a strict grid of 4 columns by 4 rows, read left to right, top to bottom. Every cell is the same size, with generous empty space between cells, and contains exactly one subject, centered. 2048 x 2048 pixels, square 1:1. Use the attached image of the golden owl Lili only as the style reference (material, lighting, colors, level of detail). Do not draw the owl unless a cell asks for her. Every picture illustrates a simple word for a child learning to read, so show the thing itself in the clearest way.

1. Row 1, column 1: a lemon
2. Row 1, column 2: a melon
3. Row 1, column 3: an open hand
4. Row 1, column 4: a peacock
5. Row 2, column 1: a bell pepper
6. Row 2, column 2: a bread
7. Row 2, column 3: a television
8. Row 2, column 4: a shark
9. Row 3, column 1: a guitar
10. Row 3, column 2: a volcano
11. Row 3, column 3: a friendly cartoon witch with a pointed hat and a broom
12. Row 3, column 4: a broccoli
13. Row 4, column 1: a paperclip
14. Row 4, column 2: a snake
15. Row 4, column 3: a dragon
16. Row 4, column 4: a star

Style for every object: glossy stylized 3D render matching the attached owl mascot image (Lili): the same soft, chunky rounded shapes, smooth glossy material with gentle highlights and a soft warm glow, warm golden and creamy tones mixed with bright friendly colors (sky blue, leaf green, coral red, sunny yellow), soft studio lighting. Cute and friendly for children aged 5 to 7: simple bold silhouettes that are easy to recognize even when tiny, big rounded forms, no small clutter, no scary details. Each object compact and fully inside its cell, centered, no shadows on the ground. Plain pure white background everywhere. Absolutely no text, no letters, no numbers, no labels, no watermark, no borders, no grid lines.
```

| Casa | Destino | Figura |
|---|---|---|
| linha 1, col. 1 | `imagens/1F34B` | LIMÃO |
| linha 1, col. 2 | `imagens/1F348` | MELÃO |
| linha 1, col. 3 | `imagens/270B` | MÃO |
| linha 1, col. 4 | `imagens/1F99A` | PAVÃO |
| linha 2, col. 1 | `imagens/1FAD1` | PIMENTÃO |
| linha 2, col. 2 | `imagens/1F35E` | PÃO |
| linha 2, col. 3 | `imagens/1F4FA` | TELEVISÃO |
| linha 2, col. 4 | `imagens/1F988` | TUBARÃO |
| linha 3, col. 1 | `imagens/1F3B8` | VIOLÃO |
| linha 3, col. 2 | `imagens/1F30B` | VULCÃO |
| linha 3, col. 3 | `imagens/1F9D9` | BRUXA |
| linha 3, col. 4 | `imagens/1F966` | BRÓCOLIS |
| linha 4, col. 1 | `imagens/1F4CE` | CLIPE |
| linha 4, col. 2 | `imagens/1F40D` | COBRA |
| linha 4, col. 3 | `imagens/1F409` | DRAGÃO |
| linha 4, col. 4 | `imagens/2B50` | ESTRELA |

## Palavras 16 (mundo 6) · lote `palavras-16` (4 × 4)

```
A sprite sheet of 16 separate game icons arranged in a strict grid of 4 columns by 4 rows, read left to right, top to bottom. Every cell is the same size, with generous empty space between cells, and contains exactly one subject, centered. 2048 x 2048 pixels, square 1:1. Use the attached image of the golden owl Lili only as the style reference (material, lighting, colors, level of detail). Do not draw the owl unless a cell asks for her. Every picture illustrates a simple word for a child learning to read, so show the thing itself in the clearest way.

1. Row 1, column 1: a flamingo
2. Row 1, column 2: a colorful flower
3. Row 1, column 3: a factory with a chimney
4. Row 1, column 4: a world globe on a stand
5. Row 2, column 1: a cricket
6. Row 2, column 2: a church
7. Row 2, column 3: an open book
8. Row 2, column 4: an otter
9. Row 3, column 1: a subway train
10. Row 3, column 2: an oyster
11. Row 3, column 3: a rock
12. Row 3, column 4: a ringed planet
13. Row 4, column 1: a beach with a sun umbrella
14. Row 4, column 2: an empty round plate
15. Row 4, column 3: a wrapped gift box with a bow
16. Row 4, column 4: a computer keyboard

Style for every object: glossy stylized 3D render matching the attached owl mascot image (Lili): the same soft, chunky rounded shapes, smooth glossy material with gentle highlights and a soft warm glow, warm golden and creamy tones mixed with bright friendly colors (sky blue, leaf green, coral red, sunny yellow), soft studio lighting. Cute and friendly for children aged 5 to 7: simple bold silhouettes that are easy to recognize even when tiny, big rounded forms, no small clutter, no scary details. Each object compact and fully inside its cell, centered, no shadows on the ground. Plain pure white background everywhere. Absolutely no text, no letters, no numbers, no labels, no watermark, no borders, no grid lines.
```

| Casa | Destino | Figura |
|---|---|---|
| linha 1, col. 1 | `imagens/1F9A9` | FLAMINGO |
| linha 1, col. 2 | `imagens/1F338` | FLOR |
| linha 1, col. 3 | `imagens/1F3ED` | FÁBRICA |
| linha 1, col. 4 | `imagens/1F310` | GLOBO |
| linha 2, col. 1 | `imagens/1F997` | GRILO |
| linha 2, col. 2 | `imagens/26EA` | IGREJA |
| linha 2, col. 3 | `imagens/1F4D6` | LIVRO |
| linha 2, col. 4 | `imagens/1F9A6` | LONTRA |
| linha 3, col. 1 | `imagens/1F687` | METRÔ |
| linha 3, col. 2 | `imagens/1F9AA` | OSTRA |
| linha 3, col. 3 | `imagens/1FAA8` | PEDRA |
| linha 3, col. 4 | `imagens/1FA90` | PLANETA |
| linha 4, col. 1 | `imagens/1F3D6` | PRAIA |
| linha 4, col. 2 | `imagens/1F37D` | PRATO |
| linha 4, col. 3 | `imagens/1F381` | PRESENTE |
| linha 4, col. 4 | `imagens/2328` | TECLADO |

## Palavras 17 (mundos 6, 7) · lote `palavras-17` (4 × 4)

```
A sprite sheet of 16 separate game icons arranged in a strict grid of 4 columns by 4 rows, read left to right, top to bottom. Every cell is the same size, with generous empty space between cells, and contains exactly one subject, centered. 2048 x 2048 pixels, square 1:1. Use the attached image of the golden owl Lili only as the style reference (material, lighting, colors, level of detail). Do not draw the owl unless a cell asks for her. Every picture illustrates a simple word for a child learning to read, so show the thing itself in the clearest way.

1. Row 1, column 1: a tiger
2. Row 1, column 2: a tractor
3. Row 1, column 3: a train
4. Row 1, column 4: a sled
5. Row 2, column 1: a trophy
6. Row 2, column 2: a trumpet
7. Row 2, column 3: a zebra
8. Row 2, column 4: a hat
9. Row 3, column 1: a bored cartoon face with half-closed eyes
10. Row 3, column 2: a key
11. Row 3, column 3: a chocolate bar
12. Row 3, column 4: a cloud with rain
13. Row 4, column 1: a cup of tea
14. Row 4, column 2: a spiral shell
15. Row 4, column 3: an axe
16. Row 4, column 4: a school backpack

Style for every object: glossy stylized 3D render matching the attached owl mascot image (Lili): the same soft, chunky rounded shapes, smooth glossy material with gentle highlights and a soft warm glow, warm golden and creamy tones mixed with bright friendly colors (sky blue, leaf green, coral red, sunny yellow), soft studio lighting. Cute and friendly for children aged 5 to 7: simple bold silhouettes that are easy to recognize even when tiny, big rounded forms, no small clutter, no scary details. Each object compact and fully inside its cell, centered, no shadows on the ground. Plain pure white background everywhere. Absolutely no text, no letters, no numbers, no labels, no watermark, no borders, no grid lines.
```

| Casa | Destino | Figura |
|---|---|---|
| linha 1, col. 1 | `imagens/1F42F` | TIGRE |
| linha 1, col. 2 | `imagens/1F69C` | TRATOR |
| linha 1, col. 3 | `imagens/1F686` | TREM |
| linha 1, col. 4 | `imagens/1F6F7` | TRENÓ |
| linha 2, col. 1 | `imagens/1F3C6` | TROFÉU |
| linha 2, col. 2 | `imagens/1F3BA` | TROMPETE |
| linha 2, col. 3 | `imagens/1F993` | ZEBRA |
| linha 2, col. 4 | `imagens/1F452` | CHAPÉU |
| linha 3, col. 1 | `imagens/1F612` | CHATO |
| linha 3, col. 2 | `imagens/1F511` | CHAVE |
| linha 3, col. 3 | `imagens/1F36B` | CHOCOLATE |
| linha 3, col. 4 | `imagens/1F327` | CHUVA |
| linha 4, col. 1 | `imagens/1F375` | CHÁ |
| linha 4, col. 2 | `imagens/1F41A` | CONCHA |
| linha 4, col. 3 | `imagens/1FA93` | MACHADO |
| linha 4, col. 4 | `imagens/1F392` | MOCHILA |

## Palavras 18 (mundo 7) · lote `palavras-18` (4 × 4)

```
A sprite sheet of 16 separate game icons arranged in a strict grid of 4 columns by 4 rows, read left to right, top to bottom. Every cell is the same size, with generous empty space between cells, and contains exactly one subject, centered. 2048 x 2048 pixels, square 1:1. Use the attached image of the golden owl Lili only as the style reference (material, lighting, colors, level of detail). Do not draw the owl unless a cell asks for her. Every picture illustrates a simple word for a child learning to read, so show the thing itself in the clearest way.

1. Row 1, column 1: a hot dog
2. Row 1, column 2: a sandwich
3. Row 1, column 3: a honeybee
4. Row 1, column 4: a sewing needle
5. Row 2, column 1: a garlic bulb
6. Row 2, column 2: a spider
7. Row 2, column 3: soap bubbles
8. Row 2, column 4: a delivery truck
9. Row 3, column 1: a chestnut
10. Row 3, column 2: a rabbit
11. Row 3, column 3: a spoon
12. Row 3, column 4: a pea pod
13. Row 4, column 1: a mirror
14. Row 4, column 2: a green leaf
15. Row 4, column 3: a hen
16. Row 4, column 4: a dolphin

Style for every object: glossy stylized 3D render matching the attached owl mascot image (Lili): the same soft, chunky rounded shapes, smooth glossy material with gentle highlights and a soft warm glow, warm golden and creamy tones mixed with bright friendly colors (sky blue, leaf green, coral red, sunny yellow), soft studio lighting. Cute and friendly for children aged 5 to 7: simple bold silhouettes that are easy to recognize even when tiny, big rounded forms, no small clutter, no scary details. Each object compact and fully inside its cell, centered, no shadows on the ground. Plain pure white background everywhere. Absolutely no text, no letters, no numbers, no labels, no watermark, no borders, no grid lines.
```

| Casa | Destino | Figura |
|---|---|---|
| linha 1, col. 1 | `imagens/1F32D` | SALSICHA |
| linha 1, col. 2 | `imagens/1F96A` | SANDUÍCHE |
| linha 1, col. 3 | `imagens/1F41D` | ABELHA |
| linha 1, col. 4 | `imagens/1FAA1` | AGULHA |
| linha 2, col. 1 | `imagens/1F9C4` | ALHO |
| linha 2, col. 2 | `imagens/1F577` | ARANHA |
| linha 2, col. 3 | `imagens/1FAE7` | BOLHA |
| linha 2, col. 4 | `imagens/1F69A` | CAMINHÃO |
| linha 3, col. 1 | `imagens/1F330` | CASTANHA |
| linha 3, col. 2 | `imagens/1F430` | COELHO |
| linha 3, col. 3 | `imagens/1F944` | COLHER |
| linha 3, col. 4 | `imagens/1FADB` | ERVILHA |
| linha 4, col. 1 | `imagens/1FA9E` | ESPELHO |
| linha 4, col. 2 | `imagens/1F343` | FOLHA |
| linha 4, col. 3 | `imagens/1F414` | GALINHA |
| linha 4, col. 4 | `imagens/1F42C` | GOLFINHO |

## Palavras 19 (mundo 7) · lote `palavras-19` (4 × 4)

```
A sprite sheet of 16 separate game icons arranged in a strict grid of 4 columns by 4 rows, read left to right, top to bottom. Every cell is the same size, with generous empty space between cells, and contains exactly one subject, centered. 2048 x 2048 pixels, square 1:1. Use the attached image of the golden owl Lili only as the style reference (material, lighting, colors, level of detail). Do not draw the owl unless a cell asks for her. Every picture illustrates a simple word for a child learning to read, so show the thing itself in the clearest way.

1. Row 1, column 1: a small island with a palm tree
2. Row 1, column 2: a ladybug
3. Row 1, column 3: a gold medal with a ribbon
4. Row 1, column 4: an ear of corn
5. Row 2, column 1: a worm
6. Row 2, column 2: a mountain
7. Row 2, column 3: a nest with eggs
8. Row 2, column 4: a big cartoon eye
9. Row 3, column 1: an ear
10. Row 3, column 2: a sheep
11. Row 3, column 3: a battery
12. Row 3, column 4: a baby chick
13. Row 4, column 1: a bowl of white rice
14. Row 4, column 2: a tent
15. Row 4, column 3: a dog
16. Row 4, column 4: a car

Style for every object: glossy stylized 3D render matching the attached owl mascot image (Lili): the same soft, chunky rounded shapes, smooth glossy material with gentle highlights and a soft warm glow, warm golden and creamy tones mixed with bright friendly colors (sky blue, leaf green, coral red, sunny yellow), soft studio lighting. Cute and friendly for children aged 5 to 7: simple bold silhouettes that are easy to recognize even when tiny, big rounded forms, no small clutter, no scary details. Each object compact and fully inside its cell, centered, no shadows on the ground. Plain pure white background everywhere. Absolutely no text, no letters, no numbers, no labels, no watermark, no borders, no grid lines.
```

| Casa | Destino | Figura |
|---|---|---|
| linha 1, col. 1 | `imagens/1F3DD` | ILHA |
| linha 1, col. 2 | `imagens/1F41E` | JOANINHA |
| linha 1, col. 3 | `imagens/1F3C5` | MEDALHA |
| linha 1, col. 4 | `imagens/1F33D` | MILHO |
| linha 2, col. 1 | `imagens/1FAB1` | MINHOCA |
| linha 2, col. 2 | `imagens/26F0` | MONTANHA |
| linha 2, col. 3 | `imagens/1FABA` | NINHO |
| linha 2, col. 4 | `imagens/1F441` | OLHO |
| linha 3, col. 1 | `imagens/1F442` | ORELHA |
| linha 3, col. 2 | `imagens/1F411` | OVELHA |
| linha 3, col. 3 | `imagens/1F50B` | PILHA |
| linha 3, col. 4 | `imagens/1F424` | PINTINHO |
| linha 4, col. 1 | `imagens/1F35A` | ARROZ |
| linha 4, col. 2 | `imagens/26FA` | BARRACA |
| linha 4, col. 3 | `imagens/1F436` | CACHORRO |
| linha 4, col. 4 | `imagens/1F697` | CARRO |

## Palavras 20 (mundo 7) · lote `palavras-20` (4 × 4)

```
A sprite sheet of 16 separate game icons arranged in a strict grid of 4 columns by 4 rows, read left to right, top to bottom. Every cell is the same size, with generous empty space between cells, and contains exactly one subject, centered. 2048 x 2048 pixels, square 1:1. Use the attached image of the golden owl Lili only as the style reference (material, lighting, colors, level of detail). Do not draw the owl unless a cell asks for her. Every picture illustrates a simple word for a child learning to read, so show the thing itself in the clearest way.

1. Row 1, column 1: a bottle
2. Row 1, column 2: a plate of spaghetti
3. Row 1, column 3: a queen with a crown and a long dress
4. Row 1, column 4: a lightning bolt from a cloud
5. Row 2, column 1: a fox
6. Row 2, column 2: a mouse
7. Row 2, column 3: a king with a crown and a red cape
8. Row 2, column 4: a winding blue river between green banks
9. Row 3, column 1: a friendly robot
10. Row 3, column 2: a wheel
11. Row 3, column 3: a rose
12. Row 3, column 4: a radio
13. Row 4, column 1: a straight ruler
14. Row 4, column 2: the planet Earth
15. Row 4, column 3: an ambulance
16. Row 4, column 4: a balance scale

Style for every object: glossy stylized 3D render matching the attached owl mascot image (Lili): the same soft, chunky rounded shapes, smooth glossy material with gentle highlights and a soft warm glow, warm golden and creamy tones mixed with bright friendly colors (sky blue, leaf green, coral red, sunny yellow), soft studio lighting. Cute and friendly for children aged 5 to 7: simple bold silhouettes that are easy to recognize even when tiny, big rounded forms, no small clutter, no scary details. Each object compact and fully inside its cell, centered, no shadows on the ground. Plain pure white background everywhere. Absolutely no text, no letters, no numbers, no labels, no watermark, no borders, no grid lines.
```

| Casa | Destino | Figura |
|---|---|---|
| linha 1, col. 1 | `imagens/1F37E` | GARRAFA |
| linha 1, col. 2 | `imagens/1F35D` | MACARRÃO |
| linha 1, col. 3 | `imagens/1F478` | RAINHA |
| linha 1, col. 4 | `imagens/26A1` | RAIO |
| linha 2, col. 1 | `imagens/1F98A` | RAPOSA |
| linha 2, col. 2 | `imagens/1F42D` | RATO |
| linha 2, col. 3 | `imagens/1F934` | REI |
| linha 2, col. 4 | `imagens/1F3DE` | RIO |
| linha 3, col. 1 | `imagens/1F916` | ROBÔ |
| linha 3, col. 2 | `imagens/1F6DE` | RODA |
| linha 3, col. 3 | `imagens/1F339` | ROSA |
| linha 3, col. 4 | `imagens/1F4FB` | RÁDIO |
| linha 4, col. 1 | `imagens/1F4CF` | RÉGUA |
| linha 4, col. 2 | `imagens/1F30E` | TERRA |
| linha 4, col. 3 | `imagens/1F691` | AMBULÂNCIA |
| linha 4, col. 4 | `imagens/2696` | BALANÇA |

## Palavras 21 (mundo 7) · lote `palavras-21` (4 × 4)

```
A sprite sheet of 16 separate game icons arranged in a strict grid of 4 columns by 4 rows, read left to right, top to bottom. Every cell is the same size, with generous empty space between cells, and contains exactly one subject, centered. 2048 x 2048 pixels, square 1:1. Use the attached image of the golden owl Lili only as the style reference (material, lighting, colors, level of detail). Do not draw the owl unless a cell asks for her. Every picture illustrates a simple word for a child learning to read, so show the thing itself in the clearest way.

1. Row 1, column 1: a bicycle
2. Row 1, column 2: a strong flexed arm
3. Row 1, column 3: a compass
4. Row 1, column 4: a pair of trousers
5. Row 2, column 1: a bow and arrow
6. Row 2, column 2: an onion
7. Row 2, column 3: a mobile phone
8. Row 2, column 4: a carrot
9. Row 3, column 1: two cherries
10. Row 3, column 2: a basket
11. Row 3, column 3: a circus tent
12. Row 3, column 4: a swan
13. Row 4, column 1: a red heart
14. Row 4, column 2: a friendly long-necked dinosaur
15. Row 4, column 3: a ribbon bow
16. Row 4, column 4: a red apple

Style for every object: glossy stylized 3D render matching the attached owl mascot image (Lili): the same soft, chunky rounded shapes, smooth glossy material with gentle highlights and a soft warm glow, warm golden and creamy tones mixed with bright friendly colors (sky blue, leaf green, coral red, sunny yellow), soft studio lighting. Cute and friendly for children aged 5 to 7: simple bold silhouettes that are easy to recognize even when tiny, big rounded forms, no small clutter, no scary details. Each object compact and fully inside its cell, centered, no shadows on the ground. Plain pure white background everywhere. Absolutely no text, no letters, no numbers, no labels, no watermark, no borders, no grid lines.
```

| Casa | Destino | Figura |
|---|---|---|
| linha 1, col. 1 | `imagens/1F6B2` | BICICLETA |
| linha 1, col. 2 | `imagens/1F4AA` | BRAÇO |
| linha 1, col. 3 | `imagens/1F9ED` | BÚSSOLA |
| linha 1, col. 4 | `imagens/1F456` | CALÇA |
| linha 2, col. 1 | `imagens/1F3F9` | CAÇA |
| linha 2, col. 2 | `imagens/1F9C5` | CEBOLA |
| linha 2, col. 3 | `imagens/1F4F1` | CELULAR |
| linha 2, col. 4 | `imagens/1F955` | CENOURA |
| linha 3, col. 1 | `imagens/1F352` | CEREJA |
| linha 3, col. 2 | `imagens/1F9FA` | CESTA |
| linha 3, col. 3 | `imagens/1F3AA` | CIRCO |
| linha 3, col. 4 | `imagens/1F9A2` | CISNE |
| linha 4, col. 1 | `imagens/2764` | CORAÇÃO |
| linha 4, col. 2 | `imagens/1F995` | DINOSSAURO |
| linha 4, col. 3 | `imagens/1F380` | LAÇO |
| linha 4, col. 4 | `imagens/1F34E` | MAÇÃ |

## Palavras 22 (mundo 7) · lote `palavras-22` (4 × 4)

```
A sprite sheet of 16 separate game icons arranged in a strict grid of 4 columns by 4 rows, read left to right, top to bottom. Every cell is the same size, with generous empty space between cells, and contains exactly one subject, centered. 2048 x 2048 pixels, square 1:1. Use the attached image of the golden owl Lili only as the style reference (material, lighting, colors, level of detail). Do not draw the owl unless a cell asks for her. Every picture illustrates a simple word for a child learning to read, so show the thing itself in the clearest way.

1. Row 1, column 1: a watermelon
2. Row 1, column 2: a cute bat
3. Row 1, column 3: a jaguar (onça-pintada) with spots
4. Row 1, column 4: a bone
5. Row 2, column 1: a clown with a red nose
6. Row 2, column 2: a peach
7. Row 2, column 3: a rhinoceros
8. Row 2, column 4: a small farm field with a little barn and rows of crops
9. Row 3, column 1: a broom
10. Row 3, column 2: a crab
11. Row 3, column 3: a squirrel
12. Row 3, column 4: a rocket
13. Row 4, column 1: a mosquito
14. Row 4, column 2: a stack of pancakes
15. Row 4, column 3: a sloth
16. Row 4, column 4: a picture frame with a painting

Style for every object: glossy stylized 3D render matching the attached owl mascot image (Lili): the same soft, chunky rounded shapes, smooth glossy material with gentle highlights and a soft warm glow, warm golden and creamy tones mixed with bright friendly colors (sky blue, leaf green, coral red, sunny yellow), soft studio lighting. Cute and friendly for children aged 5 to 7: simple bold silhouettes that are easy to recognize even when tiny, big rounded forms, no small clutter, no scary details. Each object compact and fully inside its cell, centered, no shadows on the ground. Plain pure white background everywhere. Absolutely no text, no letters, no numbers, no labels, no watermark, no borders, no grid lines.
```

| Casa | Destino | Figura |
|---|---|---|
| linha 1, col. 1 | `imagens/1F349` | MELANCIA |
| linha 1, col. 2 | `imagens/1F987` | MORCEGO |
| linha 1, col. 3 | `imagens/1F406` | ONÇA |
| linha 1, col. 4 | `imagens/1F9B4` | OSSO |
| linha 2, col. 1 | `imagens/1F921` | PALHAÇO |
| linha 2, col. 2 | `imagens/1F351` | PÊSSEGO |
| linha 2, col. 3 | `imagens/1F98F` | RINOCERONTE |
| linha 2, col. 4 | `imagens/1F33E` | ROÇA |
| linha 3, col. 1 | `imagens/1F9F9` | VASSOURA |
| linha 3, col. 2 | `imagens/1F980` | CARANGUEJO |
| linha 3, col. 3 | `imagens/1F43F` | ESQUILO |
| linha 3, col. 4 | `imagens/1F680` | FOGUETE |
| linha 4, col. 1 | `imagens/1F99F` | MOSQUITO |
| linha 4, col. 2 | `imagens/1F95E` | PANQUECA |
| linha 4, col. 3 | `imagens/1F9A5` | PREGUIÇA |
| linha 4, col. 4 | `imagens/1F5BC` | QUADRO |

## Palavras 23 (mundo 7) · lote `palavras-23` (4 × 4)

```
A sprite sheet of 11 separate game icons arranged in a strict grid of 4 columns by 4 rows, read left to right, top to bottom. Every cell is the same size, with generous empty space between cells, and contains exactly one subject, centered. 2048 x 2048 pixels, square 1:1. Use the attached image of the golden owl Lili only as the style reference (material, lighting, colors, level of detail). Do not draw the owl unless a cell asks for her. Every picture illustrates a simple word for a child learning to read, so show the thing itself in the clearest way.

1. Row 1, column 1: a cheese wedge
2. Row 1, column 2: a cartoon face seen from the side with a finger pointing to the chin
3. Row 1, column 3: a doughnut
4. Row 1, column 4: an ice cube
5. Row 2, column 1: a giraffe
6. Row 2, column 2: a sunflower
7. Row 2, column 3: a friendly genie coming out of a lamp
8. Row 2, column 4: an alarm clock
9. Row 3, column 1: a hippopotamus
10. Row 3, column 2: a hospital
11. Row 3, column 3: a taxi

Style for every object: glossy stylized 3D render matching the attached owl mascot image (Lili): the same soft, chunky rounded shapes, smooth glossy material with gentle highlights and a soft warm glow, warm golden and creamy tones mixed with bright friendly colors (sky blue, leaf green, coral red, sunny yellow), soft studio lighting. Cute and friendly for children aged 5 to 7: simple bold silhouettes that are easy to recognize even when tiny, big rounded forms, no small clutter, no scary details. Each object compact and fully inside its cell, centered, no shadows on the ground. Plain pure white background everywhere. Absolutely no text, no letters, no numbers, no labels, no watermark, no borders, no grid lines.
```

| Casa | Destino | Figura |
|---|---|---|
| linha 1, col. 1 | `imagens/1F9C0` | QUEIJO |
| linha 1, col. 2 | `imagens/1F9D4` | QUEIXO |
| linha 1, col. 3 | `imagens/1F369` | ROSQUINHA |
| linha 1, col. 4 | `imagens/1F9CA` | GELO |
| linha 2, col. 1 | `imagens/1F992` | GIRAFA |
| linha 2, col. 2 | `imagens/1F33B` | GIRASSOL |
| linha 2, col. 3 | `imagens/1F9DE` | GÊNIO |
| linha 2, col. 4 | `imagens/23F0` | RELÓGIO |
| linha 3, col. 1 | `imagens/1F99B` | HIPOPÓTAMO |
| linha 3, col. 2 | `imagens/1F3E5` | HOSPITAL |
| linha 3, col. 3 | `imagens/1F695` | TÁXI |

---

## Depois de gerar

Mande as imagens dizendo o lote de cada uma. Eu fatio com o `fatiar_grade.py` (mesmo processo da Quitanda), tiro o fundo, gero os WebP e troco no Ler Brincando: as palavras substituem `imagens/<código>.svg` (o jogo passa a carregar o WebP próprio e mantém o OpenMoji como reserva), e a Lili, os avatares, os mundos, a lojinha, as medalhas e os ícones entram nas telas. Os créditos do OpenMoji saem da tela Sobre quando todas as figuras forem próprias.
