# Prompt para o Nano Banana 2 Lite · refazer a arte anterior a 16/11/2026

Refaz todas as imagens do jogo que entraram **antes de 16/11/2026** e não foram trocadas depois (conferido no histórico do repositório): **52 itens** da Quitanda (2 deles também usados na Rota) e **9 mercados**. O que foi gerado hoje (os outros 52 itens, os 13 itens próprios da Rota, os 28 personagens, as 12 decorações e os mercados 03, 05 e 06) já está no estilo novo e fica de fora.

- **Grades de itens:** peça 2048 × 2048. **Mercados:** um por vez, 2048 × 1152.
- **Envie como arquivo** (documento/anexo), não como foto, para o app não comprimir.
- Itens e mercados vão em prompts separados: na mesma imagem, o modelo mistura o 3D e a pintura.

---

## A · Itens, grade 1 de 4 (4 × 4): Frutas, Verduras e frango

```
A sprite sheet of 16 separate game item icons arranged in a strict grid of 4 columns by 4 rows, read left to right, top to bottom. Every cell is the same size, with generous empty space between cells, and contains exactly one object, centered. Square image, 1:1, 2048 x 2048 pixels. Within each food family the objects grow richer and more special from the first to the last.

1. Row 1, column 1: one small glossy green lime with a single leaf.
2. Row 1, column 2: a round bright orange with a small green leaf.
3. Row 1, column 3: a bunch of three ripe yellow bananas.
4. Row 1, column 4: a ripe mango blushing from red to yellow-green, with a leaf.
5. Row 2, column 1: a whole pineapple with a tall spiky green crown.
6. Row 2, column 2: a cashew apple: a glossy red-orange pear-shaped fruit with the gray kidney-shaped cashew nut hanging below it.
7. Row 2, column 3: a short tree-trunk piece covered in clusters of glossy dark purple jabuticaba berries growing right on the bark.
8. Row 2, column 4: a small bundle of fresh parsley and green onions tied with string.
9. Row 3, column 1: a bunch of large dark green collard leaves.
10. Row 3, column 2: two orange carrots with leafy green tops.
11. Row 3, column 3: a ripe red tomato with a green stem.
12. Row 3, column 4: an ear of yellow corn with the husk partly peeled back.
13. Row 4, column 1: two brown cassava roots, one cut open showing white flesh.
14. Row 4, column 2: a big round orange pumpkin with a curly stem.
15. Row 4, column 3: a big bowl of colorful fresh salad with lettuce, tomato, carrot and onion rings.
16. Row 4, column 4: a golden roasted chicken drumstick.

Style for every object: glossy stylized 3D render like a casual mobile game icon, smooth rounded shapes, vivid saturated colors with soft gradients, soft studio lighting with gentle highlights, each object compact and fully inside its cell, no shadows on the ground. Plain pure white background everywhere. Absolutely no text, no letters, no numbers, no labels, no watermark, no borders, no grid lines.
```

| Posição | Destino | Imagem |
|---|---|---|
| linha 1, col. 1 | `fr-1` | Limão |
| linha 1, col. 2 | `fr-2` | Laranja |
| linha 1, col. 3 | `fr-3` | Banana |
| linha 1, col. 4 | `fr-4` | Manga |
| linha 2, col. 1 | `fr-5` | Abacaxi |
| linha 2, col. 2 | `fr-6` | Caju |
| linha 2, col. 3 | `fr-7` | Jabuticaba |
| linha 2, col. 4 | `ve-1` | Cheiro-verde |
| linha 3, col. 1 | `ve-2` | Couve |
| linha 3, col. 2 | `ve-3` | Cenoura |
| linha 3, col. 3 | `ve-4` | Tomate |
| linha 3, col. 4 | `ve-5` | Milho |
| linha 4, col. 1 | `ve-6` | Mandioca |
| linha 4, col. 2 | `ve-7` | Abóbora |
| linha 4, col. 3 | `ve-8` | Salada |
| linha 4, col. 4 | `ca-2` | Frango |

## A · Itens, grade 2 de 4 (4 × 4): Peixes, Temperos e rapadura

