# 1-2번 「비슷한 것끼리 묶기」 이미지 제작 명세서

| 항목 | 내용 |
|---|---|
| 페이지 | 1-2_grouping_similar.html |
| 모드 / 주 앵커 | 교과서 / D 생활·현장: 테트리스 블록 정리(무엇을 잴까), 시험 점수, 주머니, 족보 |
| 시즌 | 기본 |
| 대결 | 얼굴 24장을 4묶음으로 → 결과 R (주판봇 승), 차이 20.9%p (70.8% vs 91.7%) |
| 새로 그릴 그림 | P1 1장 (cover_1-2, COVER_1-2_grouping_similar.md) · P2 1장 (sc_1-2_outro) |
| 재사용 | 표정 15장 — 캐릭터 팩 ea5da3f |
| 그림이 없을 때 | 표지(16:7)·아웃트로는 캔버스(블록 더미 → 종류별 주머니 네 개, 얼굴 그림 상자 + 팩 캐릭터)로 완성 상태 |

## 1. 필요한 그림

| # | 키 | 판 | 상태 | 우선 | 들어가는 곳 | 대신 쓰는 그림 |
|---|---|---|---|---|---|---|
| 0 | cover_1-2 | L 1920×1080 | 새로 (COVER_1-2 지시문) | P1 | 첫 화면 표지 (16:7) | 캔버스 대체 표지 |
| 1 | sc_1-2_outro | E 1200×800 | 새로 | P2 | 아웃트로 | 캔버스 장면 |
| 2 | doc_think · doc_front · doc_magic · doc_judge | A | 재사용 (팩) | — | 히어로, 등장인물, 아웃트로, 판정 | — |
| 3 | asst_smile · asst_firm · asst_ledger | B | 재사용 (팩) | — | 히어로, ①칸, 발표, 꾸러미 | — |
| 4 | fly_point · fly_clip · fly_cry | C | 재사용 (팩) | — | 히어로, ③칸, 대결 후, 아웃트로 | — |
| 5 | robo_coin · robo_smile · robo_calc · robo_happy | D | 재사용 (팩) | — | 히어로, ②칸, 대결 후, 아웃트로 | — |
| — | ③칸·대결 얼굴 그림 24장 | 32×32 | 팩에서 만듦 (1-1과 같은 데이터) | — | 족보 잎, 합치기 애니메이션 | — |

## 2. 새로 그릴 그림 상세 — `sc_1-2_outro`
| 항목 | 내용 |
|---|---|
| 구도 | 무승부. 오른쪽 앞 주판봇은 열린 천 주머니 네 개 옆에서 어깨를 으쓱(본전), 왼쪽 앞 초파리는 벽의 나무 모양 족보 그림 앞에서 커피잔을 들고 덤덤. 둘 사이 작업대에 똑같은 높이의 막대 두 개가 선 점수판. 박사는 가운데 뒤에서 저울을 들고, 조수는 주머니 하나를 열어 들여다보며 미소 |
| 표정 | robo_meh, fly_coffee, doc_scale, asst_smile |
| 소품 | 천 주머니 네 개(각각 얼굴 사진 몇 장, 얼굴은 흐린 실루엣), 벽의 족보(가지만, 글자 없음), 자 하나 |
| 대체 글 (alt) | 주판봇과 초파리 연구원이 똑같은 점수판 앞에서 서로를 바라보고, 박사와 조수가 정리된 얼굴 그림 묶음을 지켜보는 연구실 장면 |

**프롬프트 (복사해서 사용)**
```
16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights, consistent with the reference images, cozy night laboratory mood, purple light, soft magenta and green fluorescent accents, 3:2 landscape scene, medium brightness, four open cloth drawstring pouches on the right, each holding a few blurry portrait photos, a tree-shaped family-tree chart pinned on the wall on the left with only branches and no writing, a ruler on the floor, a small blank scoreboard on the workbench with two bars of exactly the same height, small boxy retro computer robot with a beige rounded-corner CRT-monitor head, a dark green screen face with mint pixel eyes and mouth, a thin antenna topped with one small red-brown abacus bead, chunky gray segmented arms with round gray mitten hands and two dark gray tank treads, about three quarters the height of the scientist, in the front right facing left with a small shrug, a wooden abacus in one hand, anthropomorphic fruit fly researcher with a black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat and transparent wings in the front left facing right in front of the tree chart, calmly holding a coffee cup, chibi scientist with round glasses, black hair with one white streak, white lab coat over black vest and tie at the back center holding a small balance scale level, girl researcher with pink hair in two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie opening one pouch and smiling, no white glossy round robot head, no black pill-shaped visor, no yellow eyes, no ball-shaped antenna knob, no cyan chest light, no floating robot, no gold coins, no text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands
```

## 3. 체크리스트
- [x] HTML의 `data-img` 키 16개가 1장 표에 있음
- [x] 대결 D (95.8% vs 95.8%, 2026-11-05 주판봇 v2로 다시 계산) → fly_coffee, robo_meh, asst_smile, doc_scale (5-8절)
- [x] 아웃트로 순서: 박사 → 주판봇(승) → 초파리 → 조수
- [x] 결과 전 그림에 승패 암시 없음, 그림 안 글자 없음

## 4. 매니페스트
```json
{"page":"1-2_grouping_similar","anchor":"D:tetris-pouches-and-family-tree","season":"default","duel":{"result":"R","gap":20.9,"metric":"purity %"},
 "images":[
  {"key":"cover_1-2","plate":"L","size":[1920,1080],"status":"new","priority":"P1","slot":"cover-tall 16:7","fallback":"canvas","alt":"밤의 연구실에서 크기도 방향도 제각각인 테트리스 블록 더미가 종류별 주머니 네 개로 정리되고, 네 캐릭터가 큰 자와 족보 그림 앞에 선 1-2편 표지"},
  {"key":"sc_1-2_outro","plate":"E","size":[1200,800],"status":"new","priority":"P2","slot":"outro","fallback":"canvas","alt":"주판봇과 초파리 연구원이 똑같은 점수판 앞에서 서로를 바라보고, 박사와 조수가 정리된 얼굴 그림 묶음을 지켜보는 연구실 장면"}
 ]}
```
