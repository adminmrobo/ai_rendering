# 01번 「렌더링을 거꾸로 돌리면 — 정답표 없이 배우는 AI 렌더링」 이미지 제작 명세서

| 항목 | 내용 |
|---|---|
| 페이지 | 01_inverse_rendering.html |
| 모드 / 주 앵커 | 교과서 / D 생활·현장: 그림자놀이 작업대 (연구실 안) |
| 시즌 | 기본 |
| 대결 | 움직이는 화면, 한 장을 잘 키울까 네 장을 모을까? → 결과 R (Money-Robo 승), 차이 24.49 dB (35.51 vs 60.00) |
| 새로 그릴 그림 | P1 1장 (cover_01) · P2 2장 (sc_01_outro, thumb_01) · P3 2장 (bg_01, og_01) |
| 재사용 | 표정 16장 + 대결 대비 6장 = 22장, 캐릭터 팩 ea5da3f(96px WebP)를 페이지에 base64로 넣음 (합계 약 139 KB) |
| 그림이 없을 때 | 페이지는 픽셀 지도와 CSS·캔버스 배경으로 이미 완성 상태 |

## 1. 그림체와 고정 외형
- 스타일: SKILL 18-3 (16비트 RPG 픽셀아트, 굵은 외곽선, 2~3단계 명암)
- 캐릭터 고정 외형: SKILL 18-4 표 그대로 (기준 저장소 `adminmrobo/fruitfly-lab-expressions`)
- 이 페이지 장소: 밤의 연구실 한쪽의 그림자놀이 작업대 — 손전등, 핀홀 카메라 상자, 유리컵, 벽에 거꾸로 맺힌 상. 생물 앵커가 아니므로 현미경·초파리 해부 소품은 넣지 않는다
- 장소 영어 묘사: *a shadow-play workbench rendered as part of the same night lab world, a small flashlight, a dark pinhole camera box, a clear glass cup, an upside-down blurry image on the wall, purple lab light spilling in from one side*

## 2. 필요한 그림 전체

| # | 키 | 판 | 크기 | 상태 | 우선 | 들어가는 곳 | 대신 쓰는 그림 |
|---|---|---|---|---|---|---|---|
| 0 | cover_01 | L | 1920×1080 | 새로 (COVER_01_inverse_rendering.md) | P1 | 맨 위 글 표지 | 대체 표지 (캔버스 + 픽셀 넷) |
| 1 | bg_01 | F | 1920×720 | 새로 | P3 (표지 있음) | 히어로 오른쪽 배경 | 핀홀 픽셀 애니메이션 (코드) |
| 2 | doc_think | A | 192×192 | 재사용 (팩) | — | 히어로 대화창 | doc_front |
| 3 | asst_smile | B | 180×220 | 재사용 (팩) | — | 히어로 대화창, 등장인물 | — |
| 4 | fly_point | C | 220×220 | 재사용 (팩) | — | 히어로, ②칸 말풍선, 대결 전 | fly_clip |
| 5 | robo_coin | D | 180×200 | 재사용 (팩) | — | 히어로, 대결 전 | robo_smile |
| 6 | doc_front | A | 192×192 | 재사용 (팩) | — | 등장인물 | — |
| 7 | fly_clip | C | 220×220 | 재사용 (팩) | — | 등장인물 | — |
| 8 | robo_smile | D | 180×200 | 재사용 (팩) | — | 등장인물 | — |
| 9 | asst_firm | B | 180×220 | 재사용 (팩) | — | ①칸 말풍선, 결과 발표 전 | asst_smile |
| 10 | robo_calc | D | 180×200 | 재사용 (팩) | — | ④칸 말풍선 | robo_smile |
| 11 | doc_magic | A | 192×192 | 재사용 (팩) | — | ⑤칸 "박사의 한 줄", 아웃트로 | doc_front |
| 12 | fly_cry | C | 220×220 | 재사용 (팩) | — | 대결 후 (차이 10 이상) — 스크립트가 바꿈 | fly_coffee |
| 13 | robo_happy | D | 180×200 | 재사용 (팩) | — | 대결 후, 아웃트로 | robo_smile |
| 14 | asst_spark | B | 180×220 | 재사용 (팩) | — | 대결 후 발표, 아웃트로 | asst_smile |
| 15 | doc_judge | A | 192×192 | 재사용 (팩) | — | 대결 판정 | doc_front |
| 16 | fly_coffee | C | 220×220 | 재사용 (팩) | — | 아웃트로 (인정) | fly_clip |
| 17 | asst_ledger | B | 180×220 | 재사용 (팩) | — | 꾸러미 섹션 | asst_firm |
| 18 | sc_01_outro | E | 1200×800 | 새로 | P2 | 아웃트로 장면 | 픽셀 캐릭터 + 겹친 프레임 (캔버스) |
| 19 | thumb_01 | I | 600×400 | 새로 (cover_01 3:2 자르기) | P2 | 목차 카드 (페이지 밖) | 색 카드 |
| 20 | og_01 | K | 1200×630 | 새로 (cover_01 자르기) | P3 | 공유 미리보기 (페이지 밖) | 없음 |
| — | 행동으로 보기 ①~⑤, 대결 막대 | — | — | 코드 | — | 캔버스 | — |

