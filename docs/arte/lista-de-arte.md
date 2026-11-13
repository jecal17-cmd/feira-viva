# Feira Viva · Lista de arte

Lista de tudo o que precisa de imagem na Versão B (Quitanda Zen / *Quitanda: Merge Across Brazil*). Gerada a partir dos dados do jogo em `versao-b-quitanda-zen/index.html`: se os dados mudarem, a lista precisa ser atualizada.

A mesma lista está em `lista-de-arte.csv`, com uma coluna `prompt_en` pronta para colar em geradores de imagem.

**Para continuar gerando, use `falta-gerar.md`:** ele traz só o que ainda falta, linha por linha, com o nome do arquivo e o prompt pronto para copiar, além da lista do que vale refazer.

## Progresso da arte

Atualizado por `atualizar_status.py`. ✅ = imagem já no jogo · ⬜ = falta gerar.

| Grupo | Prontas | Faltam |
|---|---|---|
| Mercados | 12 de 12 | 0 |
| Itens do tabuleiro | 58 de 104 | 46 |
| Itens da Rota das Feiras | 3 de 15 | 12 |
| Personagens | 0 de 28 | 28 |
| Decoração da banca | 0 de 12 | 12 |

**Itens que faltam, por linha:**

- Armazém (1): Farinha de mandioca
- Doces (6): Chocolate, Cocada, Quindim, Sonho, Goiabada, Bolo de rolo
- Carnes (7): Ovo, Torresmo, Linguiça, Carne de sol, Costela, Espetinho, Feijoada
- Laticínios (8): Leite, Manteiga, Queijo minas, Requeijão, Queijo coalho, Doce de leite, Romeu e Julieta, Pudim
- Lanches (8): Pastel, Tapioca, Sanduíche de mortadela, Coxinha, Acarajé, X-tudo, Tapioca recheada, Marmita
- Padaria (8): Trigo, Pão de forma, Pão francês, Pão de queijo, Rosca, Bolo de fubá, Empadão, Bolo de festa
- Flores (8): Muda, Margarida, Orquídea, Girassol, Bromélia, Hibisco, Ipê-amarelo, Buquê tropical

## Como gerar

São **dois estilos**, de propósito: os mercados (e os personagens que vivem neles) têm cara de ilustração pintada, e as peças do tabuleiro têm cara de objeto 3D brilhante. O texto de estilo já está no fim de cada `prompt_en` do CSV; basta colar o prompt inteiro.

**Mercados e personagens: ilustração pintada.** Referências em `referencias/mercado-*.jpg`.
- Estilo: *painted 2D illustration in a warm retro travel-poster style: golden late-afternoon light, big soft cumulus clouds, slightly grainy brush texture, flat shapes with soft shading, warm reds, ochres and teal greens, small figures of shoppers and vendors for scale*.
- Formato: mercados em paisagem 16:9 (por exemplo, 1024 × 576 ou maior); personagens em busto, quadrado, fundo liso claro (o fundo é removido depois).

**Itens do tabuleiro e decoração da banca: render 3D brilhante.** Referência em `referencias/item-estilo-caju.jpg`.
- Estilo: *glossy stylized 3D render, smooth rounded shapes, vivid saturated colors with soft gradients, soft studio lighting with gentle highlights, single object centered and fully in frame, plain pure white background, no shadow, no text, square 1:1*.
- Formato: quadrado, fundo branco liso, sem sombra no chão. O fundo branco é tirado depois e a imagem vira PNG de 512 × 512 com fundo transparente.
- Para pôr no jogo: `python docs/arte/itens/recortar_itens.py fr-1=limao.png fr-2=laranja.png ...` tira o fundo (com o rembg), apaga textos soltos que o gerador escreveu, centraliza, salva a matriz de 512 px em `docs/arte/itens/` e o WebP de 256 px em `versao-b-quitanda-zen/itens/`. O WebP do jogo sai normalizado: itens compridos e deitados vão para a diagonal e todos ocupam a mesma área visível da casa (`AREA_ALVO`). Para mudar essa regra e refazer todos sem recortar de novo, rode o script com `--todos`. Depois, acrescente os códigos em `ITEM_ART`, no `index.html`, e rode `python docs/arte/atualizar_status.py` para marcar a lista.
- Os itens de uma mesma linha devem parecer uma evolução: do nível 1 ao 8 o item fica maior, mais caprichado e mais valioso. O prompt do nível 1 pede algo simples e o do nível 8, a versão mais caprichada.

