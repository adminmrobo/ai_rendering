# AI 렌더링 연구실 — 표지 프롬프트 모음 (18장 + 첫 화면 1장)

Genspark에 한 장씩 붙여 넣으면 됩니다. 매번 **참고 이미지 4장**(`doc_e13`, `asst_e13`, `fly_e13`, 주판봇 `images/jupanbot/E13_neutral.png` — adminmrobo/fruitfly-lab-expressions, 커밋 5269662, 2026-11-05 새 픽셀 그림)을 함께 올립니다.

| 순서 | 묶음 | 비율 · 크기 | 저장할 파일 이름 |
|---|---|---|---|
| A1~A3 | 각 부 목차(index) 표지 | 1:1 · 1280×1280 | `cover_ch1.png` ~ `cover_ch3.png` |
| B1~B15 | 각 편 첫 화면 표지 | 16:9 · 가로 1920 이상 | `cover_1-1.png` ~ `cover_3-5.png` |

**받은 뒤 확인:** 비율 맞음 · 그림 안에 글자 없음 · 네 캐릭터 외형이 참고 그림과 같음 · 주판봇이 무한궤도로 바닥에 서 있고 키가 박사의 약 3/4. 파일 이름을 위 표대로 붙여 한 zip으로 주시면 18쪽과 6개 언어판에 한 번에 넣습니다.

**고칠 때 (같은 대화에서):** `Same four characters, same art style and composition. Change only: {고칠 점}. Still no text.`

**주판봇이 옛 모습(흰 둥근 머리·노란 눈)으로 나오면:** `Same scene. Redraw only the robot to match the attached E13_neutral reference exactly: beige CRT-monitor head, dark green screen with mint pixel face, thin antenna with one red-brown abacus bead, gray segmented arms with mitten hands, two dark gray tank treads on the floor. Still no text.`

> 2026-11-05: 주판봇 새 픽셀 그림(캐릭터 팩 1.3)에 맞춰 19개 프롬프트의 주판봇 묘사·금지 항목·참고 이미지를 모두 고쳤습니다.

---

## A. 목차 표지 — 정사각 1280×1280

목차 칸은 가로로 보여서 위아래가 잘릴 수 있습니다. 프롬프트에 “얼굴과 소품은 세로 가운데 띠 안”을 넣어 두었습니다.

### A1. 1부 · 정답표 없이 배우기 → `cover_ch1.png`

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

### A2. 2부 · 렌더링을 거꾸로 → `cover_ch2.png`

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

### A3. 3부 · 적게 그리고 AI로 채우기 → `cover_ch3.png`

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

---
## B. 각 편 표지 — 16:9 (가로 1920 이상)

각 편 첫 화면에는 위아래가 조금 잘린 16:7 띠로 보입니다. 프롬프트에 그 여유가 들어 있습니다.

### B1. 1-1 정답표가 없으면 어떻게 배우지? (1부 표지 그림을 1-1편 표지로) → `cover_1-1.png`

```
웹페이지 맨 위에 거는 표지 그림 1장을 만들어 줘.
- 비율 16:9, 가로 1920px 이상
- 첨부한 참고 이미지의 네 캐릭터(박사, 조수, 초파리 연구원, 주판봇)를 같은 그림체·같은 외형으로, 넷 모두 등장
- 주판봇은 새 외형(참고 그림 E13_neutral)대로: 베이지색 CRT 모니터 머리와 작은 상자 몸, 짙은 초록 화면에 민트 픽셀 눈·입, 끝에 적갈색 주판알 하나가 달린 가는 안테나, 회색 마디 팔과 벙어리장갑 손, 짙은 회색 무한궤도 두 개로 바닥에 선다(떠 있지 않음). 키는 박사의 약 3/4. 흰 둥근 머리·검은 알약 화면·노란 눈·금화는 넣지 말 것
- 그림 안에 글자·숫자·로고를 넣지 말 것 (이름표는 빈칸으로)
- 블록은 실제 테트리스처럼 같은 모양은 같은 색: 막대(일자 4칸) 하늘색, 네모(2×2) 노랑, T자 보라. 블록은 크고 또렷하게
- 얼굴과 손은 가장자리에서 떨어진 가운데 영역에, 왼쪽 아래 구석은 어둡고 단순하게
- 이 그림은 아래위가 잘린 가로 띠(16:5)로도 쓰이니, 네 캐릭터의 얼굴은 세로 가운데 40% 안에 두기
아래 영어 프롬프트를 그대로 써 줘.

Website top cover illustration, wide 16:9.
Match the art style, proportions and colors of the attached reference images exactly.
Cozy night laboratory mood, purple light, soft magenta and green fluorescent accents.
Scene: a big workbench inside the same night lab world; on the left a messy pile of large Tetris-style blocks lying in random orientations — straight four-in-a-row pieces in cyan, 2x2 square pieces in yellow, T-shaped pieces in purple (same shape always same color), each block made of beveled pixel squares; in the middle three open cloth drawstring pouches where the same shapes are being gathered together; on the right a scattered stack of unlabeled portrait photos showing only blurry face silhouettes, with blank paper tags floating above them.
All four characters together:
  chibi scientist with round glasses, black hair with one white streak, white lab coat over black vest and tie, at the back center with both hands spread over the workbench;
  girl researcher with pink hair in two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, at the right side holding one unlabeled photo and tilting her head;
  anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat, transparent wings, on the left facing right, dropping a T-shaped block into a pouch;
  small boxy retro computer robot with a beige rounded-corner CRT-monitor head, a big dark green screen face with mint pixel eyes and mouth, a thin antenna on a small gray base topped with one small red-brown abacus bead, a small beige box body, chunky gray segmented tube arms with round gray mitten hands, two dark gray tank treads instead of legs, about three quarters the height of the scientist, on the right facing left, fanning out a bundle of blank tags like cards.
Visual metaphor of the topic: sorting without labels — blocks finding their pouches by shape, photos waiting without names, no text.
Composition: keep every face and hand inside the central safe area (12% margin left and right, 10% top, 18% bottom) and within the middle 40% of the height; keep the bottom-left corner dark and simple; the light falls on the pouches.
Mood: curious, friendly rivalry, the moment before the result.
No white glossy round robot head, no black pill-shaped visor, no yellow eyes, no ball-shaped antenna knob, no cyan chest light, no floating robot, no gold coins. No text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands.
```

### B2. 1-2 비슷한 것끼리 묶기 (cover_1-2) → `cover_1-2.png`

