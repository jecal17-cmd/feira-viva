# Prompts para o Nano Banana 2 Lite · imagens que faltam

Itens que ainda aparecem como emoji no jogo: **46 da Quitanda Zen** e **12 da Rota das Feiras** (58 no total), no mesmo estilo 3D dos itens que já estão no jogo. Personagens e decoração da banca ainda não aparecem no jogo e ficaram de fora.

## Como usar

1. Cole o prompt no Nano Banana 2 Lite, peça a imagem no maior tamanho disponível e em formato quadrado.
2. Confira a imagem: cada célula deve ter um objeto só, na ordem da tabela, sem texto. Se algum vier errado, gere só aquele de novo com o prompt individual do `falta-gerar.md`.
3. Mande a imagem para mim, ou fatie você mesmo: `python docs/arte/itens/fatiar_grade.py GRADE.png 8 8 todos` (ou `1`, `2`, `3`, `4` para os lotes). O script recorta cada célula, dá o nome certo, tira o fundo e põe no jogo certo. Os itens da Rota têm os mesmos códigos `pe-3`, `pe-4` e `pe-5` de itens da Quitanda, mas são outros pratos; no mapa da grade (`docs/arte/itens/grades.json`) eles levam o prefixo `rota/` e vão para a pasta da Rota.

**Tudo de uma vez ou em lotes?** O prompt único gera as 58 numa imagem só, mas com 58 objetos o modelo costuma trocar a ordem, repetir ou pular itens, e cada um sai pequeno (cerca de 250 px numa imagem de 2048 px). Os 4 lotes de 4 × 4 dão resultado bem mais confiável e com mais detalhe. Sugestão: tente o prompt único; se a ordem vier bagunçada, use os lotes.

## Prompt único (58 itens, grade 8 × 8)

```
A sprite sheet of 58 separate game item icons arranged in a strict grid of 8 columns by 8 rows, read left to right, top to bottom. Every cell is the same size, with generous white space between cells, and contains exactly one object, centered. Square image, 1:1. The last 6 cells of the bottom row stay completely empty and white.

1. Row 1, column 1: a small burlap sack of coarse yellow cassava flour with a wooden scoop.
2. Row 1, column 2: a chocolate bar with a few squares broken off.
3. Row 1, column 3: a round chewy white coconut candy with toasted golden edges.
4. Row 1, column 4: a glossy bright-yellow coconut and egg-yolk custard dome on a paper cup.
5. Row 1, column 5: a sugar-dusted round doughnut split open, filled with cream.
6. Row 1, column 6: a thick dark-red block of guava paste with one slice cut.
7. Row 1, column 7: a slice of thin rolled cake showing many fine swirls of guava filling.
8. Row 1, column 8: a single brown egg.
9. Row 2, column 1: a few pieces of puffy golden crispy pork crackling.
10. Row 2, column 2: a coil of plump grilled pork sausage.
11. Row 2, column 3: a thick piece of salted sun-dried beef with white salt crystals.
12. Row 2, column 4: a rack of roasted beef ribs, golden brown.
13. Row 2, column 5: two meat skewers grilled over charcoal on wooden sticks.
14. Row 2, column 6: a clay pot of black bean stew with pork pieces, orange slice on the side.
15. Row 2, column 7: a glass milk bottle with a blue cap.
16. Row 2, column 8: a block of pale yellow butter on a small dish.
17. Row 3, column 1: a round white fresh cheese with a wedge cut out.
18. Row 3, column 2: a short glass cup of creamy white spreadable cheese with a lid.
19. Row 3, column 3: a stick of golden grilled cheese with grill marks on a wooden skewer.
20. Row 3, column 4: a glass jar of glossy caramel-brown milk jam with a spoon.
21. Row 3, column 5: a slice of white cheese stacked with a slice of dark-red guava paste.
22. Row 3, column 6: a glossy caramel flan with a hole in the middle, caramel dripping.
23. Row 3, column 7: a rectangular golden crispy fried pastry with bubbly crust.
24. Row 3, column 8: a folded white tapioca crepe.
25. Row 4, column 1: a tall sandwich in a French roll overflowing with many pink mortadella slices.
26. Row 4, column 2: a teardrop-shaped golden fried croquette.
27. Row 4, column 3: a split golden black-eyed-pea fritter filled with shrimp and green salad.
28. Row 4, column 4: a huge fully loaded burger with egg, bacon, cheese, lettuce and tomato.
29. Row 4, column 5: a folded tapioca crepe filled with melted cheese and coconut.
30. Row 4, column 6: an open aluminium lunch box with rice, beans, steak, fried egg and salad.
31. Row 4, column 7: a small bundle of golden wheat stalks.
32. Row 4, column 8: a sliced sandwich loaf of bread.
33. Row 5, column 1: a crusty Brazilian bread roll with a split on top.
34. Row 5, column 2: three small round golden cheese breads.
35. Row 5, column 3: a braided sweet bread ring with sugar glaze.
36. Row 5, column 4: a round yellow cornmeal bundt cake with one slice cut.
37. Row 5, column 5: a round golden savory pot pie with a decorated crust.
38. Row 5, column 6: a tall two-tier party cake with colorful frosting and candles.
39. Row 5, column 7: a small green seedling sprouting in a little clay pot.
40. Row 5, column 8: a white daisy with a yellow center.
41. Row 6, column 1: a purple orchid flower stem.
42. Row 6, column 2: a big bright sunflower.
43. Row 6, column 3: a red and green bromeliad plant.
44. Row 6, column 4: a large red hibiscus flower.
45. Row 6, column 5: a small ipê tree covered in bright yellow blossoms.
46. Row 6, column 6: a lush tropical bouquet of colorful flowers wrapped in paper.
47. Row 6, column 7: a bunch of small dark-purple açaí palm berries on a branched stem.
48. Row 6, column 8: a handful of loose round dark-purple açaí berries.
49. Row 7, column 1: a small glass jar of thick deep-purple açaí pulp.
50. Row 7, column 2: a tall glass of blended deep-purple açaí with a straw.
51. Row 7, column 3: a raw white fish fillet on a green leaf.
52. Row 7, column 4: a whole roasted fish on a plate with lemon slices.
53. Row 7, column 5: a clay dish layered with shredded salted fish, golden farofa and banana slices.
54. Row 7, column 6: a single green jambu leaf with a tiny yellow flower bud.
55. Row 7, column 7: a tied bunch of green jambu herb with tiny yellow flower buds.
56. Row 7, column 8: a clay bowl of bright yellow tucupi broth.
57. Row 8, column 1: a dark gourd bowl (cuia) of yellow soup with green jambu leaves and small shrimp.
58. Row 8, column 2: roast duck pieces in yellow tucupi broth with jambu leaves, in a clay pot.

Style for every object: glossy stylized 3D render like a casual mobile game icon, smooth rounded shapes, vivid saturated colors with soft gradients, soft studio lighting with gentle highlights, each object compact and fully inside its cell, no shadows on the ground. Plain pure white background everywhere. Absolutely no text, no letters, no numbers, no labels, no watermark, no borders, no grid lines.
```

