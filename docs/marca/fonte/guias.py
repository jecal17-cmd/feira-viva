"""Gera os guias de identidade visual (HTML -> PDF e Markdown) de cada app da Bentevi Apps.
Uso: python3 guias.py  (gera guias/<id>.html e guias/<id>.md; o PDF sai com node pdf.js)"""
import json, os, html
os.makedirs('guias', exist_ok=True)

MESTRE = {
  'cores': [('Creme', '#FFF6D9', 'Fundo da marca, vinheta e peças'), ('Verde Bentevi', '#1D4A3F', 'Texto e logotipo'),
            ('Ouro “te”', '#E0A800', 'Sílaba “te” do logotipo'), ('Amarelo bem-te-vi', '#F7C51E', 'Sublinhado, fundo do perfil'),
            ('Verde-musgo', '#557A6E', '“APPS” e textos de apoio')],
}

APPS = {
'bentevi-apps': dict(
  nome='Bentevi Apps', sub='Marca-mãe: o estúdio', cor='#1D4A3F', fundo='#FFF6D9', destino='feira-viva/docs/marca',
  essencia='Estúdio independente brasileiro de jogos e apps calmos, bonitos e com cara de Brasil, que resolvem coisas de verdade.',
  promessa='Jogos e apps com cara de Brasil.',
  logo='<div class="wm">Ben<span class="y">te</span>vi<i></i></div><div class="wsub">apps</div>',
  logo_txt='“Bentevi” em Baloo 2 ExtraBold (800), verde #1D4A3F, com a sílaba “te” em ouro #E0A800 e um sublinhado arredondado amarelo #F7C51E. Embaixo, “APPS” em Baloo 2 800, caixa alta, espaçamento largo, verde-musgo #557A6E. O bem-te-vi 3D (da vinheta) fica acima do nome ou à esquerda.',
  simbolo='O bem-te-vi, o passarinho que canta o próprio nome. A vinheta de 5 s (voo, pouso no galho e o canto real “bem-te-vi”) abre todos os apps.',
  cores=MESTRE['cores'],
  fontes=[('Baloo 2', '800 no logotipo e títulos; 500 e 700 em textos', 'OFL, Google Fonts')],
  img=['bentevi-no-galho.png'],
  visual=['Fundo creme liso ou amarelo bem-te-vi; nada de gradientes pesados.', 'O pássaro sempre em 3D, com sombra suave, nunca recolorido ou espelhado de cabeça para baixo.',
          'Cartões brancos com cantos bem arredondados (raio 44 px em peças 1080) e sombra verde suave.',
          'Cada app mantém a própria cor; a Bentevi aparece como assinatura: o pássaro + “Bentevi Apps” no rodapé.'],
  voz=['Calorosa, simples e brasileira; frases curtas.', 'Fala com “você”; nada de jargão técnico.', 'Sem promessa exagerada: o que dizemos, o app faz.'],
  nao=['Trocar as cores do logotipo ou separar “te” do resto.', 'Usar “Bentevi Games” (o nome atual é Bentevi Apps).', 'Pôr o logotipo sobre foto movimentada sem cartão de fundo.', 'Usar o selo do Google Play antes de o app estar publicado.'],
  telas=[],
  arquitetura=[('Quitanda Zen', 'quitanda-512.png', 'Jogo calmo de juntar itens'), ('Ler Brincando', 'lerbrincando-512.png', 'Alfabetização 5 a 7 anos'), ('Teto', 'TETO', 'Dinheiro do dia a dia'), ('Rota das Feiras', 'rota-512.png', 'Puzzle com turnos')],
),
'quitanda-zen': dict(
  nome='Quitanda Zen', sub='Nome internacional: Quitanda: Merge Across Brazil', cor='#2A8F63', fundo='#DCEFE4', destino='feira-viva/docs/marca',
  essencia='Passatempo relaxante de juntar itens: monte sua banca, atenda a turma da feira e viaje por 12 mercados reais do Brasil, sem pressa e sem derrota.',
  promessa='Junte · Entregue · Viaje pelo Brasil.',
  logo='<img src="../assets/quitanda-512.png" class="icg">',
  logo_txt='Ícone: banca de feira com toldo listrado vermelho e creme e uma caixa transbordando de frutas sobre fundo verde-folha. Nome em Baloo 2 800, verde-escuro.',
  simbolo='O toldo listrado vermelho e creme, recortado em ondas, é a assinatura gráfica: vai no topo das peças e telas.',
  cores=[('Creme', '#FFF6D9', 'Fundo das peças e da abertura'), ('Verde-escuro', '#1D4A3F', 'Textos e títulos'), ('Verde-folha', '#2A8F63', 'Cor de destaque do jogo, botões'),
         ('Menta', '#DCEFE4', 'Fundo das telas do jogo'), ('Vermelho do toldo', '#E4573D', 'Toldo, números, chamadas'), ('Amarelo sol', '#F2B33D', 'Moedas e destaques'), ('Ouro', '#B87A00', 'Moedas no tema claro')],
  fontes=[('Baloo 2', 'Títulos (700 e 800)', 'OFL'), ('Nunito', 'Textos (600 a 900)', 'OFL')],
  img=['fr-8.webp', 'pe-8.webp', 'be-5.webp', 'rosinha.webp', 'cicero.webp', 'dandara.webp'],
  visual=['Itens do jogo em 3D “flutuando” com sombra, como recortes de massinha brilhante.', 'Personagens da feira em 3D estilizado, simpáticos, de diversas idades e regiões.',
          'Mercados reais pintados (Ver-o-Peso, Mercadão, São Joaquim...).', 'Tema escuro: fundo #11231E e destaque #4CC38A.'],
  voz=['Calma e acolhedora: “sem pressa”, “sem derrota”.', 'Valoriza o Brasil real: nomes de mercados, cidades e pratos em português, mesmo na versão em inglês.', 'Convida em vez de pressionar.'],
  nao=['Linguagem de urgência (“corra!”, “última chance!”).', 'Toldo em outras cores que não vermelho e creme.', 'Itens chapados (2D) misturados aos 3D.'],
  telas=['2-inicio.png', '1-tabuleiro.png', '3-map.png'],
),
'rota-das-feiras': dict(
  nome='Rota das Feiras', sub='Versão A da Feira Viva', cor='#0F7A73', fundo='#E2F0EE', destino='feira-viva/docs/marca',
  essencia='Puzzle de fusão com turnos contados, fases com 1 a 3 estrelas e um chefe por mercado, numa viagem pelos 12 mercados do Brasil.',
  promessa='Cada toque conta.',
  logo='<img src="../assets/rota-512.png" class="icg">',
  logo_txt='Ícone: uma estrada sinuosa que sobe até uma cesta dourada de frutas, sobre fundo verde-azulado. Nome em Baloo 2 800, azul-petróleo escuro.',
  simbolo='A estrada (rota) e o toldo listrado verde-azulado e creme. A Rota é a irmã “desafio” da Quitanda: mesma família, cor própria.',
  cores=[('Verde-azulado', '#0F7A73', 'Destaque, botões, toldo'), ('Petróleo', '#0E3F44', 'Textos e títulos'), ('Névoa', '#E2F0EE', 'Fundo das telas'),
         ('Ouro', '#F0C04A', 'Estrelas e moedas'), ('Caixote', '#C99A63', 'Obstáculo caixote'), ('Lilás', '#A87BD6', 'Níveis e selos'), ('Creme', '#FFF6D9', 'Abertura (vinheta)')],
  fontes=[('Baloo 2', 'Títulos (700 e 800)', 'OFL'), ('Nunito', 'Textos', 'OFL')],
  img=['rota-pers.webp', 'ca-6.webp', 'la-5.webp', 'pa-6.webp'],
  visual=['Os mesmos itens 3D da Quitanda, com obstáculos (caixote, mofo) e ferramentas (martelo, caldeirão).', 'Mapa do Brasil colorido por região (Norte, Nordeste, Centro-Oeste, Sudeste, Sul).', 'Cartões do Diário de Viagem com fotos pintadas dos mercados.'],
  voz=['Desafiadora, mas gentil: explica a regra e celebra a estrela.', 'Curiosa: cada mercado traz uma história real (“Saiba mais”).'],
  nao=['Usar o verde-folha da Quitanda como cor principal (confunde os dois jogos).', 'Prometer “sem derrota”: aqui existe derrota.'],
  telas=['rota-1-inicio.png', 'rota-2.png', 'rota-4.png'],
),
'ler-brincando': dict(
  nome='Ler Brincando', sub='Alfabetização pelo som das letras, de 5 a 7 anos', cor='#3A6DF0', fundo='#E5F4FB', destino='lerbrincando/marca',
  essencia='A corujinha Lili ensina a criança a ligar o som às letras e a ler palavras de verdade, pelo método fônico, sem anúncios e sem castigo pelo erro.',
  promessa='Aprender a ler pelo som das letras.',
  logo='<img src="../assets/lerbrincando-512.png" class="icg">',
  logo_txt='Ícone: a corujinha Lili dourada em 3D, rodeada de letras coloridas, sobre azul-céu. Logotipo “Ler Brincando” em Baloo 2 800: “Ler” branco com contorno azul e “Brincando” em amarelo.',
  simbolo='A Lili, coruja que lê: aparece em 9 poses (acena, aponta, comemora, dorme, fala, feliz, ideia, lê, pensa).',
  cores=[('Azul Lili', '#3A6DF0', 'Botões e títulos'), ('Azul profundo', '#2147B8', 'Sombra dos botões'), ('Tinta', '#24304F', 'Textos'),
         ('Céu', '#7FD6F5', 'Fundo de cima das telas'), ('Areia', '#FFE8A3', 'Fundo de baixo (praia)'), ('Brilho', '#FFD54A', 'Estrelas e “Brincando”'), ('Acerto', '#17804A', 'Acertos (nunca “X” vermelho)'), ('Papel', '#FFFAF0', 'Fundo de leitura')],
  fontes=[('Baloo 2', 'Interface e títulos (500, 700, 800)', 'OFL'), ('Andika', 'Tudo o que a criança lê: letras e palavras com “a” e “g” de escola', 'OFL')],
  img=['acena.webp', 'comemora.webp', 'le.webp', 'ideia.webp', 'mundo1.webp'],
  visual=['Céu azul com nuvens e sol em cima; areia amarela embaixo.', 'Botões grandes (alvo mínimo 64 px) com sombra “de massinha” embaixo.', 'Cartões de vidro branco (86% de opacidade) com raio 22 px.', 'Modos de alto contraste e de menos estímulos.'],
  voz=['Fala com a família (pais e professores) com calma e base pedagógica.', 'Com a criança: carinhosa, elogia o esforço, nunca pune.', 'Concreta: 8 mundos, 93 fases, 363 palavras, 11 historinhas.'],
  nao=['Usar letra cursiva ou fonte sem “a” e “g” de escola para conteúdo de leitura.', 'Mostrar “X” vermelho, vidas ou derrota.', 'Linguagem de venda agressiva para crianças.'],
  telas=['celular-1-inicio.png', 'celular-3-mapa.png', 'celular-5-trem-das-silabas.png'],
),
'teto': dict(
  nome='Teto', sub='Antes chamado Folga · identificador app.folga', cor='#1B6E4F', fundo='#E9F2EC', destino='folga/docs',
  essencia='Responde a uma pergunta: quanto posso gastar hoje sem faltar dinheiro até a próxima entrada? Feito para quem tem renda que varia, parcelas e contas que vencem antes do dinheiro entrar.',
  promessa='Quanto posso gastar hoje?',
  logo='<div style="display:flex;align-items:center;gap:18px">TETOMARCA<span style="font:700 72px SG;color:#1B6E4F;letter-spacing:-2px">teto</span></div>',
  logo_txt='Símbolo: um telhado em V com beiradas retas, a função teto da matemática (⌈x⌉) desenhada como casa, com uma moeda âmbar embaixo: o dinheiro do dia, dentro do limite. Nome “teto” em minúsculas, Space Grotesk Bold, verde #1B6E4F.',
  simbolo='Telhado ⌈x⌉ + moeda. No ícone, telhado branco sobre quadrado verde de cantos arredondados; no widget, telhado verde sem fundo.',
  cores=[('Verde Teto', '#1B6E4F', 'Cor principal, telhado, botões'), ('Âmbar moeda', '#F2A900', 'Moeda do símbolo, destaques'), ('Borda da moeda', '#C98200', 'Anel interno da moeda'),
         ('Verde claro', '#CDEBDD', 'Seleção, fundo de destaque'), ('Verde noite', '#0B2E21', 'Texto sobre verde claro'), ('Positivo', '#1B8A4B', 'Valores com +'), ('Negativo', '#C62828', 'Valores com −'), ('Atenção', '#8A5A00', 'Estado “Atenção”')],
  fontes=[('Space Grotesk', 'Logotipo, títulos e números grandes (400 a 700)', 'OFL, embutida no app'), ('Roboto (fonte do sistema)', 'Texto corrido, mais legível em tamanho pequeno', 'Android')],
  img=[],
  visual=['Material 3 limpo: cartões verde-acinzentados claros, raio 12 dp, sem enfeite.', 'O número do teto em destaque, grande, sempre com o estado escrito (Tranquilo, Atenção, Aperto): nunca só a cor.', 'Valores sempre com sinal (+/−), positivo em verde e negativo em vermelho.', 'Tema escuro: verde #8ED6B5 e âmbar #F2BE5C.'],
  voz=['Direta e calma, como um amigo bom de conta.', 'Mostra de onde vem cada número (“De onde vem?”).', 'Sem culpa: quando estoura, diz quanto gastar por dia para compensar.'],
  nao=['Prometer enriquecimento ou “sair das dívidas rápido”.', 'Usar a cor como única informação.', 'Desenhar o telhado com pontas arredondadas ou sem as beiradas retas.', 'Trocar o âmbar da moeda por dourado metálico.'],
  telas=['teto-1-hoje.png', 'teto-2-explica.png', 'teto-3-ganha.png'],
),
}

