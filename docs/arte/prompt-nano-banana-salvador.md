# Prompts do Nano Banana · Rota das Feiras, 3º mercado (Feira de São Joaquim, Salvador)

Arte gerada em 25/11/2026 e já recortada para o jogo. Os originais ficam em `docs/arte/referencias/grade-rota-salvador.jpg` (itens) e `docs/arte/obstaculos/{engradado,sol,saveiro}-original.jpg`.

- **Itens:** `python docs/arte/itens/fatiar_grade.py docs/arte/referencias/grade-rota-salvador.jpg 4 4 rota-salvador` (de dentro de `docs/arte/itens/`). Saída em `versao-a-rota-das-feiras/itens/` (`ff-*`, `cm-*`, `cc-*` e `toldo`).
- **Obstáculos e saveiro:** `python docs/arte/obstaculos/recortar_obstaculos.py engradado sol saveiro`. Saída em `versao-a-rota-das-feiras/obstaculos/`.
- Envie as imagens como arquivo (documento), não como foto, para o app não comprimir.

## A · Itens 3D (grade 4 × 4, 2048 × 2048)

```
A sprite sheet of 16 separate game item icons arranged in a strict grid of 4 columns by 4 rows, read left to right, top to bottom. Every cell is the same size, with generous empty space between cells, and contains exactly one object, centered. Square image, 1:1, 2048 x 2048 pixels. Within each food family the objects grow richer and more special from the first to the last.

1. Row 1, column 1: a small pile of dry cream-colored black-eyed peas, each bean with its tiny black spot.
2. Row 1, column 2: a small clay bowl of peeled black-eyed peas soaking in water.
3. Row 1, column 3: a clay bowl of fluffy pale beige whipped bean batter with a wooden spoon.
4. Row 1, column 4: an abará: a steamed bean cake wrapped in a folded green banana leaf, opened at the top showing orange-tinted dough.
5. Row 2, column 1: an acarajé: a golden-orange deep-fried bean fritter split open and filled with vatapá, dried shrimp and a little green-and-red salad.
6. Row 2, column 2: two pink fresh raw shrimps.
7. Row 2, column 3: a small pile of dried smoked shrimp, deep orange-red and wrinkled.
8. Row 2, column 4: a clay bowl of vatapá: a smooth thick golden-orange creamy paste topped with two dried shrimps.
9. Row 3, column 1: a clay bowl of bobó de camarão: thick creamy pale-orange cassava purée with whole pink shrimps on top and a cilantro leaf.
10. Row 3, column 2: a round black clay pot of moqueca de camarão: bright orange coconut-and-palm-oil stew with pink shrimps, tomato and onion rings and green cilantro.
11. Row 3, column 3: a green young coconut with the top cut open and a striped straw.
12. Row 3, column 4: a brown hairy dry coconut, whole.
13. Row 4, column 1: a dry coconut cracked in half showing white flesh, with a small heap of fresh white grated coconut beside it.
14. Row 4, column 2: a small glass bottle of white coconut milk next to half a coconut shell.
15. Row 4, column 3: a stack of three cocadas: chunky golden-brown coconut candy squares, one on a small piece of paper.
16. Row 4, column 4: a small beach-style sunshade parasol with red and white stripes, closed halfway, seen slightly from above.

Style for every object: glossy stylized 3D render like a casual mobile game icon, smooth rounded shapes, vivid saturated colors with soft gradients, soft studio lighting with gentle highlights, each object compact and fully inside its cell, no shadows on the ground. Plain pure white background everywhere. Absolutely no text, no letters, no numbers, no labels, no watermark, no borders, no grid lines.
```

| Posição | Código | Item |
|---|---|---|
| linha 1 | `ff-1` a `ff-4` | Feijão-fradinho, Fradinho de molho, Massa de acarajé, Abará |
| linha 2 | `ff-5`, `cm-1` a `cm-3` | Acarajé, Camarão fresco, Camarão seco, Vatapá |
| linha 3 | `cm-4`, `cm-5`, `cc-1`, `cc-2` | Bobó de camarão, Moqueca de camarão, Coco verde, Coco seco |
| linha 4 | `cc-3` a `cc-5`, `toldo` | Coco ralado, Leite de coco, Cocada, ícone do Toldo |

## B · Engradado de coco (tira de 5 quadros, 2320 × 464, pixel art como o caixote)

```
A horizontal pixel art animation strip of 5 frames, side by side, equal size, on a plain pure white background, 2320 x 464 pixels. Subject: a sturdy wooden slatted crate seen straight from the front, with gaps between the slats showing brown hairy coconuts inside, reinforced with dark iron straps at the corners. Frame 1: intact crate. Frame 2: same crate with a big crack across the slats and one iron strap snapped. Frame 3: crate bursting outward, slats and splinters flying, a coconut visible in the middle. Frame 4: only a broken frame outline with scattered wood pieces and a few nails. Frame 5: just small flying splinters and dust fading away. Style: clean detailed pixel art, warm wood tones, dark brown outlines, flat shading, same scale in every frame. No text, no grid lines, no shadows on the ground.
```

Quadro 1 = engradado inteiro; 2 = rachado (falta 1 fusão); 3 a 5 = abertura.

## C · Sol e Toldo no tabuleiro (tira de 5 quadros, 2320 × 464)

```
A horizontal pixel art animation strip of 5 frames, side by side, equal size, on a plain pure white background, 2320 x 464 pixels. Each frame is a square floor tile seen from above. Frames 1 to 3: a sandy stone tile flooded with bright warm yellow sunlight, with wavy heat shimmer lines and small sparkles that shift position from frame to frame so they loop. Frame 4: the same tile covered by a red-and-white striped sunshade seen from directly above, casting cool blue shade. Frame 5: a small puff of white steam and a tiny orange heat swirl rising, as if something got too hot. Style: clean pixel art, soft outlines, flat shading, consistent scale. No text, no grid lines.
```

Quadros 1 a 3 = casa ao sol (animação em laço); 4 = casa com toldo; 5 = item que esquentou e perdeu nível.

## D · Saveiro do chefe (ilustração pintada, como os mercados)

```
A single traditional Bahian wooden sailing boat (saveiro) seen from the side, sailing to the right on small calm turquoise waves, with a large patched off-white sail, a dark wooden hull painted with a blue and red stripe, and its deck piled with wooden crates of coconuts and green bananas. Warm late-morning light. Painted illustration style matching a cozy mobile game: soft brush texture, rich warm colors, gentle outlines. The boat is isolated in the center on a plain pure white background with generous empty space around it. No people, no text, no letters, no watermark.
```
