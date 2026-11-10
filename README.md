# Feira Viva

Jogo mobile 2D de merge com tema de feiras e mercados brasileiros, planejado em duas versões:

- **Versão A · Rota das Feiras**: puzzle com fases, turnos limitados e um mapa do Brasil com mercados reais. Receita por compras no app.
- **Versão B · Quitanda Zen**: passatempo relaxante, sem derrota e com progressão lenta. Receita por anúncios.

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

- O protótipo da Versão B tem o loop principal, níveis 1 a 50, receitas, decoração, missões diárias e anúncios **simulados**.
- Os itens usam emojis como arte provisória.
- O progresso fica salvo apenas no navegador de quem joga.
- Em **Ajustes** há um painel com métricas de teste (tempo de jogo, XP por minuto, anúncios vistos) e um modo que acelera os cestos.

## Próximos passos

1. Testar a Versão B com 10 a 20 pessoas do público-alvo.
2. Portar o núcleo para Unity ou Godot.
3. Integrar SDKs reais de anúncios e compras.
4. Produzir a arte final.
