# Contexto do projeto (para retomar o trabalho)

Resumo do estado atual, das decisões tomadas e de como continuar. Atualizado em 12/11/2026.

## O que é

Três jogos mobile em português, todos feitos em HTML5 de arquivo único e empacotados como app Android com Capacitor:

| Jogo | Repositório e pasta | Público e proposta | Receita | Estado |
|---|---|---|---|---|
| **Quitanda Zen** (Versão B da Feira Viva; nome internacional *Quitanda: Merge Across Brazil*) | `feira-viva` · `versao-b-quitanda-zen/` | Passatempo de juntar itens, sem derrota, viajando por 12 mercados do Brasil em voltas infinitas | Anúncios + compras (simulados) | Protótipo v0.5 |
| **Rota das Feiras** (Versão A da Feira Viva) | `feira-viva` · `versao-a-rota-das-feiras/` | Puzzle de fusão com turnos contados, fases, estrelas e chefe | Compras (simuladas), sem anúncios | Protótipo de teste v0.1 (só o Ver-o-Peso) |
| **Ler Brincando** | `LerBrincando` (raiz) | Alfabetização pelo método fônico, 5 a 7 anos | Nenhuma (sem anúncios, compras ou rastreadores) | v1.3.1 |

A desenvolvedora se chama **Bentevi** (Bentevi Games): a vinheta de abertura da Quitanda e da Rota mostra o bem-te-vi pousando e cantando.

## Onde está cada coisa (feira-viva)

| Caminho | Conteúdo |
|---|---|
| `versao-b-quitanda-zen/index.html` | O jogo Quitanda Zen inteiro (HTML, CSS e JS num arquivo). Dados de balanceamento no bloco `DADOS`, no topo do script |
| `versao-a-rota-das-feiras/index.html` | O jogo Rota das Feiras inteiro |
| `app-android/` | App Android da Quitanda (Capacitor 8, `com.feiraviva.quitanda`, com AdMob de teste) |
| `app-android-rota/` | App Android da Rota (Capacitor 8, `com.feiraviva.rota`, sem anúncios) |
| `.github/workflows/android.yml` | Compila os dois APKs a cada push que mexa nos jogos ou nos apps; também por **Actions → Apps Android (APKs de teste) → Run workflow** |
| `docs/design-de-jogo.md` | Documento de design das duas versões, com as revisões numeradas (seções 3.9, 3.10, 4.8 a 4.10) |
| `docs/avaliacoes/` | Relatórios de avaliação como usuário novo (um .docx por jogo, inclusive o Ler Brincando) |
| `docs/arte/` | Lista de arte (104 itens, 12 mercados, 28 personagens), ícones e o canto do bem-te-vi |
| `docs/arte/icones/` | Artes dos ícones (`quitanda-arte.png`, `rota-arte.png`, `ler-brincando/arte-icone.png`), ícones 512 px da loja e o gerador `gerar_icones_arte.py` |
| `docs/mockups/` | Telas de sugestão em SVG do início do projeto |
| `docs/loja-play/quitanda-zen/` | Página da Play Store da Quitanda: textos pt-BR e en-US, capturas, gráfico de destaque, ícone, respostas da Play Console e passo a passo (`LEIAME.md`) |
| `versao-b-quitanda-zen/privacidade.html` | Política de privacidade da Quitanda (pt e en), publicada pelo GitHub Pages |
| `.github/workflows/quitanda-aab.yml` | Gera o AAB assinado da Quitanda para a Play Store (só manual: **Actions → Quitanda · AAB para a Play Store → Run workflow**) |

## Como rodar e testar

- **Navegador:** abrir o `index.html` de cada versão. Parâmetros úteis: `?lang=en` ou `?lang=pt` (idioma) e `?intro=0` (pula a vinheta).
- **Web publicada (GitHub Pages da `main`):** `https://jecal17-cmd.github.io/feira-viva/versao-b-quitanda-zen/` e `.../versao-a-rota-das-feiras/`.
- **APKs:** aba **Actions**, execução mais recente de *Apps Android (APKs de teste)*, em **Artifacts**: `quitanda-apk-teste` e `rota-das-feiras-apk-teste` (APK de debug, instala direto no celular).
- **Ferramentas de teste dentro dos jogos:**
  - Quitanda: em **Ajustes**, 5 toques no número da versão mostram o Modo teste, o painel de métricas e "Remover anúncios (simulado)".
  - Rota: em **Ajustes** há o Modo teste (libera fases e oferece +5 turnos) e o painel por fase (tentativas, vitórias, derrotas, taxa de derrota).
