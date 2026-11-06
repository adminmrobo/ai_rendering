# 시리즈 공용 이미지 명세서 — AI 렌더링 연구실

| 항목 | 내용 |
|---|---|
| 시리즈 | AI 렌더링 연구실, 현재 페이지 1개 (01 렌더링을 거꾸로 돌리면) |
| 시즌 | 기본 |
| 공용 표정 | 18-5 사전 중 이 시리즈에서 쓴 16키. 캐릭터 팩 v1.0 (`adminmrobo/fruitfly-lab-expressions` 커밋 ea5da3f, 96px WebP)과 대조 완료. 16키 모두 있음, 그중 근사 2·대체 1 |

## 1. 공용 표정 현황

팩에 없는 장면(장부, 저울, 계산기)이 꼭 필요해지면 아래 프롬프트로 새로 만든다. 지금은 근사 표정으로 대신한다.

| 키 | 판 | 상태 | 쓰는 페이지 | 얼굴 · 몸짓 (18-5) |
|---|---|---|---|---|
| doc_front | A | 있음 — 팩 doc_e08 | 01 | 눈 감고 활짝 웃음 · 한 손을 들어 앞을 가리킴 |
| doc_think | A | 있음 — 팩 doc_e09 | 01 | 눈썹을 올리고 입을 다묾 · 턱에 손 |
| doc_magic | A | 있음 — 팩 doc_e16 | 01 | 크게 웃음 · 두 손에 보랏빛 불꽃 |
| doc_judge | A | 있음 — 팩 doc_e10 (근사: 윙크 + 엄지 + 체크 표시) | 01 | 눈 감고 웃음 · 옆을 힘 있게 가리킴 |
| asst_smile | B | 있음 — 팩 asst_e13 | 01 | 입꼬리만 살짝 · 가슴 앞에 두 손 |
| asst_firm | B | 있음 — 팩 asst_e12 | 01 | 단단한 눈빛 · 주먹 쥠 |
| asst_spark | B | 있음 — 팩 asst_e01 | 01 | 입 벌려 웃음, 양옆 반짝이 · 두 손을 가슴 앞에 |
| asst_ledger | B | 있음 — 팩 asst_e07 (근사: 장부 그림 없음 → 검지 세워 발표) | 01 | 진지한 눈, 다문 입 · 줄무늬 장부(글자 없음)를 펼치고 펜 |
| fly_clip | C | 있음 — 팩 fly_e10 | 01 | 집중한 눈 · 클립보드에 기록 |
| fly_point | C | 있음 — 팩 fly_e08 | 01 | 한쪽 겹눈을 가늘게 · 오른쪽을 손가락으로 가리킴 |
| fly_cry | C | 있음 — 팩 fly_e21 | 01 | 울며 땀방울 · 두 손을 얼굴에 |
| fly_coffee | C | 있음 — 팩 fly_e13 | 01 | 느긋하게 반쯤 감은 눈 · 커피잔을 듦 |
| robo_smile | D | 있음 — 팩 robo_e13 | 01 | 동그란 눈, 작은 미소 · 두 팔을 내림 |
| robo_coin | D | 있음 — 팩 robo_e16 | 01 | 가늘게 뜬 눈, 히죽 · 금화를 반짝 들어 보임 |
| robo_calc | D | 있음 — 팩 robo_e09 (근사: 톱니바퀴 생각 (계산기 없음)) | 01 | 집중한 눈 · 계산기를 두드림 |
| robo_happy | D | 있음 — 팩 robo_e12 | 01 | 초승달 눈, 활짝 · 두 팔을 듦 |

**표정 프롬프트 틀 (복사 후 { }만 바꿈)**

박사 (A판, 192×192)
```
16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights, consistent with the reference images, cozy night laboratory mood, purple light, soft magenta and green fluorescent accents, single character, transparent background, centered with a small margin, facing front, bust, chibi scientist, round glasses, black hair with one white streak, white lab coat over black vest and tie, {face and pose in English}, no text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands
```
조수 (B판, 180×220): 위 문장에서 캐릭터 부분을 *girl researcher, pink hair in two round buns with a navy streak, blue eyes, white lab coat over lavender hoodie, jeans* 로 바꾼다.
초파리 (C판, 220×220): *facing right, full body, anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat, transparent wings*
Money-Robo (D판, 180×200): *facing left, from antenna to floor shadow, round white floating robot, short antenna, black face screen with yellow pixel eyes, blue chest light, no legs, oval shadow below*

영어 표정 구절: doc_think *eyebrows raised, mouth closed, hand on chin* · doc_magic *big laugh, purple sparks in both hands* · doc_judge *eyes closed smiling, pointing firmly to the side* · asst_firm *determined eyes, fists clenched* · asst_spark *open-mouth smile with sparkles on both sides, both hands in front of chest* · asst_ledger *serious eyes, closed mouth, holding open a striped ledger with blank pages and a pen* · fly_point *one compound eye narrowed, pointing to the right* · fly_cry *crying with sweat drops, both hands on face* · fly_coffee *relaxed half-closed eyes, holding a coffee cup* · robo_coin *narrowed eyes, sly grin, holding up a shiny gold coin* · robo_calc *focused eyes, tapping a small calculator* · robo_happy *crescent eyes, big smile, both arms raised*

## 2. 목차·표지 그림

| 키 | 판 | 내용 | 우선 |
|---|---|---|---|
| cover_index | L | 목차가 생길 때 만든다. 연구실 복도에 방(페이지)이 줄지어 있고, 첫 방 문틈으로 핀홀 상자의 초록 빛이 샌다. 넷이 복도 입구에 함께 섬 | P1 (목차 제작 시) |
| bg_index | F | 같은 복도, 사람 없음 | P2 |
| lineup | G | 넷이 나란히 선 소개 컷, 이름표 자리 비움 | P2 |
| icon_fly, icon_robo, icon_draw, icon_dq | H | 점수판 아이콘: 초파리 머리, 로봇 머리, 저울, 빨간 X | P2 |

## 3. 페이지별 대표 그림 모음

| 페이지 | 앵커 | cover | bg | outro | thumb | 대결 | 상태 |
|---|---|---|---|---|---|---|---|
| 01 렌더링을 거꾸로 돌리면 | D 그림자놀이 작업대 | cover_01 | bg_01 | sc_01_outro | thumb_01 | R | 새로 |

**시리즈 대결 균형:** 01은 R(Money-Robo 승). 다음 편은 초파리 쪽이 이기는 판(F)이나 무승부를 우선 검토한다.

## 4. 매니페스트
```json
{"series":"AI 렌더링 연구실","season":"default",
 "shared":["doc_front","doc_think","doc_magic","doc_judge","asst_smile","asst_firm","asst_spark","asst_ledger","fly_clip","fly_point","fly_cry","fly_coffee","robo_smile","robo_coin","robo_calc","robo_happy"],
 "pages":[{"page":"01_inverse_rendering","anchor":"D","cover":"cover_01","duel":"R"}]}
```
