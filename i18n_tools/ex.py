# 추출·조립 도구 (AI 렌더링 연구실용, 언어팩 VER1.0 흐름을 따름)
import re, json, sys
HANG = re.compile(r'[가-힣]')
def has_ko(s): return bool(HANG.search(s))
INLINE = set('a b i em strong sup sub span code small u mark abbr kbd s q br img wbr label'.split())
VOID = set('area base br col embed hr img input link meta source track wbr'.split())
TAG = re.compile(r'<(/?)([a-zA-Z][a-zA-Z0-9-]*)((?:[^>"\']|"[^"]*"|\'[^\']*\')*)>|<!--.*?-->', re.S)
ATTR = re.compile(r'(\s)(alt|aria-label|title|placeholder|content)=("([^"]*)"|\'([^\']*)\')')

def js_strings(code, base):
    """자바스크립트 안의 문자열 리터럴 위치 (주석·정규식 건너뜀). 반환: (시작, 끝, 따옴표) — 따옴표 안쪽 범위"""
    out = []; i = 0; n = len(code); prev = ''
    while i < n:
        c = code[i]
        if c in ' \t\r\n': i += 1; continue
        if code.startswith('//', i):
            j = code.find('\n', i); i = n if j < 0 else j; continue
        if code.startswith('/*', i):
            j = code.find('*/', i + 2); i = n if j < 0 else j + 2; continue
        if c in '\'"`':
            j = i + 1
            while j < n and code[j] != c:
                if code[j] == '\\': j += 2; continue
                if c == '`' and code.startswith('${', j):  # 템플릿 식은 이 시리즈에서 쓰지 않음
                    raise ValueError('template expr at %d' % (base + j))
                j += 1
            out.append((base + i + 1, base + j, c)); i = j + 1; prev = 'str'; continue
        if c == '/' and (prev in ('', 'op') ):
            j = i + 1; cls = False
            while j < n:
                if code[j] == '\\': j += 2; continue
                if code[j] == '[': cls = True
                elif code[j] == ']': cls = False
                elif code[j] == '/' and not cls: break
                elif code[j] == '\n': break
                j += 1
            i = j + 1
            while i < n and code[i].isalpha(): i += 1
            prev = 'val'; continue
        if c.isalnum() or c in '_$':
            j = i
            while j < n and (code[j].isalnum() or code[j] in '_$.'): j += 1
            w = code[i:j]; i = j
            prev = 'op' if w in ('return', 'typeof', 'case', 'in', 'of', 'new', 'delete', 'void', 'else', 'do') else 'val'; continue
        prev = 'val' if c in ')]}' else 'op'
        i += 1
    return out

