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

