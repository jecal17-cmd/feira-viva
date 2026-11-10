# App Android (Capacitor)

Empacota o jogo da Versão B (`versao-b-quitanda-zen/index.html`) como app Android, com anúncios **de teste** do AdMob.

## Baixar o APK pronto

A cada mudança no jogo ou nesta pasta, o GitHub compila o APK sozinho:

1. Abra a aba **Actions** do repositório e entre na execução mais recente de **App Android (APK de teste)**.
2. No fim da página, em **Artifacts**, baixe **quitanda-apk-teste** (vem num .zip).
3. Copie o `app-debug.apk` para o celular Android e abra. O Android vai pedir para permitir a instalação de apps de fonte desconhecida.

Também dá para compilar na hora: **Actions → App Android (APK de teste) → Run workflow**.

## Anúncios

- No app, os anúncios simulados viram anúncios reais do AdMob, com os **IDs de teste oficiais do Google**: aparecem com a marca "Test Ad" e não geram receita.
- No navegador, o jogo continua com anúncios simulados.
- **Antes de publicar**, troque os IDs de teste pelos seus, criados no AdMob:
  - ID do app: `android/app/src/main/res/values/strings.xml` (`admob_app_id`);
  - blocos de anúncio com recompensa e intersticial: constante `ADMOB` em `versao-b-quitanda-zen/index.html`, com `test:false`.
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

## Antes de publicar na Play Store

- O identificador `com.feiraviva.quitanda` (em `capacitor.config.json` e `android/app/build.gradle`) não pode mudar depois da publicação.
- Gerar uma versão assinada (AAB) com a sua chave, trocar o ícone e a tela de abertura pelos definitivos, e preencher política de privacidade, classificação etária e o formulário de segurança de dados.
