# AI 렌더링 연구실 — 3부작

**보기: https://adminmrobo.github.io/ai_rendering/** (GitHub Pages)

글 · 안상선 ((주)M-Robo 대표) · CC BY-NC 4.0

## 2026-11-05 · 연구실 로봇 교체: Money-Robo → 주판봇 (새 픽셀 그림 반영)

- 이름: 한국어 주판봇 · en·uz·vi AbaBot · ja アバボット · zh 算盘宝 · ru АбаБот. 표정 그림은 캐릭터 팩 1.3(adminmrobo/fruitfly-lab-expressions 5269662)의 새 픽셀 그림.
- 1부 수치 재계산: 1-1~1-4의 얼굴 그림 24장을 새 주판봇 그림으로 바꿔 다시 계산했다(1-4 신경망 재학습 포함). 본문·요약 카드·표·퀴즈를 새 수치로 고쳤다. 1-5의 주판봇 셀카 8장도 새 그림이다.
- 주판봇 표정: 장면마다 대사에 맞춰 24종 중 19종을 골라 쓴다(예전에는 뿌듯한 얼굴 한 장이 53곳). 캐릭터 소개 카드만 기본 얼굴(E13).
- 결과가 바뀐 곳: 1-2 대결이 주판봇 승 → 무승부(족보 95.8% vs k-평균 95.8%)가 되어 설명·대사·퀴즈를 고쳤다. 시리즈 대결 기록은 F6 · R5 · D3 · X1.
- 표지 18장과 첫 화면 그림을 새 주판봇이 나오는 그림 19장으로 모두 바꿨다(프롬프트는 `specs/COVER_ALL_18.md`, 한눈에 보기 `specs/assets/covers/contact_sheet_19.png`).

## 3부작 시리즈 (완성판 · 한국어 + 6개 언어)

**첫 화면: [index.html](index.html)** — 3부작 전체 목차(세 부와 15편으로 바로 가기). 언어판은 `en/index.html`처럼 언어 폴더 안에 있습니다.

3부 × 5편 = 15편과 목차 3쪽, 모두 18쪽입니다. 한국어판에 영어·중국어·일본어·러시아어·우즈베크어·베트남어판이 더해져 모두 126쪽이고, 첫 화면 7쪽이 따로 있습니다. 세 폴더(part1, part2, part3)를 같은 위치에 두면 목차끼리 서로 이어집니다.

| 부 | 편 |
|---|---|
| 1부 정답표 없이 배우기 (`part1/`) | [목차](part1/index.html) · [1-1 세 가지 학습](part1/1-1_learning_without_labels.html) · [1-2 묶기](part1/1-2_grouping_similar.html) · [1-3 지도 위 점](part1/1-3_faces_on_a_map.html) · [1-4 가리고 맞히기](part1/1-4_mask_and_predict.html) · [1-5 이 얼굴은 누구?](part1/1-5_who_is_this.html) |
| 2부 렌더링을 거꾸로 (`part2/`) | [목차](part2/index.html) · [2-1 사진은 왜 납작할까](part2/2-1_why_photos_are_flat.html) · [2-2 몽타주 그리기](part2/2-2_drawing_a_montage.html) · [2-3 계단과 미끄럼틀](part2/2-3_stairs_and_slides.html) · [2-4 여러 각도에서 보기](part2/2-4_many_angles.html) · [2-5 머그컵을 3D로](part2/2-5_mug_in_3d.html) |
| 3부 적게 그리고 AI로 채우기 (`part3/`) | [목차](part3/index.html) · [3-1 작게 그리고 크게](part3/3-1_render_small_upscale.html) · [3-2 시간이 도와준다](part3/3-2_time_helps.html) · [3-3 사이 프레임](part3/3-3_frame_generation.html) · [3-4 AI가 빛을 다시 그린다](part3/3-4_relight_with_ai.html) · [3-5 최종 미션](part3/3-5_any_angle_assistant.html) |

### 외국어판

| 언어 | 폴더 | 첫 화면 |
|---|---|---|
| English | `partN/en/` | [en/index.html](en/index.html) |
| 中文 (简体) | `partN/zh/` | [zh/index.html](zh/index.html) |
| 日本語 | `partN/ja/` | [ja/index.html](ja/index.html) |
| Русский | `partN/ru/` | [ru/index.html](ru/index.html) |
| Oʻzbekcha | `partN/uz/` | [uz/index.html](uz/index.html) |
| Tiếng Việt | `partN/vi/` | [vi/index.html](vi/index.html) |

- 모든 쪽 맨 위에 언어 전환 줄이 있습니다. 한국어판을 처음 열면 브라우저 언어에 맞는 판으로 넘어가고, 한 번 고르면 그 선택을 유지합니다. `?lang=ko`처럼 주소에 붙여 고를 수도 있습니다.
- 다른 부로 가는 링크도 같은 언어판으로 이어집니다.
- 코드 상자(Colab 코드와 결과)는 번역하지 않았습니다.
- 원어민 검수 전입니다(특히 우즈베크어·러시아어·베트남어). 우즈베크어판의 CC 라이선스 링크는 영어 안내문으로 연결됩니다.

### specs/ — 그림 지시문과 기록

- 표지 프롬프트 `COVER_*`: ch1, 1-2, 1-3, 1-4, 1-5, ch2, 2-1, 2-2, 2-3, 2-4, 2-5, ch3, 3-1, 3-2, 3-3, 3-4, 3-5 (16:9)
- 목차 표지 정사각 1280×1280 `COVER_INDEX_square_1280.md` (1·2·3부)
- 표지 프롬프트 18장 한 파일 모음 `COVER_ALL_18.md`
- 저장소 표지(GitHub 소셜 미리보기 1280×640) 프롬프트 `COVER_REPO_social_1280x640.md`
- 표지 그림 18장 `assets/covers/` (원본 PNG와 페이지에 넣은 WebP — 각 편 1600×900, 목차 1000×1000)
- 첫 화면 대표 그림 `assets/landing/` (원본 1920×1080, 페이지에 넣은 판 1280×720)
- 이미지 명세 `IMG_*`, 시리즈 기록 `IMG_00_series`(대결 기록 포함), 개념 목록 `KG_00_registry.json`, 받은 그림 원본 `assets/`

## i18n_tools/ — 번역 도구 (언어팩 VER1.0 흐름)

추출 → 묶기 → 번역 → 검사 → 합치기 → 화면 검사 순서와 명령은 [i18n_tools/README.md](i18n_tools/README.md)에 있습니다. 번역 메모리(`tm/`)가 함께 들어 있어서, 검수 의견이 들어오면 메모리만 고치고 `mergeall.py`를 한 번 다시 돌리면 18쪽 × 6개 언어가 다시 만들어집니다. 비용 기록은 `cost.csv`에 있습니다. 첫 화면은 `make_landing.py <사이트 폴더>`로 각 부 목차의 글을 가져와 다시 만듭니다.

## early_full_version/ — 3부작으로 나누기 전 초기 전체판 (2026-10-31)

- rendering_dlss.md · 01_inverse_rendering.html — 비지도 학습 → 역렌더링 → DLSS를 한 편에
- code1.py · code2.py, 초기 표지·이미지 명세
