import cmath

def root2(a, b, c):
    # 計算判別式
    D = b*b - 4*a*c
    
    # 兩個根（使用 cmath.sqrt，可處理複數）
    r1 = (-b + cmath.sqrt(D)) / (2*a)
    r2 = (-b - cmath.sqrt(D)) / (2*a)
    
    return r1, r2

def verify_roots(a, b, c, r1, r2):
    # 驗證 f(root) 是否接近 0
    f = lambda x: a*x*x + b*x + c
    return cmath.isclose(f(r1), 0, rel_tol=1e-9) and \
           cmath.isclose(f(r2), 0, rel_tol=1e-9)


# === 範例使用 ===
if __name__ == "__main__":
    a, b, c = 1, 2, 5   # 判別式為負 → 有複數根
    r1, r2 = root2(a, b, c)

    print("r1 =", r1)
    print("r2 =", r2)
    print("驗證結果：", verify_roots(a, b, c, r1, r2))
  #有用chatgpt
