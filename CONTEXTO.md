# Contexto do projeto (para retomar o trabalho)

Resumo do estado atual, das decisões tomadas e de como continuar. Atualizado em 26/11/2026 (Rota das Feiras: 4º mercado, Recife, e arte própria de Manaus).

## O que é

Três jogos mobile em português, todos feitos em HTML5 de arquivo único e empacotados como app Android com Capacitor:

| Jogo | Repositório e pasta | Público e proposta | Receita | Estado |
|---|---|---|---|---|
| **Quitanda Zen** (Versão B da Feira Viva; nome internacional *Quitanda: Merge Across Brazil*) | `feira-viva` · `versao-b-quitanda-zen/` | Passatempo de juntar itens, sem derrota, viajando por 12 mercados do Brasil em voltas infinitas | Anúncios (AdMob) + compras (simuladas) | v1.1.0 (código 5) em teste fechado na Play Store |
| **Rota das Feiras** (Versão A da Feira Viva) | `feira-viva` · `versao-a-rota-das-feiras/` | Puzzle de fusão com turnos contados, fases, estrelas e chefe | Compras (simuladas), sem anúncios | Protótipo de teste v0.4 (Ver-o-Peso, Manaus, Salvador e Recife), APK de teste |
| **Ler Brincando** | `LerBrincando` (raiz) | Alfabetização pelo método fônico, 5 a 7 anos | Nenhuma (sem anúncios, compras ou rastreadores) | v1.3.1 |

A desenvolvedora se chama **Bentevi Apps** (antes, Bentevi Games). Desde 25/11/2026 a vinheta de abertura é a mesma em todos os apps (Quitanda, Rota, Ler Brincando e Teto): o bem-te-vi chega voando e batendo as asas, freia, pousa no galho e canta; embaixo do nome aparece "apps". A arte veio do Nano Banana e o código fica em `vinheta.montar`/`vinheta.quadro` (bloco `VINHETA_IMG` + motor, antes de `let introState`); fontes, recortes, prompts e o vídeo em `docs/arte/vinheta/`. O canto é uma gravação real (0,84 s), isolada de um vídeo com filtro de ruído espectral e embutida em base64 nos dois `index.html` (`CANTO`); se o aparelho não decodificar, volta o canto sintetizado (`birdSynth`). O bico e as letras "bem · te · vi" seguem o tempo das notas da gravação (`CALL`). Arquivos em `docs/arte/bentevi-canto.wav` e `.mp3`.

## Onde está cada coisa (feira-viva)

| Caminho | Conteúdo |
|---|---|
| `versao-b-quitanda-zen/index.html` | O jogo Quitanda Zen inteiro (HTML, CSS e JS num arquivo). Dados de balanceamento no bloco `DADOS`, no topo do script |
| `versao-a-rota-das-feiras/index.html` | O jogo Rota das Feiras inteiro |
| `app-android/` | App Android da Quitanda (Capacitor 8, `com.feiraviva.quitanda`, com AdMob de teste) |
| `app-android-rota/` | App Android da Rota (Capacitor 8, `com.feiraviva.rota`, sem anúncios) |
| `.github/workflows/android.yml` | Compila os dois APKs a cada push que mexa nos jogos ou nos apps; também por **Actions → Apps Android (APKs de teste) → Run workflow** |
| `docs/design-de-jogo.md` | Documento de design das duas versões, com as revisões numeradas (seções 3.9 a 3.15, 4.8 a 4.12) |
| `docs/avaliacoes/` | Relatórios de avaliação como usuário novo (um .docx por jogo, inclusive o Ler Brincando) |
| `docs/arte/` | Lista de arte (`lista-de-arte.md/.csv`: 104 itens, 60 itens da Rota, 12 mercados, 28 personagens, 12 decorações, tudo pronto), prompts do Nano Banana, scripts de recorte, ícones e o canto do bem-te-vi |
| `versao-*/personagens/`, `versao-b-quitanda-zen/decoracao/` | Arte dos personagens (WebP 192 px) e da decoração da banca (WebP 128 px) usada nos jogos |
| `docs/expansao/quitanda-sugestao-de-expansao.pdf` | Proposta de 10 mercados novos, com linhas regionais, receitas, personagens e trilhas |
| `docs/marketing/instagram/` | Material do Instagram da Bentevi (guia em `GUIA.md`) |
| `docs/arte/icones/` | Artes dos ícones (`quitanda-arte.png`, `rota-arte.png`, `ler-brincando/arte-icone.png`), ícones 512 px da loja e o gerador `gerar_icones_arte.py` |
| `docs/mockups/` | Telas de sugestão em SVG do início do projeto |
| `docs/loja-play/quitanda-zen/` | Página da Play Store da Quitanda: textos pt-BR e en-US, capturas, gráfico de destaque, ícone, respostas da Play Console e passo a passo (`LEIAME.md`) |
| `versao-b-quitanda-zen/privacidade.html` | Política de privacidade da Quitanda (pt e en), publicada pelo GitHub Pages |
| `.github/workflows/quitanda-aab.yml` | Gera o AAB assinado da Quitanda para a Play Store (só manual: **Actions → Quitanda · AAB para a Play Store → Run workflow**; a opção "compras" liga a Loja com dinheiro real) |
| `app-android*/android/app/src/main/java/com/feiraviva/compras/ComprasPlugin.java` | Plugin próprio de compras pela Google Play (Play Billing 8.0.0), igual nos dois apps; registrado no `MainActivity` |
| `docs/loja-play/compras-google-play.md` | Como funciona o motor de compras, IDs e preços dos produtos e o passo a passo na Play Console |

