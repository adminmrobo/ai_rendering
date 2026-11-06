# 2-3번 「계단과 미끄럼틀」 이미지 제작 명세서

| 항목 | 내용 |
|---|---|
| 페이지 | 2-3_stairs_and_slides.html |
| 모드 / 주 앵커 | 교과서 / D 생활·현장: 계단 위의 공, 흐린 안경, 안개 낀 산 |
| 시즌 | 기본 |
| 대결 | 같은 계산 시간으로 숫자 넷 찾기: 다듬기 60장 vs 미끄럼 40걸음, 마지막 어긋남(낮을수록 좋음) → 결과 R (주판봇 승). 3.3% vs 2.2%, 차이 1.1 (무승부 폭 0.5 초과, bigGap 5 미만 → 초파리 coffee) |
| 새로 그릴 그림 | P1 1장 (cover_2-3) · P2 1장 (sc_2-3_outro) |
| 재사용 | 표정 — 캐릭터 팩 ea5da3f |
| 그림이 없을 때 | 표지·아웃트로는 페이지가 직접 렌더링한 장면 + 팩 캐릭터로 완성 상태 |

## 1. 필요한 그림

| # | 키 | 판 | 상태 | 우선 | 들어가는 곳 | 대신 쓰는 그림 |
|---|---|---|---|---|---|---|
| 0 | cover_2-3 | L 1920×1080 | 새로 (COVER 지시문) | P1 | 첫 화면 (16:7) | 캔버스 |
| 1 | sc_2-3_outro | E 1200×800 | 새로 | P2 | 아웃트로 | 캔버스 |
| 2 | doc_think · doc_front · doc_judge | A | 재사용 | — | 히어로, 등장인물, 판정, 아웃트로 | — |
| 3 | asst_smile · asst_firm · asst_ledger | B | 재사용 | — | 히어로, ①칸, 발표, 꾸러미 | — |
| 4 | fly_point · fly_clip · fly_coffee | C | 재사용 | — | 히어로, ③칸, 대결 후, 아웃트로 | — |
| 5 | robo_coin · robo_smile · robo_calc · robo_happy | D | 재사용 | — | 히어로, ②칸, 대결 후, 아웃트로 | — |

## 2. 새로 그릴 그림 상세 — `sc_2-3_outro`
| 항목 | 내용 |
|---|---|
| 구도 | 벽에 다듬기로 찾은 몽타주와 미끄럼으로 찾은 몽타주 두 장(둘 다 사진과 닮았지만 미끄럼 쪽이 조금 더 잘 맞음). 박사가 주판봇 쪽으로 손을 들어 판정. 주판봇은 미끄럼틀 모형 옆에서 기뻐함. 초파리는 커피를 마시며 고개를 끄덕임. 조수는 옆에서 웃음 |
| 표정 | doc_judge, robo_happy, fly_coffee, asst_smile |
| 피할 것 | 화면 속 글자·숫자 |
| 대체 글 (alt) | 다듬기 60장과 미끄럼 40걸음으로 찾은 몽타주 두 장 앞에서 박사가 주판봇의 승리를 판정하고, 초파리 연구원이 커피를 마시며 고개를 끄덕이고 주판봇이 기뻐하는 연구실 장면 |

**프롬프트 (복사해서 사용)**
```
16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights, consistent with the reference images, cozy night laboratory mood, purple light, soft magenta and green fluorescent accents, 3:2 landscape scene, medium brightness, two cup sketches pinned on the wall that both nearly match a white cup silhouette, the chibi scientist raising a hand toward the beige box-shaped robot who cheers beside a small slide model with a rolling marble, the fruit fly researcher calmly sipping coffee and nodding, the pink-haired assistant smiling, no white glossy round robot head, no black pill-shaped visor, no yellow eyes, no ball-shaped antenna knob, no cyan chest light, no floating robot, no gold coins, no text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands.
```

## 3. 체크리스트
- [x] HTML의 `data-img` 키가 1장 표에 있음
- [x] 대결 결과 R, 차이 1.1 → fly_coffee / robo_happy (작은 차이 규칙)
- [x] 결과 전 그림(표지, 히어로)에 승패 암시 없음, 그림 안 글자 없음

## 4. 매니페스트
```json
{"page":"2-3_stairs_and_slides","anchor":"D","season":"default","duel":{"result":"R","gap":1.1,"metric":"silhouette mismatch % (lower better)"},
 "images":[
  {"key":"cover_2-3","plate":"L","size":[1920,1080],"status":"new","priority":"P1","slot":"cover-tall 16:7","fallback":"canvas","alt":"밤의 연구실, 한쪽에는 공이 멈춰 선 계단 모양 그래프, 다른 쪽에는 공이 굴러 내려가는 미끄럼틀 모양 그래프가 붙어 있고 네 캐릭터가 번진 컵 실루엣을 들여다보는 2-3편 표지"},
  {"key":"sc_2-3_outro","plate":"E","size":[1200,800],"status":"new","priority":"P2","slot":"outro","fallback":"canvas"}
 ]}
```
