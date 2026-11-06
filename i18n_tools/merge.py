import sys, json, re, os
sys.path.insert(0, '/home/claude/i18n'); from ex import has_ko
LANGS = ['en', 'zh', 'ja', 'ru', 'uz', 'vi']
NAMES = {'ko': '한국어', 'en': 'English', 'zh': '中文', 'ja': '日本語', 'ru': 'Русский', 'uz': 'Oʻzbekcha', 'vi': 'Tiếng Việt'}
def key(u): return u['ko'] + '\u0001' + u.get('hint', '')
def switcher(lang, fname, avail):
    links = []
    for L in ['ko'] + avail:
        if L == lang: links.append('<b>%s</b>' % NAMES[L]); continue
        if lang == 'ko': href = '%s/%s' % (L, fname)
        elif L == 'ko': href = '../%s?lang=ko' % fname
        else: href = '../%s/%s' % (L, fname)
        links.append('<a href="%s" hreflang="%s" lang="%s">%s</a>' % (href, L, L, NAMES[L]))
    js = ("<script>(function(){var L='%s',P=%s,f='%s';var q=null;try{q=new URLSearchParams(location.search).get('lang');}catch(e){}"
          "if(L==='ko'){var t=q;if(!t){var c=null;try{c=sessionStorage.getItem('langChosen');}catch(e){}if(!c)t=(navigator.language||'').slice(0,2).toLowerCase();}"
          "if(t&&P.indexOf(t)>=0){location.replace(t+'/'+f+location.hash);return;}}"
          "document.querySelectorAll('.langsw a').forEach(function(a){a.addEventListener('click',function(){try{sessionStorage.setItem('langChosen','1');}catch(e){}a.href=a.getAttribute('href').split('#')[0]+location.hash;});});})();</script>"
          ) % (lang, json.dumps(avail), fname)
    return ('<div class="langsw" style="max-width:1100px;margin:0 auto;padding:6px 16px;font-size:12.5px;display:flex;flex-wrap:wrap;gap:4px 12px;color:var(--muted)">'
            '<span aria-hidden="true">🌐</span>' + ' · '.join(links) + '</div>' + js)
def esc_js(t, q):
    t = t.replace('\\', '\\\\').replace('\n', '\\n').replace('\r', '')
    return t.replace(q, '\\' + q)
