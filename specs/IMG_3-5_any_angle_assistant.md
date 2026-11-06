# 3-5번 「최종 미션: 어느 각도에서든 조수」 이미지 제작 명세서

| 항목 | 내용 |
|---|---|
| 페이지 | 3-5_any_angle_assistant.html |
| 모드 / 주 앵커 | 교과서 / D 생활·현장: 할인 쿠폰, 증명사진, 시험지 봉투 |
| 시즌 | 기본 (3부 마지막 편) |
| 대결 | 봉인된 시험 사진 120장 정확도: 초파리(렌더러로 한 바퀴 학습) 96.7% vs 주판봇(시험 사진까지 학습) 100% → 결과 X (주판봇 실격, 데이터 누수) |
| 새로 그릴 그림 | P1 1장 (cover_3-5) · P2 1장 (sc_3-5_outro) |
| 재사용 | 표정 15장 — 캐릭터 팩 ea5da3f |
| 그림이 없을 때 | 표지·아웃트로는 페이지가 직접 렌더링한 흉상 + 팩 캐릭터로 완성 상태 |

## 1. 필요한 그림

| # | 키 | 판 | 상태 | 우선 | 들어가는 곳 | 대신 쓰는 그림 |
|---|---|---|---|---|---|---|
| 0 | cover_3-5 | L 1920×1080 | 새로 (COVER_3-5 지시문) | P1 | 3-5 첫 화면 (16:7) | 캔버스 (흉상 앞 · 옆 · 뒤) |
| 1 | sc_3-5_outro | E 1200×800 | 새로 | P2 | 아웃트로 | 캔버스 (앞·옆·뒤 흉상에 초록 표시) |
| 2 | doc_think · doc_front · doc_judge | A | 재사용 | — | 히어로, 등장인물, 판정, 아웃트로 | — |
| 3 | asst_smile · asst_firm · asst_ledger | B | 재사용 | — | 히어로, ③칸, 발표, 꾸러미 | — |
| 4 | fly_point · fly_clip · fly_arms | C | 재사용 | — | 히어로, ②칸, 대결 후, 아웃트로 | — |
| 5 | robo_coin · robo_smile · robo_calc · robo_blush | D | 재사용 | — | 히어로, ①칸, 대결 후, 아웃트로 | — |

## 2. 새로 그릴 그림 상세 — `sc_3-5_outro`
| 항목 | 내용 |
|---|---|
| 구도 | 가운데 위에 액자 세 개(조수 흉상의 앞·옆·뒤), 액자마다 초록 체크 표시. 박사가 가운데에서 빨간 봉인이 뜯긴 봉투를 들어 보이며 판정. 주판봇은 오른쪽에서 얼굴 화면을 붉히며 사진 더미를 내려놓음. 초파리는 왼쪽에서 팔짱을 끼고 당당함. 조수는 옆에서 웃으며 뒤돌아 쪽머리를 보여 줌 |
| 표정 | doc_judge, robo_blush, fly_arms, asst_smile |
| 피할 것 | 화면 속 글자·숫자, 화를 내거나 벌주는 장면(실격은 담담하게) |
| 대체 글 (alt) | 앞·옆·뒤에서 찍은 조수 흉상 세 화면에 모두 초록 표시가 붙고, 박사가 봉투를 들고 판정하며, 주판봇이 얼굴을 붉히고 초파리 연구원이 팔짱을 낀 연구실 장면 |

**프롬프트 (복사해서 사용)**
```
16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights, consistent with the reference images, cozy night laboratory mood, purple light, soft magenta and green fluorescent accents, 3:2 landscape scene, medium brightness, three picture frames in a row in the upper center showing a simple sphere-built bust of the girl researcher from the front, the side and the back, each frame with a small green check mark, chibi scientist with round glasses, black hair with one white streak, white lab coat over black vest and tie at the center holding up an opened envelope with a broken red wax seal like a referee, small boxy retro computer robot with a beige rounded-corner CRT-monitor head, a dark green screen face with mint pixel eyes and mouth, a thin antenna topped with one small red-brown abacus bead, chunky gray segmented arms with round gray mitten hands and two dark gray tank treads, about three quarters the height of the scientist, on the right facing left with a blushing embarrassed face setting down a pile of photos, anthropomorphic fruit fly researcher with a black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat and transparent wings on the left facing right with arms crossed proudly, girl researcher with pink hair in two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie at the side smiling and turning her head to show her buns, no white glossy round robot head, no black pill-shaped visor, no yellow eyes, no ball-shaped antenna knob, no cyan chest light, no floating robot, no gold coins, no text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands
```

## 3. 체크리스트
- [x] HTML의 `data-img` 키 15개가 1장 표에 있음
- [x] 대결 X → fly_arms, robo_blush, asst_shock(판정 순간), doc_judge
- [x] 결과 전 그림(표지, 히어로)에 승패 암시 약하게만, 그림 안 글자 없음
- [x] 흉상 색은 조수 캐릭터와 같은 규칙(분홍 쪽머리 둘, 남색 줄, 파란 눈)

## 4. 매니페스트
```json
{"page":"3-5_any_angle_assistant","anchor":"D:photo-studio-sealed-envelope","season":"default","duel":{"result":"X","gap":3.3,"metric":"accuracy on sealed test photos (%)"},
 "images":[
  {"key":"cover_3-5","plate":"L","size":[1920,1080],"status":"new","priority":"P1","slot":"cover-tall 16:7","fallback":"canvas","alt":"밤의 연구실, 돌림판 둘레를 도는 카메라 앞에 조수의 3D 흉상이 앞·옆·뒤로 비치고 네 캐릭터가 선 3-5편 표지"},
  {"key":"sc_3-5_outro","plate":"E","size":[1200,800],"status":"new","priority":"P2","slot":"outro","fallback":"canvas","alt":"앞·옆·뒤에서 찍은 조수 흉상 세 화면에 모두 초록 표시가 붙고, 박사가 봉투를 들고 판정하며, 주판봇이 얼굴을 붉히고 초파리 연구원이 팔짱을 낀 연구실 장면"}
 ]}
```

## 5. 받은 그림 (2026-11-01, 저자 제공)
- `asst_turn_000` ~ `asst_turn_315` — 조수 흉상 8방향(45° 간격). 미션 칸 "연구실 예산 공지" 아래 갤러리에 넣음 (256×256 WebP로 줄여 페이지 안에 포함). 원본 512×512 PNG는 `specs/assets/`.
- `asst_cry` — 조수 우는 얼굴. 예산 공지 대화의 조수 얼굴로 넣음.
- 실험 칸(①②③)과 표지·아웃트로의 앞·옆·뒤는 이야기 설정("자금난")에 따라 공 모형 그대로 둔다.
