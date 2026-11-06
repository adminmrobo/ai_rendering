# 목차(index) 맨 위 표지 — 정사각 1280×1280 지시문 3장

AI 렌더링 연구실 1·2·3부 목차(`partN/index.html`) 맨 위 `data-img="cover_chN"` 자리에 넣는 그림입니다.

**넣을 때 주의:** 목차 표지 칸은 가로 16:9이고 그림을 가득 채워 자릅니다(`object-fit: cover`, 중심 50%·40%). 그래서 정사각 그림은 **위아래가 약 22%씩 잘리고 가운데 가로 띠만** 보입니다. 아래 프롬프트는 네 캐릭터의 얼굴·손과 주요 소품을 모두 **세로 25~75% 띠 안**에 두도록 썼습니다. 잘리는 위아래는 하늘·벽·작업대처럼 비어도 되는 배경으로 채웁니다.

**공통 참고 이미지 (함께 올리기):** 캐릭터 팩 기본 그림 4장 — `doc_e13`, `asst_e13`, `fly_e13`, 주판봇 `images/jupanbot/E13_neutral.png` (adminmrobo/fruitfly-lab-expressions, 커밋 5269662 — 2026-11-05 새 픽셀 그림).

**받은 뒤:** 1:1·글자 없음·네 캐릭터 외형 확인 → WebP 1280×1280 (260 KB 이하) → 해당 `index.html`의 `data-img="cover_chN"` 자리에 넣습니다. 16:9로 잘린 모습에서 얼굴이 잘리지 않는지 꼭 확인합니다.

**고칠 때 (같은 대화에서):** `Same four characters, same art style and composition, square 1:1. Change only: {고칠 점}. Still no text.`
- 얼굴이 위나 아래로 치우치면: `Change only: move all four characters and the main props into the middle horizontal band (25% to 75% of the height); fill the top and bottom with plain dark background.`

---

## 1부 · 정답표 없이 배우기 (cover_ch1, part1/index.html)

| 항목 | 내용 |
|---|---|
| 주제 은유 | 왼쪽 쏟아진 테트리스 블록 더미 → 가운데 천 주머니 세 개에 같은 모양끼리 담기 → 오른쪽 이름표 없는 얼굴 사진(흐린 실루엣)과 빈 이름표 |
| 네 캐릭터 | 박사: 가운데 뒤, 두 손을 펼쳐 작업대 가리킴 / 조수: 오른쪽, 이름표 없는 사진 한 장 들고 갸웃 / 초파리: 왼쪽, T자 블록을 주머니에 넣는 중 / 주판봇: 오른쪽 위쪽에 떠서 빈 이름표 묶음을 부채처럼 |
| 대체 글 (alt) | 밤의 연구실에서 네 캐릭터가 쏟아진 테트리스 블록 더미와 이름표 없는 사진 더미를 정리하는 1부 표지 |