**Para todos:**
- **Nome dos arquivos:** use a coluna *Arquivo*. Ela segue os códigos do jogo (`fr-1` = Frutas nível 1), o que facilita trocar os emojis pela arte depois. Se o gerador salvar com outro nome, tudo bem: dá para renomear depois.
- **Mercados reais:** use fotos só como referência e desenhe ilustrações próprias, sem copiar fotos (direitos autorais). Ilustrações geradas costumam inventar detalhes da arquitetura: confira cada prédio antes de publicar.
- **Personagens:** evite estereótipos. As descrições são ponto de partida; o ideal é revisar com pessoas de cada região.

### Referências já aprovadas

Os 12 mercados já estão no jogo, em `versao-b-quitanda-zen/mercados/` (WebP de 960 px de largura). Para pôr a arte de outro mercado: salve a imagem como WebP nessa pasta, com o nome da coluna *Arquivo*, e preencha o campo `img` do mercado em `FEIRAS`, no `index.html`. Sem `img`, o jogo continua usando o emoji.

| Arquivo | Mercado |
|---|---|
| `referencias/mercado-04-sao-jose-recife.jpg` | Mercado de São José, Recife (pavilhão verde) |
| `referencias/mercado-06-feira-central-campo-grande.jpg` | Feira Central, Campo Grande (galpão à noite) |
| `referencias/mercado-07-mercadao-sp-interior.jpg` | Mercadão, São Paulo (salão interno) |
| `referencias/mercado-09-sao-cristovao-aerea.jpg` | Feira de São Cristóvão, Rio de Janeiro (vista aérea) |
| `referencias/mercado-10-porto-alegre.jpg` | Mercado Público, Porto Alegre (fachada amarela) |
| `referencias/mercado-01-ver-o-peso-belem.jpg` | Ver-o-Peso, Belém (mercado azul à beira da baía) |
| `referencias/mercado-02-adolpho-lisboa-manaus.jpg` | Mercado Adolpho Lisboa (Mercado Municipal), Manaus (fachada vermelha) |
| `referencias/mercado-03-sao-joaquim-salvador.jpg` | Feira de São Joaquim, Salvador (rua de feira) |
| `referencias/mercado-05-fortaleza.jpg` | Mercado Central, Fortaleza (prédio redondo) |
| `referencias/mercado-08-belo-horizonte-aerea.jpg` | Mercado Central, Belo Horizonte (vista de cima) |
| `referencias/mercado-11-florianopolis.jpg` | Mercado Público, Florianópolis (pátio a céu aberto) |
| `referencias/mercado-12-curitiba.jpg` | Mercado Municipal, Curitiba (fachada com arcos vermelhos) |
| `referencias/item-estilo-caju.jpg` | estilo dos itens (caju) |

## Mercados (12)

| # | Arquivo | Mercado | Cidade | Região (pt / en) | Descrição visual | Arte |
|---|---|---|---|---|---|---|
| 1 | `mercados/01-ver-o-peso-belem.png` | Ver-o-Peso | Belém (PA) | Norte / North | mercado azul com quatro torrinhas pontudas e telhado de telhas, à beira da baía, barcos e tendas brancas no cais | ✅ |
| 2 | `mercados/02-mercado-adolpho-lisboa-manaus.png` | Mercado Adolpho Lisboa | Manaus (AM) | Norte / North | fachada vermelha e amarela com torre do relógio, portão em arco verde e toldos brancos | ✅ |
| 3 | `mercados/03-feira-de-sao-joaquim-salvador.png` | Feira de São Joaquim | Salvador (BA) | Nordeste / Northeast | rua de feira com faixa de entrada, bancas com toldos verdes, cobertura de lona ao fundo | ✅ |
| 4 | `mercados/04-mercado-de-sao-jose-recife.png` | Mercado de São José | Recife (PE) | Nordeste / Northeast | pavilhão de ferro verde-claro do século XIX, frontão com arabescos e grande janela em arco de vidro ao centro | ✅ |
| 5 | `mercados/05-mercado-central-fortaleza.png` | Mercado Central | Fortaleza (CE) | Nordeste / Northeast | prédio redondo como um estádio, faixas verdes, grande arco amarelo na entrada | ✅ |
| 6 | `mercados/06-feira-central-campo-grande.png` | Feira Central | Campo Grande (MS) | Centro-Oeste / Center-West | galpão coberto à noite com arcos no teto, luz quente e bancas de sobá fumegando | ✅ |
| 7 | `mercados/07-mercadao-sao-paulo.png` | Mercadão | São Paulo (SP) | Sudeste / Southeast | salão interno com arcos de pedra clara, claraboia de vidro no teto, vitrais e corredores de bancas de frutas | ✅ |
| 8 | `mercados/08-mercado-central-belo-horizonte.png` | Mercado Central | Belo Horizonte (MG) | Sudeste / Southeast | vista aérea de um galpão com telhado em abóbadas claras e fachada vermelha, entre prédios | ✅ |
| 9 | `mercados/09-feira-de-sao-cristovao-rio-de-janeiro.png` | Feira de São Cristóvão | Rio de Janeiro (RJ) | Sudeste / Southeast | vista aérea do grande pavilhão oval, com bancas de lona azul cortadas por passarelas brancas em cruz | ✅ |
| 10 | `mercados/10-mercado-publico-porto-alegre.png` | Mercado Público | Porto Alegre (RS) | Sul / South | prédio histórico amarelo de dois andares, frontão no centro e portas em arco verdes | ✅ |
| 11 | `mercados/11-mercado-publico-florianopolis.png` | Mercado Público | Florianópolis (SC) | Sul / South | pátio a céu aberto cheio de gente e guarda-sóis, entre dois blocos amarelos com toldos verdes e torres ao fundo | ✅ |
| 12 | `mercados/12-mercado-municipal-curitiba.png` | Mercado Municipal | Curitiba (PR) | Sul / South | fachada comprida com arcos vermelhos, janelas verdes e varanda com guarda-sóis vermelhos | ✅ |

