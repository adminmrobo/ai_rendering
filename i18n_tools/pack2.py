# 여러 페이지 묶음: 같은 한국어는 한 번만(문맥 예시는 최대 2개, 앞뒤 20자), 묶음 크기는 한국어+문맥 글자 수 기준
import sys, json, glob, os
sys.path.insert(0, '/home/claude/i18n'); import merge
G = json.load(open('/home/claude/i18n/glossary.json'))
def trim(h, ko):
    i = h.find(ko)
    return h[:40] if i < 0 else h[max(0, i - 20):i + len(ko) + 20]
def make(L, files, chars=25000):
    p = '/home/claude/i18n/tm/%s.json' % L
    tm = json.load(open(p)) if os.path.exists(p) else {}
    tmko = set(k.split('\u0001')[0] for k in tm)
    by = {}
    for f in files:
        for u in json.load(open(f))['units']:
            if u['ko'] in tmko: continue
            e = by.setdefault(u['ko'], {'ko': u['ko'], 'hints': []})
            if u.get('hint'):
                h = trim(u['hint'], u['ko'])
                if h not in e['hints'] and len(e['hints']) < 2: e['hints'].append(h)
    items = list(by.values()); bundles = []; cur = []; n = 0
    for e in items:
        sz = len(e['ko']) + sum(len(h) for h in e['hints'])
        if cur and n + sz > chars: bundles.append(cur); cur = []; n = 0
        cur.append(e); n += sz
    if cur: bundles.append(cur)
    out = []
    for bi, b in enumerate(bundles):
        txt = ' '.join(e['ko'] for e in b)
        units = []
        for j, e in enumerate(b):
            u = {'id': 'u%04d' % (j + 1), 'ko': e['ko']}
            if e['hints']: u['hint'] = ' … '.join(e['hints'])
            units.append(u)
        name = '/home/claude/i18n/bundles/%s_f%s%02d.json' % (L, os.environ.get('PFX', ''), bi + 1)
        json.dump({'lang': L, 'glossary': {k: v[L] for k, v in G.items() if k in txt}, 'units': units}, open(name, 'w'), ensure_ascii=False, indent=0)
        out.append((os.path.basename(name), len(units), sum(len(u['ko']) + len(u.get('hint', '')) for u in units)))
    return out
if __name__ == '__main__':
    files = sorted(glob.glob('/home/claude/i18n/units/*.json'))
    for L in sys.argv[1:]: print(L, make(L, files))
