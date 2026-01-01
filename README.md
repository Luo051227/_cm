# 課程：程式與數學

欄位 | 內容
-----|--------
學期 | 114 學年上學期
學生 |  羅詩喬
學號末兩碼 | 01
教師 | [陳鍾誠](https://www.nqu.edu.tw/educsie/index.php?act=blog&code=list&ids=4)
學校科系 | [金門大學資訊工程系](https://www.nqu.edu.tw/educsie/index.php)
課程教材 | https://github.com/ccc114a/py2cs 
# 習題 1 : 請用程式驗證微積分基本定理
[作業](https://github.com/Luo051227/_cm/tree/main/homework/%E7%BF%92%E9%A1%8C1)

# 習題 2 : 請寫程式求解二次多項式的根
[作業](https://github.com/Luo051227/_cm/tree/main/homework/%E7%BF%92%E9%A1%8C2)

# 習題 3 : 請寫程式求解三次多項式的根 (加分題）
[作業](https://github.com/Luo051227/_cm/tree/main/homework/%E7%BF%92%E9%A1%8C3)

# 習題 4 : （思考）請寫一個函數 root(c) 求出 n 次多項式的根 （ n>=5 的時候，數學上證明沒有公式 -- 伽羅瓦定理）
[作業](https://github.com/Luo051227/_cm/tree/main/homework/%E7%BF%92%E9%A1%8C4)

# 第二週習題：有限體 
[作業](https://github.com/Luo051227/_cm/tree/main/homework/%E7%AC%AC%E4%BA%8C%E9%80%B1%E7%BF%92%E9%A1%8C%EF%BC%9A%E6%9C%89%E9%99%90%E9%AB%94)
[AI](https://chatgpt.com/share/6924476a-fd44-8012-a7be-87cdaada71f6)
# 第三週習題：幾何學：（點，線，圓）世界的建構
# 點 (Point)
`定義為只有位置、沒有大小（寬度、長度和高度）`  
* 點是零維的幾何實體
* 通常用大寫英文字母（如 A, B, P）表示  

兩點間距離公式：d = √{(x_2-x_1)^2 + (y_2-y_1)^2}

# 直線 (Line)
直線是一維的、無限延伸的、由無數點組成的集合。  

一般式 (Standard Form)：` Ax + By + C = 0，其中 A 和 B 不全為零。`  

斜截式 (Slope-intercept Form)：`y = mx + b，其中 m 是斜率，b 是 y 軸截距。`  
# 圓 (Circle)
圓是在平面上，到固定點（圓心）距離為定值（半徑）的所有點的集合。  
圓標準式 (Standard Form)：<img width="300" height="75" alt="image" src="https://github.com/user-attachments/assets/9f132c8b-9053-499b-8fcd-e273087eb16a" />`，其中 (h, k) 是圓心，r 是半徑。`  
<img width="200" height="113" alt="image" src="https://github.com/user-attachments/assets/f39e5012-3e18-473e-8021-e4f8d57d07d5" />  
<img width="600" height="397" alt="image" src="https://github.com/user-attachments/assets/02c6aba2-5767-4d93-b962-804a0b109c39" />

切線 (Tangent Line)
* 條件： d = r
* 特性： 直線與圓恰好只有一個交點
* 切點的半徑相互垂直
割線 (Secant Line)
* 條件： d < r
* 特性： 直線與圓有兩個交點。
* 割線在圓內部：弦
* 割線通過圓心：直徑
## 判斷直線與圓的交點
<img width="615" height="246" alt="image" src="https://github.com/user-attachments/assets/6ccedef2-b4b6-40d0-b59d-c63bcc8e7579" />



# 兩直線交點 (Intersection of Two Lines)
兩條直線可以用一般式表示：<img width="323" height="23" alt="image" src="https://github.com/user-attachments/assets/1b08e439-6fcd-4b42-840b-d6af650cd44b" />
```python
def intersect_lines(a1, b1, c1, a2, b2, c2):
    # 計算行列式 Determinant
    det = a1 * b2 - a2 * b1
    if det == 0:
        return None  # 平行或重合，無單一交點
    
    x = (c1 * b2 - c2 * b1) / det
    y = (a1 * c2 - a2 * c1) / det
    return (x, y)

# 範例：x + y = 2 且 x - y = 0
print(f"直線交點: {intersect_lines(1, 1, 2, 1, -1, 0)}") # 預期 (1.0, 1.0)
```

# 克拉瑪公式
<img width="156" height="92" alt="image" src="https://github.com/user-attachments/assets/d5a067f1-98fd-4f77-9770-1db49ec11f49" />
<img width="452" height="47" alt="image" src="https://github.com/user-attachments/assets/63ee211b-b92b-413d-8b7e-fcbcdd7f6291" />
<img width="477" height="502" alt="image" src="https://github.com/user-attachments/assets/00aecca4-6407-4ed4-bde3-42ee336e193e" />
<img width="504" height="108" alt="image" src="https://github.com/user-attachments/assets/12fefba4-4c13-4712-8a29-98af579ed65a" />



## 數學基礎：
`D = A_1B_2 - A_2B_1` `D_x = C_2B_1 - C_1B_2` `D_y = A_2C_1 - A_1C_2`

如果 D \neq 0，則交點為 (x, y) = (\frac{D_x}{D}, \frac{D_y}{D})。如果 $D = 0$：若 D_x = 0 且 D_y = 0，則兩線重合（無限多交點）。若 D_x \neq 0 或 D_y \neq 0，則兩線平行（無交點）。  
[作業](https://github.com/Luo051227/_cm/tree/main/homework/%E7%AC%AC%E4%B8%89%E9%80%B1%E7%BF%92%E9%A1%8C%EF%BC%9A%E5%B9%BE%E4%BD%95%E5%AD%B8%EF%BC%9A%EF%BC%88%E9%BB%9E%EF%BC%8C%E7%B7%9A%EF%BC%8C%E5%9C%93%EF%BC%89%E4%B8%96%E7%95%8C%E7%9A%84%E5%BB%BA%E6%A7%8B)
[AI](https://gemini.google.com/share/ca1dd991cd0f)
# 第八週習題：機率統計 - 檢定背後的數學原理
[作業](https://github.com/Luo051227/_cm/tree/main/homework/%E7%AC%AC%E5%85%AB%E9%80%B1%E7%BF%92%E9%A1%8C%EF%BC%9A%E6%A9%9F%E7%8E%87%E7%B5%B1%E8%A8%88%20-%20%E6%AA%A2%E5%AE%9A%E8%83%8C%E5%BE%8C%E7%9A%84%E6%95%B8%E5%AD%B8%E5%8E%9F%E7%90%86)
[AI]()
# 第九周習題：資訊理論
[作業](https://github.com/Luo051227/_cm/tree/main/homework/%E7%AC%AC%E4%B9%9D%E5%91%A8%E7%BF%92%E9%A1%8C%EF%BC%9A%E8%B3%87%E8%A8%8A%E7%90%86%E8%AB%96)
[AI]()
# 第十周習題：線性代數
[作業](https://github.com/Luo051227/_cm/tree/main/homework/%E7%AC%AC%E5%8D%81%E5%91%A8%E7%BF%92%E9%A1%8C%EF%BC%9A%E7%B7%9A%E6%80%A7%E4%BB%A3%E6%95%B8)
[AI]()
# 第11周習題：請寫出傅立葉正轉換和逆轉換的函數（不要用套件）
[作業](https://github.com/Luo051227/_cm/tree/main/homework/%E7%AC%AC11%E5%91%A8%E7%BF%92%E9%A1%8C%EF%BC%9A%E8%AB%8B%E5%AF%AB%E5%87%BA%E5%82%85%E7%AB%8B%E8%91%89%E6%AD%A3%E8%BD%89%E6%8F%9B%E5%92%8C%E9%80%86%E8%BD%89%E6%8F%9B%E7%9A%84%E5%87%BD%E6%95%B8%EF%BC%88%E4%B8%8D%E8%A6%81%E7%94%A8%E5%A5%97%E4%BB%B6%EF%BC%89)
[AI]()
# 第13周習題：請寫程式求解常係數齊次常微分方程
[作業](https://github.com/Luo051227/_cm/tree/main/homework/%E7%AC%AC13%E5%91%A8%E7%BF%92%E9%A1%8C%EF%BC%9A%E8%AB%8B%E5%AF%AB%E7%A8%8B%E5%BC%8F%E6%B1%82%E8%A7%A3%E5%B8%B8%E4%BF%82%E6%95%B8%E9%BD%8A%E6%AC%A1%E5%B8%B8%E5%BE%AE%E5%88%86%E6%96%B9%E7%A8%8B)
[AI]()
# 期中
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
## 混沌的誕生
```python
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
```
* $\rho = 14$： 熱度不夠，對流會慢慢穩定下來（螺旋收斂到一個點）  
  `會看到線條繞了幾圈後，最後吸入並停在某個黑點上。這代表天氣很穩定，不管怎樣最後都會變成那個樣子`
* $\rho = 28$： 經典的羅倫茲蝴蝶（永遠繞圈圈）  
  `線條永遠不會停下來，形成完美的蝴蝶。這就是我們真實世界的「天氣」`
* $\rho = 99$： 超級加熱，蝴蝶變成了一團亂麻（更複雜的混沌）  
  `雖然還是在繞圈，但範圍變得更大、切換頻率更快，像是躁動的蝴蝶`  
**只要改變一個參數，整個系統的行為模式，可能會從「穩定」瞬間變成「混沌」**  
[作業](https://github.com/Luo051227/_cm/tree/main/homework/%E6%9C%9F%E4%B8%AD)
[AI](https://gemini.google.com/share/277a8dea3197)