```
웹페이지 첫 화면 배경으로 쓰는 표지 그림 1장을 만들어 줘.
- 비율 16:9, 가로 1920px 이상
- 첨부한 참고 이미지의 네 캐릭터(박사, 조수, 초파리 연구원, 주판봇)를 같은 그림체·같은 외형으로, 넷 모두 등장
- 주판봇은 새 외형(참고 그림 E13_neutral)대로: 베이지색 CRT 모니터 머리와 작은 상자 몸, 짙은 초록 화면에 민트 픽셀 눈·입, 끝에 적갈색 주판알 하나가 달린 가는 안테나, 회색 마디 팔과 벙어리장갑 손, 짙은 회색 무한궤도 두 개로 바닥에 선다(떠 있지 않음). 키는 박사의 약 3/4. 흰 둥근 머리·검은 알약 화면·노란 눈·금화는 넣지 말 것
- 그림 안에 글자·숫자·로고를 넣지 말 것 (자의 눈금은 선만, 숫자 없이)
- 블록은 실제 테트리스처럼 같은 모양은 같은 색: 막대(일자 4칸) 하늘색, 네모(2×2) 노랑, T자 보라, L자 주황
- 블록은 크고 또렷하게: 화면 위쪽 절반을 블록 더미와 주머니 네 개가 채우도록. 같은 모양이라도 크기가 조금씩 다른 블록이 섞여 있게
- 위아래가 조금 잘린 16:7 띠로 쓰이니, 얼굴과 손은 세로 가운데 70% 안에 두기
- 왼쪽 아래 구석은 어둡고 단순하게 (제목 칩이 올라감)
아래 영어 프롬프트를 그대로 써 줘.

Website hero background illustration, wide 16:9.
Match the art style, proportions and colors of the attached reference images exactly: 16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights.
Cozy night laboratory mood, purple light, soft magenta and green fluorescent accents, medium brightness.
Scene: a big workbench inside the same night lab world. On the left, a large messy pile of Tetris-style blocks made of beveled pixel squares, lying in random orientations and in two or three slightly different sizes: straight four-in-a-row pieces in cyan, 2x2 square pieces in yellow, T-shaped pieces in purple, L-shaped pieces in orange (same shape always same color), big and readable. On the right, four cloth drawstring pouches standing open in a row, each holding only one shape: cyan straight pieces, yellow squares, purple T pieces, orange L pieces. On the back wall, a tree-shaped family-tree chart made only of branches with small blank cards at the leaves. A giant wooden ruler with tick lines but no numbers lies across the workbench.
All four characters together:
  girl researcher with pink hair in two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, in the front center measuring the long side of one purple T-shaped block with the giant ruler, focused;
  chibi scientist with round glasses, black hair with one white streak, white lab coat over black vest and tie, at the back center pointing at the four pouches with a thoughtful face;
  anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat, transparent wings, on the left facing right, pinning a new branch onto the family-tree chart;
  small boxy retro computer robot with a beige rounded-corner CRT-monitor head, a big dark green screen face with mint pixel eyes and mouth, a thin antenna on a small gray base topped with one small red-brown abacus bead, a small beige box body, chunky gray segmented tube arms with round gray mitten hands, two dark gray tank treads instead of legs, about three quarters the height of the scientist, on the right facing left, holding up a fifth empty pouch as if wondering how many pouches are needed.
Visual metaphor of the topic: grouping similar things — deciding what to measure, choosing the number of pouches, joining the closest ones first like a family tree.
Composition: blocks and pouches fill the upper half and are large and crisp; keep every face and hand inside the central safe area (10% margin left and right, 15% top and bottom); keep the bottom-left corner dark and simple; light falls on the pouches.
Mood: curious, friendly rivalry, the moment before the result, nobody winning yet.
No white glossy round robot head, no black pill-shaped visor, no yellow eyes, no ball-shaped antenna knob, no cyan chest light, no floating robot, no gold coins. No text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands.
```

### B3. 1-3 얼굴을 지도 위 점으로 (cover_1-3) → `cover_1-3.png`

```
웹페이지 첫 화면 배경으로 쓰는 표지 그림 1장을 만들어 줘.
- 비율 16:9, 가로 1920px 이상
- 첨부한 참고 이미지의 네 캐릭터(박사, 조수, 초파리 연구원, 주판봇)를 같은 그림체·같은 외형으로, 넷 모두 등장
- 주판봇은 새 외형(참고 그림 E13_neutral)대로: 베이지색 CRT 모니터 머리와 작은 상자 몸, 짙은 초록 화면에 민트 픽셀 눈·입, 끝에 적갈색 주판알 하나가 달린 가는 안테나, 회색 마디 팔과 벙어리장갑 손, 짙은 회색 무한궤도 두 개로 바닥에 선다(떠 있지 않음). 키는 박사의 약 3/4. 흰 둥근 머리·검은 알약 화면·노란 눈·금화는 넣지 말 것
- 그림 안에 글자·숫자·로고를 넣지 말 것
- 바닥에 커다란 빈 종이 지도(눈금만). 공중의 작은 얼굴 카드 수백 장이 종이접기처럼 접히며 지도 위 점으로 내려앉는다
- 같은 캐릭터 카드끼리 지도 위 한 곳에 모여 네 무리(파랑·분홍·빨강·초록 점)가 된다. 지도 한가운데에 흐릿한 유령 얼굴 하나
- 위아래가 조금 잘린 16:7 띠로 쓰이니, 얼굴과 손은 세로 가운데 70% 안에 두기
- 왼쪽 아래 구석은 어둡고 단순하게 (제목 칩이 올라감)
아래 영어 프롬프트를 그대로 써 줘.

Website hero background illustration, wide 16:9.
Match the art style, proportions and colors of the attached reference images exactly: 16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights.
Cozy night laboratory mood, purple light, soft magenta and green fluorescent accents, medium brightness.
Scene: inside the same night lab world, a huge blank paper map with only faint grid lines is spread across the floor. Hundreds of tiny portrait cards of the four characters, each with a slightly different expression, float in the air and fold like origami into small glowing dots as they land on the map. Cards of the same character land together, forming four clusters of dots: blue, pink, red and green. In the very center of the map hovers one blurry, ghost-like translucent face like a heat haze.
All four characters together:
  anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat, transparent wings, on the left facing right, folding one portrait card like origami into a dot;
  small boxy retro computer robot with a beige rounded-corner CRT-monitor head, a big dark green screen face with mint pixel eyes and mouth, a thin antenna on a small gray base topped with one small red-brown abacus bead, a small beige box body, chunky gray segmented tube arms with round gray mitten hands, two dark gray tank treads instead of legs, about three quarters the height of the scientist, on the right facing left, holding scissors and two tiny snipped corners of a card;
  chibi scientist with round glasses, black hair with one white streak, white lab coat over black vest and tie, at the back center pointing at the clusters with a baton;
  girl researcher with pink hair in two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, in the front center kneeling and happily peering at the pink cluster of her own cards.
Visual metaphor of the topic: folding thousands of numbers into a point on a map, where similar faces gather.
Composition: the map and the folding cards fill the upper half and are large and crisp; keep every face and hand inside the central safe area (10% margin left and right, 15% top and bottom); keep the bottom-left corner dark and simple.
Mood: curious, friendly rivalry, the moment before the result, nobody winning yet.
No white glossy round robot head, no black pill-shaped visor, no yellow eyes, no ball-shaped antenna knob, no cyan chest light, no floating robot, no gold coins. No text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands.
```

### B4. 1-4 가리고 맞히기 (cover_1-4) → `cover_1-4.png`

