# 課程：程式與數學

欄位 | 內容
-----|--------
學期 | 114 學年上學期
學生 |  羅詩喬
學號末兩碼 | 01
教師 | [陳鍾誠](https://www.nqu.edu.tw/educsie/index.php?act=blog&code=list&ids=4)
學校科系 | [金門大學資訊工程系](https://www.nqu.edu.tw/educsie/index.php)
課程教材 | https://github.com/ccc114a/py2cs 
# 習題 1 : 請用程式驗證微積分基本定理
## 數值微分 df(f, x)
<img width="473" height="74" alt="image" src="https://github.com/user-attachments/assets/6deec916-a48a-42f8-ae86-a4fa35cf2bc4" />

## 數值積分 integral(f, a, b)
<img width="559" height="79" alt="image" src="https://github.com/user-attachments/assets/0314f3ea-ad8f-42ac-aac3-325bec65d88e" />

`將曲線下的面積切成無數個寬度為 h 的小長方形，算出每個長方形的面積（高 f(x) * 寬 h）並加總`
## 微積分基本定理驗證 theorem1(f, x)
$$r = \frac{d}{dx} \left( \int_{0}^{x} f(t) \, dt \right)$$

全使用AI

[作業](https://github.com/Luo051227/_cm/tree/main/homework/%E7%BF%92%E9%A1%8C1)

# 習題 2 : 請寫程式求解二次多項式的根
使用了 cmath 函式庫

公式： $$ax^2 + bx + c = 0$$

公式解： $$x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$$

先使用a、b、c代表 $$ax^2+bx+c=0$$

**判別式**  $$b^2 - 4ac$$

<img width="764" height="347" alt="image" src="https://github.com/user-attachments/assets/84a9a5f1-5f63-41d5-9e78-8b8049ab5af9" />

用 lambda 建立了一個「簡短的數學函數」
定義 $$f(x) = ax^2 + bx + c$$
`rel_tol=1e-9`：這是容許的誤差範圍（小數點後 9 位）

全使用AI

[作業](https://github.com/Luo051227/_cm/tree/main/homework/%E7%BF%92%E9%A1%8C2)

# 習題 3 : 請寫程式求解三次多項式的根 (加分題）
全使用AI 
[作業](https://github.com/Luo051227/_cm/tree/main/homework/%E7%BF%92%E9%A1%8C3)

# 習題 4 : （思考）請寫一個函數 root(c) 求出 n 次多項式的根 （ n>=5 的時候，數學上證明沒有公式 -- 伽羅瓦定理）
全使用AI 
[作業](https://github.com/Luo051227/_cm/tree/main/homework/%E7%BF%92%E9%A1%8C4)

# 第二週習題：有限體 
## 1. 有限體是什麼?
有限體（finite field，也叫 Galois field）是一種包含有限個元素的「體」（field）。

一個體必須同時滿足：
1. 加法形成阿貝爾群（包含 0）
* 封閉性：a + b ∈ F
* 單位元：存在 0
* 反元素：每個 a 都有 −a
* 結合律、交換律
2. 乘法形成阿貝爾群（不含 0）
* 封閉性：a × b ∈ F
* 單位元：存在 1
* 反元素：每個 a ≠ 0 都有 a⁻¹
* 結合律、交換律
3. 分配律
* a × (b + c) = a × b + a × c

應用：錯誤更正碼（Reed–Solomon）、密碼學（例如 ECC 使用有限域上的點運算）、多項式插值算法、數論與代數幾何等。

直觀補充：GF(p) 可以想像成“環繞”在 0..p-1 上做加減乘除（除以 0 除外），而 GF(p^n) 則是把多項式係數放在 GF(p) 上，使用不可約多項式把次數降低，得到更大的有限集合但仍然保持域性質。
## 2. 有限體觀念（我對 AI 答案與數學的理解）
有限體（finite field）是一個包含有限個元素的域（field）。域需要兩個運算：加法與乘法，且加法構成可交換群、乘法（去掉零）也構成可交換群，兩者之間還要滿足分配律。最簡單又常見的是 GF(p)（p 為質數）——這是所有整數模 p 的集合，進行模 p 加減乘除（除以 0 例外）。更一般的 GF(p^n) 可用多項式環模不可約多項式來構造（較複雜，超出本次程式實作範圍，但在密碼學與編碼裡很常見）。

我把這些理論對應到程式：  
- 實作 GF(p) 的元素類別 `FiniteFieldElement`（operator overloading 支援 `+ - * /`），其底層運算都在 0..p-1 上做模 p 運算。  
- 用 `group_axioms.py` 提供的檢查函數，驗證加法群與乘法群（非零）是否滿足群公理。  
- 用 `field_axioms.py` 的 `check_distributivity()` 驗證分配律是否成立。  
這樣能把抽象的代數公理用程式具體驗證於有限集合上，幫助理解。

---

## 3. 程式檔案說明
- `finite_field.py` : GF(p) 元素類別（`FiniteFieldElement`），支援 `+ - * /`。  
- `group_axioms.py`  : 提供群公理檢驗工具（closure, assoc, identity, inverses, commutativity）。  
- `field_axioms.py`  : 檢查分配律 `a*(b+c) == a*b + a*c`。  
- `example_run.py`   : 範例執行檔，會對 GF(2), GF(3), GF(5), GF(7) 執行檢查並印出結果。

---

## 4. 如何執行
1. 把上述四個檔案放在同一個資料夾。  
2. 執行 `python example_run.py`。  
3. 若一切正常，你會看到 GF(2), GF(3), GF(5), GF(7) 都通過檢查的訊息。

---

## 5. 我對 AI 回答、數學與程式之間連結的補述
- AI 回答提供了有限體的定義與例子，對於程式設計的指引是：在 GF(p) 上把每個元素實作成一個物件（包含模 p 的規範化與逆元計算），然後提供加、減、乘、除的 operator。  
- 程式驗證部分把抽象的公理（群公理、分配律）變成「窮舉檢查」，這在有限集合上是可行且直接的：直接檢查所有可能的 a,b,c 組合是否符合條件。  
- 對於更進階的 GF(p^n)（當 n>1）需要做多項式運算與模不可約多項式，這會使實作與驗證更複雜；本次作業先聚焦在 GF(p) 做完整的理解與程式驗證。

全使用AI

[作業](https://github.com/Luo051227/_cm/tree/main/homework/%E7%AC%AC%E4%BA%8C%E9%80%B1%E7%BF%92%E9%A1%8C%EF%BC%9A%E6%9C%89%E9%99%90%E9%AB%94)
[AI](https://chatgpt.com/share/6924476a-fd44-8012-a7be-87cdaada71f6)
# 第三週習題：幾何學：（點，線，圓）世界的建構
## 點 (Point)
`定義為只有位置、沒有大小（寬度、長度和高度）`  
* 點是零維的幾何實體
* 通常用大寫英文字母（如 A, B, P）表示  

兩點間距離公式：d = √{(x_2-x_1)^2 + (y_2-y_1)^2}

## 直線 (Line)
直線是一維的、無限延伸的、由無數點組成的集合。  

一般式 (Standard Form)：` Ax + By + C = 0，其中 A 和 B 不全為零。`  

斜截式 (Slope-intercept Form)：`y = mx + b，其中 m 是斜率，b 是 y 軸截距。`  
## 圓 (Circle)
圓是在平面上，到固定點（圓心）距離為定值（半徑）的所有點的集合。  
圓標準式 (Standard Form)：<img width="300" height="75" alt="image" src="https://github.com/user-attachments/assets/9f132c8b-9053-499b-8fcd-e273087eb16a" />`，其中 (h, k) 是圓心，r 是半徑。`  
<img width="200" height="113" alt="image" src="https://github.com/user-attachments/assets/f39e5012-3e18-473e-8021-e4f8d57d07d5" />  
<img width="600" height="397" alt="image" src="https://github.com/user-attachments/assets/02c6aba2-5767-4d93-b962-804a0b109c39" />

切線 (Tangent Line)
* 條件： d = r
* 特性： 直線與圓恰好只有一個交點
* 切點的半徑相互垂直
割線 (Secant Line)
* 條件： d < r
* 特性： 直線與圓有兩個交點。
* 割線在圓內部：弦
* 割線通過圓心：直徑
### 判斷直線與圓的交點
<img width="615" height="246" alt="image" src="https://github.com/user-attachments/assets/6ccedef2-b4b6-40d0-b59d-c63bcc8e7579" />



## 兩直線交點 (Intersection of Two Lines)
兩條直線可以用一般式表示：<img width="323" height="23" alt="image" src="https://github.com/user-attachments/assets/1b08e439-6fcd-4b42-840b-d6af650cd44b" />
```python
def intersect_lines(a1, b1, c1, a2, b2, c2):
    # 計算行列式 Determinant
    det = a1 * b2 - a2 * b1
    if det == 0:
        return None  # 平行或重合，無單一交點
    
    x = (c1 * b2 - c2 * b1) / det
    y = (a1 * c2 - a2 * c1) / det
    return (x, y)

# 範例：x + y = 2 且 x - y = 0
print(f"直線交點: {intersect_lines(1, 1, 2, 1, -1, 0)}") # 預期 (1.0, 1.0)
```

## 克拉瑪公式
<img width="156" height="92" alt="image" src="https://github.com/user-attachments/assets/d5a067f1-98fd-4f77-9770-1db49ec11f49" />
<img width="452" height="47" alt="image" src="https://github.com/user-attachments/assets/63ee211b-b92b-413d-8b7e-fcbcdd7f6291" />
<img width="477" height="502" alt="image" src="https://github.com/user-attachments/assets/00aecca4-6407-4ed4-bde3-42ee336e193e" />
<img width="504" height="108" alt="image" src="https://github.com/user-attachments/assets/12fefba4-4c13-4712-8a29-98af579ed65a" />



### 數學基礎：
`D = A_1B_2 - A_2B_1` `D_x = C_2B_1 - C_1B_2` `D_y = A_2C_1 - A_1C_2`

如果 D \neq 0，則交點為 (x, y) = (\frac{D_x}{D}, \frac{D_y}{D})。如果 $D = 0$：若 D_x = 0 且 D_y = 0，則兩線重合（無限多交點）。若 D_x \neq 0 或 D_y \neq 0，則兩線平行（無交點）。  

全使用AI

[作業](https://github.com/Luo051227/_cm/tree/main/homework/%E7%AC%AC%E4%B8%89%E9%80%B1%E7%BF%92%E9%A1%8C%EF%BC%9A%E5%B9%BE%E4%BD%95%E5%AD%B8%EF%BC%9A%EF%BC%88%E9%BB%9E%EF%BC%8C%E7%B7%9A%EF%BC%8C%E5%9C%93%EF%BC%89%E4%B8%96%E7%95%8C%E7%9A%84%E5%BB%BA%E6%A7%8B)
[AI](https://gemini.google.com/share/ca1dd991cd0f)
# 第八週習題：機率統計 - 檢定背後的數學原理
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
[作業](https://github.com/Luo051227/_cm/tree/main/homework/%E7%AC%AC%E5%85%AB%E9%80%B1%E7%BF%92%E9%A1%8C%EF%BC%9A%E6%A9%9F%E7%8E%87%E7%B5%B1%E8%A8%88%20-%20%E6%AA%A2%E5%AE%9A%E8%83%8C%E5%BE%8C%E7%9A%84%E6%95%B8%E5%AD%B8%E5%8E%9F%E7%90%86)
[AI](https://gemini.google.com/share/7c3ae9b3d54f)
# 第九周習題：資訊理論
## 寫一個程式，計算一公平銅板，連續投擲 10000 次，全部得到正面的機率。 (p^10000)
```python
import math

a=0.5
print(a**10000)
```

## 寫另一個程式，用 log(p^n) = n log(p) 計算 log(p^n)，然後代入 p=0.5，算出 log(0.5^10000)
```python
import math

p=0.5
print(10000*math.log10(p))
```
## 寫程式計算『熵，交叉熵，KL 散度，互熵（互資訊）』
**熵**
```python
import numpy as np

a=[0.5, 0.25, 0.25]
p=np.array(a)

print(-np.sum(p * np.log2(p)))
```
**交叉熵**
```python
import numpy as np

a=[0.5, 0.25, 0.25]
b=[0.6, 0.2, 0.2]
p=np.array(a)
q=np.array(b)

print(-np.sum(p * np.log2(q)))
```
**KL 散度**
```python
import numpy as np

a=[0.5, 0.25, 0.25]
b=[0.6, 0.2, 0.2]
p=np.array(a)
q=np.array(b)

print(np.sum(p * np.log2(p/q)))
```
**互熵（互資訊）**
```python
import numpy as np

def mutual_information(joint):
    joint = np.array(joint)
    px = np.sum(joint, axis=1)
    py = np.sum(joint, axis=0)

    mi = 0.0
    for i in range(joint.shape[0]):
        for j in range(joint.shape[1]):
            if joint[i, j] > 0:
                mi += joint[i, j] * np.log2(joint[i, j] / (px[i] * py[j]))
    return mi
# 聯合機率表 p(x,y)
Pxy = [
    [0.25, 0.25],
    [0.25, 0.25]
]

print("Mutual Information:", mutual_information(Pxy))
#此為AI寫的
```
## 夏農信道編碼定理
`由克勞德·夏農（Claude Shannon）於 1948 年提出`  
**夏農信道編碼定理（Shannon's Channel Coding Theorem）**，又稱為**有噪信道編碼定理**。它劃定了一條通信的物理極限，告訴我們：「在雜訊干擾的通道中，我們最大能以多快的速度進行『無錯誤』傳輸。」  
### 核心定義
通道容量 (Channel Capacity, $C$)：通道傳輸資訊的最大能力，定義為輸入與輸出之間的**互資訊（Mutual Information**的最大值：$$C = \max_{P(X)} I(X; Y) \quad \text{(bits/channel use)}$$  
傳輸速率 (Rate, $R$)：
我們希望每使用一次通道傳輸 $R$ bits 的資訊。若碼長為 $n$，資訊位元為 $k$，則 $R = \frac{k}{n}$  
### 定理陳述
<img width="738" height="229" alt="image" src="https://github.com/user-attachments/assets/97b53963-fc03-4d11-b373-83bad5b8ba81" />    

### 例子
**定理的第一部分：只要夠囉唆，就不會出錯**    
 * 方法 A（無編碼，講太快）： 你只說一次：「炒飯！」 結果：因為旁邊有人摔盤子，服務生聽成「炒蛋」。 --> 失敗。  
 * 方法 B（夏農的編碼，增加冗餘）： 你跟服務生約定好一種講話方式（編碼）： 你說：「我要點炒飯，炒飯的炒，炒飯的飯，是炒飯喔。」  
   * 雖然旁邊很吵，服務生聽到了：「我要點X飯，X飯的炒，炒飯的X，是炒飯喔。」  
   * 雖然漏了幾個字，但因為你給的**線索（冗餘資訊）**夠多，服務生腦補也能拼出「喔！他是要炒飯」。 --> 成功！  
`降低傳輸速率，增加檢查碼`
    
**定理的第二部分：但你不能講太快**  
講話的速度，快過了服務生耳朵分辨聲音的極限（這就是夏農極限，Channel Capacity)  
`物理極限是殘酷的。 一旦你的語速超過了這個極限，無論你用什麼聰明的確認方法、無論怎麼重複，服務生一定會聽錯。資訊一定會丟失`  

1. 離 WiFi 基地台遠的時候，網速會變慢
   * 離得遠，雜訊變大（相當於熱炒店變更吵）
   * 為了不傳錯資料（不點錯菜），路由器自動切換成「多講幾次、講慢一點」的模式（降低 Rate）
2. 為什麼 5G 比 4G 快？
   * 5G 用了更寬的馬路（頻寬更大）和更強的編碼技術（更聰明的說話方式），提升了那條「極限線」

**在吵雜的世界裡，只要你講得夠慢、廢話（檢查碼）夠多，就一定能把話講清楚；但如果你想講得比『物理極限』還快，那神仙也救不了你。**
## 夏農-哈特利定理 (Shannon–Hartley Theorem)
<img width="740" height="166" alt="image" src="https://github.com/user-attachments/assets/2a84a836-ea89-4fa7-ac92-e70421732498" />


**變數定義：**
1. C (Channel Capacity)：
通道容量，單位是 位元每秒 (bps)。這是理論上的最高速度
2. B (Bandwidth)：
頻寬，單位是 赫茲 (Hz)。代表你佔用的頻譜寬度（路有多寬）
3. S/N (Signal-to-Noise Ratio, SNR)：訊雜比。
   * S：訊號的平均功率 (Watt)
   * N：雜訊的平均功率 (Watt)
   * **注意：** 公式裡的 S/N 是線性倍數，但工程上常給 分貝 (dB)，計算前必須轉換
### 例子
把傳輸數據想像成 **「在一條高速公路上運貨」**  
1. B (Bandwidth, 頻寬)：高速公路的「車道數」
   頻寬就是車道的數量
   * 10 MHz 的頻寬 = 1 線道
   * 20 MHz 的頻寬 = 2 線道
   * 100 MHz 的頻寬 = 10 線道
   線性：把馬路從 1 線道拓寬成 2 線道，在車速不變的情況下，同一時間通過的車流量（數據量）自然就是 2 倍
2. $S/N$ (SNR, 訊雜比)：車子的「載貨量」
   一個脈衝（一台車）到底能載多少 bit（貨物）
   物理意義：   SNR 決定了訊號的 **「解析度」** 。
   雜訊 ($N$) 就像是霧氣，訊號 ($S$) 就像是燈光亮度
   * 低 SNR (霧大、燈暗)：
接收端看不清楚。你只能發送很簡單的訊號，例如「有光」代表 1，「沒光」代表 0。
$\rightarrow$ 每台車只能載 1 個 bit (BPSK)。
   * 高 SNR (晴天、燈亮)：
接收端看得很清楚。你可以玩花樣，規定：
「全亮」= 11
「七分亮」= 10
「三分亮」= 01
「沒光」= 00
$\rightarrow$ 每台車可以載 2 個 bits (QPSK)。
   * 極高 SNR (超高清)：
你可以把光線分成 256 種亮度等級，接收端都能分得出來！
$\rightarrow$ 每台車可以載 8 個 bits (256-QAM)

**要讓車子的載貨量（bits）加 1，難度是翻倍的**  
* 1 bit：你需要分辨 2 個等級 (0, 1)
* 2 bits：你需要分辨 4 個等級 (00, 01, 10, 11)
* 8 bits：你需要分辨 256 個等級
想在同一個脈衝裡塞進更多 bit，就必須把電壓（或亮度）切得更細

想但雜訊 ($N$) 是固定存在的，為了讓這 256 個等級不被雜訊混淆，必須把總功率 ($S$) 加大非常多倍，才能把每個等級之間的距離拉開

公式中 $\log_2(1 + S/N)$ 的由來：
功率 ($S$) 必須呈指數級增加，才能換取容量 ($C$) 的線性微幅增加  
[作業](https://github.com/Luo051227/_cm/tree/main/homework/%E7%AC%AC%E4%B9%9D%E5%91%A8%E7%BF%92%E9%A1%8C%EF%BC%9A%E8%B3%87%E8%A8%8A%E7%90%86%E8%AB%96)
[AI](https://gemini.google.com/share/4569a8c5f859)
# 第十周習題：線性代數
[作業](https://github.com/Luo051227/_cm/tree/main/homework/%E7%AC%AC%E5%8D%81%E5%91%A8%E7%BF%92%E9%A1%8C%EF%BC%9A%E7%B7%9A%E6%80%A7%E4%BB%A3%E6%95%B8)
[AI]()
# 第11周習題：請寫出傅立葉正轉換和逆轉換的函數（不要用套件）
[作業](https://github.com/Luo051227/_cm/tree/main/homework/%E7%AC%AC11%E5%91%A8%E7%BF%92%E9%A1%8C%EF%BC%9A%E8%AB%8B%E5%AF%AB%E5%87%BA%E5%82%85%E7%AB%8B%E8%91%89%E6%AD%A3%E8%BD%89%E6%8F%9B%E5%92%8C%E9%80%86%E8%BD%89%E6%8F%9B%E7%9A%84%E5%87%BD%E6%95%B8%EF%BC%88%E4%B8%8D%E8%A6%81%E7%94%A8%E5%A5%97%E4%BB%B6%EF%BC%89)
[AI]()
# 第13周習題：請寫程式求解常係數齊次常微分方程
[作業](https://github.com/Luo051227/_cm/tree/main/homework/%E7%AC%AC13%E5%91%A8%E7%BF%92%E9%A1%8C%EF%BC%9A%E8%AB%8B%E5%AF%AB%E7%A8%8B%E5%BC%8F%E6%B1%82%E8%A7%A3%E5%B8%B8%E4%BF%82%E6%95%B8%E9%BD%8A%E6%AC%A1%E5%B8%B8%E5%BE%AE%E5%88%86%E6%96%B9%E7%A8%8B)
[AI]()
# 期中
## 羅倫茲吸引子 (Lorenz Attractor)
### 由來
1963 年，氣象學家 愛德華·羅倫茲 (Edward Lorenz) 用電腦模擬天氣。方程式很簡單，他有一天想把運算結果重跑一遍。

為了省時間，他沒有輸入完整的數據 `0.506127`，而是四捨五入輸入了 `0.506`。他以為這 `0.000127` 的微小差距應該沒影響。

結果去喝杯咖啡回來，發現兩次模擬出來的天氣完全不同！ 一個是大晴天，一個是暴風雨。
### 圖形
`羅倫茲將這三個變數（代表氣溫、氣壓、氣流等）畫在 3D 空間中`
* 不會重複： 這條線繞了幾萬圈，永遠不會跟之前的路徑重疊
* 有範圍但無規律： 它永遠不會跑出這個「蝴蝶翅膀」的範圍（所以叫「吸引子」，把軌跡吸住），但你永遠不知道它下一秒會飛到左邊翅膀還是右邊翅膀
* 混沌 (Chaos)： 它不是亂數，它有公式，但結果卻無法預測
### 蝴蝶效應python
* 藍色點： 從 `(0, 1, 1.05)` 出發
* 黃色點： 從 `(0, 1, 1.05 + 0.01)` 出發
```python
import numpy as np
import matplotlib.pyplot as plt

# 1. 定義羅倫茲方程 (這就是天氣運作的簡化規則)
def lorenz_step(x, y, z, s=10, r=28, b=2.667, dt=0.01):
    x_dot = s * (y - x)
    y_dot = r * x - y - x * z
    z_dot = x * y - b * z
    # 更新位置 (歐拉法)
    return x + x_dot * dt, y + y_dot * dt, z + z_dot * dt

# 2. 設定參數
dt = 0.01
num_steps = 3000

# 3. 初始化兩條軌跡 (起點只差一點點！)
# 軌跡 A
xs, ys, zs = np.empty(num_steps), np.empty(num_steps), np.empty(num_steps)
xs[0], ys[0], zs[0] = (0., 1., 1.05)

# 軌跡 B (只差 0.01)
xs2, ys2, zs2 = np.empty(num_steps), np.empty(num_steps), np.empty(num_steps)
xs2[0], ys2[0], zs2[0] = (0., 1., 1.05 + 0.01) # <--- 這裡就是蝴蝶效應的源頭

# 4. 開始運算
for i in range(num_steps - 1):
    xs[i+1], ys[i+1], zs[i+1] = lorenz_step(xs[i], ys[i], zs[i])
    xs2[i+1], ys2[i+1], zs2[i+1] = lorenz_step(xs2[i], ys2[i], zs2[i])

# 5. 畫圖
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(projection='3d')

# 畫第一條線 (藍色)
ax.plot(xs, ys, zs, lw=0.8, c='blue', alpha=0.7, label='Butterfly 1')

# 畫第二條線 (黃色 dashed)
# 注意看：前幾步它們是重疊的，後面突然分開
ax.plot(xs2, ys2, zs2, lw=0.8, c='orange', linestyle='--', alpha=0.8, label='Butterfly 2 (Start +0.01)')

ax.set_title("Lorenz Attractor: The Butterfly Effect")
ax.legend()
plt.show()
```
### 數學原理
$$\begin{cases}
\frac{dx}{dt} = \sigma (y - x) \\
\frac{dy}{dt} = x (\rho - z) - y \\
\frac{dz}{dt} = xy - \beta z
\end{cases}$$
* $x$ (流速)： 對流翻滾的速度。正數代表順時針轉，負數代表逆時針轉
* $y$ (溫差)： 上升流和下降流之間的溫度差異
* $z$ (垂直溫度的扭曲)： 雖然熱空氣往上飄，但對流會把這層規律打亂，$z$ 就是用來描述這種「混亂程度」或「偏離線性分佈的程度」


**參數代表**
* $\sigma$ (Sigma, 普朗特數)： 代表流體的黏滯性（黏稠度）。氣體通常較小，油較大
* $\rho$ (Rho, 雷利數)：這是最重要的參數！ 它代表**「加熱的強度」**。
  * 火開很小 ($\rho < 1$)：氣體不動，熱量靠傳導散去
  * 火開大一點 ($\rho > 1$)：開始穩定對流
  * 火開很大 ($\rho = 28$)：`混沌出現`
* $\beta$ (Beta, 幾何因子)： 與容器的寬高比有關

#### 假設
**漏水的水車**
* 水開很小：水漏得比裝得快（靜止，收斂到一點）
* 水開大一點：水車會開始穩定地往一個方向轉（週期性運動）
* 水開得很大 (混沌發生)：開始加速轉動，轉太快，水來不及裝滿桶子，另一邊的空桶子轉上來接水變重了，水車會突然減速，然後倒著轉，一直持續發生
### 混沌的誕生
```python
import numpy as np
import matplotlib.pyplot as plt

def lorenz_system(rho_val, num_steps=3000):
    # 標準參數
    sigma = 10
    beta = 8/3
    dt = 0.01
    
    xs, ys, zs = np.empty(num_steps), np.empty(num_steps), np.empty(num_steps)
    
    # 初始起點 (微小的擾動)
    xs[0], ys[0], zs[0] = (0.1, 1.0, 1.05)
    
    for i in range(num_steps - 1):
        x, y, z = xs[i], ys[i], zs[i]
        
        # 羅倫茲方程組 (核心演算法)
        dx = sigma * (y - x)
        dy = x * (rho_val - z) - y  # <--- rho 在這裡發揮作用
        dz = x * y - beta * z
        
        # 更新位置
        xs[i+1] = x + dx * dt
        ys[i+1] = y + dy * dt
        zs[i+1] = z + dz * dt
        
    return xs, ys, zs

# 設定三種不同的 Rho 值來觀察
rhos = [14, 28, 99]
titles = ["Stability (Rho=14)", "Chaos (Rho=28, Classic)", "High Complexity (Rho=99)"]
colors = ['green', 'blue', 'red']

fig = plt.figure(figsize=(15, 5))

for i in range(3):
    ax = fig.add_subplot(1, 3, i+1, projection='3d')
    x, y, z = lorenz_system(rhos[i])
    
    ax.plot(x, y, z, lw=0.6, c=colors[i])
    ax.set_title(titles[i])
    
    # 標記最後停在哪裡 (如果是穩定的，就會看到終點)
    ax.scatter(x[-1], y[-1], z[-1], c='black', s=20, label='End')
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")

plt.tight_layout()
plt.show()
```
* $\rho = 14$： 熱度不夠，對流會慢慢穩定下來（螺旋收斂到一個點）  
  `會看到線條繞了幾圈後，最後吸入並停在某個黑點上。這代表天氣很穩定，不管怎樣最後都會變成那個樣子`
* $\rho = 28$： 經典的羅倫茲蝴蝶（永遠繞圈圈）  
  `線條永遠不會停下來，形成完美的蝴蝶。這就是我們真實世界的「天氣」`
* $\rho = 99$： 超級加熱，蝴蝶變成了一團亂麻（更複雜的混沌）  
  `雖然還是在繞圈，但範圍變得更大、切換頻率更快，像是躁動的蝴蝶`  
**只要改變一個參數，整個系統的行為模式，可能會從「穩定」瞬間變成「混沌」**

全使用AI

[作業](https://github.com/Luo051227/_cm/tree/main/homework/%E6%9C%9F%E4%B8%AD)
[AI](https://gemini.google.com/share/277a8dea3197)
