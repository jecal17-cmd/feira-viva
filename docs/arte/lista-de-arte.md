# Feira Viva · Lista de arte

Lista de tudo o que precisa de imagem na Versão B (Quitanda Zen / *Quitanda: Merge Across Brazil*). Gerada a partir dos dados do jogo em `versao-b-quitanda-zen/index.html`: se os dados mudarem, a lista precisa ser atualizada.

A mesma lista está em `lista-de-arte.csv`, com uma coluna `prompt_en` pronta para colar em geradores de imagem.

## Como gerar

- **Estilo comum** (use em todas as imagens para manter a unidade): *cute 2D game icon, soft shading, bold clean outline, warm Brazilian street-market colors, centered, transparent background, no text*.
- **Formato sugerido:** PNG quadrado de 512 × 512 px com fundo transparente. Os personagens podem ser só o busto. Os mercados ficam melhores em formato paisagem (por exemplo, 1024 × 576).
- **Nome dos arquivos:** use a coluna *Arquivo*. Ela segue os códigos do jogo (`fr-1` = Frutas nível 1), o que facilita trocar os emojis pela arte depois.
- **Itens de uma mesma linha** devem parecer uma evolução: do nível 1 ao 8 o item fica maior, mais caprichado e mais valioso.
- **Mercados reais:** use fotos só como referência e desenhe ilustrações próprias, sem copiar fotos (direitos autorais). Confira os detalhes de cada prédio antes de publicar.
- **Personagens:** evite estereótipos. As descrições são ponto de partida; o ideal é revisar com pessoas de cada região.

## Mercados (12)

| # | Arquivo | Mercado | Cidade | Região (pt / en) | Descrição visual |
|---|---|---|---|---|---|
| 1 | `mercados/01-ver-o-peso-belem.png` | Ver-o-Peso | Belém (PA) | Norte / North | mercado de ferro com torrezinhas na beira da baía, barcos coloridos |
| 2 | `mercados/02-mercado-adolpho-lisboa-manaus.png` | Mercado Adolpho Lisboa | Manaus (AM) | Norte / North | mercado de ferro art nouveau à beira do rio Negro |
| 3 | `mercados/03-feira-de-sao-joaquim-salvador.png` | Feira de São Joaquim | Salvador (BA) | Nordeste / Northeast | feira movimentada com barracas e barcos à vela na baía |
| 4 | `mercados/04-mercado-de-sao-jose-recife.png` | Mercado de São José | Recife (PE) | Nordeste / Northeast | mercado de ferro do século XIX |
| 5 | `mercados/05-mercado-central-fortaleza.png` | Mercado Central | Fortaleza (CE) | Nordeste / Northeast | prédio de vários andares cheio de redes, rendas e artesanato |
| 6 | `mercados/06-feira-central-campo-grande.png` | Feira Central | Campo Grande (MS) | Centro-Oeste / Center-West | feira coberta à noite com bancas de sobá |
| 7 | `mercados/07-mercadao-sao-paulo.png` | Mercadão | São Paulo (SP) | Sudeste / Southeast | grande salão com vitrais coloridos e bancas de frutas |
| 8 | `mercados/08-mercado-central-belo-horizonte.png` | Mercado Central | Belo Horizonte (MG) | Sudeste / Southeast | corredores com queijos, doces e café |
| 9 | `mercados/09-feira-de-sao-cristovao-rio-de-janeiro.png` | Feira de São Cristóvão | Rio de Janeiro (RJ) | Sudeste / Southeast | pavilhão com palco de forró, chapéus de couro e bandeirinhas |
| 10 | `mercados/10-mercado-publico-porto-alegre.png` | Mercado Público | Porto Alegre (RS) | Sul / South | prédio histórico amarelo de dois andares |
| 11 | `mercados/11-mercado-publico-florianopolis.png` | Mercado Público | Florianópolis (SC) | Sul / South | prédio histórico perto do mar com bancas de frutos do mar |
| 12 | `mercados/12-mercado-municipal-curitiba.png` | Mercado Municipal | Curitiba (PR) | Sul / South | mercado coberto com bancas variadas |

Os nomes dos mercados e das cidades ficam em português nas duas versões.