```
웹페이지 첫 화면 배경으로 쓰는 표지 그림 1장을 만들어 줘.
- 비율 16:9, 가로 1920px 이상
- 첨부한 참고 이미지의 네 캐릭터(박사, 조수, 초파리 연구원, 주판봇)를 같은 그림체·같은 외형으로, 넷 모두 등장
- 주판봇은 새 외형(참고 그림 E13_neutral)대로: 베이지색 CRT 모니터 머리와 작은 상자 몸, 짙은 초록 화면에 민트 픽셀 눈·입, 끝에 적갈색 주판알 하나가 달린 가는 안테나, 회색 마디 팔과 벙어리장갑 손, 짙은 회색 무한궤도 두 개로 바닥에 선다(떠 있지 않음). 키는 박사의 약 3/4. 흰 둥근 머리·검은 알약 화면·노란 눈·금화는 넣지 말 것
- 그림 안에 글자·숫자·로고를 넣지 말 것
- 작업대 위에 가운데가 잘록한 모래시계 모양 기계. 가운데가 회색으로 가려진 얼굴 카드가 왼쪽에서 들어가 잘록한 곳에서 빛 구슬로 접혔다가 오른쪽으로 빈칸이 채워진 카드로 나온다
- 위아래가 조금 잘린 16:7 띠로 쓰이니, 얼굴과 손은 세로 가운데 70% 안에 두기
- 왼쪽 아래 구석은 어둡고 단순하게 (제목 칩이 올라감)
아래 영어 프롬프트를 그대로 써 줘.

Website hero background illustration, wide 16:9.
Match the art style, proportions and colors of the attached reference images exactly: 16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights.
Cozy night laboratory mood, purple light, soft magenta and green fluorescent accents, medium brightness.
Scene: inside the same night lab world, a large hourglass-shaped machine with a narrow glowing waist stands on a workbench in the upper half. Portrait cards of the four characters, each with the middle of the face covered by a gray paper patch, ride a small conveyor into the left side of the machine; at the narrow waist they fold into a few glowing beads, and on the right side the cards come out with the gray patch gone and the face filled in. On one side of the bench lies a stack of fill-in-the-blank practice sheets, on the other side an open photo album of portrait cards.
All four characters together:
  anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat, transparent wings, on the left facing right, cutting a matching face piece out of the album with small scissors and pasting it on a card;
  small boxy retro computer robot with a beige rounded-corner CRT-monitor head, a big dark green screen face with mint pixel eyes and mouth, a thin antenna on a small gray base topped with one small red-brown abacus bead, a small beige box body, chunky gray segmented tube arms with round gray mitten hands, two dark gray tank treads instead of legs, about three quarters the height of the scientist, on the right facing left, confidently turning a crank on the machine;
  chibi scientist with round glasses, black hair with one white streak, white lab coat over black vest and tie, at the back center pointing at the machine's narrow glowing waist;
  girl researcher with pink hair in two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, in the front center playfully covering half of her face with one hand and smiling.
Visual metaphor of the topic: hiding part of a picture and learning to fill it in, with the picture itself as the answer.
Composition: the machine and the cards fill the upper half and are large and crisp; keep every face and hand inside the central safe area (10% margin left and right, 15% top and bottom); keep the bottom-left corner dark and simple.
Mood: curious, friendly rivalry, the moment before the result, nobody winning yet.
No white glossy round robot head, no black pill-shaped visor, no yellow eyes, no ball-shaped antenna knob, no cyan chest light, no floating robot, no gold coins. No text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands.
```

### B5. 1-5 이 얼굴은 누구? (cover_1-5) → `cover_1-5.png`

```
웹페이지 첫 화면 배경으로 쓰는 표지 그림 1장을 만들어 줘.
- 비율 16:9, 가로 1920px 이상
- 첨부한 참고 이미지의 네 캐릭터(박사, 조수, 초파리 연구원, 주판봇)를 같은 그림체·같은 외형으로, 넷 모두 등장
- 주판봇은 새 외형(참고 그림 E13_neutral)대로: 베이지색 CRT 모니터 머리와 작은 상자 몸, 짙은 초록 화면에 민트 픽셀 눈·입, 끝에 적갈색 주판알 하나가 달린 가는 안테나, 회색 마디 팔과 벙어리장갑 손, 짙은 회색 무한궤도 두 개로 바닥에 선다(떠 있지 않음). 키는 박사의 약 3/4. 흰 둥근 머리·검은 알약 화면·노란 눈·금화는 넣지 말 것
- 그림 안에 글자·숫자·로고를 넣지 말 것
- 큰 코르크 게시판에 네 캐릭터를 공 모양으로 단순화한 흉상 사진이 앞·옆·뒤 여러 각도로 꽂혀 있다. 맨 위 정면 사진 네 장에만 리본, 나머지 사진은 실로 리본과 이어짐(뒷모습 몇 장은 엉뚱한 리본에)
- 위아래가 조금 잘린 16:7 띠로 쓰이니, 얼굴과 손은 세로 가운데 70% 안에 두기
- 왼쪽 아래 구석은 어둡고 단순하게 (제목 칩이 올라감)
아래 영어 프롬프트를 그대로 써 줘.

Website hero background illustration, wide 16:9.
Match the art style, proportions and colors of the attached reference images exactly: 16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights.
Cozy night laboratory mood, purple light, soft magenta and green fluorescent accents, medium brightness.
Scene: inside the same night lab world, a large cork board fills the upper half, covered with pinned photos of simple sphere-built toy busts of the four characters seen from the front, the side and the back. Only the four front-view photos in the top row wear small ribbon tags. Thin strings connect every other photo to one of the four ribbons; the front-view photos are connected to the right ribbons, while a few back-view photos are connected to the wrong ones. On a side table lie a paint palette with eight color blobs and a magnifying glass.
All four characters together:
  anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat, transparent wings, on the left facing right, holding the paint palette and comparing its colors with a back-view photo;
  small boxy retro computer robot with a beige rounded-corner CRT-monitor head, a big dark green screen face with mint pixel eyes and mouth, a thin antenna on a small gray base topped with one small red-brown abacus bead, a small beige box body, chunky gray segmented tube arms with round gray mitten hands, two dark gray tank treads instead of legs, about three quarters the height of the scientist, on the right facing left, hugging a big bundle of ribbon tags;
  chibi scientist with round glasses, black hair with one white streak, white lab coat over black vest and tie, at the back center pointing at one wrongly connected string;
  girl researcher with pink hair in two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, in the front center turned away showing her two buns, smiling over her shoulder.
Visual metaphor of the topic: recognizing who is who with only a few name tags, and how a turned head breaks the match.
Composition: the cork board fills the upper half and is large and crisp; keep every face and hand inside the central safe area (10% margin left and right, 15% top and bottom); keep the bottom-left corner dark and simple.
Mood: curious, friendly rivalry, the moment before the result, nobody winning yet.
No white glossy round robot head, no black pill-shaped visor, no yellow eyes, no ball-shaped antenna knob, no cyan chest light, no floating robot, no gold coins. No text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands.
```

### B6. 2-1 사진은 왜 납작할까 (cover_2-1) → `cover_2-1.png`

```
웹페이지 첫 화면 배경으로 쓰는 표지 그림 1장을 만들어 줘.
- 비율 16:9, 가로 1920px 이상
- 첨부한 참고 이미지의 네 캐릭터(박사, 조수, 초파리 연구원, 주판봇)를 같은 그림체·같은 외형으로, 넷 모두 등장
- 주판봇은 새 외형(참고 그림 E13_neutral)대로: 베이지색 CRT 모니터 머리와 작은 상자 몸, 짙은 초록 화면에 민트 픽셀 눈·입, 끝에 적갈색 주판알 하나가 달린 가는 안테나, 회색 마디 팔과 벙어리장갑 손, 짙은 회색 무한궤도 두 개로 바닥에 선다(떠 있지 않음). 키는 박사의 약 3/4. 흰 둥근 머리·검은 알약 화면·노란 눈·금화는 넣지 말 것
- 그림 안에 글자·숫자·로고를 넣지 말 것
- 사람 키만 한 종이 바늘구멍 상자. 앞 탁자의 머그컵(손잡이는 뒤로 숨김)이 뒷막에 거꾸로 비친다. 빛줄기가 구멍에서 엇갈리는 모습
- 머그컵은 흰색에 자홍색 띠 하나
- 위아래가 조금 잘린 16:7 띠로 쓰일 수 있으니, 얼굴과 손은 세로 가운데 70% 안에 두기
- 왼쪽 아래 구석은 어둡고 단순하게 (제목 칩이 올라감)
아래 영어 프롬프트를 그대로 써 줘.

Website hero background illustration, wide 16:9.
Match the art style, proportions and colors of the attached reference images exactly: 16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights.
Cozy night laboratory mood, purple light, soft magenta and green fluorescent accents, medium brightness.
Scene: inside the same night lab world, a person-sized cardboard pinhole box camera stands in the upper half with a tiny hole on its front and a translucent paper screen at the back. A white mug with one magenta stripe sits on a small table in front of the hole with its handle turned away and hidden behind the body; thin light rays cross at the hole and the mug appears upside down on the back screen, without any handle visible. Next to the box, a small mug placed near and a big mug placed far look exactly the same size, and a ball and a flat coin lie side by side under a slanted flashlight beam.
All four characters together:
  anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat, transparent wings, on the left facing right, checking the upside-down image on the screen with a magnifying glass;
  small boxy retro computer robot with a beige rounded-corner CRT-monitor head, a big dark green screen face with mint pixel eyes and mouth, a thin antenna on a small gray base topped with one small red-brown abacus bead, a small beige box body, chunky gray segmented tube arms with round gray mitten hands, two dark gray tank treads instead of legs, about three quarters the height of the scientist, on the right facing left, pointing behind the real mug as if insisting a handle must be there;
  chibi scientist with round glasses, black hair with one white streak, white lab coat over black vest and tie, at the back center, tracing the crossing light rays with one finger;
  girl researcher with pink hair in two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, in the front center, shining a flashlight sideways at the ball and the coin to compare them.
Visual metaphor of the topic: how a 3D object becomes a flat photo through a pinhole, and what gets lost on the way.
Composition: the main props fill the upper half and are large and crisp; keep every face and hand inside the central safe area (10% margin left and right, 15% top and bottom); keep the bottom-left corner dark and simple.
Mood: curious, friendly rivalry, the moment before the result, nobody winning yet.
No white glossy round robot head, no black pill-shaped visor, no yellow eyes, no ball-shaped antenna knob, no cyan chest light, no floating robot, no gold coins. No text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands.
```

