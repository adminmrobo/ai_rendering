# 1-1번 「정답표가 없으면 어떻게 배우지?」 이미지 제작 명세서

| 항목 | 내용 |
|---|---|
| 페이지 | 1-1_learning_without_labels.html (1부 목차 index.html 포함) |
| 모드 / 주 앵커 | 교과서 / D 생활·현장: 테트리스 블록 정리 작업대 |
| 시즌 | 기본 |
| 대결 | 이름표 4장 값으로 테트리스 블록 정리하기 → 결과 F (초파리 승), 차이 16.2%p (97.2% vs 81.0%) |
| 새로 그릴 그림 | P1 1장 (cover_ch1) · P2 2장 (sc_1-1_outro, thumb_1-1) · P3 0장 |
| 재사용 | 표정 16장 — 캐릭터 팩 ea5da3f (96px WebP)를 페이지에 base64로 넣음 |
| 그림이 없을 때 | 표지·아웃트로는 캔버스(픽셀 테트리스 블록·주머니 + 캐릭터 팩 그림)로 이미 완성 상태 |

## 1. 그림체와 고정 외형
- 스타일·외형: SKILL 18-3, 18-4 / 기준: 캐릭터 팩 `adminmrobo/fruitfly-lab-expressions`
- 이 페이지 장소: 밤의 연구실 작업대 — 테트리스 블록 더미(막대 하늘·네모 노랑·T자 보라, 같은 모양 같은 색), 천 주머니, 이름표 없는 사진. 현미경·초파리 해부 소품 없음
- 장소 영어 묘사: *a big workbench inside the same night lab world, a pile of large Tetris-style blocks in random orientations (cyan straight pieces, yellow squares, purple T pieces, same shape same color), open cloth drawstring pouches, a stack of unlabeled portrait photos, purple lab light from one side*

## 2. 필요한 그림 전체

| # | 키 | 판 | 크기 | 상태 | 우선 | 들어가는 곳 | 대신 쓰는 그림 |
|---|---|---|---|---|---|---|---|
| 0 | cover_ch1 | L | 1920×1080 | 새로 (COVER_ch1_learning_without_labels.md) | P1 | 1부 목차 큰 표지, 1-1~1-5 띠 | 캔버스 대체 표지 |
| 1 | sc_1-1_outro | E | 1200×800 | 새로 | P2 | 아웃트로 | 캔버스 장면 |
| 2 | thumb_1-1 | I | 600×400 | 새로 (cover_ch1 3:2 자르기) | P2 | 1부 목차 카드 (현재 글 카드) | 글 카드 |
| 3 | doc_think · doc_front · doc_magic · doc_judge | A | 96 (팩) | 재사용 (팩 e09·e08·e16·e10) | — | 히어로, 등장인물, 아웃트로, 판정 | — |
| 4 | asst_smile · asst_firm · asst_spark · asst_ledger | B | 96 (팩) | 재사용 (팩 e13·e12·e01·e07) | — | 히어로, 결과 발표, ③칸, 꾸러미 | — |
| 5 | fly_point · fly_clip · fly_arms | C | 96 (팩) | 재사용 (팩 e08·e10·e16) | — | 히어로, ②칸, 대결 전후, 아웃트로 | — |
| 6 | robo_coin · robo_smile · robo_calc · robo_sigh | D | 96 (팩) | 재사용 (팩 e16·e13·e09·e20) | — | 히어로, ①칸, 대결 전후, 아웃트로 | — |
| — | ③칸 얼굴 그림 24장 | — | 32×32 | 팩에서 만듦 (네 캐릭터 × e01·e02·e04·e07·e09·e13) | — | ③칸 실험 데이터 | — |
| — | 행동으로 보기 ①~③ | — | — | 코드 | — | 캔버스 | — |

## 3. 새로 그릴 그림 상세

### 3-1. `cover_ch1` — COVER_ch1_learning_without_labels.md에 지시문 전체

