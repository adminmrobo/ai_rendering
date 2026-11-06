# 코드 1 · 사진 한 장만 보고 장면을 되찾기 — 미분 가능한 렌더링(역렌더링)
import numpy as np
np.random.seed(0)
N = 32
ys, xs = np.mgrid[0:N, 0:N] / (N - 1)          # 화면 픽셀 좌표 0~1

def render(p, soft=True, tau=0.03):
    """장면 변수 p = [cx, cy, r, 밝기] → 32x32 이미지"""
    cx, cy, r, c = p
    d = np.sqrt((xs - cx)**2 + (ys - cy)**2)
    if soft:   # 경계를 부드럽게: 연속 함수 → 미분 가능
        cover = 1 / (1 + np.exp(-np.clip((r - d) / tau, -50, 50)))
    else:      # 안이면 1, 밖이면 0: 불연속 함수 → 미분 0
        cover = (d < r).astype(float)
    return c * cover

def loss(p, target, soft):
    return np.mean((render(p, soft) - target) ** 2)

def grad(p, target, soft, h=1e-4):          # 수치 미분
    g = np.zeros(4)
    for i in range(4):
        e = np.zeros(4); e[i] = h
        g[i] = (loss(p + e, target, soft) - loss(p - e, target, soft)) / (2 * h)
    return g

true_p  = np.array([0.62, 0.40, 0.22, 0.90])   # 정답 장면 (모델은 모른다)
target  = render(true_p, soft=True)             # 우리가 가진 것은 이 사진 한 장뿐
start_p = np.array([0.35, 0.60, 0.12, 0.40])   # 아무렇게나 시작

for soft in (True, False):
    p = start_p.copy(); lr = 0.02; m = np.zeros(4); v = np.zeros(4)
    print(f"\n[{'부드러운 경계(연속)' if soft else '딱딱한 경계(불연속)'}]")
    for step in range(301):
        if step in (0, 10, 50, 100, 300):
            print(f"걸음 {step:3d} | 손실 {loss(p, target, soft):.5f} | "
                  f"cx {p[0]:.3f} cy {p[1]:.3f} r {p[2]:.3f} 밝기 {p[3]:.3f}")
        g = grad(p, target, soft)            # Adam: 걸음 크기를 알아서 조절
        m = 0.9*m + 0.1*g; v = 0.999*v + 0.001*g*g
        p -= lr * (m/(1-0.9**(step+1))) / (np.sqrt(v/(1-0.999**(step+1))) + 1e-8)
print("\n정답       | cx 0.620 cy 0.400 r 0.220 밝기 0.900")
