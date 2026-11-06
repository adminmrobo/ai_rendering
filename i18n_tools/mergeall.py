# mergeall.py OUT_DIR L1,L2,...  → OUT/partN/{L}/이름.html (+ 한국어판 OUT/partN/이름.html, 언어 선택 막대 포함)
import sys, json, os, glob
sys.path.insert(0, '/home/claude/i18n'); import merge
out, langs = sys.argv[1], sys.argv[2].split(',')
units = sorted(glob.glob('/home/claude/i18n/units/part*.json'))
pages = set(os.path.basename(json.load(open(u))['src']) for u in units)
bad = 0
for L in langs:
    tm = json.load(open('/home/claude/i18n/tm/%s.json' % L))
    for u in units:
        d = json.load(open(u)); part = d['src'].split('/')[-2]; f = os.path.basename(d['src'])
        try:
            left = merge.build(u, L, tm, '%s/%s/%s/%s' % (out, part, L, f), langs, pages)
        except KeyError as e:
            print(L, part, f, 'MISSING', e); bad += 1; continue
        left = [x for x in left if x != '한국어' and '가-힣' not in x]
        if left: print(L, part, f, 'HANGUL', left[:5]); bad += 1
for u in units:
    d = json.load(open(u)); part = d['src'].split('/')[-2]; f = os.path.basename(d['src'])
    os.makedirs('%s/%s' % (out, part), exist_ok=True)
    merge.ko_page(u, '%s/%s/%s' % (out, part, f), langs)
print('done', langs, 'problems', bad)
