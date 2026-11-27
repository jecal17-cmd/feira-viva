# Feira Viva — Design de Jogo (2 versões)

Rascunho v0.3 · 10 de novembro de 2026 · Base para o primeiro prompt do Claude Code

## 1. Visão geral

Duas versões do mesmo jogo de merge com tema de feiras brasileiras. Compartilham o motor (tabuleiro, fusão, pedidos) e diferem em progressão, dificuldade e monetização.

| | A · Rota das Feiras | B · Quitanda Zen |
|---|---|---|
| Perfil | Puzzle com estratégia, “cara de jogo” | Passatempo relaxante |
| Estrutura | Fases com turnos limitados, mapa do Brasil | Tabuleiro contínuo, sem fim de jogo |
| Progressão | Média, por mercados e Selos de Domínio | Muito lenta (~50 h até o nível 50, estimativa) |
| Receita | Compras no app (gemas, passe, assinatura) | Anúncios (recompensados + intersticiais) |
| Principal risco | Muito conteúdo e balanceamento | Depende de volume de usuários e da fadiga de anúncios |

**Aviso honesto:** manter as duas versões dobra conteúdo, testes e publicação. Minha recomendação é construir o núcleo comum uma vez, validar uma das versões com jogadores reais e só então decidir se vale ramificar. Todos os números abaixo são pontos de partida para teste, não valores comprovados.

## 2. Núcleo comum (as duas versões)

**Itens.** Cada item tem uma linha (ex.: Açaí) e um nível (1 a 5 na Versão A, 1 a 6 na B). Arrastar um item sobre outro de mesma linha e nível funde os dois em um item de nível +1 na célula de destino; a origem fica vazia. Itens no nível máximo não fundem, só são entregues.

**Fusão tripla.** Só acontece por escolha do jogador: ao arrastar um item, se o dedo passar por cima de um item idêntico e soltar em outro idêntico vizinho dele (4 direções), os três se juntam e o resultado sobe +2 níveis. As duas células ficam destacadas durante o arraste. Soltar direto sobre um item, ou juntar por toque, funde só dois, mesmo que haja um terceiro igual ao lado. Recompensa o planejamento do tabuleiro sem gastar itens sem querer.

**Cesto (gerador).** Um toque gera um item nível 1 da linha do cesto em uma célula vazia aleatória. Sem célula vazia, não gera.

**Pedidos.** Clientes pedem itens específicos (linha + nível). Arrastar o item até o cliente entrega e paga a recompensa.

**Salvamento.** Estado local em JSON, versionado, restaurado ao abrir o jogo.

**Dados fora do código.** Fases, itens, preços e recompensas ficam em arquivos de dados, para ajustar balanceamento sem mexer no código.

## 3. Versão A — Rota das Feiras (gamer, foco em compras no app)

### 3.1 Loop e regras de fase

- **Turno** = um toque no cesto. Fusões e entregas não gastam turno. Isso faz o turno ser o recurso escasso e o espaço do tabuleiro ser a pressão.
- **Tabuleiro** 6×7 (42 células). A fase começa com 8 a 12 itens pré-posicionados.
- **Limite de turnos:** de 18 a 30, conforme a fase. Obstáculos avançam por turno.
- **Objetivos** (um ou dois por fase): entregar N pedidos; criar um item de nível X de uma linha; limpar N obstáculos; sobreviver N turnos (chefes).
- **Derrota:** os turnos acabam sem cumprir o objetivo, ou o tabuleiro trava (nenhuma célula livre para gerar e nenhuma fusão possível).
- **Estrelas:** 1★ ao cumprir o objetivo; 2★ com pelo menos 25% dos turnos sobrando; 3★ com pelo menos 50%.
- **Vidas:** 5, regeneram 1 a cada 25 min. Nas primeiras 15 fases a derrota não gasta vida (onboarding).

### 3.2 Mapa do Brasil

5 regiões, 12 mercados, 7 fases por mercado (6 normais + 1 chefe) = 84 fases. Um mercado abre ao vencer o chefe do anterior; uma região nova exige um mínimo de estrelas (ex.: 30 para sair do Norte).

| Região | Mercado | Linhas de itens | Selo de Domínio |
|---|---|---|---|
| Norte | Ver-o-Peso (Belém) | Açaí, Peixe, Jambu/Tucupi | Força do Açaí: +3 turnos em toda fase |
| Norte | Mercado Adolpho Lisboa (Manaus) | Guaraná, Pirarucu, Cupuaçu | Guaraná: a cada 10 fusões, +1 turno |
| Nordeste | Feira de São Joaquim (Salvador) | Feijão-fradinho, Camarão, Coco | Dendê: a 1ª fusão de cada fase sobe +1 nível extra |
| Nordeste | Mercado de São José (Recife) | Carne de sol, Queijo coalho, Cana (implementado: seção 3.16) | Carne de Sol: Despensa com 2 vagas para guardar itens fora do tabuleiro |
| Nordeste | Mercado Central de Fortaleza | Caju, Tapioca, Rapadura | Cajuína: ignora o 1º obstáculo de cada fase |
| Centro-Oeste | Feira Central de Campo Grande | Sobá, Chipa, Tereré | Sobá: pedidos ganham +50% de prazo |
| Sudeste | Mercadão de São Paulo | Mortadela, Pastel, Frutas | Mortadela: 25% de chance de gerar item nível 2 grátis ao entregar pedido |
| Sudeste | Mercado Central de BH | Queijo minas, Doce de leite, Pão de queijo | Queijo Minas: 1 Caldeirão grátis por fase |
| Sudeste | Feira de São Cristóvão (Rio) | Feijão, Carne-seca, Cuscuz | Forró: 3 fusões seguidas sem gerar devolvem 1 turno |
| Sul | Mercado Público de Porto Alegre | Erva-mate, Queijo colonial, Churrasco | Chimarrão: obstáculos congelados por 2 turnos no início da fase |
| Sul | Mercado Público de Florianópolis | Ostra, Berbigão, Tainha | Pérola: 5% de chance de a fusão sair +1 nível |
| Sul | Mercado Municipal de Curitiba | Pinhão, Barreado, Pierogi | Pinhão: pedidos exigem 1 item a menos (mínimo 1) |

*Nomes de mercados, produtos e pratos devem ser validados com pesquisa local antes de produzir a arte. O Centro-Oeste ganha um segundo mercado (ex.: Goiânia) depois da validação.*

**Exemplo de linhas (Ver-o-Peso):**

| Nível | Açaí | Peixe | Jambu/Tucupi |
|---|---|---|---|
| 1 | Cacho de açaí | Peixe pequeno | Folha de jambu |
| 2 | Fruto | Peixe limpo | Maço de jambu |
| 3 | Polpa | Filé | Caldo de tucupi |
| 4 | Açaí batido | Peixe assado | Tacacá |
| 5 | Tigela de açaí com tapioca | Pirarucu de casaca | Pato no tucupi |

### 3.3 Obstáculos por região

Um obstáculo novo é apresentado por região, com mini-tutorial na primeira fase.

| Região | Obstáculo | Regra |
|---|---|---|
| Todas | Caixote | Célula bloqueada; abre quando ocorre uma fusão em célula adjacente e deixa o item que guardava. |
| Norte | Mofo | A cada 3 turnos, um item adjacente a um mofo fica mofado e não funde. Limpa com fusão adjacente. |
| Nordeste | Sol forte | Células marcadas: item de nível 3 ou mais parado ali por 5 turnos perde 1 nível. |
| Centro-Oeste | Fila impaciente | Pedidos têm prazo de 6 turnos; se vence, o cliente vai embora e você perde 2 turnos. |
| Sudeste | Horário de pico | A cada 3 turnos surge uma Sacola em célula vazia aleatória; ocupa espaço até uma fusão adjacente. |
| Sul | Minuano | A cada 5 turnos a linha de cima gira 1 coluna para a direita (o item que sai volta pela esquerda). |

### 3.4 Boosters

Máximo de 2 boosters por fase. Obtidos por recompensas de fase, baús gratuitos de estrelas e compras.

- **Martelo:** remove 1 item ou obstáculo.
- **Ímã:** escolhe um item; todos os iguais a ele (mesma linha e nível) se movem para as células vazias mais próximas dele.
- **Caldeirão:** +1 nível em um item (até o nível 4).
- **Geladeira:** congela os obstáculos por 3 turnos.
- **+3 Turnos:** só por compra ou recompensa rara.

