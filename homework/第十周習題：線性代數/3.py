import numpy as np
import scipy.linalg

# --- 設定 ---
# 設定隨機種子以確保結果可重現
np.random.seed(42)
# 矩陣大小
N = 5

# --- 輔助函式：驗證與輸出結果 ---
def verify_and_print(name, original_A, reconstructed_A):
    """
    比較原始矩陣與重建矩陣是否相等 (在浮點數誤差範圍內)。
    使用了 np.allclose()，它會檢查兩個陣列是否在設定的容許誤差內相等。
    """
    print(f"--- 驗證 {name} ---")
    
    # 計算重建誤差 (Frobenius norm)
    error = np.linalg.norm(original_A - reconstructed_A)
    
    # 進行比較
    # atol 是絕對容許誤差，rtol 是相對容許誤差
    if np.allclose(original_A, reconstructed_A, atol=1e-10):
        print(f"✅ 驗證成功！重建矩陣與原矩陣相符。")
        print(f"   最大重建誤差: {error:.4e}\n")
    else:
        print(f"❌ 驗證失敗！重建矩陣與原矩陣不符。")
        print(f"   最大重建誤差: {error:.4e}\n")

# ==========================================
# 主程式開始
# ==========================================

# 1. 生成一個隨機的方陣 A
A = np.random.rand(N, N)
print(f"原始矩陣 A ({N}x{N}):")
# 為了版面整潔，只打印前兩行看看樣子
print(A[:2, :]) 
print("... (省略後續行) ...\n")
print("="*40 + "\n")


# ==========================================
# 1. LU 分解驗證 (A = P @ L @ U)
# ==========================================
# 注意：標準的 NumPy 沒有提供方便還原的 PLU 分解，我們使用 SciPy
# P: 排列矩陣 (Permutation matrix)
# L: 下三角矩陣 (Lower triangular)
# U: 上三角矩陣 (Upper triangular)
P, L, U = scipy.linalg.lu(A)

# 執行乘法重建
A_lu_recon = P @ L @ U

verify_and_print("LU 分解 (P@L@U)", A, A_lu_recon)


# ==========================================
# 2. 特徵值分解驗證 (A = V @ Λ @ V⁻¹)
# ==========================================
# eigen_vals: 特徵值 (一維陣列)
# V: 特徵向量矩陣 (每一行是一個特徵向量)
eigen_vals, V = np.linalg.eig(A)

# 將一維的特徵值陣列轉換成對角矩陣 Λ (Lambda)
Lambda = np.diag(eigen_vals)

# 計算 V 的逆矩陣
V_inv = np.linalg.inv(V)

# 執行乘法重建
# 注意：對於隨機矩陣，特徵值通常是複數。
# 重建後的矩陣也會帶有極小的虛部 (例如 1e-16j)，np.allclose 可以正確處理這種比較。
A_eig_recon = V @ Lambda @ V_inv

verify_and_print("特徵值分解 (V@Λ@V⁻¹)", A, A_eig_recon)


# ==========================================
# 3. SVD 分解驗證 (A = U @ Σ @ Vh)
# ==========================================
# U: 左奇異向量矩陣 (正交矩陣)
# s: 奇異值 (一維陣列)
# Vh: 右奇異向量矩陣的共軛轉置 (V Hermitian)
U_svd, s, Vh = np.linalg.svd(A)

# 將一維的奇異值陣列轉換成對角矩陣 Σ (Sigma)
Sigma = np.diag(s)

# 執行乘法重建
# 數學公式是 U Σ V^H，NumPy 直接回傳了 Vh，所以直接相乘即可
A_svd_recon = U_svd @ Sigma @ Vh

verify_and_print("SVD 分解 (U@Σ@Vh)", A, A_svd_recon)
# gemini
