# 3-2번 「시간이 도와준다」 이미지 제작 명세서

| 항목 | 내용 |
|---|---|
| 페이지 | 3-2_time_helps.html |
| 모드 / 주 앵커 | 교과서 / D 생활·현장: 어두운 곳에서 여러 장 겹치기, 흔들린 사진 |
| 시즌 | 기본 |
| 대결 | 떨어지는 블록, 기억을 다 쓸까 잘라낼까 → 결과 F (초파리 승), 차이 2.88 dB (잘라내기 24.89 vs 다 쓰기 22.01) |
| 새로 그릴 그림 | P1 1장 (cover_3-2) · P2 1장 (sc_3-2_outro) |
| 재사용 | 표정 16장 — 캐릭터 팩 ea5da3f |
| 그림이 없을 때 | 표지·아웃트로는 페이지가 직접 렌더링한 테트리스 장면 + 팩 캐릭터로 완성 상태 |

## 1. 필요한 그림

| # | 키 | 판 | 상태 | 우선 | 들어가는 곳 | 대신 쓰는 그림 |
|---|---|---|---|---|---|---|
| 0 | cover_3-2 | L 1920×1080 | 새로 (COVER_3-2 지시문) | P1 | 3-2 첫 화면 (16:7) | 캔버스 (1·2·4·8·16장 모은 화면) |
| 1 | sc_3-2_outro | E 1200×800 | 새로 | P2 | 아웃트로 | 캔버스 (다 쓰기·잘라내기·정답 세 화면) |
| 2 | doc_think · doc_front · doc_magic · doc_judge | A | 재사용 | — | 히어로, 등장인물, 아웃트로, 판정 | — |
| 3 | asst_smile · asst_firm · asst_ledger | B | 재사용 | — | 히어로, ①칸, 발표, 꾸러미 | — |
| 4 | fly_point · fly_clip · fly_arms | C | 재사용 | — | 히어로, ②칸, 대결 후, 아웃트로 | — |
| 5 | robo_coin · robo_smile · robo_calc · robo_sigh | D | 재사용 | — | 히어로, ③칸, 대결 후, 아웃트로 | — |

## 2. 새로 그릴 그림 상세 — `sc_3-2_outro`
| 항목 | 내용 |
|---|---|
| 구도 | 가운데 위에 모니터 세 대(떨어지는 블록에 꼬리가 남은 화면, 꼬리 없이 깨끗한 화면, 정답 화면). 초파리가 왼쪽 앞에서 가위를 든 채 팔짱(이김). 주판봇은 오른쪽에서 투명한 판 한 아름을 안은 채 어깨를 늘어뜨림(인정, 조롱 없음). 박사는 가운데 뒤에서 보랏빛 불꽃, 조수는 옆에서 미소 |
| 표정 | fly_arms, robo_sigh, doc_magic, asst_smile |
| 피할 것 | 화면 속 글자·숫자, 승자가 패자를 놀리는 몸짓 |
| 대체 글 (alt) | 기억을 다 쓴 화면, 안 맞는 기억을 잘라낸 화면, 정답 화면 세 개 앞에서 초파리 연구원이 팔짱을 끼고, 주판봇이 어깨를 늘어뜨린 연구실 장면 |

**프롬프트 (복사해서 사용)**
```
16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights, consistent with the reference images, cozy night laboratory mood, purple light, soft magenta and green fluorescent accents, 3:2 landscape scene, medium brightness, three monitors in a row in the upper center showing the same Tetris-like game screen with falling blocks: the left one with faint ghostly trails above the falling blocks, the middle one clean without trails, the right one the sharpest reference, blocks with one color per shape (cyan straight, yellow square, purple T, orange L), anthropomorphic fruit fly researcher with a black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat and transparent wings in the front left facing right with arms crossed proudly and a pair of scissors in one hand, small boxy retro computer robot with a beige rounded-corner CRT-monitor head, a dark green screen face with mint pixel eyes and mouth, a thin antenna topped with one small red-brown abacus bead, chunky gray segmented arms with round gray mitten hands and two dark gray tank treads, about three quarters the height of the scientist, on the right facing left hugging a stack of translucent panels with drooping arms, chibi scientist with round glasses, black hair with one white streak, white lab coat over black vest and tie at the back center with purple sparks in both hands, girl researcher with pink hair in two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie smiling at the side, no white glossy round robot head, no black pill-shaped visor, no yellow eyes, no ball-shaped antenna knob, no cyan chest light, no floating robot, no gold coins, no text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands
```

## 3. 체크리스트
- [x] HTML의 `data-img` 키 16개가 1장 표에 있음
- [x] 대결 F → fly_arms, robo_sigh, asst_spark, doc_judge
- [x] 결과 전 그림(표지, 히어로)에 승패 암시 없음, 그림 안 글자 없음
- [x] 화면 속 블록 색은 1부·3-1과 같은 규칙

## 4. 매니페스트
```json
{"page":"3-2_time_helps","anchor":"D:stacked-frames","season":"default","duel":{"result":"F","gap":2.88,"metric":"PSNR dB"},
 "images":[
  {"key":"cover_3-2","plate":"L","size":[1920,1080],"status":"new","priority":"P1","slot":"cover-tall 16:7","fallback":"canvas","alt":"밤의 연구실, 같은 게임 화면이 여러 장 겹쳐 쌓이며 점점 선명해지고, 떨어지는 블록에는 화살표(모션 벡터)가 붙은 앞에 네 캐릭터가 선 3-2편 표지"},
  {"key":"sc_3-2_outro","plate":"E","size":[1200,800],"status":"new","priority":"P2","slot":"outro","fallback":"canvas","alt":"기억을 다 쓴 화면, 안 맞는 기억을 잘라낸 화면, 정답 화면 세 개 앞에서 초파리 연구원이 팔짱을 끼고, 주판봇이 어깨를 늘어뜨린 연구실 장면"}
 ]}
```
