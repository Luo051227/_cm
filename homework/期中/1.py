import numpy as np
import matplotlib.pyplot as plt

# 1. 定義羅倫茲方程 (這就是天氣運作的簡化規則)
def lorenz_step(x, y, z, s=10, r=28, b=2.667, dt=0.01):
    x_dot = s * (y - x)
    y_dot = r * x - y - x * z
    z_dot = x * y - b * z
    # 更新位置 (歐拉法)
    return x + x_dot * dt, y + y_dot * dt, z + z_dot * dt

# 2. 設定參數
dt = 0.01
num_steps = 3000

# 3. 初始化兩條軌跡 (起點只差一點點！)
# 軌跡 A
xs, ys, zs = np.empty(num_steps), np.empty(num_steps), np.empty(num_steps)
xs[0], ys[0], zs[0] = (0., 1., 1.05)

# 軌跡 B (只差 0.01)
xs2, ys2, zs2 = np.empty(num_steps), np.empty(num_steps), np.empty(num_steps)
xs2[0], ys2[0], zs2[0] = (0., 1., 1.05 + 0.01) # <--- 這裡就是蝴蝶效應的源頭

# 4. 開始運算
for i in range(num_steps - 1):
    xs[i+1], ys[i+1], zs[i+1] = lorenz_step(xs[i], ys[i], zs[i])
    xs2[i+1], ys2[i+1], zs2[i+1] = lorenz_step(xs2[i], ys2[i], zs2[i])

# 5. 畫圖
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(projection='3d')

# 畫第一條線 (藍色)
ax.plot(xs, ys, zs, lw=0.8, c='blue', alpha=0.7, label='Butterfly 1')

# 畫第二條線 (黃色 dashed)
# 注意看：前幾步它們是重疊的，後面突然分開
ax.plot(xs2, ys2, zs2, lw=0.8, c='orange', linestyle='--', alpha=0.8, label='Butterfly 2 (Start +0.01)')

ax.set_title("Lorenz Attractor: The Butterfly Effect")
ax.legend()
plt.show()