```
A sprite sheet of 16 separate game item icons arranged in a strict grid of 4 columns by 4 rows, read left to right, top to bottom. Every cell is the same size, with generous empty space between cells, and contains exactly one object, centered. Square image, 1:1, 2048 x 2048 pixels. Within each food family the objects grow richer and more special from the first to the last.

1. Row 1, column 1: one pink cooked shrimp, curled.
2. Row 1, column 2: one small shiny silver sardine.
3. Row 1, column 3: a whole fresh fish with shiny silver-blue scales.
4. Row 1, column 4: an orange-red mangrove crab with big claws.
5. Row 2, column 1: a large whole gray-silver mullet fish.
6. Row 2, column 2: a bright red lobster with long antennae.
7. Row 2, column 3: a giant pirarucu river fish, long and dark olive, with red-edged scales near the tail.
8. Row 2, column 4: a black clay pot of moqueca: fish stew in a golden-orange coconut and palm-oil sauce with tomato, bell pepper rings and cilantro.
9. Row 3, column 1: a small glass salt shaker with a silver cap, a few salt crystals beside it.
10. Row 3, column 2: a golden-brown onion and a half onion showing its rings.
11. Row 3, column 3: a small cluster of tiny fiery red malagueta chili peppers.
12. Row 3, column 4: a glossy green bell pepper with a red one behind it.
13. Row 4, column 1: a glass bottle of deep orange-red palm oil, with a few orange palm fruits beside it, no label.
14. Row 4, column 2: a round jar of golden honey with a wooden dipper dripping honey.
15. Row 4, column 3: a small clay pot of rich red homemade tomato sauce with basil leaves and a wooden spoon.
16. Row 4, column 4: a brown brick of rapadura (unrefined cane sugar block), one corner broken off.

Style for every object: glossy stylized 3D render like a casual mobile game icon, smooth rounded shapes, vivid saturated colors with soft gradients, soft studio lighting with gentle highlights, each object compact and fully inside its cell, no shadows on the ground. Plain pure white background everywhere. Absolutely no text, no letters, no numbers, no labels, no watermark, no borders, no grid lines.
```

| Posição | Destino | Imagem |
|---|---|---|
| linha 1, col. 1 | `pe-1` | Camarão |
| linha 1, col. 2 | `pe-2` + `rota/pe-1` | Sardinha (também o Peixe pequeno da Rota) |
| linha 1, col. 3 | `pe-3` + `rota/pe-2` | Peixe (também o Peixe limpo da Rota) |
| linha 1, col. 4 | `pe-4` | Caranguejo |
| linha 2, col. 1 | `pe-5` | Tainha |
| linha 2, col. 2 | `pe-6` | Lagosta |
| linha 2, col. 3 | `pe-7` | Pirarucu |
| linha 2, col. 4 | `pe-8` | Moqueca |
| linha 3, col. 1 | `te-1` | Sal |
| linha 3, col. 2 | `te-3` | Cebola |
| linha 3, col. 3 | `te-4` | Pimenta-malagueta |
| linha 3, col. 4 | `te-5` | Pimentão |
| linha 4, col. 1 | `te-6` | Azeite de dendê |
| linha 4, col. 2 | `te-7` | Mel |
| linha 4, col. 3 | `te-8` | Molho |
| linha 4, col. 4 | `do-1` | Rapadura |

## A · Itens, grade 3 de 4 (4 × 4): Bebidas, Artesanato e Armazém

```
A sprite sheet of 16 separate game item icons arranged in a strict grid of 4 columns by 4 rows, read left to right, top to bottom. Every cell is the same size, with generous empty space between cells, and contains exactly one object, centered. Square image, 1:1, 2048 x 2048 pixels. Within each family the objects grow richer and more special from the first to the last.

1. Row 1, column 1: a clear glass of fresh water with a water drop.
2. Row 1, column 2: a green coconut with a straw stuck in the top.
3. Row 1, column 3: a tall glass of orange juice with an orange slice on the rim.
4. Row 1, column 4: a glass of pale green-yellow sugarcane juice with a lime wedge and a short piece of sugarcane beside it.
5. Row 2, column 1: a chimarrão: a decorated gourd filled with bright green yerba mate and a silver straw.
6. Row 2, column 2: a glass of amber guaraná soda with ice cubes and a few red guaraná berries with black seeds beside it.
7. Row 2, column 3: a tall glass bottle of clear golden cajuína drink with a red cashew apple beside it, bottle without label.
8. Row 2, column 4: a wooden spool of colorful thread.
9. Row 3, column 1: a ball of soft colorful yarn with two knitting needles.
10. Row 3, column 2: a woven straw hat with a colorful band.
11. Row 3, column 3: a woven straw basket with a handle.
12. Row 3, column 4: a viola caipira: a wooden ten-string Brazilian folk guitar with a decorated sound hole.
13. Row 4, column 1: a small stack of paçoca: crumbly light-brown peanut candy pieces.
14. Row 4, column 2: a small pile of roasted peanuts in their shells.
15. Row 4, column 3: a few Brazil nuts, some in hard brown shells and some shelled.
16. Row 4, column 4: a red and white striped paper bag overflowing with popcorn.

Style for every object: glossy stylized 3D render like a casual mobile game icon, smooth rounded shapes, vivid saturated colors with soft gradients, soft studio lighting with gentle highlights, each object compact and fully inside its cell, no shadows on the ground. Plain pure white background everywhere. Absolutely no text, no letters, no numbers, no labels, no watermark, no borders, no grid lines.
```