- **Testes automatizados:** não há suíte no repositório. Os testes desta fase foram robôs Playwright descartáveis (bot que joga, fusão tripla por arraste, capturas). Para repetir, abra o HTML com Playwright e chame as funções globais do jogo (`spawn`, `merge`, `deliver`, `travel`, `startPhase` etc.).

## Ícones

As artes vieram do Midjourney (prompts na conversa e em `docs/arte/`) e já trazem a própria moldura (quadrado arredondado) sobre um fundo liso. O script apaga o fundo de fora da moldura e encaixa a arte inteira em cada formato, sem cortar nada: no ícone adaptativo ela cabe no círculo seguro de 66 dp, sobre a cor de fundo. Ele gera os ícones adaptativos e antigos do Android em todas as densidades, as telas de abertura, o ícone da web (192 px) e o ícone da loja (512 px):

```bash
python docs/arte/icones/gerar_icones_arte.py docs/arte/icones/quitanda-arte.png app-android/android/app/src/main/res --cor '#3E9B5F' --web versao-b-quitanda-zen/icone-192.png --loja docs/arte/icones/quitanda-512.png
python docs/arte/icones/gerar_icones_arte.py docs/arte/icones/rota-arte.png app-android-rota/android/app/src/main/res --cor '#139C8C' --web versao-a-rota-das-feiras/icone-192.png --loja docs/arte/icones/rota-512.png
```

No Ler Brincando, a arte nova (coruja) e os ícones já gerados estão em `docs/arte/icones/ler-brincando/` (pasta `res/` para copiar em `android/app/src/main/res`, `icone-192.png`, `icone-512.png` e `loja-512.png`); copie também o `gerar_icones_arte.py` novo para `ferramentas/`. Comando lá: `python ferramentas/gerar_icones_arte.py icones/arte-icone.png android/app/src/main/res --cor '#7FD6F5' --web icones/icone-192.png icones/icone-512.png --loja loja/icone-512.png`.

O antigo `docs/arte/icones/gerar-icones.js` (ícones desenhados em SVG) sobrescreve os novos; não rodar.

## Arte dos mercados

Os 12 mercados têm ilustração, em `versao-b-quitanda-zen/mercados/*.webp`, ligadas pelo campo `img` em `FEIRAS`. Aparecem no topo dos avisos de viagem, chegada e feira concluída, no cartão do mercado na tela inicial, na lista e nos pontos do mapa e na faixa do tabuleiro. Mercados sem `img` continuam com o emoji. O `app-android/scripts/copy-web.js` copia a pasta para o app. As imagens originais e os estilos de arte estão em `docs/arte/referencias/` e `docs/arte/lista-de-arte.md`.

## Arte dos itens

Os itens do tabuleiro com arte ficam em `versao-b-quitanda-zen/itens/<código>.webp` (256 px, fundo transparente) e são listados em `ITEM_ART`, no `index.html`; os demais continuam com o emoji. A imagem aparece no tabuleiro, nos pedidos, nos cestos, na prateleira da tela inicial, nas receitas e ao arrastar. Para recortar arte nova: `docs/arte/itens/recortar_itens.py` (rembg). Para marcar o que já está pronto na lista de arte: `docs/arte/atualizar_status.py`.

**Botão voltar do Android** (Quitanda): o plugin `@capacitor/app` entrega o botão ao jogo (`voltar()` no `index.html`). Ele fecha a camada da frente (vinheta, aviso com botão de fechar ou continuar, painel), volta do tabuleiro para a tela inicial e, na tela inicial, sai do app no segundo toque em até 2 s. Anúncio simulado só fecha depois da contagem. A Rota das Feiras ainda não tem isso.

**Álbum de ingredientes** (aba "Ingredientes" do Caderno de Receitas): mostra as 13 linhas × 8 níveis; tudo o que passa pelo tabuleiro entra (`S.seen`, 1 = novo, 2 = visto; o nível 1 já entra como visto). Um ponto no botão Receitas avisa quando há novidade, e o Caderno abre direto nessa aba. Completar os 8 níveis de uma linha rende +100 XP e +150 moedas, com o bônus da volta (`ALB_XP`, `ALB_CO`, `S.albumDone`). Saves antigos começam com o que estiver no tabuleiro.

## Decisões importantes