### B7. 2-2 몽타주 그리기 (cover_2-2) → `cover_2-2.png`

```
웹페이지 첫 화면 배경으로 쓰는 표지 그림 1장을 만들어 줘.
- 비율 16:9, 가로 1920px 이상
- 첨부한 참고 이미지의 네 캐릭터(박사, 조수, 초파리 연구원, 주판봇)를 같은 그림체·같은 외형으로, 넷 모두 등장
- 주판봇은 새 외형(참고 그림 E13_neutral)대로: 베이지색 CRT 모니터 머리와 작은 상자 몸, 짙은 초록 화면에 민트 픽셀 눈·입, 끝에 적갈색 주판알 하나가 달린 가는 안테나, 회색 마디 팔과 벙어리장갑 손, 짙은 회색 무한궤도 두 개로 바닥에 선다(떠 있지 않음). 키는 박사의 약 3/4. 흰 둥근 머리·검은 알약 화면·노란 눈·금화는 넣지 말 것
- 그림 안에 글자·숫자·로고를 넣지 말 것
- 가운데 이젤에 컵 실루엣 사진 한 장, 옆 벽에 점점 사진과 닮아 가는 컵 몽타주 그림들
- 바닥에 바둑판처럼 줄 맞춘 컵 그림들과 여기저기 흩뿌려진 컵 그림들
- 위아래가 조금 잘린 16:7 띠로 쓰일 수 있으니, 얼굴과 손은 세로 가운데 70% 안에 두기
- 왼쪽 아래 구석은 어둡고 단순하게 (제목 칩이 올라감)
아래 영어 프롬프트를 그대로 써 줘.

Website hero background illustration, wide 16:9.
Match the art style, proportions and colors of the attached reference images exactly: 16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights.
Cozy night laboratory mood, purple light, soft magenta and green fluorescent accents, medium brightness.
Scene: inside the same night lab world, a central easel holds one silhouette photo of a white cup. On the wall beside it hangs a row of hand-drawn sketches of the cup, each one corrected a little and looking more and more like the photo from left to right. On the floor, some cup sketches are laid out in a neat checkerboard grid while others are scattered randomly.
All four characters together:
  anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat, transparent wings, on the left facing right, walking between the neatly gridded sketches measuring them with a ruler;
  small boxy retro computer robot with a beige rounded-corner CRT-monitor head, a big dark green screen face with mint pixel eyes and mouth, a thin antenna on a small gray base topped with one small red-brown abacus bead, a small beige box body, chunky gray segmented tube arms with round gray mitten hands, two dark gray tank treads instead of legs, about three quarters the height of the scientist, on the right facing left, tossing sketch cards into the air so they scatter;
  chibi scientist with round glasses, black hair with one white streak, white lab coat over black vest and tie, at the back center, pointing back and forth between the photo and the sketches;
  girl researcher with pink hair in two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, in the front center, correcting the outline of a sketch with a pencil.
Visual metaphor of the topic: guessing a 3D shape, drawing it, comparing with the photo and fixing it again — analysis by synthesis.
Composition: the main props fill the upper half and are large and crisp; keep every face and hand inside the central safe area (10% margin left and right, 15% top and bottom); keep the bottom-left corner dark and simple.
Mood: curious, friendly rivalry, the moment before the result, nobody winning yet.
No white glossy round robot head, no black pill-shaped visor, no yellow eyes, no ball-shaped antenna knob, no cyan chest light, no floating robot, no gold coins. No text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands.
```

### B8. 2-3 계단과 미끄럼틀 (cover_2-3) → `cover_2-3.png`

```
웹페이지 첫 화면 배경으로 쓰는 표지 그림 1장을 만들어 줘.
- 비율 16:9, 가로 1920px 이상
- 첨부한 참고 이미지의 네 캐릭터(박사, 조수, 초파리 연구원, 주판봇)를 같은 그림체·같은 외형으로, 넷 모두 등장
- 주판봇은 새 외형(참고 그림 E13_neutral)대로: 베이지색 CRT 모니터 머리와 작은 상자 몸, 짙은 초록 화면에 민트 픽셀 눈·입, 끝에 적갈색 주판알 하나가 달린 가는 안테나, 회색 마디 팔과 벙어리장갑 손, 짙은 회색 무한궤도 두 개로 바닥에 선다(떠 있지 않음). 키는 박사의 약 3/4. 흰 둥근 머리·검은 알약 화면·노란 눈·금화는 넣지 말 것
- 그림 안에 글자·숫자·로고를 넣지 말 것
- 왼쪽에는 작은 나무 계단 모형 위에 멈춘 공, 오른쪽에는 매끈한 미끄럼틀 모형을 굴러 내려가는 공
- 가운데 벽에는 흰 컵 실루엣 판 하나, 그 옆에 가장자리가 부드럽게 번진 초록 컵 실루엣 판 하나
- 위아래가 조금 잘린 16:7 띠로 쓰일 수 있으니, 얼굴과 손은 세로 가운데 70% 안에 두기
- 왼쪽 아래 구석은 어둡고 단순하게 (제목 칩이 올라감)
아래 영어 프롬프트를 그대로 써 줘.

Website hero background illustration, wide 16:9.
Match the art style, proportions and colors of the attached reference images exactly: 16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights.
Cozy night laboratory mood, purple light, soft magenta and green fluorescent accents, medium brightness.
Scene: inside the same night lab world, on the left a small wooden staircase model with a glowing ball resting still on one step, on the right a smooth curved slide model with a glowing ball rolling down; on the back wall two boards, one with a crisp white cup silhouette and one with a soft blurry glowing green cup silhouette whose edges fade out.
All four characters together:
  anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat, transparent wings, on the left facing right, pointing at the staircase model with a ruler, skeptical;
  small boxy retro computer robot with a beige rounded-corner CRT-monitor head, a big dark green screen face with mint pixel eyes and mouth, a thin antenna on a small gray base topped with one small red-brown abacus bead, a small beige box body, chunky gray segmented tube arms with round gray mitten hands, two dark gray tank treads instead of legs, about three quarters the height of the scientist, on the right facing left, rolling a marble down the slide, holding a small wooden abacus, confident;
  chibi scientist with round glasses, black hair with one white streak, white lab coat over black vest and tie, at the back center, holding up a pair of slightly foggy glasses, thinking;
  girl researcher with pink hair in two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, in the front center, holding the blurry green cup board, smiling.
Visual metaphor of the topic: a ball that cannot roll on flat stair steps versus a ball rolling down a smooth slide, and a crisp silhouette next to a softly blurred one.
Composition: the main props fill the upper half and are large and crisp; keep every face and hand inside the central safe area (10% margin left and right, 15% top and bottom); keep the bottom-left corner dark and simple.
Mood: curious, friendly rivalry, the moment before the result, nobody winning yet.
No white glossy round robot head, no black pill-shaped visor, no yellow eyes, no ball-shaped antenna knob, no cyan chest light, no floating robot, no gold coins. No text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands.
```