### 3-2. `sc_1-1_outro` — 주머니 세 개와 초파리의 승리
| 항목 | 내용 |
|---|---|
| 판 · 크기 | E · 1200×800 |
| 구도 | 가운데 위에 천 주머니 세 개(하늘색 막대만, 노란 네모만, 보라 T자만 가지런히). 초파리가 왼쪽 앞에서 팔짱(이김), 주판봇은 오른쪽에서 빈 이름표 한 장을 들고 어깨를 늘어뜨림(인정, 조롱 없음), 박사는 가운데 뒤에서 두 손에 보랏빛 불꽃, 조수는 옆에서 미소 |
| 표정 | fly_arms, robo_sigh, doc_magic, asst_smile |
| 피할 것 | 글자(이름표는 빈칸), 승자가 패자를 놀리는 몸짓 |
| 대체 글 (alt) | 초파리 연구원이 세 주머니로 정리된 테트리스 블록 앞에서 팔짱을 끼고, 주판봇이 옆에서 남은 이름표 한 장을 들고 있는 연구실 장면 |

**프롬프트 (복사해서 사용)**
```
16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights, consistent with the reference images, cozy night laboratory mood, purple light, soft magenta and green fluorescent accents, 3:2 landscape scene, medium brightness, three open cloth drawstring pouches in the upper center, one holding only cyan straight Tetris pieces, one only yellow square pieces, one only purple T pieces, anthropomorphic fruit fly researcher with a black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat and transparent wings in the front left facing right with arms crossed proudly, small boxy retro computer robot with a beige rounded-corner CRT-monitor head, a dark green screen face with mint pixel eyes and mouth, a thin antenna topped with one small red-brown abacus bead, chunky gray segmented arms with round gray mitten hands and two dark gray tank treads, about three quarters the height of the scientist, on the right facing left holding one blank tag with drooping arms, chibi scientist with round glasses, black hair with one white streak, white lab coat over black vest and tie at the back center with purple sparks in both hands, girl researcher with pink hair in two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie smiling at the side, no white glossy round robot head, no black pill-shaped visor, no yellow eyes, no ball-shaped antenna knob, no cyan chest light, no floating robot, no gold coins, no text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands
```

## 4. 일관성 지침
- 참고 이미지: 팩 기본 표정(e13) 4장. 같은 캐릭터는 같은 세션에서 만든다.
- 표정만 바꿀 때: *same character, same size and position, only change the facial expression and pose to ...*

## 5. 넘겨받은 뒤 처리
1. 표지: SKILL 18-15 (16:9 확인 → WebP 1600×900 → index는 큰 표지, 각 편은 띠)
2. 아웃트로: WebP 너비 760 → `data-img="sc_1-1_outro"` 자리(지금은 캔버스)에 넣는다
3. 페이지 그림 합계: 표정 약 139 KB + 얼굴 데이터 98 KB, 표지 포함 600 KB 이하 유지

## 6. 체크리스트
- [x] HTML의 `data-img` 키 17개가 2장 표에 있음
- [x] 대결 F (16.2%p) → fly_arms, robo_sigh (차이 10%p 이상이지만 진 쪽이 로봇이라 sigh), asst_spark, doc_judge
- [x] 결과 전 그림(표지, 히어로)에 승패 암시 없음
- [x] 그림 안 글자 없음 (이름표는 빈칸)
- [x] 장소가 D 앵커, 현미경 소품 없음

## 7. 매니페스트
```json
{"page":"1-1_learning_without_labels","anchor":"D:tetris-workbench","season":"default","duel":{"result":"F","gap":16.2,"metric":"accuracy %"},
 "images":[
  {"key":"cover_ch1","plate":"L","size":[1920,1080],"status":"new","priority":"P1","slot":"cover (index) / cover-tall (1-1)","fallback":"canvas","alt":"밤의 연구실에서 네 캐릭터가 쏟아진 테트리스 블록 더미와 이름표 없는 사진 더미를 정리하는 1부 표지"},
  {"key":"sc_1-1_outro","plate":"E","size":[1200,800],"status":"new","priority":"P2","slot":"outro","fallback":"canvas","alt":"초파리 연구원이 세 주머니로 정리된 테트리스 블록 앞에서 팔짱을 끼고, 주판봇이 옆에서 남은 이름표 한 장을 들고 있는 연구실 장면"},
  {"key":"thumb_1-1","plate":"I","size":[600,400],"status":"new-crop","priority":"P2","slot":"index-card","fallback":"text-card"},
  {"key":"faces32","plate":"-","size":[32,32],"status":"derived-from-pack","slot":"lv3-data","count":24}
 ]}
```