Os nomes dos mercados e das cidades ficam em português nas duas versões.

## Itens (13 linhas × 8 níveis = 104)

Na versão em inglês, os nomes tipicamente brasileiros ficam em português e ganham uma explicação curta (coluna *Explicação*), que aparece no jogo ao tocar no item.

### Frutas / Fruits (`fr`)

| Nível | Arquivo | Português | Inglês | Explicação (inglês) | Emoji provisório | Arte |
|---|---|---|---|---|---|---|
| 1 | `itens/fr-1.png` | Limão | Lime |  | 🍋 | ✅ |
| 2 | `itens/fr-2.png` | Laranja | Orange |  | 🍊 | ✅ |
| 3 | `itens/fr-3.png` | Banana | Banana |  | 🍌 | ✅ |
| 4 | `itens/fr-4.png` | Manga | Mango |  | 🥭 | ✅ |
| 5 | `itens/fr-5.png` | Abacaxi | Pineapple |  | 🍍 | ✅ |
| 6 | `itens/fr-6.png` | Caju | Caju | cashew fruit: the juicy part that grows above the nut | 🍎 | ✅ |
| 7 | `itens/fr-7.png` | Jabuticaba | Jabuticaba | grape-like berry that grows right on the tree trunk | 🫐 | ✅ |
| 8 | `itens/fr-8.png` | Açaí na tigela | Açaí bowl | frozen Amazonian berry purée, eaten with a spoon | 🍇 | ✅ |

### Verduras / Veggies (`ve`)

| Nível | Arquivo | Português | Inglês | Explicação (inglês) | Emoji provisório | Arte |
|---|---|---|---|---|---|---|
| 1 | `itens/ve-1.png` | Cheiro-verde | Cheiro-verde | bundle of parsley and green onion, in almost every Brazilian dish | 🌿 | ✅ |
| 2 | `itens/ve-2.png` | Couve | Collard greens |  | 🥬 | ✅ |
| 3 | `itens/ve-3.png` | Cenoura | Carrot |  | 🥕 | ✅ |
| 4 | `itens/ve-4.png` | Tomate | Tomato |  | 🍅 | ✅ |
| 5 | `itens/ve-5.png` | Milho | Corn |  | 🌽 | ✅ |
| 6 | `itens/ve-6.png` | Mandioca | Mandioca | cassava root, a staple all over Brazil | 🍠 | ✅ |
| 7 | `itens/ve-7.png` | Abóbora | Pumpkin |  | 🎃 | ✅ |
| 8 | `itens/ve-8.png` | Salada | Salad |  | 🥗 | ✅ |

### Peixes / Seafood (`pe`)

| Nível | Arquivo | Português | Inglês | Explicação (inglês) | Emoji provisório | Arte |
|---|---|---|---|---|---|---|
| 1 | `itens/pe-1.png` | Camarão | Shrimp |  | 🦐 | ✅ |
| 2 | `itens/pe-2.png` | Sardinha | Sardine |  | 🐟 | ✅ |
| 3 | `itens/pe-3.png` | Peixe | Fish |  | 🐠 | ✅ |
| 4 | `itens/pe-4.png` | Caranguejo | Crab |  | 🦀 | ✅ |
| 5 | `itens/pe-5.png` | Tainha | Tainha | mullet, the winter catch of southern Brazil | 🐡 | ✅ |
| 6 | `itens/pe-6.png` | Lagosta | Lobster |  | 🦞 | ✅ |
| 7 | `itens/pe-7.png` | Pirarucu | Pirarucu | giant Amazon river fish | 🎣 | ✅ |
| 8 | `itens/pe-8.png` | Moqueca | Moqueca | Brazilian fish stew, often with coconut milk and dendê oil | 🍲 | ✅ |

