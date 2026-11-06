import sys, json, re, os
sys.path.insert(0, '/home/claude/i18n'); import merge
G = json.load(open('/home/claude/i18n/glossary.json'))
def tmfile(L): return '/home/claude/i18n/tm/%s.json' % L
def load_tm(L):
    return json.load(open(tmfile(L))) if os.path.exists(tmfile(L)) else {}
def pending(units_files, L, chars=10000, tag=''):
    tm = load_tm(L); seen = set(); todo = []
    for uf in units_files:
        for u in json.load(open(uf))['units']:
            k = merge.key(u)
            if k in tm or k in seen: continue
            seen.add(k); todo.append(u)
    bundles = []; cur = []; n = 0
    for u in todo:
        if cur and n + len(u['ko']) > chars: bundles.append(cur); cur = []; n = 0
        cur.append(u); n += len(u['ko'])
    if cur: bundles.append(cur)
    names = []
    for i, b in enumerate(bundles):
        txt = ' '.join(u['ko'] for u in b)
        gl = {k: v[L] for k, v in G.items() if k in txt}
        name = '/home/claude/i18n/bundles/%s_%s%03d.json' % (L, tag, i + 1)
        json.dump({'lang': L, 'glossary': gl, 'units': [dict(id=u['id'], ko=u['ko'], **({'hint': u['hint']} if u.get('hint') else {})) for u in b]}, open(name, 'w'), ensure_ascii=False, indent=0)
        names.append((name, len(b), sum(len(u['ko']) for u in b)))
    return names
if __name__ == '__main__':
    L = sys.argv[1]; print(pending(sys.argv[2:], L, 11000))
