import numpy as np
from typing import Tuple

def lu_decomposition_no_pivot(A: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    """
    執行基礎 LU 分解 (Doolittle Algorithm)。
    
    數學原理: A = L @ U
    - L: Unit Lower Triangular Matrix (對角線為 1)
    - U: Upper Triangular Matrix
    
    注意：此為教學用基礎實作，未包含 Partial Pivoting (列交換)。
    若矩陣對角線出現 0，數值會不穩定或報錯。
    """
    n = A.shape[0]
    if A.shape[0] != A.shape[1]:
        raise ValueError("LU 分解僅適用於方陣")

    # 1. 初始化
    # L 預設為單位矩陣 (對角線為 1，其餘 0)
    L = np.eye(n)
    # U 複製 A 的數據 (必須轉為 float 以防整數除法誤差)
    U = A.astype(float).copy()

    # 2. 高斯消去 (Gaussian Elimination)
    for k in range(n - 1): # k 是主元 (Pivot) 的索引
        pivot = U[k, k]
        
        # 簡單的防呆檢查
        if np.isclose(pivot, 0.0):
            raise ValueError(f"主元 U[{k},{k}] 為 0，標準 LU 分解失效，需要 Pivot 機制。")

        # --- 向量化運算 (Vectorization) ---
        # 找出第 k 列下方所有的元素
        # 我們要消去 U[k+1:, k] 這些位置的數值
        
        # 計算乘數向量 (Multipliers)
        # factors shape: (n - 1 - k, )
        factors = U[k+1:, k] / pivot
        
        # 將乘數填入 L 的對應位置
        L[k+1:, k] = factors
        
        # 更新 U 矩陣的剩餘部分
        # Row_i = Row_i - factor * Row_k
        # 利用廣播 (Broadcasting): (n-1-k, 1) * (1, n-k) -> (n-1-k, n-k)
        # 這裡我們一次更新所有下方的列
        U[k+1:, k:] -= factors[:, np.newaxis] * U[k, k:]

    return L, U

def det_using_lu(A: np.ndarray) -> float:
    """
    利用 LU 分解計算行列式。
    
    數學原理: 
    det(A) = det(L) * det(U)
           = 1 * prod(diag(U))
    """
    try:
        L, U = lu_decomposition_no_pivot(A)
        
        # 計算 U 的對角線乘積
        # np.diag(U) 取出對角線陣列
        det_val = np.prod(np.diag(U))
        return det_val
        
    except ValueError as e:
        print(f"計算失敗: {e}")
        return 0.0

# --- 測試主程式 ---
if __name__ == "__main__":
    # 1. 定義一個 3x3 測試矩陣
    # 這裡刻意設計一個可逆矩陣
    A_test = np.array([
        [2, -1, -2],
        [-4, 6, 3],
        [-4, -2, 8]
    ])
    
    print(f"--- 原始矩陣 A ---\n{A_test}\n")

    # 2. 執行 LU 分解
    L_res, U_res = lu_decomposition_no_pivot(A_test)
    
    print(f"--- 下三角 L (det=1) ---\n{L_res}")
    print(f"--- 上三角 U ---\n{U_res}\n")

    # 3. 計算行列式
    my_det = det_using_lu(A_test)
    
    # 驗證步驟
    # U 的對角線元素
    diag_u = np.diag(U_res)
    print(f"U 的對角線元素: {diag_u}")
    print(f"計算過程: {' * '.join(map(str, diag_u))}")
    print(f"我的行列式結果: {my_det:.4f}")

    # 4. 與 NumPy 內建函數比對
    np_det = np.linalg.det(A_test)
    print(f"NumPy 標準結果: {np_det:.4f}")
    
    # 5. 驗證準確度
    if np.isclose(my_det, np_det):
        print("\n✅ 驗證成功！結果一致。")
    else:
        print("\n❌ 驗證失敗。")

    # 6. 驗證 L * U 是否還原 A
    reconstructed_A = L_res @ U_res
    print(f"\n重建矩陣 L@U 誤差: {np.linalg.norm(A_test - reconstructed_A):.2e}")
  # gemini
