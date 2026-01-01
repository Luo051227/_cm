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

## 夏農-哈特利定理 (Shannon–Hartley Theorem)