## Como rodar e testar

- **Navegador:** abrir o `index.html` de cada versão. Parâmetros úteis: `?lang=en` ou `?lang=pt` (idioma) e `?intro=0` (pula a vinheta).
- **Web publicada (GitHub Pages da `main`):** `https://jecal17-cmd.github.io/feira-viva/versao-b-quitanda-zen/` e `.../versao-a-rota-das-feiras/`.
- **APKs:** aba **Actions**, execução mais recente de *Apps Android (APKs de teste)*, em **Artifacts**: `quitanda-apk-teste` e `rota-das-feiras-apk-teste` (APK de debug, instala direto no celular). Desde 21/11/2026 os dois saem assinados com a **chave fixa de teste** (`chave-teste/apk-teste.keystore`): o APK novo instala **por cima** do antigo, sem desinstalar. Só a primeira instalação depois dessa mudança exige desinstalar uma vez.
- **Ferramentas de teste dentro dos jogos:**
  - Quitanda: em **Ajustes**, 5 toques no número da versão mostram o Modo teste, o painel de métricas e "Remover anúncios (simulado)".
  - Rota: em **Ajustes** há o Modo teste (libera fases e oferece +5 turnos) e o painel por fase (tentativas, vitórias, derrotas, taxa de derrota).
- **Testes automatizados:** não há suíte no repositório. Os testes desta fase foram robôs Playwright descartáveis (bot que joga, fusão tripla por arraste, capturas). Para repetir, abra o HTML com Playwright e chame as funções globais do jogo (`spawn`, `merge`, `deliver`, `travel`, `startPhase` etc.).

## Ícones

As artes vieram do Midjourney (prompts na conversa e em `docs/arte/`) e já trazem a própria moldura (quadrado arredondado) sobre um fundo liso. O script apaga o fundo de fora da moldura. No ícone adaptativo, a arte fica com 78 dp (de 108) sobre uma versão desfocada dela mesma, para encher a máscara do celular sem anel de cor em volta; a prévia com máscaras de vários celulares está em `previa-icones.png`. Ele gera os ícones adaptativos e antigos do Android em todas as densidades, as telas de abertura, o ícone da web (192 px) e o ícone da loja (512 px):

```bash
python docs/arte/icones/gerar_icones_arte.py docs/arte/icones/quitanda-arte.png app-android/android/app/src/main/res --cor '#3E9B5F' --web versao-b-quitanda-zen/icone-192.png --loja docs/arte/icones/quitanda-512.png
python docs/arte/icones/gerar_icones_arte.py docs/arte/icones/rota-arte.png app-android-rota/android/app/src/main/res --cor '#139C8C' --web versao-a-rota-das-feiras/icone-192.png --loja docs/arte/icones/rota-512.png
```

No Ler Brincando, a arte nova (coruja) e os ícones já gerados estão em `docs/arte/icones/ler-brincando/` (pasta `res/` para copiar em `android/app/src/main/res`, `icone-192.png`, `icone-512.png` e `loja-512.png`); copie também o `gerar_icones_arte.py` novo para `ferramentas/`. Comando lá: `python ferramentas/gerar_icones_arte.py icones/arte-icone.png android/app/src/main/res --cor '#7FD6F5' --web icones/icone-192.png icones/icone-512.png --loja loja/icone-512.png`.

