# App Android (Capacitor)

Empacota o jogo da Versão B (`versao-b-quitanda-zen/index.html`) como app Android, com anúncios **de teste** do AdMob.

## Baixar o APK pronto

A cada mudança no jogo ou nesta pasta, o GitHub compila o APK sozinho:

1. Abra a aba **Actions** do repositório e entre na execução mais recente de **Apps Android (APKs de teste)**.
2. No fim da página, em **Artifacts**, baixe **quitanda-apk-teste** (vem num .zip).
3. Copie o `app-debug.apk` para o celular Android e abra. O Android vai pedir para permitir a instalação de apps de fonte desconhecida.

Também dá para compilar na hora: **Actions → Apps Android (APKs de teste) → Run workflow**.

## Anúncios

- No app, os anúncios simulados viram anúncios reais do AdMob, com os **IDs de teste oficiais do Google**: aparecem com a marca "Test Ad" e não geram receita.
- No navegador, o jogo continua com anúncios simulados.
- Na publicação, os IDs reais vêm das variáveis do repositório `ADMOB_APP_ID`, `ADMOB_REWARDED_ID` e `ADMOB_INTERSTITIAL_ID` (veja `docs/loja-play/quitanda-zen/LEIAME.md`). Não é preciso editar o código.
- Nunca clique nos seus próprios anúncios reais: o AdMob pode suspender a conta.

## Compilar no computador

Precisa de Node 22+, JDK 21 e Android Studio (ou o Android SDK).

```bash
cd app-android
npm ci
npm run sync          # copia o jogo e atualiza o projeto Android
cd android && ./gradlew assembleDebug
```

O APK sai em `android/app/build/outputs/apk/debug/app-debug.apk`.

## Publicar na Play Store

- O AAB assinado sai em **Actions → Quitanda · AAB para a Play Store → Run workflow**.
- O passo a passo completo (chave de upload, AdMob, textos, imagens e respostas da Play Console) está em `docs/loja-play/quitanda-zen/LEIAME.md`.
- O identificador `com.feiraviva.quitanda` não pode mudar depois da publicação.
