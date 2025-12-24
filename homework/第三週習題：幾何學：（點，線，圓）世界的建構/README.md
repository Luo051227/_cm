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


## 數學基礎：
`D = A_1B_2 - A_2B_1` `D_x = C_2B_1 - C_1B_2` `D_y = A_2C_1 - A_1C_2`

如果 D \neq 0，則交點為 (x, y) = (\frac{D_x}{D}, \frac{D_y}{D})。如果 $D = 0$：若 D_x = 0 且 D_y = 0，則兩線重合（無限多交點）。若 D_x \neq 0 或 D_y \neq 0，則兩線平行（無交點）。
## AI
參考：[Gemini](https://gemini.google.com/share/7c487b510690)