### Temperos / Spices (`te`)

| Nível | Arquivo | Português | Inglês | Explicação (inglês) | Emoji provisório | Arte |
|---|---|---|---|---|---|---|
| 1 | `itens/te-1.png` | Sal | Salt |  | 🧂 | ✅ |
| 2 | `itens/te-2.png` | Alho | Garlic |  | 🧄 | ✅ |
| 3 | `itens/te-3.png` | Cebola | Onion |  | 🧅 | ✅ |
| 4 | `itens/te-4.png` | Pimenta-malagueta | Malagueta pepper | small, fiery Brazilian chili | 🌶️ | ✅ |
| 5 | `itens/te-5.png` | Pimentão | Bell pepper |  | 🫑 | ✅ |
| 6 | `itens/te-6.png` | Azeite de dendê | Dendê oil | red palm oil, the soul of Bahian cooking | 🫒 | ✅ |
| 7 | `itens/te-7.png` | Mel | Honey |  | 🍯 | ✅ |
| 8 | `itens/te-8.png` | Molho | Sauce |  | 🥫 | ✅ |

### Bebidas / Drinks (`be`)

| Nível | Arquivo | Português | Inglês | Explicação (inglês) | Emoji provisório | Arte |
|---|---|---|---|---|---|---|
| 1 | `itens/be-1.png` | Água | Water |  | 💧 | ✅ |
| 2 | `itens/be-2.png` | Água de coco | Coconut water |  | 🥥 | ✅ |
| 3 | `itens/be-3.png` | Suco | Juice |  | 🧃 | ✅ |
| 4 | `itens/be-4.png` | Café | Coffee |  | ☕ | ✅ |
| 5 | `itens/be-5.png` | Caldo de cana | Caldo de cana | fresh-pressed sugarcane juice | 🍵 | ✅ |
| 6 | `itens/be-6.png` | Chimarrão | Chimarrão | hot yerba mate sipped from a gourd | 🧉 | ✅ |
| 7 | `itens/be-7.png` | Guaraná | Guaraná | soda made from an Amazonian berry | 🥤 | ✅ |
| 8 | `itens/be-8.png` | Cajuína | Cajuína | clear, sweet cashew-fruit drink from the Northeast | 🍹 | ✅ |

### Artesanato / Crafts (`ar`)

| Nível | Arquivo | Português | Inglês | Explicação (inglês) | Emoji provisório | Arte |
|---|---|---|---|---|---|---|
| 1 | `itens/ar-1.png` | Linha | Thread |  | 🧵 | ✅ |
| 2 | `itens/ar-2.png` | Novelo | Ball of yarn |  | 🧶 | ✅ |
| 3 | `itens/ar-3.png` | Fita do Bonfim | Fita do Bonfim | wish ribbon from Salvador: tie it on and make three wishes | 🎗️ | ✅ |
| 4 | `itens/ar-4.png` | Renda | Bobbin lace |  | 🎀 | ✅ |
| 5 | `itens/ar-5.png` | Chapéu de palha | Straw hat |  | 👒 | ✅ |
| 6 | `itens/ar-6.png` | Cesto de palha | Straw basket |  | 🧺 | ✅ |
| 7 | `itens/ar-7.png` | Boneco de barro | Clay figurine |  | 🏺 | ✅ |
| 8 | `itens/ar-8.png` | Viola | Viola caipira | ten-string Brazilian country guitar | 🎸 | ✅ |

### Armazém / Pantry (`gr`)

| Nível | Arquivo | Português | Inglês | Explicação (inglês) | Emoji provisório | Arte |
|---|---|---|---|---|---|---|
| 1 | `itens/gr-1.png` | Amendoim | Peanuts |  | 🥜 | ✅ |
| 2 | `itens/gr-2.png` | Castanha-do-pará | Brazil nuts |  | 🌰 | ✅ |
| 3 | `itens/gr-3.png` | Pipoca | Popcorn |  | 🍿 | ✅ |
| 4 | `itens/gr-4.png` | Arroz | Rice |  | 🍚 | ✅ |
| 5 | `itens/gr-5.png` | Farinha de mandioca | Cassava flour |  | 🥣 | ⬜ |
| 6 | `itens/gr-6.png` | Feijão | Beans |  | 🫘 | ✅ |
| 7 | `itens/gr-7.png` | Cuscuz | Cuscuz | steamed cornmeal cake from the Northeast | 🥮 | ✅ |
| 8 | `itens/gr-8.png` | Baião de dois | Baião de dois | rice and beans cooked together with cheese, from Ceará | 🍛 | ✅ |

