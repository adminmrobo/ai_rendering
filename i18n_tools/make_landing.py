# make_landing.py TRILOGY_DIR — 3부작 첫 화면 index.html (한국어 + 6개 언어)를 각 부 목차에서 글을 가져와 만든다
import re, json, sys, html, os
sys.path.insert(0, '/home/claude/i18n'); from merge import switcher
T = sys.argv[1]; LANGS = ['en', 'zh', 'ja', 'ru', 'uz', 'vi']
UI = {
 'ko': ('3부작', '정답표 없이 배우기에서 시작해 사진에서 3D를 되찾고, 적게 그린 화면을 AI로 채우기까지 — 미션 15개.', '목차 보기'),
 'en': ('Trilogy', 'From learning without an answer key, to recovering 3D from photos, to drawing less and letting AI fill in the rest — 15 missions.', 'Open contents'),
 'zh': ('三部曲', '从没有答案也能学，到从照片找回3D，再到少画一点、让AI补全——共15个任务。', '查看目录'),
 'ja': ('三部作', '正解表なしで学ぶことから、写真から3Dを取り戻し、少なく描いてAIで補うまで——ミッションは全15個です。', '目次を見る'),
 'ru': ('Трилогия', 'От обучения без ключа ответов к восстановлению 3D по фотографиям и к рендерингу «меньше рисуем — остальное дорисует ИИ» — 15 миссий.', 'Открыть оглавление'),
 'uz': ('Trilogiya', 'Javoblar kalitisiz oʻrganishdan rasmlardan 3D ni tiklashgacha, kamroq chizib qolganini AI ga toʻldirtirishgacha — 15 ta missiya.', 'Mundarijani ochish'),
 'vi': ('Bộ ba phần', 'Từ học không cần đáp án, đến khôi phục 3D từ ảnh, rồi vẽ ít hơn và để AI lấp đầy phần còn lại — 15 nhiệm vụ.', 'Xem mục lục'),
}
COL = ['#5ee39c', '#82b8ff', '#e48cff']
import base64
ASSET = os.path.join(T, 'specs/assets/landing')
def du(f): return 'data:image/webp;base64,' + base64.b64encode(open(os.path.join(ASSET, f), 'rb').read()).decode()
ALT = {
 'ko': '밤의 연구실, 테트리스 블록과 주머니, 사진 고리 속에서 떠오르는 3D 머그컵, 거친 화면과 선명한 화면의 모니터 두 대 사이에 네 캐릭터가 선 3부작 대표 그림',
 'en': 'A night lab: Tetris blocks and pouches, a 3D mug rising inside a ring of photos, and two monitors going from blocky to sharp, with the four characters standing among them',
 'zh': '夜晚的研究室：俄罗斯方块和布袋、在照片环中浮起的3D马克杯、从粗糙到清晰的两台显示器，四个角色站在其间的三部曲主图',
 'ja': '夜の研究室。テトリスのブロックと袋、写真の輪の中に浮かぶ3Dのマグカップ、粗い画面と鮮明な画面のモニター2台のあいだに4人のキャラクターが立つ三部作のメイン画像です',
 'ru': 'Ночная лаборатория: блоки тетриса и мешочки, 3D-кружка, поднимающаяся в кольце фотографий, и два монитора — грубый и чёткий экран; между ними стоят четыре персонажа',
 'uz': 'Tungi laboratoriya: tetris bloklari va xaltachalar, rasmlar halqasi ichida koʻtarilayotgan 3D krujka, qoʻpol va aniq ekranli ikki monitor, ular orasida toʻrt qahramon turibdi',
 'vi': 'Phòng thí nghiệm ban đêm: khối Tetris và túi vải, chiếc cốc 3D nổi lên giữa vòng ảnh, hai màn hình từ thô đến sắc nét, bốn nhân vật đứng giữa chúng',
}
HERO_IMG = None
def page(L):
    sub = '' if L == 'ko' else L + '/'
    up = '' if L == 'ko' else '../'
    def rd(p): return open(os.path.join(T, p)).read()
    ch = rd('part2/%s2-1_why_photos_are_flat.html' % sub)
    series = json.loads(re.search(r'id="page-meta">(.*?)</script>', ch, re.S).group(1))['series'].split(' · ')[0]
    parts = []
    byline = None
    for n in (1, 2, 3):
        s = rd('part%d/%sindex.html' % (n, sub))
        title = re.search(r'<title>(.*?)</title>', s).group(1)
        ptitle = title.split(' — ', 1)[1].split(' | ')[0] if ' — ' in title else title
        h1 = re.search(r'<h1>(.*?)</h1>', s, re.S).group(1)
        q = re.search(r'<p class="question">(.*?)</p>', s, re.S).group(1)
        byline = byline or re.search(r'<p class="byline">(.*?)</p>', s).group(1)
        cards = []
        for c in re.findall(r'<div class="mcard">(.*?)</div></div>', s, re.S):
            href = re.search(r'href="([^"]+)"', c).group(1); h3 = re.search(r'<h3>(.*?)</h3>', c).group(1); h3 = h3[:1].upper() + h3[1:]
            num = re.match(r'(\d-\d)', href).group(1)
            cards.append('<li><a href="%spart%d/%s%s"><b>%s</b> %s</a></li>' % (up, n, sub, href, num, h3))
        parts.append((n, ptitle, h1, q, cards))
    lab, tag, btn = UI[L]
    global HERO_IMG
    if HERO_IMG is None: HERO_IMG = (du('cover_landing_wide.webp'),)
    hero = ('<figure class="hero-art"><img src="%s" width="1280" height="720" alt="%s"></figure>') % (HERO_IMG[0], html.escape(ALT[L]))
    secs = ''.join(
        '<section class="part" style="--c:%s"><p class="pn">%s</p><h2><a href="%spart%d/%sindex.html">%s</a></h2><p class="q">%s</p><ol>%s</ol>'
        '<p class="go"><a href="%spart%d/%sindex.html">▶ %s</a></p></section>' % (COL[n-1], ptitle, up, n, sub, h1, q, ''.join(cards), up, n, sub, btn)
        for n, ptitle, h1, q, cards in parts)
    deed = {'ko': 'ko', 'en': 'en', 'zh': 'zh-hans', 'ja': 'ja', 'ru': 'ru', 'uz': 'en', 'vi': 'vi'}[L]
    doc = '''<!doctype html>
<html lang="%s"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>%s — %s</title><meta name="description" content="%s">
<style>
:root{--bg:#13141f;--panel:#1c1e2d;--rule:#363a52;--text:#eceaf3;--muted:#9d9bb8;--accent:#e48cff;color-scheme:dark}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--text);font:16px/1.6 "IBM Plex Sans KR",system-ui,-apple-system,"Segoe UI",sans-serif}
a{color:inherit}.wrap{max-width:1100px;margin:0 auto;padding:0 16px}
header{padding:56px 0 28px;background:radial-gradient(120%% 90%% at 20%% 0%%,#2a1f4a 0,#13141f 70%%)}
.kick{color:var(--accent);font-size:13px;letter-spacing:.08em;text-transform:uppercase;margin:0 0 8px}
h1{font-size:clamp(28px,5vw,46px);line-height:1.15;margin:0 0 12px}.tag{color:var(--muted);max-width:720px;margin:0 0 10px}.by{font-size:14px;color:var(--muted);margin:0}
.parts{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:16px;padding:28px 0 40px}
.part{background:var(--panel);border:1px solid var(--rule);border-top:3px solid var(--c);border-radius:14px;padding:18px 18px 14px;min-width:0}
.pn{color:var(--c);font-size:13px;font-weight:600;margin:0 0 6px}.part h2{font-size:20px;line-height:1.3;margin:0 0 8px}.part h2 a{text-decoration:none}.part h2 a:hover{text-decoration:underline}
.q{color:var(--muted);font-size:14px;margin:0 0 12px}ol{list-style:none;padding:0;margin:0 0 12px;border-top:1px solid var(--rule)}
li a{display:block;padding:8px 2px;border-bottom:1px solid var(--rule);text-decoration:none;font-size:15px;overflow-wrap:anywhere}li a:hover{background:#25283a}li b{color:var(--c);font-variant-numeric:tabular-nums;margin-right:6px}
.go{margin:0}.go a{display:inline-block;padding:7px 14px;border-radius:999px;background:var(--c);color:#13141f;font-weight:600;text-decoration:none;font-size:14px}
.hero-art{margin:0;background:#0f1a1c}.hero-art img{display:block;width:100%%;height:auto;max-height:78vh;object-fit:cover;object-position:50%% 50%%}
header{padding-top:28px}
footer{border-top:1px solid var(--rule);padding:18px 0 28px;color:var(--muted);font-size:13px}
</style></head><body>
%s<header><div class="wrap"><p class="kick">%s</p><h1>%s</h1><p class="tag">%s</p><p class="by">%s</p></div></header>
<main class="wrap"><div class="parts">%s</div></main>
<footer><div class="wrap">%s · <a href="https://creativecommons.org/licenses/by-nc/4.0/deed.%s">CC BY-NC 4.0</a></div></footer>
</body></html>
''' % (L, html.escape(series), lab, html.escape(tag), hero, lab, series, tag, byline, secs, byline, deed)
    doc = doc.replace('<body>', '<body>' + switcher(L, 'index.html', LANGS), 1)
    out = os.path.join(T, sub, 'index.html'); os.makedirs(os.path.dirname(out), exist_ok=True); open(out, 'w').write(doc)
    return out
for L in ['ko'] + LANGS: print(page(L))