## Itens (13 linhas × 8 níveis = 104)

Na versão em inglês, os nomes tipicamente brasileiros ficam em português e ganham uma explicação curta (coluna *Explicação*), que aparece no jogo ao tocar no item.

### Frutas / Fruits (`fr`)

| Nível | Arquivo | Português | Inglês | Explicação (inglês) | Emoji provisório |
|---|---|---|---|---|---|
| 1 | `itens/fr-1.png` | Limão | Lime |  | 🍋 |
| 2 | `itens/fr-2.png` | Laranja | Orange |  | 🍊 |
| 3 | `itens/fr-3.png` | Banana | Banana |  | 🍌 |
| 4 | `itens/fr-4.png` | Manga | Mango |  | 🥭 |
| 5 | `itens/fr-5.png` | Abacaxi | Pineapple |  | 🍍 |
| 6 | `itens/fr-6.png` | Melancia | Watermelon |  | 🍉 |
| 7 | `itens/fr-7.png` | Uva | Grapes |  | 🍇 |
| 8 | `itens/fr-8.png` | Morango | Strawberry |  | 🍓 |

### Verduras / Veggies (`ve`)

| Nível | Arquivo | Português | Inglês | Explicação (inglês) | Emoji provisório |
|---|---|---|---|---|---|
| 1 | `itens/ve-1.png` | Cheiro-verde | Cheiro-verde | bundle of parsley and green onion, in almost every Brazilian dish | 🌿 |
| 2 | `itens/ve-2.png` | Couve | Collard greens |  | 🥬 |
| 3 | `itens/ve-3.png` | Cenoura | Carrot |  | 🥕 |
| 4 | `itens/ve-4.png` | Tomate | Tomato |  | 🍅 |
| 5 | `itens/ve-5.png` | Milho | Corn |  | 🌽 |
| 6 | `itens/ve-6.png` | Brócolis | Broccoli |  | 🥦 |
| 7 | `itens/ve-7.png` | Abóbora | Pumpkin |  | 🎃 |
| 8 | `itens/ve-8.png` | Salada | Salad |  | 🥗 |

### Peixes / Seafood (`pe`)

| Nível | Arquivo | Português | Inglês | Explicação (inglês) | Emoji provisório |
|---|---|---|---|---|---|
| 1 | `itens/pe-1.png` | Camarão | Shrimp |  | 🦐 |
| 2 | `itens/pe-2.png` | Sardinha | Sardine |  | 🐟 |
| 3 | `itens/pe-3.png` | Peixe | Fish |  | 🐠 |
| 4 | `itens/pe-4.png` | Caranguejo | Crab |  | 🦀 |
| 5 | `itens/pe-5.png` | Lula | Squid |  | 🦑 |
| 6 | `itens/pe-6.png` | Lagosta | Lobster |  | 🦞 |
| 7 | `itens/pe-7.png` | Polvo | Octopus |  | 🐙 |
| 8 | `itens/pe-8.png` | Moqueca | Moqueca | Brazilian fish stew, often with coconut milk and dendê palm oil | 🍲 |

### Temperos / Spices (`te`)

| Nível | Arquivo | Português | Inglês | Explicação (inglês) | Emoji provisório |
|---|---|---|---|---|---|
| 1 | `itens/te-1.png` | Sal | Salt |  | 🧂 |
| 2 | `itens/te-2.png` | Alho | Garlic |  | 🧄 |
| 3 | `itens/te-3.png` | Cebola | Onion |  | 🧅 |
| 4 | `itens/te-4.png` | Pimenta | Chili pepper |  | 🌶️ |
| 5 | `itens/te-5.png` | Pimentão | Bell pepper |  | 🫑 |
| 6 | `itens/te-6.png` | Azeitona | Olive |  | 🫒 |
| 7 | `itens/te-7.png` | Mel | Honey |  | 🍯 |
| 8 | `itens/te-8.png` | Molho | Sauce |  | 🥫 |

### Bebidas / Drinks (`be`)

