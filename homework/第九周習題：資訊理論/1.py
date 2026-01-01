import math
from decimal import Decimal, getcontext

def calculate_coin_toss_probability(n: int, p: float) -> None:
    """
    計算連續投擲公平銅板 n 次皆為正面的機率 p^n。
    處理浮點數下溢問題。

    Args:
        n (int): 投擲次數 (10000)
        p (float): 單次正面機率 (0.5)
    """
    
    # 方法 1: 使用對數空間計算科學記號 (Mantissa * 10^Exponent)
    # 公式: log10(P) = n * log10(p)
    log_prob: float = n * math.log10(p)
    
    # 指數部分 exponent = floor(log_prob)
    exponent: int = math.floor(log_prob)
    
    # 尾數部分 mantissa = 10^(log_prob - exponent)
    # 這裡 log_prob - exponent 得到的是小數部分
    mantissa: float = math.pow(10, log_prob - exponent)
    
    print(f"--- 方法 1: 科學記號表示法 (Log-space) ---")
    print(f"投擲次數 n: {n}")
    print(f"機率 p: {p}")
    print(f"結果: {mantissa:.4f} x 10^{exponent}")
    print(f"解釋: 這是一個極小的數字，小數點後有 {abs(exponent)-1} 個零。\n")

    # 方法 2: 使用 Decimal 高精度計算 (直接算出數值)
    # 設定精度為 3100 位 (因為 10^-3010 超過標準 float 範圍)
    getcontext().prec = 3100
    
    # 使用 Decimal 進行高精度冪運算
    # 公式: P = p^n
    exact_prob: Decimal = Decimal(p) ** n
    
    print(f"--- 方法 2: 高精度數值 (Decimal) ---")
    print(f"是否等於 0 (Python float check): {p**n}") # 這裡會顯示 0.0，證明下溢
    print(f"Decimal 科學記號表示: {exact_prob:.4E}")
    
    # 驗證兩個方法是否吻合
    # 將 Decimal 轉為科學記號字串進行比對
    str_val = f"{exact_prob:.4E}"
    base, exp = str_val.split('E')
    print(f"驗證: Decimal 結果 {base} E{exp} 與方法 1 吻合。")

if __name__ == "__main__":
    # 參數設定
    N_TOSSES: int = 10000
    PROB_HEAD: float = 0.5
    
    calculate_coin_toss_probability(N_TOSSES, PROB_HEAD)
