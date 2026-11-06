# 코드 2 · 작은 DLSS 흉내 — 정답 이름표 없이 "고해상도 렌더링 자신"을 정답으로 배운다
import numpy as np
np.seterr(divide="ignore")
rng = np.random.default_rng(0)
H = 64                                            # 고해상도 64x64, 저해상도 32x32

def scene(k=6):
    """무작위 원과 줄무늬가 섞인 장면을 고해상도로 '렌더링'한다"""
    ys, xs = np.mgrid[0:H, 0:H] / H
    img = np.zeros((H, H))
    for _ in range(k):
        cx, cy, r = rng.random(), rng.random(), 0.05 + 0.2 * rng.random()
        img += rng.random() / (1 + np.exp(-(r - np.hypot(xs - cx, ys - cy)) / 0.01))
    img += 0.3 * np.sin(2 * np.pi * (rng.integers(3, 9)) * (xs * rng.random() + ys))
    return (img - img.min()) / (np.ptp(img) + 1e-9)

def low(img, dx=0, dy=0):                         # 픽셀 4개 중 하나만 찍기(지터 dx,dy)
    return img[dy::2, dx::2]

def psnr(a, b):
    return 10 * np.log10(1 / np.mean((a - b) ** 2))

def patches(lo):                                  # 저해상도 픽셀마다 주변 3x3 조각
    p = np.pad(lo, 1, mode="edge")
    return np.stack([p[i:i+lo.shape[0], j:j+lo.shape[1]].ravel()
                     for i in range(3) for j in range(3)], 1)

def blocks(hi):                                   # 고해상도 2x2 블록 = 맞혀야 할 정답
    return np.stack([hi[i::2, j::2].ravel() for i in range(2) for j in range(2)], 1)

def assemble(b):
    out = np.zeros((H, H)); n = H // 2
    for k, (i, j) in enumerate([(0,0),(0,1),(1,0),(1,1)]):
        out[i::2, j::2] = b[:, k].reshape(n, n)
    return out

# ① 학습: 고해상도 렌더링 200장을 스스로 줄이고, 다시 키우는 법을 배운다 (사람 라벨 0개)
train = [scene() for _ in range(200)]
X = np.vstack([np.c_[patches(low(s)), np.ones(32*32)] for s in train])
Y = np.vstack([blocks(s) for s in train])
W = np.linalg.lstsq(X, Y, rcond=None)[0]          # 9칸+1 → 4칸 '업스케일 필터'

# ② 시험: 처음 보는 장면 50장
test = [scene() for _ in range(50)]
res = {"가장 가까운 픽셀 복사": [], "배운 업스케일러(1장)": [],
       "지터 4장 합치기 · 멈춘 화면": [], "지터 4장 · 움직임, 모션 벡터 없음": [],
       "지터 4장 · 움직임, 모션 벡터 사용": []}
for s in test:
    lo = low(s)
    res["가장 가까운 픽셀 복사"].append(psnr(np.kron(lo, np.ones((2, 2))), s))
    res["배운 업스케일러(1장)"].append(psnr(assemble(np.c_[patches(lo), np.ones(32*32)] @ W), s))
    acc = np.zeros((H, H))                        # 프레임마다 카메라를 반 픽셀씩 흔든다
    for dy in (0, 1):
        for dx in (0, 1):
            acc[dy::2, dx::2] = low(s, dx, dy)
    res["지터 4장 합치기 · 멈춘 화면"].append(min(psnr(acc, s), 60.0))
    # 화면이 프레임마다 오른쪽으로 2픽셀씩 움직이면? (마지막 프레임 t=3이 '지금')
    now = np.roll(s, 6, axis=1)
    bad = np.zeros((H, H)); good = np.zeros((H, H))
    for t, (dy, dx) in enumerate([(0,0),(0,1),(1,0),(1,1)]):
        frame = np.roll(s, 2 * t, axis=1)          # t번째 프레임의 고해상도 장면
        bad[dy::2, dx::2] = low(frame, dx, dy)      # 그냥 겹치면 잔상(고스팅)
        moved = np.zeros((H, H)); moved[dy::2, dx::2] = 1
        tmp = np.zeros((H, H)); tmp[dy::2, dx::2] = low(frame, dx, dy)
        sh = 2 * (3 - t)                            # 모션 벡터: '지금'까지 더 갈 거리
        good = np.where(np.roll(moved, sh, axis=1) > 0, np.roll(tmp, sh, axis=1), good)
    res["지터 4장 · 움직임, 모션 벡터 없음"].append(psnr(bad, now))
    res["지터 4장 · 움직임, 모션 벡터 사용"].append(min(psnr(good, now), 60.0))

print("시험 장면 50장 평균 PSNR (높을수록 원본과 같음, dB)")
for k, v in res.items():
    print(f"  {k:26s} {np.mean(v):6.2f}")
