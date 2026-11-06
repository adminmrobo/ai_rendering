# 3-4번 「AI가 빛을 다시 그린다」 이미지 제작 명세서

| 항목 | 내용 |
|---|---|
| 페이지 | 3-4_relight_with_ai.html |
| 모드 / 주 앵커 | 교과서 / D 생활·현장: 어두운 곳의 자글자글한 사진, 사진 앱 노이즈 제거, 보정 전문가의 붓 |
| 시즌 | 기본 |
| 대결 | 손 필터(길잡이 반경 3, 한 가지 설정) vs 배운 필터, 여덟 경우 평균 빛 PSNR → 결과 R (주판봇 승). 30.78 vs 32.03 dB, 차이 1.25 dB (bigGap 1.5 미만 → 초파리 coffee) |
| 새로 그릴 그림 | P1 1장 (cover_3-4) · P2 1장 (sc_3-4_outro) |
| 재사용 | 표정 15장 — 캐릭터 팩 ea5da3f |
| 그림이 없을 때 | 표지·아웃트로는 페이지가 직접 렌더링한 장면 + 팩 캐릭터로 완성 상태 |

## 1. 필요한 그림

| # | 키 | 판 | 상태 | 우선 | 들어가는 곳 | 대신 쓰는 그림 |
|---|---|---|---|---|---|---|
| 0 | cover_3-4 | L 1920×1080 | 새로 (COVER_3-4 지시문) | P1 | 3-4 첫 화면 (16:7) | 캔버스 (광선 1줄 → AI가 다시 그린 빛 → 정답) |
| 1 | sc_3-4_outro | E 1200×800 | 새로 | P2 | 아웃트로 | 캔버스 (손 필터 · 배운 필터 · 정답) |
| 2 | doc_think · doc_front · doc_judge | A | 재사용 | — | 히어로, 등장인물, 판정, 아웃트로 | — |
| 3 | asst_smile · asst_firm · asst_ledger | B | 재사용 | — | 히어로, ①칸, 발표, 꾸러미 | — |
| 4 | fly_point · fly_clip · fly_coffee | C | 재사용 | — | 히어로, ②칸, 대결 후, 아웃트로 | — |
| 5 | robo_coin · robo_smile · robo_calc · robo_happy | D | 재사용 | — | 히어로, ③칸, 대결 후, 아웃트로 | — |

## 2. 새로 그릴 그림 상세 — `sc_3-4_outro`
| 항목 | 내용 |
|---|---|
| 구도 | 가운데 위에 모니터 세 대(그림자 끝이 조금 뭉개진 화면, 매끄럽고 또렷한 화면, 정답 화면). 박사가 가운데에서 판정하듯 손을 들어 오른쪽(주판봇 쪽)을 가리킴. 주판봇은 오른쪽에서 기쁜 얼굴로 반짝이는 신경망 그물을 들고, 초파리는 왼쪽에서 커피를 들고 담담하게 체를 내려놓음. 조수는 옆에서 카메라를 들고 미소 |
| 표정 | doc_judge, robo_happy, fly_coffee, asst_smile |
| 피할 것 | 화면 속 글자·숫자, 초파리가 우는 모습(차이가 크지 않음) |
| 대체 글 (alt) | 손 필터, 배운 필터, 정답 세 화면 앞에서 박사가 판정하고, 주판봇이 기뻐하며 초파리 연구원이 커피를 드는 연구실 장면 |

**프롬프트 (복사해서 사용)**
```
16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights, consistent with the reference images, cozy night laboratory mood, purple light, soft magenta and green fluorescent accents, 3:2 landscape scene, medium brightness, three monitors in a row in the upper center showing the same side view of Tetris-like blocks lit by a long ceiling bar lamp with soft shadows: the left one with slightly blurred shadow edges, the middle and right ones clean and crisp, blocks with one color per shape (cyan straight, yellow square, purple T, orange L), chibi scientist with round glasses, black hair with one white streak, white lab coat over black vest and tie at the center raising one hand toward the robot like a referee, small boxy retro computer robot with a beige rounded-corner CRT-monitor head, a dark green screen face with mint pixel eyes and mouth, a thin antenna topped with one small red-brown abacus bead, chunky gray segmented arms with round gray mitten hands and two dark gray tank treads, about three quarters the height of the scientist, on the right facing left looking happy and holding a glowing neural network net of dots and lines, anthropomorphic fruit fly researcher with a black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat and transparent wings on the left facing right holding a coffee cup calmly with a square hand sieve set down beside it, girl researcher with pink hair in two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie holding a camera and smiling at the side, no white glossy round robot head, no black pill-shaped visor, no yellow eyes, no ball-shaped antenna knob, no cyan chest light, no floating robot, no gold coins, no text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands
```

## 3. 체크리스트
- [x] HTML의 `data-img` 키 15개가 1장 표에 있음
- [x] 대결 R (차이 1.25 dB < bigGap 1.5) → fly_coffee, robo_happy, asst_spark, doc_judge
- [x] 결과 전 그림(표지, 히어로)에 승패 암시 없음, 그림 안 글자 없음
- [x] 화면 속 블록 색은 1부·3-1~3-3과 같은 규칙

## 4. 매니페스트
```json
{"page":"3-4_relight_with_ai","anchor":"D:grainy-photo-denoise","season":"default","duel":{"result":"R","gap":1.25,"metric":"mean light PSNR dB over 8 cases"},
 "images":[
  {"key":"cover_3-4","plate":"L","size":[1920,1080],"status":"new","priority":"P1","slot":"cover-tall 16:7","fallback":"canvas","alt":"밤의 연구실, 지글거리는 빛의 화면이 AI를 거쳐 매끄러운 그림자로 바뀌는 세 화면 앞에 네 캐릭터가 선 3-4편 표지"},
  {"key":"sc_3-4_outro","plate":"E","size":[1200,800],"status":"new","priority":"P2","slot":"outro","fallback":"canvas","alt":"손 필터, 배운 필터, 정답 세 화면 앞에서 박사가 판정하고, 주판봇이 기뻐하며 초파리 연구원이 커피를 드는 연구실 장면"}
 ]}
```
