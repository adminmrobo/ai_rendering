# 시리즈 공용 이미지 명세서 — AI 렌더링 연구실 (3부작)

| 항목 | 내용 |
|---|---|
| 시리즈 | 1부 정답표 없이 배우기 (1-1~1-5) · 2부 렌더링을 거꾸로 (2-1~2-5) · 3부 적게 그리고 AI로 채우기 (3-1~3-5) |
| 시즌 | 기본 |
| 캐릭터 | 캐릭터 팩 v1.0 (`adminmrobo/fruitfly-lab-expressions`, 커밋 ea5da3f), 96px WebP 22키를 페이지에 넣어 씀 |

## 1. 공용 표정 (팩 대응)
| 키 | 팩 | 대응 | 키 | 팩 | 대응 |
|---|---|---|---|---|---|
| doc_front | doc_e08 | 정확 | fly_point | fly_e08 | 정확 (왼쪽을 가리켜 대결에서 좌우 뒤집음) |
| doc_think | doc_e09 | 정확 | fly_clip | fly_e10 | 정확 |
| doc_magic | doc_e16 | 정확 | fly_arms | fly_e16 | 정확 |
| doc_judge | doc_e10 | 근사 (윙크·엄지) | fly_coffee | fly_e13 | 정확 |
| doc_scale | doc_e13 | 없음 → 기본 표정 | fly_cry | fly_e21 | 정확 |
| asst_smile | asst_e13 | 정확 | robo_smile | robo_e13 | 정확 |
| asst_firm | asst_e12 | 정확 | robo_coin | robo_e16 | 정확 |
| asst_spark | asst_e01 | 정확 | robo_calc | robo_e09 | 근사 (톱니 생각) |
| asst_ledger | asst_e07 | 없음 → 설명 표정 | robo_happy | robo_e12 | 정확 |
| asst_shock | asst_e24 | 정확 | robo_sigh / meh / blush | e20 / e18 / e14 | 근사 / 정확 / 정확 |

팩에 없는 장면(저울, 장부, 계산기)은 근사 표정으로 대신한다. 꼭 필요해지면 SKILL 18-5 문구로 새로 만든다.

## 2. 부 표지 (챕터 = 부)
| 키 | 판 | 쓰는 곳 | 상태 | 주제 소품 (겹치지 않게) |
|---|---|---|---|---|
| cover_ch1 | L | 1부 목차 + 1-1 표지 | 지시문 있음 (part1/COVER_ch1) | 테트리스 블록 더미, 천 주머니, 이름표 없는 사진 |
| cover_1-2 | L | 1-2 표지 (16:7) | 지시문 있음 (part1/COVER_1-2) | 크기·방향 제각각인 블록 네 종류, 주머니 네 개, 큰 자, 족보 |
| cover_1-3 | L | 1-3 표지 (16:7) | 지시문 있음 (part1/COVER_1-3) | 바닥의 빈 종이 지도, 접혀 내려앉는 얼굴 카드, 네 무리의 점, 가위 |
| cover_1-4 | L | 1-4 표지 (16:7) | 지시문 있음 (part1/COVER_1-4) | 가운데가 잘록한 모래시계 기계, 가려진 얼굴 카드, 빈칸 연습지, 앨범과 가위 |
| cover_1-5 | L | 1-5 표지 (16:7) | 지시문 있음 (part1/COVER_1-5) | 코르크 게시판, 여러 각도의 흉상 사진, 이름표 리본과 실, 팔레트 |
| cover_2-2 | L | 2-2 표지 (16:7) | 지시문 있음 (part2/COVER_2-2) | 이젤의 컵 사진, 점점 닮아 가는 몽타주 줄, 바둑판과 흩뿌린 그림 |
| cover_2-3 | L | 2-3 표지 (16:7) | 지시문 있음 (part2/COVER_2-3) | 공이 멈춘 계단 모형과 공이 구르는 미끄럼틀 모형, 또렷한 실루엣과 번진 실루엣 |
| cover_2-4 | L | 2-4 표지 (16:7) | 지시문 있음 (part2/COVER_2-4) | 둘레의 사진기들, 정육면체 블록을 깎아 드러나는 머그컵, 도넛과 그릇 그림자 |
| cover_2-5 | L | 2-5 표지 (16:7) | 지시문 있음 (part2/COVER_2-5) | 유리 탁자 위 머그컵과 위·아래 깊이 카메라, 컵 속이 빈 3D 블록 머그컵 |
| cover_ch3 | L | 3부 목차 표지 | 지시문 있음 (part3/COVER_ch3) | 모니터 세 대(거친 화면 → 신경망 상자 → 선명한 화면) |
| cover_3-1 | L | 3-1 표지 (16:7) | 지시문 있음 (part3/COVER_3-1) | 작은 모니터·큰 모니터, 돋보기 속 3×3 픽셀 조각 |
| cover_3-2 | L | 3-2 표지 (16:7) | 지시문 있음 (part3/COVER_3-2) | 겹쳐 쌓인 화면 판, 모션 벡터 화살표, 잔상 꼬리와 가위 |
| cover_3-3 | L | 3-3 표지 (16:7) | 지시문 있음 (part3/COVER_3-3) | 필름 띠(진짜·사이 장면 번갈아), 파란·노란 화살표, 게임 패드와 모래시계 |
| cover_3-5 | L | 3-5 표지 (16:7) | 지시문 있음 (part3/COVER_3-5) | 둥근 돌림판과 도는 카메라, 공 모양 조수 흉상, 떠 있는 액자, 빨간 봉인 봉투 |
| cover_3-4 | L | 3-4 표지 (16:7) | 지시문 있음 (part3/COVER_3-4) | 천장의 긴 막대 조명, 자글자글한 쪽과 매끄러운 쪽으로 나뉜 진열대, 네모 체와 신경망 그물, 카메라 |
| cover_ch2 | L | 2부 목차 표지 | 지시문 있음 (part2/COVER_ch2) | 바늘구멍 상자, 사진 액자 고리, 떠오르는 3D 머그컵 |
| cover_2-1 | L | 2-1 표지 (16:7) | 지시문 있음 (part2/COVER_2-1) | 사람 키만 한 바늘구멍 상자, 거꾸로 비친 컵, 공과 동전, 손전등 |

