## 傅立葉轉換
題目給出的是連續傅立葉轉換（Continuous Fourier Transform）的積分定義，但在電腦數值計算中，我們必須處理離散訊號，因此將實作 離散傅立葉轉換 (Discrete Fourier Transform, DFT) 及其逆轉換 (IDFT)

**原理**

取樣 (Sampling)：
將連續訊號 $f(x)$ 轉換為長度為 $N$ 的離散序列 $x[n]$

離散化公式：
積分 $\int$ 變為求和 $\sum$，連續頻率 $\omega$ 變為離散頻率索引 $k$

### 正轉換 (DFT)

$$X[k] = \sum_{n=0}^{N-1} x[n] \cdot e^{-i \frac{2\pi}{N} k n}, \quad k = 0, \dots, N-1$$

### 逆轉換 (IDFT)

$$x[n] = \frac{1}{N} \sum_{k=0}^{N-1} X[k] \cdot e^{i \frac{2\pi}{N} k n}, \quad n = 0, \dots, N-1$$

### 分三個層次
1. 【數學直觀】：傅立葉轉換到底在算什麼？（內積的概念）

傅立葉轉換的核心精神是： **「比較」你的訊號跟某個頻率的波長得像不像**  

公式： $$X[k] = \sum_{n=0}^{N-1} x[n] \cdot e^{-i \frac{2\pi}{N} k n}$$  
* $x[n]$：原始訊號
* $e^{-i \frac{2\pi}{N} k n}$：頻率為 $k$ 的「測試波」（由餘弦和正弦組成）
* $\sum$ (加總)：計算「相似度」

`加總出來的值很大（絕對值大），代表訊號裡含有很強的 $k$ 頻率成分；如果接近 0，代表兩者不相關（正交）`  

