# Prompt para o Nano Banana 2 Lite · imagens restantes e refações

Tudo o que ainda falta, mais as imagens que já estão no jogo e valem refazer. **Peça 2048 × 2048 nas grades** (cada célula fica com uns 400 px, o dobro da primeira grade).

**Envie para mim como arquivo** (documento/anexo) e não como foto: a última grade chegou com 1024 px, porque o app comprime as fotos.

## Por que são 2 prompts (e não 1)

Itens e decoração são objetos em 3D brilhante; os personagens são ilustração pintada, no estilo dos mercados. Na mesma imagem, o modelo mistura os dois estilos e estraga ambos. Por isso: **um prompt para tudo o que é 3D** (A) e **um para os personagens** (B). Os 3 mercados com texto embaralhado (C) são cenas largas, 16:9, e precisam ser geradas uma a uma.

## O que muda nas imagens que já estão no jogo

| Item | Problema |
|---|---|
| Açaí na tigela (`fr-8`, e a tigela da Rota `ac-5`) | o creme saiu marrom, com cara de chocolate; açaí é roxo-escuro |
| Café (`be-4`) | muito claro, parece chá com leite |
| Alho (`te-2`) | rosado e liso, quase igual à cebola (`te-3`) |
| Renda (`ar-4`) | é uma rede vermelha, parece rede de pesca, não renda de bilro |
| Boneco de barro (`ar-7`) | boneco laranja sem rosto, sem nada da tradição de Caruaru |
| Tapioca recheada (`ln-7`) | quase igual à tapioca simples (`ln-2`) |
| Fita do Bonfim (`ar-3`) | letras sem sentido nas fitas; você pediu para manter, então é **opcional**: se preferir a atual, eu ignoro essa célula |

## A · Itens e decoração (3D), grade 5 × 4

```
A sprite sheet of 19 separate game item icons arranged in a strict grid of 5 columns by 4 rows, read left to right, top to bottom. Every cell is the same size, with generous empty space between cells, and contains exactly one object, centered. Square image, 1:1, 2048 x 2048 pixels. The last 1 cells of the bottom row stay completely empty.

1. Row 1, column 1: a bowl of thick deep-purple açaí purée topped with banana slices, white tapioca flakes and granola, with a spoon.
2. Row 1, column 2: a white cup and saucer of strong dark black coffee.
3. Row 1, column 3: a white garlic bulb with visible cloves and papery skin, one loose clove beside it.
4. Row 1, column 4: a round piece of white bobbin lace with an intricate flower pattern, with a few wooden bobbins.
5. Row 1, column 5: a small hand-painted clay figurine in the folk-art style of Caruaru, Brazil: a smiling farmer with a straw hat and colorful clothes.
6. Row 2, column 1: an open tapioca crepe generously filled with melted cheese, shredded coconut and red jam, clearly overflowing.
7. Row 2, column 2: a bunch of plain colorful satin wish ribbons tied in a knot, completely blank ribbons with nothing printed on them.
8. Row 2, column 3: a red and white striped market stall awning.
9. Row 2, column 4: three small clay pots with fresh green herbs.
10. Row 2, column 5: a rustic wooden bench.
11. Row 3, column 1: a small blank green chalkboard on a wooden easel, with chalk doodles of fruit but no writing.
12. Row 3, column 2: a vintage red and gold market scale with a weighing pan.
13. Row 3, column 3: a string of warm glowing round light bulbs hanging in a loose curve.
14. Row 3, column 4: a small retro transistor radio with a round speaker grille.
15. Row 3, column 5: a delivery bicycle with a big wicker basket full of fruit in front.
16. Row 4, column 1: a two-wheeled street-market shopping trolley full of vegetables.
17. Row 4, column 2: a round vintage wall clock with a wooden frame.
18. Row 4, column 3: a string of small colorful festa junina paper flags in a loose curve.
19. Row 4, column 4: a round cozy cat bed with a soft cushion and a small fish toy.

Style for every object: glossy stylized 3D render like a casual mobile game icon, smooth rounded shapes, vivid saturated colors with soft gradients, soft studio lighting with gentle highlights, each object compact and fully inside its cell, no shadows on the ground. Plain pure white background everywhere. Absolutely no text, no letters, no numbers, no labels, no watermark, no borders, no grid lines.
```

