import numpy as np
import matplotlib.pyplot as plt
from typing import Tuple

def run_pca(X: np.ndarray, n_components: int) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    執行主成份分析 (PCA)。
    
    數學原理:
    1. Center: X - mean
    2. Covariance: C = (X.T @ X) / (n-1)
    3. Eigen: C v = lambda v
    4. Project: Z = X @ W
    
    Args:
        X: 輸入數據矩陣 (n_samples, n_features)
        n_components: 欲保留的主成份數量 (k)
        
    Returns:
        X_projected: 降維後的數據 (n_samples, n_components)
        components: 主成份向量 (n_components, n_features) -> 也就是特徵向量
        explained_variance: 解釋變異數 (特徵值)
    """
    # 1. 數據中心化 (Centering)
    # axis=0 代表沿著 "列" (樣本) 方向計算平均，得到每個特徵的平均
    mean_vec = np.mean(X, axis=0)
    X_centered = X - mean_vec
    
    # 2. 計算共變異數矩陣 (Covariance Matrix)
    n_samples = X.shape[0]
    # 公式: C = 1/(n-1) * X.T * X
    # rowvar=False 代表每一列是一個樣本，每一行是一個特徵 (與 NumPy 預設相反，需注意)
    # 這裡我們手動算以對應數學公式
    cov_matrix = (X_centered.T @ X_centered) / (n_samples - 1)
    
    # 3. 特徵值分解 (Eigendecomposition)
    # 使用 eigh 因為共變異數矩陣是對稱的 (Hermitian)，更穩定
    eigen_vals, eigen_vecs = np.linalg.eigh(cov_matrix)
    
    # 4. 排序 (Sort)
    # eigh 回傳是由小到大，我們需要由大到小
    sorted_indices = np.argsort(eigen_vals)[::-1]
    
    eigen_vals = eigen_vals[sorted_indices]
    eigen_vecs = eigen_vecs[:, sorted_indices]
    
    # 5. 選取前 k 個主成份 (Top-k Components)
    # components_matrix 形狀: (n_features, n_components)
    components_matrix = eigen_vecs[:, :n_components]
    
    # 6. 投影 (Projection)
    # Z = X_centered @ W
    X_projected = X_centered @ components_matrix
    
    # 回傳時轉置 components 以符合 scikit-learn 慣例 (n_components, n_features)
    return X_projected, components_matrix.T, eigen_vals[:n_components]

def plot_pca_result(X: np.ndarray, pca_components: np.ndarray, mean: np.ndarray):
    """
    視覺化 PCA 找到的主軸
    """
    plt.figure(figsize=(8, 8))
    
    # 繪製原始數據
    plt.scatter(X[:, 0], X[:, 1], alpha=0.4, label='Data')
    
    # 繪製主成份向量 (箭頭)
    # pca_components[0] 是第一主成份 (變異數最大)
    # pca_components[1] 是第二主成份
    colors = ['r', 'g']
    labels = ['PC1 (Max Variance)', 'PC2']
    
    for i, (comp, color) in enumerate(zip(pca_components, colors)):
        # 畫箭頭: 從平均值出發，指向特徵向量方向
        # 乘上 3 * std 是為了讓箭頭長度在圖上明顯一點 (視覺效果)
        length = 3.0 * np.sqrt(np.var(X @ comp.T)) 
        end_point = mean + comp * length
        
        plt.arrow(mean[0], mean[1], 
                  comp[0] * length, comp[1] * length,
                  head_width=0.3, head_length=0.4, fc=color, ec=color, linewidth=2, label=labels[i])

    plt.title('PCA Analysis: Principal Components')
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.legend()
    plt.axis('equal') # 確保比例尺一致，才看得出垂直關係
    plt.grid(True, linestyle=':', alpha=0.6)
    plt.show()

# --- 主程式 ---
if __name__ == "__main__":
    np.random.seed(42)
    
    # 1. 生成相關性數據 (Correlated Data)
    # 先生成標準常態分佈
    n_samples = 300
    X_random = np.random.randn(n_samples, 2)
    
    # 定義變換矩陣來拉伸與旋轉數據 (模擬特徵間的相關性)
    # [ 2, 1]
    # [ 1, 3]
    transformation = np.array([[0.6, -0.6], [-0.4, 0.8]]) * 5
    
    # X = X_rand @ T + mean
    X_synthetic = X_random @ transformation + np.array([2, 3])
    
    # 2. 執行 PCA
    # 我們保留 2 個成份來觀察它們的方向
    X_pca, components, explained_vars = run_pca(X_synthetic, n_components=2)
    
    print(f"--- PCA 結果 ---")
    print(f"主成份向量 (Eigenvectors):\n{components}")
    print(f"解釋變異數 (Eigenvalues): {explained_vars}")
    
    # 驗證 PC1 與 PC2 是否正交 (點積為 0)
    orthogonality = np.dot(components[0], components[1])
    print(f"向量正交性檢查 (Dot Product): {orthogonality:.4e}")
    
    # 3. 視覺化
    plot_pca_result(X_synthetic, components, np.mean(X_synthetic, axis=0))
  # gemini