O antigo `docs/arte/icones/gerar-icones.js` (ícones desenhados em SVG) sobrescreve os novos; não rodar.

## Arte dos mercados

Os 12 mercados têm ilustração, em `versao-b-quitanda-zen/mercados/*.webp`, ligadas pelo campo `img` em `FEIRAS`. Aparecem no topo dos avisos de viagem, chegada e feira concluída, no cartão do mercado na tela inicial, na lista e nos pontos do mapa e na faixa do tabuleiro. Mercados sem `img` continuam com o emoji. O `app-android/scripts/copy-web.js` copia a pasta para o app. As imagens originais e os estilos de arte estão em `docs/arte/referencias/` e `docs/arte/lista-de-arte.md`.

## Arte dos itens

Os itens do tabuleiro com arte ficam em `versao-b-quitanda-zen/itens/<código>.webp` (256 px, fundo transparente) e são listados em `ITEM_ART`, no `index.html`; os demais continuam com o emoji. A imagem aparece no tabuleiro, nos pedidos, nos cestos, na prateleira da tela inicial, nas receitas e ao arrastar. Para recortar arte nova: `docs/arte/itens/recortar_itens.py` (rembg). O WebP do jogo é normalizado a partir da matriz de 512 px: itens compridos e deitados são girados para a diagonal (`GIRO` define os que sobem pela direita) e todos ocupam 36% da casa (`AREA_ALVO`); `--todos` refaz tudo. Para marcar o que já está pronto na lista de arte: `docs/arte/atualizar_status.py`.

**Botão voltar do Android** (Quitanda e Rota): o plugin `@capacitor/app` entrega o botão ao jogo (`voltar()` no `index.html`). Só sai do app na tela inicial, no segundo toque em até 2 s; em qualquer outra tela volta um passo: fecha a camada da frente (vinheta, viagem, aviso, pop-up), volta ao painel anterior quando um painel foi aberto por cima de outro (`sheetPilha`), volta do tabuleiro para a tela inicial (Quitanda) e, na Rota, da fase abre a Pausa, do mercado vai ao mapa e do mapa à tela inicial. Anúncio simulado só fecha depois da contagem. Detalhes no `design-de-jogo.md`, seção 4.14.

**Trocar de aparelho** (Ajustes): `saveCode()` transforma o progresso inteiro (`S`) num código de texto (`QZ1-<JSON comprimido com deflate-raw em base64url>-<verificação>`, uns 900 caracteres; `QZ0` sem compressão em aparelhos sem `CompressionStream`). No outro aparelho, `readCode()` confere a verificação e a versão, mostra nível, feiras e moedas, e, se a pessoa confirmar, grava em `localStorage` e recarrega. Não usa servidor nem conta.

**Banca da tela inicial** (Quitanda): cena de feira vista de cima, com tampo inclinado; começa vazia e cada linha descoberta vira uma fileira de itens no tampo (sem caixotes). A banca ocupa só a altura que sobra, para a tela inicial caber sem rolar. As 12 decorações ficam no lugar e em tamanho proporcional, sem sombra (balança no tampo, rádio no banco, relógio no poste), e o toldo cobre luzinhas e bandeirinhas (`bancaHtml`, `DECOR_POS`). **Arranjo dinâmico** (`arranjoBanca`, igual na Rota): conforme as linhas descobertas aumentam, o jogo escolhe quantas ficam lado a lado por fileira (2 a 6) e o quanto o tampo se aprofunda, para tudo caber com os maiores itens possíveis, sem nada atrás do toldo. Detalhes no `design-de-jogo.md`, seções 4.12 e 4.13.

**Detalhes no álbum** (Quitanda e Rota): tocar num ingrediente, numa receita ou num personagem abre um pop-up com arte grande, curiosidade (pt e en), fila de níveis da linha, onde encontrar e, conforme o caso, receitas, fãs, moedas por pedido ou a ficha da profissão (`verIng`, `verRec`, `verCast`/`verCli`; textos nos blocos `INFO`, `REC_INFO` e `BIO`). Na Rota, o Álbum ganhou a aba **Clientes** com os 28 personagens, que entram ao fazer o primeiro pedido (`S.met`).

**Álbum de ingredientes** (aba "Ingredientes" do Caderno de Receitas): mostra as 13 linhas × 8 níveis; tudo o que passa pelo tabuleiro entra (`S.seen`, 1 = novo, 2 = visto; o nível 1 já entra como visto). Um ponto no botão Receitas avisa quando há novidade, e o Caderno abre direto nessa aba. Completar os 8 níveis de uma linha rende +100 XP e +150 moedas, com o bônus da volta (`ALB_XP`, `ALB_CO`, `S.albumDone`). Saves antigos começam com o que estiver no tabuleiro.

