import numpy as np
from collections import Counter

def solve_ode_general(coefficients):
    # 1. 使用 numpy 求根
    roots = np.roots(coefficients)
    
    # 2. 數據清洗：解決浮點數誤差
    # 將實部和虛部四捨五入到小數點後 5 位，這樣 1.999999 就會變成 2.0
    # 這樣 Counter 才能正確識別出它們是「同一個根」
    cleaned_roots = []
    for r in roots:
        real_part = round(r.real, 5)
        imag_part = round(r.imag, 5)
        # 如果虛部極小（視為實數），強制設為 0j
        if abs(imag_part) == 0:
            cleaned_roots.append(real_part + 0j)
        else:
            cleaned_roots.append(real_part + imag_part * 1j)
            
    # 3. 統計每個根出現的次數 (處理重根)
    counts = Counter(cleaned_roots)
    
    # 用來存放結果字串的列表
    terms = []
    c_index = 1  # 常數 C 的編號，從 1 開始
    
    # 為了輸出順序固定，我們先對根進行排序 (實部由小到大，虛部由小到大)
    # key=lambda x: (x.real, x.imag)
    unique_roots = sorted(counts.keys(), key=lambda x: (x.real, abs(x.imag)))

    processed_conjugates = set() # 用來記錄處理過的共軛複數

    for r in unique_roots:
        count = counts[r]
        
        # --- 情況 A: 實根 (虛部為 0) ---
        if r.imag == 0:
            real_val = r.real
            # 針對重根次數進行迴圈 (例如三重根，k=0, 1, 2)
            for k in range(count):
                # 建構 x^k 部分
                x_str = ""
                if k == 1: x_str = "x"
                elif k > 1: x_str = f"x^{k}"
                
                # 建構 e^(rx) 部分
                e_str = format_exp_term(real_val)
                
                # 組合: C_n * x^k * e^(rx)
                term = f"C_{c_index}{x_str}{e_str}"
                terms.append(term)
                c_index += 1
                
        # --- 情況 B: 複數根 (虛部不為 0) ---
        else:
            # 檢查是否已經處理過這對共軛根 (例如處理過 2i，就跳過 -2i)
            if r in processed_conjugates:
                continue
            
            # 標記這對共軛根已處理
            processed_conjugates.add(r)
            processed_conjugates.add(r.conjugate())
            
            alpha = r.real
            beta = abs(r.imag) # 取正值放入 sin/cos
            
            # 針對重根次數進行迴圈
            for k in range(count):
                # 建構 x^k 部分
                x_str = ""
                if k == 1: x_str = "x"
                elif k > 1: x_str = f"x^{k}"
                
                # 建構 e^(alpha x) 部分
                e_str = format_exp_term(alpha)
                
                # 建構三角函數部分 (beta x)
                beta_str = f"{int(beta)}" if beta.is_integer() else f"{beta}"
                if beta_str == "1": beta_str = "" # 簡化 1x 為 x
                
                # 組合 cos 項: C_n * x^k * e^(alpha x) * cos(beta x)
                term_cos = f"C_{c_index}{x_str}{e_str}cos({beta_str}x)"
                terms.append(term_cos)
                c_index += 1
                
                # 組合 sin 項: C_{n+1} * ... * sin(beta x)
                term_sin = f"C_{c_index}{x_str}{e_str}sin({beta_str}x)"
                terms.append(term_sin)
                c_index += 1

    return " + ".join(terms)

# 輔助函數：美化指數項顯示
def format_exp_term(val):
    if val == 0:
        return "" # e^0 = 1，不顯示
    
    # 處理整數顯示 (例如 2.0 -> 2)
    val_str = f"{int(val)}" if val.is_integer() else f"{val}"
    
    if val_str == "1":
        return "e^x"
    elif val_str == "-1":
        return "e^(-x)"
    else:
        return f"e^({val_str}x)"

# --- 以下是你的測試主程式 (保持不變) ---
# 範例測試 (1): 實數單根
print("--- 實數單根範例 ---")
coeffs1 = [1, -3, 2]
print(f"方程係數: {coeffs1}")
print(solve_ode_general(coeffs1))

# 範例測試 (2): 實數重根
print("\n--- 實數重根範例 ---")
coeffs2 = [1, -4, 4]
print(f"方程係數: {coeffs2}")
print(solve_ode_general(coeffs2))

# 範例測試 (3): 複數共軛根
print("\n--- 複數共軛根範例 ---")
coeffs3 = [1, 0, 4]
print(f"方程係數: {coeffs3}")
print(solve_ode_general(coeffs3))

# 範例測試 (4): 複數重根 (二重)
print("\n--- 複數重根範例 ---")
coeffs4 = [1, 0, 2, 0, 1]
print(f"方程係數: {coeffs4}")
print(solve_ode_general(coeffs4))

# 範例測試 (5): 高階重根
print("\n--- 高階重根範例 ---")
coeffs5 = [1, -6, 12, -8]
print(f"方程係數: {coeffs5}")
print(solve_ode_general(coeffs5))
# gemini
