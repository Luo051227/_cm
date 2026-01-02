import numpy as np

def svd_via_eig(A: np.ndarray):
    """
    使用特徵值分解 (Eigenvalue Decomposition) 來實作 SVD。
    
    數學原理:
    1. A^T A 的特徵向量 => V (Right Singular Vectors)
    2. sqrt(A^T A 的特徵值) => Sigma (Singular Values)
    3. u_i = (A v_i) / sigma_i => U (Left Singular Vectors)
    """
    
    # 1. 計算 A^T A (Covariance-like matrix)
    ATA = A.T @ A
    
    # 2. 對 A^T A 進行特徵值分解
    # eigenvalues: 特徵值, eigenvectors: 特徵向量 (即 V)
    # 使用 eigh 因為 ATA 必為對稱矩陣 (Symmetric)，eigh 比 eig 更穩定且保證實數解
    eig_vals, V = np.linalg.eigh(ATA)
    
    # 3. 排序 (Sort)
    # eigh 回傳的順序通常是由小到大，SVD 需要由大到小
    # argsort 回傳的是索引
    sorted_indices = np.argsort(eig_vals)[::-1]
    
    eig_vals = eig_vals[sorted_indices]
    V = V[:, sorted_indices]
    
    # 4. 過濾非零奇異值 (數值誤差處理)
    # 取絕對值避免浮點數誤差導致極小的負數 (-1e-15)
    # 只取大於極小閾值的特徵值
    non_zero_indices = eig_vals > 1e-10
    sigma_squared = eig_vals[non_zero_indices]
    V = V[:, non_zero_indices] # 這是對應的 V (Reduced)
    
    # 5. 計算奇異值 Sigma (開根號)
    singular_values = np.sqrt(sigma_squared)
    
    # 6. 計算 U (Left Singular Vectors)
    # 公式: u_i = A * v_i / sigma_i
    # 這裡我們利用廣播機制計算
    # (M x N) @ (N x k) -> (M x k)
    U = A @ V
    # 將每一行除以對應的 singular_value 進行歸一化 (Normalization)
    U = U / singular_values
    
    # 7. 整理格式以符合標準 SVD 輸出
    # V 需要轉置成 V^T (Vh)
    Vh = V.T
    
    # 構造對角矩陣 Sigma
    Sigma_mat = np.diag(singular_values)
    
    return U, Sigma_mat, Vh

# --- 驗證程式 ---
if __name__ == "__main__":
    np.random.seed(42)
    
    # 建立一個非方陣 (例如 4x3) 來測試通用性
    A = np.array([
        [3.0, 1.0, 1.0],
        [-1.0, 3.0, 1.0],
        [1.0, 1.0, 1.0],
        [1.0, 1.0, 1.0] # 增加一列讓它是長方形矩陣
    ])
    
    print(f"--- 原始矩陣 A ({A.shape}) ---\n{A}\n")
    
    # 1. 執行我們手寫的 SVD
    my_U, my_S, my_Vh = svd_via_eig(A)
    
    print("--- 手寫 SVD 結果 ---")
    print(f"U shape: {my_U.shape}")
    print(f"Sigma shape: {my_S.shape}")
    print(f"Vh shape: {my_Vh.shape}")
    print(f"奇異值列表: {np.diag(my_S)}")
    
    # 2. 驗證重建 A = U * S * Vh
    A_reconstructed = my_U @ my_S @ my_Vh
    
    print(f"\n--- 重建驗證 ---")
    # print(A_reconstructed)
    error = np.linalg.norm(A - A_reconstructed)
    print(f"重建誤差: {error:.4e}")
    
    if np.allclose(A, A_reconstructed):
        print("✅ 成功！手寫 SVD 能夠還原矩陣。")
    else:
        print("❌ 失敗。")
        
    # 3. 與 NumPy 標準 svd 比對
    print(f"\n--- 與 NumPy 標準庫比對 (奇異值) ---")
    _, np_s, _ = np.linalg.svd(A)
    print(f"我的奇異值: {np.diag(my_S)}")
    print(f"標準奇異值: {np_s}")
  # gemini