TETOMARCA = lambda c='#1B6E4F', s=90: f'<svg width="{s}" height="{s}" viewBox="0 0 120 120"><path d="M10,64 H26 L60,28 L94,64 H110" fill="none" stroke="{c}" stroke-width="13" stroke-linecap="round" stroke-linejoin="round"/><circle cx="60" cy="80" r="18" fill="#F2A900"/><circle cx="60" cy="80" r="12" fill="none" stroke="#C98200" stroke-width="3"/></svg>'
TETOIC = lambda s: f'<div style="width:{s}px;height:{s}px;border-radius:22%;background:#1B6E4F;display:grid;place-items:center">{TETOMARCA("#fff", int(s*.74))}</div>'

CSS = open('guia.css').read()

def lum(h):
    r, g, b = (int(h[i:i+2], 16)/255 for i in (1, 3, 5))
    return .299*r+.587*g+.114*b

def gerar(id_, a):
    logo = a['logo'].replace('TETOMARCA', TETOMARCA(s=110))
    if id_ == 'teto':
        ic = TETOIC(150)
    elif id_ == 'bentevi-apps':
        ic = '<img src="../assets/bentevi-no-galho.png" style="height:240px;box-shadow:none;border-radius:0;width:auto">'
    else:
        ic = logo
    sw = ''.join(f'<div class="sw"><div class="cx" style="background:{h};color:{"#fff" if lum(h)<.55 else "#1D2B26"}">{h}</div><b>{n}</b><span>{u}</span></div>' for n, h, u in a['cores'])
    fs = ''.join(f'<div class="ft"><div class="amostra" style="font-family:{ {"Baloo 2":"Baloo","Space Grotesk":"SG","Andika":"Andika","Nunito":"Baloo"}.get(f.split(" (")[0],"Roboto")}">{f.split(" (")[0]} · Aa Bb 123</div><b>{f}</b> · {u} <span class="lic">{l}</span></div>' for f, u, l in a['fontes'])
    imgs = ''.join(f'<img src="../assets/{i}">' for i in a['img'])
    telas = ''.join(f'<div class="cel"><img src="../assets/{t}"></div>' for t in a['telas'])
    li = lambda xs: ''.join(f'<li>{x}</li>' for x in xs)
    arq = ''
    if a.get('arquitetura'):
        arq = '<h2>Arquitetura de marca</h2><p>A Bentevi Apps é a marca-mãe; cada app tem nome, cor e personagem próprios e leva a assinatura “um app Bentevi” (ou “um jogo Bentevi”) com o pássaro.</p><div class="arq">' + ''.join(
            f'<div>{TETOIC(110) if f=="TETO" else f"<img src=../assets/{f}>"}<b>{n}</b><span>{d}</span></div>' for n, f, d in a['arquitetura']) + '</div>'
    endosso = '' if id_ == 'bentevi-apps' else f'''<h2>Assinatura Bentevi Apps</h2><div class="endo"><img src="../assets/pousado-limpo.png"><div><b>um app Bentevi</b> (ou <b>um jogo Bentevi</b>), com o pássaro, no rodapé de peças e na tela Sobre. Toda abertura do app toca a vinheta Bentevi Apps (5 s).
      Cores da marca-mãe: creme #FFF6D9, verde #1D4A3F, ouro #E0A800, amarelo #F7C51E, musgo #557A6E. O {a["nome"]} mantém a própria paleta; a da Bentevi só aparece na assinatura.</div></div>'''
    h = f'''<!doctype html><html><head><meta charset="utf-8"><title>Identidade visual · {a["nome"]}</title><style>{CSS}</style></head><body>
<section class="capa" style="background:{a["fundo"]}"><div class="topo"><img src="../assets/pousado-limpo.png"> Bentevi Apps · Guia de identidade visual</div>
<div class="capa-c"><div class="ic">{ic}</div><h1 style="color:{a["cor"]}">{a["nome"]}</h1><div class="sub">{a["sub"]}</div><div class="prom">“{a["promessa"]}”</div></div>
<div class="rod">Versão 1.0 · novembro de 2026</div></section>
<section><h2>Essência</h2><p class="lead">{a["essencia"]}</p>{arq}
<h2>Logotipo e símbolo</h2><div class="logo">{logo}</div><p>{a["logo_txt"]}</p><p>{a["simbolo"]}</p>
<p class="nota">Área de proteção: deixe em volta do logotipo um espaço livre igual à altura da letra “e”. Tamanho mínimo: 24 px de altura no digital.</p></section>
<section><h2>Cores</h2><div class="sws">{sw}</div>
<h2>Tipografia</h2>{fs}
{f'<h2>Ilustração e personagens</h2><div class="imgs">{imgs}</div>' if imgs else ''}
<h2>Estilo visual</h2><ul>{li(a["visual"])}</ul></section>
<section>{f'<h2>Telas do app</h2><div class="telas">{telas}</div>' if telas else ''}
<div class="duas"><div><h2>Tom de voz</h2><ul>{li(a["voz"])}</ul></div><div><h2>Não fazer</h2><ul class="nao">{li(a["nao"])}</ul></div></div>
{endosso}</section></body></html>'''
    open(f'guias/{id_}.html', 'w').write(h)
    # Markdown
    md = [f'# Identidade visual · {a["nome"]}', '', f'*{a["sub"]}* · Guia da Bentevi Apps, versão 1.0 (novembro de 2026). Versão ilustrada: `identidade-visual-{id_}.pdf`, nesta mesma pasta.', '',
          '## Essência', '', a['essencia'], '', f'**Promessa:** {a["promessa"]}', '']
    if a.get('arquitetura'):
        md += ['## Arquitetura de marca', '', 'A Bentevi Apps é a marca-mãe; cada app tem nome, cor e personagem próprios e leva a assinatura “um app Bentevi” (ou “um jogo Bentevi”) com o pássaro.', '',
               '| App | Papel |', '|---|---|'] + [f'| {n} | {d} |' for n, _, d in a['arquitetura']] + ['']
    md += ['## Logotipo e símbolo', '', a['logo_txt'], '', a['simbolo'], '', 'Área de proteção: espaço livre igual à altura da letra “e” em volta do logotipo. Tamanho mínimo: 24 px de altura.', '',
           '## Cores', '', '| Nome | Hex | Uso |', '|---|---|---|'] + [f'| {n} | `{h}` | {u} |' for n, h, u in a['cores']] + ['',
           '## Tipografia', '', '| Fonte | Uso | Licença |', '|---|---|---|'] + [f'| {f} | {u} | {l} |' for f, u, l in a['fontes']] + ['',
           '## Estilo visual', ''] + [f'- {x}' for x in a['visual']] + ['', '## Tom de voz', ''] + [f'- {x}' for x in a['voz']] + ['', '## Não fazer', ''] + [f'- {x}' for x in a['nao']] + ['']
    if id_ != 'bentevi-apps':
        md += ['## Assinatura Bentevi Apps', '', f'“um app Bentevi” (ou “um jogo Bentevi”), com o pássaro, no rodapé de peças e na tela Sobre; a vinheta Bentevi Apps (5 s) abre o app. Cores da marca-mãe: creme `#FFF6D9`, verde `#1D4A3F`, ouro `#E0A800`, amarelo `#F7C51E`, musgo `#557A6E`. O {a["nome"]} mantém a própria paleta; a da Bentevi só aparece na assinatura.', '']
    open(f'guias/{id_}.md', 'w').write('\n'.join(md))

for k, v in APPS.items():
    gerar(k, v)
print('ok')
