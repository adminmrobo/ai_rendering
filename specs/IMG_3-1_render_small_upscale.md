# 3-1번 「작게 그리고 크게」 이미지 제작 명세서

| 항목 | 내용 |
|---|---|
| 페이지 | 3-1_render_small_upscale.html (3부 목차 index.html 포함) |
| 모드 / 주 앵커 | 교과서 / D 생활·현장: 게임 화면, 사진 확대 |
| 시즌 | 기본 |
| 대결 | 처음 보는 화면 4장을 ×2로 키우기 → 결과 R (주판봇 승), 차이 1.12 dB (쌍선형 22.54 vs 배운 업스케일러 23.65), 큰 차이 아님 → fly_coffee |
| 새로 그릴 그림 | P1 2장 (cover_ch3, cover_3-1) · P2 1장 (sc_3-1_outro) |
| 재사용 | 표정 16장 — 캐릭터 팩 ea5da3f |
| 그림이 없을 때 | 표지·아웃트로는 페이지가 직접 렌더링한 테트리스 화면 + 팩 캐릭터로 완성 상태 |

## 1. 필요한 그림

| # | 키 | 판 | 상태 | 우선 | 들어가는 곳 | 대신 쓰는 그림 |
|---|---|---|---|---|---|---|
| 0 | cover_ch3 | L 1920×1080 | 새로 (COVER_ch3 지시문) | P1 | 3부 목차 큰 표지 | 캔버스 (작은 화면 → AI 상자 → 큰 화면) |
| 1 | cover_3-1 | L 1920×1080 | 새로 (COVER_3-1 지시문) | P1 | 3-1 첫 화면 (16:7) | 캔버스 (32×32 → 96×96) |
| 2 | sc_3-1_outro | E 1200×800 | 새로 | P2 | 아웃트로 | 캔버스 (쌍선형·배운 업스케일러·정답 세 화면) |
| 3 | doc_think · doc_front · doc_magic · doc_judge | A | 재사용 | — | 히어로, 등장인물, 아웃트로, 판정 | — |
| 4 | asst_smile · asst_firm · asst_ledger | B | 재사용 | — | 히어로, ①칸, 발표, 꾸러미 | — |
| 5 | fly_point · fly_clip · fly_coffee | C | 재사용 | — | 히어로, ②칸, 대결 후, 아웃트로 | — |
| 6 | robo_coin · robo_smile · robo_calc · robo_happy | D | 재사용 | — | 히어로, ③칸, 대결 후, 아웃트로 | — |

## 2. 새로 그릴 그림 상세 — `sc_3-1_outro`
| 항목 | 내용 |
|---|---|
| 구도 | 가운데 위에 모니터 세 대(흐린 화면, 조금 더 선명한 화면, 가장 선명한 정답 화면). 주판봇이 오른쪽 앞에서 두 팔을 듦(이김). 초파리는 왼쪽 앞에서 커피 잔을 들고 고개를 끄덕임(작은 차이로 짐, 인정). 박사는 가운데 뒤에서 두 손에 보랏빛 불꽃, 조수는 옆에서 미소 |
| 표정 | robo_happy, fly_coffee, doc_magic, asst_smile |
| 피할 것 | 화면 속 글자·숫자, 승자가 패자를 놀리는 몸짓 |
| 대체 글 (alt) | 쌍선형으로 키운 화면, 배운 업스케일러로 키운 화면, 정답 화면 세 개 앞에서 주판봇이 두 팔을 들고, 초파리 연구원이 커피를 들고 고개를 끄덕이는 연구실 장면 |

**프롬프트 (복사해서 사용)**
```
16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights, consistent with the reference images, cozy night laboratory mood, purple light, soft magenta and green fluorescent accents, 3:2 landscape scene, medium brightness, three monitors in a row in the upper center showing the same Tetris-like game screen: the left one slightly blurry, the middle one sharper, the right one the sharpest, blocks with one color per shape (cyan straight, yellow square, purple T, orange L), small boxy retro computer robot with a beige rounded-corner CRT-monitor head, a dark green screen face with mint pixel eyes and mouth, a thin antenna topped with one small red-brown abacus bead, chunky gray segmented arms with round gray mitten hands and two dark gray tank treads, about three quarters the height of the scientist, in the front right facing left raising both arms happily, anthropomorphic fruit fly researcher with a black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat and transparent wings in the front left facing right holding a coffee cup and nodding, accepting a narrow loss, chibi scientist with round glasses, black hair with one white streak, white lab coat over black vest and tie at the back center with purple sparks in both hands, girl researcher with pink hair in two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie smiling at the side, no white glossy round robot head, no black pill-shaped visor, no yellow eyes, no ball-shaped antenna knob, no cyan chest light, no floating robot, no gold coins, no text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands
```

## 3. 체크리스트
- [x] HTML의 `data-img` 키 16개가 1장 표에 있음
- [x] 대결 R, 차이 1.12 dB (큰 차이 기준 1.5 dB 미만) → fly_coffee, robo_happy, asst_spark, doc_judge
- [x] 결과 전 그림(표지, 히어로)에 승패 암시 없음, 그림 안 글자 없음
- [x] 화면 속 블록 색은 1부와 같은 규칙 (같은 모양 같은 색)

## 4. 매니페스트
```json
{"page":"3-1_render_small_upscale","anchor":"D:game-screen","season":"default","duel":{"result":"R","gap":1.12,"metric":"PSNR dB"},
 "images":[
  {"key":"cover_ch3","plate":"L","size":[1920,1080],"status":"new","priority":"P1","slot":"cover (part3/index)","fallback":"canvas","alt":"밤의 연구실, 거칠게 작게 그린 게임 화면이 AI를 거쳐 선명하고 매끄러운 큰 화면으로 바뀌는 앞에 네 캐릭터가 선 3부 표지"},
  {"key":"cover_3-1","plate":"L","size":[1920,1080],"status":"new","priority":"P1","slot":"cover-tall 16:7","fallback":"canvas","alt":"밤의 연구실 큰 모니터 두 대. 왼쪽은 거칠게 작게 그린 테트리스 화면, 오른쪽은 선명한 큰 화면이고, 네 캐릭터가 그 사이에서 AI가 채우는 장면을 지켜보는 3-1편 표지"},
  {"key":"sc_3-1_outro","plate":"E","size":[1200,800],"status":"new","priority":"P2","slot":"outro","fallback":"canvas","alt":"쌍선형으로 키운 화면, 배운 업스케일러로 키운 화면, 정답 화면 세 개 앞에서 주판봇이 두 팔을 들고, 초파리 연구원이 커피를 들고 고개를 끄덕이는 연구실 장면"}
 ]}
```

## 5. 받은 그림 (2026-11-01, 저자 제공) — 실험 재료
- `lab_bench_01`, `block_wall_02`, `bookshelf_03`, `rooftop_04` (학습), `desk_05`, `greenhouse_06` (시험) — 1024×1024 일러스트 6장. 320×320 WebP로 줄여 페이지 안에 포함(`art31.js`), 원본은 `specs/assets/`.
- ①②③칸의 "장면" 버튼으로 테트리스 ↔ 그림 6장을 바꾼다. 학습 4장의 네 귀퉁이 중 셋씩(12조각), 시험 2장의 왼쪽 위·오른쪽 아래(4조각).
- 결과: ×2에서 쌍선형 23.32 dB vs 배운 업스케일러 22.92 dB로 테트리스(22.54 vs 23.65)와 반대. 본문과 대결 주석에 그대로 적음. 대결 판정은 테트리스 기준.