**Pedidos relâmpago e anúncios** (Quitanda): o prazo para de contar durante qualquer anúncio, real ou simulado (`rushPausa`/`rushVolta` em `showAd`); ao fechar, o prazo dos relâmpagos ainda ativos é estendido pelo tempo do anúncio. Painéis e menus não pausam.

**Música dos mercados** (Quitanda): cada mercado tem uma trilha calma em loop (`versao-b-quitanda-zen/musica/NN.ogg`, Opus 48 kbps, 30 a 48 s), com um toque discreto da música do lugar: carimbó (Belém), toada de boi (Manaus), ijexá (Salvador), ciranda (Recife), baião com rabeca (Fortaleza), guarânia (Campo Grande), choro (São Paulo), viola caipira (BH), xote (Rio), milonga (Porto Alegre), valsa açoriana (Florianópolis) e polca (Curitiba). São geradas por `docs/arte/musica/trilhas_mercados.py`. O objeto `Musica` toca a do mercado atual, troca com fade ao viajar e, se o arquivo não carregar (jogo aberto direto do disco), volta à melodia procedural antiga. O `copy-web.js` copia a pasta `musica/`.

**Volume** (Quitanda e Rota): em Ajustes, Som e Música têm cada um uma barra de 0 a 100% (`S.opts.vSom`, `S.opts.vMus`, de 0 a 1), além do botão Ligado/Desligado. Os toques, as moedas e o canto do bem-te-vi usam `vSom()`; a música usa `vMus()` e muda na hora (`Musica.volume()`). A música não depende mais do botão Som.

**Instagram:** o material de lançamento da Bentevi (Quitanda Zen em PT/EN e Ler Brincando em PT) está em `docs/marketing/instagram/`, com o guia em `GUIA.md`.

**Sons de dinheiro** (Quitanda e Rota, `Sfx.tocar`): moedinhas (A3) a cada pedido entregue, punhado de moedas (B4) no baú e no bônus do álbum, caixa registradora (C4) ao concluir a feira (Quitanda) ou a fase (Rota). Embutidos em base64 no `index.html`; respeitam a opção Som. Gerados por `docs/arte/musica/sons_dinheiro.py`; os MP3 finais estão em `docs/arte/musica/sons/`. O Teto usa o carimbo (F) ao registrar gasto e as moedinhas ao registrar entrada.

**Novidades do dia, avisos e anúncios** (Quitanda, revisão 4.11 do design): na primeira abertura do dia, um aviso animado (`boasVindas()`) mostra o presente do dia, os anúncios com prêmio renovados e os cestos cheios; o botão pega o presente. No app Android, ao sair do jogo, um aviso no celular é agendado para quando os cestos encherem (`Avisos`, plugin `@capacitor/local-notifications`, ícone `res/drawable/ic_stat_quitanda.xml`; opção "Avisos" em Ajustes). Os anúncios de tela cheia ficaram mais espaçados (`INTER_*` no bloco DADOS). Na tela de Melhorias, saldo fixo no topo e bolinhas de nível (`pips`). Pedidos de receita mostram o nome do cliente e um selinho 📖; o aviso de feira concluída lista as receitas descobertas no mercado (`recFeiraHtml()`). O `package-lock.json` do `app-android` ainda não lista o plugin novo (sem internet na sessão): os workflows caem em `npm install` quando o `npm ci` falha; vale rodar `npm install` no `app-android` uma vez e enviar a lista travada atualizada. O mesmo vale para o `app-android-rota`, que ganhou o `@capacitor/app` em 26/11/2026.

**Valor dos pedidos:** cada pedido mostra quantas moedas paga (`orderPay(o)`, a mesma conta que `deliver()` credita). Na Quitanda: itens (`COV`) com o bônus da volta, em dobro no relâmpago dentro do prazo e com +30 da receita ainda não descoberta. Na Rota: `ORDER_COIN` (2) × nível de cada item.

## Rota das Feiras: mercados, arte, álbum e troca de aparelho

