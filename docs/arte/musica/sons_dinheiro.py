"""Sons de dinheiro (ganho e gasto) para Quitanda Zen, Rota das Feiras e Teto. Tudo sintetizado aqui: sem direitos de terceiros.

Uso:  python sons_dinheiro.py PASTA_SAIDA
Gera um .wav (44,1 kHz, mono) por opção.

Ganho (jogos):
  A-moeda       uma moeda tilintando
  B-moedas      punhado de moedas caindo
  C-caixa       caixa registradora: "plim" do sino com a gaveta abrindo
Gasto (Teto):
  D-saida       moeda deslizando para fora, em dois tons que descem
  E-notas       notas sendo contadas, com um "tic" de confirmação
  F-carimbo     carimbo suave de registro
Versão 2 (segundo as referências enviadas): A2-moedinhas, B2-punhado, C2-caixa-antiga, C3-cha-ching
"""
import os, sys, wave
import numpy as np

SR = 44100
rng = np.random.default_rng(42)

def t_(d): return np.arange(int(d * SR)) / SR
def env(t, a, d): return np.minimum(1, t / max(a, 1e-4)) * np.exp(-t / d)

def moeda(f0=2600, d=.9, v=1.0, brilho=1.0):
    """Moeda: parciais inarmônicas de disco metálico, com batida curta no início."""
    t = t_(d); s = np.zeros_like(t)
    for r, a, dec in [(1, 1, .32), (1.53, .7, .22), (2.12, .5, .16), (2.67, .35, .12), (3.43, .22, .08)]:
        s += a * np.sin(2 * np.pi * f0 * r * t + rng.random() * 6) * np.exp(-t / (dec * brilho))
    s *= np.minimum(1, t / .0015)
    clique = rng.standard_normal(len(t)) * np.exp(-t / .004) * .5
    return (s * .32 + np.diff(clique, prepend=0)) * v

def sino(f=1760, d=1.2, v=1.0):
    t = t_(d)
    s = np.sin(2 * np.pi * f * t) + .5 * np.sin(2 * np.pi * f * 2.0 * t) * np.exp(-t * 3) + .3 * np.sin(2 * np.pi * f * 3.01 * t) * np.exp(-t * 6)
    return s * env(t, .002, .45) * .35 * v

def chocalho_metal(d=.18, v=1.0):
    t = t_(d); n = np.diff(rng.standard_normal(len(t)), prepend=0)
    return n * env(t, .004, .05) * .25 * v

def baque(f=140, d=.25, v=1.0):
    t = t_(d); f_ = f * (1 + .8 * np.exp(-t / .02)); ph = 2 * np.pi * np.cumsum(f_) / SR
    return (np.sin(ph) * env(t, .002, .07) + .3 * rng.standard_normal(len(t)) * np.exp(-t / .006)) * .55 * v

def tom(f0, f1, d, v=1.0, forma='seno'):
    t = t_(d); f = f0 * (f1 / f0) ** (t / d); ph = 2 * np.pi * np.cumsum(f) / SR
    s = np.sin(ph) + (.25 * np.sin(2 * ph) if forma == 'cheio' else 0)
    return s * np.minimum(1, t / .01) * np.clip((d - t) / .06, 0, 1) * .3 * v

def deslize(d=.35, v=1.0, f_alta=4500, f_baixa=1500):
    """Ruído filtrado que desce, como algo deslizando para fora."""
    n = rng.standard_normal(int(d * SR)); X = np.fft.rfft(n); fr = np.fft.rfftfreq(len(n), 1 / SR)
    out = np.zeros(len(n)); passos = 8
    for k in range(passos):
        fc = f_alta * (f_baixa / f_alta) ** (k / (passos - 1)); banda = np.exp(-((fr - fc) / (fc * .35)) ** 2)
        seg = np.fft.irfft(X * banda, len(n)); i0, i1 = k * len(n) // passos, (k + 1) * len(n) // passos
        janela = np.zeros(len(n)); janela[i0:i1] = np.hanning(i1 - i0); out += seg * janela
    return out / (np.abs(out).max() + 1e-9) * .22 * v

def papel(d=.06, v=1.0):
    t = t_(d); n = rng.standard_normal(len(t)); X = np.fft.rfft(n); fr = np.fft.rfftfreq(len(n), 1 / SR)
    n = np.fft.irfft(X * ((fr > 1800) & (fr < 7000)), len(n))
    return n / (np.abs(n).max() + 1e-9) * env(t, .003, .018) * .3 * v

def mix(partes, dur):
    out = np.zeros(int(dur * SR))
    for sig, t0, g in partes:
        i = int(t0 * SR); j = min(len(out), i + len(sig)); out[i:j] += sig[:j - i] * g
    return out

def finalizar(x, pico=.85, fade=.02):
    n = int(fade * SR); x[-n:] *= np.linspace(1, 0, n)
    return x / (np.abs(x).max() + 1e-9) * pico

