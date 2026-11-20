# Compras com dinheiro real (Google Play)

Como funciona o motor de compras dos dois jogos e o que falta fazer na Play Console para ligá-lo.

## Como está montado

| Parte | Onde | O que faz |
|---|---|---|
| Motor do jogo | Bloco `COMPRAS` no `index.html` de cada jogo (mesmo código) | Mostra os preços da Google Play, abre a compra, entrega o item, salva e conclui a compra |
| Plugin nativo | `app-android*/android/app/src/main/java/com/feiraviva/compras/ComprasPlugin.java` (mesmo arquivo nos dois apps) | Conversa com a Google Play (Play Billing 8.0.0); registrado no `MainActivity` |
| Chave | `const PAGAMENTO='simulado'` no `index.html` | O `copy-web.js` troca para `'play'` quando roda com `COMPRAS=play` |

**Modos**

- **Simulado** (navegador e APKs de teste do workflow *Apps Android*): confirmação do próprio jogo, nada é cobrado. É como era antes.
- **Google Play** (`COMPRAS=play`): a própria Google Play mostra a confirmação e cobra, no preço e na moeda do jogador. A Loja ganha o botão **Restaurar compras**. Só funciona no app baixado da Play Store (teste interno, fechado ou produção): os APKs de teste são assinados com outra chave e a Google Play recusa.

**Regras do motor**

- Cada compra tem um token. O jogo guarda os tokens já entregues (`S.iap.tok`, até 200) e nunca entrega a mesma compra duas vezes, mesmo que ela chegue pelo aviso e pela conferência ao mesmo tempo.
- O jogo primeiro entrega e salva; só depois avisa a Google Play. Se o app fechar no meio, a compra volta na próxima abertura e só é concluída, sem entregar de novo. Compras não concluídas em 3 dias são reembolsadas pela própria Google Play.
- **Consumíveis** (moedas, ferramentas e a maioria dos kits): são consumidos e podem ser comprados de novo.
- **Permanentes** (`qz_noads_0`, `qz_pack_p1`, `rf_pack_k1`): são reconhecidos e nunca consumidos. Depois de reinstalar o jogo ou trocar de celular (mesma conta Google), "Remover anúncios" volta sozinho e o kit fica marcado como comprado, sem repetir as moedas.
- **Pagamento pendente** (boleto, Pix por código, dinheiro em loja): o jogo avisa e entrega quando a Google Play confirmar.
- O jogo confere as compras ao abrir e sempre que volta para a frente da tela.
- Produto que a Google Play não devolve (não criado ou inativo) aparece como **Indisponível**, com o botão desligado.
- Atenção: o "Remover anúncios" que vem dentro do Kit Quitanda Lendária (`qz_pack_p4`, consumível) fica só no progresso do jogo; numa reinstalação ele só volta pelo código de **Trocar de aparelho**.

## O que fazer na Play Console (Quitanda)

1. **Perfil de pagamentos:** Play Console → Configuração → Perfil de pagamentos. Sem ele não dá para criar produtos pagos.
2. **Enviar um AAB com o plugin:** a Play Console só libera a criação de produtos depois de receber um app que tenha a biblioteca de pagamentos. Rode **Actions → Quitanda · AAB para a Play Store → Run workflow** (pode ser com "compras" desmarcado) e envie ao teste interno.
3. **Criar os produtos:** Monetizar → Produtos → Produtos no app → Criar produto. O ID tem que ser **exatamente** o da tabela abaixo (não dá para mudar depois). Preencha nome, descrição e o preço em US$ (a Play converte para as outras moedas) e **ative** o produto.
4. **Chave de licença (recomendado):** Monetizar → Configuração de monetização → copie a chave (texto longo em base64) e grave no GitHub em Settings → Secrets and variables → Actions → **Variables** → `PLAY_LICENSE_KEY`. Com ela, o app confere a assinatura de cada compra e ignora compras falsificadas.
5. **Testadores de licença:** Configuração → Teste de licença → inclua os e-mails dos testadores. Eles compram com cartões de teste e nada é cobrado.
6. **Gerar o AAB com a Loja ligada:** Actions → Quitanda · AAB para a Play Store → Run workflow, marcando **compras**. Envie ao teste interno, instale pela Play Store e compre com uma conta de testador.
7. Conferir: preço em reais na Loja, compra de moedas (repetir), "Remover anúncios" (não deixa comprar de novo), desinstalar e instalar de novo (o "Remover anúncios" volta), compra pendente ("Lento, aprovado depois" no cartão de teste).