**Dois mercados (v0.2):** Ver-o-Peso (Belém) e Mercado Adolpho Lisboa (Manaus), com 7 fases cada. Manaus abre ao vencer o chefe do Ver-o-Peso. As fases ficam numa lista só (`PHASES`, campo `m` = mercado; as de Manaus são as posições 7 a 13), e o índice da lista é a chave do progresso, por isso os saves antigos continuam valendo. Manaus tem linhas próprias (Peixes do rio, Mandioca, Frutas), o chefe Encontro das Águas (rios sobem nas colunas das pontas) e o Selo Guaraná (+1 turno a cada 10 fusões). `OPEN_M` diz quantos mercados estão abertos; detalhes no `design-de-jogo.md`, seção 3.11.

**Terceiro mercado (v0.3): Feira de São Joaquim (Salvador)**, aberto ao vencer o chefe de Manaus. Fases nas posições 18 a 24 de `PHASES` (depois das 4 do Natal); `unlocked()` agora olha a fase anterior do mesmo mercado e, na primeira, o chefe do mercado anterior. Linhas Fradinho (`ff`), Camarão (`cm`) e Coco (`cc`), com arte 3D própria. Regras novas: **sol forte** (faixa de 2 colunas; item de nível 3+ parado ali 5 turnos perde 1 nível; nas fases 5, 6 e chefe o sol anda 1 coluna a cada 4 turnos; `cfg.sun`, `inSun`, `sunny`, `salvadorTick`), **Toldo** (ferramenta de 🪙 100, sombra 2 × 2 na fase; `P.shade`), **engradado de coco** (`o:'engr'`, 2 fusões para abrir), **pedido da Dona Dadá** (`cfg.dada`, 2 itens, prazo de 8 turnos, +2 turnos e moedas em dobro; meta `dada`) e o chefe **Chegada do saveiro** (3 engradados a cada 5 turnos pela esquerda). Selo Dendê: a 1ª fusão da fase sobe +1 nível. Os cartões do Diário guardam a fase em `ph` (`cardOf(i)`). Detalhes e balanceamento no `design-de-jogo.md`, seção 3.15; prompts da arte em `docs/arte/prompt-nano-banana-salvador.md`.

**Quarto mercado (v0.4): Mercado de São José (Recife)**, aberto ao vencer o chefe de Salvador. Fases nas posições 25 a 31 de `PHASES`; `OPEN_M=4`. Linhas Carne de sol (`cs`), Queijo coalho (`qc`) e Cana (`cn`; a Macaxeira prevista no design foi trocada porque Manaus já tem Mandioca), com arte 3D própria. Regras novas, todas de movimento: **roda de ciranda** (bloco 3 × 3; a cada 3 turnos as 8 casas em volta do centro giram 1 casa, cada roda com seu sentido; `cfg.ciranda`, `roda()`, `girar()`, `recifeTick`), **encomenda da Maria Flor** (3 itens pedidos um de cada vez, o próximo escondido, +1 turno por item, moedas em dobro; `cfg.flor`, `newFlor`, `florNow`, meta `flor`), chefe **Galo da Madrugada** (a cada 5 turnos a borda inteira gira 1 casa; `BORDA`, `fxGalo`) e o **Selo Carne de Sol** (Despensa com 2 vagas fora do tabuleiro: arrastar ou tocar para guardar; tocar na vaga e depois numa casa vazia ou num pedido; `P.desp`, `guardar`, `tirar`). O sol forte volta nas fases 3 e 6. Balanceamento com robô, cartões do Diário e curiosidades no `design-de-jogo.md`, seção 3.16; prompts da arte em `docs/arte/prompt-nano-banana-recife.md`. Na mesma leva, os 15 itens de Manaus ganharam arte própria (antes eram cópias da Quitanda).

**Música e banca:** a Rota toca a trilha do mercado atual (`versao-a-rota-das-feiras/musica/01.ogg` a `04.ogg`, cópias das da Quitanda; o `copy-web.js` copia a pasta). A tela inicial mostra a banca da Quitanda (`bancaHtml()`, toldo verde-água, sem decorações), que enche com o Álbum, com o mesmo arranjo dinâmico da Quitanda (`arranjoBanca`).