### B9. 2-4 여러 각도에서 보기 (cover_2-4) → `cover_2-4.png`

```
웹페이지 첫 화면 배경으로 쓰는 표지 그림 1장을 만들어 줘.
- 비율 16:9, 가로 1920px 이상
- 첨부한 참고 이미지의 네 캐릭터(박사, 조수, 초파리 연구원, 주판봇)를 같은 그림체·같은 외형으로, 넷 모두 등장
- 주판봇은 새 외형(참고 그림 E13_neutral)대로: 베이지색 CRT 모니터 머리와 작은 상자 몸, 짙은 초록 화면에 민트 픽셀 눈·입, 끝에 적갈색 주판알 하나가 달린 가는 안테나, 회색 마디 팔과 벙어리장갑 손, 짙은 회색 무한궤도 두 개로 바닥에 선다(떠 있지 않음). 키는 박사의 약 3/4. 흰 둥근 머리·검은 알약 화면·노란 눈·금화는 넣지 말 것
- 그림 안에 글자·숫자·로고를 넣지 말 것
- 가운데 탁자 위에 작은 정육면체 블록들로 된 덩어리가 깎여 머그컵 모양(손잡이 포함)이 드러나는 중
- 탁자 둘레에 작은 사진기 여러 대가 둥글게, 벽에는 도넛과 그릇의 그림자
- 위아래가 조금 잘린 16:7 띠로 쓰일 수 있으니, 얼굴과 손은 세로 가운데 70% 안에 두기
- 왼쪽 아래 구석은 어둡고 단순하게 (제목 칩이 올라감)
아래 영어 프롬프트를 그대로 써 줘.

Website hero background illustration, wide 16:9.
Match the art style, proportions and colors of the attached reference images exactly: 16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights.
Cozy night laboratory mood, purple light, soft magenta and green fluorescent accents, medium brightness.
Scene: inside the same night lab world, on a round table in the center, a block made of many small glowing cubes is being carved into the shape of a mug with a handle; several small cameras on tripods stand in a circle around the table; on the back wall, a flashlight casts two shadows, a donut shadow with a hole and a bowl shadow that is solid.
All four characters together:
  anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat, transparent wings, on the left facing right, pointing proudly at a neat ring of eight cameras;
  small boxy retro computer robot with a beige rounded-corner CRT-monitor head, a big dark green screen face with mint pixel eyes and mouth, a thin antenna on a small gray base topped with one small red-brown abacus bead, a small beige box body, chunky gray segmented tube arms with round gray mitten hands, two dark gray tank treads instead of legs, about three quarters the height of the scientist, on the right facing left, hugging an armful of many cameras, holding a small wooden abacus, confident;
  chibi scientist with round glasses, black hair with one white streak, white lab coat over black vest and tie, at the back center, shining a flashlight at a donut and a bowl, thinking;
  girl researcher with pink hair in two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, in the front center, carving the cube block with a small carving tool, smiling.
Visual metaphor of the topic: carving a block of small cubes into a mug using views from many cameras, and a donut shadow with a hole next to a solid bowl shadow.
Composition: the main props fill the upper half and are large and crisp; keep every face and hand inside the central safe area (10% margin left and right, 15% top and bottom); keep the bottom-left corner dark and simple.
Mood: curious, friendly rivalry, the moment before the result, nobody winning yet.
No white glossy round robot head, no black pill-shaped visor, no yellow eyes, no ball-shaped antenna knob, no cyan chest light, no floating robot, no gold coins. No text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands.
```

### B10. 2-5 머그컵을 3D로 (중간 미션) (cover_2-5) → `cover_2-5.png`

```
웹페이지 첫 화면 배경으로 쓰는 표지 그림 1장을 만들어 줘.
- 비율 16:9, 가로 1920px 이상
- 첨부한 참고 이미지의 네 캐릭터(박사, 조수, 초파리 연구원, 주판봇)를 같은 그림체·같은 외형으로, 넷 모두 등장
- 주판봇은 새 외형(참고 그림 E13_neutral)대로: 베이지색 CRT 모니터 머리와 작은 상자 몸, 짙은 초록 화면에 민트 픽셀 눈·입, 끝에 적갈색 주판알 하나가 달린 가는 안테나, 회색 마디 팔과 벙어리장갑 손, 짙은 회색 무한궤도 두 개로 바닥에 선다(떠 있지 않음). 키는 박사의 약 3/4. 흰 둥근 머리·검은 알약 화면·노란 눈·금화는 넣지 말 것
- 그림 안에 글자·숫자·로고를 넣지 말 것
- 가운데 유리 탁자 위 진짜 머그컵, 위와 탁자 밑에서 작은 깊이 카메라들이 부드러운 빛줄기를 비춤
- 그 위 공중에 작은 블록으로 된 3D 머그컵이 떠 있고, 컵 속이 비어 있는 것이 보임
- 위아래가 조금 잘린 16:7 띠로 쓰일 수 있으니, 얼굴과 손은 세로 가운데 70% 안에 두기
- 왼쪽 아래 구석은 어둡고 단순하게 (제목 칩이 올라감)
아래 영어 프롬프트를 그대로 써 줘.

Website hero background illustration, wide 16:9.
Match the art style, proportions and colors of the attached reference images exactly: 16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights.
Cozy night laboratory mood, purple light, soft magenta and green fluorescent accents, medium brightness.
Scene: inside the same night lab world, on a glass table in the center a real mug, small depth cameras above and below the glass table shine soft light beams into it; floating above, a 3D mug built from small glowing cubes, clearly hollow inside with its handle.
All four characters together:
  anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat, transparent wings, on the left facing right, holding four small depth cameras and pointing at the floating mug;
  small boxy retro computer robot with a beige rounded-corner CRT-monitor head, a big dark green screen face with mint pixel eyes and mouth, a thin antenna on a small gray base topped with one small red-brown abacus bead, a small beige box body, chunky gray segmented tube arms with round gray mitten hands, two dark gray tank treads instead of legs, about three quarters the height of the scientist, on the right facing left, carrying a big stack of photos, holding a small wooden abacus, confident;
  chibi scientist with round glasses, black hair with one white streak, white lab coat over black vest and tie, at the back center, dipping a ruler into the real mug to measure its depth, thinking;
  girl researcher with pink hair in two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, in the front center, looking up at the floating cube mug, smiling.
Visual metaphor of the topic: light beams measuring how far away the inside of a mug is, and a hollow cube-built mug floating above the real one.
Composition: the main props fill the upper half and are large and crisp; keep every face and hand inside the central safe area (10% margin left and right, 15% top and bottom); keep the bottom-left corner dark and simple.
Mood: curious, friendly rivalry, the moment before the result, nobody winning yet.
No white glossy round robot head, no black pill-shaped visor, no yellow eyes, no ball-shaped antenna knob, no cyan chest light, no floating robot, no gold coins. No text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands.
```

### B11. 3-1 작게 그리고 크게 (cover_3-1) → `cover_3-1.png`

