"""Trilhas de fundo dos 12 mercados do Quitanda Zen.

Cada mercado ganha um loop calmo (16 compassos) com um toque discreto da música do lugar: o ritmo, os timbres e o
andamento lembram o gênero local, mas tudo fica suave, para combinar com o clima "zen" do jogo. O loop fecha sem
emenda (a reverberação e as caudas das notas dão a volta para o começo).

Uso:  python trilhas_mercados.py PASTA_SAIDA [NN ...]
Gera PASTA_SAIDA/NN.wav (44,1 kHz, mono). Para o jogo: ffmpeg -i NN.wav -c:a libopus -b:a 56k NN.ogg
Precisa de numpy.
"""
import os, sys, wave
import numpy as np

SR = 44100

# ----------------------------------------------------------------- instrumentos (tudo vetorizado)
def _t(d): return np.arange(int(d * SR)) / SR
def hz(m): return 440 * 2 ** ((m - 69) / 12)
def env_ad(t, a, d): return np.minimum(1, t / max(a, 1e-4)) * np.exp(-t / d)

def pluck(m, d=1.6, brilho=1.0, dec=1.0):
    """Corda dedilhada (violão, viola, cavaquinho, harpa, banjo): parciais que somem mais rápido quanto mais agudas."""
    t = _t(d); f = hz(m); s = np.zeros_like(t)
    for h in range(1, 9):
        if f * h > 9000: break
        s += (brilho ** (h - 1)) / h * np.sin(2 * np.pi * f * h * t) * np.exp(-t * (1.2 + .9 * h) / dec)
    return s * np.minimum(1, t / .003) * .5

def sanfona(m, d, v=1.0):
    t = _t(d); f = hz(m); s = np.zeros_like(t)
    for det in (-.1, .1):
        ph = 2 * np.pi * np.cumsum(f * 2 ** (det / 12) * (1 + .003 * np.sin(2 * np.pi * 5.2 * t))) / SR
        for h, a in [(1, 1), (2, .5), (3, .32), (4, .16), (5, .08)]: s += a * np.sin(h * ph)
    e = np.minimum(1, t / .03) * np.clip((d - t) / .08, 0, 1)
    return s * e * .16 * v

def sopro(m, d, v=1.0, ar=.08):
    """Flauta / pífano: seno com vibrato e um pouco de sopro."""
    t = _t(d); f = hz(m); vib = 1 + .006 * np.sin(2 * np.pi * 5 * t) * np.minimum(1, t / .4)
    ph = 2 * np.pi * np.cumsum(f * vib) / SR
    s = np.sin(ph) + .18 * np.sin(2 * ph) + .05 * np.sin(3 * ph)
    s += .05 * np.random.default_rng(int(m * 7)).standard_normal(len(t)) * np.exp(-t / .08)
    e = np.minimum(1, t / ar) * np.clip((d - t) / .12, 0, 1)
    return s * e * .3 * v

def rabeca(m, d, v=1.0):
    """Rabeca / violino rústico: dente de serra suavizado com vibrato."""
    t = _t(d); f = hz(m); vib = 1 + .007 * np.sin(2 * np.pi * 5.6 * t) * np.minimum(1, t / .3)
    ph = 2 * np.pi * np.cumsum(f * vib) / SR; s = np.zeros_like(t)
    for h in range(1, 8): s += (.75 ** h) / h * np.sin(h * ph)
    e = np.minimum(1, t / .07) * np.clip((d - t) / .1, 0, 1)
    return s * e * .42 * v

def sino(m, d=1.4, v=1.0):
    t = _t(d); f = hz(m)
    return (np.sin(2 * np.pi * f * t) + .25 * np.sin(2 * np.pi * f * 2.76 * t) * np.exp(-t * 6)) * env_ad(t, .002, .5) * .3 * v