### Doces / Sweets (`do`)

| Nível | Arquivo | Português | Inglês | Explicação (inglês) | Emoji provisório | Arte |
|---|---|---|---|---|---|---|
| 1 | `itens/do-1.png` | Rapadura | Rapadura | block of unrefined cane sugar | 🍬 | ✅ |
| 2 | `itens/do-2.png` | Paçoca | Paçoca | crumbly peanut candy | 🍭 | ✅ |
| 3 | `itens/do-3.png` | Chocolate | Chocolate |  | 🍫 | ⬜ |
| 4 | `itens/do-4.png` | Cocada | Cocada | chewy coconut candy | 🍪 | ⬜ |
| 5 | `itens/do-5.png` | Quindim | Quindim | glossy coconut and egg-yolk custard | 🧁 | ⬜ |
| 6 | `itens/do-6.png` | Sonho | Sonho | cream-filled doughnut; the name means “dream” | 🍩 | ⬜ |
| 7 | `itens/do-7.png` | Goiabada | Goiabada | thick guava paste | 🍡 | ⬜ |
| 8 | `itens/do-8.png` | Bolo de rolo | Bolo de rolo | thin rolled cake with guava filling, from Pernambuco | 🍥 | ⬜ |

### Carnes / Meats (`ca`)

| Nível | Arquivo | Português | Inglês | Explicação (inglês) | Emoji provisório | Arte |
|---|---|---|---|---|---|---|
| 1 | `itens/ca-1.png` | Ovo | Egg |  | 🥚 | ⬜ |
| 2 | `itens/ca-2.png` | Frango | Chicken |  | 🍗 | ✅ |
| 3 | `itens/ca-3.png` | Torresmo | Torresmo | crispy pork crackling | 🥓 | ⬜ |
| 4 | `itens/ca-4.png` | Linguiça | Linguiça | Brazilian pork sausage | 🌭 | ⬜ |
| 5 | `itens/ca-5.png` | Carne de sol | Carne de sol | salted, sun-cured beef | 🥩 | ⬜ |
| 6 | `itens/ca-6.png` | Costela | Ribs |  | 🍖 | ⬜ |
| 7 | `itens/ca-7.png` | Espetinho | Espetinho | street-food skewer grilled on charcoal | 🍢 | ⬜ |
| 8 | `itens/ca-8.png` | Feijoada | Feijoada | black bean and pork stew, a national favorite | 🥘 | ⬜ |

### Laticínios / Dairy (`la`)

| Nível | Arquivo | Português | Inglês | Explicação (inglês) | Emoji provisório | Arte |
|---|---|---|---|---|---|---|
| 1 | `itens/la-1.png` | Leite | Milk |  | 🥛 | ⬜ |
| 2 | `itens/la-2.png` | Manteiga | Butter |  | 🧈 | ⬜ |
| 3 | `itens/la-3.png` | Queijo minas | Queijo minas | mild fresh cheese from Minas Gerais | 🧀 | ⬜ |
| 4 | `itens/la-4.png` | Requeijão | Requeijão | creamy spreadable cheese | 🍶 | ⬜ |
| 5 | `itens/la-5.png` | Queijo coalho | Queijo coalho | firm cheese grilled on a stick | 🧇 | ⬜ |
| 6 | `itens/la-6.png` | Doce de leite | Doce de leite | slow-cooked milk caramel | 🍨 | ⬜ |
| 7 | `itens/la-7.png` | Romeu e Julieta | Romeu e Julieta | cheese with guava paste, a classic pairing | 🍰 | ⬜ |
| 8 | `itens/la-8.png` | Pudim | Pudim | Brazilian caramel flan made with condensed milk | 🍮 | ⬜ |

### Lanches / Snacks (`ln`)

