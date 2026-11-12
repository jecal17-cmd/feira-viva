# Quitanda Zen na Google Play: tudo para publicar

Material da página da loja e respostas da Play Console para a **Quitanda Zen** (`com.feiraviva.quitanda`), versão **1.0.0**.

## Arquivos desta pasta

| Arquivo | Onde vai na Play Console | Exigência da loja |
|---|---|---|
| `icone-512.png` | Página principal da loja → Ícone do app | 512 × 512 PNG, até 1 MB |
| `pt-BR/grafico-destaque-1024x500.png` | Gráfico de recursos (pt-BR) | 1024 × 500, obrigatório |
| `en-US/grafico-destaque-1024x500.png` | Gráfico de recursos (inglês) | idem |
| `pt-BR/capturas/1…6.png` | Capturas de tela do telefone (pt-BR) | 2 a 8, 1080 × 1920 |
| `en-US/capturas/1…6.png` | Capturas de tela do telefone (inglês) | idem |
| `*/titulo.txt` | Nome do app | até 30 caracteres |
| `*/descricao-curta.txt` | Descrição curta | até 80 caracteres |
| `*/descricao-completa.txt` | Descrição completa | até 4.000 caracteres |
| `*/novidades.txt` | Notas da versão (na hora de lançar) | até 500 caracteres |

As capturas mostram o jogo real, no modo de publicação (sem a Loja paga). Foram geradas com Playwright, num estado de jogo avançado (nível 14, Mercado Central de Fortaleza), pelo script `gerar-imagens.js` desta pasta: `node docs/loja-play/quitanda-zen/gerar-imagens.js`.

A política de privacidade fica em `versao-b-quitanda-zen/privacidade.html`. Depois do merge na `main`, o endereço público é:

**https://jecal17-cmd.github.io/feira-viva/versao-b-quitanda-zen/privacidade.html**


## Textos da página

| Campo | Português (pt-BR, idioma padrão) | Inglês (en-US) |
|---|---|---|
| Nome | Quitanda Zen: Feira do Brasil | Quitanda: Merge Across Brazil |
| Descrição curta | Junte frutas e quitutes, atenda a freguesia e viaje pelas feiras do Brasil. | Merge fruits and treats, serve customers and travel to markets across Brazil. |

A descrição completa está nos arquivos `descricao-completa.txt`.

## Detalhes do app

| Campo | Resposta |
|---|---|
| App ou jogo | Jogo |
| Categoria | Casual (alternativa: Quebra-cabeça) |
| Tags sugeridas | Juntar (Merge), Casual, Relaxante, Simulação de loja, Offline |
| Gratuito ou pago | Gratuito (não dá para mudar depois) |
| E-mail de contato | jecal17@gmail.com (o mesmo da política de privacidade) |
| Site | opcional; pode ser `https://jecal17-cmd.github.io/feira-viva/` |
| Idioma padrão | Português (Brasil) – pt-BR; adicionar a tradução Inglês (Estados Unidos) – en-US |

## Conteúdo do app (Política → Conteúdo do app)

**Política de privacidade:** o endereço acima.

**Anúncios:** Sim, o app contém anúncios.

**Acesso ao app:** Todas as funcionalidades estão disponíveis sem restrições (não há login).

**Classificação do conteúdo (questionário IARC):**
- Categoria: Jogo.
- Violência, medo, sexo, linguagem imprópria, drogas, álcool e tabaco: **Não** para tudo.
- Jogos de azar ou apostas simuladas: **Não**.
- Os usuários interagem ou trocam conteúdo entre si: **Não**.
- Compartilha a localização do usuário com outros usuários: **Não**.
- Compras de produtos digitais: **Não** (nesta versão não há compras).
- Resultado esperado: **Livre** (ClassInd), **Everyone/E** (ESRB), **PEGI 3**.

**Público-alvo e conteúdo:**
- Faixas etárias recomendadas: **13 a 15, 16 a 17 e 18 ou mais**.
- "O app pode atrair crianças sem intenção?": responda com sinceridade. O visual é de emojis, mas o tema (gerir uma banca de feira) e o texto são para adolescentes e adultos.
- Por que não incluir menores de 13 anos: aí o app entra na política de Famílias, e os anúncios precisam ser marcados como direcionados a crianças (sem anúncios personalizados) e passar por uma revisão mais rígida. Dá para fazer depois, numa atualização.

**Segurança dos dados:** o jogo não envia dados próprios; tudo o que é coletado vem do SDK do Google AdMob.
- Coleta ou compartilha dados do usuário: **Sim**.
- Todos os dados são criptografados em trânsito: **Sim**.
- Oferece um jeito de pedir a exclusão dos dados: **Não** (não há contas; o progresso fica só no aparelho).

| Tipo de dado | Coletado | Compartilhado | Opcional? | Finalidade |
|---|---|---|---|---|
| Local → Local aproximado | Sim | Sim | Não | Publicidade ou marketing; prevenção de fraudes |
| Atividade no app → Interações com o app | Sim | Sim | Não | Publicidade ou marketing; análise |
| Informações e desempenho do app → Registros de falhas; Diagnóstico | Sim | Sim | Não | Análise; prevenção de fraudes |
| Dispositivo ou outros IDs | Sim | Sim | Não | Publicidade ou marketing; prevenção de fraudes |

Confira com o guia oficial do Google: *"Divulgação de dados do SDK dos anúncios para dispositivos móveis do Google"* (support.google.com/admob/answer/11048436). Se o Google atualizar a lista, siga a dele.

**ID de publicidade:** Sim, o app usa o ID de publicidade, para **Publicidade ou marketing**. O SDK do AdMob já inclui a permissão `AD_ID` no manifesto.

