## 常係數齊次線性常微分方程（Constant Coefficient Homogeneous Linear ODE）
標準形式（以二階為例）如下： $$ay'' + by' + cy = 0$$  

 $a, b, c$ 是常數，$y$ 是 $x$ 的函數。所謂「齊次」是指等號右邊為 $0$（沒有外力項）  

1. 核心觀念：特徵方程式 (Characteristic Equation)
指數函數 $y = e^{rx}$ 是解答的原型
指因為指數函數的微分還是指數函數（$y' = re^{rx}$, $y'' = r^2 e^{rx}$）
將 $y = e^{rx}$ 代入方程 $ay'' + by' + cy = 0$，我們可以消去 $e^{rx}$（因為 $e^{rx} \neq 0$），得到一個代數方程式，稱為特徵方程式： $$ar^2 + br + c = 0$$  

