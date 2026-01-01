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