| Nível | Arquivo | Português | Inglês | Explicação (inglês) | Emoji provisório | Arte |
|---|---|---|---|---|---|---|
| 1 | `itens/ln-1.png` | Pastel | Pastel | crispy fried pastry, the classic street-market snack | 🥟 | ⬜ |
| 2 | `itens/ln-2.png` | Tapioca | Tapioca | crepe made from cassava starch | 🫓 | ⬜ |
| 3 | `itens/ln-3.png` | Sanduíche de mortadela | Mortadella sandwich |  | 🥪 | ⬜ |
| 4 | `itens/ln-4.png` | Coxinha | Coxinha | teardrop-shaped chicken croquette | 🍤 | ⬜ |
| 5 | `itens/ln-5.png` | Acarajé | Acarajé | black-eyed pea fritter fried in dendê oil | 🧆 | ⬜ |
| 6 | `itens/ln-6.png` | X-tudo | X-tudo | “cheese-everything”: a fully loaded burger | 🍔 | ⬜ |
| 7 | `itens/ln-7.png` | Tapioca recheada | Filled tapioca |  | 🌮 | ⬜ |
| 8 | `itens/ln-8.png` | Marmita | Marmita | home-style packed lunch | 🍱 | ⬜ |

### Padaria / Bakery (`pa`)

| Nível | Arquivo | Português | Inglês | Explicação (inglês) | Emoji provisório | Arte |
|---|---|---|---|---|---|---|
| 1 | `itens/pa-1.png` | Trigo | Wheat |  | 🌾 | ⬜ |
| 2 | `itens/pa-2.png` | Pão de forma | Sandwich loaf |  | 🍞 | ⬜ |
| 3 | `itens/pa-3.png` | Pão francês | Pão francês | crusty bread roll eaten every morning in Brazil | 🥖 | ⬜ |
| 4 | `itens/pa-4.png` | Pão de queijo | Pão de queijo | chewy little cheese bread | 🥯 | ⬜ |
| 5 | `itens/pa-5.png` | Rosca | Sweet bread ring |  | 🥨 | ⬜ |
| 6 | `itens/pa-6.png` | Bolo de fubá | Bolo de fubá | cornmeal cake | 🥞 | ⬜ |
| 7 | `itens/pa-7.png` | Empadão | Empadão | savory pot pie | 🥧 | ⬜ |
| 8 | `itens/pa-8.png` | Bolo de festa | Party cake |  | 🎂 | ⬜ |

### Flores / Flowers (`fl`)

| Nível | Arquivo | Português | Inglês | Explicação (inglês) | Emoji provisório | Arte |
|---|---|---|---|---|---|---|
| 1 | `itens/fl-1.png` | Muda | Seedling |  | 🌱 | ⬜ |
| 2 | `itens/fl-2.png` | Margarida | Daisy |  | 🌼 | ⬜ |
| 3 | `itens/fl-3.png` | Orquídea | Orchid |  | 🌷 | ⬜ |
| 4 | `itens/fl-4.png` | Girassol | Sunflower |  | 🌻 | ⬜ |
| 5 | `itens/fl-5.png` | Bromélia | Bromeliad |  | 🌹 | ⬜ |
| 6 | `itens/fl-6.png` | Hibisco | Hibiscus |  | 🌺 | ⬜ |
| 7 | `itens/fl-7.png` | Ipê-amarelo | Ipê-amarelo | tree that bursts into yellow bloom | 🌳 | ⬜ |
| 8 | `itens/fl-8.png` | Buquê tropical | Tropical bouquet |  | 💐 | ⬜ |

## Itens da Rota das Feiras (3 linhas × 5 níveis = 15)

A Versão A tem itens próprios do Ver-o-Peso. Ficam em `versao-a-rota-das-feiras/itens/`; o código no jogo é o mesmo da coluna *Arquivo* (por exemplo, `ac-1`). Mesmo estilo 3D dos itens da Quitanda. Alguns reaproveitam imagens da Quitanda.

### Açaí (`ac`)

| Nível | Arquivo | Português | Inglês | Arte |
|---|---|---|---|---|
| 1 | `rota/itens/ac-1.png` | Cacho de açaí | Açaí bunch | ⬜ |
| 2 | `rota/itens/ac-2.png` | Fruto | Açaí berries | ⬜ |
| 3 | `rota/itens/ac-3.png` | Polpa | Açaí pulp | ⬜ |
| 4 | `rota/itens/ac-4.png` | Açaí batido | Blended açaí | ⬜ |
| 5 | `rota/itens/ac-5.png` | Tigela de açaí com tapioca | Açaí bowl with tapioca | ✅ |

### Peixe (`pe`)

| Nível | Arquivo | Português | Inglês | Arte |
|---|---|---|---|---|
| 1 | `rota/itens/pe-1.png` | Peixe pequeno | Small fish | ✅ |
| 2 | `rota/itens/pe-2.png` | Peixe limpo | Cleaned fish | ✅ |
| 3 | `rota/itens/pe-3.png` | Filé | Fillet | ⬜ |
| 4 | `rota/itens/pe-4.png` | Peixe assado | Roast fish | ⬜ |
| 5 | `rota/itens/pe-5.png` | Pirarucu de casaca | Pirarucu de casaca | ⬜ |

