# 3-3번 「사이 프레임」 이미지 제작 명세서

| 항목 | 내용 |
|---|---|
| 페이지 | 3-3_frame_generation.html |
| 모드 / 주 앵커 | 교과서 / D 생활·현장: 그림책 애니메이션, 무대 조명, 영상 통화 |
| 시즌 | 기본 |
| 대결 | 모션 벡터 vs 광학 흐름, 두 판 → 결과 D (무승부, 1판씩). 블록 판 23.62 vs 21.80, 불꽃 판 18.09 vs 22.43 dB |
| 새로 그릴 그림 | P1 1장 (cover_3-3) · P2 1장 (sc_3-3_outro) |
| 재사용 | 표정 16장 — 캐릭터 팩 ea5da3f (doc_scale은 팩에 없어 가장 가까운 표정으로 대체 중) |
| 그림이 없을 때 | 표지·아웃트로는 페이지가 직접 렌더링한 장면 + 팩 캐릭터로 완성 상태 |

## 1. 필요한 그림

| # | 키 | 판 | 상태 | 우선 | 들어가는 곳 | 대신 쓰는 그림 |
|---|---|---|---|---|---|---|
| 0 | cover_3-3 | L 1920×1080 | 새로 (COVER_3-3 지시문) | P1 | 3-3 첫 화면 (16:7) | 캔버스 (그린 장면 → 사이 장면 → 그린 장면) |
| 1 | sc_3-3_outro | E 1200×800 | 새로 | P2 | 아웃트로 | 캔버스 (모션 벡터만·광학 흐름만·둘 다) |
| 2 | doc_think · doc_front · doc_scale · doc_judge | A | 재사용 (doc_scale은 대체 표정) | — | 히어로, 등장인물, 아웃트로, 판정 | — |
| 3 | asst_smile · asst_firm · asst_ledger | B | 재사용 | — | 히어로, ③칸, 발표, 꾸러미 | — |
| 4 | fly_point · fly_clip · fly_coffee | C | 재사용 | — | 히어로, ②칸, 대결 후, 아웃트로 | — |
| 5 | robo_coin · robo_smile · robo_calc · robo_meh | D | 재사용 | — | 히어로, ①칸, 대결 후, 아웃트로 | — |

## 2. 새로 그릴 그림 상세 — `sc_3-3_outro`
| 항목 | 내용 |
|---|---|
| 구도 | 가운데 위에 모니터 세 대(불꽃이 반쪽씩 남은 사이 장면, 블록 가장자리가 흐트러진 사이 장면, 둘 다 깨끗한 사이 장면). 박사가 가운데에서 양쪽 접시가 수평인 저울을 들고 있음(무승부). 초파리는 왼쪽에서 커피를 들고 어깨를 으쓱, 주판봇은 오른쪽에서 담담한 얼굴. 조수는 옆에서 미소 |
| 표정 | doc_scale, fly_coffee, robo_meh, asst_smile |
| 피할 것 | 화면 속 글자·숫자, 한쪽이 이긴 듯한 몸짓 |
| 대체 글 (alt) | 모션 벡터만, 광학 흐름만, 둘 다 써서 만든 사이 장면 세 개 앞에서 박사가 저울을 들고, 초파리 연구원과 주판봇이 무승부를 받아들이는 연구실 장면 |

**프롬프트 (복사해서 사용)**
```
16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights, consistent with the reference images, cozy night laboratory mood, purple light, soft magenta and green fluorescent accents, 3:2 landscape scene, medium brightness, three monitors in a row in the upper center showing the same Tetris-like game frame with flying orange sparks: the left one with sparks split into two faint halves, the middle one with slightly broken block edges, the right one clean, blocks with one color per shape (cyan straight, yellow square, purple T, orange L), chibi scientist with round glasses, black hair with one white streak, white lab coat over black vest and tie at the center holding a balance scale with both pans perfectly level, anthropomorphic fruit fly researcher with a black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat and transparent wings on the left facing right holding a coffee cup and shrugging, small boxy retro computer robot with a beige rounded-corner CRT-monitor head, a dark green screen face with mint pixel eyes and mouth, a thin antenna topped with one small red-brown abacus bead, chunky gray segmented arms with round gray mitten hands and two dark gray tank treads, about three quarters the height of the scientist, on the right facing left with a calm neutral face, girl researcher with pink hair in two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie smiling at the side, no white glossy round robot head, no black pill-shaped visor, no yellow eyes, no ball-shaped antenna knob, no cyan chest light, no floating robot, no gold coins, no text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands
```

## 3. 체크리스트
- [x] HTML의 `data-img` 키 16개가 1장 표에 있음
- [x] 대결 D → fly_coffee, robo_meh, asst_smile, doc_scale
- [x] 결과 전 그림(표지, 히어로)에 승패 암시 없음, 그림 안 글자 없음
- [x] 화면 속 블록 색은 1부·3-1·3-2와 같은 규칙. 불꽃은 주황·흰빛

## 4. 매니페스트
```json
{"page":"3-3_frame_generation","anchor":"D:flipbook-film-strip","season":"default","duel":{"result":"D","gap":0,"metric":"rounds won (PSNR dB per round)"},
 "images":[
  {"key":"cover_3-3","plate":"L","size":[1920,1080],"status":"new","priority":"P1","slot":"cover-tall 16:7","fallback":"canvas","alt":"밤의 연구실, 진짜로 그린 두 장면 사이에 AI가 만든 장면이 끼워지는 필름 띠 앞에 네 캐릭터가 선 3-3편 표지"},
  {"key":"sc_3-3_outro","plate":"E","size":[1200,800],"status":"new","priority":"P2","slot":"outro","fallback":"canvas","alt":"모션 벡터만, 광학 흐름만, 둘 다 써서 만든 사이 장면 세 개 앞에서 박사가 저울을 들고, 초파리 연구원과 주판봇이 무승부를 받아들이는 연구실 장면"}
 ]}
```
