# Bentevi no Instagram · guia de lançamento

Material para abrir o perfil da Bentevi com foco no **Quitanda Zen** (nome internacional: *Quitanda: Merge Across Brazil*). Tudo está em português (`pt-BR/`) e inglês (`en-US/`).

## 1. Antes de postar

- **O jogo precisa estar público.** As peças dizem "Disponível no Google Play" e "Grátis". Se o Quitanda Zen ainda estiver só no teste fechado, segure os posts de lançamento (feed 01, story 1 e story 3) até a versão de produção sair. Os outros podem ir antes, como "em breve".
- **Selo do Google Play.** O selo das peças foi desenhado aqui, imitando o oficial. As regras de marca do Google pedem o selo oficial. Baixe em <https://play.google.com/intl/pt-BR/badges/> (português) e <https://play.google.com/intl/en_us/badges/> (inglês), troque nas peças (o modelo está em `fonte/pecas.html`, função `gp()`) ou cole o selo por cima no editor que você usar.
- **Link na bio:** `https://play.google.com/store/apps/details?id=com.feiraviva.quitanda`. Quando houver mais de um produto, use uma página de links (por exemplo, a própria página do GitHub Pages do projeto).

## 2. Bentevi Games ou Bentevi Software?

**Recomendação: use só "Bentevi" como marca, com a descrição "jogos e apps".**

| Opção | A favor | Contra |
|---|---|---|
| **Bentevi Games** | Fala direto com quem joga; combina com Quitanda e Ler Brincando | O Teto (finanças) não cabe; mudar de nome depois custa seguidores |
| **Bentevi Software** | Cabe tudo | Soa corporativo, de empresa que atende empresas; não atrai jogador nem família |
| **Bentevi (jogos e apps)** | Cabe os três projetos, mantém o calor do nome e não envelhece | Precisa da bio para explicar o que é |

Como os públicos são diferentes, uma divisão que funciona bem:

- **@bentevi (perfil principal):** os jogos, Quitanda Zen e Ler Brincando, e os bastidores do estúdio.
- **Teto:** quando for lançar, ganha perfil próprio. Quem procura app de finanças é outro público, e misturar enfraquece os dois perfis.
- **Ler Brincando:** cabe no perfil principal, num destaque próprio. Por ser educativo e sem fins lucrativos, ajuda a dar credibilidade à marca.

**Sugestões de @** (confira se estão livres): `@bentevi.app`, `@benteviapps`, `@bentevi.studio`, `@bentevistudio`, `@bentevi.br`.

**Nome do perfil:** `Bentevi | Jogos e apps`. O campo de nome entra na busca do Instagram, então o "Jogos e apps" ajuda a ser encontrado.

## 3. Bio (até 150 caracteres)

**Opção A, marca "Bentevi" (recomendada)**

Português:
```
🐦 Estúdio brasileiro de jogos e apps
🧺 Quitanda Zen: junte, entregue e viaje pelos mercados do Brasil
⬇️ Grátis no Google Play
```
Inglês:
```
🐦 Indie studio from Brazil · games & apps
🧺 Quitanda: merge, deliver & travel through Brazil’s markets
⬇️ Free on Google Play
```
Bilíngue, para um perfil só nas duas línguas:
```
🐦 Jogos e apps com cara de Brasil
🌎 Games & apps from Brazil
🧺 Quitanda Zen: junte, entregue, viaje
⬇️ Google Play
```

**Opção B, marca "Bentevi Games"**

Português:
```
🎮 Jogos calmos com cara de Brasil
🧺 Quitanda Zen: sua banca pelos 12 mercados do país
⬇️ Grátis no Google Play
```
Inglês:
```
🎮 Cozy games that feel like Brazil
🧺 Quitanda: run a market stall across 12 real markets
⬇️ Free on Google Play
```

**Uma conta ou duas?** Comece com **uma conta**, com as imagens em português e a legenda nas duas línguas (português primeiro, inglês embaixo). As peças em inglês (`en-US/`) servem para anúncios fora do Brasil, para repostar em outro perfil ou para um perfil em inglês no futuro.

## 4. Identidade visual

| Uso | Cor |
|---|---|
| Fundo creme (o mesmo da vinheta) | `#FFF6D9` |
| Verde-escuro (texto, logotipo) | `#1B4A3F` |
| Verde-folha (Quitanda) | `#2A8F63` |
| Vermelho do toldo | `#E4573D` |
| Amarelo bem-te-vi | `#F2CB25` |
| Amarelo sol (moedas, destaques) | `#F2B33D` |

- **Fontes:** Baloo 2 (títulos) e Nunito (texto), as mesmas do jogo. As duas são gratuitas no Google Fonts.
- **Elementos de marca:** o toldo listrado vermelho e creme no topo das peças, os itens do jogo em 3D "flutuando" com sombra, cartões brancos de cantos bem arredondados e a assinatura "um jogo Bentevi" com o bem-te-vi.
- **Foto de perfil:** `perfil/foto-bentevi.png` (o bem-te-vi sobre amarelo) para a marca Bentevi. Se preferir um perfil só do jogo, use `perfil/foto-quitanda.png` (o ícone do app).
- **Capas dos destaques** (`destaques/`): Quitanda, Como jogar, Mercados, Bentevi e Novidades. Ao criar o destaque, ajuste o recorte para o desenho ficar no centro do círculo.