| Posição | Código | Item |
|---|---|---|
| linha 1, coluna 1 | `gr-5` | Farinha de mandioca |
| linha 1, coluna 2 | `do-3` | Chocolate |
| linha 1, coluna 3 | `do-4` | Cocada |
| linha 1, coluna 4 | `do-5` | Quindim |
| linha 1, coluna 5 | `do-6` | Sonho |
| linha 1, coluna 6 | `do-7` | Goiabada |
| linha 1, coluna 7 | `do-8` | Bolo de rolo |
| linha 1, coluna 8 | `ca-1` | Ovo |
| linha 2, coluna 1 | `ca-3` | Torresmo |
| linha 2, coluna 2 | `ca-4` | Linguiça |
| linha 2, coluna 3 | `ca-5` | Carne de sol |
| linha 2, coluna 4 | `ca-6` | Costela |
| linha 2, coluna 5 | `ca-7` | Espetinho |
| linha 2, coluna 6 | `ca-8` | Feijoada |
| linha 2, coluna 7 | `la-1` | Leite |
| linha 2, coluna 8 | `la-2` | Manteiga |
| linha 3, coluna 1 | `la-3` | Queijo minas |
| linha 3, coluna 2 | `la-4` | Requeijão |
| linha 3, coluna 3 | `la-5` | Queijo coalho |
| linha 3, coluna 4 | `la-6` | Doce de leite |
| linha 3, coluna 5 | `la-7` | Romeu e Julieta |
| linha 3, coluna 6 | `la-8` | Pudim |
| linha 3, coluna 7 | `ln-1` | Pastel |
| linha 3, coluna 8 | `ln-2` | Tapioca |
| linha 4, coluna 1 | `ln-3` | Sanduíche de mortadela |
| linha 4, coluna 2 | `ln-4` | Coxinha |
| linha 4, coluna 3 | `ln-5` | Acarajé |
| linha 4, coluna 4 | `ln-6` | X-tudo |
| linha 4, coluna 5 | `ln-7` | Tapioca recheada |
| linha 4, coluna 6 | `ln-8` | Marmita |
| linha 4, coluna 7 | `pa-1` | Trigo |
| linha 4, coluna 8 | `pa-2` | Pão de forma |
| linha 5, coluna 1 | `pa-3` | Pão francês |
| linha 5, coluna 2 | `pa-4` | Pão de queijo |
| linha 5, coluna 3 | `pa-5` | Rosca |
| linha 5, coluna 4 | `pa-6` | Bolo de fubá |
| linha 5, coluna 5 | `pa-7` | Empadão |
| linha 5, coluna 6 | `pa-8` | Bolo de festa |
| linha 5, coluna 7 | `fl-1` | Muda |
| linha 5, coluna 8 | `fl-2` | Margarida |
| linha 6, coluna 1 | `fl-3` | Orquídea |
| linha 6, coluna 2 | `fl-4` | Girassol |
| linha 6, coluna 3 | `fl-5` | Bromélia |
| linha 6, coluna 4 | `fl-6` | Hibisco |
| linha 6, coluna 5 | `fl-7` | Ipê-amarelo |
| linha 6, coluna 6 | `fl-8` | Buquê tropical |
| linha 6, coluna 7 | `ac-1` | Cacho de açaí |
| linha 6, coluna 8 | `ac-2` | Fruto |
| linha 7, coluna 1 | `ac-3` | Polpa |
| linha 7, coluna 2 | `ac-4` | Açaí batido |
| linha 7, coluna 3 | `pe-3` | Filé |
| linha 7, coluna 4 | `pe-4` | Peixe assado |
| linha 7, coluna 5 | `pe-5` | Pirarucu de casaca |
| linha 7, coluna 6 | `jt-1` | Folha de jambu |
| linha 7, coluna 7 | `jt-2` | Maço de jambu |
| linha 7, coluna 8 | `jt-3` | Caldo de tucupi |
| linha 8, coluna 1 | `jt-4` | Tacacá |
| linha 8, coluna 2 | `jt-5` | Pato no tucupi |