def pad(ms, d, v=1.0):
    t = _t(d); s = sum(np.sin(2 * np.pi * hz(m) * t) + .3 * np.sin(4 * np.pi * hz(m) * t) for m in ms)
    e = np.minimum(1, t / (d * .3)) * np.minimum(1, (d - t) / (d * .3))
    return s * e * .05 * v

_rng = np.random.default_rng(3)
def tambor(f0=90, d=.5, v=1.0, pele=.25):
    t = _t(d); f = f0 * (1 + .6 * np.exp(-t / .03)); ph = 2 * np.pi * np.cumsum(f) / SR
    return (np.sin(ph) * env_ad(t, .002, d * .35) + pele * _rng.standard_normal(len(t)) * np.exp(-t / .015)) * .5 * v

def chocalho(d=.09, v=1.0):
    t = _t(d); n = _rng.standard_normal(len(t)); n = np.diff(n, prepend=0)          # chiado agudo
    return n * env_ad(t, .006, d * .3) * .08 * v

def agogo(alto=True, v=1.0):
    t = _t(.35); f = 1250 if alto else 900
    return (np.sin(2 * np.pi * f * t) + .4 * np.sin(2 * np.pi * f * 2.4 * t)) * env_ad(t, .001, .09) * .12 * v

def triangulo(aberto=False, v=1.0):
    t = _t(.4 if aberto else .06)
    return sum(a * np.sin(2 * np.pi * f * t) for f, a in [(5280, 1), (7130, .6), (9050, .35)]) * env_ad(t, .001, .2 if aberto else .02) * .03 * v

def palma(v=1.0):
    t = _t(.12); n = _rng.standard_normal(len(t))
    e = sum(np.exp(-np.maximum(0, t - k * .008) / .01) * (t >= k * .008) for k in range(3))
    return np.diff(n, prepend=0) * e * .07 * v

# ----------------------------------------------------------------- harmonia e melodia
MAIOR, MENOR, MIXO = [0, 2, 4, 5, 7, 9, 11], [0, 2, 3, 5, 7, 8, 10], [0, 2, 4, 5, 7, 9, 10]

def nota_escala(raiz, esc, grau):          # grau 0 = tônica; pode passar de 7 (oitavas)
    o, g = divmod(grau, 7); return raiz + 12 * o + esc[g]

def acorde(raiz, esc, grau):
    return [nota_escala(raiz, esc, grau + k) for k in (0, 2, 4)]

def melodia(raiz, esc, prog, ritmos, semente, faixa=(7, 15)):
    """Motivo de 4 compassos que se repete com variação (A A' B A''): soa composto, não aleatório."""
    rng = np.random.default_rng(semente)
    def frase(prog4, ritmo4, ini):
        g = ini; ev = []
        for b, (cg, rit) in enumerate(zip(prog4, ritmo4)):
            tons = [cg + k for k in (0, 2, 4, 7, 9, 11)]
            for k, (st, du) in enumerate(rit):
                if k == 0:   # cai num tom do acorde, perto da nota anterior
                    g = min([x for x in tons if faixa[0] <= x <= faixa[1]] or [cg + 7], key=lambda x: abs(x - g) + rng.random() * .5)
                else:
                    g = int(np.clip(g + rng.choice([-2, -1, -1, 1, 1, 2, 0]), *faixa))
                ev.append((b, st, du, g))
        return ev
    A = frase(prog[0:4], ritmos[0:4], 9)
    B = frase(prog[8:12], ritmos[8:12], 11)
    ev = [(b, s, d, g) for b, s, d, g in A]
    ev += [(b + 4, s, d, g) for b, s, d, g in A[:-2]] + [(7, s, d, g) for b, s, d, g in frase(prog[7:8], ritmos[7:8], A[-1][3])]
    ev += [(b + 8, s, d, g) for b, s, d, g in B]
    fim = [(b + 12, s, d, g) for b, s, d, g in A if b < 3]
    ult = ritmos[15]; fim += [(15, ult[0][0], sum(x[1] for x in ult), 7)]   # termina na tônica
    ev += fim
    return [(b, s, d, nota_escala(raiz, esc, g)) for b, s, d, g in ev]