| Posição | Destino | Imagem |
|---|---|---|
| linha 1, coluna 1 | `fr-8+rota/ac-5` | Açaí na tigela (refazer) |
| linha 1, coluna 2 | `be-4` | Café (refazer) |
| linha 1, coluna 3 | `te-2` | Alho (refazer) |
| linha 1, coluna 4 | `ar-4` | Renda (refazer) |
| linha 1, coluna 5 | `ar-7` | Boneco de barro (refazer) |
| linha 2, coluna 1 | `ln-7` | Tapioca recheada (refazer) |
| linha 2, coluna 2 | `ar-3` | Fita do Bonfim (opcional) |
| linha 2, coluna 3 | `decoracao/01-toldo-listrado` | Toldo listrado |
| linha 2, coluna 4 | `decoracao/02-vasos-de-ervas` | Vasos de ervas |
| linha 2, coluna 5 | `decoracao/03-banco-de-madeira` | Banco de madeira |
| linha 3, coluna 1 | `decoracao/04-lousa-de-precos` | Lousa de preços |
| linha 3, coluna 2 | `decoracao/05-balanca-antiga` | Balança antiga |
| linha 3, coluna 3 | `decoracao/06-luzinhas` | Luzinhas |
| linha 3, coluna 4 | `decoracao/07-radio-de-pilha` | Rádio de pilha |
| linha 3, coluna 5 | `decoracao/08-bicicleta-de-entrega` | Bicicleta de entrega |
| linha 4, coluna 1 | `decoracao/09-carrinho-de-feira` | Carrinho de feira |
| linha 4, coluna 2 | `decoracao/10-relogio-de-parede` | Relógio de parede |
| linha 4, coluna 3 | `decoracao/11-bandeirinhas` | Bandeirinhas |
| linha 4, coluna 4 | `decoracao/12-caminha-do-mingau` | Caminha do Mingau |

## B · Personagens (ilustração pintada), grade 6 × 5

```
A sprite sheet of 28 separate character portraits arranged in a strict grid of 6 columns by 5 rows, read left to right, top to bottom. Every cell is the same size, with generous empty space between cells, and contains exactly one character portrait, centered. Square image, 1:1, 2048 x 2048 pixels. The last 2 cells of the bottom row stay completely empty.

1. Row 1, column 1: man around 60, straw hat, plaid shirt, apron, big warm smile.
2. Row 1, column 2: girl about 10, ponytail, small apron, carrying a wooden crate.
3. Row 1, column 3: chubby white cat with a sleepy look.
4. Row 1, column 4: truck driver in a cap, arm on the window of a colorful truck.
5. Row 1, column 5: elderly woman, gray hair in a bun, printed dress, holding a gourd bowl of tacacá soup.
6. Row 1, column 6: bearded fisherman in a hat holding a river fish.
7. Row 2, column 1: young woman with curly hair weaving a straw basket.
8. Row 2, column 2: riverside man in a hat, wooden canoe behind him.
9. Row 2, column 3: Bahian street-food cook in a white turban and wide white skirt, with a tray of snacks.
10. Row 2, column 4: smiling young man playing a hand drum.
11. Row 2, column 5: older craftsman shaping a small clay figurine.
12. Row 2, column 6: woman with a bobbin-lace pillow on her lap.
13. Row 3, column 1: fruit seller in a leather hat with a fruit cart.
14. Row 3, column 2: girl in a bright floral chita dress with a hair bow.
15. Row 3, column 3: Japanese-Brazilian cook in an apron holding a steaming bowl of sobá.
16. Row 3, column 4: Pantanal cowboy in a hat and neckerchief, holding a horn cup of tereré.
17. Row 3, column 5: mustached snack-bar owner in an apron with a huge mortadella sandwich.
18. Row 3, column 6: woman in office clothes, phone in hand, walking fast.
19. Row 4, column 1: elderly woman from Minas Gerais in an apron, with a coffee pot and pão de queijo.
20. Row 4, column 2: young man in a hat holding a wheel of aged Minas cheese.
21. Row 4, column 3: older accordion player in a leather hat.
22. Row 4, column 4: cook in a head scarf stirring a big pot.
23. Row 4, column 5: gaúcho in bombacha trousers, neckerchief and beret, holding a churrasco skewer.
24. Row 4, column 6: young woman with a chimarrão gourd and a thermos.
25. Row 5, column 1: fisherman with a fishing net over his shoulder.
26. Row 5, column 2: elderly florist with a bucket of flowers.
27. Row 5, column 3: cook of Polish descent in a head scarf with a plate of pierogi.
28. Row 5, column 4: older man in an apron behind a general store counter.

Style for every portrait: painted 2D illustration in a warm retro travel-poster style, golden light, slightly grainy brush texture, soft shading, warm reds, ochres and teal greens; friendly, dignified, natural faces of real Brazilians, no caricature or stereotype. Each character shown from the chest up, centered and fully inside its cell, facing slightly toward the viewer. Plain off-white background everywhere (the same flat color in all cells). Absolutely no text, no names, no letters, no labels, no watermark, no borders, no grid lines.
```