## Alternativa: 4 lotes (grade 4 × 4)

### Lote 1: Armazém, Doces e Carnes

```
A sprite sheet of 16 separate game item icons arranged in a strict grid of 4 columns by 4 rows, read left to right, top to bottom. Every cell is the same size, with generous white space between cells, and contains exactly one object, centered. Square image, 1:1.

1. Row 1, column 1: a small burlap sack of coarse yellow cassava flour with a wooden scoop.
2. Row 1, column 2: a chocolate bar with a few squares broken off.
3. Row 1, column 3: a round chewy white coconut candy with toasted golden edges.
4. Row 1, column 4: a glossy bright-yellow coconut and egg-yolk custard dome on a paper cup.
5. Row 2, column 1: a sugar-dusted round doughnut split open, filled with cream.
6. Row 2, column 2: a thick dark-red block of guava paste with one slice cut.
7. Row 2, column 3: a slice of thin rolled cake showing many fine swirls of guava filling.
8. Row 2, column 4: a single brown egg.
9. Row 3, column 1: a few pieces of puffy golden crispy pork crackling.
10. Row 3, column 2: a coil of plump grilled pork sausage.
11. Row 3, column 3: a thick piece of salted sun-dried beef with white salt crystals.
12. Row 3, column 4: a rack of roasted beef ribs, golden brown.
13. Row 4, column 1: two meat skewers grilled over charcoal on wooden sticks.
14. Row 4, column 2: a clay pot of black bean stew with pork pieces, orange slice on the side.
15. Row 4, column 3: a glass milk bottle with a blue cap.
16. Row 4, column 4: a block of pale yellow butter on a small dish.

Style for every object: glossy stylized 3D render like a casual mobile game icon, smooth rounded shapes, vivid saturated colors with soft gradients, soft studio lighting with gentle highlights, each object compact and fully inside its cell, no shadows on the ground. Plain pure white background everywhere. Absolutely no text, no letters, no numbers, no labels, no watermark, no borders, no grid lines.
```