### 3.5 Selos de Domínio (a progressão “gamer”)

- **Como ganhar:** entregar pelo menos 3 itens nível 5 de cada linha do mercado (acumulado) e vencer o chefe.
- **Selo nível 2:** 3★ em todas as fases do mercado intensifica o efeito (ex.: +3 turnos vira +5).
- **Mochila de Selos:** 1 vaga no início; 2ª ao concluir o Norte; 3ª ao concluir o Nordeste. Antes de cada fase o jogador escolhe quais Selos levar. Isso cria a decisão estratégica.
- **Regra de ouro:** Selos só são ganhos jogando, nunca vendidos. Vendê-los transformaria o jogo em pay-to-win e destruiria a graça da escolha.
- **Balanceamento:** testar combinações (ex.: Força do Açaí + Guaraná empilham turnos). Cada efeito deve ser útil, mas nenhum obrigatório.

### 3.6 Chefes

Um por mercado, com regra própria e objetivo de entregar ou sobreviver. Exemplos:

- **Ver-o-Peso, “Maré cheia”:** a cada 4 turnos a linha de baixo é alagada; itens ali ficam presos por 2 turnos. Objetivo: entregar 5 pedidos em 28 turnos.
- **Mercadão, “Domingo de pico”:** surge uma Sacola a cada 2 turnos; 6 pedidos grandes em 30 turnos.

### 3.7 Economia e monetização (foco em compras)

Moedas são grátis (fases, pedidos, baús de estrelas). Gemas vêm de compras e eventos raros.

| Produto | Preço sugerido (hipótese a testar) | Observação |
|---|---|---|
| Pacote do Feirante (1 vez) | R$ 9,90 | gemas + 3 boosters + 1 h de vidas ilimitadas |
| Pacotes de gemas (5 faixas) | R$ 4,90 a R$ 99,90 | bônus crescente nas faixas maiores |
| Turnos extras ao perder | 10 gemas por +5 turnos (máx. 2 por fase) | principal ponto de conversão |
| Vidas | 5 vidas por gemas ou vidas ilimitadas por 1 h | |
| Passe da Temporada (30 dias) | R$ 19,90 premium; trilha gratuita | cosméticos + boosters |
| Feirante VIP (assinatura) | R$ 14,90 por mês | sem anúncios, 1 booster por dia, +2 vidas |
| Cosméticos | R$ 4,90 a R$ 14,90 | skins de barraca, avatares |

**Cuidados:**

- Evite baús aleatórios pagos: geram risco regulatório e de reputação. Verifique as regras atuais das lojas e a legislação brasileira (por exemplo, o ECA Digital trata de caixas de recompensa) antes de decidir.
- Anúncios na Versão A: só recompensados e opcionais (vida extra, +2 turnos uma vez por fase).
- Preços claros, sem contadores enganosos, controle parental e definição de classificação indicativa.

### 3.8 Métricas a acompanhar

Retenção D1/D7/D30, conversão em pagantes, ARPPU, taxa de derrota por fase. Heurística minha: fases com derrota acima de 60% ou abaixo de 10% pedem ajuste.

### 3.9 Protótipo de teste (v0.1)

Implementado em `versao-a-rota-das-feiras/`, seguindo o marco 2 (seção 7), com estas decisões e números iniciais:

| Fase | Objetivos | Turnos | Obstáculos |
|---|---|---|---|
| 1 · Bom dia, Ver-o-Peso | entregar 4 pedidos | 14 | — |
| 2 · Caixotes no caminho | criar Açaí batido (nível 4) + limpar 3 obstáculos | 15 | 4 caixotes |
| 3 · Chegou o jambu | entregar 6 pedidos | 17 | 3 caixotes |
| 4 · Cuidado com o mofo | limpar 4 obstáculos + entregar 4 pedidos | 16 | 2 caixotes, 2 mofos |
| 5 · Pirarucu de casaca | criar Pirarucu de casaca (nível 5) | 21 | 2 caixotes, 2 mofos |
| 6 · Hora do almoço | entregar 6 pedidos + limpar 3 obstáculos | 25 | 2 caixotes, 3 mofos |
| Chefe · Maré cheia | entregar 6 pedidos | 24 | 2 caixotes, 1 mofo, maré |

- **Item mofado** não junta e não pode ser entregue; uma fusão ao lado limpa. Uma fusão ao lado de um caixote ou de um foco de mofo o remove.
- **Maré cheia:** a cada 4 turnos, a fileira de baixo fica alagada por 2 turnos (itens presos e sem colheita ali).
- **Selo de Domínio:** os itens de nível 5 vão para um espaço próprio (🏅); 3 de cada linha + chefe vencido dão o Selo Força do Açaí.
- **Sem vidas** neste teste (as 15 primeiras fases não gastariam vida de qualquer forma), sem gemas e sem anúncios. Moedas vêm das vitórias e compram ferramentas.
- **Balanceamento inicial** feito com um robô que joga cada fase 300 vezes: vence quase sempre as fases 1 a 5 e cerca de 55% a 65% das fases 6 e chefe. Os números devem ser ajustados com o painel de teste (taxa de derrota por fase) e jogadores reais.

**Versão em inglês (protótipo):** mesmo arquivo, com o idioma do navegador ou `?lang=en`. Ficam em português os nomes do jogo, dos mercados, das cidades, dos clientes e dos pratos típicos (tacacá, pato no tucupi, pirarucu de casaca), com explicação curta ao tocar no item; "Selo de Domínio" vira *Mastery Seal* e "Força do Açaí" vira *Açaí Power*. Os textos do Diário também foram traduzidos e precisam de revisão por falante nativo, além da checagem de fatos.

### 3.10 Loja do protótipo (compras simuladas)

A pedido, o protótipo ganhou uma loja com preços de US$ 0,50 a US$ 9,99. As compras são simuladas (nada é cobrado); no app publicado passariam pela cobrança da loja do celular. Selos de Domínio e cartões do Diário continuam fora da loja, e não há caixas aleatórias pagas.

**Valor de referência (item avulso):** 150 moedas = US$ 0,50 · Martelo = US$ 0,33 · Caldeirão = US$ 0,33 · +3 Turnos = US$ 0,50. A "economia" de cada kit é calculada sobre esses valores.

| Produto | Conteúdo | Preço | Economia |
|---|---|---|---|
| Kit do Feirante (1 vez) | 300 moedas, 2 Martelos, 2 Caldeirões, 2 × +3 Turnos | US$ 1,99 | 40% |
| Kit Maré Cheia | 2 Martelos, 2 Caldeirões, 4 × +3 Turnos | US$ 2,49 | 25% |
| Kit Mestre da Feira | 1.500 moedas, 5 de cada ferramenta | US$ 5,99 | 45% |
| Kit Banca Completa | 4.000 moedas, 10 de cada ferramenta | US$ 9,99 | 60% |
| +3 Turnos | 1 / 3 / 10 | US$ 0,50 / 1,29 / 3,99 | — / 14% / 20% |
| Martelo ou Caldeirão | 3 | US$ 0,99 | — |
| Moedas | 150 / 500 / 1.200 / 2.500 / 6.000 | US$ 0,50 / 1,49 / 2,99 / 4,99 / 9,99 | bônus de 0 / 12 / 34 / 67 / 100% |

- **+3 Turnos** é a ferramenta nova, só da loja (seção 3.4). Pode ser usada durante a fase (conta no limite de 2 ferramentas) ou ao ficar sem turnos, para continuar (até 2 vezes por fase). Esse é o principal ponto de conversão previsto na seção 3.7.
- **Pedidos** agora rendem moedas (2 por nível de item entregue), mesmo quando não fazem parte do objetivo.
- **Objetivo em destaque:** o painel "Para vencer a fase" mostra só o que libera a próxima fase; os pedidos ganham o rótulo "contam para vencer" ou "extras", os obstáculos pulsam quando limpar é objetivo e o cesto da linha a criar leva um 🎯.
- **A observar:** neste teste as moedas só compram Martelo e Caldeirão, então os kits grandes de moedas têm pouco uso; vale criar mais usos para moedas antes de publicar.

### 3.11 Segundo mercado: Mercado Adolpho Lisboa, Manaus (novembro de 2026)

Como na Quitanda, a Rota ganhou o segundo mercado. Ele abre ao vencer o chefe do Ver-o-Peso (o progresso continua na mesma lista de fases: o Manaus usa as fases 8 a 14 da lista, então saves antigos seguem valendo).

