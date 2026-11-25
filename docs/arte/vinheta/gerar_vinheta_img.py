"""Gera o bloco VINHETA_IMG (WebP em base64) a partir dos recortes. Uso: python gerar_vinheta_img.py > vinheta-img.js
Depois, troque o bloco "const VINHETA_IMG={...};" nos index.html (Quitanda, Rota) e o vinheta-img.js do Ler Brincando."""
import base64, io, os
from PIL import Image
AQUI=os.path.dirname(os.path.abspath(__file__)); F=0.75
NOMES=['galho','pousado','cantando','v2_corpo','v2_asacima','v2_asabaixo','v2_pouso']
linhas=[]
for n in NOMES:
    im=Image.open(os.path.join(AQUI,'recortes',n+'.png')); w,h=im.size
    b=io.BytesIO(); im.resize((round(w*F),round(h*F)),Image.LANCZOS).save(b,'WEBP',quality=82,method=6)
    linhas.append(f"  {n}:'data:image/webp;base64,{base64.b64encode(b.getvalue()).decode()}'")
print('/* Arte da vinheta (WebP embutido). Originais em docs/arte/vinheta/. */\nconst VINHETA_IMG={\n'+',\n'.join(linhas)+'\n};')