히어로 무대(R2 `sc_01_hero`)와 본문 컷(R5)은 이 페이지에 자리가 없어 만들지 않는다. 사다리 칸마다 캔버스 실험이 그 역할을 한다.

## 3. 새로 그릴 그림 상세

### 3-1. `cover_01` — 네 캐릭터와 거꾸로 맺힌 컵
COVER_01_inverse_rendering.md에 지시문 전체가 있다.

### 3-2. `bg_01` — 그림자놀이 작업대 (사람 없음)
| 항목 | 내용 |
|---|---|
| 판 · 크기 | F · 1920×720 (정수배 가능) |
| 배경 | 그림 전체 |
| 구도 | 왼쪽 45%는 어둡고 단순(제목이 얹힘). 오른쪽에 작업대: 유리컵 → 핀홀 상자 → 벽의 거꾸로 된 상 |
| 소품 | 손전등, 핀홀 상자, 유리컵, 벽의 흐린 상, 빈 액자 (글자 없음) |
| 빛·분위기 | 남보라 어둠, 핀홀에서 새는 초록 점, 광선은 옅은 분홍 |
| 피할 것 | 캐릭터, 글자, 현미경 |
| 대체 글 (alt) | 핀홀 카메라가 유리컵을 벽에 거꾸로 맺는 밤의 연구실 작업대 |
| 대신 쓰는 그림 | 핀홀 픽셀 애니메이션 (코드) |

**프롬프트 (복사해서 사용)**
```
16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights, consistent with the reference images, cozy night laboratory mood, purple light, soft magenta and green fluorescent accents, wide 8:3 background, left side simple and calm for title text, details on the right, a shadow-play workbench rendered as part of the same night lab world, a small flashlight, a dark pinhole camera box with a tiny glowing green hole, a clear glass cup, faint pink light rays passing through the pinhole, an upside-down blurry image of the cup on the wall and an empty picture frame beside it, purple lab light spilling in from the left, no characters, no text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands
```

