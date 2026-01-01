import numpy as np
import matplotlib.pyplot as plt

def lorenz_system(rho_val, num_steps=3000):
    # 標準參數
    sigma = 10
    beta = 8/3
    dt = 0.01
    
    xs, ys, zs = np.empty(num_steps), np.empty(num_steps), np.empty(num_steps)
    
    # 初始起點 (微小的擾動)
    xs[0], ys[0], zs[0] = (0.1, 1.0, 1.05)
    
    for i in range(num_steps - 1):
        x, y, z = xs[i], ys[i], zs[i]
        
        # 羅倫茲方程組 (核心演算法)
        dx = sigma * (y - x)
        dy = x * (rho_val - z) - y  # <--- rho 在這裡發揮作用
        dz = x * y - beta * z
        
        # 更新位置
        xs[i+1] = x + dx * dt
        ys[i+1] = y + dy * dt
        zs[i+1] = z + dz * dt
        
    return xs, ys, zs

# 設定三種不同的 Rho 值來觀察
rhos = [14, 28, 99]
titles = ["Stability (Rho=14)", "Chaos (Rho=28, Classic)", "High Complexity (Rho=99)"]
colors = ['green', 'blue', 'red']

fig = plt.figure(figsize=(15, 5))

for i in range(3):
    ax = fig.add_subplot(1, 3, i+1, projection='3d')
    x, y, z = lorenz_system(rhos[i])
    
    ax.plot(x, y, z, lw=0.6, c=colors[i])
    ax.set_title(titles[i])
    
    # 標記最後停在哪裡 (如果是穩定的，就會看到終點)
    ax.scatter(x[-1], y[-1], z[-1], c='black', s=20, label='End')
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")

plt.tight_layout()
plt.show()