```
웹페이지 첫 화면 배경으로 쓰는 표지 그림 1장을 만들어 줘.
- 비율 16:9, 가로 1920px 이상
- 첨부한 참고 이미지의 네 캐릭터(박사, 조수, 초파리 연구원, 주판봇)를 같은 그림체·같은 외형으로, 넷 모두 등장
- 주판봇은 새 외형(참고 그림 E13_neutral)대로: 베이지색 CRT 모니터 머리와 작은 상자 몸, 짙은 초록 화면에 민트 픽셀 눈·입, 끝에 적갈색 주판알 하나가 달린 가는 안테나, 회색 마디 팔과 벙어리장갑 손, 짙은 회색 무한궤도 두 개로 바닥에 선다(떠 있지 않음). 키는 박사의 약 3/4. 흰 둥근 머리·검은 알약 화면·노란 눈·금화는 넣지 말 것
- 그림 안에 글자·숫자·로고를 넣지 말 것 (모니터 화면에도 글자 없이)
- 왼쪽 작은 모니터는 큼직한 픽셀로 깨진 화면, 오른쪽 큰 모니터는 같은 장면의 선명한 화면. 둘 다 크고 또렷하게, 화면 위쪽 절반을 채우도록
- 화면 속 블록은 테트리스처럼 같은 모양 같은 색: 막대 하늘색, 네모 노랑, T자 보라, L자 주황
- 위아래가 조금 잘린 16:7 띠로 쓰이니, 얼굴과 손은 세로 가운데 70% 안에 두기
- 왼쪽 아래 구석은 어둡고 단순하게 (제목 칩이 올라감)
아래 영어 프롬프트를 그대로 써 줘.

Website hero background illustration, wide 16:9.
Match the art style, proportions and colors of the attached reference images exactly: 16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights.
Cozy night laboratory mood, purple light, soft magenta and green fluorescent accents, medium brightness.
Scene: inside the same night lab world. On the left, a small monitor showing a Tetris-like game screen rendered at low resolution, with big blocky pixels and jagged stair-step edges. On the right, a large monitor showing exactly the same game screen sharp and smooth, with clean thin borders and soft highlights on every block. Tetris-style blocks keep one color per shape: cyan straight pieces, yellow squares, purple T pieces, orange L pieces. On the workbench in the middle, a floating magnified 3x3 square of pixels, and behind it a sharper, more detailed version of the same square sliding into place like a puzzle piece. A few glowing abacus beads on the floor.
All four characters together:
  girl researcher with pink hair in two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, in the front center looking through a big magnifying glass at the floating 3x3 pixel square, focused;
  chibi scientist with round glasses, black hair with one white streak, white lab coat over black vest and tie, at the back center pointing at the sharp right monitor, explaining;
  anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat, transparent wings, on the left facing right, standing next to the jagged small monitor with arms crossed, skeptical;
  small boxy retro computer robot with a beige rounded-corner CRT-monitor head, a big dark green screen face with mint pixel eyes and mouth, a thin antenna on a small gray base topped with one small red-brown abacus bead, a small beige box body, chunky gray segmented tube arms with round gray mitten hands, two dark gray tank treads instead of legs, about three quarters the height of the scientist, on the right facing left, flicking glowing abacus beads.
Visual metaphor of the topic: render small, then fill in the missing detail by learning — rough small screen to sharp big screen.
Composition: both monitors fill the upper half and are large and crisp; keep every face and hand inside the central safe area (10% margin left and right, 15% top and bottom); keep the bottom-left corner dark and simple; light falls on the magnified pixel square.
Mood: curious, friendly rivalry, the moment before the result, nobody winning yet.
No white glossy round robot head, no black pill-shaped visor, no yellow eyes, no ball-shaped antenna knob, no cyan chest light, no floating robot, no gold coins. No text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands.
```

### B12. 3-2 시간이 도와준다 (cover_3-2) → `cover_3-2.png`

```
웹페이지 첫 화면 배경으로 쓰는 표지 그림 1장을 만들어 줘.
- 비율 16:9, 가로 1920px 이상
- 첨부한 참고 이미지의 네 캐릭터(박사, 조수, 초파리 연구원, 주판봇)를 같은 그림체·같은 외형으로, 넷 모두 등장
- 주판봇은 새 외형(참고 그림 E13_neutral)대로: 베이지색 CRT 모니터 머리와 작은 상자 몸, 짙은 초록 화면에 민트 픽셀 눈·입, 끝에 적갈색 주판알 하나가 달린 가는 안테나, 회색 마디 팔과 벙어리장갑 손, 짙은 회색 무한궤도 두 개로 바닥에 선다(떠 있지 않음). 키는 박사의 약 3/4. 흰 둥근 머리·검은 알약 화면·노란 눈·금화는 넣지 말 것
- 그림 안에 글자·숫자·로고를 넣지 말 것 (화면 판에도 글자 없이)
- 같은 게임 화면이 반투명한 판 여러 장으로 겹쳐 있고, 뒤쪽 판은 거칠고 앞쪽 판일수록 선명하게. 판들이 화면 위쪽 절반을 채우도록 크고 또렷하게
- 화면 속 블록은 테트리스처럼 같은 모양 같은 색: 막대 하늘색, 네모 노랑, T자 보라, L자 주황. 떨어지는 블록에는 아래를 가리키는 흰 화살표
- 위아래가 조금 잘린 16:7 띠로 쓰이니, 얼굴과 손은 세로 가운데 70% 안에 두기
- 왼쪽 아래 구석은 어둡고 단순하게 (제목 칩이 올라감)
아래 영어 프롬프트를 그대로 써 줘.

Website hero background illustration, wide 16:9.
Match the art style, proportions and colors of the attached reference images exactly: 16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights.
Cozy night laboratory mood, purple light, soft magenta and green fluorescent accents, medium brightness.
Scene: inside the same night lab world, five or six translucent glass panels float in a row from back to front, each showing the same Tetris-like game screen; the panels at the back look rough and blocky, the panels toward the front get sharper and cleaner, as if many frames are being stacked into one clear picture. Tetris-style blocks keep one color per shape: cyan straight pieces, yellow squares, purple T pieces, orange L pieces. Several falling blocks carry small white arrows pointing down (motion). On one panel, a falling purple block leaves a faint ghostly trail above it.
All four characters together:
  anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat, transparent wings, on the left facing right, cutting away the faint ghostly trail from one panel with a big pair of scissors;
  girl researcher with pink hair in two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, in the front center flipping through the stacked panels and peeking between them, curious;
  chibi scientist with round glasses, black hair with one white streak, white lab coat over black vest and tie, at the back center pointing at the white arrows on the falling blocks;
  small boxy retro computer robot with a beige rounded-corner CRT-monitor head, a big dark green screen face with mint pixel eyes and mouth, a thin antenna on a small gray base topped with one small red-brown abacus bead, a small beige box body, chunky gray segmented tube arms with round gray mitten hands, two dark gray tank treads instead of legs, about three quarters the height of the scientist, on the right facing left, hugging an armful of panels tightly as if refusing to throw any away.
Visual metaphor of the topic: time helps — stack many frames for real detail, follow the motion arrows, cut away memories that no longer match.
Composition: the stacked panels fill the upper half and are large and crisp; keep every face and hand inside the central safe area (10% margin left and right, 15% top and bottom); keep the bottom-left corner dark and simple.
Mood: curious, friendly rivalry, the moment before the result, nobody winning yet.
No white glossy round robot head, no black pill-shaped visor, no yellow eyes, no ball-shaped antenna knob, no cyan chest light, no floating robot, no gold coins. No text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands.
```

### B13. 3-3 사이 프레임 (cover_3-3) → `cover_3-3.png`

