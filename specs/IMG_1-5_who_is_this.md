# 1-5번 「이 얼굴은 누구?」 이미지 제작 명세서

| 항목 | 내용 |
|---|---|
| 페이지 | 1-5_who_is_this.html |
| 모드 / 주 앵커 | 교과서 / D 생활·현장: 증명사진으로 단체 사진에서 찾기, 뒷모습 착각, 머리 색으로 알아보기 |
| 시즌 | 기본 |
| 대결 | 색 비율 + 이름표 4장 vs 픽셀 + 정면 이름표 40장, 아무 각도 사진 120장 정답률 → 결과 F (초파리 승). 88.3% vs 61.7%, 차이 26.6%p |
| 새로 그릴 그림 | P1 1장 (cover_1-5) · P2 1장 (sc_1-5_outro) |
| 재사용 | 표정 15장 — 캐릭터 팩 ea5da3f |
| 그림이 없을 때 | 표지·아웃트로는 페이지가 직접 그린 흉상 + 팩 캐릭터로 완성 상태 |

## 1. 필요한 그림

| # | 키 | 판 | 상태 | 우선 | 들어가는 곳 | 대신 쓰는 그림 |
|---|---|---|---|---|---|---|
| 0 | cover_1-5 | L 1920×1080 | 새로 (COVER_1-5 지시문) | P1 | 1-5 첫 화면 (16:7) | 캔버스 (조수 앞·옆·뒤 + 다른 캐릭터 뒷모습) |
| 1 | sc_1-5_outro | E 1200×800 | 새로 | P2 | 아웃트로 | 캔버스 (네 캐릭터 뒷모습에 맞는 이름) |
| 2 | doc_think · doc_front · doc_judge | A | 재사용 | — | 히어로, 등장인물, 판정, 아웃트로 | — |
| 3 | asst_smile · asst_firm · asst_ledger | B | 재사용 | — | 히어로, ②칸, 발표, 꾸러미 | — |
| 4 | fly_point · fly_clip · fly_arms | C | 재사용 | — | 히어로, ①칸, 대결 후, 아웃트로 | — |
| 5 | robo_coin · robo_smile · robo_calc · robo_sigh | D | 재사용 | — | 히어로, ③칸, 대결 후, 아웃트로 | — |

## 2. 새로 그릴 그림 상세 — `sc_1-5_outro`
| 항목 | 내용 |
|---|---|
| 구도 | 뒤쪽 게시판에 네 캐릭터 흉상의 뒷모습 사진 네 장, 각각 맞는 이름표 리본과 실로 이어짐. 박사가 가운데에서 초파리 쪽으로 손을 들어 판정. 초파리는 왼쪽에서 팔레트를 들고 팔짱. 주판봇은 오른쪽에서 정면 이름표 리본 뭉치를 안고 한숨. 조수는 옆에서 뒤돌아 쪽머리를 보여 주며 웃음 |
| 표정 | doc_judge, fly_arms, robo_sigh, asst_smile |
| 피할 것 | 화면 속 글자·숫자, 사진 속 실제 얼굴 |
| 대체 글 (alt) | 네 캐릭터의 뒷모습 사진에 각각 맞는 이름표가 붙어 있고, 박사가 판정하며 초파리 연구원이 팔짱을 끼고 주판봇이 이름표 뭉치를 들고 한숨 쉬는 연구실 장면 |

**프롬프트 (복사해서 사용)**
```
16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights, consistent with the reference images, cozy night laboratory mood, purple light, soft magenta and green fluorescent accents, 3:2 landscape scene, medium brightness, a cork board on the back wall with four pinned back-view photos of simple sphere-built toy busts of the characters, each connected by a string to its correct ribbon tag, chibi scientist with round glasses, black hair with one white streak, white lab coat over black vest and tie at the center raising one hand toward the fly researcher like a referee, anthropomorphic fruit fly researcher with a black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat and transparent wings on the left facing right with arms crossed proudly holding a paint palette, small boxy retro computer robot with a beige rounded-corner CRT-monitor head, a dark green screen face with mint pixel eyes and mouth, a thin antenna topped with one small red-brown abacus bead, chunky gray segmented arms with round gray mitten hands and two dark gray tank treads, about three quarters the height of the scientist, on the right facing left sighing while hugging a big bundle of ribbon tags, girl researcher with pink hair in two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie turned away showing her buns and smiling over her shoulder, no white glossy round robot head, no black pill-shaped visor, no yellow eyes, no ball-shaped antenna knob, no cyan chest light, no floating robot, no gold coins, no text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands
```

## 3. 체크리스트
- [x] HTML의 `data-img` 키가 1장 표에 있음
- [x] 대결 F → fly_arms, robo_sigh, asst_spark, doc_judge
- [x] 결과 전 그림(표지, 히어로)에 승패 암시 없음, 그림 안 글자 없음
- [x] 흉상은 공 모양 장난감처럼 단순하게 (캐릭터 색 규칙 유지)

## 4. 매니페스트
```json
{"page":"1-5_who_is_this","anchor":"D:corkboard-name-strings","season":"default","duel":{"result":"F","gap":26.6,"metric":"accuracy on any-angle photos (%)"},
 "images":[
  {"key":"cover_1-5","plate":"L","size":[1920,1080],"status":"new","priority":"P1","slot":"cover-tall 16:7","fallback":"canvas","alt":"밤의 연구실, 조수의 앞모습·옆모습·뒷모습 사진과 다른 캐릭터들의 뒷모습 사진이 벽에 붙어 있고 네 캐릭터가 누가 누구인지 맞혀 보는 1-5편 표지"},
  {"key":"sc_1-5_outro","plate":"E","size":[1200,800],"status":"new","priority":"P2","slot":"outro","fallback":"canvas","alt":"네 캐릭터의 뒷모습 사진에 각각 맞는 이름표가 붙어 있고, 박사가 판정하며 초파리 연구원이 팔짱을 끼고 주판봇이 이름표 뭉치를 들고 한숨 쉬는 연구실 장면"}
 ]}
```

## 5. 받은 그림 (2026-11-01, 저자 제공)
- `doc_turn_*`, `asst_turn_*`, `fly_turn_*`, `robo_turn_*` — 네 캐릭터 흉상 8방향(45° 간격), 모두 32장. 미션 칸 "연구실 예산 공지" 아래 갤러리에 넣음(144×144 WebP로 줄여 페이지 안에 포함). 원본 512×512 PNG는 `specs/assets/`.
- `asst_cry` — 조수 우는 얼굴. 예산 공지 대화에 넣음.
- 실험 칸은 이야기 설정("자금난")에 따라 공 모형 흉상 그대로 둔다. 3-5의 같은 농담으로 이어진다.
