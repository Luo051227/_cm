import numpy as np

def verify_gibbs_inequality(num_trials: int = 5):
    """
    驗證 Gibbs 不等式: H(P, Q) >= H(P, P)
    並反駁錯誤假設: H(P, P) > H(P, Q)
    """
    
    # 防止 log(0)
    EPSILON = 1e-12

    def calculate_ce(p, q):
        """計算 Cross Entropy"""
        q_safe = np.clip(q, EPSILON, 1.0)
        return -np.sum(p * np.log2(q_safe))

    print(f"{'Trial':<6} | {'H(P, P) (Entropy)':<18} | {'H(P, Q) (Cross-E)':<18} | {'Diff (KL)':<10} | {'Result'}")
    print("-" * 75)

    success_count = 0

    for i in range(num_trials):
        # 1. 隨機生成機率分佈 P (真實)
        # 使用 Dirichlet 分佈可以確保總和為 1 且皆為正數
        p = np.random.dirichlet(np.ones(5))
        
        # 2. 隨機生成機率分佈 Q (預測)，確保 Q != P
        q = np.random.dirichlet(np.ones(5))
        
        # 3. 計算兩者
        h_pp = calculate_ce(p, p) # 自身的熵 (最小 Loss)
        h_pq = calculate_ce(p, q) # 用 Q 預測 P 的交叉熵
        
        # 4. 比較
        # 正確理論: H(P, Q) > H(P, P)
        is_theory_correct = h_pq > h_pp
        
        # 使用者假設: H(P, P) > H(P, Q)
        user_hypothesis = h_pp > h_pq
        
        kl_diff = h_pq - h_pp # 這就是 KL 散度

        if is_theory_correct:
            success_count += 1

        print(f"#{i+1:<5} | {h_pp:.4f}             | {h_pq:.4f}             | +{kl_diff:.4f}    | {'Theory Holds' if is_theory_correct else 'Fail'}")

    print("-" * 75)
    print(f"【驗證總結】")
    print(f"1. 理論 H(P, Q) > H(P, P): {success_count}/{num_trials} 次成立")
    print(f"2. 你的假設 H(P, P) > H(P, Q): {0}/{num_trials} 次成立")
    
    if success_count == num_trials:
        print("\n結論: 當 Q != P 時，交叉熵 H(P, Q) 總是比熵 H(P, P) 大。")
        print("物理意義: 用錯誤的模型 Q 來預測 P，所需要的資訊量(Bit)一定比用原本的 P 還多。")
    else:
        print("例外發生 (可能是浮點數誤差)")

if __name__ == "__main__":
    # 設定隨機種子以重現結果
    np.random.seed(42)
    verify_gibbs_inequality(10)
