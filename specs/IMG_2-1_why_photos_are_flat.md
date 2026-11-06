# 2-1번 「사진은 왜 납작할까」 이미지 제작 명세서

| 항목 | 내용 |
|---|---|
| 페이지 | 2-1_why_photos_are_flat.html |
| 모드 / 주 앵커 | 교과서 / D 생활·현장: 바늘구멍 사진기, 단체 사진 속 가려진 친구, 손전등 |
| 시즌 | 기본 |
| 대결 | 사진 한 장으로 손잡이 맞히기: 보이는 것만 믿기 vs 늘 있다 → 결과 F (초파리 승). 77.5% vs 50.0%, 차이 27.5%p |
| 새로 그릴 그림 | P1 1장 (cover_2-1) · P2 1장 (sc_2-1_outro) |
| 재사용 | 표정 — 캐릭터 팩 ea5da3f |
| 그림이 없을 때 | 표지·아웃트로는 페이지가 직접 렌더링한 장면 + 팩 캐릭터로 완성 상태 |

## 1. 필요한 그림

| # | 키 | 판 | 상태 | 우선 | 들어가는 곳 | 대신 쓰는 그림 |
|---|---|---|---|---|---|---|
| 0 | cover_2-1 | L 1920×1080 | 새로 (COVER 지시문) | P1 | 첫 화면 (16:7) | 캔버스 |
| 1 | sc_2-1_outro | E 1200×800 | 새로 | P2 | 아웃트로 | 캔버스 |
| 2 | doc_think · doc_front · doc_judge | A | 재사용 | — | 히어로, 등장인물, 판정, 아웃트로 | — |
| 3 | asst_smile · asst_firm · asst_ledger | B | 재사용 | — | 히어로, ①칸, 발표, 꾸러미 | — |
| 4 | fly_point · fly_clip · fly_arms | C | 재사용 | — | 히어로, ②칸, 대결 후, 아웃트로 | — |
| 5 | robo_coin · robo_smile · robo_calc · robo_sigh | D | 재사용 | — | 히어로, ③칸, 대결 후, 아웃트로 | — |

## 2. 새로 그릴 그림 상세 — `sc_2-1_outro`
| 항목 | 내용 |
|---|---|
| 구도 | 뒤쪽 벽에 앞·옆·위에서 찍은 머그컵 사진 세 장. 박사가 초파리 쪽으로 손을 들어 판정. 초파리는 돋보기를 들고 팔짱. 주판봇은 손잡이 없는 컵을 들고 한숨. 조수는 옆에서 웃음 |
| 표정 | doc_judge, fly_arms, robo_sigh, asst_smile |
| 피할 것 | 화면 속 글자·숫자 |
| 대체 글 (alt) | 앞, 옆, 위에서 찍은 머그컵 사진 세 장 앞에서 박사가 판정하고, 초파리 연구원이 팔짱을 끼고 주판봇이 한숨 쉬는 연구실 장면 |

**프롬프트 (복사해서 사용)**
```
16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights, consistent with the reference images, cozy night laboratory mood, purple light, soft magenta and green fluorescent accents, 3:2 landscape scene, medium brightness, three framed photos of a white mug with a magenta stripe seen from the front, the side and from above on the back wall, chibi scientist with round glasses, black hair with one white streak, white lab coat over black vest and tie at the center raising one hand toward the fly researcher like a referee, anthropomorphic fruit fly researcher with a black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat and transparent wings on the left facing right with arms crossed holding a magnifying glass, small boxy retro computer robot with a beige rounded-corner CRT-monitor head, a dark green screen face with mint pixel eyes and mouth, a thin antenna topped with one small red-brown abacus bead, chunky gray segmented arms with round gray mitten hands and two dark gray tank treads, about three quarters the height of the scientist, on the right facing left sighing while holding a mug without a handle, girl researcher with pink hair in two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie smiling at the side, no white glossy round robot head, no black pill-shaped visor, no yellow eyes, no ball-shaped antenna knob, no cyan chest light, no floating robot, no gold coins, no text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands.
```

## 3. 체크리스트
- [x] HTML의 `data-img` 키가 1장 표에 있음
- [x] 대결 F → fly_arms, robo_sigh, asst_spark, doc_judge
- [x] 결과 전 그림(표지, 히어로)에 승패 암시 없음, 그림 안 글자 없음

## 4. 매니페스트
```json
{"page":"2-1_why_photos_are_flat","anchor":"D:pinhole-box","season":"default","duel":{"result":"F","gap":27.5,"metric":"accuracy of handle detection from one photo (%)"},
 "images":[
  {"key":"cover_2-1","plate":"L","size":[1920,1080],"status":"new","priority":"P1","slot":"cover-tall 16:7","fallback":"canvas","alt":"밤의 연구실, 큰 바늘구멍 상자 뒷벽에 머그컵이 거꾸로 비치고 네 캐릭터가 상자를 들여다보는 2-1편 표지"},
  {"key":"sc_2-1_outro","plate":"E","size":[1200,800],"status":"new","priority":"P2","slot":"outro","fallback":"canvas"}
 ]}
```