**Quitanda Zen (v0.5)**
- 13 linhas de itens com 8 níveis, quase todos brasileiros; cada mercado usa 4 linhas (2 no primeiro, 3 no segundo).
- Meta por mercado: 30 + 3 × parada clientes (teto 60). Voltas infinitas, com +10% de XP e moedas por volta.
- Cestos: 10 cargas. No primeiro mercado começam cheios e recarregam 1 carga a cada 20 s; a recarga sobe 15 s por parada até 90 s, e nos mercados seguintes os cestos começam vazios.
- Fusão tripla só por escolha: arrastar passando por cima de um item igual e soltar em outro igual vizinho.
- Anúncios de tela cheia, "Dobrar" e convites à loja só a partir do segundo mercado.
- Loja vende só o que economiza tempo (kits, moedas, Recarga, Junta-tudo, remover anúncios). Melhorias, ampliações e decorações são só por moedas do jogo.
- Tutorial de 3 passos no tabuleiro (juntar, entregar, colher); vinheta inteira só na 1ª abertura do dia; música calma gerada no jogo.

**Rota das Feiras (v0.1)**
- Ver-o-Peso com 6 fases e o chefe Maré cheia; linhas Açaí, Peixe e Jambu/Tucupi com 5 níveis.
- Cada toque no cesto gasta 1 turno; juntar e entregar são de graça. 3 ⭐ com metade dos turnos sobrando.
- Caixote e mofo; Martelo, Caldeirão e +3 Turnos (máximo 2 ferramentas por fase); Diário com 7 cartões; Selo Força do Açaí.
- Balanceamento inicial com robô: fases 1 a 5 quase sempre vencidas; fase 6 e chefe entre 55% e 65%.
- Loja com kits de US$ 0,50 a 9,99. Selos e cartões nunca são vendidos.

**Regras comuns**
- Português e inglês no mesmo arquivo (idioma do aparelho, botões na tela inicial e em Ajustes). Nomes de mercados, cidades, personagens e pratos típicos ficam em português, com explicação curta em inglês.
- Todas as compras são **simuladas**: aparece uma confirmação e nada é cobrado. Na Quitanda, os anúncios usam os IDs de **teste** do AdMob.

## Pendências e riscos

1. **Arte dos itens:** os itens ainda são emojis provisórios, alguns pouco fiéis (caju aparece como maçã). A lista de arte e os prompts estão em `docs/arte/`.
2. **Publicação da Quitanda** (passo a passo em `docs/loja-play/quitanda-zen/LEIAME.md`):
   - Feito: build de publicação (`PUBLICACAO=1` no `copy-web.js`: sem Loja paga e sem ferramentas de teste), workflow do AAB, política de privacidade, textos, capturas e respostas da Play Console.
   - Falta: criar a chave de upload e os segredos `QUITANDA_*`; criar os blocos do AdMob e as variáveis `ADMOB_*`; teste fechado de 14 dias.
   - Depois: integrar Google Play Billing e religar a Loja (`PUB.loja`).
3. **Rota das Feiras:**
   - Só 7 fases.
   - Casas do tabuleiro pequenas no celular (26 a 29 px): é o principal ponto do relatório de avaliação ainda não resolvido.
   - Moedas com pouco uso.
4. **Textos culturais** (Diário, mercados, glosas em inglês) precisam de revisão local e de falante nativo de inglês.
5. **Nome e marca:** verificar "Quitanda" e "Bentevi" no INPI e nas lojas.
6. **Testes reais:** nada foi testado em celular real nem com jogadores; o canto do bem-te-vi e a música não foram ouvidos por quem desenvolveu.

## Ler Brincando (repositório LerBrincando)

- Versão 1.3.1, com as 11 melhorias da avaliação (instruções na tela, bolinhas de progresso, ajuda 🛟, adiantar ⏩, revisão no fim da fase, Área técnica separada, resumo para os pais, portão com perguntas sorteadas) e o ícone novo.
- Testes: `node ferramentas/testar.js` (V1–V12) e `node ferramentas/testes_funcionais.js`.
- APK: **Actions → App Android → Run workflow** (não roda sozinho a cada push).
- As etiquetas de instrução e a tela "Conheça o mapa" são só visuais: para a Lili falar esses textos, é preciso incluí-los no Banco de Áudio e rodar `gerar_audios`.
- O manual completo é o `LEIAME.md` do próprio repositório.

## Como o trabalho foi conduzido

- Desenvolvimento em branch (`ccr-c071cb1f-ws02kc` na feira-viva; `claude/...` no LerBrincando), com pull request e merge na `main` a cada entrega aprovada pelo dono do projeto.
- Mudanças de balanceamento e de regra são registradas no `docs/design-de-jogo.md`, em seções de revisão numeradas.
