# Vinheta Bentevi Apps

Vinheta de abertura de todos os apps da Bentevi Apps (Quitanda Zen, Rota das Feiras, Ler Brincando e Teto). O bem-te-vi chega voando e batendo as asas, freia com as asas abertas, pousa no galho (que balança com o peso), respira e canta "bem · te · vi" com a gravação real (`../bentevi-canto.mp3`). O nome aparece sílaba por sílaba no tempo do canto e, por fim, "apps". Dura 5,35 s.

| Arquivo | O que é |
|---|---|
| `vinheta-motor.js` | A animação inteira (`vinheta.montar(palco, raiz)` e `vinheta.quadro(t)`). É o mesmo código embutido nos `index.html` dos jogos e no `vinheta.js` do Ler Brincando |
| `gerar_vinheta_img.py` | Gera o bloco `VINHETA_IMG` (WebP em base64, 75% do tamanho dos recortes) |
| `recortes/` | Partes já recortadas do fundo magenta: galho, pousado, cantando (bico aberto), corpo em voo, asa no alto, asa embaixo e freada |
| `originais/` | Imagens do Nano Banana como chegaram |
| `vinheta-bentevi-apps.mp4` | Vídeo da vinheta (1080 × 1920, 60 quadros/s, com o canto). É o que o Teto toca na abertura e serve para Instagram e loja |

## Tempos

| s | Acontece |
|---|---|
| 0 a 1,42 | voo em curva, 7 batidas de asa (a asa desce mais rápido do que sobe) |
| 1,42 a 1,86 | freada: asas abertas, pernas esticadas até tocar o galho |
| 1,86 | pouso: amortece, o galho balança |
| 2,05 | canto: sílabas e bico aberto no tempo do `CALL` |
| 3,8 | sublinhado e "apps" |
| 5,35 | fim |

Para trocar a arte, mantenha as poses e o enquadramento: os pontos de encaixe (pés, ombro das asas) estão no topo do `vinheta-motor.js`.

## Prompts usados no Nano Banana

Fundo magenta liso (`#FF00FF`), e não branco, porque o bem-te-vi tem sobrancelha e garganta brancas. Peça 2048 × 2048 e envie como arquivo.

1. **Referência:** três poses do mesmo bem-te-vi (pousado, cantando de bico aberto, voando com as asas para cima), 3D estilizado de jogo casual.
2. **Galho:** galho fino na diagonal, da esquerda embaixo para a direita em cima, com folhinhas e botões amarelos, sem pássaro.
3. **Voo e freada (anexando a referência):** grade 2 × 2 com o corpo em voo sem asas, uma asa sozinha no alto (ombro embaixo à direita), a mesma asa embaixo (ombro em cima à direita) e a pose de freada, com asas abertas e pernas esticadas.