**Genspark에 붙여 넣기 ↓**
```
웹페이지 맨 위 표지로 쓰는 정사각형 그림 1장을 만들어 줘.
- 비율 1:1, 1280×1280px
- 첨부한 참고 이미지의 네 캐릭터(박사, 조수, 초파리 연구원, 주판봇)를 같은 그림체·같은 외형으로, 넷 모두 등장
- 주판봇은 새 외형(참고 그림 E13_neutral)대로: 베이지색 CRT 모니터 머리와 작은 상자 몸, 짙은 초록 화면에 민트 픽셀 눈·입, 끝에 적갈색 주판알 하나가 달린 가는 안테나, 회색 마디 팔과 벙어리장갑 손, 짙은 회색 무한궤도 두 개로 바닥에 선다(떠 있지 않음). 키는 박사의 약 3/4. 흰 둥근 머리·검은 알약 화면·노란 눈·금화는 넣지 말 것
- 그림 안에 글자·숫자·로고를 넣지 말 것 (이름표는 빈칸으로)
- 블록은 같은 모양은 같은 색: 막대(일자 4칸) 하늘색, 네모(2×2) 노랑, T자 보라. 크고 또렷하게
- 이 그림은 가로 16:9로 위아래가 잘려서 쓰인다. 네 캐릭터의 얼굴·손과 블록·주머니·사진은 모두 세로 가운데(높이 25~75%) 띠 안에 두고, 위아래는 어두운 벽과 작업대처럼 단순한 배경으로
- 왼쪽 아래 구석은 어둡고 단순하게 (제목 칩이 올라감)
아래 영어 프롬프트를 그대로 써 줘.

Square website cover illustration, 1:1, 1280x1280.
Match the art style, proportions and colors of the attached reference images exactly: 16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights.
Cozy night laboratory mood, purple light, soft magenta and green fluorescent accents, medium brightness.
Scene: a big workbench inside the same night lab world, seen at eye level. On the left a messy pile of large Tetris-style blocks in random orientations — straight four-in-a-row pieces in cyan, 2x2 squares in yellow, T-shaped pieces in purple (same shape always same color). In the middle three open cloth drawstring pouches where the same shapes are being gathered together. On the right a small stack of unlabeled portrait photos showing only blurry face silhouettes, with blank paper tags floating above them.
All four characters together, standing close around the workbench:
  chibi scientist with round glasses, black hair with one white streak, white lab coat over black vest and tie, at the back center with both hands spread over the workbench;
  girl researcher with pink hair in two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, at the right holding one unlabeled photo and tilting her head;
  anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat, transparent wings, at the left facing right, dropping a T-shaped block into a pouch;
  small boxy retro computer robot with a beige rounded-corner CRT-monitor head, a big dark green screen face with mint pixel eyes and mouth, a thin antenna on a small gray base topped with one small red-brown abacus bead, a small beige box body, chunky gray segmented tube arms with round gray mitten hands, two dark gray tank treads instead of legs, about three quarters the height of the scientist, standing on its treads at the right facing left, fanning out a bundle of blank tags like cards.
Visual metaphor: sorting without labels — blocks finding their pouches by shape, photos waiting without names.
Composition: square frame; all faces, hands, blocks, pouches and photos stay inside the middle horizontal band from 25% to 75% of the height and inside 10% side margins; the top quarter is a dim lab wall with soft lights, the bottom quarter is the plain front edge of the workbench; keep the bottom-left corner dark and simple; the light falls on the pouches.
Mood: curious, friendly rivalry, the moment before the result.
No white glossy round robot head, no black pill-shaped visor, no yellow eyes, no ball-shaped antenna knob, no cyan chest light, no floating robot, no gold coins. No text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands.
```

---

## 2부 · 렌더링을 거꾸로 (cover_ch2, part2/index.html)

| 항목 | 내용 |
|---|---|
| 주제 은유 | 왼쪽 바늘구멍 상자 뒷벽에 거꾸로 비친 머그컵 → 가운데 여러 각도의 머그컵 사진 액자 고리, 그 안에서 떠오르는 3D 머그컵(반은 와이어프레임, 반은 단단함) → 오른쪽 위에서 내려다본 컵 사진(안쪽 구멍) |
| 네 캐릭터 | 초파리: 왼쪽, 바늘구멍 상자 들여다봄 / 주판봇: 오른쪽, 사진 액자 더미를 안음 / 박사: 가운데 뒤, 떠오르는 3D 머그컵 가리킴 / 조수: 가운데 앞, 진짜 머그컵을 두 손으로 돌려 봄 |
| 대체 글 (alt) | 밤의 연구실, 핀홀 상자 벽에 거꾸로 비친 머그컵과 여러 각도의 사진에서 되살아나는 3D 머그컵 앞에 네 캐릭터가 선 2부 표지 |

