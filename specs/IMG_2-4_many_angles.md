# 2-4번 「여러 각도에서 보기」 이미지 제작 명세서

| 항목 | 내용 |
|---|---|
| 페이지 | 2-4_many_angles.html |
| 모드 / 주 앵커 | 교과서 / D 생활·현장: 손전등 그림자, 조각가, 도넛과 그릇 |
| 시즌 | 기본 |
| 대결 | 머그컵 깎기: 둘레 8장 vs 높이까지 바꾼 64장, 겹친 비율(높을수록 좋음) → 결과 D (무승부). 25.4% vs 26.5%, 차이 1.1 (무승부 폭 2 이내 → 초파리 coffee / 주판봇 meh) |
| 새로 그릴 그림 | P1 1장 (cover_2-4) · P2 1장 (sc_2-4_outro) |
| 재사용 | 표정 — 캐릭터 팩 ea5da3f |
| 그림이 없을 때 | 표지·아웃트로는 페이지가 직접 렌더링한 장면 + 팩 캐릭터로 완성 상태 |

## 1. 필요한 그림

| # | 키 | 판 | 상태 | 우선 | 들어가는 곳 | 대신 쓰는 그림 |
|---|---|---|---|---|---|---|
| 0 | cover_2-4 | L 1920×1080 | 새로 (COVER 지시문) | P1 | 첫 화면 (16:7) | 캔버스 |
| 1 | sc_2-4_outro | E 1200×800 | 새로 | P2 | 아웃트로 | 캔버스 |
| 2 | doc_think · doc_front · doc_judge | A | 재사용 | — | 히어로, 등장인물, 판정, 아웃트로 | — |
| 3 | asst_smile · asst_firm · asst_ledger | B | 재사용 | — | 히어로, ①칸, 발표, 꾸러미 | — |
| 4 | fly_point · fly_clip · fly_coffee | C | 재사용 | — | 히어로, ③칸, 대결 후, 아웃트로 | — |
| 5 | robo_coin · robo_smile · robo_calc · robo_meh | D | 재사용 | — | 히어로, ②칸, 대결 후, 아웃트로 | — |

## 2. 새로 그릴 그림 상세 — `sc_2-4_outro`
| 항목 | 내용 |
|---|---|
| 구도 | 벽에 깎은 머그컵 단면 그림 두 장(둘 다 컵 속이 빨갛게 꽉 차 있음). 박사가 두 손을 양쪽으로 펴 무승부 판정. 초파리는 커피를 마시며 여유. 주판봇은 사진기 더미 옆에서 시큰둥. 조수는 다음 미션 머그컵을 들고 웃음 |
| 표정 | doc_judge, fly_coffee, robo_meh, asst_smile |
| 피할 것 | 화면 속 글자·숫자 |
| 대체 글 (alt) | 8장과 64장으로 깎은 머그컵 단면 두 장 앞에서 박사가 무승부를 판정하고, 초파리 연구원이 커피를 마시고 주판봇이 시큰둥한 연구실 장면 |

**프롬프트 (복사해서 사용)**
```
16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights, consistent with the reference images, cozy night laboratory mood, purple light, soft magenta and green fluorescent accents, 3:2 landscape scene, medium brightness, two cross-section drawings of a carved mug pinned on the wall, both with the inside of the cup still filled, the chibi scientist spreading both hands to call a draw, the fruit fly researcher relaxed with coffee, the beige box-shaped robot looking unimpressed beside a pile of cameras, the pink-haired assistant smiling and holding a real mug, no white glossy round robot head, no black pill-shaped visor, no yellow eyes, no ball-shaped antenna knob, no cyan chest light, no floating robot, no gold coins, no text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands.
```

## 3. 체크리스트
- [x] HTML의 `data-img` 키가 1장 표에 있음
- [x] 대결 결과 D → fly_coffee / robo_meh
- [x] 결과 전 그림(표지, 히어로)에 승패 암시 없음, 그림 안 글자 없음

## 4. 매니페스트
```json
{"page":"2-4_many_angles","anchor":"D","season":"default","duel":{"result":"D","gap":1.1,"metric":"voxel IoU % (higher better)"},
 "images":[
  {"key":"cover_2-4","plate":"L","size":[1920,1080],"status":"new","priority":"P1","slot":"cover-tall 16:7","fallback":"canvas","alt":"밤의 연구실, 머그컵 둘레에 사진기 여러 대가 둥글게 놓여 있고, 가운데에는 작은 정육면체 블록 덩어리를 조각칼로 깎아 머그컵 모양을 만드는 2-4편 표지"},
  {"key":"sc_2-4_outro","plate":"E","size":[1200,800],"status":"new","priority":"P2","slot":"outro","fallback":"canvas"}
 ]}
```