A Versão A usa as mesmas ilustrações dos 12 mercados (`versao-a-rota-das-feiras/mercados/`, campo `img` em `MARKETS`): no mapa (os mercados abertos coloridos, os demais em cinza com cadeado), na lista do mapa e no topo da tela de cada mercado. Os itens dela são próprios (5 níveis); a arte dos 60 fica em `versao-a-rota-das-feiras/itens/` e todos estão em `ITEM_ART`, com arte própria em todos os mercados. A lista de arte tem a seção "Itens da Rota das Feiras" (tipo `item-rota`). O botão **Álbum** da tela inicial mostra os 60 ingredientes, agrupados por mercado (`S.alb`, `S.albDone`); linha completa rende +100 moedas. Em Ajustes, **Trocar de aparelho** gera e restaura um código `RF1-…`, igual ao da Quitanda. Caixote e mofo têm arte em pixel art com animação de remoção (`versao-a-rota-das-feiras/obstaculos/`, `fxObs()`); todo caixote guarda um item, que fica na casa ao quebrar (`abrir()`, seção 3.14 do design). Os clientes dos pedidos são sorteados entre os 28 personagens (`FACES`, com ilustração por `fc()`). O `app-android-rota/scripts/copy-web.js` copia as pastas `mercados/`, `itens/`, `personagens/`, `musica/` e `obstaculos/` (caixote, mofo, engradado, sol, saveiro, roda de ciranda e Galo).

## Eventos (Natal 2026) nos dois jogos

Bloco `EVENTOS` no `index.html` de cada jogo (mesmo código): lista de eventos com datas (horário de Brasília, relógio do aparelho), botão flutuante com contagem regressiva nas telas iniciais, pop-up do evento e 4 prêmios exclusivos por evento, guardados para sempre em `S.ev.got` (sobrevivem a "Recomeçar do zero"). Primeiro evento: **Natal na Feira, de 10/12/2026 a 26/12/2026** (Panetone, Rabanada, Farofa natalina e Enfeites de Natal). Na Rota as etapas são 4 fases especiais (`PHASES` com `ev` e `evn`); na Quitanda, 4 metas de jogo. **Para criar o Carnaval:** acrescentar um item a `EVENTOS` (e, na Rota, 4 fases). Testar fora das datas: abrir o jogo com `?evento=natal26`. Detalhes na seção 3.13 do `design-de-jogo.md`.

## Decisões importantes

**Quitanda Zen (v0.5)**
- 13 linhas de itens com 8 níveis, quase todos brasileiros; cada mercado usa 4 linhas (2 no primeiro, 3 no segundo).
- Meta por mercado: 30 + 3 × parada clientes (teto 60). Voltas infinitas, com +10% de XP e moedas por volta.
- Anúncios de tela cheia: a partir de 10 min de jogo, no mínimo 6 min entre eles, a cada 6 pedidos ou na chegada a um mercado; nunca logo ao abrir o app nem logo depois de um anúncio com prêmio.
- Cestos: 10 cargas. No primeiro mercado começam cheios e recarregam 1 carga a cada 20 s; a recarga sobe 15 s por parada até 90 s, e nos mercados seguintes os cestos começam vazios.
- Fusão tripla só por escolha: arrastar passando por cima de um item igual e soltar em outro igual vizinho.
- Anúncios de tela cheia, "Dobrar" e convites à loja só a partir do segundo mercado.
- Loja vende só o que economiza tempo (kits, moedas, Recarga, Junta-tudo, remover anúncios). Melhorias, ampliações e decorações são só por moedas do jogo.
- Tutorial de 3 passos no tabuleiro (juntar, entregar, colher); vinheta inteira só na 1ª abertura do dia; música calma gerada no jogo.

**Rota das Feiras (v0.4)**
- Ver-o-Peso com 6 fases e o chefe Maré cheia; linhas Açaí, Peixe e Jambu/Tucupi com 5 níveis.
- Manaus com 6 fases e o chefe Encontro das Águas; linhas Peixes do rio, Mandioca e Frutas; Selo Guaraná.
- Salvador com 6 fases e o chefe Chegada do saveiro; linhas Fradinho, Camarão e Coco; sol forte (que anda), Toldo, engradado de coco, pedido da Dona Dadá; Selo Dendê.
- Recife com 6 fases e o chefe Galo da Madrugada; linhas Carne de sol, Queijo coalho e Cana; roda de ciranda, encomenda da Maria Flor (um item de cada vez), borda que gira no chefe; Selo Carne de Sol (Despensa).
- Cada toque no cesto gasta 1 turno; juntar e entregar são de graça. 3 ⭐ com metade dos turnos sobrando.
- Caixote e mofo; Martelo, Caldeirão e +3 Turnos (máximo 2 ferramentas por fase); Diário com 7 cartões; Selo Força do Açaí.
- Balanceamento inicial com robô: fases 1 a 5 quase sempre vencidas; fase 6 e chefe entre 55% e 65%.
- Loja com kits de US$ 0,50 a 9,99. Selos e cartões nunca são vendidos.