**Linhas novas (5 níveis cada).** A arte própria entrou em 26/11/2026 (antes reaproveitava itens 3D da Quitanda; lista em `docs/arte/lista-de-arte.md`).

| Nível | Peixes do rio (`pr`) | Mandioca (`md`) | Frutas (`fr`) |
|---|---|---|---|
| 1 | Camarão regional | Mandioca | Castanha-do-pará |
| 2 | Jaraqui | Farinha do Uarini | Banana pacovã |
| 3 | Pirarucu | Goma de tapioca | Abacaxi |
| 4 | Caldeirada de tambaqui | Tapioca | Suco de frutas |
| 5 | Prato do mercado | Tapioquinha de tucumã | Guaraná |

**Fases:**

| Fase | Objetivos | Turnos | Linhas | Obstáculos |
|---|---|---|---|---|
| 1 · Bem-vindo a Manaus | entregar 5 pedidos | 16 | Peixes, Mandioca | 2 caixotes |
| 2 · Farinha do Uarini | criar Tapioca (nível 4) + limpar 3 obstáculos | 17 | Peixes, Mandioca | 3 caixotes, 1 mofo |
| 3 · Chegou o guaraná | entregar 6 pedidos | 18 | as três | 3 caixotes, 1 mofo |
| 4 · Chuva na feira | limpar 5 obstáculos + entregar 4 pedidos | 18 | as três | 2 caixotes, 3 mofos |
| 5 · Guaraná gelado | criar Guaraná (nível 5) | 22 | as três | 2 caixotes, 2 mofos |
| 6 · Almoço no Mercadão | entregar 7 pedidos + limpar 3 obstáculos | 27 | as três | 2 caixotes, 3 mofos |
| Chefe · Encontro das Águas | entregar 6 pedidos | 25 | as três | 2 caixotes, 2 mofos, rios |

- **Chefe Encontro das Águas:** a cada 4 turnos, os rios Negro e Solimões sobem nas duas colunas das pontas do tabuleiro por 2 turnos (itens presos, sem colheita ali). É a mesma regra da Maré cheia, aplicada às colunas.
- **Selo Guaraná:** 3 itens de nível 5 de cada linha de Manaus + chefe vencido. Efeito: a cada 10 fusões numa fase, +1 turno (o contador aparece no topo da fase). A mochila leva os dois selos do Norte; cada um tem a sua caixa para levar ou não.
- **Diário:** 7 cartões novos (Mercado Adolpho Lisboa, Jaraqui, Farinha do Uarini, Tucumã, Tambaqui, Guaraná, Encontro das Águas), a validar com pesquisa e revisão local. Completar os cartões de um mercado rende 150 moedas (antes era só o Ver-o-Peso).
- **Balanceamento:** comparado com um robô simples que joga cada fase 300 vezes, cada fase de Manaus fica perto da fase de mesmo número do Ver-o-Peso (a 6 um pouco mais difícil, o chefe parecido). Ajustar com o painel do teste, que agora separa as fases por mercado.

### 3.12 Música, volume e banca (novembro de 2026)

- **Música:** a Rota toca a mesma trilha da Quitanda para cada mercado (`musica/01.ogg` no Ver-o-Peso, `02.ogg` em Manaus), em loop e com troca suave ao mudar de mercado. Começa no primeiro toque na tela. Liga e desliga em Ajustes.
- **Volume (Quitanda e Rota):** em Ajustes, Som e Música têm cada um a sua barra de 0 a 100%, além do botão Ligado/Desligado. A música muda de volume na hora; ao soltar a barra do som, toca uma moedinha de amostra. Na Quitanda, a música deixou de depender do botão Som.
- **Banca da tela inicial (Rota):** no lugar da foto do Ver-o-Peso, a tela inicial mostra a banca da Quitanda (toldo nas cores da Rota, sem decorações). Começa vazia e cada linha com ingrediente descoberto no Álbum vira uma fileira no tampo, em duas colunas. Desde 26/11/2026 o arranjo é dinâmico, igual ao da Quitanda (seção 4.13); antes o espaço entre fileiras era fixo e, com Salvador, a 5ª fileira sumia atrás do toldo.

### 3.13 Eventos (novembro de 2026; valem para a Rota e a Quitanda)

Mecânica reutilizável de eventos temporários, com o mesmo código nos dois jogos (bloco `EVENTOS` no `index.html` de cada um).

- **Calendário:** a lista `EVENTOS` fica dentro do app. Cada evento tem `id`, início (`from`), fim (`to`, em horário de Brasília), ícone, cor, nome, texto e 4 prêmios. O jogo escolhe o evento que estiver no período pelo **relógio do aparelho** (quem adiantar o relógio só ganha tempo para si). Para criar o Carnaval: acrescentar um item à lista (e, na Rota, 4 fases com `ev` e `evn` em `PHASES`). Como as datas ficam no app, cada evento novo precisa de uma atualização na loja.
- **Botão flutuante:** pílula no canto superior direito das telas iniciais, com o ícone do tema e o tempo que falta ("14d 13h", depois "5h 20min", depois "mm:ss"). Some sozinho quando o evento acaba e fica escondido durante as partidas.
- **Pop-up do evento:** abre ao tocar no botão e, uma vez por evento, sozinho na primeira vez que o jogador chega à tela inicial. Mostra o tempo que falta, as 4 etapas com o prêmio de cada uma e os prêmios já conquistados. Também abre por **Ajustes > Eventos**, mesmo sem evento ativo (mostra a coleção e a data do próximo evento).
- **Etapas e prêmios exclusivos:** as 4 etapas são feitas na ordem e cada uma libera um prêmio exclusivo. Na **Rota**, são 4 fases especiais (só jogáveis durante o evento; vencer dá o prêmio, e jogar de novo não repete). Na **Quitanda**, que não tem fases, são 4 metas de jogo que contam enquanto o evento está ativo, uma por vez.
- **Para sempre:** os prêmios ficam em `S.ev.got` (`"idDoEvento:idDoPrêmio"`), valem depois do evento e **sobrevivem a "Recomeçar do zero"**. Quem não conseguiu durante o evento só poderá se o evento voltar (basta repetir as datas).
- **O que o prêmio faz hoje:** aparece na banca da tela inicial (emojis sobre o tampo) e na coleção do pop-up. Na Quitanda, receitas e itens também entram no Caderno de Receitas (seção "Dos eventos") e **cada prêmio dá +1% de XP**, como as decorações. Não há ainda uma linha nova de itens jogáveis por evento (seria o próximo passo, com arte própria).

**Evento de Natal na Feira (10/12/2026 a 26/12/2026):**

| Etapa | Prêmio | Rota (fase) | Quitanda (meta) |
|---|---|---|---|
| 1 | 🍞 Panetone (item) | Cesta de Natal: 5 pedidos, 17 turnos | Atenda 8 pedidos |
| 2 | 🍮 Rabanada (receita) | Rabanada dourada: criar Tapioca (nível 4) + limpar 2, 20 turnos | Faça 40 fusões |
| 3 | 🥘 Farofa natalina (receita) | Ceia na beira do rio: 6 pedidos + limpar 3, 22 turnos | Colha 50 itens dos cestos |
| 4 | 🎄 Enfeites de Natal (decoração) | Grande ceia de Natal: 7 pedidos + limpar 3, 26 turnos | Crie 2 itens de nível 5 ou mais |

Balanceamento da Rota (robô simples, 300 partidas por fase): etapas 1, 3 e 4 com 100%, 93% e 44% de vitória; a etapa 2 (meta de criar item) segue o padrão das outras fases desse tipo, em que o robô vai mal. As metas da Quitanda ainda não foram medidas com jogadores. Os textos dos prêmios precisam de revisão cultural, como os demais.

### 3.14 Arte e regra do caixote e do mofo (novembro de 2026)

- **Arte:** o caixote e o mofo trocaram os desenhos feitos em CSS por pixel art em 5 quadros (`versao-a-rota-das-feiras/obstaculos/caixa-1..5.webp` e `mofo-1..5.webp`). O quadro 1 é o obstáculo parado no tabuleiro; os seguintes animam a remoção (caixa racha, estoura e vira lascas; a esponja esfrega o mofo até sumir). O item mofado ganha uma camada translúcida do mofo, no lugar do 🦠, e, ao ser limpo, aparece a esponja passando. Originais e o script de recorte em `docs/arte/obstaculos/`.
- **Regra nova:** todo caixote guarda um item embaixo (nível 1 em 70% das vezes, nível 2 nas demais, de uma das linhas da fase). Ao quebrar, por fusão ao lado ou pelo Martelo, o item fica na casa. O Martelo no mofo continua só removendo. O balanceamento das fases não foi refeito com o robô: o caixote agora dá material de graça, o que deve facilitar um pouco as fases com muitos caixotes.