## 3. 미리 준비하면 좋은 그림 (2·3부 실험용)
| 키 | 판 | 내용 | 쓰는 편 | 우선 |
|---|---|---|---|---|
| asst_turn_front · asst_turn_34 · asst_turn_side · asst_turn_back | B판 확장 (전신 아님, 머리~어깨, 투명 배경, 512×512) | 조수 턴어라운드: 정면, 45°, 옆(오른쪽 보기), 뒤. 같은 크기·같은 머리 높이 | 1-5(정면/옆 실패 사례), 3-5(최종 미션) | P1 |
| mug_front · mug_side · mug_top | G판 소품 (투명 배경, 512×512) | 같은 머그컵: 앞(손잡이가 뒤로 가려짐), 옆(손잡이 보임), 위(안쪽 구멍) | 2-1, 2-5 | P1 |

**조수 턴어라운드 프롬프트 (Genspark 등, 참고 이미지: asst_e13)**
```
Character turnaround sheet of the same girl researcher as the reference image: pink hair in two round buns with a navy streak, blue eyes, white lab coat over lavender hoodie. Four separate views at the same scale and the same head height, head and shoulders only: front view, three-quarter view facing right, side profile facing right, back view (showing both buns and the navy streak from behind). Neutral expression, mouth closed. Transparent background, each view on its own 512x512 square, evenly lit, no shadows on the background. Match the art style, line weight and colors of the reference exactly. No text, no letters, no numbers, no logos.
```

**머그컵 프롬프트**
```
Simple ceramic mug in the same pixel-art style as the reference images, white mug with a single magenta stripe, one handle on the right side. Three separate views at the same scale: front view with the handle hidden directly behind the mug, side view with the handle fully visible, top-down view showing the hollow inside. Transparent background, each view on its own 512x512 square. No text, no letters, no numbers, no logos.
```

