# Chave fixa dos APKs de teste

`apk-teste.keystore` assina os APKs de teste dos dois jogos (Quitanda Zen e Rota das Feiras).

- **Para que serve:** como a chave é sempre a mesma, o celular aceita instalar o APK novo **por cima** do antigo, sem desinstalar (e sem perder o progresso salvo).
- **Não é a chave da Play Store.** O AAB de publicação usa a chave de upload guardada nos segredos do repositório (`QUITANDA_KEYSTORE_BASE64`). Esta aqui é pública de propósito e só vale para testes.
- Dados: apelido `apkteste`, senhas `android`. Impressão digital SHA-256:
  `BF:0A:A4:C4:77:9C:DA:A0:60:6C:87:5B:5C:83:10:80:D4:DC:93:5C:81:B2:5D:27:63:74:3F:30:04:F0:88:BB`
- **Não troque este arquivo:** se a chave mudar, será preciso desinstalar o app no celular mais uma vez.
- Configuração: bloco `signingConfigs.debug` em `app-android/android/app/build.gradle` e `app-android-rota/android/app/build.gradle`. O workflow *Apps Android (APKs de teste)* confere a impressão digital a cada APK.