## 5. O que tem no pacote

| Pasta | Conteúdo | Formato |
|---|---|---|
| `pt-BR/feed/`, `en-US/feed/` | 6 posts: 01 lançamento, 02 como jogar (carrossel de 5), 03 os 12 mercados (carrossel de 5), 04 do limão ao açaí, 05 prazer, Bentevi, 06 recursos | 1080 × 1350 (4:5) |
| `pt-BR/stories/`, `en-US/stories/` | Lançamento (com espaço para o adesivo de link), enquete dos mercados (com espaço para o adesivo de enquete) e "baixe" | 1080 × 1920 |
| `pt-BR/reels/`, `en-US/reels/` | 2 Reels de 15 s com música, narração e legendas gravadas, mais as capas | MP4 1080 × 1920, 30 fps |
| `audio/` | Trilha "Baião da Quitanda" (15 s e 30 s) e as 4 narrações separadas | MP3 |
| `destaques/`, `perfil/` | Capas dos destaques e fotos de perfil | 1080 × 1920 e 1080 × 1080 |
| `fonte/` | Modelos e scripts que geraram tudo, para mudar textos e gerar de novo | HTML, JS, Python |

**Sobre os Reels:**
- **reel-jogo:** abertura com o bem-te-vi, "Junte · Entregue · Viaje!", uma partida real gravada no celular e o fechamento com o ícone e o Google Play.
- **reel-mercados:** os 12 mercados em sequência, cada um com nome e cidade.
- **Narração:** feita com voz sintética (Microsoft Azure, vozes Thalita e Jenny).
- **Trilha:** composta para o projeto (zabumba, triângulo, baixo e sanfona), com o canto real do bem-te-vi no começo e no fim. É música própria, então não há problema de direitos.
- **Volume:** os vídeos estão nivelados em −14 LUFS, o padrão das redes.
- **Legendas:** gravadas no vídeo, porque muita gente assiste sem som.

**Para fazer mais Reels:** use `audio/trilha-baiao-30s.mp3` como fundo no editor do Instagram ou no CapCut, por cima de gravações de tela do jogo.

## 6. Plano das primeiras 3 semanas

O perfil não deve parecer vazio no dia da estreia, então publique 3 posts no primeiro dia para fechar a primeira linha da grade. O Instagram mostra o mais novo à esquerda, por isso publique nesta ordem:

| Dia | Post | Formato |
|---|---|---|
| 1 | 05 · Prazer, Bentevi | Foto |
| 1 | 06 · Recursos | Foto |
| 1 | 01 · Lançamento + stories 1 e 3 | Foto + stories |
| 3 | Reel do jogo | Reel |
| 5 | 02 · Como jogar | Carrossel |
| 7 | Story 2 (enquete) | Story |
| 8 | Reel dos mercados | Reel |
| 10 | 03 · Os 12 mercados | Carrossel |
| 12 | 04 · Do limão ao açaí | Foto |
| 14 | Repost do Reel do jogo nos stories | Story |
| 15 em diante | Um post por mercado: a ilustração e uma curiosidade real do lugar (dá 12 posts) | Foto ou carrossel |

**Boas práticas:**
- Responda os comentários na primeira hora.
- Nos Reels, marque a localização do mercado mostrado.
- Fixe no topo do perfil o post 01 e o Reel do jogo.

## 7. Legendas

Em cada post, publique a legenda em português e, embaixo, a versão em inglês, separada por uma linha com 🌎.

### 01 · Lançamento
**PT:** Chegou a Quitanda Zen! 🧺 Monte sua banca, junte itens iguais para criar coisas melhores e atenda a turma da feira. Depois, pegue a estrada: são 12 mercados de verdade, do Ver-o-Peso ao Mercado Público de Porto Alegre. Sem pressa e sem derrota. Grátis no Google Play, link na bio. 🐦

**EN:** Meet Quitanda! 🧺 Run a little market stall, merge matching items into better ones and serve the market crew. Then hit the road: 12 real Brazilian markets, from Ver-o-Peso to Porto Alegre. No rush, no losing. Free on Google Play, link in bio. 🐦

### 02 · Como jogar (carrossel)
**PT:** Aprende em 30 segundos 👇 1️⃣ Junte dois itens iguais e eles viram um melhor. 2️⃣ Entregue os pedidos e ganhe moedas (cada pedido mostra quanto paga). 3️⃣ Complete a feira e viaje para o próximo mercado. Qual item você quer chegar primeiro: o açaí na tigela ou a moqueca? 🍲