| Posição | Código | Item |
|---|---|---|
| linha 1, coluna 1 | `gr-5` | Farinha de mandioca |
| linha 1, coluna 2 | `do-3` | Chocolate |
| linha 1, coluna 3 | `do-4` | Cocada |
| linha 1, coluna 4 | `do-5` | Quindim |
| linha 2, coluna 1 | `do-6` | Sonho |
| linha 2, coluna 2 | `do-7` | Goiabada |
| linha 2, coluna 3 | `do-8` | Bolo de rolo |
| linha 2, coluna 4 | `ca-1` | Ovo |
| linha 3, coluna 1 | `ca-3` | Torresmo |
| linha 3, coluna 2 | `ca-4` | Linguiça |
| linha 3, coluna 3 | `ca-5` | Carne de sol |
| linha 3, coluna 4 | `ca-6` | Costela |
| linha 4, coluna 1 | `ca-7` | Espetinho |
| linha 4, coluna 2 | `ca-8` | Feijoada |
| linha 4, coluna 3 | `la-1` | Leite |
| linha 4, coluna 4 | `la-2` | Manteiga |

### Lote 2: Laticínios e Lanches

```
A sprite sheet of 16 separate game item icons arranged in a strict grid of 4 columns by 4 rows, read left to right, top to bottom. Every cell is the same size, with generous white space between cells, and contains exactly one object, centered. Square image, 1:1.

1. Row 1, column 1: a round white fresh cheese with a wedge cut out.
2. Row 1, column 2: a short glass cup of creamy white spreadable cheese with a lid.
3. Row 1, column 3: a stick of golden grilled cheese with grill marks on a wooden skewer.
4. Row 1, column 4: a glass jar of glossy caramel-brown milk jam with a spoon.
5. Row 2, column 1: a slice of white cheese stacked with a slice of dark-red guava paste.
6. Row 2, column 2: a glossy caramel flan with a hole in the middle, caramel dripping.
7. Row 2, column 3: a rectangular golden crispy fried pastry with bubbly crust.
8. Row 2, column 4: a folded white tapioca crepe.
9. Row 3, column 1: a tall sandwich in a French roll overflowing with many pink mortadella slices.
10. Row 3, column 2: a teardrop-shaped golden fried croquette.
11. Row 3, column 3: a split golden black-eyed-pea fritter filled with shrimp and green salad.
12. Row 3, column 4: a huge fully loaded burger with egg, bacon, cheese, lettuce and tomato.
13. Row 4, column 1: a folded tapioca crepe filled with melted cheese and coconut.
14. Row 4, column 2: an open aluminium lunch box with rice, beans, steak, fried egg and salad.
15. Row 4, column 3: a small bundle of golden wheat stalks.
16. Row 4, column 4: a sliced sandwich loaf of bread.

Style for every object: glossy stylized 3D render like a casual mobile game icon, smooth rounded shapes, vivid saturated colors with soft gradients, soft studio lighting with gentle highlights, each object compact and fully inside its cell, no shadows on the ground. Plain pure white background everywhere. Absolutely no text, no letters, no numbers, no labels, no watermark, no borders, no grid lines.
```

| Posição | Código | Item |
|---|---|---|
| linha 1, coluna 1 | `la-3` | Queijo minas |
| linha 1, coluna 2 | `la-4` | Requeijão |
| linha 1, coluna 3 | `la-5` | Queijo coalho |
| linha 1, coluna 4 | `la-6` | Doce de leite |
| linha 2, coluna 1 | `la-7` | Romeu e Julieta |
| linha 2, coluna 2 | `la-8` | Pudim |
| linha 2, coluna 3 | `ln-1` | Pastel |
| linha 2, coluna 4 | `ln-2` | Tapioca |
| linha 3, coluna 1 | `ln-3` | Sanduíche de mortadela |
| linha 3, coluna 2 | `ln-4` | Coxinha |
| linha 3, coluna 3 | `ln-5` | Acarajé |
| linha 3, coluna 4 | `ln-6` | X-tudo |
| linha 4, coluna 1 | `ln-7` | Tapioca recheada |
| linha 4, coluna 2 | `ln-8` | Marmita |
| linha 4, coluna 3 | `pa-1` | Trigo |
| linha 4, coluna 4 | `pa-2` | Pão de forma |

### Lote 3: Padaria e Flores