**Genspark에 붙여 넣기 ↓**
```
웹페이지 맨 위 표지로 쓰는 정사각형 그림 1장을 만들어 줘.
- 비율 1:1, 1280×1280px
- 첨부한 참고 이미지의 네 캐릭터(박사, 조수, 초파리 연구원, 주판봇)를 같은 그림체·같은 외형으로, 넷 모두 등장
- 주판봇은 새 외형(참고 그림 E13_neutral)대로: 베이지색 CRT 모니터 머리와 작은 상자 몸, 짙은 초록 화면에 민트 픽셀 눈·입, 끝에 적갈색 주판알 하나가 달린 가는 안테나, 회색 마디 팔과 벙어리장갑 손, 짙은 회색 무한궤도 두 개로 바닥에 선다(떠 있지 않음). 키는 박사의 약 3/4. 흰 둥근 머리·검은 알약 화면·노란 눈·금화는 넣지 말 것
- 그림 안에 글자·숫자·로고를 넣지 말 것
- 왼쪽에 바늘구멍 상자(뒷벽에 머그컵이 거꾸로 비침), 가운데에 여러 각도의 머그컵 사진 액자가 고리 모양으로 떠 있고 그 안에서 3D 머그컵이 떠오름
- 머그컵은 흰색에 자홍색 띠 하나, 손잡이 하나
- 이 그림은 가로 16:9로 위아래가 잘려서 쓰인다. 네 캐릭터의 얼굴·손과 상자·사진 고리·3D 머그컵은 모두 세로 가운데(높이 25~75%) 띠 안에 두고, 위아래는 어두운 벽과 작업대처럼 단순한 배경으로
- 왼쪽 아래 구석은 어둡고 단순하게 (제목 칩이 올라감)
아래 영어 프롬프트를 그대로 써 줘.

Square website cover illustration, 1:1, 1280x1280.
Match the art style, proportions and colors of the attached reference images exactly: 16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights.
Cozy night laboratory mood, purple light, soft magenta and green fluorescent accents, medium brightness.
Scene: inside the same night lab world, at eye level. On the left a pinhole box camera shows an upside-down image of a mug on its back wall. In the center, a compact ring of small framed photos of the same mug taken from many angles floats above a workbench, and inside the ring a glowing 3D mug rises, half wireframe and half solid. On the right a framed photo looks straight down into the mug, showing its hollow inside. The mug is white with a single magenta stripe and one handle.
All four characters together, close around the workbench:
  anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat, transparent wings, at the left facing right, peering into the pinhole box;
  small boxy retro computer robot with a beige rounded-corner CRT-monitor head, a big dark green screen face with mint pixel eyes and mouth, a thin antenna on a small gray base topped with one small red-brown abacus bead, a small beige box body, chunky gray segmented tube arms with round gray mitten hands, two dark gray tank treads instead of legs, about three quarters the height of the scientist, at the right facing left, hugging a stack of photo frames;
  chibi scientist with round glasses, black hair with one white streak, white lab coat over black vest and tie, at the back center, pointing at the rising 3D mug;
  girl researcher with pink hair in two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, in the front center, holding a real mug in both hands and turning it around curiously.
Visual metaphor: turning flat photos back into a 3D object — rendering in reverse.
Composition: square frame; all faces, hands, the pinhole box, the photo ring and the 3D mug stay inside the middle horizontal band from 25% to 75% of the height and inside 10% side margins; the top quarter is a dim lab wall with soft lights, the bottom quarter is the plain front edge of the workbench; keep the bottom-left corner dark and simple.
Mood: curious, friendly rivalry, the moment before the result, nobody winning yet.
No white glossy round robot head, no black pill-shaped visor, no yellow eyes, no ball-shaped antenna knob, no cyan chest light, no floating robot, no gold coins. No text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands.
```

---

## 3부 · 적게 그리고 AI로 채우기 (cover_ch3, part3/index.html)

| 항목 | 내용 |
|---|---|
| 주제 은유 | 왼쪽 모니터: 큼직한 픽셀로 깨진 작은 게임 화면 → 가운데: 빛나는 신경망 상자(점과 선만) → 오른쪽 모니터: 같은 장면이 선명하고 매끄러운 화면 |
| 네 캐릭터 | 박사: 가운데 뒤, 보랏빛 불꽃으로 신경망 상자 가리킴 / 조수: 오른쪽, 선명한 화면 쪽으로 몸을 기울이며 기대 / 초파리: 왼쪽, 깨진 화면을 돋보기로 의심스럽게 봄 / 주판봇: 오른쪽 위쪽, 빛나는 주판알이 달린 나무 주판(아낀 픽셀)를 안음 |
| 대체 글 (alt) | 밤의 연구실, 거칠게 작게 그린 게임 화면이 AI를 거쳐 선명하고 매끄러운 큰 화면으로 바뀌는 앞에 네 캐릭터가 선 3부 표지 |