| Posição | Destino | Imagem |
|---|---|---|
| linha 1, col. 1 | `be-1` | Água |
| linha 1, col. 2 | `be-2` | Água de coco |
| linha 1, col. 3 | `be-3` | Suco |
| linha 1, col. 4 | `be-5` | Caldo de cana |
| linha 2, col. 1 | `be-6` | Chimarrão |
| linha 2, col. 2 | `be-7` | Guaraná |
| linha 2, col. 3 | `be-8` | Cajuína |
| linha 2, col. 4 | `ar-1` | Linha |
| linha 3, col. 1 | `ar-2` | Novelo |
| linha 3, col. 2 | `ar-5` | Chapéu de palha |
| linha 3, col. 3 | `ar-6` | Cesto de palha |
| linha 3, col. 4 | `ar-8` | Viola |
| linha 4, col. 1 | `do-2` | Paçoca |
| linha 4, col. 2 | `gr-1` | Amendoim |
| linha 4, col. 3 | `gr-2` | Castanha-do-pará |
| linha 4, col. 4 | `gr-3` | Pipoca |

## A · Itens, grade 4 de 4 (2 × 2): Armazém

```
A sprite sheet of 4 separate game item icons arranged in a strict grid of 2 columns by 2 rows, read left to right, top to bottom. Every cell is the same size, with generous empty space between cells, and contains exactly one object, centered. Square image, 1:1, 2048 x 2048 pixels. The objects grow richer and more special from the first to the last.

1. Row 1, column 1: a bowl of fluffy white rice.
2. Row 1, column 2: a small burlap sack overflowing with brown beans.
3. Row 2, column 1: a Northeastern Brazilian cuscuz: a dome-shaped yellow steamed cornmeal cake on a plate, with a pat of butter melting on top.
4. Row 2, column 2: a clay pot of baião de dois: rice and beans cooked together, topped with golden cubes of grilled cheese and cilantro.

Style for every object: glossy stylized 3D render like a casual mobile game icon, smooth rounded shapes, vivid saturated colors with soft gradients, soft studio lighting with gentle highlights, each object compact and fully inside its cell, no shadows on the ground. Plain pure white background everywhere. Absolutely no text, no letters, no numbers, no labels, no watermark, no borders, no grid lines.
```

| Posição | Destino | Imagem |
|---|---|---|
| linha 1, col. 1 | `gr-4` | Arroz |
| linha 1, col. 2 | `gr-6` | Feijão |
| linha 2, col. 1 | `gr-7` | Cuscuz |
| linha 2, col. 2 | `gr-8` | Baião de dois |

---

## B · Mercados (um por vez, 2048 × 1152)

Valem para a Quitanda e para a Rota. Todos pedem placas sem palavras, porque o texto gerado sai embaralhado.

### Ver-o-Peso, Belém (`mercados/01`)

```
Ver-o-Peso market in Belém: a blue iron market hall with four small pointed corner turrets and a tiled roof, on the edge of a wide bay, colorful wooden fishing boats moored at the quay, white market tents along the waterfront, view from the water's edge. Painted 2D illustration in a warm retro travel-poster style: golden late-afternoon light, big soft cumulus clouds, slightly grainy brush texture, flat shapes with soft shading, warm reds, ochres and teal greens, small figures of shoppers and vendors for scale. Wide 16:9 landscape, 2048 x 1152 pixels. Absolutely no text anywhere: no signs, no banners with words, no lettering, no logos, no watermark; any sign or banner is blank or shows only simple shapes.
```

### Mercado Adolpho Lisboa, Manaus (`mercados/02`)

```
Mercado Adolpho Lisboa in Manaus: an ornate red and yellow market facade with a central clock tower, a green iron arched gateway and white awnings, palm trees and shoppers in front, street-level view. Painted 2D illustration in a warm retro travel-poster style: golden late-afternoon light, big soft cumulus clouds, slightly grainy brush texture, flat shapes with soft shading, warm reds, ochres and teal greens, small figures of shoppers and vendors for scale. Wide 16:9 landscape, 2048 x 1152 pixels. Absolutely no text anywhere: no signs, no banners with words, no lettering, no logos, no watermark; any sign or banner is blank or shows only simple shapes.
```

### Mercado de São José, Recife (`mercados/04`)

```
Mercado de São José in Recife: a 19th-century light green iron market pavilion, a decorated pediment with arabesque ironwork and a large arched glass window in the center, fruit stalls and shoppers in front, street-level view. Painted 2D illustration in a warm retro travel-poster style: golden late-afternoon light, big soft cumulus clouds, slightly grainy brush texture, flat shapes with soft shading, warm reds, ochres and teal greens, small figures of shoppers and vendors for scale. Wide 16:9 landscape, 2048 x 1152 pixels. Absolutely no text anywhere: no signs, no banners with words, no lettering, no logos, no watermark; any sign or banner is blank or shows only simple shapes.
```