### 3.15 Terceiro mercado: Feira de São Joaquim, Salvador (novembro de 2026)

Primeiro mercado do Nordeste. Abre ao vencer o chefe de Manaus. As fases ficam no fim da lista `PHASES` (posições 18 a 24, depois das 4 fases do Natal), então os saves antigos seguem valendo. A regra de desbloqueio passou a olhar a fase anterior **do mesmo mercado** e, na primeira fase, o chefe do mercado anterior (antes olhava a posição anterior da lista, o que quebraria com o evento no meio).

**Ideia central: o sol anda.** O Norte era água (maré, rios). A Bahia é calor e movimento: o sol atravessa o tabuleiro, e o jogador precisa planejar onde deixa os itens grandes.

**Linhas novas (5 níveis, arte 3D própria):**

| Nível | Fradinho (`ff`) | Camarão (`cm`) | Coco (`cc`) |
|---|---|---|---|
| 1 | Feijão-fradinho | Camarão fresco | Coco verde |
| 2 | Fradinho de molho | Camarão seco | Coco seco |
| 3 | Massa de acarajé | Vatapá | Coco ralado |
| 4 | Abará | Bobó de camarão | Leite de coco |
| 5 | Acarajé | Moqueca de camarão | Cocada |

**Regras novas:**

- **☀️ Sol forte** (o obstáculo do Nordeste, seção 3.3): uma faixa de 2 colunas fica ao sol. Um item de **nível 3 ou mais** parado ali soma 1 de calor por turno; com 5, perde 1 nível. O número 🔥 no item mostra quantos turnos faltam. Sair do sol zera o calor; juntar cria um item novo, sem calor. Níveis 1 e 2 não sofrem. Nas fases 5, 6 e no chefe, **o sol anda 1 coluna para a direita a cada 4 turnos** (e volta pela esquerda). Constantes `SUN_HEAT` e `SUN_LV`.
- **⛱️ Toldo** (ferramenta nova): faz sombra em 4 casas (2 × 2) até o fim da fase; casas com sombra não esquentam, mesmo quando o sol passa. Custa 🪙 100 no mercado (só moedas, nunca dinheiro real), conta no limite de 2 ferramentas por fase e só aparece nas fases com sol. O tutorial da fase 5 dá 2 Toldos. É um uso novo para as moedas, que tinham pouco uso (seção 3.10).
- **🥥 Engradado de coco:** caixote reforçado. A 1ª fusão ao lado racha (quadro 2 da arte), a 2ª abre; o Martelo abre de uma vez. Dentro vem um Coco seco. Só conta como obstáculo limpo quando abre.
- **👩🏾‍🍳 Pedido da Dona Dadá:** pedido especial de 2 itens de linhas diferentes, com prazo (⏱️) de 8 turnos. Atender dá **+2 turnos** e moedas em dobro e conta também como pedido comum. Se o prazo acabar, ela vai embora sem castigo. Ela ocupa o lugar do pedido com menos itens entregues e só há uma por vez; aparece a cada 5 a 7 turnos, conforme a fase. Nas fases com a Dadá, ela não aparece como cliente comum.
- **⛵ Chefe Chegada do saveiro:** a cada 5 turnos, um saveiro passa pela esquerda e deixa 3 engradados de coco nas casas livres mais à esquerda (`SAVEIRO_*`). O sol continua andando e a Dona Dadá aparece a cada 6 turnos.
- **🌴 Selo Dendê:** 3 itens de nível 5 de cada linha de Salvador + chefe vencido. A 1ª fusão de cada fase sobe 1 nível extra (indicador 🌴 no topo da fase). A mochila leva os três selos.

**Fases:**

| Fase | Objetivo | Turnos | Linhas | Obstáculos e regras |
|---|---|---|---|---|
| 1 · Bom dia, Salvador | entregar 5 pedidos | 16 | Fradinho, Camarão | 2 caixotes |
| 2 · O sol da Bahia | criar Abará (nível 4) | 17 | Fradinho, Camarão | 2 caixotes, sol parado (tutorial) |
| 3 · Chegou o coco | entregar 6 pedidos | 18 | as três | 1 caixote, 3 engradados, sol parado (tutorial) |
| 4 · Tabuleiro da baiana | 3 pedidos da Dona Dadá + 5 pedidos | 19 | as três | 2 caixotes, 1 engradado, Dadá a cada 5 turnos (tutorial) |
| 5 · O sol anda | criar Moqueca de camarão (nível 5) | 23 | as três | 2 caixotes, 2 engradados, sol que anda, Toldo (tutorial) |
| 6 · Hora do acarajé | entregar 7 pedidos + limpar 4 | 25 | as três | 2 caixotes, 2 engradados, sol que anda, Dadá a cada 7 |
| Chefe · Chegada do saveiro | 7 pedidos, 2 deles da Dona Dadá | 22 | as três | 1 caixote, 1 engradado, sol que anda, Dadá a cada 6, saveiro |

**Balanceamento.** Um robô simples (entrega, foge do sol, junta e colhe o que os pedidos pedem, sem ferramentas nem selos) jogou cada fase 300 vezes. Para comparar, o mesmo robô jogou os mercados anteriores:

| Fase | Ver-o-Peso | Manaus | Salvador |
|---|---|---|---|
| 1 | 100% | 100% | 100% |
| 2 | 32% | 10% | 40% |
| 3 | 95% | 97% | 97% |
| 4 | 32% | 37% | 70% |
| 5 | 28% | 28% | 26% |
| 6 | 82% | 60% | 68% |
| Chefe | 70% | 73% | 70% |

Esse robô vai mal em metas de criar item e de limpar obstáculos (fases 2 e 5), como já se via na seção 3.11; o que vale é a comparação entre mercados. A fase 4 ficou mais fácil de propósito, por ser o tutorial da Dona Dadá. Os engradados do saveiro precisavam de 2 fusões: com 1 só, o chefe ficava com 86% (os cocos de dentro viravam material de graça).

**Diário:** 7 cartões novos (Feira de São Joaquim, Feijão-fradinho, Coco, Baianas de acarajé, Moqueca baiana, Azeite de dendê, Saveiros), a validar com pesquisa e revisão local. Cada cartão agora guarda a fase a que pertence (`ph`), porque as fases do evento ficam no meio da lista.

**Arte e música:** itens 3D próprios, engradado e sol em pixel art (como o caixote e o mofo), toldo e saveiro; prompts em `docs/arte/prompt-nano-banana-salvador.md`. A música é a do mercado 03 da Quitanda (ijexá), em `versao-a-rota-das-feiras/musica/03.ogg`.

### 3.16 Quarto mercado: Mercado de São José, Recife (26/11/2026)

Segundo mercado do Nordeste. Abre ao vencer o chefe de Salvador. As fases ficam no fim da lista `PHASES` (posições 25 a 31), então os saves antigos seguem valendo. `OPEN_M` passou para 4.

**Ideia central: em Pernambuco, tudo dança.** O Norte era água (maré, rios), a Bahia era calor (o sol que anda). Recife é movimento: o tabuleiro gira com a ciranda e com o Galo da Madrugada, e o jogador aprende a usar o giro a favor (trazer vizinhos para perto) ou a se proteger dele.

**Linhas novas (5 níveis, arte 3D própria).** A tabela da seção 3.2 previa Macaxeira, mas Manaus já tem a linha Mandioca; a terceira linha virou **Cana**, que conta a história dos engenhos da Zona da Mata e chega ao bolo de rolo.

| Nível | Carne de sol (`cs`) | Queijo coalho (`qc`) | Cana (`cn`) |
|---|---|---|---|
| 1 | Sal grosso | Leite | Caldo de cana |
| 2 | Carne de sol | Manteiga de garrafa | Rapadura |
| 3 | Espetinho de carne de sol | Queijo coalho | Mel de engenho |
| 4 | Feijão-verde | Requeijão | Goiabada |
| 5 | Baião de dois | Cartola | Bolo de rolo |

**Regras novas:**

