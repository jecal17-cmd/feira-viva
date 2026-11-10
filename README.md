# Feira Viva

Jogo mobile 2D de merge com tema de feiras e mercados brasileiros, planejado em duas versões:

- **Versão A · Rota das Feiras**: puzzle com fases, turnos limitados e um mapa do Brasil com mercados reais. Receita por compras no app.
- **Versão B · Quitanda Zen**: passatempo relaxante, sem derrota e com progressão contínua e sem fim. Receita por anúncios.

## Conteúdo

| Pasta | O que tem |
|---|---|
| `docs/design-de-jogo.md` | Documento de design completo das duas versões |
| `docs/mockups/` | 7 telas de sugestão em SVG; abra `index.html` para ver todas |
| `versao-b-quitanda-zen/` | Protótipo jogável da Versão B em HTML5 |

## Como jogar o protótipo

Abra `versao-b-quitanda-zen/index.html` no navegador, de preferência no celular. Não precisa instalar nada.

Para publicar online com GitHub Pages: **Settings → Pages → Deploy from a branch → `main` / root**. O jogo fica em `https://<usuario>.github.io/<repositorio>/versao-b-quitanda-zen/`.

## Estado atual

Protótipo da Versão B (revisão v0.3, mais rápida e sem fim):

- **Tela inicial** com a banca, o Seu Zé, presente diário e atalhos.
- **Mapa do Brasil** com a Rota das Feiras: 12 mercados por volta e voltas infinitas, cada uma com +10% de XP e moedas. Cada feira troca as bancas (linhas de itens) e o tabuleiro chega cheio.
- **Turma da Feira:** 28 personagens (4 que viajam com o jogador e 2 por mercado), com amizade sem limite.
- **13 linhas de itens com 8 níveis** (104 itens), cestos com 20 cargas e recarga de 10 s, combos, pedidos relâmpago, 🧲 Junta-tudo e ⚡ Recarga.
- **Níveis sem teto**, missões e encomendas que se renovam, 25 receitas, melhorias de cestos, ampliações e decoração.
- Anúncios **simulados**; itens e personagens usam emojis como arte provisória.
- O progresso fica salvo apenas no navegador de quem joga.
- Em **Ajustes** (na tela inicial) há um painel com métricas de teste e um modo que acelera os cestos.

Os números de balanceamento ficam no bloco `DADOS`, no topo do script, e ainda não foram testados com jogadores. Os textos curtos de cada mercado precisam de validação local.

## Próximos passos

1. Testar a Versão B com 10 a 20 pessoas do público-alvo.
2. Portar o núcleo para Unity ou Godot.
3. Integrar SDKs reais de anúncios e compras.
4. Produzir a arte final.
