# 1-4번 「가리고 맞히기」 이미지 제작 명세서

| 항목 | 내용 |
|---|---|
| 페이지 | 1-4_mask_and_predict.html |
| 모드 / 주 앵커 | 교과서 / D 생활·현장: 옷 압축 팩, 빈칸 채우기 공부, 연습보다 큰 빈칸 |
| 시즌 | 기본 |
| 대결 | 1-1의 베끼기 vs 가리고 배운 상자, 처음 보는 표정 40장의 가린 곳 오차(×1000, 낮을수록 좋음) → 결과 R (주판봇 승). 47.0 vs 44.7, 차이 2.3 (bigGap 5 미만 → 초파리 coffee) |
| 새로 그릴 그림 | P1 1장 (cover_1-4) · P2 1장 (sc_1-4_outro) |
| 재사용 | 표정 15장 — 캐릭터 팩 ea5da3f |
| 그림이 없을 때 | 표지·아웃트로는 페이지가 직접 채운 얼굴 + 팩 캐릭터로 완성 상태 |

## 1. 필요한 그림

| # | 키 | 판 | 상태 | 우선 | 들어가는 곳 | 대신 쓰는 그림 |
|---|---|---|---|---|---|---|
| 0 | cover_1-4 | L 1920×1080 | 새로 (COVER_1-4 지시문) | P1 | 1-4 첫 화면 (16:7) | 캔버스 (가린 얼굴 → 상자가 채운 얼굴 → 원본) |
| 1 | sc_1-4_outro | E 1200×800 | 새로 | P2 | 아웃트로 | 캔버스 (상자가 채운 얼굴 4장) |
| 2 | doc_think · doc_front · doc_judge | A | 재사용 | — | 히어로, 등장인물, 판정, 아웃트로 | — |
| 3 | asst_smile · asst_firm · asst_ledger | B | 재사용 | — | 히어로, ②칸, 발표, 꾸러미 | — |
| 4 | fly_point · fly_clip · fly_coffee | C | 재사용 | — | 히어로, ①칸, 대결 후, 아웃트로 | — |
| 5 | robo_coin · robo_smile · robo_calc · robo_happy | D | 재사용 | — | 히어로, ③칸, 대결 후, 아웃트로 | — |

## 2. 새로 그릴 그림 상세 — `sc_1-4_outro`
| 항목 | 내용 |
|---|---|
| 구도 | 뒤쪽 벽에 빈칸이 채워진 얼굴 카드 네 장. 박사가 가운데에서 주판봇 쪽으로 손을 들어 판정(아슬아슬한 승리라 표정은 담담). 주판봇은 오른쪽에서 상자 옆에서 기뻐함. 초파리는 왼쪽에서 앨범을 옆에 끼고 커피를 듦(크게 가린 카드 한 장을 자기가 채운 것으로 들어 보임). 조수는 옆에서 웃음 |
| 표정 | doc_judge, robo_happy, fly_coffee, asst_smile |
| 피할 것 | 화면 속 글자·숫자, 초파리가 우는 모습(차이가 작음) |
| 대체 글 (alt) | 빈칸이 채워진 얼굴 그림 네 장 앞에서 박사가 판정하고, 주판봇이 기뻐하며 초파리 연구원이 커피를 드는 연구실 장면 |

**프롬프트 (복사해서 사용)**
```
16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights, consistent with the reference images, cozy night laboratory mood, purple light, soft magenta and green fluorescent accents, 3:2 landscape scene, medium brightness, four portrait cards of the characters pinned on the back wall with their faces neatly filled in, an hourglass-shaped machine with a narrow glowing waist on the right, chibi scientist with round glasses, black hair with one white streak, white lab coat over black vest and tie at the center calmly raising one hand toward the robot like a referee, small boxy retro computer robot with a beige rounded-corner CRT-monitor head, a dark green screen face with mint pixel eyes and mouth, a thin antenna topped with one small red-brown abacus bead, chunky gray segmented arms with round gray mitten hands and two dark gray tank treads, about three quarters the height of the scientist, on the right facing left looking happy beside the machine, anthropomorphic fruit fly researcher with a black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat and transparent wings on the left facing right holding a coffee cup with a photo album under one arm, girl researcher with pink hair in two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie smiling at the side, no white glossy round robot head, no black pill-shaped visor, no yellow eyes, no ball-shaped antenna knob, no cyan chest light, no floating robot, no gold coins, no text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands
```

## 3. 체크리스트
- [x] HTML의 `data-img` 키가 1장 표에 있음
- [x] 대결 R (차이 2.3 < bigGap 5) → fly_coffee, robo_happy, asst_spark, doc_judge
- [x] 결과 전 그림(표지, 히어로)에 승패 암시 없음, 그림 안 글자 없음
- [x] 가린 곳은 회색 종이로 표현 (글자 없음)

## 4. 매니페스트
```json
{"page":"1-4_mask_and_predict","anchor":"D:hourglass-box-cloze","season":"default","duel":{"result":"R","gap":2.3,"metric":"masked-region error x1000 on unseen expression (lower is better)"},
 "images":[
  {"key":"cover_1-4","plate":"L","size":[1920,1080],"status":"new","priority":"P1","slot":"cover-tall 16:7","fallback":"canvas","alt":"밤의 연구실, 가운데가 가려진 얼굴 카드가 접었다 펴는 상자를 지나 빈칸이 채워진 얼굴로 나오고 네 캐릭터가 지켜보는 1-4편 표지"},
  {"key":"sc_1-4_outro","plate":"E","size":[1200,800],"status":"new","priority":"P2","slot":"outro","fallback":"canvas","alt":"빈칸이 채워진 얼굴 그림 네 장 앞에서 박사가 판정하고, 주판봇이 기뻐하며 초파리 연구원이 커피를 드는 연구실 장면"}
 ]}
```
