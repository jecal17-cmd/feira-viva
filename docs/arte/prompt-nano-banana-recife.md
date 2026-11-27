# Prompts do Nano Banana · Rota das Feiras: Recife (4º mercado) e itens próprios de Manaus

Arte gerada em 26/11/2026 e já recortada para o jogo. Originais: `docs/arte/referencias/grade-rota-recife.jpg` e `grade-rota-manaus.jpg` (itens), `docs/arte/obstaculos/ciranda-original.jpg` e `galo-original.jpg`.

- **Itens** (de dentro de `docs/arte/itens/`): `python fatiar_grade.py ../referencias/grade-rota-recife.jpg 4 4 rota-recife` e `python fatiar_grade.py ../referencias/grade-rota-manaus.jpg 4 4 rota-manaus`. Na grade do Recife, a manteiga, o requeijão e a rapadura vieram com pedaços da casa de baixo: `python limpar_fragmentos.py rota/qc-2 rota/qc-4 rota/cn-2`.
- **Ciranda e Galo:** `python docs/arte/obstaculos/recortar_obstaculos.py ciranda galo`. A ciranda gera os quadros 1 a 5 e as versões espelhadas `ciranda-1i` e `ciranda-2i` (rodas que giram ao contrário). O quadro 3 (meia roda) não é usado.
- Envie as imagens como arquivo (documento), não como foto, para o app não comprimir.

## A · Itens de Recife (grade 4 × 4, 2048 × 2048)

```
A sprite sheet of 16 separate game item icons arranged in a strict grid of 4 columns by 4 rows, read left to right, top to bottom. Every cell is the same size, with generous empty space between cells, and contains exactly one object, centered. Square image, 1:1, 2048 x 2048 pixels. Within each food family the objects grow richer and more special from the first to the last.

1. Row 1, column 1: a small wooden bowl heaped with coarse white sea salt crystals.
2. Row 1, column 2: a thick slab of carne de sol: sun-dried salted beef, deep red with a light crust of white salt, tied with a string.
3. Row 1, column 3: a wooden skewer with four grilled cubes of carne de sol, browned and juicy, with a small piece of grilled white cheese at the tip.
4. Row 1, column 4: a clay bowl of cooked fresh green beans (feijão-verde), pale green beans with chopped cilantro on top.
5. Row 2, column 1: a round clay pot of baião de dois: rice and green beans mixed, topped with melted cubes of white grilled cheese and small pieces of browned dried beef.
6. Row 2, column 2: an old-fashioned aluminum milk can with a lid, beside a small glass of fresh milk.
7. Row 2, column 3: a small glass bottle of golden liquid clarified butter (manteiga de garrafa) with a cork.
8. Row 2, column 4: a rectangular block of firm white queijo coalho cheese with a thick slice cut off, the slice slightly golden from the grill.
9. Row 3, column 1: a block of Northeastern requeijão: firm golden-brown cooked cheese with a darker toasted crust, one slice cut.
10. Row 3, column 2: a cartola on a small white plate: fried banana slices covered with melted white cheese, sprinkled with sugar and cinnamon.
11. Row 3, column 3: a tall glass of greenish-yellow fresh sugarcane juice with a slice of lime, next to a short piece of green sugarcane stalk.
12. Row 3, column 4: a brown brick of rapadura (solid raw cane sugar), with a small piece broken off.
13. Row 4, column 1: a small glass jar of dark amber sugarcane molasses with a wooden dipper dripping.
14. Row 4, column 2: a block of deep red guava paste (goiabada) on a little wooden board, one slice cut.
15. Row 4, column 3: a bolo de rolo: a rolled cake log showing a tight spiral of many paper-thin cake layers and red guava, with one thin slice lying in front, dusted with sugar.
16. Row 4, column 4: a small wooden pantry chest with the lid half open, showing a glass jar and a cloth bundle inside.

Style for every object: glossy stylized 3D render like a casual mobile game icon, smooth rounded shapes, vivid saturated colors with soft gradients, soft studio lighting with gentle highlights, each object compact and fully inside its cell, no shadows on the ground. Plain pure white background everywhere. Absolutely no text, no letters, no numbers, no labels, no watermark, no borders, no grid lines.
```

| Posição | Código | Item |
|---|---|---|
| linha 1 | `cs-1` a `cs-4` | Sal grosso, Carne de sol, Espetinho de carne de sol, Feijão-verde |
| linha 2 | `cs-5`, `qc-1` a `qc-3` | Baião de dois, Leite, Manteiga de garrafa, Queijo coalho |
| linha 3 | `qc-4`, `qc-5`, `cn-1`, `cn-2` | Requeijão, Cartola, Caldo de cana, Rapadura |
| linha 4 | `cn-3` a `cn-5`, `despensa` | Mel de engenho, Goiabada, Bolo de rolo, ícone da Despensa (Selo Carne de Sol) |