| Nível | Arquivo | Português | Inglês | Explicação (inglês) | Emoji provisório |
|---|---|---|---|---|---|
| 1 | `itens/be-1.png` | Água | Water |  | 💧 |
| 2 | `itens/be-2.png` | Água de coco | Coconut water |  | 🥥 |
| 3 | `itens/be-3.png` | Suco | Juice |  | 🧃 |
| 4 | `itens/be-4.png` | Café | Coffee |  | ☕ |
| 5 | `itens/be-5.png` | Chá | Tea |  | 🍵 |
| 6 | `itens/be-6.png` | Mate | Mate | herbal tea made from yerba mate leaves | 🧉 |
| 7 | `itens/be-7.png` | Guaraná | Guaraná | soda made from an Amazonian berry | 🥤 |
| 8 | `itens/be-8.png` | Refresco | Fruit cooler |  | 🍹 |

### Artesanato / Crafts (`ar`)

| Nível | Arquivo | Português | Inglês | Explicação (inglês) | Emoji provisório |
|---|---|---|---|---|---|
| 1 | `itens/ar-1.png` | Linha | Thread |  | 🧵 |
| 2 | `itens/ar-2.png` | Novelo | Ball of yarn |  | 🧶 |
| 3 | `itens/ar-3.png` | Meia | Sock |  | 🧦 |
| 4 | `itens/ar-4.png` | Cachecol | Scarf |  | 🧣 |
| 5 | `itens/ar-5.png` | Chapéu de palha | Straw hat |  | 👒 |
| 6 | `itens/ar-6.png` | Cesto | Basket |  | 🧺 |
| 7 | `itens/ar-7.png` | Vaso de barro | Clay pot |  | 🏺 |
| 8 | `itens/ar-8.png` | Viola | Viola caipira | ten-string Brazilian country guitar | 🎸 |

### Armazém / Pantry (`gr`)

| Nível | Arquivo | Português | Inglês | Explicação (inglês) | Emoji provisório |
|---|---|---|---|---|---|
| 1 | `itens/gr-1.png` | Amendoim | Peanuts |  | 🥜 |
| 2 | `itens/gr-2.png` | Castanha-do-pará | Brazil nuts |  | 🌰 |
| 3 | `itens/gr-3.png` | Pipoca | Popcorn |  | 🍿 |
| 4 | `itens/gr-4.png` | Arroz | Rice |  | 🍚 |
| 5 | `itens/gr-5.png` | Mingau | Mingau | warm, creamy porridge | 🥣 |
| 6 | `itens/gr-6.png` | Macarrão | Pasta |  | 🍝 |
| 7 | `itens/gr-7.png` | Sopa | Soup |  | 🍜 |
| 8 | `itens/gr-8.png` | Baião de dois | Baião de dois | rice and beans cooked together with cheese, from Ceará | 🍛 |

### Doces / Sweets (`do`)

| Nível | Arquivo | Português | Inglês | Explicação (inglês) | Emoji provisório |
|---|---|---|---|---|---|
| 1 | `itens/do-1.png` | Bala | Candy |  | 🍬 |
| 2 | `itens/do-2.png` | Pirulito | Lollipop |  | 🍭 |
| 3 | `itens/do-3.png` | Chocolate | Chocolate |  | 🍫 |
| 4 | `itens/do-4.png` | Biscoito | Cookie |  | 🍪 |
| 5 | `itens/do-5.png` | Bolinho | Cupcake |  | 🧁 |
| 6 | `itens/do-6.png` | Sonho | Sonho | cream-filled doughnut; the name means “dream” | 🍩 |
| 7 | `itens/do-7.png` | Doce no palito | Candy on a stick |  | 🍡 |
| 8 | `itens/do-8.png` | Caixa de bombons | Box of chocolates |  | 🎁 |

### Carnes / Meats (`ca`)

| Nível | Arquivo | Português | Inglês | Explicação (inglês) | Emoji provisório |
|---|---|---|---|---|---|
| 1 | `itens/ca-1.png` | Ovo | Egg |  | 🥚 |
| 2 | `itens/ca-2.png` | Frango | Chicken |  | 🍗 |
| 3 | `itens/ca-3.png` | Bacon | Bacon |  | 🥓 |
| 4 | `itens/ca-4.png` | Linguiça | Linguiça | Brazilian pork sausage | 🌭 |
| 5 | `itens/ca-5.png` | Carne | Steak |  | 🥩 |
| 6 | `itens/ca-6.png` | Costela | Ribs |  | 🍖 |
| 7 | `itens/ca-7.png` | Espetinho | Espetinho | street-food skewer grilled on charcoal | 🍢 |
| 8 | `itens/ca-8.png` | Feijoada | Feijoada | black bean and pork stew, a national favorite | 🥘 |