```
웹페이지 첫 화면 배경으로 쓰는 표지 그림 1장을 만들어 줘.
- 비율 16:9, 가로 1920px 이상
- 첨부한 참고 이미지의 네 캐릭터(박사, 조수, 초파리 연구원, 주판봇)를 같은 그림체·같은 외형으로, 넷 모두 등장
- 주판봇은 새 외형(참고 그림 E13_neutral)대로: 베이지색 CRT 모니터 머리와 작은 상자 몸, 짙은 초록 화면에 민트 픽셀 눈·입, 끝에 적갈색 주판알 하나가 달린 가는 안테나, 회색 마디 팔과 벙어리장갑 손, 짙은 회색 무한궤도 두 개로 바닥에 선다(떠 있지 않음). 키는 박사의 약 3/4. 흰 둥근 머리·검은 알약 화면·노란 눈·금화는 넣지 말 것
- 그림 안에 글자·숫자·로고를 넣지 말 것
- 가로로 긴 필름 띠가 화면 위쪽 절반을 가로지르고, 칸마다 같은 게임 장면이 조금씩 움직인다. 파란 테두리 칸(진짜 장면)과 노란 테두리 칸(AI가 만든 사이 장면)이 번갈아
- 화면 속 블록은 테트리스처럼 같은 모양 같은 색: 막대 하늘색, 네모 노랑, T자 보라, L자 주황. 몇 칸에는 주황 불꽃
- 위아래가 조금 잘린 16:7 띠로 쓰이니, 얼굴과 손은 세로 가운데 70% 안에 두기
- 왼쪽 아래 구석은 어둡고 단순하게 (제목 칩이 올라감)
아래 영어 프롬프트를 그대로 써 줘.

Website hero background illustration, wide 16:9.
Match the art style, proportions and colors of the attached reference images exactly: 16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights.
Cozy night laboratory mood, purple light, soft magenta and green fluorescent accents, medium brightness.
Scene: inside the same night lab world, a long horizontal film strip floats across the upper half. Its frames alternate: frames with a blue border (really rendered) and frames with a softly glowing yellow border (generated in-between frames). In every frame the same Tetris-like game scene moves a little; blocks keep one color per shape: cyan straight pieces, yellow squares, purple T pieces, orange L pieces. In some frames small orange-white sparks fly across. Thin blue arrows come out of a small engine box and attach only to the moving blocks; thin yellow arrows come out of a big magnifying glass and attach to both the blocks and the sparks. In the lower right, a game controller and a small hourglass.
All four characters together:
  anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat, transparent wings, on the left facing right, comparing two frames through a big magnifying glass and drawing yellow arrows;
  small boxy retro computer robot with a beige rounded-corner CRT-monitor head, a big dark green screen face with mint pixel eyes and mouth, a thin antenna on a small gray base topped with one small red-brown abacus bead, a small beige box body, chunky gray segmented tube arms with round gray mitten hands, two dark gray tank treads instead of legs, about three quarters the height of the scientist, on the right facing left, pulling a bundle of blue arrows out of the engine box;
  chibi scientist with round glasses, black hair with one white streak, white lab coat over black vest and tie, at the back center pointing at a glowing yellow in-between frame;
  girl researcher with pink hair in two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, in the front center holding the game controller and looking at the hourglass with a puzzled tilt of the head.
Visual metaphor of the topic: making frames that were never drawn — in-between frames slotted into a film strip, two kinds of motion arrows, and the question of delay.
Composition: the film strip fills the upper half and is large and crisp; keep every face and hand inside the central safe area (10% margin left and right, 15% top and bottom); keep the bottom-left corner dark and simple.
Mood: curious, friendly rivalry, the moment before the result, nobody winning yet.
No white glossy round robot head, no black pill-shaped visor, no yellow eyes, no ball-shaped antenna knob, no cyan chest light, no floating robot, no gold coins. No text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands.
```

### B14. 3-4 AI가 빛을 다시 그린다 (cover_3-4) → `cover_3-4.png`

```
웹페이지 첫 화면 배경으로 쓰는 표지 그림 1장을 만들어 줘.
- 비율 16:9, 가로 1920px 이상
- 첨부한 참고 이미지의 네 캐릭터(박사, 조수, 초파리 연구원, 주판봇)를 같은 그림체·같은 외형으로, 넷 모두 등장
- 주판봇은 새 외형(참고 그림 E13_neutral)대로: 베이지색 CRT 모니터 머리와 작은 상자 몸, 짙은 초록 화면에 민트 픽셀 눈·입, 끝에 적갈색 주판알 하나가 달린 가는 안테나, 회색 마디 팔과 벙어리장갑 손, 짙은 회색 무한궤도 두 개로 바닥에 선다(떠 있지 않음). 키는 박사의 약 3/4. 흰 둥근 머리·검은 알약 화면·노란 눈·금화는 넣지 말 것
- 그림 안에 글자·숫자·로고를 넣지 말 것
- 화면 위쪽 절반에 긴 진열대. 천장의 가로로 긴 막대 조명이 테트리스 블록을 비춰 부드러운 그림자가 진다
- 진열대 왼쪽 절반은 자글자글한 점(잡음)으로 덮여 있고, 가운데 반짝이는 신경망 그물이 지나간 오른쪽 절반은 그림자가 매끄럽다
- 블록은 테트리스처럼 같은 모양 같은 색: 막대 하늘색, 네모 노랑, T자 보라, L자 주황
- 위아래가 조금 잘린 16:7 띠로 쓰이니, 얼굴과 손은 세로 가운데 70% 안에 두기
- 왼쪽 아래 구석은 어둡고 단순하게 (제목 칩이 올라감)
아래 영어 프롬프트를 그대로 써 줘.

Website hero background illustration, wide 16:9.
Match the art style, proportions and colors of the attached reference images exactly: 16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights.
Cozy night laboratory mood, purple light, soft magenta and green fluorescent accents, medium brightness.
Scene: inside the same night lab world, a long display shelf fills the upper half. A long horizontal bar lamp hangs from the ceiling above it and lights Tetris-like blocks standing on the shelf, casting soft shadows. Blocks keep one color per shape: cyan straight pieces, yellow squares, purple T pieces, orange L pieces. The left half of the shelf is covered in grainy speckled noise like an old TV screen, with a few thin light rays from the lamp to the blocks, some of them cut off where a block is in the way. In the middle a glowing small neural network net (dots connected by lines) sweeps across, and the right half behind it shows clean, smooth soft shadows.
All four characters together:
  anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat, transparent wings, on the left facing right, sifting the grainy speckles through a square hand sieve;
  small boxy retro computer robot with a beige rounded-corner CRT-monitor head, a big dark green screen face with mint pixel eyes and mouth, a thin antenna on a small gray base topped with one small red-brown abacus bead, a small beige box body, chunky gray segmented tube arms with round gray mitten hands, two dark gray tank treads instead of legs, about three quarters the height of the scientist, on the right facing left, spreading the glowing neural network net with both arms;
  chibi scientist with round glasses, black hair with one white streak, white lab coat over black vest and tie, at the back center looking up and pointing at the long ceiling lamp;
  girl researcher with pink hair in two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, in the front center holding a camera and comparing the grainy side with the smooth side.
Visual metaphor of the topic: a few light rays give a grainy picture, and a learned filter redraws the light smoothly.
Composition: the shelf and lamp fill the upper half and are large and crisp; keep every face and hand inside the central safe area (10% margin left and right, 15% top and bottom); keep the bottom-left corner dark and simple.
Mood: curious, friendly rivalry, the moment before the result, nobody winning yet.
No white glossy round robot head, no black pill-shaped visor, no yellow eyes, no ball-shaped antenna knob, no cyan chest light, no floating robot, no gold coins. No text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands.
```

### B15. 3-5 최종 미션: 어느 각도에서든 조수 (cover_3-5) → `cover_3-5.png`

