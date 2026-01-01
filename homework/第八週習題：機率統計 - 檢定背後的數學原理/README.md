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

## T 檢定 (One-Sample T-Test)
**單樣本 T 檢定 (One-Sample T-Test)** 
情境：你有一組樣本，想知道它是否來自某個特定平均值 $\mu_0$ 的母體，但你不知道母體的 $\sigma$ 
<img width="731" height="426" alt="image" src="https://github.com/user-attachments/assets/e0fbc461-75eb-4365-968b-9a3c71d4dced" />

**雙樣本獨立 T 檢定 (Independent Two-Sample T-Test)** 
情境：兩組完全不相干的人（例如：實驗組吃藥，對照組吃糖），比較兩組平均值是否有差異。假設兩組變異數相等（Homogeneity of Variance） 
「兩個平均值的差」：$\Delta = \bar{X}_1 - \bar{X}_2$
<img width="720" height="506" alt="image" src="https://github.com/user-attachments/assets/0151236a-de41-40cc-9f9e-784dd03b1384" />

**雙樣本配對 T 檢定 (Paired Sample T-Test)** 
情境：同一組人，測量兩次（例如：減肥前 vs. 減肥後）。這兩組數據高度相關，不是獨立的  
因為樣本不獨立，我們不能用上面的公式。我們要做的第一件事是 **「消除個體差異」**  
* **計算差值 (Difference)**：
對於每一對樣本 $(X_{1i}, X_{2i})$，計算 $D_i = X_{1i} - X_{2i}$。
這一步把「雙樣本」問題直接降維成「單樣本」問題
* **轉化為單樣本檢定**：現在我們只需要檢驗 $D$ 這個新樣本的平均值 $\bar{D}$ 是否顯著不為 0。
<img width="119" height="63" alt="image" src="https://github.com/user-attachments/assets/1c18796b-5674-414c-bd40-8d420415cc83" />

$S_D$ 是差值樣本 $D$ 的標準差
$df = n - 1$
### 例子
**「減肥藥實驗」**  
單樣本 T 檢定 (One-Sample T-test)  
跟「標準」比  
情境：一款減肥藥，包裝上宣稱「平均能瘦 5 公斤」，你不相信，於是你找了 10 個朋友來吃吃看  
數據：這 10 個朋友平均瘦了 3 公斤  
單樣本 T 檢定就是幫你判斷： 你的「3 公斤」跟廠商宣稱的「5 公斤」差得夠不夠遠？夠遠就是廠商說謊  

雙樣本獨立 T 檢定 (Independent Two-Sample T-test)  
這一群 vs. 那一群（毫不相干）  
情境：「A 牌減肥藥」 和 「B 牌減肥藥」 哪個比較有效  
20 個人：  
* A 組：10 個男生，給他們吃 A 藥
* B 組：10 個女生，給他們吃 B 藥  
數據：A 組平均瘦 4 公斤，B 組平均瘦 6 公斤
獨立 T 檢定就是幫你判斷： 在考慮到兩群人本身就很雜亂的情況下，這 2 公斤的差距算不算「顯著」

雙樣本配對 T 檢定 (Paired T-test)  
現在的我 vs. 過去的我（自己跟自己比）  
情境： 這是最強大的測法。你不想被「體質不同」干擾，所以你決定 **「同一群人測兩次」**  
10 個人：  
* 第一次：先量體重（吃藥前）
* 第二次：吃藥一個月後，同一個人再量一次體重（吃藥後）  

**數據：**
* 小明：90kg -> 88kg (瘦 2kg)
* 小美：50kg -> 48kg (瘦 2kg)

雖然小明和小美體重差很多（90 vs 50，雜訊很大），但他們都瘦了 2 公斤（變化量很一致）  

* **單樣本**：標準是死的，雜訊只來自你的樣本
* **獨立雙樣本**訊最大，因為兩組人不一樣，你要同時處理兩邊的混亂
* **配對雙樣本**：透過「自己比自己」，把「個人差異」這個最大的雜訊消掉了，所以通常最容易測出結果

[AI]()