### Laticínios / Dairy (`la`)

| Nível | Arquivo | Português | Inglês | Explicação (inglês) | Emoji provisório |
|---|---|---|---|---|---|
| 1 | `itens/la-1.png` | Leite | Milk |  | 🥛 |
| 2 | `itens/la-2.png` | Manteiga | Butter |  | 🧈 |
| 3 | `itens/la-3.png` | Queijo | Cheese |  | 🧀 |
| 4 | `itens/la-4.png` | Casquinha | Ice cream cone |  | 🍦 |
| 5 | `itens/la-5.png` | Sorvete | Ice cream |  | 🍨 |
| 6 | `itens/la-6.png` | Taça gelada | Sundae |  | 🍧 |
| 7 | `itens/la-7.png` | Torta de creme | Cream cake |  | 🍰 |
| 8 | `itens/la-8.png` | Pudim | Pudim | Brazilian caramel flan made with condensed milk | 🍮 |

### Lanches / Snacks (`ln`)

| Nível | Arquivo | Português | Inglês | Explicação (inglês) | Emoji provisório |
|---|---|---|---|---|---|
| 1 | `itens/ln-1.png` | Pastel | Pastel | crispy fried pastry, the classic street-market snack | 🥟 |
| 2 | `itens/ln-2.png` | Tapioca | Tapioca | crepe made from cassava starch | 🫓 |
| 3 | `itens/ln-3.png` | Sanduíche | Sandwich |  | 🥪 |
| 4 | `itens/ln-4.png` | Batata frita | Fries |  | 🍟 |
| 5 | `itens/ln-5.png` | Pizza | Pizza |  | 🍕 |
| 6 | `itens/ln-6.png` | Hambúrguer | Burger |  | 🍔 |
| 7 | `itens/ln-7.png` | Tapioca recheada | Filled tapioca |  | 🌮 |
| 8 | `itens/ln-8.png` | Marmita | Marmita | home-style packed lunch | 🍱 |

### Padaria / Bakery (`pa`)

| Nível | Arquivo | Português | Inglês | Explicação (inglês) | Emoji provisório |
|---|---|---|---|---|---|
| 1 | `itens/pa-1.png` | Trigo | Wheat |  | 🌾 |
| 2 | `itens/pa-2.png` | Pão de forma | Sandwich loaf |  | 🍞 |
| 3 | `itens/pa-3.png` | Pão francês | Pão francês | crusty bread roll eaten every morning in Brazil | 🥖 |
| 4 | `itens/pa-4.png` | Croissant | Croissant |  | 🥐 |
| 5 | `itens/pa-5.png` | Rosca | Sweet bread ring |  | 🥯 |
| 6 | `itens/pa-6.png` | Panqueca | Pancake |  | 🥞 |
| 7 | `itens/pa-7.png` | Torta | Pie |  | 🥧 |
| 8 | `itens/pa-8.png` | Bolo | Cake |  | 🎂 |

### Flores / Flowers (`fl`)

| Nível | Arquivo | Português | Inglês | Explicação (inglês) | Emoji provisório |
|---|---|---|---|---|---|
| 1 | `itens/fl-1.png` | Muda | Seedling |  | 🌱 |
| 2 | `itens/fl-2.png` | Margarida | Daisy |  | 🌼 |
| 3 | `itens/fl-3.png` | Tulipa | Tulip |  | 🌷 |
| 4 | `itens/fl-4.png` | Girassol | Sunflower |  | 🌻 |
| 5 | `itens/fl-5.png` | Rosa | Rose |  | 🌹 |
| 6 | `itens/fl-6.png` | Hibisco | Hibiscus |  | 🌺 |
| 7 | `itens/fl-7.png` | Vaso | Potted plant |  | 🪴 |
| 8 | `itens/fl-8.png` | Buquê | Bouquet |  | 💐 |

## Personagens (28)