# ----------------------------------------------------------------- estilos
def estilo(nome):
    R = {}
    if nome == '01':   # Belém · carimbó: curimbó, maracas, banjo, flauta
        R.update(bpm=100, comp=4, raiz=62, esc=MIXO, prog=[0, 0, 4, 4, 3, 3, 4, 0, 3, 3, 0, 0, 4, 3, 4, 0], lead='sopro', semente=11)
        R['perc'] = lambda b: [('tambor', 0, 1, 85), ('tambor', 1.5, .6, 120), ('tambor', 2, .9, 85), ('tambor', 3.5, .6, 120)] + [('chocalho', k / 2, .8 if k % 2 else .5) for k in range(8)]
        R['comp_'] = lambda b, ac: [('pluck', s, ac[k % 3] + 12, .5, .9, .5) for k, s in enumerate([.5, 1.5, 2.5, 3.5])] + [('pluck', 0, ac[0] - 12, .8, .4, 1.2)]
        R['rit'] = [[(0, 1), (1, .5), (1.5, .5), (2, 2)], [(0, .5), (.5, .5), (1, 1), (2, 1), (3, 1)]] * 8
    elif nome == '02':   # Manaus · toada de boi: marcação, palmas, dedilhado, pad
        R.update(bpm=92, comp=4, raiz=64, esc=MENOR, prog=[0, 5, 2, 6, 0, 5, 3, 4, 5, 2, 6, 0, 3, 5, 4, 0], lead='sopro', semente=12)
        R['perc'] = lambda b: [('tambor', 0, 1, 70), ('tambor', 2, 1, 70), ('palma', 1, .6), ('palma', 3, .6), ('chocalho', 3.5, .5)]
        R['comp_'] = lambda b, ac: [('pluck', k * .5, [ac[0], ac[1], ac[2], ac[1] + 12, ac[2], ac[1], ac[0] + 12, ac[2]][k], .5, .7, .8) for k in range(8)] + [('pad', 0, ac, 4)]
        R['rit'] = [[(0, 1.5), (1.5, .5), (2, 2)], [(0, 1), (1, 1), (2, 2)]] * 8
    elif nome == '03':   # Salvador · ijexá: agogô, atabaque suave, violão
        R.update(bpm=96, comp=4, raiz=67, esc=MAIOR, prog=[0, 3, 1, 4, 0, 3, 1, 4, 5, 3, 4, 0, 5, 1, 4, 0], lead='sino', semente=13)
        R['perc'] = lambda b: [('agogo', 0, 1, 1), ('agogo', .75, .6, 1), ('agogo', 1.5, .7, 0), ('agogo', 2, .8, 1), ('agogo', 3, .7, 0), ('agogo', 3.5, .6, 0),
                               ('tambor', 0, .7, 140), ('tambor', 1.5, .5, 180), ('tambor', 2.5, .6, 140), ('tambor', 3, .5, 110)] + [('chocalho', k / 2, .5) for k in range(8)]
        R['comp_'] = lambda b, ac: [('pluck', s, n, .6, .8, .7) for s, n in [(0, ac[0] - 12), (.75, ac[1]), (1.5, ac[2]), (2, ac[0] - 12), (2.75, ac[1]), (3.5, ac[2])]]
        R['rit'] = [[(0, .75), (.75, .75), (1.5, 2.5)], [(0, 1), (1, .5), (1.5, .5), (2, 2)]] * 8
    elif nome == '04':   # Recife · ciranda: bumbo lento, ganzá, violão
        R.update(bpm=84, comp=4, raiz=69, esc=MENOR, prog=[0, 0, 3, 3, 6, 6, 4, 4, 0, 3, 6, 2, 3, 6, 4, 0], lead='sopro', semente=14)
        R['perc'] = lambda b: [('tambor', 0, 1.1, 60), ('tambor', 3, .5, 75)] + [('chocalho', k / 4, .6 if k % 4 == 2 else .35) for k in range(16)]
        R['comp_'] = lambda b, ac: [('pluck', s, n, .55, .8, .9) for s, n in [(0, ac[0] - 12), (1, ac[1]), (1.5, ac[2]), (2, ac[0]), (3, ac[1]), (3.5, ac[2])]]
        R['rit'] = [[(0, 2), (2, 1), (3, 1)], [(0, 1), (1, 1), (2, 2)]] * 8
    elif nome == '05':   # Fortaleza · baião com rabeca
        R.update(bpm=100, comp=4, raiz=65, esc=MIXO, prog=[0, 0, 4, 0, 3, 3, 4, 0, 3, 0, 4, 0, 3, 4, 4, 0], lead='rabeca', semente=15)
        R['perc'] = lambda b: [x for h in (0, 2) for x in [('tambor', h, .9, 80), ('tambor', h + .75, .5, 80), ('tambor', h + 1, .7, 95)]] + [('triangulo', k / 4, .6 if k % 4 == 3 else .3, k % 4 == 3) for k in range(16)]
        R['comp_'] = lambda b, ac: [('pluck', s, ac[0] - 12, .6, .5, 1) for s in (0, .75, 2, 2.75)] + [('sanf', s, ac, .3) for s in (1, 3)]
        R['rit'] = [[(0, .75), (.75, .25), (1, 1), (2, 2)], [(0, .5), (.5, .5), (1, .5), (1.5, .5), (2, 2)]] * 8
    elif nome == '06':   # Campo Grande · guarânia: harpa paraguaia em 3/4
        R.update(bpm=84, comp=3, raiz=62, esc=MAIOR, prog=[0, 0, 4, 4, 3, 4, 0, 0, 5, 1, 4, 0, 3, 4, 4, 0], lead='harpa', semente=16)
        R['perc'] = lambda b: [('chocalho', 1, .3), ('chocalho', 2, .3)]
        R['comp_'] = lambda b, ac: [('pluck', 0, ac[0] - 12, .7, .5, 1.4)] + [('pluck', k * .5, [ac[0], ac[1], ac[2], ac[0] + 12, ac[2], ac[1]][k], .9, .9, .6) for k in range(6)]
        R['rit'] = [[(0, 1), (1, 1), (2, 1)], [(0, 2), (2, 1)]] * 8
    elif nome == '07':   # São Paulo · choro: cavaquinho, violão de 7, flauta, pandeiro
        R.update(bpm=92, comp=4, raiz=67, esc=MAIOR, prog=[0, 5, 1, 4, 0, 5, 1, 4, 3, 3, 0, 5, 1, 4, 4, 0], lead='sopro', semente=17)
        R['perc'] = lambda b: [('chocalho', k / 4, .55 if k % 4 in (0, 3) else .3) for k in range(16)] + [('tambor', 0, .35, 120), ('tambor', 2, .35, 120)]
        R['comp_'] = lambda b, ac: [('pluck', s, ac[0] - 12 + d, .6, .5, 1) for s, d in [(0, 0), (1, 7), (2, -5), (3, 2)]] + [('pluck', s, n + 12, .3, 1.0, .35) for s in (.5, 1.25, 2.5, 3.25) for n in ac[1:]]
        R['rit'] = [[(0, .5), (.5, .5), (1, .5), (1.5, .5), (2, 1), (3, 1)], [(0, 1), (1, .5), (1.5, .5), (2, 2)]] * 8
    elif nome == '08':   # Belo Horizonte · viola caipira em 6/8 (3 tempos pontuados)
        R.update(bpm=70, comp=3, raiz=64, esc=MAIOR, prog=[0, 3, 4, 0, 5, 3, 4, 4, 0, 3, 5, 1, 3, 4, 4, 0], lead='sopro', semente=18)
        R['perc'] = lambda b: []
        R['comp_'] = lambda b, ac: [x for k, n in enumerate([ac[0] - 12, ac[2], ac[1] + 12, ac[2] + 12, ac[1] + 12, ac[2]]) for x in [('pluck', k * .5, n, .6, .95, .9), ('pluck', k * .5 + .01, n + 12, .25, .95, .6)]] + [('pad', 0, ac, 3)]
        R['rit'] = [[(0, 1.5), (1.5, 1.5)], [(0, 1), (1, .5), (1.5, 1.5)]] * 8
    elif nome == '09':   # Rio · Feira de São Cristóvão · xote: sanfona, zabumba, triângulo
        R.update(bpm=88, comp=4, raiz=69, esc=MIXO, prog=[0, 0, 4, 4, 3, 3, 0, 4, 0, 3, 4, 0, 3, 3, 4, 0], lead='sanfona', semente=19)
        R['perc'] = lambda b: [('tambor', 0, .9, 75), ('tambor', 1.5, .5, 75), ('tambor', 2, .8, 75), ('tambor', 3, .5, 90)] + [('triangulo', k / 2, .6 if k % 2 else .35, k % 2 == 1) for k in range(8)]
        R['comp_'] = lambda b, ac: [('pluck', s, ac[0] - 12, .7, .45, 1.1) for s in (0, 2)] + [('sanf', s, ac, .28) for s in (1, 1.5, 3, 3.5)]
        R['rit'] = [[(0, 1), (1, .5), (1.5, .5), (2, 2)], [(0, .5), (.5, 1), (1.5, .5), (2, 1), (3, 1)]] * 8
    elif nome == '10':   # Porto Alegre · milonga: violão 3-3-2, gaita
        R.update(bpm=80, comp=4, raiz=64, esc=MENOR, prog=[0, 0, 4, 4, 3, 3, 4, 0, 5, 3, 4, 0, 3, 5, 4, 0], lead='sanfona', semente=20)
        R['perc'] = lambda b: []
        R['comp_'] = lambda b, ac: [('pluck', s, n, .55, .6, 1) for s, n in [(0, ac[0] - 12), (1.5, ac[0] - 12), (3, ac[2] - 12)]] + [('pluck', s, n, .4, .85, .6) for s in (.5, 2, 3.5) for n in ac]
        R['rit'] = [[(0, 1.5), (1.5, 1.5), (3, 1)], [(0, 2), (2, 1), (3, 1)]] * 8
    elif nome == '11':   # Florianópolis · valsa açoriana / ratoeira: rabeca, viola, tambor leve
        R.update(bpm=96, comp=3, raiz=60, esc=MAIOR, prog=[0, 4, 4, 0, 3, 0, 4, 0, 5, 3, 4, 0, 3, 0, 4, 0], lead='rabeca', semente=21)
        R['perc'] = lambda b: [('tambor', 0, .6, 100)]
        R['comp_'] = lambda b, ac: [('pluck', 0, ac[0] - 12, .7, .5, 1)] + [('pluck', s, n, .4, .85, .5) for s in (1, 2) for n in ac]
        R['rit'] = [[(0, 2), (2, 1)], [(0, 1), (1, 1), (2, 1)]] * 8
    elif nome == '12':   # Curitiba · polca suave: sanfona "um-pá", clarinete (sopro)
        R.update(bpm=104, comp=4, raiz=65, esc=MAIOR, prog=[0, 4, 4, 0, 0, 4, 4, 0, 3, 0, 4, 0, 3, 0, 4, 0], lead='sopro', semente=22)
        R['perc'] = lambda b: [('tambor', 0, .5, 70), ('chocalho', 1, .3), ('tambor', 2, .45, 70), ('chocalho', 3, .3)]
        R['comp_'] = lambda b, ac: [('pluck', 0, ac[0] - 12, .7, .45, 1), ('sanf', 1, ac, .3), ('pluck', 2, ac[2] - 24, .6, .45, 1), ('sanf', 3, ac, .3)]
        R['rit'] = [[(0, .5), (.5, .5), (1, 1), (2, 1), (3, 1)], [(0, 1.5), (1.5, .5), (2, 2)]] * 8
    return R