## B · Itens de Manaus (grade 4 × 4, 2048 × 2048)

```
A sprite sheet of 16 separate game item icons arranged in a strict grid of 4 columns by 4 rows, read left to right, top to bottom. Every cell is the same size, with generous empty space between cells, and contains exactly one object, centered. Square image, 1:1, 2048 x 2048 pixels. Within each food family the objects grow richer and more special from the first to the last.

1. Row 1, column 1: a small pile of tiny translucent pinkish Amazon river shrimps.
2. Row 1, column 2: a jaraqui: a small silvery river fish with black-and-yellow striped tail fins, slightly curved.
3. Row 1, column 3: a pirarucu: a large Amazon fish with big scales turning red toward the tail, curled into a compact C shape.
4. Row 1, column 4: a deep bowl of caldeirada de tambaqui: golden fish broth with a thick fish steak, potato, half a boiled egg and cilantro.
5. Row 2, column 1: a lunch plate from an Amazon market: a grilled fish rib, white rice, yellow cassava farofa and a little tomato-and-onion vinaigrette.
6. Row 2, column 2: two cassava roots with rough brown bark, one cut open showing bright white flesh.
7. Row 2, column 3: a clay bowl of farinha do Uarini: crunchy yellow cassava flour in round little beads.
8. Row 2, column 4: a bowl of moist white tapioca starch, crumbly, with a small sieve.
9. Row 3, column 1: a plain white tapioca crepe folded in half, slightly toasted.
10. Row 3, column 2: a tapioca crepe folded and filled with bright orange slices of tucumã palm fruit and melted white cheese.
11. Row 3, column 3: a round woody Brazil nut pod cracked open, with several Brazil nuts in their shells spilling out.
12. Row 3, column 4: two big thick pacovã bananas (plantain-like), yellow with a few brown spots.
13. Row 4, column 1: a whole ripe pineapple with its green crown, compact.
14. Row 4, column 2: a tall glass of orange-yellow tropical fruit juice with a slice of fruit on the rim and a striped straw.
15. Row 4, column 3: a cluster of red guaraná fruits split open, each showing a black seed with a white edge like a small eye, next to a glass of amber guaraná soda with ice.
16. Row 4, column 4: a small colorful frevo umbrella, half open, with bright red, yellow, green and blue segments.

Style for every object: glossy stylized 3D render like a casual mobile game icon, smooth rounded shapes, vivid saturated colors with soft gradients, soft studio lighting with gentle highlights, each object compact and fully inside its cell, no shadows on the ground. Plain pure white background everywhere. Absolutely no text, no letters, no numbers, no labels, no watermark, no borders, no grid lines.
```

| Posição | Código | Item |
|---|---|---|
| linha 1 | `pr-1` a `pr-4` | Camarão regional, Jaraqui, Pirarucu, Caldeirada de tambaqui |
| linha 2 | `pr-5`, `md-1` a `md-3` | Prato do mercado, Mandioca, Farinha do Uarini, Goma de tapioca |
| linha 3 | `md-4`, `md-5`, `fr-1`, `fr-2` | Tapioca, Tapioquinha de tucumã, Castanha-do-pará, Banana pacovã |
| linha 4 | `fr-3` a `fr-5`, `frevo` | Abacaxi, Suco de frutas, Guaraná, sombrinha de frevo (ícone extra de Recife) |

## C · Casa da Roda de ciranda (tira de 5 quadros, 2320 × 464, pixel art como o sol)

```
A horizontal pixel art animation strip of 5 frames, side by side, equal size, on a plain pure white background, 2320 x 464 pixels. Each frame is a square floor tile seen from above. Frames 1 to 3: a warm sandy beach-colored tile with a dashed circular ring of small footprints and a curved arrow going clockwise around the edge; the footprints shift a little along the ring from frame to frame so they loop. Frame 4: the center tile of the dance: the same sandy tile with a small straw hat and a ring of tiny flowers in the middle. Frame 5: a swirl of curved motion lines and a few confetti dots, as if the tile just spun. Style: clean pixel art, soft outlines, flat shading, warm sand, teal and coral colors, consistent scale. No text, no grid lines.
```

Quadros 1 a 3 = casa da roda (laço); 4 = centro da roda; 5 = efeito quando a roda gira.

## D · Galo da Madrugada do chefe (ilustração pintada, como o saveiro)

```
A single giant carnival rooster sculpture on a parade float, seen from the side and facing right, built of glittering sequins and colorful feathers in red, yellow, green and blue, with a proud raised chest and a big curved tail, surrounded by a few small colorful frevo umbrellas and confetti in the air. Joyful festive morning light. Painted illustration style matching a cozy mobile game: soft brush texture, rich warm colors, gentle outlines. The float is isolated in the center on a plain pure white background with generous empty space around it. No people, no text, no letters, no logos, no watermark.
```