| Arquivo | Nome | Papel (pt) | Papel (en) | Onde aparece | Descrição visual |
|---|---|---|---|---|---|
| `personagens/ze.png` | 👨‍🌾 Seu Zé | feirante e seu guia | market vendor and your guide | viaja com o jogador | homem de uns 60 anos, chapéu de palha, camisa xadrez, avental, sorriso largo |
| `personagens/bia.png` | 👧 Bia | aprendiz da banca | stall apprentice | viaja com o jogador | menina de uns 10 anos, rabo de cavalo, avental pequeno, carregando um caixote |
| `personagens/mingau.png` | 🐈 Mingau | gato da quitanda | the shop cat | viaja com o jogador | gato branco e gordinho, olhar preguiçoso |
| `personagens/tonho.png` | 🚚 Tonho | caminhoneiro | truck driver | viaja com o jogador | caminhoneiro de boné, braço na janela de um caminhão colorido |
| `personagens/naza.png` | 👵 Dona Nazaré | tacacazeira | tacacá soup cook | Ver-o-Peso, Belém | senhora idosa, cabelo grisalho preso, vestido estampado, cuia de tacacá nas mãos |
| `personagens/raimundo.png` | 🧔 Seu Raimundo | pescador | fisherman | Ver-o-Peso, Belém | pescador de barba e chapéu, segurando um peixe de rio |
| `personagens/iara.png` | 👩‍🦱 Iara | artesã | artisan | Mercado Adolpho Lisboa, Manaus | mulher jovem de cabelo cacheado tecendo um cesto de palha |
| `personagens/chico.png` | 🧑‍🌾 Seu Chico | ribeirinho | riverside dweller | Mercado Adolpho Lisboa, Manaus | ribeirinho de chapéu com uma canoa de madeira ao fundo |
| `personagens/dada.png` | 👩🏾‍🍳 Dona Dadá | baiana de tabuleiro | baiana street-food cook | Feira de São Joaquim, Salvador | baiana de acarajé com turbante e saia rodada brancos, tabuleiro de quitutes |
| `personagens/jorginho.png` | 🧑🏾‍🎤 Jorginho | percussionista | percussionist | Feira de São Joaquim, Salvador | rapaz sorridente tocando um tambor de mão |
| `personagens/biu.png` | 👨🏽‍🎨 Mestre Biu | ceramista | master potter | Mercado de São José, Recife | artesão mais velho moldando um bonequinho de barro |
| `personagens/flor.png` | 👩🏽 Maria Flor | rendeira | lacemaker | Mercado de São José, Recife | mulher com uma almofada de renda de bilro no colo |
| `personagens/cicero.png` | 👨🏽‍🌾 Seu Cícero | vendedor de frutas | fruit seller | Mercado Central, Fortaleza | vendedor de frutas de chapéu de couro com um carrinho de frutas |
| `personagens/rosinha.png` | 👧🏽 Rosinha | neta da rendeira | the lacemaker’s granddaughter | Mercado Central, Fortaleza | menina de vestido de chita florida e laço no cabelo |
| `personagens/keiko.png` | 👩🏻‍🍳 Dona Keiko | cozinheira de sobá | sobá noodle cook | Feira Central, Campo Grande | cozinheira nipo-brasileira de avental com uma tigela de sobá fumegante |
| `personagens/antenor.png` | 🤠 Seu Antenor | peão pantaneiro | Pantanal cowboy | Feira Central, Campo Grande | peão pantaneiro de chapéu e lenço no pescoço, com uma guampa de tereré |
| `personagens/giuseppe.png` | 👨🏻‍🍳 Seu Giuseppe | dono da lanchonete | snack bar owner | Mercadão, São Paulo | dono de lanchonete de bigode e avental, com um sanduíche de mortadela enorme |
| `personagens/paula.png` | 👩🏻‍💼 Paula | sempre apressada | always in a rush | Mercadão, São Paulo | mulher em roupa de escritório, celular na mão, andando apressada |
| `personagens/geralda.png` | 👵🏽 Dona Geralda | quitandeira mineira | quitandeira from Minas | Mercado Central, Belo Horizonte | senhora mineira de avental com bule de café e pão de queijo |
| `personagens/tiao.png` | 🧑🏽‍🍳 Tiãozinho | queijeiro | cheesemaker | Mercado Central, Belo Horizonte | rapaz de chapéu segurando uma peça de queijo minas curado |
| `personagens/jacinto.png` | 👨🏾‍🦳 Seu Jacinto | sanfoneiro | accordion player | Feira de São Cristóvão, Rio de Janeiro | sanfoneiro mais velho de chapéu de couro tocando sanfona |
| `personagens/dandara.png` | 👩🏾 Dandara | cozinheira | cook | Feira de São Cristóvão, Rio de Janeiro | cozinheira de lenço na cabeça mexendo uma panela grande |
| `personagens/gaudencio.png` | 🧔🏻 Seu Gaudêncio | assador | churrasco grill master | Mercado Público, Porto Alegre | gaúcho de bombacha, lenço e boina, com um espeto de churrasco |
| `personagens/livia.png` | 👩🏼 Lívia | dona da cuia | keeper of the mate gourd | Mercado Público, Porto Alegre | jovem gaúcha com cuia de chimarrão e garrafa térmica |
| `personagens/dico.png` | 🧑🏼‍🦰 Dico | pescador | fisherman | Mercado Público, Florianópolis | pescador com uma rede de pesca no ombro |
| `personagens/zulma.png` | 👩🏼‍🦳 Dona Zulma | florista | florist | Mercado Público, Florianópolis | senhora florista com um balde de flores |
| `personagens/halina.png` | 👩🏼‍🍳 Dona Halina | cozinheira | cook | Mercado Municipal, Curitiba | cozinheira de origem polonesa, lenço na cabeça, prato de pierogi |
| `personagens/estanislau.png` | 👨🏻‍🦳 Seu Estanislau | vendedor do armazém | general store keeper | Mercado Municipal, Curitiba | senhor de avental atrás do balcão do armazém |