# ----------------------------------------------------------------- render
def render(nome):
    R = estilo(nome); B = 60 / R['bpm']; comp = R['comp']; nb = 16
    L = int(round(nb * comp * B * SR)); mix = np.zeros(L + SR * 4)
    def add(sig, t, g=1.0):
        i = int(round(t * SR)); j = i + len(sig)
        if i >= len(mix): return
        mix[i:min(j, len(mix))] += sig[:min(j, len(mix)) - i] * g
    raiz, esc = R['raiz'], R['esc']
    for b in range(nb):
        t0 = b * comp * B; ac = acorde(raiz - 12, esc, R['prog'][b])
        for ev in R['perc'](b):
            k, st = ev[0], ev[1]
            if k == 'tambor': add(tambor(ev[3], .5, ev[2]), t0 + st * B)
            elif k == 'chocalho': add(chocalho(v=ev[2]), t0 + st * B)
            elif k == 'agogo': add(agogo(ev[3] == 1, ev[2]), t0 + st * B)
            elif k == 'triangulo': add(triangulo(ev[3], ev[2]), t0 + st * B)
            elif k == 'palma': add(palma(ev[2]), t0 + st * B)
        for ev in R['comp_'](b, ac):
            k, st = ev[0], ev[1]
            if k == 'pluck': add(pluck(ev[2], 1.8, ev[4], ev[5]), t0 + st * B, ev[3])
            elif k == 'pad': add(pad([n + 12 for n in ev[2]], ev[3] * B), t0 + st * B)
            elif k == 'sanf': add(sum(sanfona(n + 12, .3 * B, ev[3]) for n in ev[2]), t0 + st * B)
    lead = R['lead']
    for b, st, du, m in melodia(raiz, esc, R['prog'], R['rit'], R['semente']):
        t, d = (b * comp + st) * B, du * B
        if lead == 'sopro': add(sopro(m, d * .95), t, .8)
        elif lead == 'rabeca': add(rabeca(m, d * .95), t, .7)
        elif lead == 'sanfona': add(sanfona(m, d * .95, 1.1), t)
        elif lead == 'sino': add(sino(m, max(d, 1.0)), t, 1.1)
        elif lead == 'harpa': add(pluck(m, max(d, 1.4), .95, .9), t, 1.0)
    # loop sem emenda: o que passa do fim volta para o começo
    loop = mix[:L].copy(); cauda = mix[L:]; loop[:len(cauda)] += cauda[:L]
    # reverberação circular (sala pequena), também sem emenda
    n = len(loop); ir_t = np.arange(int(1.4 * SR)) / SR
    ir = np.random.default_rng(5).standard_normal(len(ir_t)) * np.exp(-ir_t / .35); ir[0] = 0
    wet = np.fft.irfft(np.fft.rfft(loop) * np.fft.rfft(ir, n), n)
    out = loop + wet / np.abs(wet).max() * np.abs(loop).max() * .22
    # nível: todas as trilhas com a mesma intensidade média (RMS) e sem estourar
    out *= 10 ** (-24 / 20) / np.sqrt((out ** 2).mean())
    pk = np.abs(out).max()
    if pk > .85: out *= .85 / pk
    return out, R

if __name__ == '__main__':
    saida = sys.argv[1]; os.makedirs(saida, exist_ok=True)
    for nome in (sys.argv[2:] or [f'{k:02d}' for k in range(1, 13)]):
        x, R = render(nome)
        w = wave.open(os.path.join(saida, nome + '.wav'), 'wb'); w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
        w.writeframes((x * 32767).astype(np.int16).tobytes()); w.close()
        print(nome, f"{len(x) / SR:.1f} s", R['bpm'], 'bpm', R['comp'], 'tempos')
