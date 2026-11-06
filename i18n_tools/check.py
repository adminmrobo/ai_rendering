import sys, json, re, os
sys.path.insert(0, '/home/claude/i18n'); import merge
from ex import has_ko
TAGRE = re.compile(r'</?[a-zA-Z][^>]*>')
def nums(s, man=True):
    if man: s = re.sub(r'(\d+)만(?![가-힣])', lambda m: str(int(m.group(1)) * 10000), s)   # '4분의 1만 그리고'의 '만'(only)은 빼기
    s = re.sub(r'(?<=\d),(?=\d{3})', '', s)
    return sorted(re.findall(r'\d+(?:\.\d+)?', s))
def check(bundle, outfile, L):
    b = json.load(open(bundle)); errs = {}
    try:
        out = json.load(open(outfile))
    except Exception as e:
        txt = open(outfile).read(); out = {}
        for m in re.finditer(r'"(u\d{4})"\s*:\s*"((?:[^"\\]|\\.)*)"', txt):
            try: out[m.group(1)] = json.loads('"' + m.group(2) + '"')
            except Exception: pass
    ok = {}
    for u in b['units']:
        i = u['id']; t = out.get(i)
        if t is None: errs[i] = 'missing'; continue
        if has_ko(t) and not re.fullmatch(r'.*한국어.*', t): errs[i] = 'hangul'; continue
        if [re.sub(r'\s+', ' ', x) for x in TAGRE.findall(u['ko'])] != [re.sub(r'\s+', ' ', x) for x in TAGRE.findall(t)]: errs[i] = 'tags'; continue
        if L not in ('zh', 'ja') and u.get('hint'):
            if (u['ko'][:1] == ' ' and t[:1] != ' ') or (u['ko'][-1:] == ' ' and t[-1:] != ' '): errs[i] = 'space'; continue   # 공백을 잃으면 실패 (단위 앞 공백 추가는 허용)
        nt = nums(t); bad = None
        for nk in (nums(u['ko']), nums(u['ko'], False)):     # '만'을 수로 볼 때와 아닐 때 둘 중 하나만 맞으면 통과
            m2 = [x for x in nk if x not in nt and not any(abs(float(x) - float(y)) <= 0.01 * max(1, float(x)) for y in nt)]   # 1% 안 반올림 차이 허용
            m2 = [x for x in m2 if not (re.fullmatch(r'\d', x) or x == '10')]   # 1~10은 낱말로 쓸 수 있음
            if not m2: bad = None; break
            bad = m2
        if bad: errs[i] = 'num %s / %s' % (bad, nt); continue
        ok[i] = t
    return ok, errs
def absorb(bundle, ok, L):
    b = json.load(open(bundle)); tm = {}
    p = '/home/claude/i18n/tm/%s.json' % L
    if os.path.exists(p): tm = json.load(open(p))
    for u in b['units']:
        if u['id'] in ok: tm[u['ko'] + '\u0001' + ('' if '_f' in bundle else u.get('hint', ''))] = ok[u['id']]
    os.makedirs(os.path.dirname(p), exist_ok=True); json.dump(tm, open(p, 'w'), ensure_ascii=False)
    return len(tm)
if __name__ == '__main__':
    L, bundle, outfile = sys.argv[1:4]
    ok, errs = check(bundle, outfile, L)
    n = absorb(bundle, ok, L)
    if errs:
        b = json.load(open(bundle)); bad = [u for u in b['units'] if u['id'] in errs]
        rname = bundle.replace('.json', 'r.json'); json.dump({'lang': L, 'glossary': b['glossary'], 'units': bad}, open(rname, 'w'), ensure_ascii=False, indent=0)
        print(L, os.path.basename(bundle), 'ok', len(ok), 'fail', len(errs), 'retry->', os.path.basename(rname)); [print('  ', k, v) for k, v in list(errs.items())[:8]]
    else: print(L, os.path.basename(bundle), 'ok', len(ok), 'fail 0', 'tm', n)
