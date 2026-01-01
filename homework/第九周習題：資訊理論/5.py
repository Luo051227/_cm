import numpy as np
from typing import Tuple, Dict

class Hamming74:
    """
    Hamming(7, 4) Code implementation using Matrix operations over GF(2).
    Uses systematic form: G = [I_4 | P]
    """
    def __init__(self):
        # 定義生成矩陣 G (4x7)
        # 前 4 列是單位矩陣 (I4)，後 3 列是同位檢查位 (P)
        self.G = np.array([
            [1, 0, 0, 0, 1, 1, 0],
            [0, 1, 0, 0, 1, 0, 1],
            [0, 0, 1, 0, 0, 1, 1],
            [0, 0, 0, 1, 1, 1, 1]
        ], dtype=int)

        # 定義同位檢查矩陣 H (3x7)
        # H = [P.T | I3]
        self.H = np.array([
            [1, 1, 0, 1, 1, 0, 0],
            [1, 0, 1, 1, 0, 1, 0],
            [0, 1, 1, 1, 0, 0, 1]
        ], dtype=int)

        # 建立 Syndrome 到 H 矩陣列索引(Column Index) 的映射表
        # 用於快速查找錯誤位置
        # Key: Syndrome 的十進制值 (例如 [1,0,1] -> 5)
        # Value: 錯誤位元的索引 (0-6)
        self.syndrome_map = {}
        rows, cols = self.H.shape
        for i in range(cols):
            # 取出 H 的第 i 列 (Column) 作為 Syndrome 特徵
            col_vec = self.H[:, i]
            # 將二進制向量轉為整數 key
            syndrome_val = int("".join(map(str, col_vec)), 2)
            self.syndrome_map[syndrome_val] = i

    def encode(self, data: np.ndarray) -> np.ndarray:
        """
        編碼函數：將 4-bit 數據轉換為 7-bit 碼字。
        
        Args:
            data (np.ndarray): 形狀為 (N, 4) 的二進制數據矩陣。
            
        Returns:
            np.ndarray: 形狀為 (N, 7) 的編碼後矩陣。
        """
        # 矩陣乘法: C = D . G (mod 2)
        # vectorization: (N, 4) @ (4, 7) -> (N, 7)
        encoded = np.dot(data, self.G) % 2
        return encoded.astype(int)

    def decode(self, received: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
        """
        解碼函數：計算伴隨式並修正 1-bit 錯誤。
        
        Args:
            received (np.ndarray): 形狀為 (N, 7) 的接收矩陣。
            
        Returns:
            Tuple[np.ndarray, np.ndarray]: (修正後的完整碼字, 解碼出的 4-bit 數據)
        """
        N = received.shape[0]
        
        # 1. 計算伴隨式 (Syndrome): S = R . H^T (mod 2)
        # (N, 7) @ (7, 3) -> (N, 3)
        syndrome_matrix = np.dot(received, self.H.T) % 2
        
        # 2. 錯誤修正 (Error Correction)
        # 建立錯誤遮罩矩陣 E (N, 7)，初始全為 0
        error_mask = np.zeros_like(received, dtype=int)
        
        # 將 Syndrome 矩陣的每一列轉換為十進制數值以便查表
        # 利用位元權重 [4, 2, 1] 快速轉換
        weights = np.array([4, 2, 1])
        syndrome_values = np.dot(syndrome_matrix, weights)
        
        # 找出有錯誤的樣本 (Syndrome != 0)
        error_indices = np.where(syndrome_values != 0)[0]
        
        if len(error_indices) > 0:
            for idx in error_indices:
                s_val = syndrome_values[idx]
                if s_val in self.syndrome_map:
                    # 查找錯誤位元的位置
                    bit_to_flip = self.syndrome_map[s_val]
                    # 設定遮罩以翻轉該位元
                    error_mask[idx, bit_to_flip] = 1
        
        # 3. 修正錯誤: Corrected = Received + Error_Mask (mod 2)
        corrected_code = (received + error_mask) % 2
        
        # 4. 提取數據: 系統碼的前 4 位即為原始數據
        decoded_data = corrected_code[:, :4]
        
        return corrected_code, decoded_data

# --- 測試程式碼 ---
if __name__ == "__main__":
    # 1. 準備測試數據 (Batch Size = 3)
    input_data = np.array([
        [1, 0, 1, 1], # Data A
        [0, 1, 1, 0], # Data B
        [1, 1, 1, 1]  # Data C
    ])
    
    hamming = Hamming74()
    
    print(f"--- 1. 原始數據 (Input) ---\n{input_data}")
    
    # 2. 編碼
    encoded = hamming.encode(input_data)
    print(f"\n--- 2. 編碼結果 (Encoded) ---\n{encoded}")
    
    # 3. 模擬雜訊通道 (加入錯誤)
    received = encoded.copy()
    # 故意翻轉第 0 筆數據的第 2 個 bit (index 2)
    received[0, 2] = (received[0, 2] + 1) % 2 
    # 故意翻轉第 1 筆數據的第 5 個 bit (index 5)
    received[1, 5] = (received[1, 5] + 1) % 2
    
    print(f"\n--- 3. 接收數據 (含雜訊) ---\n{received}")
    print("注意: Row 0 和 Row 1 被注入了錯誤。")
    
    # 4. 解碼與修正
    corrected_code, decoded_data = hamming.decode(received)
    
    print(f"\n--- 4. 修正後的碼字 ---\n{corrected_code}")
    print(f"\n--- 5. 解碼數據 (Decoded) ---\n{decoded_data}")
    
    # 驗證
    is_correct = np.array_equal(input_data, decoded_data)
    print(f"\n--- 驗證結果: {'成功' if is_correct else '失敗'} ---")
