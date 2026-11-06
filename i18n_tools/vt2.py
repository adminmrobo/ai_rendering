# vt2.py SITE L W  → 모든 편: 스크립트 오류, 가로 넘침, 화면에 남은 한글, 버튼 눌러 본 뒤 오류
import asyncio, sys, glob, re, os
from playwright.async_api import async_playwright
SITE, L, W = sys.argv[1], sys.argv[2], int(sys.argv[3])
pages = sorted(glob.glob('%s/part*/%s/*.html' % (SITE, L)))
HAN = re.compile(r'[가-힣]+')
async def one(b, f):
    pg = await b.new_page(viewport={'width': W, 'height': 900}); errs = []
    pg.on('pageerror', lambda e: errs.append(str(e)[:120]))
    await pg.goto('file://' + f); await pg.wait_for_timeout(1200)
    h = await pg.evaluate('document.body.scrollHeight')
    for y in range(0, h, 700):
        await pg.evaluate('window.scrollTo(0,%d)' % y); await pg.wait_for_timeout(120)
    # 버튼 몇 개 눌러 보기 (링크·언어 막대 제외)
    n = await pg.evaluate("""()=>{var bs=[...document.querySelectorAll('button')].filter(b=>!b.closest('.langsw')&&b.offsetParent);
      var k=0;bs.slice(0,40).forEach(b=>{try{b.click();k++;}catch(e){}});return k;}""")
    await pg.wait_for_timeout(2500)
    sw = await pg.evaluate('document.documentElement.scrollWidth')
    txt = await pg.evaluate("(function(){var c=document.body.cloneNode(true);c.querySelectorAll('pre,.langsw').forEach(function(e){e.remove();});document.body.appendChild(c);c.style.position='absolute';var t=c.innerText;c.remove();return t;})()")
    han = sorted(set(HAN.findall(txt)))[:8]
    await pg.close()
    flag = 'OK' if (not errs and sw <= W + 1 and not han) else 'XX'
    print(flag, L, W, os.path.relpath(f, SITE), 'btn', n, 'sw', sw, 'errs', errs[:3], 'han', han, flush=True)
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path='/usr/bin/google-chrome', args=['--no-sandbox'])
        for f in pages: await one(b, f)
        await b.close()
asyncio.run(main())
