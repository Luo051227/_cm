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
通道容量 (Channel Capacity, $C$)：通道傳輸資訊的最大能力，定義為輸入與輸出之間的**互資訊（Mutual Information）**的最大值：$$C = \max_{P(X)} I(X; Y) \quad \text{(bits/channel use)}$$  
傳輸速率 (Rate, $R$)：
我們希望每使用一次通道傳輸 $R$ bits 的資訊。若碼長為 $n$，資訊位元為 $k$，則 $R = \frac{k}{n}$  
### 定理陳述
可達性（Achievability / Forward Theorem）：如果傳輸速率 $R < C$，那麼必然存在一種編碼方式，使得當碼長 $n \to \infty$ 時，解碼錯誤的機率 $P_e$ 趨近於 0。$$\lim_{n \to \infty} P_e = 0$$  
逆定理（Converse Theorem）：
如果傳輸速率 $R > C$，那麼無論採用何種編碼方式，錯誤機率 $P_e$ 都有一個非零的下界，無法做到可靠通訊。  

## 夏農-哈特利定理 (Shannon–Hartley Theorem)
