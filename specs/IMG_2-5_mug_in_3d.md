# 2-5번 「머그컵을 3D로」 이미지 제작 명세서

| 항목 | 내용 |
|---|---|
| 페이지 | 2-5_mug_in_3d.html |
| 모드 / 주 앵커 | 교과서 / D 생활·현장: 컵 속에 자 넣기, 유리 탁자, 여러 사람의 증언 |
| 시즌 | 기본 |
| 대결 | 봉인된 새 각도 6개에서 깊이가 맞는 픽셀: 실루엣 8장 + 깊이 4장 vs 실루엣 64장 → 결과 F (초파리 승). 85.4% vs 43.0%, 차이 42.4 (bigGap 5 이상 → 초파리 arms / 주판봇 sigh) |
| 새로 그릴 그림 | P1 1장 (cover_2-5) · P2 1장 (sc_2-5_outro) |
| 재사용 | 표정 — 캐릭터 팩 ea5da3f |
| 그림이 없을 때 | 표지·아웃트로는 페이지가 직접 렌더링한 장면 + 팩 캐릭터로 완성 상태 |

## 1. 필요한 그림

| # | 키 | 판 | 상태 | 우선 | 들어가는 곳 | 대신 쓰는 그림 |
|---|---|---|---|---|---|---|
| 0 | cover_2-5 | L 1920×1080 | 새로 (COVER 지시문) | P1 | 첫 화면 (16:7) | 캔버스 |
| 1 | sc_2-5_outro | E 1200×800 | 새로 | P2 | 아웃트로 | 캔버스 |
| 2 | doc_think · doc_front · doc_judge | A | 재사용 | — | 히어로, 등장인물, 판정, 아웃트로 | — |
| 3 | asst_smile · asst_firm · asst_ledger | B | 재사용 | — | 히어로, ①칸, 발표, 꾸러미 | — |
| 4 | fly_point · fly_clip · fly_arms | C | 재사용 | — | 히어로, ③칸, 대결 후, 아웃트로 | — |
| 5 | robo_coin · robo_smile · robo_calc · robo_sigh | D | 재사용 | — | 히어로, ②칸, 대결 후, 아웃트로 | — |

## 2. 새로 그릴 그림 상세 — `sc_2-5_outro`
| 항목 | 내용 |
|---|---|
| 구도 | 벽에 깎은 머그컵 단면 두 장(왼쪽은 컵 속이 빨갛게 꽉 참, 오른쪽은 컵 속이 비어 있음). 박사가 초파리 쪽으로 손을 들어 판정. 초파리는 팔짱을 끼고 뿌듯. 주판봇은 사진 더미 옆에서 한숨. 조수는 3D 머그컵 모형을 들고 웃음 |
| 표정 | doc_judge, fly_arms, robo_sigh, asst_smile |
| 피할 것 | 화면 속 글자·숫자 |
| 대체 글 (alt) | 실루엣 64장과 실루엣 8장 더하기 깊이 4장으로 깎은 머그컵 단면 두 장 앞에서 박사가 초파리 연구원의 승리를 판정하고, 초파리 연구원이 팔짱을 끼고 주판봇이 한숨 쉬는 연구실 장면 |

**프롬프트 (복사해서 사용)**
```
16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights, consistent with the reference images, cozy night laboratory mood, purple light, soft magenta and green fluorescent accents, 3:2 landscape scene, medium brightness, two cross-section drawings of a mug pinned on the wall, one with the inside filled solid and one correctly hollow, the chibi scientist raising a hand toward the fruit fly researcher who stands proudly with arms crossed, the beige box-shaped robot sighing beside a big pile of photos, the pink-haired assistant smiling and holding a small cube-built mug model, no white glossy round robot head, no black pill-shaped visor, no yellow eyes, no ball-shaped antenna knob, no cyan chest light, no floating robot, no gold coins, no text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands.
```

## 3. 체크리스트
- [x] HTML의 `data-img` 키가 1장 표에 있음
- [x] 대결 결과 F, 큰 차이 → fly_arms / robo_sigh
- [x] 결과 전 그림(표지, 히어로)에 승패 암시 없음, 그림 안 글자 없음

## 4. 매니페스트
```json
{"page":"2-5_mug_in_3d","anchor":"D","season":"default","duel":{"result":"F","gap":42.4,"metric":"held-out view depth accuracy % (higher better)"},
 "images":[
  {"key":"cover_2-5","plate":"L","size":[1920,1080],"status":"new","priority":"P1","slot":"cover-tall 16:7","fallback":"canvas","alt":"밤의 연구실, 유리 탁자 위 머그컵을 위와 아래에서 깊이 카메라가 비추고, 공중에 머그컵의 3D 블록 모형이 컵 속까지 비어 있는 채로 떠오르는 2-5편 표지"},
  {"key":"sc_2-5_outro","plate":"E","size":[1200,800],"status":"new","priority":"P2","slot":"outro","fallback":"canvas"}
 ]}
```