### 3-3. `sc_01_outro` — 네 장의 프레임과 Money-Robo의 승리
| 항목 | 내용 |
|---|---|
| 판 · 크기 | E · 1200×800 |
| 배경 | 그림 전체 |
| 구도 | 가운데 위에 반투명한 파란 사각 프레임 네 장이 살짝 비켜 겹쳐 떠 있음. Money-Robo가 오른쪽 앞에 크게(두 팔을 듦), 초파리는 왼쪽 뒤에서 커피잔을 들고 고개를 끄덕임(인정), 박사는 가운데에서 두 손에 보랏빛 불꽃, 조수는 박사 옆에서 반짝이며 웃음 |
| 표정·몸짓 | robo_happy, fly_coffee, doc_magic, asst_spark (18-5) |
| 소품 | 겹친 프레임 네 장, 그 위를 지나는 짧은 초록 화살표(모션 벡터 은유) — 글자 없음 |
| 빛·분위기 | 프레임에서 나오는 파란 빛, 연구실 보라 조명 |
| 피할 것 | 초파리를 조롱하는 연출, 글자, 실존 게임 화면·그래픽카드 브랜드 |
| 대체 글 (alt) | Money-Robo가 앞에서 두 팔을 들고, 초파리 연구원이 뒤에서 고개를 끄덕이며, 박사와 조수가 겹쳐진 프레임 네 장을 바라보는 연구실 장면 |
| 대신 쓰는 그림 | 캔버스 픽셀 장면 |

**프롬프트 (복사해서 사용)**
```
16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights, consistent with the reference images, cozy night laboratory mood, purple light, soft magenta and green fluorescent accents, 3:2 landscape scene, medium brightness, four translucent blue rectangular frames floating and slightly offset over each other in the upper center with short green arrows sliding them into place, round white floating robot with a short antenna, black face screen with yellow pixel eyes and a blue chest light, no legs, oval shadow below, in the front right, larger, facing left, raising both arms happily, anthropomorphic fruit fly researcher with a black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat and transparent wings at the back left, facing right, holding a coffee cup and nodding calmly, chibi scientist with round glasses, black hair with one white streak, white lab coat over black vest and tie in the center with purple sparks in both hands, girl researcher with pink hair in two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie and jeans beside him smiling with sparkles, no text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands
```

### 3-4. `thumb_01`, `og_01`
cover_01을 받으면 thumb_01은 3:2(600×400, 네 캐릭터 얼굴이 모두 들어가게 가운데 기준), og_01은 1200×630으로 자른다. 새로 그리지 않는다. 대체 글: "네 캐릭터와 핀홀 상자, 거꾸로 맺힌 컵".

## 4. 일관성 지침
- 참고 이미지: `adminmrobo/fruitfly-lab-expressions`의 기본 그림 4장 (없으면 cover_01이 이후의 기준)
- 같은 캐릭터는 같은 세션에서, 시드 고정 가능하면 고정
- 표정만 바꿀 때: *same character, same size and position, only change the facial expression and pose to ...*
- 투명 배경이 안 되면: *solid flat #00ff00 background*

## 5. 넘겨받은 뒤 처리
1. 크기·투명 배경 확인, 단색 배경 제거
2. 빌드 크기로 줄이고 WebP 압축 (18-2 "빌드 후 크기")
3. 표정은 64×64로 줄여 기존 표정과 나란히 비교
4. `data-img` 키 자리에 넣는다 — 표정은 스크립트의 `SPRITE` 객체에 `'fly_point':'data:image/webp;base64,...'` 형태로, 장면은 해당 `div`의 배경으로. 그림 합계 표지 제외 400 KB, 표지 포함 600 KB 이하
5. 표지는 SKILL 18-15 절차

## 6. 체크리스트
- [x] HTML의 모든 `data-img` 키(18개)가 2장 표에 있고, fly_cry는 대결 스크립트가 바꾸는 키로 함께 적음
- [x] 대결 결과 후 표정이 5-8절과 일치 (R, 차이 10 이상 → fly_cry, robo_happy, asst_spark, doc_judge)
- [x] 결과 전 그림(cover_01, 히어로 표정)에 승패 암시 없음
- [x] 모든 프롬프트에 18-4 고정 외형 영어 묘사와 금지 구절
- [x] 장소가 D 앵커와 일치, 현미경·해부 소품 없음
- [x] P1 1장 (표지)
- [x] 표정 그림 합계 약 139 KB (표지 제외 400 KB 이하)
- 근사 표정: doc_judge → doc_e10(윙크·엄지), robo_calc → robo_e09(톱니 생각), asst_ledger → asst_e07(검지 세워 발표, 장부 그림 없음)

