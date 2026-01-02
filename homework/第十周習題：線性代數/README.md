## 線性代數中的『線性』指的是什麼？為何要稱為『代數』

**線性 (Linear)**：指的是運算規則滿足「疊加性」與「齊次性」，在幾何上表現為「平直」且「過原點」

**代數 (Algebra)**：指的是將數值「符號化」與「抽象化」，探討運算結構（如向量空間）而非單純的數字計算

一個函數或變換 $L$ 若要被稱為「線性的」，必須嚴格滿足以下兩個條件：

1. **加法性 (Additivity / Superposition)**：兩個向量先相加再變換，等於先變換再相加。 $$L(u + v) = L(u) + L(v)$$

2. **齊次性 (Homogeneity / Scaling)**：向量放大 $c$ 倍後再變換，等於變換後再放大 $c$ 倍。 $$L(c \cdot u) = c \cdot L(u)$$

兩者合併，即為線性組合 (Linear Combination) 的保存： $$L(c_1 u + c_2 v) = c_1 L(u) + c_2 L(v)$$

直線方程式 $y = mx + b$ (若 $b \neq 0$) 在線性代數中不是線性變換，因為它不滿足 $L(0) = 0$（原點必須映射到原點）。這被稱為「仿射變換 (Affine Transformation)」

「代數」源於阿拉伯語 al-jabr，原意是還原與移項。

1. 抽象化：我們不再處理具體的 $1, 2, 3$，而是處理向量 $\mathbf{v}$、矩陣 $\mathbf{A}$
2. 結構研究：我們定義了一個集合（向量空間）以及在其上的運算規則（加法、數乘），並研究這些規則產生的性質（如秩 Rank、特徵值 Eigenvalue），這就是代數結構

## 數學中的『空間』是什麼？為何『向量空間』被稱為空間
「空間」＝「集合」＋「結構（規則）」

**『空間』 (Space)**

* 定義了「距離」，它就是度量空間
* 「鄰近性」，它就是拓樸空間
* 「加法與數乘」，它就是向量空間

比喻： 想像一個「空房間」（集合）
* 「如何測量兩人之間的距離」，這房間就變成了度量空間
* 「人可以在房間裡自由走動（加法）和伸縮（數乘），且不會撞牆掉出房間」，這房間就變成了向量空間

**為何稱為『向量空間』 (Vector Space)**'

之所以稱為「空間」，是因為它提供了一個活動場所，讓向量在其中進行線性運算（移動與縮放）後，永遠不會跑出去。這被稱為封閉性 (Closure)

一個集合 $V$ 是向量空間，必須滿足：

* 加法封閉性：你在空間裡隨便找兩個點 $\mathbf{u}, \mathbf{v}$，把它們加起來 $\mathbf{u}+\mathbf{v}$，結果一定還在這個空間裡
* 數乘封閉性：你在空間裡隨便找個點 $\mathbf{u}$，把它放大縮小 $c$ 倍 $c\mathbf{u}$，結果也一定還在這個空間裡

**子空間測試法**

給定 $\mathbb{R}^n$ 的一個子集 $W$：

1. 零向量存在： $\mathbf{0} \in W$。（空間必須包含原點，這是基準點）
2. 加法封閉：若 $\mathbf{u}, \mathbf{v} \in W$，則 $\mathbf{u} + \mathbf{v} \in W$
3. 數乘封閉：若 $\mathbf{u} \in W, c \in \mathbb{R}$，則 $c\mathbf{u} \in W$

## 矩陣和向量之間有何關係？矩陣代表的意義是什麼？

* **向量 (Vector) 是名詞**：它代表狀態、數據、或是空間中的一個點
* **矩陣 (Matrix) 是動詞**：它代表一種運動或變換（Transformation）

矩陣與向量的關係在於： **矩陣作用於向量，使向量發生移動、旋轉或變形**

**幾何意義：空間的變換 (Linear Transformation)** 

這是理解矩陣最直觀的方式。矩陣 $\mathbf{A}$ 是一個函數，它吃進一個向量 $\mathbf{x}$，吐出一個新向量 $\mathbf{y}$。 $$\mathbf{y} = f(\mathbf{x}) = \mathbf{A}\mathbf{x} $$這個「變換」包含了：旋轉 (Rotation)縮放 (Scaling)剪切 (Shear)投影 (Projection)

**代數意義：聯立方程式 (System of Equations)** 

矩陣是解方程組的工具。 
<img width="784" height="162" alt="image" src="https://github.com/user-attachments/assets/6ceca15f-c3be-4292-aa68-cc468dc1b139" />

矩陣 $\mathbf{A}$ 代表系統的結構，向量 $\mathbf{x}$ 是未知數，向量 $\mathbf{b}$ 是結果

**數據意義：張量 (Tensor)**

在電腦科學（如機器學習）中，矩陣是 2D 張量。 $$\mathbf{X} \in \mathbb{R}^{m \times n}$$ 例如：一張 $100 \times 100$ 的黑白照片，就是一個矩陣，每個數值代表像素亮度。這裡的矩陣不代表運動，只代表靜態資訊

## 如何用矩陣代表 2D / 3D 幾何學中的『平移，縮放，旋轉』操作？

要用矩陣統一表示這三種操作，我們必須引入一個關鍵概念：齊次座標 (Homogeneous Coordinates)

**為什麼需要「齊次座標」？**  

矩陣乘法 $\mathbf{A}\mathbf{x}$ 只能表示「線性變換」（變換後原點必須保持在原點）
* 縮放 (Scaling)：是線性的。 $S(\mathbf{0}) = \mathbf{0}$
* 旋轉 (Rotation)：是線性的。繞原點旋轉，原點不動
* 平移 (Translation)：不是線性的。 $T(\mathbf{x}) = \mathbf{x} + \mathbf{t}$，當 $\mathbf{x}=\mathbf{0}$ 時，結果是    $\mathbf{t}$，原點移動了

<img width="431" height="217" alt="image" src="https://github.com/user-attachments/assets/90308b1f-bca4-4d4e-9aac-18efbad2de80" />

### 2D
1. 平移 (Translation)

<img width="596" height="312" alt="image" src="https://github.com/user-attachments/assets/de76f637-c799-44e5-b1d8-528f31d54047" />


