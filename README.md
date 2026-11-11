# Feira Viva

Jogo mobile 2D de merge com tema de feiras e mercados brasileiros, planejado em duas versões:

- **Versão A · Rota das Feiras**: puzzle com fases, turnos limitados e um mapa do Brasil com mercados reais. Receita por compras no app.
- **Versão B · Quitanda Zen**: passatempo relaxante, sem derrota e com progressão contínua e sem fim. Receita por anúncios.

## Conteúdo

| Pasta | O que tem |
|---|---|
| `docs/design-de-jogo.md` | Documento de design completo das duas versões |
| `docs/mockups/` | 7 telas de sugestão em SVG; abra `index.html` para ver todas |
| `docs/arte/` | Lista de arte (mercados, itens, personagens) em Markdown e CSV, com prompts em inglês |
| `versao-a-rota-das-feiras/` | Protótipo de teste da Versão A (Ver-o-Peso, 6 fases e chefe) em HTML5 |
| `app-android-rota/` | App Android da Versão A (Capacitor), sem monetização; o APK é gerado na aba Actions |
| `app-android/` | App Android da Versão B (Capacitor) com anúncios de teste do AdMob; o APK é gerado na aba Actions |
| `versao-b-quitanda-zen/` | Protótipo jogável da Versão B em HTML5, em português e inglês |

## Como jogar o protótipo

Abra `versao-b-quitanda-zen/index.html` no navegador, de preferência no celular. Não precisa instalar nada.

O jogo abre no idioma do navegador. Para escolher, use os botões na tela inicial, em **Ajustes**, ou o endereço com `?lang=en` ou `?lang=pt`.

Para publicar online com GitHub Pages: **Settings → Pages → Deploy from a branch → `main` / root**. O jogo fica em `https://<usuario>.github.io/<repositorio>/versao-b-quitanda-zen/`.

## Versão A · protótipo de teste

Abra `versao-a-rota-das-feiras/index.html` (ou, com o GitHub Pages ligado, `https://<usuario>.github.io/<repositorio>/versao-a-rota-das-feiras/`). Segue o marco "Versão A mínima" do documento de design:

- **Ver-o-Peso** com 6 fases e o chefe **Maré cheia**; turnos limitados (cada toque num cesto gasta 1 turno; juntar e entregar são de graça) e 1 a 3 ⭐ conforme os turnos que sobram.
- **Linhas** Açaí, Peixe e Jambu/Tucupi, com 5 níveis; fusão tripla só por escolha do jogador.
- **Obstáculos:** caixote e mofo; **ferramentas:** Martelo e Caldeirão (máximo de 2 por fase), compradas com moedas do jogo.
- **Diário de Viagem** com 7 cartões ("Saiba mais" opcional) e **Selo de Domínio** Força do Açaí (+3 turnos).
- **Mapa do Brasil** com os 12 mercados; só o Ver-o-Peso está aberto neste teste.
- **Painel do teste** em Ajustes: tentativas, vitórias, derrotas e taxa de derrota por fase. **Modo teste** libera todas as fases.
- Sem anúncios e sem compras. Textos dos cartões a validar com pesquisa e revisão local.

## Estado atual

Protótipo da Versão B (revisão v0.4, sem fim e em dois idiomas):

- **Tela inicial** com a banca, o Seu Zé, presente diário, ajuda e escolha de idioma.
- **Mapa do Brasil** com estados e regiões em cores e um ícone por mercado. Cada feira pede de 30 a 60 clientes; a rota tem 12 mercados por volta e voltas infinitas.
- **Viagem animada** de ônibus ou avião pelo mapa até o próximo mercado.
- **Turma da Feira:** 28 personagens, com amizade sem limite.
- **13 linhas de itens com 8 níveis**, quase todos brasileiros; fusão tripla só por escolha do jogador.
- **Cestos lentos:** 10 cargas, 1 a cada 90 s, vazios a cada mercado novo; anúncios simulados dão cargas, dobram prêmios e abrem o baú.
- **Melhorias** com imagem e o efeito de agora e depois; tela **Como jogar** com cada elemento explicado.
- **Versão em inglês** com o nome internacional *Quitanda: Merge Across Brazil*.
- O progresso fica salvo apenas no navegador de quem joga. Em **Ajustes** há métricas de teste e um modo que acelera os cestos.

Os números de balanceamento ficam no bloco `DADOS`, no topo do script, e ainda não foram testados com jogadores.

**Vinheta Bentevi:** ao abrir, o jogo mostra a vinheta da desenvolvedora: o bem-te-vi desce planando, pousa no galho e canta o próprio nome, enquanto o logo aparece sílaba por sílaba. O canto é sintetizado no próprio jogo (amostra em `docs/arte/bentevi-canto.wav`). Um toque pula a vinheta; para pular nos testes, use `?intro=0`.

**Créditos:** contornos dos estados do pacote [@svg-maps/brazil](https://www.npmjs.com/package/@svg-maps/brazil), licença [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/), simplificados para o jogo.

## Próximos passos

1. Testar a Versão B com 10 a 20 pessoas do público-alvo.
2. Portar o núcleo para Unity ou Godot.
3. Integrar SDKs reais de anúncios e compras.
4. Produzir a arte final.
