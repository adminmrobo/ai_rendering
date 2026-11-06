# 2-2번 「몽타주 그리기」 이미지 제작 명세서

| 항목 | 내용 |
|---|---|
| 페이지 | 2-2_drawing_a_montage.html |
| 모드 / 주 앵커 | 교과서 / D 생활·현장: 몽타주, 운동장에서 열쇠 찾기, 라디오 다이얼 |
| 시즌 | 기본 |
| 대결 | 몽타주 81장으로 숫자 넷 찾기: 격자 vs 무작위, 최선 어긋남(낮을수록 좋음) → 결과 R (주판봇 승). 17.7% vs 11.2%, 차이 6.5 (bigGap 5 이상 → 초파리 cry) |
| 새로 그릴 그림 | P1 1장 (cover_2-2) · P2 1장 (sc_2-2_outro) |
| 재사용 | 표정 — 캐릭터 팩 ea5da3f |
| 그림이 없을 때 | 표지·아웃트로는 페이지가 직접 렌더링한 장면 + 팩 캐릭터로 완성 상태 |

## 1. 필요한 그림

| # | 키 | 판 | 상태 | 우선 | 들어가는 곳 | 대신 쓰는 그림 |
|---|---|---|---|---|---|---|
| 0 | cover_2-2 | L 1920×1080 | 새로 (COVER 지시문) | P1 | 첫 화면 (16:7) | 캔버스 |
| 1 | sc_2-2_outro | E 1200×800 | 새로 | P2 | 아웃트로 | 캔버스 |
| 2 | doc_think · doc_front · doc_judge | A | 재사용 | — | 히어로, 등장인물, 판정, 아웃트로 | — |
| 3 | asst_smile · asst_firm · asst_ledger | B | 재사용 | — | 히어로, ①칸, 발표, 꾸러미 | — |
| 4 | fly_point · fly_clip · fly_cry | C | 재사용 | — | 히어로, ③칸, 대결 후, 아웃트로 | — |
| 5 | robo_coin · robo_smile · robo_calc · robo_happy | D | 재사용 | — | 히어로, ②칸, 대결 후, 아웃트로 | — |

## 2. 새로 그릴 그림 상세 — `sc_2-2_outro`
| 항목 | 내용 |
|---|---|
| 구도 | 벽에 격자로 찾은 몽타주와 무작위로 찾은 몽타주 두 장(무작위 쪽이 사진과 더 닮음). 박사가 주판봇 쪽으로 손을 들어 판정. 주판봇은 흩뿌린 카드 사이에서 기뻐함. 초파리는 자를 쥔 채 울상. 조수는 옆에서 웃음 |
| 표정 | doc_judge, robo_happy, fly_cry, asst_smile |
| 피할 것 | 화면 속 글자·숫자 |
| 대체 글 (alt) | 격자와 무작위로 찾은 몽타주 두 장 앞에서 박사가 주판봇의 승리를 판정하고, 초파리 연구원이 울상이 되고 주판봇이 기뻐하는 연구실 장면 |

**프롬프트 (복사해서 사용)**
```
16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights, consistent with the reference images, cozy night laboratory mood, purple light, soft magenta and green fluorescent accents, 3:2 landscape scene, medium brightness, two framed cup sketches on the back wall next to a cup photo, the right one matching the photo better, chibi scientist with round glasses, black hair with one white streak, white lab coat over black vest and tie at the center raising one hand toward the robot like a referee, small boxy retro computer robot with a beige rounded-corner CRT-monitor head, a dark green screen face with mint pixel eyes and mouth, a thin antenna topped with one small red-brown abacus bead, chunky gray segmented arms with round gray mitten hands and two dark gray tank treads, about three quarters the height of the scientist, on the right facing left looking happy among scattered sketch cards, anthropomorphic fruit fly researcher with a black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat and transparent wings on the left facing right holding a ruler with teary eyes, girl researcher with pink hair in two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie smiling at the side, no white glossy round robot head, no black pill-shaped visor, no yellow eyes, no ball-shaped antenna knob, no cyan chest light, no floating robot, no gold coins, no text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands.
```

## 3. 체크리스트
- [x] HTML의 `data-img` 키가 1장 표에 있음
- [x] 대결 R (차이 6.5 ≥ bigGap 5) → fly_cry, robo_happy, asst_spark, doc_judge
- [x] 결과 전 그림(표지, 히어로)에 승패 암시 없음, 그림 안 글자 없음

## 4. 매니페스트
```json
{"page":"2-2_drawing_a_montage","anchor":"D:police-sketch","season":"default","duel":{"result":"R","gap":6.5,"metric":"best silhouette mismatch with 81 renders (lower is better)"},
 "images":[
  {"key":"cover_2-2","plate":"L","size":[1920,1080],"status":"new","priority":"P1","slot":"cover-tall 16:7","fallback":"canvas","alt":"밤의 연구실, 컵 사진 한 장 옆에 고쳐 그린 몽타주 컵 그림들이 줄지어 붙어 있고 네 캐릭터가 사진과 몽타주를 맞춰 보는 2-2편 표지"},
  {"key":"sc_2-2_outro","plate":"E","size":[1200,800],"status":"new","priority":"P2","slot":"outro","fallback":"canvas"}
 ]}
```