## 7. 매니페스트
```json
{
  "page": "01_inverse_rendering",
  "anchor": "D:shadow-play-workbench",
  "season": "default",
  "duel": {"result": "R", "gap": 24.49, "metric": "PSNR dB"},
  "images": [
    {"key":"cover_01","plate":"L","size":[1920,1080],"status":"new","priority":"P1","slot":"cover","fallback":"canvas-pixel-four","alt":"밤의 연구실에서 네 캐릭터가 유리컵과 핀홀 상자, 벽에 거꾸로 맺힌 컵의 상을 둘러싸고 바라보는 표지"},
    {"key":"bg_01","plate":"F","size":[1920,720],"status":"new","priority":"P3","slot":"hero-bg","fallback":"code-pinhole","alt":"핀홀 카메라가 유리컵을 벽에 거꾸로 맺는 밤의 연구실 작업대"},
    {"key":"sc_01_outro","plate":"E","size":[1200,800],"status":"new","priority":"P2","slot":"outro","fallback":"canvas-pixel-scene","alt":"Money-Robo가 앞에서 두 팔을 들고, 초파리 연구원이 뒤에서 고개를 끄덕이며, 박사와 조수가 겹쳐진 프레임 네 장을 바라보는 연구실 장면"},
    {"key":"thumb_01","plate":"I","size":[600,400],"status":"new-crop","priority":"P2","slot":"index-card","fallback":"color-card","alt":"네 캐릭터와 핀홀 상자, 거꾸로 맺힌 컵"},
    {"key":"og_01","plate":"K","size":[1200,630],"status":"new-crop","priority":"P3","slot":"og","fallback":"none","alt":"네 캐릭터와 핀홀 상자, 거꾸로 맺힌 컵"},
    {"key":"doc_think","plate":"A","status":"reuse-pack","slot":"hero-dialog","fallback":"doc_front","alt":""},
    {"key":"doc_front","plate":"A","status":"reuse-pack","slot":"cast","alt":""},
    {"key":"doc_magic","plate":"A","status":"reuse-pack","slot":"lv5,outro","fallback":"doc_front","alt":""},
    {"key":"doc_judge","plate":"A","status":"reuse-pack","slot":"duel-after","fallback":"doc_front","alt":""},
    {"key":"asst_smile","plate":"B","status":"reuse-pack","slot":"hero-dialog,cast","alt":""},
    {"key":"asst_firm","plate":"B","status":"reuse-pack","slot":"lv1,duel-before","fallback":"asst_smile","alt":""},
    {"key":"asst_spark","plate":"B","status":"reuse-pack","slot":"duel-after,outro","fallback":"asst_smile","alt":""},
    {"key":"asst_ledger","plate":"B","status":"reuse-pack","slot":"export","fallback":"asst_firm","alt":""},
    {"key":"fly_point","plate":"C","status":"reuse-pack","slot":"hero-dialog,lv2,duel-before","fallback":"fly_clip","alt":""},
    {"key":"fly_clip","plate":"C","status":"reuse-pack","slot":"cast","alt":""},
    {"key":"fly_cry","plate":"C","status":"reuse-pack","slot":"duel-after","fallback":"fly_coffee","alt":""},
    {"key":"fly_coffee","plate":"C","status":"reuse-pack","slot":"outro","fallback":"fly_clip","alt":""},
    {"key":"robo_coin","plate":"D","status":"reuse-pack","slot":"hero-dialog,duel-before","fallback":"robo_smile","alt":""},
    {"key":"robo_smile","plate":"D","status":"reuse-pack","slot":"cast","alt":""},
    {"key":"robo_calc","plate":"D","status":"reuse-pack","slot":"lv4","fallback":"robo_smile","alt":""},
    {"key":"robo_happy","plate":"D","status":"reuse-pack","slot":"duel-after,outro","fallback":"robo_smile","alt":""}
  ]
}
```