### Jambu/Tucupi (`jt`)

| Nível | Arquivo | Português | Inglês | Arte |
|---|---|---|---|---|
| 1 | `rota/itens/jt-1.png` | Folha de jambu | Jambu leaf | ⬜ |
| 2 | `rota/itens/jt-2.png` | Maço de jambu | Jambu bunch | ⬜ |
| 3 | `rota/itens/jt-3.png` | Caldo de tucupi | Tucupi broth | ⬜ |
| 4 | `rota/itens/jt-4.png` | Tacacá | Tacacá | ⬜ |
| 5 | `rota/itens/jt-5.png` | Pato no tucupi | Pato no tucupi | ⬜ |

## Personagens (28)

| Arquivo | Nome | Papel (pt) | Papel (en) | Onde aparece | Descrição visual | Arte |
|---|---|---|---|---|---|---|
| `personagens/ze.png` | 👨‍🌾 Seu Zé | feirante e seu guia | market vendor and your guide | viaja com o jogador | homem de uns 60 anos, chapéu de palha, camisa xadrez, avental, sorriso largo | ⬜ |
| `personagens/bia.png` | 👧 Bia | aprendiz da banca | stall apprentice | viaja com o jogador | menina de uns 10 anos, rabo de cavalo, avental pequeno, carregando um caixote | ⬜ |
| `personagens/mingau.png` | 🐈 Mingau | gato da quitanda | the shop cat | viaja com o jogador | gato branco e gordinho, olhar preguiçoso | ⬜ |
| `personagens/tonho.png` | 🚚 Tonho | caminhoneiro | truck driver | viaja com o jogador | caminhoneiro de boné, braço na janela de um caminhão colorido | ⬜ |
| `personagens/naza.png` | 👵 Dona Nazaré | tacacazeira | tacacá soup cook | Ver-o-Peso, Belém | senhora idosa, cabelo grisalho preso, vestido estampado, cuia de tacacá nas mãos | ⬜ |
| `personagens/raimundo.png` | 🧔 Seu Raimundo | pescador | fisherman | Ver-o-Peso, Belém | pescador de barba e chapéu, segurando um peixe de rio | ⬜ |
| `personagens/iara.png` | 👩‍🦱 Iara | artesã | artisan | Mercado Adolpho Lisboa, Manaus | mulher jovem de cabelo cacheado tecendo um cesto de palha | ⬜ |
| `personagens/chico.png` | 🧑‍🌾 Seu Chico | ribeirinho | riverside dweller | Mercado Adolpho Lisboa, Manaus | ribeirinho de chapéu com uma canoa de madeira ao fundo | ⬜ |
| `personagens/dada.png` | 👩🏾‍🍳 Dona Dadá | baiana de tabuleiro | baiana street-food cook | Feira de São Joaquim, Salvador | baiana de acarajé com turbante e saia rodada brancos, tabuleiro de quitutes | ⬜ |
| `personagens/jorginho.png` | 🧑🏾‍🎤 Jorginho | percussionista | percussionist | Feira de São Joaquim, Salvador | rapaz sorridente tocando um tambor de mão | ⬜ |
| `personagens/biu.png` | 👨🏽‍🎨 Mestre Biu | ceramista | master potter | Mercado de São José, Recife | artesão mais velho moldando um bonequinho de barro | ⬜ |
| `personagens/flor.png` | 👩🏽 Maria Flor | rendeira | lacemaker | Mercado de São José, Recife | mulher com uma almofada de renda de bilro no colo | ⬜ |
| `personagens/cicero.png` | 👨🏽‍🌾 Seu Cícero | vendedor de frutas | fruit seller | Mercado Central, Fortaleza | vendedor de frutas de chapéu de couro com um carrinho de frutas | ⬜ |
| `personagens/rosinha.png` | 👧🏽 Rosinha | neta da rendeira | the lacemaker’s granddaughter | Mercado Central, Fortaleza | menina de vestido de chita florida e laço no cabelo | ⬜ |
| `personagens/keiko.png` | 👩🏻‍🍳 Dona Keiko | cozinheira de sobá | sobá noodle cook | Feira Central, Campo Grande | cozinheira nipo-brasileira de avental com uma tigela de sobá fumegante | ⬜ |
| `personagens/antenor.png` | 🤠 Seu Antenor | peão pantaneiro | Pantanal cowboy | Feira Central, Campo Grande | peão pantaneiro de chapéu e lenço no pescoço, com uma guampa de tereré | ⬜ |
| `personagens/giuseppe.png` | 👨🏻‍🍳 Seu Giuseppe | dono da lanchonete | snack bar owner | Mercadão, São Paulo | dono de lanchonete de bigode e avental, com um sanduíche de mortadela enorme | ⬜ |
| `personagens/paula.png` | 👩🏻‍💼 Paula | sempre apressada | always in a rush | Mercadão, São Paulo | mulher em roupa de escritório, celular na mão, andando apressada | ⬜ |
| `personagens/geralda.png` | 👵🏽 Dona Geralda | quitandeira mineira | quitandeira from Minas | Mercado Central, Belo Horizonte | senhora mineira de avental com bule de café e pão de queijo | ⬜ |
| `personagens/tiao.png` | 🧑🏽‍🍳 Tiãozinho | queijeiro | cheesemaker | Mercado Central, Belo Horizonte | rapaz de chapéu segurando uma peça de queijo minas curado | ⬜ |
| `personagens/jacinto.png` | 👨🏾‍🦳 Seu Jacinto | sanfoneiro | accordion player | Feira de São Cristóvão, Rio de Janeiro | sanfoneiro mais velho de chapéu de couro tocando sanfona | ⬜ |
| `personagens/dandara.png` | 👩🏾 Dandara | cozinheira | cook | Feira de São Cristóvão, Rio de Janeiro | cozinheira de lenço na cabeça mexendo uma panela grande | ⬜ |
| `personagens/gaudencio.png` | 🧔🏻 Seu Gaudêncio | assador | churrasco grill master | Mercado Público, Porto Alegre | gaúcho de bombacha, lenço e boina, com um espeto de churrasco | ⬜ |
| `personagens/livia.png` | 👩🏼 Lívia | dona da cuia | keeper of the mate gourd | Mercado Público, Porto Alegre | jovem gaúcha com cuia de chimarrão e garrafa térmica | ⬜ |
| `personagens/dico.png` | 🧑🏼‍🦰 Dico | pescador | fisherman | Mercado Público, Florianópolis | pescador com uma rede de pesca no ombro | ⬜ |
| `personagens/zulma.png` | 👩🏼‍🦳 Dona Zulma | florista | florist | Mercado Público, Florianópolis | senhora florista com um balde de flores | ⬜ |
| `personagens/halina.png` | 👩🏼‍🍳 Dona Halina | cozinheira | cook | Mercado Municipal, Curitiba | cozinheira de origem polonesa, lenço na cabeça, prato de pierogi | ⬜ |
| `personagens/estanislau.png` | 👨🏻‍🦳 Seu Estanislau | vendedor do armazém | general store keeper | Mercado Municipal, Curitiba | senhor de avental atrás do balcão do armazém | ⬜ |