Os nomes dos personagens não são traduzidos. As falas em inglês mantêm expressões regionais (*égua*, *oxente*, *uai*, *bah*, *tchê*) como toque de cultura local.

## Extras: decoração da banca (12)

Aparecem na banca da tela inicial.

| Arquivo | Português | Inglês | Emoji provisório |
|---|---|---|---|
| `decoracao/01-toldo-listrado.png` | Toldo listrado | Striped awning | ⛱️ |
| `decoracao/02-vasos-de-ervas.png` | Vasos de ervas | Herb pots | 🪴 |
| `decoracao/03-banco-de-madeira.png` | Banco de madeira | Wooden bench | 🪑 |
| `decoracao/04-lousa-de-precos.png` | Lousa de preços | Price chalkboard | 📋 |
| `decoracao/05-balanca-antiga.png` | Balança antiga | Vintage scale | ⚖️ |
| `decoracao/06-luzinhas.png` | Luzinhas | String lights | ✨ |
| `decoracao/07-radio-de-pilha.png` | Rádio de pilha | Transistor radio | 📻 |
| `decoracao/08-bicicleta-de-entrega.png` | Bicicleta de entrega | Delivery bike | 🚲 |
| `decoracao/09-carrinho-de-feira.png` | Carrinho de feira | Market trolley | 🛒 |
| `decoracao/10-relogio-de-parede.png` | Relógio de parede | Wall clock | 🕰️ |
| `decoracao/11-bandeirinhas.png` | Bandeirinhas | Bandeirinhas (festa junina flags) | 🎊 |
| `decoracao/12-caminha-do-mingau.png` | Caminha do Mingau | Mingau’s cat bed | 🐈 |

## Sugestão antes de gerar a arte

Algumas linhas ainda têm itens genéricos (uva, morango, croissant, tulipa, pizza, hambúrguer). Se a ideia é mostrar o Brasil para o mundo, este é o melhor momento para trocá-los, antes de gastar com imagens. Candidatos: **caju, acerola, jabuticaba, cupuaçu e açaí** (Frutas); **pão de queijo** (Padaria); **coxinha e acarajé** (Lanches); **brigadeiro, cocada e rapadura** (Doces); **ipê** (Flores); **cuscuz** (Armazém). Para trocar, basta editar `LINES` no início do script do jogo e gerar esta lista de novo.
