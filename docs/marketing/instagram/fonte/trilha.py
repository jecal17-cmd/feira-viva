"""Trilha 'Baião da Quitanda': zabumba, triângulo, baixo, sanfona e o canto do bem-te-vi. Uso: python trilha.py SAIDA.wav SEGUNDOS"""
import sys, wave, numpy as np
SR=44100; BPM=120; B=60/BPM
out, dur = sys.argv[1], float(sys.argv[2])
N=int(SR*dur); mix=np.zeros(N)
rng=np.random.default_rng(7)
def add(sig,t,g=1.0):
    i=int(t*SR); 
    if i>=N: return
    j=min(N,i+len(sig)); mix[i:j]+=sig[:j-i]*g
def env(n,a,d): t=np.arange(n)/SR; e=np.exp(-t/d); k=int(a*SR); e[:k]*=np.linspace(0,1,k) if k>0 else 1; return e
def zabumba(strong=True):
    n=int(.45*SR); t=np.arange(n)/SR; f=55+75*np.exp(-t/.04); ph=2*np.pi*np.cumsum(f)/SR
    s=.8*np.sin(ph)*env(n,.002,.18 if strong else .1); s+= .25*rng.standard_normal(n)*env(n,0,.012)
    return s*(1 if strong else .6)
def bacalhau():
    n=int(.08*SR); return (rng.standard_normal(n)*env(n,0,.01)+.5*np.sin(2*np.pi*900*np.arange(n)/SR)*env(n,0,.015))*.35
def triangulo(open_=False):
    n=int((.45 if open_ else .06)*SR); t=np.arange(n)/SR; d=.22 if open_ else .025
    return sum(a*np.sin(2*np.pi*f*t) for f,a in [(5280,1),(7130,.6),(9050,.4),(11200,.25)])*env(n,.001,d)*.045
def nota(m): return 440*2**((m-69)/12)
def sanfona(m,d,g=1.0):
    n=int(d*SR); t=np.arange(n)/SR; f=nota(m); s=np.zeros(n)
    for det in (-0.12,0.12):
        ff=f*2**(det/12)*(1+.003*np.sin(2*np.pi*5.5*t))
        ph=2*np.pi*np.cumsum(ff)/SR
        for h,a in [(1,1),(2,.55),(3,.4),(4,.22),(5,.15),(6,.08)]: s+=a*np.sin(h*ph)
    e=np.minimum(1,t/.012)*np.minimum(1,(d-t)/.04).clip(0,1)*(1+.08*np.sin(2*np.pi*6*t))
    return s*e*.11*g
def baixo(m,d):
    n=int(d*SR); t=np.arange(n)/SR; ph=2*np.pi*nota(m)*t
    return (np.sin(ph)+.3*np.sin(2*ph))*env(n,.004,.35)*.2
CH={'G':[55,59,62],'C':[48,52,55],'D':[50,54,57]}
prog=['G','C','D','G','G','C','D','G']
mel=[[(0,.75,74),(.75,.25,71),(1,.5,74),(1.5,.5,79),(2,.75,77),(2.75,.25,76),(3,1,74)],
     [(0,.75,76),(.75,.25,74),(1,.5,72),(1.5,.5,76),(2,1,79),(3,.5,77),(3.5,.5,76)],
     [(0,.75,74),(.75,.25,72),(1,.5,69),(1.5,.5,72),(2,.75,78),(2.75,.25,76),(3,1,74)],
     [(0,.5,71),(.5,.5,74),(1,.5,79),(1.5,.5,77),(2,2,79)]]
mel=mel+[mel[0],mel[1],[(0,.75,74),(.75,.25,76),(1,.5,78),(1.5,.5,81),(2,.75,79),(2.75,.25,78),(3,1,76)],[(0,.5,79),(.5,.5,74),(1,.5,71),(1.5,.5,74),(2,2,79)]]
INI=1.0                                       # o bem-te-vi canta antes da banda entrar
bars=int((dur-INI-1.2)//(4*B))
for b in range(bars):
    t0=INI+b*4*B; ch=prog[b%8]; root=CH[ch][0]-12
    for half in (0,2):
        th=t0+half*B
        add(zabumba(True),th); add(zabumba(False),th+.75*B); add(bacalhau(),th+1.5*B); add(zabumba(True),th+1.0*B,.7)
        add(baixo(root,.7*B),th); add(baixo(root+7,.3*B),th+.75*B); add(baixo(root,.45*B),th+B)
    for s in range(16): add(triangulo(s%4==3),t0+s*B/4, 1.0 if s%4==3 else (.7 if s%2 else .5))
    for k in (.5,1.5,2.5,3.5):
        for m in CH[ch]: add(sanfona(m+12,.22*B,.35),t0+k*B)
    if b>=1 or bars<=4:
        for st,d,m in mel[b%8]: add(sanfona(m,d*B*.95),t0+st*B)
fim=INI+bars*4*B
for m in [55,59,62,67]: add(sanfona(m+12,1.0,.7),fim)
add(zabumba(True),fim,1.2); add(triangulo(True),fim)
# canto do bem-te-vi (gravação) no começo e no fim
w=wave.open('/home/user/feira-viva/docs/arte/bentevi-canto.wav'); bv=np.frombuffer(w.readframes(w.getnframes()),np.int16).astype(float)/32768
if w.getframerate()!=SR: bv=np.interp(np.arange(0,len(bv),w.getframerate()/SR),np.arange(len(bv)),bv)
add(bv,.1,.55); add(bv,fim+.35,.45)
fade=int(.8*SR); mix[-fade:]*=np.linspace(1,0,fade)
mix/=np.abs(mix).max()/0.89
w=wave.open(out,'wb'); w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes((mix*32767).astype(np.int16).tobytes()); w.close()
print(out, dur, 's', bars, 'compassos, fim em', round(fim,2))