| Posição | Destino | Imagem |
|---|---|---|
| linha 1, coluna 1 | `ze` | Seu Zé |
| linha 1, coluna 2 | `bia` | Bia |
| linha 1, coluna 3 | `mingau` | Mingau |
| linha 1, coluna 4 | `tonho` | Tonho |
| linha 1, coluna 5 | `naza` | Dona Nazaré |
| linha 1, coluna 6 | `raimundo` | Seu Raimundo |
| linha 2, coluna 1 | `iara` | Iara |
| linha 2, coluna 2 | `chico` | Seu Chico |
| linha 2, coluna 3 | `dada` | Dona Dadá |
| linha 2, coluna 4 | `jorginho` | Jorginho |
| linha 2, coluna 5 | `biu` | Mestre Biu |
| linha 2, coluna 6 | `flor` | Maria Flor |
| linha 3, coluna 1 | `cicero` | Seu Cícero |
| linha 3, coluna 2 | `rosinha` | Rosinha |
| linha 3, coluna 3 | `keiko` | Dona Keiko |
| linha 3, coluna 4 | `antenor` | Seu Antenor |
| linha 3, coluna 5 | `giuseppe` | Seu Giuseppe |
| linha 3, coluna 6 | `paula` | Paula |
| linha 4, coluna 1 | `geralda` | Dona Geralda |
| linha 4, coluna 2 | `tiao` | Tiãozinho |
| linha 4, coluna 3 | `jacinto` | Seu Jacinto |
| linha 4, coluna 4 | `dandara` | Dandara |
| linha 4, coluna 5 | `gaudencio` | Seu Gaudêncio |
| linha 4, coluna 6 | `livia` | Lívia |
| linha 5, coluna 1 | `dico` | Dico |
| linha 5, coluna 2 | `zulma` | Dona Zulma |
| linha 5, coluna 3 | `halina` | Dona Halina |
| linha 5, coluna 4 | `estanislau` | Seu Estanislau |

## C · Mercados para refazer (um por vez, 2048 × 1152)

O texto que o gerador escreve nas placas sai embaralhado; os prompts pedem placas sem palavras.

### Feira de São Joaquim, Salvador (`mercados/03`)

```
Feira de São Joaquim in Salvador: a sunny market street lined with stalls under teal awnings, hanging baskets, pans and colorful goods, a translucent canopy over the lane further ahead, shoppers walking, a red wall on the right, street-level view down the lane. Painted 2D illustration in a warm retro travel-poster style: golden late-afternoon light, big soft cumulus clouds, slightly grainy brush texture, flat shapes with soft shading, warm reds, ochres and teal greens, small figures of shoppers and vendors for scale. Wide 16:9 landscape, 2048 x 1152 pixels. Absolutely no text anywhere: no signs, no banners with words, no lettering, no logos, no watermark; any sign or banner is blank or shows only simple shapes.
```