- **💃 Roda de ciranda** (`ciranda` na fase): um bloco de 3 × 3 casas marcado com a arte da roda. A cada 3 turnos (`CIRANDA_EVERY`), as 8 casas em volta do centro **giram 1 casa** no sentido da seta, levando itens e caixotes juntos; o centro fica parado. Cada roda tem sentido próprio (`dir` 1 = horário, −1 = anti-horário, arte espelhada). O contador "💃 Roda gira em N" fica no topo, e as casas pulsam no turno anterior ao giro. Item no sol continua esquentando enquanto gira (o calor vai junto).
- **🧵 Encomenda da Maria Flor** (`flor`): a rendeira pede **3 itens, um de cada vez**, em níveis crescentes (de `lv[0]` a `lv[1]`) e de linhas alternadas. Só o item atual aparece; os próximos ficam como ❔. Cada item entregue dá **+1 turno** (`FLOR_BONUS`) e a encomenda completa paga moedas em dobro e conta também como pedido comum. Não há prazo. Só há uma por vez; a próxima chega `every` turnos depois da anterior (contador "🧵 Maria Flor em N"). Ela ocupa o lugar do pedido comum com menos itens entregues (nunca o da Dona Dadá) e, no Recife, não aparece como freguesa comum. Diferença para a Dona Dadá: a Dadá cobra rapidez (prazo); a Maria Flor cobra planejamento (não se sabe o próximo item).
- **🐓 Chefe Galo da Madrugada** (`boss:'galo'`): a cada 5 turnos (`GALO_EVERY`) o bloco dá a volta no tabuleiro: **todas as 22 casas da borda giram 1 casa** no sentido horário, com itens e caixotes. A arte do Galo desfila por cima do tabuleiro. A roda de ciranda do meio continua girando a cada 3 turnos.
- **🥩 Selo Carne de Sol** (Despensa): 3 itens de nível 5 de cada linha do Recife + chefe vencido. Na fase, aparecem **2 vagas de Despensa** ao lado da barra de informações. Arrastar um item até a vaga (ou tocar no item e depois na vaga) guarda o item fora do tabuleiro, livre do sol, das rodas, do Galo e do mofo. Tocar na vaga seleciona o item: depois, uma casa vazia o devolve ao tabuleiro e um pedido recebe a entrega direto. Guardar e tirar não gastam turno. O tabuleiro não é considerado travado enquanto der para guardar um item ou entregar o que está na Despensa. A mochila leva os quatro selos.
- O **sol forte** do Nordeste volta em duas fases (parado na 3, andando na 6), para manter a identidade da região.

**Fases:**

| Fase | Objetivo | Turnos | Linhas | Obstáculos e regras |
|---|---|---|---|---|
| 1 · Bom dia, Recife | entregar 5 pedidos | 16 | Carne de sol, Queijo coalho | 2 caixotes |
| 2 · Roda de ciranda | criar Requeijão (nível 4) | 17 | Carne de sol, Queijo coalho | 2 caixotes, 1 roda (tutorial) |
| 3 · Chegou a cana | entregar 6 pedidos | 18 | as três | 3 caixotes, 1 roda, sol parado |
| 4 · Encomenda da Maria Flor | 2 encomendas da Maria Flor + 4 pedidos | 19 | as três | 2 caixotes, encomenda a cada 4 turnos, níveis 1 a 3 (tutorial) |
| 5 · Duas rodas | criar Bolo de rolo (nível 5) | 23 | as três | 2 caixotes, 2 rodas em sentidos contrários |
| 6 · Frevo no mercado | entregar 7 pedidos + limpar 4 | 25 | as três | 5 caixotes, 1 roda, sol que anda, encomenda a cada 6 (níveis 2 a 4); tutorial do Selo |
| Chefe · Galo da Madrugada | 7 pedidos + 1 encomenda da Maria Flor | 25 | as três | 2 caixotes, 1 roda, Galo a cada 5, encomenda a cada 5 (níveis 2 a 3) |

**Balanceamento.** Um robô simples (entrega, tira itens grandes do sol, junta o que os pedidos e a meta pedem, colhe a linha que falta; sem ferramentas, selos nem Despensa; ignora as rodas) jogou cada fase 400 vezes. Esse robô é um pouco mais fraco que o da seção 3.15, por isso os números de Salvador mudaram; o que vale é a comparação na mesma coluna de robô:

| Fase | Ver-o-Peso | Manaus | Salvador | Recife |
|---|---|---|---|---|
| 1 | 100% | 100% | 100% | 100% |
| 2 | 9% | 11% | 11% | 15% |
| 3 | 97% | 99% | 99% | 98% |
| 4 | 32% | 31% | 40% | 74% |
| 5 | 3% | 2% | 3% | 3% |
| 6 | 75% | 56% | 62% | 52% |
| Chefe | 70% | 68% | 53% | 43% |

O robô vai mal nas metas de criar item (fases 2 e 5), como nos outros mercados. A fase 4 ficou mais fácil de propósito, por ser o tutorial da Maria Flor. O chefe ficou um pouco mais difícil que o de Salvador, seguindo a subida de dificuldade entre mercados. Na primeira versão a encomenda do chefe ia até o nível 4 e o robô vencia só 11%: o 3º item (nível 4, desconhecido até o fim) travava a fase; com níveis 2 a 3 e 25 turnos, 43%. Vigiar com jogadores: se a roda parece ajudar ou atrapalhar, e se a encomenda "um de cada vez" fica clara sem ler o tutorial.

**Diário:** 7 cartões novos (Mercado de São José, Ciranda, Cana-de-açúcar, Renda renascença, Bolo de rolo, Frevo, Galo da Madrugada) e as curiosidades dos 15 ingredientes no Álbum, a validar com pesquisa e revisão local.

**Arte e música:** itens 3D próprios (grade do Nano Banana) e, na mesma leva, a arte própria dos 15 itens de Manaus, que até então eram cópias da Quitanda. A casa da roda de ciranda (pixel art em quadros, como o sol), o ícone da Despensa e o Galo da Madrugada (ilustração pintada, como o saveiro). Prompts em `docs/arte/prompt-nano-banana-recife.md`. A música é a do mercado 04 da Quitanda (ciranda), em `versao-a-rota-das-feiras/musica/04.ogg`.

## 4. Versão B — Quitanda Zen (passatempo, foco em anúncios)

### 4.1 Loop

Sem derrota e sem limite de turnos. O jogador gera, funde e entrega no próprio ritmo. O que limita o ritmo são as **cargas dos cestos**, que recarregam com o tempo ou por anúncio.

### 4.2 Tabuleiro e cestos

- Tabuleiro inicial 6×7, com 3 expansões compradas com moedas até 7×9 (6×8 por 500, 7×8 por 2.000, 7×9 por 8.000 moedas; valores a calibrar).
- Itens com níveis 1 a 6. Botão **Organizar** (grátis) agrupa itens iguais.
- **Cesto:** capacidade de 8 cargas; recarga de 1 carga a cada 90 s (inclusive offline, até o máximo). Cada toque gasta 1 carga e gera 1 item.
- **Anúncio recompensado:** +4 cargas (até 6 por dia).

### 4.3 Pedidos e XP

- Fila fixa de 3 clientes, sem prazo. Pedidos simples: 1 a 2 itens de nível 2 a 4.
- **Encomenda diária** (1 por dia): 6 a 10 itens nível 5, com recompensa grande.
- XP por item entregue: nível 2 = 4; nível 3 = 8; nível 4 = 15; nível 5 = 30; nível 6 = 60.

### 4.4 Progressão lenta

Nível da Quitanda de 1 a 50. XP para ir do nível n ao n+1 = **100 + 60 × n**.

| Meta | XP acumulado | Tempo estimado* |
|---|---|---|
| Nível 10 | ~3.600 | ~2,4 h |
| Nível 25 | ~20.400 | ~14 h |
| Nível 50 | ~78.400 | ~52 h |

*Considerando média de 25 XP por minuto ativo. Estimativa para calibrar com dados reais.

| Nível | Desbloqueio |
|---|---|
| 1 | Linha Frutas |
| 3 | Linha Verduras |
| 5 | Linha Padaria |
| 8 | Linha Laticínios |
| 10 | 1ª expansão do tabuleiro; Caderno de Receitas |
| 12 | Linha Doces |
| 15 | Linha Temperos; decoração da calçada |
| 20 | Linha Bebidas; 2ª expansão |
| 25 | Linha Peixes; eventos semanais |
| 30 | Linha Carnes; 3ª expansão |
| 35 | Receitas especiais regionais (ponte com o tema Brasil) |
| 40 | Feira noturna (tema visual + eventos) |
| 50 | Quitanda Lendária; opção de “Nova Feira” (recomeçar em outra cidade com bônus) |

