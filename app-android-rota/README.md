# App Android da Versão A (Rota das Feiras)

Empacota o protótipo de teste da Versão A (`versao-a-rota-das-feiras/index.html`) como app Android com Capacitor. Sem anúncios; a loja do jogo tem compras simuladas (nada é cobrado).

## Baixar o APK pronto

1. Abra a aba **Actions** do repositório e entre na execução mais recente de **Apps Android (APKs de teste)**.
2. Em **Artifacts**, baixe **rota-das-feiras-apk-teste** (vem num .zip).
3. Copie o `app-debug.apk` para o celular Android e abra. O Android vai pedir para permitir a instalação de apps de fonte desconhecida.

O app instala ao lado da Quitanda (identificadores diferentes: `com.feiraviva.rota` e `com.feiraviva.quitanda`).

## Compilar no computador

Precisa de Node 22+, JDK 21 e Android Studio (ou o Android SDK).

```bash
cd app-android-rota
npm ci
npm run sync
cd android && ./gradlew assembleDebug
```
