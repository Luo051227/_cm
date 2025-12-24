# 兩直線的交點
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


# 一直線與一圓的交點
import math

def intersect_line_circle(h, k, r, m, b):
    # 代入後展開整理：Ax^2 + Bx + C = 0
    # A = 1 + m^2
    # B = -2h + 2m(b - k)
    # C = h^2 + (b - k)^2 - r^2
    A = 1 + m**2
    B = -2*h + 2*m*(b - k)
    C = h**2 + (b - k)**2 - r**2
    
    delta = B**2 - 4*A*C
    if delta < 0:
        return [] # 無交點
    
    points = []
    for sign in [1, -1]:
        x = (-B + sign * math.sqrt(delta)) / (2 * A)
        y = m * x + b
        points.append((x, y))
    
    return list(set(points)) # 使用 set 移除切線時重複的點

# 範例：圓心(0,0), 半徑5, 直線 y = 3 (水平線)
print(f"線圓交點: {intersect_line_circle(0, 0, 5, 0, 3)}")


# 兩個圓的交點
def intersect_circles(x1, y1, r1, x2, y2, r2):
    dx, dy = x2 - x1, y2 - y1
    d = math.sqrt(dx**2 + dy**2)
    
    # 無交點的情況
    if d > r1 + r2 or d < abs(r1 - r2) or d == 0:
        return []

    # 計算 a (圓 1 到交點連線中點的距離)
    a = (r1**2 - r2**2 + d**2) / (2 * d)
    h = math.sqrt(max(0, r1**2 - a**2))
    
    # 找到圓心連線上的中點 P2
    x2_mid = x1 + a * dx / d
    y2_mid = y1 + a * dy / d
    
    # 計算交點偏移量
    rx = -dy * (h / d)
    ry = dx * (h / d)
    
    p1 = (x2_mid + rx, y2_mid + ry)
    p2 = (x2_mid - rx, y2_mid - ry)
    
    return list(set([p1, p2]))

# 範例：圓1(0,0, r=5), 圓2(8,0, r=5)
print(f"兩圓交點: {intersect_circles(0, 0, 5, 8, 0, 5)}")