### Mercado Central, Fortaleza (`mercados/05`)

```
Mercado Central in Fortaleza: a large rounded building shaped like a stadium, cream walls with teal-green bands and yellow trim, a great yellow arch over the entrance, trees and street vendors in front, red cars on the avenue, street-level view. Painted 2D illustration in a warm retro travel-poster style: golden late-afternoon light, big soft cumulus clouds, slightly grainy brush texture, flat shapes with soft shading, warm reds, ochres and teal greens, small figures of shoppers and vendors for scale. Wide 16:9 landscape, 2048 x 1152 pixels. Absolutely no text anywhere: no signs, no banners with words, no lettering, no logos, no watermark; any sign or banner is blank or shows only simple shapes.
```

### Feira Central, Campo Grande (`mercados/06`)

```
Feira Central in Campo Grande at night: a long covered hall with arched roof beams and hanging lamps, rows of stalls with red canopies serving steaming bowls of noodle soup, warm orange glow, people strolling down the central aisle, view down the aisle. Painted 2D illustration in a warm retro travel-poster style: golden late-afternoon light, big soft cumulus clouds, slightly grainy brush texture, flat shapes with soft shading, warm reds, ochres and teal greens, small figures of shoppers and vendors for scale. Wide 16:9 landscape, 2048 x 1152 pixels. Absolutely no text anywhere: no signs, no banners with words, no lettering, no logos, no watermark; any sign or banner is blank or shows only simple shapes.
```

## D · Os 5 personagens que faltaram (grade 3 × 2)

Na grade B, as posições 22 a 28 vieram trocadas. Aproveitei a 25 como Seu Gaudêncio e a 28 como Dona Zulma. Este prompt usa o estilo que o modelo de fato produziu nos outros 23 (desenho com contorno), para os 5 combinarem com eles.

```
A sheet of 5 separate character illustrations arranged in a strict grid of 3 columns by 2 rows, read left to right, top to bottom. Every cell is the same size, with generous empty space between cells so no figure touches another, and contains exactly one character, centered. The last cell of the bottom row stays empty. Square image, 1:1, 2048 x 2048 pixels.

1. Row 1, column 1: a young Afro-Brazilian woman cook in a colorful head scarf and apron, stirring a big cooking pot with a wooden spoon.
2. Row 1, column 2: a young woman from southern Brazil holding a chimarrão gourd with a metal straw, a thermos under her arm.
3. Row 1, column 3: a young fisherman in a cap carrying a folded fishing net over his shoulder.
4. Row 2, column 1: an older woman of Polish descent in a flowered head scarf and apron, holding a plate of pierogi dumplings.
5. Row 2, column 2: an older man with a gray mustache in a shopkeeper's apron, standing behind a small wooden counter with jars and a scale.

Style for every character: friendly cartoon illustration for a cozy mobile game, clean soft brown outlines, flat warm colors with gentle shading, natural, dignified faces of real Brazilians, no caricature or stereotype; each character shown from the knees or waist up, fully inside its cell. Plain pure white background everywhere. Absolutely no text, no names, no letters, no labels, no watermark, no borders, no grid lines.
```

| Posição | Destino | Personagem |
|---|---|---|
| linha 1, coluna 1 | `personagens/dandara` | Dandara |
| linha 1, coluna 2 | `personagens/livia` | Lívia |
| linha 1, coluna 3 | `personagens/dico` | Dico |
| linha 2, coluna 1 | `personagens/halina` | Dona Halina |
| linha 2, coluna 2 | `personagens/estanislau` | Seu Estanislau |

## Depois de gerar

Mande os arquivos. Eu fatio as grades (`docs/arte/itens/fatiar_grade.py GRADE.png 5 4 extra` e `... 6 5 personagens`), tiro o fundo, troco as imagens no jogo e atualizo a lista de arte.