**Outros formulários:** app de notícias **Não**; app de rastreamento de contatos ou de saúde **Não**; recursos financeiros **Nenhum**; app governamental **Não**.

## Antes de gerar o AAB final

### 1. Chave de upload (uma vez só)

A Play Store exige que o AAB seja assinado. Com a **Assinatura de apps do Google Play** (padrão para apps novos), o Google guarda a chave final e você assina só com a **chave de upload**. Se ela se perder, dá para pedir uma nova ao suporte do Google.

Para criar a chave no computador (precisa do Java/JDK):

```bash
keytool -genkeypair -v -keystore quitanda-upload.jks -alias upload -keyalg RSA -keysize 2048 -validity 10000
```

Guarde o arquivo `.jks` e as senhas fora do repositório (gerenciador de senhas e um backup). **Nunca** coloque o `.jks` no git.

Em **GitHub → Settings → Secrets and variables → Actions → New repository secret**, crie:

| Segredo | Valor |
|---|---|
| `QUITANDA_KEYSTORE_BASE64` | o `.jks` em base64: `base64 -w0 quitanda-upload.jks` (Linux), `base64 -i quitanda-upload.jks` (Mac) ou `[Convert]::ToBase64String([IO.File]::ReadAllBytes("quitanda-upload.jks"))` (PowerShell) |
| `QUITANDA_KEYSTORE_PASSWORD` | a senha do arquivo |
| `QUITANDA_KEY_ALIAS` | `upload` |
| `QUITANDA_KEY_PASSWORD` | a senha da chave (no keytool atual, a mesma do arquivo) |

### 2. Anúncios reais do AdMob

1. Em [admob.google.com](https://admob.google.com), crie o app Android "Quitanda Zen" (dá para vincular à Play depois de publicado).
2. Crie dois blocos de anúncio: **Premiado** (rewarded) e **Intersticial**.
3. Em **Settings → Secrets and variables → Actions → aba Variables**, crie:

| Variável | Exemplo de formato |
|---|---|
| `ADMOB_APP_ID` | `ca-app-pub-1234567890123456~1234567890` (tem **~**) |
| `ADMOB_REWARDED_ID` | `ca-app-pub-1234567890123456/1111111111` (tem **/**) |
| `ADMOB_INTERSTITIAL_ID` | `ca-app-pub-1234567890123456/2222222222` |

4. No AdMob, em **Privacidade e mensagens**, crie a mensagem de consentimento do GDPR (o jogo já chama esse formulário) e publique.
5. Mais tarde, o AdMob vai pedir o arquivo `app-ads.txt` no site da desenvolvedora (o mesmo informado na Play). Ele precisa ficar na raiz do domínio, por exemplo num repositório `jecal17-cmd.github.io`. Os anúncios funcionam sem ele, mas podem render menos.

Sem essas variáveis, o AAB sai com os anúncios de **teste** do Google: funciona, mas não gera receita. Serve para o teste interno.

### 3. Gerar o AAB

**Actions → Quitanda · AAB para a Play Store → Run workflow**, informando:
- **versao**: `1.0.0` (o que o jogador vê);
- **codigo**: deixe vazio (usa o número da execução) ou informe um número maior que o do último envio.

No fim da execução, baixe o artefato `quitanda-aab-v1.0.0-N` (um .zip com o `.aab`). Se o nome tiver `NAO-ASSINADO`, faltam os segredos do passo 1.

Para compilar no computador: crie `app-android/android/keystore.properties` (já ignorado pelo git) com as mesmas chaves (`QUITANDA_KEYSTORE=caminho/do/arquivo.jks`, `QUITANDA_KEYSTORE_PASSWORD=...`, `QUITANDA_KEY_ALIAS=upload`, `QUITANDA_KEY_PASSWORD=...`) e rode:

```bash
cd app-android
npm ci
PUBLICACAO=1 VERSAO=1.0.0 node scripts/copy-web.js && npx cap sync android
cd android && ./gradlew bundleRelease
```

## O que muda no modo de publicação

O `copy-web.js` com `PUBLICACAO=1` gera o jogo assim:
- **Sem a Loja com dinheiro real.** As compras do protótipo são simuladas, e a Play proíbe vender itens digitais fora do Google Play Billing. O botão de moedas passa a abrir Melhorias. A loja volta quando a cobrança real for integrada.
- **Sem ferramentas de teste** (os 5 toques na versão não fazem nada).
- Versão exibida como "v1.0.0" em vez de "protótipo v0.5".
- **Ajustes** passa a mostrar o link da política de privacidade e, onde a lei exige, o botão "Privacidade dos anúncios".

No navegador (GitHub Pages) e no APK de teste, nada muda.

## Ordem sugerida na Play Console

1. Criar o app: nome "Quitanda Zen", idioma pt-BR, Jogo, Gratuito.
2. Preencher **Conteúdo do app** (seções acima) e a **Página principal da loja** (textos e imagens desta pasta).
3. **Testes → Teste interno**: enviar o AAB, adicionar o seu e-mail como testador e instalar pelo link.
4. Contas pessoais criadas depois de novembro de 2023 precisam de **teste fechado com pelo menos 12 testadores por 14 dias seguidos** antes de liberar a produção.
5. **Produção**: criar a versão com o mesmo AAB (ou um novo, com código maior), colar o `novidades.txt` e enviar para revisão.

## Pendências conhecidas

- O ícone da loja é uma ilustração pintada, enquanto os itens no jogo ainda são emojis. Quando a arte final dos itens chegar, refaça as imagens com `node docs/loja-play/quitanda-zen/gerar-imagens.js`.
- Os nomes "Quitanda" e "Bentevi" ainda não foram verificados no INPI nem nas lojas.
- Não há capturas para tablet (são opcionais). O jogo funciona em tablet, mas foi pensado para celular em pé.