**Regras comuns**
- Português e inglês no mesmo arquivo (idioma do aparelho, botões na tela inicial e em Ajustes). Nomes de mercados, cidades, personagens e pratos típicos ficam em português, com explicação curta em inglês.
- Compras: os dois jogos têm o motor de compras pela Google Play (bloco `COMPRAS` no `index.html` e plugin nativo `ComprasPlugin.java`). Ele só liga com `COMPRAS=play` (no AAB da Quitanda, marcando "compras" no workflow); no navegador e nos APKs de teste as compras continuam **simuladas** (confirmação do jogo, nada é cobrado). Passo a passo e IDs dos produtos em `docs/loja-play/compras-google-play.md`. Na Quitanda, os anúncios usam os IDs de **teste** do AdMob.

## Pendências e riscos

1. **Play Console:** a versão 1.1.0 (código 5) avisou que deixa de fora 19.560 aparelhos. Nada no código explica (só entrou o `@capacitor/app`, sem permissões nem recursos novos); falta ver o motivo em **Catálogo de dispositivos → Excluídos**.
2. **Publicação da Quitanda** (passo a passo em `docs/loja-play/quitanda-zen/LEIAME.md`):
   - Feito: build de publicação (`PUBLICACAO=1` no `copy-web.js`: sem Loja paga e sem ferramentas de teste), workflow do AAB, política de privacidade, textos, capturas e respostas da Play Console.
   - Feito também: app criado na Play Console com o pacote `com.feiraviva.quitanda` (um app antigo da conta ficou preso a `feiraviva.myapp` e foi deixado de lado), teste interno e teste fechado, ID de publicidade declarado (publicidade e prevenção de fraudes).
   - Falta: concluir os 14 dias do teste fechado com 12 testadores e pedir a produção; conferir os blocos reais do AdMob (`ADMOB_*`).
   - Compras: o motor está pronto (Play Billing 8). Falta na Play Console: perfil de pagamentos, criar e ativar os 14 produtos `qz_*`, gravar a variável `PLAY_LICENSE_KEY` no GitHub, testadores de licença e gerar o AAB com "compras" marcado. Nunca testado com a Google Play de verdade (só com uma simulada no navegador).
3. **Rota das Feiras:**
   - 28 fases (4 mercados), todas com arte própria.
   - Salvador e Recife não foram testados com jogadores: vigiar se o sol que anda, o pedido da Dona Dadá, a roda de ciranda e a encomenda "um de cada vez" da Maria Flor ficam claros sem ler o tutorial. O chefe do Recife é o mais difícil até agora (43% no robô).
   - Casas do tabuleiro pequenas no celular (26 a 29 px): é o principal ponto do relatório de avaliação ainda não resolvido.
   - Moedas com pouco uso (o Toldo de Salvador, só por moedas, é o primeiro uso novo).
   - Eventos: os prêmios ainda não são linhas de itens jogáveis (só aparecem na banca, na coleção e, na Quitanda, no Caderno de Receitas, com +1% de XP); arte própria do Natal e revisão dos textos pendentes; as metas da Quitanda não foram medidas com jogadores.
4. **Textos culturais** (Diário, mercados, glosas em inglês e as curiosidades e fichas do álbum) precisam de revisão local e de falante nativo de inglês.
5. **Nome e marca:** verificar "Quitanda" e "Bentevi" no INPI e nas lojas.
6. **Testes reais:** nada foi testado em celular real nem com jogadores; a música não foi ouvida por quem desenvolveu (o canto do bem-te-vi agora é uma gravação enviada pela dona do projeto).

## Ler Brincando (repositório LerBrincando)

- Versão 1.3.1, com as 11 melhorias da avaliação (instruções na tela, bolinhas de progresso, ajuda 🛟, adiantar ⏩, revisão no fim da fase, Área técnica separada, resumo para os pais, portão com perguntas sorteadas) e o ícone novo.
- Testes: `node ferramentas/testar.js` (V1–V12) e `node ferramentas/testes_funcionais.js`.
- APK: **Actions → App Android → Run workflow** (não roda sozinho a cada push).
- As etiquetas de instrução e a tela "Conheça o mapa" são só visuais: para a Lili falar esses textos, é preciso incluí-los no Banco de Áudio e rodar `gerar_audios`.
- O manual completo é o `LEIAME.md` do próprio repositório.
- **Identidade visual própria (prompts prontos, 21/11/2026):** `docs/arte/ler-brincando/prompt-nano-banana-ler-brincando.md` traz 29 grades para o Nano Banana 2 Lite (Lili em 9 poses, 12 avatares, 8 emblemas dos mundos, enfeites e lojinha, 12 medalhas, 16 ícones da interface e as 363 palavras em 23 grades, na ordem de ensino), todas com a arte do ícone (`referencia-lili.png`) como referência de estilo, para trocar o OpenMoji. `grades.json` diz o destino de cada casa; `gerar_prompts.py <data.json do LerBrincando>` refaz tudo quando entrarem palavras novas. Falta gerar as imagens e ligá-las no jogo (repositório LerBrincando).

