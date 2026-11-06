# 표지 지시문 — 3부 적게 그리고 AI로 채우기 (cover_ch3)

| 항목 | 내용 |
|---|---|
| 키 · 판 | cover_ch3 · L (16:9, 가로 1920 이상). 3부 목차(`part3/index.html`)의 큰 표지 |
| 장소 (앵커) | D 생활·현장 — 같은 밤의 연구실. 게임용 모니터 세 대가 나란히 있는 책상 |
| 주제 은유 | 왼쪽 모니터: 거칠고 계단진 작은 화면(테트리스 블록이 큼직한 픽셀로 깨짐) → 가운데: 빛나는 신경망 상자(점과 선만, 글자 없음) → 오른쪽 모니터: 선명하고 매끄러운 큰 화면. 화면 속 블록은 같은 모양 같은 색(막대 하늘, 네모 노랑, T자 보라, L자 주황) |
| 네 캐릭터 포즈 | 박사: 가운데 뒤, 두 손에 보랏빛 불꽃으로 신경망 상자를 가리킴 / 조수: 오른쪽 모니터 앞에서 자기 얼굴이 비친 화면을 들여다보며 기대 / 초파리: 왼쪽에서 오른쪽을 보며 계단진 화면을 돋보기로 의심스럽게 봄 / 주판봇: 오른쪽에서 왼쪽을 보며 빛나는 주판알이 달린 나무 주판(아낀 픽셀)를 안고 있음 |
| 대체 글 (alt) | 밤의 연구실, 거칠게 작게 그린 게임 화면이 AI를 거쳐 선명하고 매끄러운 큰 화면으로 바뀌는 앞에 네 캐릭터가 선 3부 표지 |
| 다른 부와 다른 점 | 1부는 블록 더미·주머니·사진, 2부는 머그컵·카메라. 3부는 모니터·화면·신경망 상자만 쓴다 |

**참고 이미지 (함께 올리기):** 캐릭터 팩 기본 그림 4장 — `doc_e13`, `asst_e13`, `fly_e13`, 주판봇 `images/jupanbot/E13_neutral.png` (adminmrobo/fruitfly-lab-expressions, 커밋 5269662 — 2026-11-05 새 픽셀 그림).

**Genspark에 붙여 넣기 ↓**
```
웹페이지 맨 위에 거는 표지 그림 1장을 만들어 줘.
- 비율 16:9, 가로 1920px 이상
- 첨부한 참고 이미지의 네 캐릭터(박사, 조수, 초파리 연구원, 주판봇)를 같은 그림체·같은 외형으로, 넷 모두 등장
- 주판봇은 새 외형(참고 그림 E13_neutral)대로: 베이지색 CRT 모니터 머리와 작은 상자 몸, 짙은 초록 화면에 민트 픽셀 눈·입, 끝에 적갈색 주판알 하나가 달린 가는 안테나, 회색 마디 팔과 벙어리장갑 손, 짙은 회색 무한궤도 두 개로 바닥에 선다(떠 있지 않음). 키는 박사의 약 3/4. 흰 둥근 머리·검은 알약 화면·노란 눈·금화는 넣지 말 것
- 그림 안에 글자·숫자·로고를 넣지 말 것 (모니터 화면에도 글자 없이)
- 왼쪽 모니터는 큼직한 픽셀로 깨진 거친 화면, 오른쪽 모니터는 같은 장면이 선명한 화면이어야 한다. 비교가 한눈에 보이게 모니터를 크게
- 화면 속 블록은 테트리스처럼 같은 모양 같은 색: 막대 하늘색, 네모 노랑, T자 보라, L자 주황
- 얼굴과 손은 가운데 영역에, 왼쪽 아래 구석은 어둡고 단순하게
아래 영어 프롬프트를 그대로 써 줘.

Website top cover illustration, wide 16:9.
Match the art style, proportions and colors of the attached reference images exactly: 16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights.
Cozy night laboratory mood, purple light, soft magenta and green fluorescent accents, medium brightness.
Scene: a long desk in the same night lab world with three gaming monitors in a row. The left monitor shows a Tetris-like game screen rendered at very low resolution — big blocky jagged pixels, broken thin lines. The middle shows a glowing box of a small neural network made only of dots and connecting lines, no text. The right monitor shows the very same game screen, sharp and smooth at high resolution. On both screens, Tetris-style blocks keep one color per shape: cyan straight pieces, yellow squares, purple T pieces, orange L pieces. A soft beam of light flows from the left monitor through the neural box into the right monitor.
All four characters together:
  chibi scientist with round glasses, black hair with one white streak, white lab coat over black vest and tie, at the back center pointing at the glowing neural box with purple sparks in both hands;
  girl researcher with pink hair in two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, at the right side leaning toward the sharp right monitor, curious and hopeful;
  anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat, transparent wings, on the left facing right, inspecting the jagged left monitor with a magnifying glass, skeptical;
  small boxy retro computer robot with a beige rounded-corner CRT-monitor head, a big dark green screen face with mint pixel eyes and mouth, a thin antenna on a small gray base topped with one small red-brown abacus bead, a small beige box body, chunky gray segmented tube arms with round gray mitten hands, two dark gray tank treads instead of legs, about three quarters the height of the scientist, on the right facing left, hugging a small wooden abacus with glowing beads.
Visual metaphor of the topic: render less, let AI fill the rest — the same scene going from rough and small to sharp and large.
Composition: the three monitors fill the upper half and are large and readable; keep every face and hand inside the central safe area (12% margin left and right, 10% top, 18% bottom); keep the bottom-left corner dark and simple.
Mood: curious, friendly rivalry, the moment before the result.
No white glossy round robot head, no black pill-shaped visor, no yellow eyes, no ball-shaped antenna knob, no cyan chest light, no floating robot, no gold coins. No text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands.
```

**고칠 때 (같은 대화에서):** `Same four characters, same art style and composition. Change only: {고칠 점}. Still no text.`
- 두 화면이 비슷해 보이면: `Change only: make the left monitor much more blocky and jagged, with pixels four times bigger; keep the right monitor sharp.`
- 색이 섞이면: `Change only: every straight block cyan, every square block yellow, every T block purple, every L block orange.`

**받은 뒤:** 16:9·글자 없음·네 캐릭터 외형 확인 → WebP 1600×900 (220 KB 이하) → `part3/index.html`의 `data-img="cover_ch3"` 자리에 큰 표지로 넣는다. 지금은 캔버스 대체 표지(작은 화면 → AI 상자 → 큰 화면 + 네 캐릭터)가 들어가 있다.