### 4.5 Metas de longo prazo

- **Caderno de Receitas:** 60 receitas a descobrir entregando combinações de itens de linhas diferentes.
- **Decoração:** moedas compram mesas, toldos, plantas e mascote; bônus pequeno de XP (+1% por peça, máximo +20%).
- **Missões:** 3 diárias e 3 semanais; sequência de login de 7 dias.
- **Eventos de 7 dias** (Festa Junina, Natal) com linha de itens temporária.

### 4.6 Anúncios

| Local | Tipo | Regra |
|---|---|---|
| Recarga de cesto | Recompensado | +4 cargas, máx. 6 por dia |
| Dobrar recompensa de pedido | Recompensado | máx. 10 por dia |
| Baú diário | Recompensado | 3 por dia |
| Acelerar expansão/decoração | Recompensado | reduz a espera pela metade |
| Entre momentos do jogo | Intersticial | no máx. 1 a cada 5 min; só após subir de nível ou a cada 5 entregas; nunca durante o arraste; nenhum nos primeiros 15 min do 1º dia |
| Banner | Não usar | polui a tela e prejudica a leitura do tabuleiro |

- **Remover anúncios:** compra única de R$ 14,90 remove os intersticiais; os recompensados continuam opcionais, com +25% de bônus.
- **Compras complementares:** pacotes de moedas de R$ 4,90 a R$ 29,90, sem pressão.
- **Conformidade:** consentimento conforme a LGPD, plataforma de mediação de anúncios (avaliar AdMob, AppLovin MAX, Unity LevelPlay) e definição clara do público-alvo; evite direcionar a menores sem a política adequada das lojas.
- **Receita:** depende de volume, país e qualidade do tráfego. Não estimo valores sem dados.

### 4.7 Retenção

No máximo 1 notificação por dia (cestos cheios). Recarga offline. Modo Zen com música e sons ambiente (liga/desliga).

### 4.8 Revisão v0.4 do protótipo (jogo sem fim, ritmo mais lento e mais anúncios)

Onde houver conflito com as seções 4.2 a 4.6, vale esta seção. Os valores são pontos de partida, ainda sem teste com jogadores.

- **Tela inicial:** banca decorada, dica do Seu Zé, botão Jogar, presente diário (sequência de até 7 dias), atalhos e escolha de idioma.
- **Mapa (Rota das Feiras):** mapa do Brasil com os estados e as 5 regiões em cores diferentes; cada mercado aparece com um ícone. Concluir uma feira exige atender 30 + 3 × parada clientes (teto de 60). Depois da 12ª parada começa uma nova volta, com +10% de XP e moedas por volta, sem limite.
- **Viagem animada:** ao viajar, um ônibus (até 900 km) ou um avião (acima disso) percorre o mapa até o próximo mercado, com a distância em km. Dá para pular.
- **Ao chegar:** as linhas que não existem na feira nova são vendidas, o tabuleiro é completado até ficar cheio e **os cestos começam vazios**.
- **Cestos:** 10 cargas, 1 carga a cada 90 s (também com o jogo fechado). Subir de nível e entregar pedidos não recarregam mais os cestos. ⚡ Recarga é rara: a cada 10 níveis e nas encomendas.
- **Fusão tripla:** só por escolha do jogador (seção 2).
- **Pedidos:** 4 clientes; o nível pedido cresce com o nível do jogador; 22% são relâmpago (⏱️ 75 s, pagam em dobro, sem punição).
- **Anúncios (simulados):** +6 cargas em todos os cestos (12 por dia, também oferecido ao tocar num cesto vazio); dobrar a recompensa do pedido (15 por dia); dobrar o prêmio da viagem (1 por viagem); baú diário (5 por dia); intersticial no máximo a cada 3 min, a partir de 5 min de jogo, a cada 4 pedidos, ao subir de nível e ao chegar num mercado.
- **Melhorias com imagem e efeito explícito:** cada compra mostra uma imagem, o que faz e o valor de agora e depois (ex.: "Agora: 10 cargas / Depois: 12 cargas").
- **Ajuda:** tela "Como jogar" com ícone e explicação de cada elemento; abre sozinha no primeiro jogo e fica no botão ❓.
- **Riscos a observar no teste:** com cestos lentos e vazios a cada mercado, o jogo depende mais de anúncios; vigiar fadiga de anúncios, desistência no primeiro mercado (30 clientes) e avaliações nas lojas. A regra antiga de "nenhum intersticial nos primeiros 15 min" foi reduzida para 5 min a pedido; vale testar as duas.

### 4.9 Loja do protótipo (compras simuladas)

A pedido, a Versão B passou a ter compras com dinheiro real além dos anúncios, o que muda a premissa da seção 4.6 (receita só por anúncios, com compras complementares). No protótipo as compras são simuladas; preços de US$ 0,50 a US$ 9,99.

**Valor de referência (item avulso):** 300 moedas = US$ 0,50 · ⚡ Recarga = US$ 0,33 · 🧲 Junta-tudo = US$ 0,33 · 1 nível de melhoria = US$ 0,99 · remover anúncios = US$ 2,99.

| Produto | Conteúdo | Preço | Economia |
|---|---|---|---|
| Kit Boas-vindas (1 vez) | 500 moedas, 3 ⚡, 3 🧲 | US$ 0,99 | 65% |
| Kit Viajante | 2.000 moedas, 5 ⚡, 5 🧲 | US$ 3,99 | 40% |
| Kit Feirante | 5.000 moedas, 10 ⚡, 10 🧲, +1 nível em cada melhoria de cesto | US$ 6,99 | 61% |
| Kit Quitanda Lendária | 8.000 moedas, 15 ⚡, 15 🧲, sem anúncios de tela cheia | US$ 9,99 | 62% |
| Moedas | 300 / 1.000 / 2.500 / 6.000 / 12.000 | US$ 0,50 / 1,49 / 2,99 / 5,99 / 9,99 | bônus de 0 / 12 / 39 / 67 / 100% |
| ⚡ Recarga ou 🧲 Junta-tudo | 3 / 10 | US$ 0,99 / 2,49 | — / 25% |
| Remover anúncios | intersticiais | US$ 2,99 | — |
| Melhoria de cesto | +1 nível | US$ 0,99 | — |
| Ampliação do tabuleiro | próxima ampliação | US$ 1,99 | — |
| Decoração | 1 peça, conforme a faixa | US$ 0,50 / 0,99 / 1,99 | — |
| Todas as decorações | as peças que faltam | US$ 7,99 | 43% com as 12 |

- A loja abre pelo saldo de moedas no topo do jogo, pela tela inicial, por Melhorias e pelo aviso de cesto vazio.
- **Pedidos em destaque:** cartões maiores, com o rosto do cliente, e o nível de cada item pedido na cor da banca. A encomenda foi para a faixa do mercado.
- **A observar:** melhorias e decorações pagas encurtam a progressão; vigiar se quem compra perde o motivo para continuar. Verificar as regras das lojas e a legislação (seção 3.7) antes de publicar.

### 4.10 Revisão v0.5 (a partir da avaliação de usuário novo)

Mudanças feitas com base em `docs/avaliacoes/avaliacao-quitanda-zen.docx`. Onde houver conflito com as seções anteriores, vale esta.

- **Primeiro mercado mais leve:** os cestos começam cheios no primeiro mercado (vazios nos seguintes) e a recarga é de 20 s por carga, subindo 15 s por parada até os 90 s. Na simulação, a espera pelos cestos no primeiro mercado caiu para cerca de 10 minutos (mediana).
- **Tutorial no tabuleiro:** no lugar da tela de ajuda aberta no primeiro jogo, o Seu Zé guia três passos (juntar, entregar, colher), destacando onde tocar. A tela completa continua no ❓.
- **Vinheta:** inteira só na primeira abertura do dia; nas demais, 1,5 s. A tela avisa que um toque pula.
- **Tela inicial:** os seis atalhos cabem numa linha no celular pequeno.
- **Anúncios e loja só a partir do segundo mercado:** sem anúncio de tela cheia, sem "Dobrar" e sem convites para a loja no primeiro mercado; fica só o anúncio opcional de cargas.
- **Loja:** vende só o que economiza tempo (kits, moedas, Recarga, Junta-tudo e remover anúncios). Melhorias, ampliações e decorações voltam a ser só por moedas do jogo. O Kit Feirante passou a ter 5.000 moedas, 12 ⚡ e 12 🧲 por US$ 6,99.
- **Viagem:** itens de nível 5 ou mais valem o dobro ao serem vendidos na viagem.
- **Pedidos:** só o primeiro nome do cliente no cartão; ao tocar num pedido, a barra mostra o nome de cada item pedido.
- **Encomenda:** é explicada na primeira vez que o jogador cria um item que serve, e o botão pisca até o primeiro uso.
- **Música:** melodia calma gerada pelo próprio jogo, com botão em Ajustes.
- **Ferramentas de teste escondidas:** Modo teste, painel e "Remover anúncios (simulado)" aparecem após 5 toques no número da versão, em Ajustes.
- **Não feito:** a arte no lugar dos emojis, que depende das imagens.