A Play Console não separa consumível de permanente: todos são "produtos no app". Quem decide é o jogo, pela tabela abaixo.

### Produtos da Quitanda Zen (`com.feiraviva.quitanda`)

| ID do produto | Nome | Tipo no jogo | Preço (US$) |
|---|---|---|---|
| `qz_pack_p1` | Kit Boas-vindas / Welcome kit | Permanente (só 1 vez) | 0.99 |
| `qz_pack_p2` | Kit Viajante / Traveler kit | Consumível | 3.99 |
| `qz_pack_p3` | Kit Feirante / Vendor kit | Consumível | 6.99 |
| `qz_pack_p4` | Kit Quitanda Lendária / Legendary Quitanda kit | Consumível | 9.99 |
| `qz_coins_c1` | 300 moedas / 300 coins | Consumível | 0.50 |
| `qz_coins_c2` | 1.000 moedas / 1,000 coins | Consumível | 1.49 |
| `qz_coins_c3` | 2.500 moedas / 2,500 coins | Consumível | 2.99 |
| `qz_coins_c4` | 6.000 moedas / 6,000 coins | Consumível | 5.99 |
| `qz_coins_c5` | 12.000 moedas / 12,000 coins | Consumível | 9.99 |
| `qz_item_r3` | 3 Recargas / 3 Refills | Consumível | 0.99 |
| `qz_item_m3` | 3 Junta-tudo / 3 Magnets | Consumível | 0.99 |
| `qz_item_r10` | 10 Recargas / 10 Refills | Consumível | 2.49 |
| `qz_item_m10` | 10 Junta-tudo / 10 Magnets | Consumível | 2.49 |
| `qz_noads_0` | Remover anúncios / Remove ads | Permanente | 2.99 |

### Produtos da Rota das Feiras (`com.feiraviva.rota`)

A Rota ainda não tem app na Play Console nem workflow de AAB. Quando tiver, os produtos são estes, e o empacotamento usa `COMPRAS=play node scripts/copy-web.js`.

| ID do produto | Nome | Tipo no jogo | Preço (US$) |
|---|---|---|---|
| `rf_pack_k1` | Kit do Feirante / Vendor Kit | Permanente (só 1 vez) | 1.99 |
| `rf_pack_k2` | Kit Maré Cheia / High Tide Kit | Consumível | 2.49 |
| `rf_pack_k3` | Kit Mestre da Feira / Market Master Kit | Consumível | 5.99 |
| `rf_pack_k4` | Kit Banca Completa / Full Stall Kit | Consumível | 9.99 |
| `rf_coins_c1` | 150 moedas / 150 coins | Consumível | 0.50 |
| `rf_coins_c2` | 500 moedas / 500 coins | Consumível | 1.49 |
| `rf_coins_c3` | 1.200 moedas / 1,200 coins | Consumível | 2.99 |
| `rf_coins_c4` | 2.500 moedas / 2,500 coins | Consumível | 4.99 |
| `rf_coins_c5` | 6.000 moedas / 6,000 coins | Consumível | 9.99 |
| `rf_item_t1` | 1 +3 Turnos / 1 +3 Turns | Consumível | 0.50 |
| `rf_item_h3` | 3 Martelos / 3 Hammers | Consumível | 0.99 |
| `rf_item_p3` | 3 Caldeirões / 3 Cauldrons | Consumível | 0.99 |
| `rf_item_t3` | 3 +3 Turnos / 3 +3 Turns | Consumível | 1.29 |
| `rf_item_t10` | 10 +3 Turnos / 10 +3 Turns | Consumível | 3.99 |

O ID sai da chave do item no jogo: prefixo do jogo (`qz` ou `rf`) + `_` + chave com `_` no lugar de `-` (`pack-p1` → `qz_pack_p1`). Um item novo na `SHOP` vira um produto novo com esse ID.

## Limites conhecidos

- Não há servidor: a conferência é a assinatura no próprio aparelho (com `PLAY_LICENSE_KEY`). Um servidor com a Google Play Developer API seria mais seguro, mas não é necessário para começar.
- A compilação do plugin só é testada no GitHub Actions (não há Android SDK nas sessões do Claude). O motor do jogo foi testado no navegador com uma Google Play simulada: compra única, mesma compra chegando duas vezes, app fechado antes de concluir, permanente restaurado após reinstalação, pendente, assinatura falsa, item já comprado e produto indisponível.
