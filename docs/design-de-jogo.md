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
| Nordeste | Mercado de São José (Recife) | Carne de sol, Macaxeira, Queijo coalho | Carne de Sol: Despensa com 2 vagas para guardar itens fora do tabuleiro |
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
| Todas | Caixote | Célula bloqueada; abre quando ocorre uma fusão em célula adjacente. |
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

### 4.8 Revisão v0.3 do protótipo (ritmo rápido e jogo sem fim)

A pedido, o protótipo trocou a progressão lenta das seções 4.2 a 4.5 por um ritmo rápido. Onde houver conflito, vale esta seção. Os valores são pontos de partida, ainda sem teste com jogadores.

- **Tela inicial:** banca decorada, dica do Seu Zé, botão Jogar, presente diário (sequência de até 7 dias) e atalhos para Mapa, Turma, Missões e Ajustes.
- **Mapa (Rota das Feiras):** os 12 mercados da seção 3.2 viram paradas. Concluir uma feira exige atender 6 + 2 × parada clientes (teto de 24). Ao viajar, as linhas que não existem na feira seguinte são vendidas, o tabuleiro é completado até ficar cheio e os cestos enchem. Depois da 12ª parada começa uma nova volta, com +10% de XP e moedas por volta, sem limite.
- **Linhas por feira:** 13 linhas de 8 níveis; cada feira usa 4 (a 1ª usa 2 e a 2ª usa 3, como tutorial).
- **Tabuleiro inicial cheio:** as 42 células começam ocupadas com itens de nível 1 a 4.
- **Cestos:** 20 cargas, 1 carga a cada 10 s; cada pedido atendido devolve 1 carga; subir de nível enche os cestos. Anúncio recompensado: +10 cargas.
- **XP:** fusões dão XP (metade do nível, mais bônus de combo e de fusão tripla). XP para ir do nível n ao n+1 = 50 + 15 × n, sem nível máximo.
- **Pedidos:** 4 clientes; o nível pedido cresce com o nível do jogador; 22% são relâmpago (75 s, pagam em dobro, sem punição); um pedido pode ser trocado a cada 20 s.
- **Turma da Feira:** 28 personagens com papel, fala e linha favorita. Cada pedido rende amizade; cada nível de amizade paga moedas, e a cada dois níveis um Junta-tudo.
- **Auxílios:** 🧲 Junta-tudo (funde todos os pares) e ⚡ Recarga (enche os cestos), ganhos jogando.
- **Metas sem fim:** missões que se renovam ao receber, encomendas numeradas com exigência crescente, melhorias de cestos e 12 decorações.
- **Riscos a observar no teste:** o ritmo rápido reduz a necessidade de anúncio de recarga; a troca de linhas a cada feira pode frustrar quem acumulou itens altos.

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
