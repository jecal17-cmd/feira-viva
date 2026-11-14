import sys, subprocess, html
voz, estilo, taxa, texto, saida = sys.argv[1:6]
lang = voz[:5]
corpo = html.escape(texto).replace('[pausa]','<break time="250ms"/>')
if estilo != '-': corpo = f'<mstts:express-as style="{estilo}">{corpo}</mstts:express-as>'
ssml = f'<speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis" xmlns:mstts="https://www.w3.org/2001/mstts" xml:lang="{lang}"><voice name="{voz}"><prosody rate="{taxa}">{corpo}</prosody></voice></speak>'
r = subprocess.run(['curl','-sS','-X','POST','https://brazilsouth.tts.speech.microsoft.com/cognitiveservices/v1','-H','Ocp-Apim-Subscription-Key: x',
  '-H','Content-Type: application/ssml+xml','-H','X-Microsoft-OutputFormat: riff-24khz-16bit-mono-pcm','-H','User-Agent: feira-viva','--data-binary','@-','-o',saida,'-w','%{http_code}'],
  input=ssml.encode(), capture_output=True)
print(saida, r.stdout.decode(), r.stderr.decode())