Os nomes dos personagens não são traduzidos. As falas em inglês mantêm expressões regionais (*égua*, *oxente*, *uai*, *bah*, *tchê*) como toque de cultura local.

## Extras: decoração da banca (12)

Aparecem na banca da tela inicial.

| Arquivo | Português | Inglês | Emoji provisório | Arte |
|---|---|---|---|---|
| `decoracao/01-toldo-listrado.png` | Toldo listrado | Striped awning | ⛱️ | ⬜ |
| `decoracao/02-vasos-de-ervas.png` | Vasos de ervas | Herb pots | 🪴 | ⬜ |
| `decoracao/03-banco-de-madeira.png` | Banco de madeira | Wooden bench | 🪑 | ⬜ |
| `decoracao/04-lousa-de-precos.png` | Lousa de preços | Price chalkboard | 📋 | ⬜ |
| `decoracao/05-balanca-antiga.png` | Balança antiga | Vintage scale | ⚖️ | ⬜ |
| `decoracao/06-luzinhas.png` | Luzinhas | String lights | ✨ | ⬜ |
| `decoracao/07-radio-de-pilha.png` | Rádio de pilha | Transistor radio | 📻 | ⬜ |
| `decoracao/08-bicicleta-de-entrega.png` | Bicicleta de entrega | Delivery bike | 🚲 | ⬜ |
| `decoracao/09-carrinho-de-feira.png` | Carrinho de feira | Market trolley | 🛒 | ⬜ |
| `decoracao/10-relogio-de-parede.png` | Relógio de parede | Wall clock | 🕰️ | ⬜ |
| `decoracao/11-bandeirinhas.png` | Bandeirinhas | Bandeirinhas (festa junina flags) | 🎊 | ⬜ |
| `decoracao/12-caminha-do-mingau.png` | Caminha do Mingau | Mingau’s cat bed | 🐈 | ⬜ |
