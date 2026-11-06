# 표지 지시문 — 01 렌더링을 거꾸로 돌리면

| 항목 | 내용 |
|---|---|
| 키 · 판 | cover_01 · L (16:9, 가로 1920 이상) |
| 장소 (앵커) | D 생활·현장 — 같은 밤의 연구실 안 "그림자놀이 작업대": 손전등, 핀홀 카메라 상자, 유리컵, 벽에 비친 거꾸로 된 상 |
| 주제 은유 | 유리컵 → 핀홀 상자 → 벽에 거꾸로 맺힌 흐린 상. 그 상 옆에 빈 액자 하나(“사진 = 채점표”), 상과 액자 사이를 잇는 초록 점선 화살표가 컵 쪽으로 되돌아간다 (렌더링을 거꾸로) |
| 네 캐릭터 포즈 | 박사: 가운데 뒤, 턱에 손을 대고 벽의 상을 올려다봄 / 조수: 오른쪽 옆, 카메라를 들고 다른 각도에서 컵을 찍으려 함 / 초파리: 왼쪽에서 오른쪽을 보며 한쪽 겹눈을 가늘게 뜨고 벽의 상을 손가락으로 가리킴 / Money-Robo: 오른쪽에서 왼쪽을 보며 금화 하나를 들고 핀홀 상자를 바라봄 |
| 대체 글 (alt) | 밤의 연구실에서 네 캐릭터가 유리컵과 핀홀 상자, 벽에 거꾸로 맺힌 컵의 상을 둘러싸고 바라보는 표지 |
| 앞 표지와 다른 점 | 시리즈 첫 표지 (앞 표지 없음). 이후 표지는 작업대·핀홀 상자 구도를 피한다 |

**참고 이미지 (함께 올리기):** 네 캐릭터 기본 그림 4장 (기준: GitHub `adminmrobo/fruitfly-lab-expressions`). 없으면 이 표지가 이후의 기준이 된다.

**Genspark에 붙여 넣기 ↓**
```
웹페이지 맨 위에 거는 표지 그림 1장을 만들어 줘.
- 비율 16:9, 가로 1920px 이상
- 첨부한 참고 이미지의 네 캐릭터(박사, 조수, 초파리 연구원, Money-Robo)를 같은 그림체·같은 외형으로, 넷 모두 등장
- 그림 안에 글자·숫자·로고를 넣지 말 것
- 얼굴과 손은 가장자리에서 떨어진 가운데 영역에, 왼쪽 아래 구석은 어둡고 단순하게
아래 영어 프롬프트를 그대로 써 줘.

Website top cover illustration, wide 16:9.
Match the art style, proportions and colors of the attached reference images exactly
(if there are no reference images: 16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights).
Cozy night laboratory mood, purple light, soft magenta and green fluorescent accents.
Scene: a shadow-play workbench rendered as part of the same night lab world, a small flashlight, a dark pinhole camera box with a tiny glowing green hole, a clear glass cup on the bench, and on the wall behind an upside-down blurry image of the cup, next to it an empty picture frame, a dotted green arrow loops from the frame back toward the cup, purple lab light spilling in from one side.
All four characters together:
  chibi scientist, round glasses, black hair with one white streak, white lab coat over black vest and tie, standing at the back center with a hand on his chin, looking up at the upside-down image;
  girl researcher, pink hair in two round buns with a navy streak, blue eyes, white lab coat over lavender hoodie, jeans, at the right side holding a small camera to photograph the cup from another angle;
  anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat, transparent wings, on the left facing right, one eye narrowed, pointing at the image on the wall;
  round white floating robot, short antenna, black face screen with yellow pixel eyes, blue chest light, no legs, oval shadow below, on the right facing left, holding up one shiny gold coin and looking at the pinhole box.
Visual metaphor of the topic: light goes from the cup through the pinhole to an upside-down image, and a dotted arrow goes back from the image to the cup (rendering in reverse), no text.
Composition: keep every face and hand inside the central safe area (12% margin left and right, 10% top, 18% bottom);
  keep the bottom-left corner dark and simple; the light falls on the glass cup and the pinhole.
Mood: curious, friendly rivalry, the moment before the result.
No text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands.
```

**고칠 때 (같은 대화에서):** `Same four characters, same art style and composition. Change only: {고칠 점}. Still no text.`

**받은 뒤:** SKILL 18-15 절차 — 16:9·가로 1600 이상·글자 없음·네 캐릭터 외형 확인 → WebP 1600×900(220 KB 이하) → HTML의 `<!-- lab-cover -->` 사이 `data-img="cover_01"` 자리에 넣고 390·768·1280 폭 점검.