**Genspark에 붙여 넣기 ↓**
```
웹페이지 맨 위 표지로 쓰는 정사각형 그림 1장을 만들어 줘.
- 비율 1:1, 1280×1280px
- 첨부한 참고 이미지의 네 캐릭터(박사, 조수, 초파리 연구원, 주판봇)를 같은 그림체·같은 외형으로, 넷 모두 등장
- 주판봇은 새 외형(참고 그림 E13_neutral)대로: 베이지색 CRT 모니터 머리와 작은 상자 몸, 짙은 초록 화면에 민트 픽셀 눈·입, 끝에 적갈색 주판알 하나가 달린 가는 안테나, 회색 마디 팔과 벙어리장갑 손, 짙은 회색 무한궤도 두 개로 바닥에 선다(떠 있지 않음). 키는 박사의 약 3/4. 흰 둥근 머리·검은 알약 화면·노란 눈·금화는 넣지 말 것
- 그림 안에 글자·숫자·로고를 넣지 말 것 (모니터 화면에도 글자 없이)
- 왼쪽 모니터는 큼직한 픽셀로 깨진 거친 화면, 오른쪽 모니터는 같은 장면이 선명한 화면. 비교가 한눈에 보이게 모니터를 크게
- 화면 속 블록은 같은 모양 같은 색: 막대 하늘색, 네모 노랑, T자 보라, L자 주황
- 이 그림은 가로 16:9로 위아래가 잘려서 쓰인다. 네 캐릭터의 얼굴·손과 모니터 세 대는 모두 세로 가운데(높이 25~75%) 띠 안에 두고, 위아래는 어두운 벽과 책상처럼 단순한 배경으로
- 왼쪽 아래 구석은 어둡고 단순하게 (제목 칩이 올라감)
아래 영어 프롬프트를 그대로 써 줘.

Square website cover illustration, 1:1, 1280x1280.
Match the art style, proportions and colors of the attached reference images exactly: 16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights.
Cozy night laboratory mood, purple light, soft magenta and green fluorescent accents, medium brightness.
Scene: a desk in the same night lab world with three gaming monitors in a row, seen at eye level. The left monitor shows a Tetris-like game screen rendered at very low resolution — big blocky jagged pixels, broken thin lines. The middle shows a glowing box of a small neural network made only of dots and connecting lines, no text. The right monitor shows the very same game screen, sharp and smooth at high resolution. On both screens, Tetris-style blocks keep one color per shape: cyan straight pieces, yellow squares, purple T pieces, orange L pieces. A soft beam of light flows from the left monitor through the neural box into the right monitor.
All four characters together, close in front of the desk:
  chibi scientist with round glasses, black hair with one white streak, white lab coat over black vest and tie, at the back center pointing at the glowing neural box with purple sparks in both hands;
  girl researcher with pink hair in two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, at the right leaning toward the sharp right monitor, curious and hopeful;
  anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat, transparent wings, at the left facing right, inspecting the jagged left monitor with a magnifying glass, skeptical;
  small boxy retro computer robot with a beige rounded-corner CRT-monitor head, a big dark green screen face with mint pixel eyes and mouth, a thin antenna on a small gray base topped with one small red-brown abacus bead, a small beige box body, chunky gray segmented tube arms with round gray mitten hands, two dark gray tank treads instead of legs, about three quarters the height of the scientist, standing on its treads at the right facing left, hugging a small wooden abacus with glowing beads.
Visual metaphor: render less, let AI fill the rest — the same scene going from rough and small to sharp and large.
Composition: square frame; all faces, hands and the three monitors stay inside the middle horizontal band from 25% to 75% of the height and inside 10% side margins; the monitors are large and readable; the top quarter is a dim lab wall with soft lights, the bottom quarter is the plain front edge of the desk; keep the bottom-left corner dark and simple.
Mood: curious, friendly rivalry, the moment before the result.
No white glossy round robot head, no black pill-shaped visor, no yellow eyes, no ball-shaped antenna knob, no cyan chest light, no floating robot, no gold coins. No text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands.
```
- 두 화면이 비슷해 보이면: `Change only: make the left monitor much more blocky and jagged, with pixels four times bigger; keep the right monitor sharp.`
