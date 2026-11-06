import sys, json, re, hashlib
sys.path.insert(0, '/home/claude/i18n'); from ex import *
src = sys.argv[1]; html = open(src).read()
spans, raw = scan(html); ju = json_units(html, raw)
units = {}; order = []
def add(text, ctx, kind):
    key = text + '\u0001' + (ctx if kind == 'jsfrag' else '')
    if key not in units:
        uid = 'u%04d' % (len(units) + 1); units[key] = {'id': uid, 'ko': text}
        if ctx: units[key]['hint'] = ctx
        order.append(key)
    return units[key]['id']
mp = []
for a, b, k, ctx in spans:
    t = html[a:b]
    if k.startswith('js'):
        # 자바스크립트 이스케이프 풀기 (\' \" \\ \n)
        t2 = t.encode('utf-8').decode('unicode_escape').encode('latin-1').decode('utf-8') if '\\' in t else t
        uid = add(t2, ctx, 'jsfrag' if ctx else 'js')
    else:
        uid = add(t, '', k)
    mp.append([a, b, k, uid])
jm = []
for bid, path, t in ju:
    jm.append([bid, path, add(t, '', 'json')])
json.dump({'src': src, 'map': mp, 'jmap': jm, 'units': [units[k] for k in order]}, open(sys.argv[2], 'w'), ensure_ascii=False, indent=0)
n = sum(len(units[k]['ko']) for k in order)
print('spans', len(mp), 'json', len(jm), 'units', len(order), 'chars', n)