### Mercadão, São Paulo (`mercados/07`)

```
Inside the Mercadão of São Paulo: a grand market hall with light stone arches, a glass skylight in the high ceiling, colorful stained-glass windows, long aisles of stalls piled with fruit, shoppers walking, view down the central aisle. Painted 2D illustration in a warm retro travel-poster style: warm golden light pouring through the skylight, slightly grainy brush texture, flat shapes with soft shading, warm reds, ochres and teal greens, small figures of shoppers and vendors for scale. Wide 16:9 landscape, 2048 x 1152 pixels. Absolutely no text anywhere: no signs, no banners with words, no lettering, no logos, no watermark; any sign or banner is blank or shows only simple shapes.
```

### Mercado Central, Belo Horizonte (`mercados/08`)

```
Mercado Central in Belo Horizonte seen from above: a large market building with a roof of pale barrel vaults and a red facade, surrounded by city buildings, streets with small cars and trees, high aerial view. Painted 2D illustration in a warm retro travel-poster style: golden late-afternoon light, big soft cumulus clouds, slightly grainy brush texture, flat shapes with soft shading, warm reds, ochres and teal greens, small figures of shoppers and vendors for scale. Wide 16:9 landscape, 2048 x 1152 pixels. Absolutely no text anywhere: no signs, no banners with words, no lettering, no logos, no watermark; any sign or banner is blank or shows only simple shapes.
```

### Feira de São Cristóvão, Rio de Janeiro (`mercados/09`)

```
Feira de São Cristóvão in Rio de Janeiro seen from above: a huge oval pavilion with an open roof, filled with rows of stalls under blue tarps, crossed by white walkways in a cross shape, green hills of Rio in the distance, high aerial view. Painted 2D illustration in a warm retro travel-poster style: golden late-afternoon light, big soft cumulus clouds, slightly grainy brush texture, flat shapes with soft shading, warm reds, ochres and teal greens, small figures of shoppers and vendors for scale. Wide 16:9 landscape, 2048 x 1152 pixels. Absolutely no text anywhere: no signs, no banners with words, no lettering, no logos, no watermark; any sign or banner is blank or shows only simple shapes.
```

### Mercado Público, Porto Alegre (`mercados/10`)

```
Mercado Público in Porto Alegre: a historic two-story yellow building with a central pediment, rows of green arched doors and windows, shoppers and a few trees on the square in front, street-level view. Painted 2D illustration in a warm retro travel-poster style: golden late-afternoon light, big soft cumulus clouds, slightly grainy brush texture, flat shapes with soft shading, warm reds, ochres and teal greens, small figures of shoppers and vendors for scale. Wide 16:9 landscape, 2048 x 1152 pixels. Absolutely no text anywhere: no signs, no banners with words, no lettering, no logos, no watermark; any sign or banner is blank or shows only simple shapes.
```

### Mercado Público, Florianópolis (`mercados/11`)

```
Mercado Público in Florianópolis: a lively open-air courtyard full of people and white and green market umbrellas, between two long yellow buildings with green awnings, small corner towers in the background, view across the courtyard. Painted 2D illustration in a warm retro travel-poster style: golden late-afternoon light, big soft cumulus clouds, slightly grainy brush texture, flat shapes with soft shading, warm reds, ochres and teal greens, small figures of shoppers and vendors for scale. Wide 16:9 landscape, 2048 x 1152 pixels. Absolutely no text anywhere: no signs, no banners with words, no lettering, no logos, no watermark; any sign or banner is blank or shows only simple shapes.
```

### Mercado Municipal, Curitiba (`mercados/12`)

```
Mercado Municipal in Curitiba: a long low market facade with a row of red arches, green window frames and a terrace with red umbrellas and people at tables, trees along the sidewalk, street-level view. Painted 2D illustration in a warm retro travel-poster style: golden late-afternoon light, big soft cumulus clouds, slightly grainy brush texture, flat shapes with soft shading, warm reds, ochres and teal greens, small figures of shoppers and vendors for scale. Wide 16:9 landscape, 2048 x 1152 pixels. Absolutely no text anywhere: no signs, no banners with words, no lettering, no logos, no watermark; any sign or banner is blank or shows only simple shapes.
```

---

## Depois de gerar

Mande os arquivos. Eu acrescento os lotes `refazer-1` a `refazer-4` no `docs/arte/itens/grades.json`, fatio as grades (`fatiar_grade.py GRADE.png 4 4 refazer-1`, …, `fatiar_grade.py GRADE.png 2 2 refazer-4`), tiro o fundo com o `recortar_itens.py`, copio a sardinha e o peixe também para a Rota, troco os 9 mercados nas duas pastas `mercados/` e gero os APKs de teste.
