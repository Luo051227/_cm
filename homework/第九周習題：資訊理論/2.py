import math

def calculate_log_probability(n: int, p: float) -> float:
    """
    利用對數性質 log10(p^n) = n * log10(p) 計算極小機率的對數值。
    
    Args:
        n (int): 投擲次數 (10000)
        p (float): 單次正面機率 (0.5)
        
    Returns:
        float: log10(p^n) 的值
    """
    
    # 步驟 1: 計算單次事件機率的對數 log10(p)
    # log10(0.5) ≈ -0.30103
    single_log: float = math.log10(p)
    
    # 步驟 2: 利用對數律將指數運算轉換為乘法
    # log10(p^n) = n * log10(p)
    total_log: float = n * single_log
    
    return total_log

if __name__ == "__main__":
    # 設定參數
    n_tosses: int = 10000
    p_head: float = 0.5
    
    # 執行計算
    result: float = calculate_log_probability(n_tosses, p_head)
    
    # 輸出結果
    print(f"計算公式: {n_tosses} * log10({p_head})")
    print(f"計算結果 (log10值): {result:.5f}")
    
    # 結果解讀
    print("-" * 30)
    print("【數值解讀】")
    print(f"這代表原本的機率 P 約等於 10 的 {result:.5f} 次方。")
    print(f"即 P ≈ 10^{result:.5f}")
    print(f"也就是說，小數點後大約有 {abs(int(result))} 個零。")