### 4.11 Revisão de novembro de 2026 (avisos, novidades do dia e anúncios mais espaçados)

Pedido da dona do projeto: deixar o jogo mais "livre", avisar quando os cestos encherem e mostrar melhor o que se ganha e o que se tem. Onde houver conflito com as seções anteriores, vale esta.

- **Anúncios de tela cheia mais espaçados** (constantes `INTER_*` no bloco DADOS): primeiro só depois de 10 min de jogo desde a instalação (eram 5); pelo menos 6 min entre um e outro (eram 3); a cada 6 pedidos (eram 4); nunca nos 2 primeiros minutos depois de abrir o app (ou de voltar após mais de 5 min fora); nunca nos 4 min seguintes a um anúncio com prêmio que a pessoa escolheu ver; e não aparece mais ao subir de nível, que fica só como comemoração. Continua aparecendo ao chegar a um mercado, se as regras acima deixarem. Os anúncios com prêmio (cargas, baú, dobrar) não mudaram.
- **Novidades de hoje:** na primeira abertura de cada dia, depois da vinheta, um aviso mostra linha por linha, com animação: o presente do dia (moedas contando, e quanto vale amanhã), os anúncios de cargas renovados, o baú diário renovado, o "Dobrar" renovado (a partir do segundo mercado) e, se for o caso, que os cestos encheram. O botão já pega o presente. Também aparece se o dia virar com o jogo aberto. Não aparece no primeiro dia do jogador (o tutorial já basta).
- **Aviso de cestos cheios (só no app Android):** ao sair do jogo, o app agenda um aviso no celular para a hora em que todos os cestos do mercado atual estarão cheios; ao voltar, cancela. Usa `@capacitor/local-notifications`. A licença é pedida uma vez, num momento que faz sentido (primeiro cesto vazio, chegada a um mercado ou ao fechar as novidades do dia), e há a opção "Avisos" em Ajustes.
- **Pedidos de receita:** o cartão mostra o nome do cliente, como os demais; a receita é indicada por um selinho 📖 no canto (antes, a palavra "Receita" ocupava o lugar do nome).
- **Receitas no fim da feira:** o aviso de feira concluída lista as receitas descobertas naquele mercado (ingredientes e descrição curta) e quantas o Caderno já tem. A lista recomeça a cada viagem (`S.recFeira`).
- **Melhorias:** o saldo de moedas fica fixo no topo da tela (e pulsa depois de cada compra), e cada melhoria mostra bolinhas cheias até o nível atual e vazias até o máximo, com o número (ex.: 3/10). O mesmo vale para a ampliação do tabuleiro (0/3) e para as decorações (0/12).

### 4.12 Banca da tela inicial (novembro de 2026)

- A banca da tela inicial é uma cena de feira vista de cima, com o tampo inclinado para quem olha (`bancaHtml()`). Ela ocupa só a altura que sobra (mínimo de 170 px) e a cena encolhe sem distorcer, para que a tela inicial inteira caiba sem rolar: logo, banca, Seu Zé (até 2 linhas), Jogar, presente, mercado, botões de navegação e idioma.
- **Começa vazia e enche com o Álbum:** cada linha com pelo menos um item descoberto (`S.seen`) ganha um lugar no tampo, da frente para o fundo (arranjo dinâmico desde 26/11/2026, seção 4.13). As fileiras do fundo são menores, pela perspectiva. Não há caixotes: os itens ficam deitados lado a lado, sem brilho (o aviso de novidade fica no botão do Álbum).
- **Decorações no lugar e no tamanho de verdade** (`DECOR_POS`, 1 m ≈ 22% da largura), sem sombra: os objetos de chão ficam no piso, à frente do balcão e sem encostar nele, nesta ordem: vasos, banco (com o rádio no assento), caminha do Mingau, lousa, carrinho e bicicleta. A balança fica em cima do tampo, no canto da frente à esquerda, e o relógio fica pregado no poste da direita. O toldo e o chão cobrem a largura toda; as luzinhas e as bandeirinhas ficam penduradas por baixo do toldo. Sem toldo, aparece só a viga de madeira. O toldo é desenhado em código (não é imagem): 14 listras e uma franja arredondada embaixo de cada listra, na mesma cor dela. Desde 26/11/2026 listras e franjas usam o mesmo ladrilho (1/7 da largura), o que as mantém alinhadas em qualquer tela; antes as franjas ficavam meia listra deslocadas e quase todas vermelhas (o mesmo nos dois jogos). Os emojis em volta do logo ficam parados.

### 4.13 Banca dinâmica (26/11/2026; vale para a Quitanda e a Rota)

- **Problema:** o lugar de cada fileira era fixo (Quitanda: 2 por fileira, até 7 fileiras; Rota: 2 por fileira, 4 fileiras). Com o 3º mercado da Rota (9 linhas, 5 fileiras), a fileira do coco ficou atrás do toldo, e qualquer linha nova nos dois jogos teria o mesmo destino.
- **Regra nova (`arranjoBanca`, mesmo código nos dois `index.html`):** a cada vez que a tela inicial é desenhada, o jogo testa de 2 a 6 linhas lado a lado por fileira e 5 funduras de tampo (topo em 31%, 29%, 27%, 25% ou 23% da cena) e fica com a combinação que deixa os itens maiores, respeitando três limites: cada linha cabe na sua parte do tampo (os itens podem se sobrepor até 60%), uma fileira não cobre demais a de trás, e os itens do fundo não entram no toldo nem nas bandeirinhas.
- **Preferência pelo visual de sempre:** cada linha a mais por fileira custa 8% e cada ponto de fundura a mais custa 2%; só mudam quando o ganho de tamanho compensa. Poucas linhas ficam juntas na frente (distância máxima entre fileiras: 8% da altura na Quitanda, 12% na Rota), com itens maiores; conforme o Álbum enche, as fileiras se espalham, o tampo se aprofunda e, se preciso, entram mais linhas por fileira.
- **Detalhes:** a fileira usa a quantidade real de itens descobertos de cada linha (linhas curtas não apertam as outras). Na Quitanda, a folga da balança (2 fileiras da frente, à esquerda) só existe se a balança foi comprada e agora se divide entre as linhas da fileira; o relógio do poste sobe junto com o tampo. Não há mais limite de 14 linhas.
- **Resultado medido (tela de 360 px):** Quitanda com as 13 linhas, 2 por fileira e itens do mesmo tamanho de antes; Rota com as 9 linhas, 5 fileiras inteiras à vista. Simulado com até 48 linhas: tudo continua dentro da banca (3 a 5 por fileira, itens menores).

### 4.14 Botão voltar e detalhes no álbum (26/11/2026; vale para a Quitanda e a Rota)

- **Botão voltar do Android.** Regra: só sai do app na tela inicial, com dois toques em até 2 s (o primeiro mostra “Toque em voltar de novo para sair”). Em qualquer outra tela, volta um passo:
  - fecha a camada da frente: vinheta, viagem entre mercados (Quitanda), aviso ou pop-up (pelo botão de fechar, continuar ou cancelar; anúncio simulado só depois da contagem);
  - painel aberto por cima de outro (por exemplo, Melhorias → Loja, Diário → Loja) volta ao painel anterior (`sheetPilha`, função `empilha`), e só depois fecha;
  - Quitanda: tabuleiro → tela inicial;
  - Rota: dentro da fase, o voltar abre a **Pausa** (Continuar, Recomeçar, Sair para o mercado) em vez de abandonar a fase, para não contar derrota por engano; com a pausa aberta, voltar continua a fase. Mercado → mapa → tela inicial. Com ferramenta armada, o voltar só a desarma.
  - A Rota ganhou o plugin `@capacitor/app` no `app-android-rota/package.json` (antes, o voltar fechava o app em qualquer tela).