def scan(html):
    """번역 단위 위치 목록: (시작, 끝, 종류, 문맥)"""
    spans = []
    # 1) 스크립트·스타일·pre 범위
    raw = []
    for m in re.finditer(r'<(script|style|pre)\b([^>]*)>', html):
        e = html.index('</%s>' % m.group(1), m.end()); raw.append((m.start(), e, m.group(1), m.group(2), m.end()))
    def in_raw(p): return any(a <= p < b for a, b, *_ in raw)
    # 2) 스크립트 문자열
    for a, b, t, at, s0 in raw:
        if t != 'script' or 'type=' in at: continue
        code = html[s0:b]
        for x, y, q in js_strings(code, s0):
            v = html[x:y]
            if has_ko(v):
                # 문맥: 짧은 조각이거나 공백으로 시작·끝나면 앞뒤 40자
                hint = html[max(s0, x - 41):min(b, y + 41)] if (len(v) < 20 or v != v.strip()) else ''
                spans.append((x, y, 'js' + q, hint))
    # 3) HTML 본문: 블록 경계 사이의 인라인 묶음
    masked = list(html)
    for a, b, t, at, s0 in raw:
        for k in range(s0, b): masked[k] = ' ' if masked[k] != '\n' else '\n'
    masked = ''.join(masked)
    stack = []; run = None
    def close_run(end):
        nonlocal run
        if run is not None:
            s, toks = run
            seg = html[s:end]
            if has_ko(re.sub(r'<[^>]+>', '', seg)): spans.append((s, end, 'html', ''))
        run = None
    pos = 0
    for m in TAG.finditer(masked):
        text = masked[pos:m.start()]
        if text.strip():
            if run is None: run = (pos + (len(text) - len(text.lstrip())), [])
        if m.group(0).startswith('<!--'):
            pos = m.end(); continue
        closing, name = m.group(1), m.group(2).lower()
        if name in INLINE:
            if run is None and not closing: run = (m.start(), [])
        else:
            if run is not None:
                end = m.start()
                # 끝 공백 잘라내기
                while end > run[0] and html[end - 1] in ' \t\r\n': end -= 1
                close_run(end)
        # 속성
        for am in ATTR.finditer(m.group(0)):
            val = am.group(4) if am.group(4) is not None else am.group(5)
            if val and has_ko(val):
                off = m.start() + am.start(3) + 1
                spans.append((off, off + len(val), 'attr', am.group(2)))
        pos = m.end()
    # 인라인 묶음의 태그 균형 확인 → 깨지면 텍스트 조각 단위로
    fixed = []
    for s in spans:
        if s[2] == 'html':
            seg = html[s[0]:s[1]]; st = []
            ok = True
            for tm in TAG.finditer(seg):
                if tm.group(0).startswith('<!--'): continue
                nm = tm.group(2).lower()
                if nm in VOID: continue
                if tm.group(1): 
                    if not st or st[-1] != nm: ok = False; break
                    st.pop()
                else: st.append(nm)
            # 앞뒤가 태그로 시작해 끝나는 경우 그대로, 균형 아니면 텍스트 조각으로 쪼갬
            if not ok or st:
                for tm in re.finditer(r'[^<>]+', seg):
                    t = tm.group(0)
                    if has_ko(t):
                        a = s[0] + tm.start() + (len(t) - len(t.lstrip())); b = s[0] + tm.end() - (len(t) - len(t.rstrip()))
                        fixed.append((a, b, 'html', 'frag'))
                continue
        fixed.append(s)
    fixed.sort()
    # 겹침 검사 (속성 단위가 html 묶음 안에 있으면 묶음이 이긴다: 속성은 태그 안이라 묶음 텍스트에 함께 들어감)
    out = []
    for s in fixed:
        if out and s[0] < out[-1][1]:
            continue
        out.append(s)
    return out, raw

def json_units(html, raw):
    """데이터 블록 중 화면에 나오는 한국어: kg-raw 이름·정의·다른 이름, refs-csl의 쓰인 곳·위치·메모, page-meta 제목·시리즈"""
    units = []
    for a, b, t, at, s0 in raw:
        idm = re.search(r'id="([^"]+)"', at)
        if t != 'script' or not idm: continue
        bid = idm.group(1)
        if bid not in ('kg-raw', 'refs-csl', 'page-meta'): continue
        data = json.loads(html[s0:b])
        def walk(o, path):
            if isinstance(o, dict):
                for k, v in o.items(): walk(v, path + [k])
            elif isinstance(o, list):
                for i, v in enumerate(o): walk(v, path + [i])
            elif isinstance(o, str) and has_ko(o):
                keep = False
                if bid == 'kg-raw': keep = ('ko' in path and ('label' in path or 'definition' in path or 'altLabel' in path)) or 'topicLabels' in path
                if bid == 'refs-csl': keep = path[-1] in ('usedIn', 'loc', 'note', 'checkedBy')
                if bid == 'page-meta': keep = path[-1] in ('title', 'series', 'suggestedCitation', 'description')
                if keep: units.append((bid, path, o))
        walk(data, [])
    return units