def build(units_file, lang, tm, out, avail, translated_pages):
    d = json.load(open(units_file)); html = open(d['src']).read()
    U = {u['id']: u for u in d['units']}
    def tr(uid):
        u = U[uid]; k = key(u)
        if k in tm: return tm[k]
        alt = [v for kk, v in tm.items() if kk.split('\u0001')[0] == u['ko'] and (kk.split('\u0001')[1] or not u.get('hint'))]
        if not alt: alt = [v for kk, v in tm.items() if kk.split('\u0001')[0] == u['ko']]
        if alt:   # 문맥(hint)만 바뀐 경우: 같은 원문의 번역 중 가장 많은 것 (조각이면 조각 번역을 먼저)
            import collections; return collections.Counter(alt).most_common(1)[0][0]
        raise KeyError(uid)
    # 1) 본문·스크립트 문자열 (뒤에서부터 바꿔 끼우기)
    for a, b, kind, uid in sorted(d['map'], key=lambda m: -m[0]):
        t = tr(uid)
        if kind.startswith('js'): t = esc_js(t, kind[2])
        elif kind == 'attr': t = t.replace('&', '&amp;').replace('&amp;amp;', '&amp;').replace('"', '&quot;')
        html = html[:a] + t + html[b:]
    # 2) 데이터 블록
    for bid in ('kg-raw', 'refs-csl', 'page-meta'):
        m = re.search(r'(<script type="application/json" id="%s">)(.*?)(</script>)' % bid, html, re.S)
        if not m: continue
        data = json.loads(m.group(2))
        for jb, path, uid in d['jmap']:
            if jb != bid: continue
            t = tr(uid); o = data
            for p in path[:-1]: o = o[p]
            last = path[-1]
            if bid == 'kg-raw' and 'ko' in path:
                ki = path.index('ko'); o2 = data
                for p in path[:ki]: o2 = o2[p]
                if isinstance(last, int):
                    o2.setdefault(lang, list(o2['ko'])); o2[lang][last] = t
                else: o2[lang] = t
            else: o[last] = t
        EX = json.load(open('/home/claude/i18n/extra.json'))
        def walk(o):   # 남은 짧은 한글 값(출처 위치, 저자 이름, 수준 등)은 extra.json 사전으로
            items = o.items() if isinstance(o, dict) else enumerate(o) if isinstance(o, list) else []
            for k, v in list(items):
                if k == 'ko': continue
                if isinstance(v, str) and v in EX: o[k] = EX[v][lang]
                elif isinstance(v, (dict, list)): walk(v)
        walk(data)
        s = json.dumps(data, ensure_ascii=False).replace('</', '<\\/')
        html = html[:m.start(2)] + s + html[m.end(2):]
    # 3) 지식 색인 화면: 그 언어 이름·정의를 먼저 (JSON-LD 내보내기는 그대로)
    html = re.sub(r"(byId\[[\w.]+\])\.label\.ko(?!,'@language')", r"(\1.label[LANG]||\1.label.en||\1.label.ko)", html)
    html = re.sub(r"n\.label\.ko(?!,'@language')", "(n.label[LANG]||n.label.en||n.label.ko)", html)
    html = re.sub(r"n\.definition\.ko(?!,'@language')", "(n.definition[LANG]||n.definition.ko)", html)
    html = html.replace("(n.definition&&(n.definition[LANG]||n.definition.ko))", "(n.definition&&(n.definition[LANG]||n.definition.ko))")
    # 내보내기(Turtle·CSV)의 한국어 칸은 한국어 그대로
    html = html.replace("esc((n.label[LANG]||n.label.en||n.label.ko))+'\"@ko", "esc(n.label.ko)+'\"@ko")
    html = html.replace("return [n.id,n.type,(n.label[LANG]||n.label.en||n.label.ko),n.label.en", "return [n.id,n.type,n.label.ko,n.label.en")
    DEED = {'en': 'en', 'zh': 'zh-hans', 'ja': 'ja', 'ru': 'ru', 'uz': 'en', 'vi': 'vi'}
    html = re.sub(r'(creativecommons\.org/licenses/by-nc/4\.0/deed\.)[a-z-]+', r'\g<1>' + DEED[lang], html)
    if lang == 'en': html = html.replace('<span class="small muted">\'+n.label.en+\'</span>', '')
    html = html.replace('<script>', "<script>var LANG='%s';" % lang, 1)
    # 4) 언어 표시, 링크 (번역 안 된 편은 한국어판으로)
    html = re.sub(r'<html lang="ko"', '<html lang="%s"' % lang, html, 1)
    def fix(m):
        h = m.group(1)
        if h.startswith(('http', '#', 'mailto', 'data:')) or not re.search(r'\.html', h): return m.group(0)
        base = h.split('#')[0].split('/')[-1]; anchor = h[len(h.split('#')[0]):]
        if not h.startswith('../') and base in translated_pages: return m.group(0)
        pm = re.match(r'\.\./(part\d)/([^#]+)', h)
        if pm and ('%s/%s' % (pm.group(1), pm.group(2)) in translated_pages or pm.group(2) in translated_pages):
            return 'href="../../%s/%s/%s%s"' % (pm.group(1), lang, pm.group(2), anchor)
        return 'href="../%s"' % h
    html = re.sub(r'href="([^"]+)"', fix, html)
    fname = os.path.basename(d['src'])
    html = html.replace('<body>', '<body>' + switcher(lang, fname, avail), 1)
    # 번역문은 한국어보다 길다: 요약 카드 큰 글씨가 좁은 화면에서 넘치지 않게
    html = html.replace('</head>', '<style>.kpi{min-width:0}.kpi b{overflow-wrap:anywhere;font-size:clamp(17px,5.6vw,24px)}</style></head>', 1)
    os.makedirs(os.path.dirname(out), exist_ok=True); open(out, 'w').write(html)
    # 보고: 화면 한글 남음
    vis = re.sub(r'<script[^>]*type="application/(?:ld\+)?json"[^>]*>.*?</script>|<pre[^>]*>.*?</pre>|<style.*?</style>', '', html, flags=re.S)
    vis = re.sub(r'/\*.*?\*/', '', vis, flags=re.S); vis = re.sub(r'(?m)//[^\n]*', '', vis)
    left = HANGS(vis)
    return left
def HANGS(s):
    import re as _r
    return [m.group(0) for m in _r.finditer(r'[^\s<>"\']*[\uac00-\ud7a3][^\s<>"\']*', s)][:20]
def ko_page(units_file, out, avail):
    d = json.load(open(units_file)); html = open(d['src']).read(); fname = os.path.basename(d['src'])
    html = html.replace('<body>', '<body>' + switcher('ko', fname, avail), 1); open(out, 'w').write(html)