## Como o trabalho foi conduzido

- Desenvolvimento em branch (`ccr-c071cb1f-ws02kc` na feira-viva; `claude/...` no LerBrincando), com pull request e merge na `main` a cada entrega aprovada pelo dono do projeto.
- Mudanças de balanceamento e de regra são registradas no `docs/design-de-jogo.md`, em seções de revisão numeradas.

## Arte gerada com o Nano Banana (novembro de 2026)

- Prompts em `docs/arte/prompt-nano-banana.md` e `prompt-nano-banana-2.md` (3D dos itens, personagens, mercados). As grades geradas ficam em `docs/arte/referencias/grade-*.jpg`, e `docs/arte/itens/grades.json` diz o que é cada casa.
- Itens e decoração: `fatiar_grade.py` corta a grade em casas e `recortar_itens.py` tira o fundo (rembg) e normaliza. Sem o rembg instalado, o script usa `mascara_fundo_branco` (branco ligado à borda e vãos grandes de branco puro viram fundo).
- **Arte toda no estilo novo (16/11, fim da tarde):** tudo o que tinha entrado antes de 16/11 foi refeito com `prompt-nano-banana-3.md`: 52 itens da Quitanda em 4 grades (`grade-refazer-1..4.jpg`, lotes `refazer-1..4` no `grades.json`; a sardinha e o peixe também servem de `pe-1` e `pe-2` da Rota) e 9 mercados (todos menos 03, 05 e 06, que já eram de hoje), nas pastas `mercados/` dos dois jogos. O saleiro (`te-1`) foi recortado sem tirar os brancos internos.
- Personagens: `fatiar_por_silhueta.py <grade> <colunas> <linhas> <chave>` recorta pela silhueta (não corta cabeças), trata branco ligado à borda e vãos fechados entre braços e objetos como fundo. Ajustes finos (Dona Geralda, Seu Giuseppe) foram feitos tapando vãos internos transparentes.
- Status da lista: `python docs/arte/atualizar_status.py` (tudo pronto: 12/12 mercados, 104/104 itens, 45/45 da Rota, 28/28 personagens, 12/12 decorações).
- No jogo: personagens com `pf(c)` (Quitanda: pedidos, Turma da Feira, mapa, chegada, Seu Zé da tela inicial) e decorações com `de(i)` (banca e loja). Os scripts `copy-web.js` copiam `personagens/` e `decoracao/`.

## Ícones sem anel de cor

Os ícones dos três apps (Quitanda, Rota, Ler Brincando) foram refeitos sem o anel colorido em volta: a arte ocupa 78 dp de 108 sobre um fundo desfocado da própria arte.

## Teto (repositório Folga)

App Kotlin de controle de gastos, no repositório `Folga`. Usa `Sons.kt` (SoundPool) com o carimbo ao registrar gasto e as moedinhas ao registrar entrada. APK pelo workflow "Build e testes" (artefato `folga-debug-apk`).

## Sessões do Claude Code sobre estes jogos

| Sessão | Assunto |
|---|---|
| Melhorias de consistência do projeto (09/11) | Ler Brincando: sons e consistência |
| Projeto versão B desenvolvimento (10 a 12/11) | Quitanda v0.5, Rota v0.1, avaliações, ícones, primeiro `CONTEXTO.md` |
| Versão AAB e descrição Quitanda Zen (12 a 15/11) | AAB, Play Console (pacote, testes, textos da loja, ID de publicidade), compatibilidade com o Moto G54 |
| Geração de imagens para repositório (13 a 16/11) | Toda a arte (mercados, itens, personagens, decoração), álbum, troca de aparelho, botão voltar, música, sons de dinheiro, Instagram, expansão, ícones, integração da arte nos dois jogos |
| Rota: 4º mercado, Recife (26/11) | Mercado de São José (ciranda, Maria Flor, Galo da Madrugada, Despensa), arte própria de Recife e Manaus, robô de balanceamento |