```
A sprite sheet of 14 separate game item icons arranged in a strict grid of 4 columns by 4 rows, read left to right, top to bottom. Every cell is the same size, with generous white space between cells, and contains exactly one object, centered. Square image, 1:1. The last 2 cells of the bottom row stay completely empty and white.

1. Row 1, column 1: a crusty Brazilian bread roll with a split on top.
2. Row 1, column 2: three small round golden cheese breads.
3. Row 1, column 3: a braided sweet bread ring with sugar glaze.
4. Row 1, column 4: a round yellow cornmeal bundt cake with one slice cut.
5. Row 2, column 1: a round golden savory pot pie with a decorated crust.
6. Row 2, column 2: a tall two-tier party cake with colorful frosting and candles.
7. Row 2, column 3: a small green seedling sprouting in a little clay pot.
8. Row 2, column 4: a white daisy with a yellow center.
9. Row 3, column 1: a purple orchid flower stem.
10. Row 3, column 2: a big bright sunflower.
11. Row 3, column 3: a red and green bromeliad plant.
12. Row 3, column 4: a large red hibiscus flower.
13. Row 4, column 1: a small ipê tree covered in bright yellow blossoms.
14. Row 4, column 2: a lush tropical bouquet of colorful flowers wrapped in paper.

Style for every object: glossy stylized 3D render like a casual mobile game icon, smooth rounded shapes, vivid saturated colors with soft gradients, soft studio lighting with gentle highlights, each object compact and fully inside its cell, no shadows on the ground. Plain pure white background everywhere. Absolutely no text, no letters, no numbers, no labels, no watermark, no borders, no grid lines.
```

| Posição | Código | Item |
|---|---|---|
| linha 1, coluna 1 | `pa-3` | Pão francês |
| linha 1, coluna 2 | `pa-4` | Pão de queijo |
| linha 1, coluna 3 | `pa-5` | Rosca |
| linha 1, coluna 4 | `pa-6` | Bolo de fubá |
| linha 2, coluna 1 | `pa-7` | Empadão |
| linha 2, coluna 2 | `pa-8` | Bolo de festa |
| linha 2, coluna 3 | `fl-1` | Muda |
| linha 2, coluna 4 | `fl-2` | Margarida |
| linha 3, coluna 1 | `fl-3` | Orquídea |
| linha 3, coluna 2 | `fl-4` | Girassol |
| linha 3, coluna 3 | `fl-5` | Bromélia |
| linha 3, coluna 4 | `fl-6` | Hibisco |
| linha 4, coluna 1 | `fl-7` | Ipê-amarelo |
| linha 4, coluna 2 | `fl-8` | Buquê tropical |

### Lote 4: Rota das Feiras

```
A sprite sheet of 12 separate game item icons arranged in a strict grid of 4 columns by 4 rows, read left to right, top to bottom. Every cell is the same size, with generous white space between cells, and contains exactly one object, centered. Square image, 1:1. The last 4 cells of the bottom row stay completely empty and white.

1. Row 1, column 1: a bunch of small dark-purple açaí palm berries on a branched stem.
2. Row 1, column 2: a handful of loose round dark-purple açaí berries.
3. Row 1, column 3: a small glass jar of thick deep-purple açaí pulp.
4. Row 1, column 4: a tall glass of blended deep-purple açaí with a straw.
5. Row 2, column 1: a raw white fish fillet on a green leaf.
6. Row 2, column 2: a whole roasted fish on a plate with lemon slices.
7. Row 2, column 3: a clay dish layered with shredded salted fish, golden farofa and banana slices.
8. Row 2, column 4: a single green jambu leaf with a tiny yellow flower bud.
9. Row 3, column 1: a tied bunch of green jambu herb with tiny yellow flower buds.
10. Row 3, column 2: a clay bowl of bright yellow tucupi broth.
11. Row 3, column 3: a dark gourd bowl (cuia) of yellow soup with green jambu leaves and small shrimp.
12. Row 3, column 4: roast duck pieces in yellow tucupi broth with jambu leaves, in a clay pot.

Style for every object: glossy stylized 3D render like a casual mobile game icon, smooth rounded shapes, vivid saturated colors with soft gradients, soft studio lighting with gentle highlights, each object compact and fully inside its cell, no shadows on the ground. Plain pure white background everywhere. Absolutely no text, no letters, no numbers, no labels, no watermark, no borders, no grid lines.
```

| Posição | Código | Item |
|---|---|---|
| linha 1, coluna 1 | `ac-1` | Cacho de açaí |
| linha 1, coluna 2 | `ac-2` | Fruto |
| linha 1, coluna 3 | `ac-3` | Polpa |
| linha 1, coluna 4 | `ac-4` | Açaí batido |
| linha 2, coluna 1 | `pe-3` | Filé |
| linha 2, coluna 2 | `pe-4` | Peixe assado |
| linha 2, coluna 3 | `pe-5` | Pirarucu de casaca |
| linha 2, coluna 4 | `jt-1` | Folha de jambu |
| linha 3, coluna 1 | `jt-2` | Maço de jambu |
| linha 3, coluna 2 | `jt-3` | Caldo de tucupi |
| linha 3, coluna 3 | `jt-4` | Tacacá |
| linha 3, coluna 4 | `jt-5` | Pato no tucupi |