- **Pop-up de detalhes.** Tocar em qualquer quadradinho do álbum abre uma ficha:
  - **Ingrediente** (Quitanda: Caderno de Receitas → Ingredientes; Rota: Álbum → Ingredientes): arte grande, linha e nível, uma curiosidade (`INFO`, pt e en), a fila de níveis da linha com o atual em destaque (os não vistos aparecem como ❔), o que sai ao juntar dois, onde encontrar (cidades/mercado) e, na Quitanda, as receitas que usam o item (as não descobertas aparecem só como contagem) e os personagens que gostam da linha; na Rota, quantas moedas o item rende num pedido. Itens ainda não descobertos também abrem, com a dica de como chegar a eles, sem revelar o nome.
  - **Receita** (Quitanda: aba Receitas): os dois ingredientes, a descrição, uma curiosidade (`REC_INFO`) e os mercados onde ela é pedida. Receita não descoberta mostra só as linhas e a dica.
  - **Personagem** (Quitanda: Turma da Feira; Rota: aba nova **Clientes** do Álbum): retrato, ocupação, mercado de origem, uma ficha que explica a profissão e uma curiosidade (`BIO`, mesmo texto nos dois jogos), a frase e, na Quitanda, a linha preferida e o nível de amizade.
- **Rota: aba Clientes.** Cada personagem entra no Álbum quando faz o primeiro pedido no tabuleiro (`S.met`; 1 = novo, 2 = visto). Novidades acendem o ponto no botão Álbum e na aba. Saves antigos começam vazios e enchem jogando.
- **Textos:** 104 curiosidades de ingredientes e 25 de receitas na Quitanda, 45 de ingredientes na Rota e 28 fichas de personagens. Escritos a partir de conhecimento geral; precisam da mesma revisão local e de inglês pedida para os textos culturais (pendência 4 do `CONTEXTO.md`).

## 5. Localização e idiomas

**Ordem de lançamento.** Português (BR) + inglês no início; espanhol em seguida (público latino-americano); outros idiomas (alemão, francês etc.) só depois que os dados mostrarem de onde vêm jogadores e receita. O inglês é quase obrigatório porque o dinheiro do gênero está concentrado em mercados ocidentais, em especial os EUA.

**Nome internacional (Versão B):** *Quitanda: Merge Across Brazil*. “Quitanda” é fácil de pronunciar (kee-TAHN-da), desconhecido fora do Brasil (gera curiosidade) e mantém a marca da versão em português; o subtítulo explica o gênero e o tema. A tela inicial em inglês traz a pronúncia e o significado. Antes de adotar, verificar registro de marca e nomes parecidos nas lojas; uma busca rápida em 10/11/2026 não encontrou jogo com esse nome.

**O que traduzir (protótipo da Versão B):** a interface, os papéis e falas dos personagens e as descrições. Ficam em português os nomes dos mercados, das cidades, dos personagens e dos pratos típicos (pastel, tapioca, feijoada, moqueca, brigadeiro…), que ganham uma explicação curta em inglês. As falas mantêm expressões regionais (égua, oxente, uai, bah, tchê).

**Teste barato antes de traduzir o jogo.** Traduza apenas a página da loja (título, descrição, capturas de tela) e observe onde surgem os downloads.

**Regras técnicas desde o primeiro dia:**

- Todos os textos em arquivos separados por idioma, nunca dentro do código nem embutidos em imagens.
- Interface flexível: inglês e alemão ocupam mais espaço que o português, e idiomas asiáticos exigem outras fontes.
- Revisão por falante nativo antes de publicar. O Claude acelera muito a tradução, mas humor, tom e nomes pedem olhar humano.
- Nomes de pratos e produtos (tapioca, açaí, pirarucu, tacacá) não são traduzidos; a explicação fica no cartão do Diário.
- Documentos legais (política de privacidade, termos de compra) nos idiomas dos países de publicação, conforme exigências das lojas e da legislação local (LGPD no Brasil, GDPR na Europa).

## 6. Diário de Viagem (cartões colecionáveis da Versão A)

Objetivo: dar ao jogador, brasileiro ou estrangeiro, um motivo para conhecer os lugares reais do mapa, sem interromper o jogo e sem texto obrigatório.

### 6.1 Como funciona

1. **Tela de vitória da fase:** aparece um botão discreto, “Novo cartão no Diário”. Sem pop-up e sem interrupção; se o jogador ignorar, o jogo segue normalmente.
2. **Cartão em duas camadas.** Frente (curta): ilustração, nome do lugar ou produto, localização no mapa e 2 a 3 frases. Botão **“Saiba mais”**: texto de cerca de 80 a 100 palavras com curiosidade e contexto cultural, que só abre se o jogador tocar.
3. **Diário na tela inicial:** reúne todos os cartões, organizados por região e mercado, consultáveis a qualquer momento. Cartões ainda não desbloqueados aparecem como silhueta com “?” e o nome do lugar.
4. **Recompensa de coleção (grátis e pequena):** completar todos os cartões de um mercado dá moedas ou um item cosmético.
5. **Regra de ouro:** cartões não são vendidos. O valor deles é a curiosidade; vender estragaria isso.

### 6.2 Exemplo de cartão (a validar antes de usar)

> **Açaí · Ver-o-Peso, Belém (PA)**
> Fruto de uma palmeira amazônica, o açaí é base da alimentação em boa parte do Norte. *Saiba mais:* no Pará, ele costuma ser servido como acompanhamento salgado, junto de peixe e farinha, e não apenas como sobremesa gelada, como ficou conhecido fora da região.

### 6.3 Escopo

| Fase do projeto | Cartões |
|---|---|
| MVP | 7 (um por fase do Ver-o-Peso) |
| Expansão inicial | 24 (um por mercado + um por chefe) |
| Versão completa | até 84 (um por fase) |

Cada cartão exige pesquisa, revisão e tradução, então o escopo cresce junto com o conteúdo.

### 6.4 Cuidados

- **Precisão:** checar cada texto em fontes confiáveis e, idealmente, com revisão de alguém da região. O Claude ajuda a redigir e organizar, mas não deve ser a única fonte de fatos culturais.
- **Imagens:** usar ilustrações próprias, não fotos, para evitar problemas de direitos autorais.
- **Respeito cultural:** evitar estereótipos e tratar com cuidado tradições, povos e comunidades de cada local.
- **Texto curto:** cartões longos são pulados; manter o “Saiba mais” enxuto.
- **Idiomas:** textos em arquivos por idioma, com nomes originais dos produtos preservados.

### 6.5 Versão B (Quitanda Zen)

O equivalente é o **Caderno de Receitas** (seção 4.5): cada receita descoberta ganha uma nota curta com origem e curiosidade, também com botão “Saiba mais” opcional. Sem cartões por fase, já que a Versão B não tem fases.

## 7. Tecnologia e primeiros marcos

**Motor.** Minha avaliação (confirme antes de decidir): Unity tem integrações maduras de anúncios e compras; Godot 4 é mais leve e gratuito, mas os plugins de anúncios e compras variam em maturidade; Flutter com Flame também é possível. Como a Versão B depende de anúncios e a A de compras, vale testar a integração desses SDKs cedo.

**Marcos.**

1. **Núcleo:** tabuleiro, arrastar e fundir, fusão tripla, cesto, pedidos, salvamento.
2. **Versão A mínima:** fases com turnos, 1 mercado (Ver-o-Peso) com 6 fases e chefe, Mofo, 2 boosters, Diário com 7 cartões, sem monetização.
3. **Teste** com 10 a 20 pessoas do público-alvo.
4. **Versão B mínima:** Quitanda com XP, 3 linhas de itens, cargas dos cestos e anúncios simulados.
5. **Integração** dos SDKs reais de anúncios e compras, e tradução para inglês.

**Prompt inicial sugerido (núcleo):**

> Crie o núcleo de um jogo mobile 2D de merge em [Unity ou Godot]. Tabuleiro 6×7; itens com linha e nível de 1 a 5; arrastar um item sobre outro igual funde em nível +1 na célula de destino; se houver um terceiro item idêntico adjacente ao destino, ele é absorvido e o resultado sobe +2; o cesto gera um item nível 1 em célula vazia aleatória; pedidos de clientes são entregues arrastando o item até eles; salvamento local em JSON. Toda a configuração deve ficar em arquivos de dados. Inclua testes unitários da lógica de fusão e uma cena de debug. Use arte placeholder.
