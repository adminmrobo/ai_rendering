# vt3.py SITE W — 가벼운 검사: 모든 언어·모든 쪽을 열어 스크립트 오류, 가로 넘침, 표지 그림 표시만 본다
import asyncio, sys, glob, os
from playwright.async_api import async_playwright
SITE, W = sys.argv[1], int(sys.argv[2])
pages = sorted(glob.glob(SITE + '/part*/*.html') + glob.glob(SITE + '/part*/*/*.html'))
skip = set(l.split()[2] for l in open(sys.argv[3]) if l.startswith('OK ')) if len(sys.argv) > 3 else set()
pages = [f for f in pages if os.path.relpath(f, SITE) not in skip]
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path='/usr/bin/google-chrome', args=['--no-sandbox'])
        sem = asyncio.Semaphore(3)
        async def one(f):
            async with sem:
                ctx = await b.new_context(viewport={'width': W, 'height': 900}); pg = await ctx.new_page(); errs = []
                pg.on('pageerror', lambda e: errs.append(str(e)[:100]))
                await pg.goto('file://' + f + '?lang=ko'); await pg.wait_for_timeout(1500)
                r = await pg.evaluate("()=>{var i=document.querySelector('#cover img');var c=document.querySelector('#cover');return [document.documentElement.scrollWidth, i?i.naturalWidth:-1, c?Math.round(c.getBoundingClientRect().width):-1]}")
                await ctx.close()
                ok = not errs and r[0] <= W + 1 and r[1] > 0 and r[2] >= W - 1
                print('OK' if ok else 'XX', W, os.path.relpath(f, SITE), r, errs[:2], flush=True)
        await asyncio.gather(*[one(f) for f in pages])
        await b.close()
asyncio.run(main())