SONS = {
    'A-moeda': lambda: mix([(moeda(2600), 0, 1), (moeda(2600, .5, .35), .085, 1)], .9),
    'B-moedas': lambda: mix([(moeda(f, .7, v), t, 1) for f, t, v in [(2400, 0, 1), (2950, .07, .8), (2200, .13, .7), (3300, .19, .6), (2700, .27, .5), (3100, .36, .35)]]
                            + [(chocalho_metal(.12, .6), .02, 1), (chocalho_metal(.1, .4), .2, 1)], 1.0),
    'C-caixa': lambda: mix([(chocalho_metal(.08, .9), 0, 1), (baque(180, .2, .7), .05, 1), (chocalho_metal(.22, .8), .07, 1),
                            (sino(1760, 1.2, 1), .16, 1), (sino(2637, .9, .55), .165, 1), (moeda(2900, .5, .4), .3, 1)], 1.3),
    'D-saida': lambda: mix([(moeda(2500, .35, .55, .7), 0, 1), (deslize(.35, .9), .03, 1), (tom(880, 830, .16, .8), .12, 1), (tom(660, 620, .3, .8), .27, 1)], .7),
    'E-notas': lambda: mix([(papel(.06, 1 - .08 * k), .065 * k, 1) for k in range(5)] + [(tom(1320, 1320, .07, .8), .42, 1)], .65),
    'F-carimbo': lambda: mix([(baque(120, .25, 1), 0, 1), (papel(.05, .5), .005, 1), (tom(990, 990, .09, .45), .12, 1), (tom(1485, 1485, .14, .4), .2, 1)], .5),
}

# ---------------- versão 2: perfis medidos nas referências enviadas (moedas agudas, caixa antiga e "cha-ching") ----------------
def tilim(v=1.0, d=.16, base=None):
    """Batida de moeda contra moeda: parciais agudas (5,5 a 12 kHz) que somem rápido."""
    t = t_(d); base = base or rng.uniform(5200, 5900); s = np.zeros_like(t)
    for r, a, dec in [(1, .8, .05), (1.72, 1, .045), (2.2, .55, .03), (2.95, .3, .02)]:
        f = base * r * rng.uniform(.985, 1.015)
        if f < 15000: s += a * np.sin(2 * np.pi * f * t + rng.random() * 6) * np.exp(-t / dec)
    clique = np.diff(rng.standard_normal(len(t)), prepend=0) * np.exp(-t / .0025) * .35
    return (s * np.minimum(1, t / .0008) * .3 + clique) * v

def punhado(n, dur, v=1.0):
    ts = np.sort(rng.uniform(0, dur, n)); ts[0] = 0
    return [(tilim(rng.uniform(.45, 1.0) * v), t, 1) for t in ts]

def catraca(n, dur, v=1.0):
    """Mecanismo da caixa antiga: cliques secos com ressonância de metal (3 a 7,5 kHz)."""
    out = []
    for k in range(n):
        t0 = k * dur / n + rng.uniform(-.01, .01); d = .05; t = t_(d); s = np.zeros_like(t)
        for f in rng.choice([3300, 3600, 4750, 4900, 5350, 5850, 7600], 3, replace=False): s += np.sin(2 * np.pi * f * t) * np.exp(-t / .012)
        s += np.diff(rng.standard_normal(len(t)), prepend=0) * np.exp(-t / .003) * 1.5
        out.append((s * .12 * v * rng.uniform(.6, 1), max(0, t0), 1))
    return out

def sino_caixa(f=2064, d=1.6, v=1.0, parciais=((1, 1, .38), (2.525, .17, .2), (.333, .03, .3)), ataque=.002):
    t = t_(d); s = sum(a * np.sin(2 * np.pi * f * r * t) * np.exp(-t / dec) for r, a, dec in parciais)
    return s * np.minimum(1, t / ataque) * .4 * v

def estalo(d=.2, v=1.0):
    """O "cha" do cha-ching: ruído com faixas em 1,5 a 2,2 kHz e 6 a 10 kHz."""
    n = rng.standard_normal(int(d * SR)); X = np.fft.rfft(n); fr = np.fft.rfftfreq(len(n), 1 / SR)
    b = np.exp(-((fr - 1850) / 400) ** 2) + .8 * np.exp(-((fr - 7500) / 2200) ** 2)
    y = np.fft.irfft(X * b, len(n)); t = t_(d)
    return y / np.abs(y).max() * env(t, .003, .06) * .45 * v

SONS.update({
    'A2-moedinhas': lambda: mix([(tilim(1, base=5600), 0, 1), (tilim(.8, base=5350), .075, 1), (tilim(.5, base=5800), .16, 1)], .45),
    'B2-punhado': lambda: mix(punhado(14, .75) + [(chocalho_metal(.3, .25), 0, 1)], 1.0),
    'C2-caixa-antiga': lambda: mix(catraca(9, .42) + [(baque(160, .2, .8), .47, 1), (chocalho_metal(.12, .5), .48, 1), (sino_caixa(2064, 1.6, 1), .52, 1)] + punhado(3, .15, .5)[:0], 2.0),
    'C3-cha-ching': lambda: mix([(estalo(.2, 1), 0, 1), (sino_caixa(5000, 1.3, .9, ((1, 1, .5), (.89, .9, .45), (.305, .45, .35), (1.6, .25, .2)), .001), .13, 1)], 1.4),
})

if __name__ == '__main__':
    out = sys.argv[1]; os.makedirs(out, exist_ok=True)
    for nome, f in SONS.items():
        x = finalizar(f()); w = wave.open(os.path.join(out, nome + '.wav'), 'wb'); w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
        w.writeframes((x * 32767).astype(np.int16).tobytes()); w.close(); print(nome, f'{len(x) / SR:.2f} s')
