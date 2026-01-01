## Z-test（Z 檢定）
看作是一個 **「訊號雜訊比 (Signal-to-Noise Ratio)」** 的測量過程

<img width="552" height="133" alt="image" src="https://github.com/user-attachments/assets/81f6e3ac-cc82-4e0c-8fda-c9b6b3eda497" />

**分子**：訊號 (Signal) $\rightarrow (\bar{X} - \mu_0)$
* $\mu_0$：是我們假設的基準線（例如：歷史平均成績 60 分）
* $\bar{X}$：是我們這次抽樣算出來的平均（例如：這班學生平均 65 分）

**分母**：雜訊 (Noise) $\rightarrow \frac{\sigma}{\sqrt{n}}$
**標準誤 (Standard Error, SE)** 
* 如果抽 1 個人 ($n=1$)，他的成績可能很不穩定（可能考 100 也可能考 0），波動很大 ($\sigma$)
* 如果抽 100 個人 ($n=100$) 算平均，這個「平均值」就會很穩定，不容易忽高忽低 
樣本數 $n$ 越大，分母 $\frac{\sigma}{\sqrt{n}}$ 就越小 
分母越小，算出來的 $Z$ 值就會越大（代表訊號越強）。這意味著：**樣本數越大，我們越容易發現微小的差異** 

**Z 值 (The Z-Score)** 
Z 值其實就是一把標準尺。它把「分數」、「公分」、「公斤」這些單位全部拿掉，轉換成 **「標準差倍數」** 

<img width="632" height="581" alt="image" src="https://github.com/user-attachments/assets/b529df0b-b5c9-484d-84ff-6231d414ff0b" />



[AI]()
