# 羅倫茲吸引子 (Lorenz Attractor)
## 由來
1963 年，氣象學家 愛德華·羅倫茲 (Edward Lorenz) 用電腦模擬天氣。方程式很簡單，他有一天想把運算結果重跑一遍。

為了省時間，他沒有輸入完整的數據 `0.506127`，而是四捨五入輸入了 `0.506`。他以為這 `0.000127` 的微小差距應該沒影響。

結果去喝杯咖啡回來，發現兩次模擬出來的天氣完全不同！ 一個是大晴天，一個是暴風雨。
## 圖形
`羅倫茲將這三個變數（代表氣溫、氣壓、氣流等）畫在 3D 空間中`
* 不會重複： 這條線繞了幾萬圈，永遠不會跟之前的路徑重疊
* 有範圍但無規律： 它永遠不會跑出這個「蝴蝶翅膀」的範圍（所以叫「吸引子」，把軌跡吸住），但你永遠不知道它下一秒會飛到左邊翅膀還是右邊翅膀
* 混沌 (Chaos)： 它不是亂數，它有公式，但結果卻無法預測
## 蝴蝶效應python
* 藍色點： 從 `(0, 1, 1.05)` 出發
* 黃色點： 從 `(0, 1, 1.05 + 0.01)` 出發
```python
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
```
## 數學原理
$$\begin{cases}
\frac{dx}{dt} = \sigma (y - x) \\
\frac{dy}{dt} = x (\rho - z) - y \\
\frac{dz}{dt} = xy - \beta z
\end{cases}$$
* $x$ (流速)： 對流翻滾的速度。正數代表順時針轉，負數代表逆時針轉
* $y$ (溫差)： 上升流和下降流之間的溫度差異
* $z$ (垂直溫度的扭曲)： 雖然熱空氣往上飄，但對流會把這層規律打亂，$z$ 就是用來描述這種「混亂程度」或「偏離線性分佈的程度」
**參數代表**
* $\sigma$ (Sigma, 普朗特數)： 代表流體的黏滯性（黏稠度）。氣體通常較小，油較大
* $\rho$ (Rho, 雷利數)：這是最重要的參數！ 它代表**「加熱的強度」**。
  * 火開很小 ($\rho < 1$)：氣體不動，熱量靠傳導散去
  * 火開大一點 ($\rho > 1$)：開始穩定對流
  * 火開很大 ($\rho = 28$)：`混沌出現`
* $\beta$ (Beta, 幾何因子)： 與容器的寬高比有關

### 假設
**漏水的水車**
* 水開很小：水漏得比裝得快（靜止，收斂到一點）
* 水開大一點：水車會開始穩定地往一個方向轉（週期性運動）
* 水開得很大 (混沌發生)：開始加速轉動，轉太快，水來不及裝滿桶子，另一邊的空桶子轉上來接水變重了，水車會突然減速，然後倒著轉，一直持續發生