## 4. 대결 균형 기록
| 편 | 결과 | 비고 |
|---|---|---|
| 1-1 | F (초파리 승) | 묶고 이름표 3개 97.2% vs 이름표 4개 81.0% |
| 1-2 | D (무승부) | 족보 4묶음 95.8% vs k-평균 10번 시작 95.8% (2026-11-05 주판봇 v2 그림으로 다시 계산) |
| 1-3 | F (초파리 승) | 지도 위 이웃 맞히기: 주성분 2개 87.1% vs 가장 많이 변하는 픽셀 2개 57.5% |
| 1-4 | R (주판봇 승) | 처음 보는 표정 40장의 가린 곳 오차(×1000): 베끼기 30.8 vs 가리고 배운 상자 28.7 (주판봇 v2 그림, 2026-11-05) |
| 1-5 | F (초파리 승) | 아무 각도 사진 120장: 색 비율 + 이름표 4장 88.3% vs 픽셀 + 정면 이름표 40장 61.7% |
| 2-1 | F (초파리 승) | 사진 한 장으로 손잡이 맞히기: 보이는 것만 77.5% vs 늘 있다 50.0% |
| 2-2 | R (주판봇 승) | 몽타주 81장으로 숫자 넷 찾기: 격자 17.7% vs 무작위 11.2% (어긋남, 낮을수록 좋음) |
| 2-3 | R (주판봇 승) | 같은 계산 시간으로 숫자 넷 찾기: 다듬기 60장 3.3% vs 미끄럼 40걸음 2.2% (어긋남, 낮을수록 좋음, 작은 차이 → fly coffee) |
| 2-4 | D (무승부) | 머그컵 깎기: 둘레 8장 25.4% vs 높이까지 바꾼 64장 26.5% (겹친 비율, 높을수록 좋음, 무승부 폭 2) |
| 2-5 | F (초파리 승) | 봉인된 새 각도의 깊이 맞음: 실루엣 8장 + 깊이 4장 85.4% vs 실루엣 64장 43.0% (높을수록 좋음, 큰 차이 → fly arms / robo sigh) |
| 3-1 | R (주판봇 승) | ×2 업스케일 PSNR: 쌍선형 22.54 dB vs 배운 업스케일러 23.65 dB |
| 3-2 | F (초파리 승) | 떨어지는 블록 누적 PSNR: 잘라내기 24.89 dB vs 기억 다 쓰기 22.01 dB |
| 3-3 | D (무승부) | 두 판: 블록 판 모션 벡터 23.62 > 광학 흐름 21.80, 불꽃 판 광학 흐름 22.43 > 모션 벡터 18.09 → 1:1 |
| 3-4 | R (주판봇 승) | 여덟 경우 평균 빛 PSNR: 손 필터(길잡이 반경 3) 30.78 dB vs 배운 필터 32.03 dB |
| 3-5 | X (주판봇 실격) | 봉인된 시험 사진 120장: 초파리 96.7% vs 주판봇 100% (시험 사진을 학습에 넣음, 데이터 누수) |

목표: 15편 합계 초파리 6 · 주판봇 6 · 무승부 2 · 실격 1 (3-5).


## 1부 공통 소품 규칙 (2026-11-01 변경)
- 레고 대신 **테트리스 블록**. 같은 모양은 같은 색: 막대(I) 하늘 #3fcfe0 · 네모(O) 노랑 #f1c84a · T자 보라 #b46ae6 · L자 주황 #f0903a. 색은 사람만 보는 정답표, AI는 흑백 카메라로 모양만 잰다는 설정.
- 서랍 대신 **천 주머니**(위를 끈으로 묶는 주머니).
- 1-1은 한 회사 세트(칸 약 12mm)·세 종류, 1-2부터 다른 회사 세트(칸 9~15mm)와 L자가 섞인다.

- 대결 균형 (15편 목표 F6 R6 D2 X1): 최종 F6 · R5 · D3 · X1 — 주판봇 v2 그림으로 1-2가 R에서 D로 바뀜 (1-1 F, 1-2 D, 1-3 F, 1-4 R, 1-5 F, 2-1 F, 2-2 R, 2-3 R, 2-4 D, 2-5 F, 3-1 R, 3-2 F, 3-3 D, 3-4 R, 3-5 X)

## 출처 공통 규칙 (2026-11-01)
- 모든 HTML에서 나무위키는 출처로 쓰지 않는다. 위키 문서가 필요하면 위키백과(영어판 우선)를 쓴다. 3-1·3-2·3-3의 나무위키 출처를 영어 위키백과 「Deep Learning Super Sampling」으로 바꿨다.
