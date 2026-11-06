# 1-3번 「얼굴을 지도 위 점으로」 이미지 제작 명세서

| 항목 | 내용 |
|---|---|
| 페이지 | 1-3_faces_on_a_map.html |
| 모드 / 주 앵커 | 교과서 / D 생활·현장: 키·몸무게 지도, 그림자 놀이, 겹쳐 인화한 사진 |
| 시즌 | 기본 |
| 대결 | 주성분 2개 vs 가장 많이 변하는 픽셀 2개, 지도 위 이웃 맞히기 → 결과 F (초파리 승). 87.1% vs 57.5%, 차이 29.6%p |
| 새로 그릴 그림 | P1 1장 (cover_1-3) · P2 1장 (sc_1-3_outro) |
| 재사용 | 표정 15장 — 캐릭터 팩 ea5da3f |
| 그림이 없을 때 | 표지·아웃트로는 페이지가 직접 그린 주성분 지도 + 팩 캐릭터로 완성 상태 |

## 1. 필요한 그림

| # | 키 | 판 | 상태 | 우선 | 들어가는 곳 | 대신 쓰는 그림 |
|---|---|---|---|---|---|---|
| 0 | cover_1-3 | L 1920×1080 | 새로 (COVER_1-3 지시문) | P1 | 1-3 첫 화면 (16:7) | 캔버스 (주성분 지도 + 원본 24장) |
| 1 | sc_1-3_outro | E 1200×800 | 새로 | P2 | 아웃트로 | 캔버스 (주성분 지도) |
| 2 | doc_think · doc_front · doc_judge | A | 재사용 | — | 히어로, 등장인물, 판정, 아웃트로 | — |
| 3 | asst_smile · asst_firm · asst_ledger | B | 재사용 | — | 히어로, ②칸, 발표, 꾸러미 | — |
| 4 | fly_point · fly_clip · fly_arms | C | 재사용 | — | 히어로, ①칸, 대결 후, 아웃트로 | — |
| 5 | robo_coin · robo_smile · robo_calc · robo_sigh | D | 재사용 | — | 히어로, ③칸, 대결 후, 아웃트로 | — |

## 2. 새로 그릴 그림 상세 — `sc_1-3_outro`
| 항목 | 내용 |
|---|---|
| 구도 | 뒤쪽 벽에 커다란 지도(네 무리의 점, 파랑·분홍·빨강·초록). 박사가 가운데에서 지도를 가리키며 초파리 쪽으로 손을 들어 판정. 초파리는 왼쪽에서 접은 종이 점을 들고 팔짱. 주판봇은 오른쪽에서 가위와 잘린 카드 귀퉁이 둘을 든 채 한숨. 조수는 옆에서 분홍 무리를 가리키며 미소 |
| 표정 | doc_judge, fly_arms, robo_sigh, asst_smile |
| 피할 것 | 화면 속 글자·숫자 |
| 대체 글 (alt) | 네 캐릭터의 얼굴 그림이 색깔별로 모인 큰 지도 앞에서 박사가 판정하고, 초파리 연구원이 팔짱을 끼고 주판봇이 한숨 쉬는 연구실 장면 |

**프롬프트 (복사해서 사용)**
```
16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights, consistent with the reference images, cozy night laboratory mood, purple light, soft magenta and green fluorescent accents, 3:2 landscape scene, medium brightness, a large map on the back wall with four clearly separated clusters of glowing dots in blue, pink, red and green, chibi scientist with round glasses, black hair with one white streak, white lab coat over black vest and tie at the center raising one hand toward the fly researcher like a referee, anthropomorphic fruit fly researcher with a black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat and transparent wings on the left facing right with arms crossed proudly holding a small folded paper dot, small boxy retro computer robot with a beige rounded-corner CRT-monitor head, a dark green screen face with mint pixel eyes and mouth, a thin antenna topped with one small red-brown abacus bead, chunky gray segmented arms with round gray mitten hands and two dark gray tank treads, about three quarters the height of the scientist, on the right facing left sighing and holding scissors and two snipped card corners, girl researcher with pink hair in two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie at the side smiling and pointing at the pink cluster, no white glossy round robot head, no black pill-shaped visor, no yellow eyes, no ball-shaped antenna knob, no cyan chest light, no floating robot, no gold coins, no text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands
```

## 3. 체크리스트
- [x] HTML의 `data-img` 키가 1장 표에 있음
- [x] 대결 F → fly_arms, robo_sigh, asst_spark, doc_judge
- [x] 결과 전 그림(표지, 히어로)에 승패 암시 없음, 그림 안 글자 없음
- [x] 점 색은 캐릭터 정답표(박사 파랑, 조수 분홍, 초파리 빨강, 주판봇 초록)

## 4. 매니페스트
```json
{"page":"1-3_faces_on_a_map","anchor":"D:paper-map-origami","season":"default","duel":{"result":"F","gap":29.6,"metric":"nearest-neighbor agreement on 2D map (%)"},
 "images":[
  {"key":"cover_1-3","plate":"L","size":[1920,1080],"status":"new","priority":"P1","slot":"cover-tall 16:7","fallback":"canvas","alt":"밤의 연구실, 얼굴 그림 카드 수백 장이 큰 지도 위의 점으로 접혀 내려앉고 네 캐릭터가 지도를 내려다보는 1-3편 표지"},
  {"key":"sc_1-3_outro","plate":"E","size":[1200,800],"status":"new","priority":"P2","slot":"outro","fallback":"canvas","alt":"네 캐릭터의 얼굴 그림이 색깔별로 모인 큰 지도 앞에서 박사가 판정하고, 초파리 연구원이 팔짱을 끼고 주판봇이 한숨 쉬는 연구실 장면"}
 ]}
```