**EN:** Learn it in 30 seconds 👇 1️⃣ Merge two matching items into a better one. 2️⃣ Fill orders and earn coins (every order shows what it pays). 3️⃣ Finish the market and travel to the next one. Which will you reach first: the açaí bowl or the moqueca? 🍲

### 03 · Os 12 mercados (carrossel)
**PT:** 12 mercados, 12 jeitos de ser Brasil 🇧🇷 Arraste e diga nos comentários: qual deles você já visitou? Belém, Manaus, Salvador, Recife, Fortaleza, Campo Grande, São Paulo, Belo Horizonte, Rio, Porto Alegre, Florianópolis e Curitiba. Todos estão na rota da Quitanda Zen.

**EN:** 12 markets, 12 ways to be Brazilian 🇧🇷 Swipe and tell us: have you been to any of them? Belém, Manaus, Salvador, Recife, Fortaleza, Campo Grande, São Paulo, Belo Horizonte, Rio, Porto Alegre, Florianópolis and Curitiba. They’re all on the Quitanda trail.

### 04 · Do limão ao açaí
**PT:** Cada linha tem 8 níveis. Nas frutas, o limão vira laranja, que vira banana… até chegar ao açaí na tigela. 🍋➡️🍇 São 13 linhas para completar no álbum de ingredientes, e cada linha completa rende bônus.

**EN:** Every line has 8 levels. In fruits, a lime becomes an orange, then a banana… all the way to an açaí bowl. 🍋➡️🍇 There are 13 lines to complete in the ingredient album, and each finished line pays a bonus.

### 05 · Prazer, Bentevi
**PT:** Prazer, somos a Bentevi! 🐦 Um estúdio independente brasileiro que faz jogos e apps calmos, bonitos e com cara de Brasil. O nome vem do bem-te-vi, o passarinho que canta o próprio nome. Nosso primeiro jogo é a Quitanda Zen, e vem mais por aí.

**EN:** Hi, we’re Bentevi! 🐦 An independent studio from Brazil making calm, good-looking games and apps that feel like home. The name comes from the bem-te-vi (“I saw you”), a bird that sings its own name. Our first game is Quitanda, with more on the way.

### 06 · Recursos
**PT:** Feito para jogar do seu jeito: sem derrota e sem cronômetro na tela, funciona sem internet, tem álbum de ingredientes e um código para levar o progresso ao trocar de celular. 💚

**EN:** Made to be played your way: no losing, no timer on screen, works offline, has an ingredient album and a code to take your progress to a new phone. 💚

### Reel do jogo
**PT:** Junte, entregue e viaje! 🧺🚚 Uma partida de verdade da Quitanda Zen. 🔊 Liga o som: tem baião e bem-te-vi.

**EN:** Merge, deliver, travel! 🧺🚚 Real gameplay from Quitanda. 🔊 Sound on: baião and a real bem-te-vi.

### Reel dos mercados
**PT:** Do Ver-o-Peso ao Mercadão, e mais 10 mercados pelo Brasil. Qual é o mercado da sua cidade? 📍

**EN:** From Ver-o-Peso to São Paulo’s Mercadão, plus 10 more markets across Brazil. What’s the market in your town? 📍

### Hashtags (use de 5 a 10 por post)
**PT:** `#QuitandaZen #Bentevi #JogoBrasileiro #JogoIndie #JogosMobile #JogoCasual #FeiraLivre #MercadoMunicipal #CulturaBrasileira #GameDevBrasil`

**EN:** `#Quitanda #IndieGame #MergeGame #CozyGames #MobileGame #AndroidGames #Brazil #BrazilianFood #GameDev #CozyGaming`

**Por mercado:** use a hashtag do lugar, por exemplo `#VerOPeso`, `#Mercadão`, `#MercadoCentralBH`, `#FeiraDeSãoCristóvão`.

## 8. Stories fixos (sequência de lançamento)

1. **story-1-lancamento:** coloque o adesivo de **link** (Play Store) no retângulo tracejado.
2. **Reel do jogo** repostado nos stories.
3. **story-2-enquete:** adesivo de **enquete** com "Ver-o-Peso / Mercadão / São Cristóvão / Porto Alegre", ou o adesivo de **quiz**.
4. **story-3-baixe:** adesivo de link de novo.

Salve tudo no destaque **Quitanda**.

## 9. Para gerar de novo ou mudar textos

Os textos de cada peça estão em `fonte/pecas.html`, e os dos Reels (roteiro e legendas) em `fonte/reel.html`. As imagens vêm das pastas do repositório (`docs/arte/referencias/`, `docs/arte/itens/`, `docs/loja-play/quitanda-zen/*/capturas/`), copiadas para uma pasta `assets/` ao lado dos modelos.

| Script | O que faz |
|---|---|
| `render.js` | Gera as imagens |
| `gameplay.js` | Grava a partida |
| `reel.js` | Gera os quadros dos Reels |
| `trilha.py` | Compõe a trilha |
| `tts.py` | Gera as narrações |
