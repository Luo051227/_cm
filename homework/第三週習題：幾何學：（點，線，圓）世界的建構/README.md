# 📐 I. 幾何物件的定義
## 1. 點 (Point)
`定義為只有位置、沒有大小（寬度、長度和高度）`  
* 點是零維的幾何實體
* 通常用大寫英文字母（如 A, B, P）表示  

兩點間距離公式：d = √{(x_2-x_1)^2 + (y_2-y_1)^2}

## 2. 直線 (Line)
直線是一維的、無限延伸的、由無數點組成的集合。  

一般式 (Standard Form)：` Ax + By + C = 0，其中 A 和 B 不全為零。`  

斜截式 (Slope-intercept Form)：`y = mx + b，其中 m 是斜率，b 是 y 軸截距。`  
## 3. 圓 (Circle)
圓是在平面上，到固定點（圓心）距離為定值（半徑）的所有點的集合。

標準式 (Standard Form)：`(x - h)^2 + (y - k)^2 = r^2，其中 (h, k) 是圓心，r 是半徑。`

# 💻 計算幾何：交點與垂直線
## 1. 兩直線交點 (Intersection of Two Lines)
給定兩條直線：`L_1: A_1x + B_1y + C_1 = 0` & `L_2: A_2x + B_2y + C_2 = 0`

這是一個二元一次聯立方程式組。我們可以利用克萊默法則 (Cramer's Rule) 或代入消去法求解 $x$ 和 $y$。
### 數學基礎：
`D = A_1B_2 - A_2B_1` `D_x = C_2B_1 - C_1B_2` `D_y = A_2C_1 - A_1C_2`

如果 D \neq 0，則交點為 (x, y) = (\frac{D_x}{D}, \frac{D_y}{D})。如果 $D = 0$：若 D_x = 0 且 D_y = 0，則兩線重合（無限多交點）。若 D_x \neq 0 或 D_y \neq 0，則兩線平行（無交點）。
## AI
參考：[Gemini](https://gemini.google.com/share/7c487b510690)