```
웹페이지 첫 화면 배경으로 쓰는 표지 그림 1장을 만들어 줘.
- 비율 16:9, 가로 1920px 이상
- 첨부한 참고 이미지의 네 캐릭터(박사, 조수, 초파리 연구원, 주판봇)를 같은 그림체·같은 외형으로, 넷 모두 등장
- 주판봇은 새 외형(참고 그림 E13_neutral)대로: 베이지색 CRT 모니터 머리와 작은 상자 몸, 짙은 초록 화면에 민트 픽셀 눈·입, 끝에 적갈색 주판알 하나가 달린 가는 안테나, 회색 마디 팔과 벙어리장갑 손, 짙은 회색 무한궤도 두 개로 바닥에 선다(떠 있지 않음). 키는 박사의 약 3/4. 흰 둥근 머리·검은 알약 화면·노란 눈·금화는 넣지 말 것
- 그림 안에 글자·숫자·로고를 넣지 말 것
- 화면 위쪽 가운데에 둥근 사진관 돌림판. 그 위에 공 모양으로 단순하게 만든 조수 흉상(분홍 쪽머리 둘, 남색 줄, 파란 눈, 흰 가운)
- 흉상 둘레를 작은 카메라 여러 대가 둥근 궤도로 돌고, 찍힌 앞·옆·뒤 사진이 작은 액자로 공중에 떠 있다
- 조금 뒤에 닮은 흉상 둘(분홍 단발, 갈색 쪽머리). 탁자 위에 빨간 봉인 도장이 찍힌 두툼한 봉투
- 위아래가 조금 잘린 16:7 띠로 쓰이니, 얼굴과 손은 세로 가운데 70% 안에 두기
- 왼쪽 아래 구석은 어둡고 단순하게 (제목 칩이 올라감)
아래 영어 프롬프트를 그대로 써 줘.

Website hero background illustration, wide 16:9.
Match the art style, proportions and colors of the attached reference images exactly: 16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights.
Cozy night laboratory mood, purple light, soft magenta and green fluorescent accents, medium brightness.
Scene: inside the same night lab world, a round photo-studio turntable stands in the upper center. On it sits a simple bust of the girl researcher built from smooth spheres: pink hair with two round buns and a navy streak, blue eyes, white coat. Several small cameras circle the bust on a glowing circular orbit, and the photos they took — front, side and back of the bust — float nearby as small picture frames. Slightly behind stand two look-alike sphere busts: one with a pink bob and no buns, one with brown hair and two buns. On a side table lies a thick envelope sealed with a red wax seal.
All four characters together:
  anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat, transparent wings, on the left facing right, holding the sealed envelope tightly with both hands, guarding it;
  small boxy retro computer robot with a beige rounded-corner CRT-monitor head, a big dark green screen face with mint pixel eyes and mouth, a thin antenna on a small gray base topped with one small red-brown abacus bead, a small beige box body, chunky gray segmented tube arms with round gray mitten hands, two dark gray tank treads instead of legs, about three quarters the height of the scientist, on the right facing left, hugging an armful of floating picture frames while glancing sideways at the envelope;
  chibi scientist with round glasses, black hair with one white streak, white lab coat over black vest and tie, at the back center tracing the circular camera orbit with one finger;
  girl researcher with pink hair in two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, in the front center next to her bust, turning her head to show her two buns from behind, smiling.
Visual metaphor of the topic: rendering a 3D character cheaply from every angle, learning from rendered photos, and keeping the test photos sealed.
Composition: the turntable, orbit and floating frames fill the upper half and are large and crisp; keep every face and hand inside the central safe area (10% margin left and right, 15% top and bottom); keep the bottom-left corner dark and simple.
Mood: curious, a final mission, friendly rivalry, the moment before the result.
No white glossy round robot head, no black pill-shaped visor, no yellow eyes, no ball-shaped antenna knob, no cyan chest light, no floating robot, no gold coins. No text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands.
```

---
## C. 3부작 첫 화면 대표 그림 — 정사각 1280×1280 (trilogy/index.html)

### C1. 3부작 대표 그림 → `cover_landing.png`

```
웹페이지 첫 화면 맨 위에 거는 시리즈 대표 그림 1장을 만들어 줘.
- 비율 1:1, 1280×1280px
- 첨부한 참고 이미지의 네 캐릭터(박사, 조수, 초파리 연구원, 주판봇)를 같은 그림체·같은 외형으로, 넷 모두 등장
- 주판봇은 새 외형(참고 그림 E13_neutral)대로: 베이지색 CRT 모니터 머리와 작은 상자 몸, 짙은 초록 화면에 민트 픽셀 눈·입, 끝에 적갈색 주판알 하나가 달린 가는 안테나, 회색 마디 팔과 벙어리장갑 손, 짙은 회색 무한궤도 두 개로 바닥에 선다(떠 있지 않음). 키는 박사의 약 3/4. 흰 둥근 머리·검은 알약 화면·노란 눈·금화는 넣지 말 것
- 그림 안에 글자·숫자·로고를 넣지 말 것
- 3부작 시리즈 대표 그림: 왼쪽에 테트리스 블록과 천 주머니(1부), 가운데에 떠오르는 3D 머그컵과 사진 액자 고리(2부), 오른쪽에 거친 화면과 선명한 화면의 모니터 두 대(3부). 두 모니터는 같은 장면이어야 한다
- 블록은 같은 모양 같은 색: 막대 하늘색, 네모 노랑, T자 보라. 머그컵은 흰색에 자홍색 띠 하나
- 가로 16:9로 잘려 쓰이니, 얼굴·손과 주요 소품은 모두 세로 가운데(높이 25~75%) 띠 안에, 위아래는 어두운 벽과 작업대처럼 단순한 배경으로
아래 영어 프롬프트를 그대로 써 줘.

Square website hero illustration, 1:1, 1280x1280.
Match the art style, proportions and colors of the attached reference images exactly: 16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights.
Cozy night laboratory mood, teal-green and purple light, warm hanging lamps, medium brightness.
Scene: one long workbench in the same night lab world, seen at eye level, showing a journey from left to right in three zones.
Left zone: a small pile of large Tetris-style blocks — cyan straight pieces, yellow 2x2 squares, purple T pieces (same shape always same color) — and two open cloth drawstring pouches holding sorted blocks.
Center zone: a compact ring of small framed photos of a white mug with one magenta stripe, and inside the ring a glowing 3D mug rising, half wireframe and half solid.
Right zone: two small gaming monitors side by side showing the very same Tetris game screen, the left one blocky and low-resolution, the right one sharp and smooth, a soft beam of light flowing between them.
All four characters together, close around the workbench:
  anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat, transparent wings, at the left facing right, dropping a T-shaped block into a pouch;
  chibi scientist with round glasses, black hair with one white streak, white lab coat over black vest and tie, at the back center, both arms open as if presenting the whole journey;
  girl researcher with pink hair in two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, in the front center-right, holding a real mug and looking toward the sharp monitor, smiling;
  small boxy retro computer robot with a beige rounded-corner CRT-monitor head, a big dark green screen face with mint pixel eyes and mouth, a thin antenna on a small gray base topped with one small red-brown abacus bead, a small beige box body, chunky gray segmented tube arms with round gray mitten hands, two dark gray tank treads instead of legs, about three quarters the height of the scientist, at the right facing left, flicking the beads of a small wooden abacus.
Visual metaphor: a three-part journey — sorting without labels, turning photos back into 3D, drawing less and letting AI fill the rest.
Composition: square frame; all faces, hands and main props stay inside the middle horizontal band from 25% to 75% of the height and inside 10% side margins; the top quarter is a dim lab wall with soft lights, the bottom quarter is the plain front edge of the workbench.
Mood: curious, warm, a team at the start of an adventure.
No white glossy round robot head, no black pill-shaped visor, no yellow eyes, no ball-shaped antenna knob, no cyan chest light, no floating robot, no gold coins. No text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands.
```
