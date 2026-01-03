import numpy as np

def dft(fx, x, omega):
    dx = x[1] - x[0]
    F = []

    for i in range(len(omega)):
        w = omega[i]
        total = 0

        for k in range(len(x)):
            total = total + fx[k] * np.exp(-1j * w * x[k]) * dx

        F.append(total)

    return np.array(F)

def idft(Fw, omega, x):
    dw = omega[1] - omega[0]
    f = []

    for i in range(len(x)):
        xi = x[i]
        total = 0

        for k in range(len(omega)):
            total = total + Fw[k] * np.exp(1j * omega[k] * xi) * dw

        total = total / (2 * np.pi)
        f.append(total)

    return np.array(f)

L = 10
N = 1000

x = np.linspace(-L, L, N)
omega = np.linspace(-L, L, N)

f = np.exp(-x**2)

F = dft(f, x, omega)# 正
f_rec = idft(F, omega, x)# 逆

error = np.max(np.abs(f - f_rec.real))
print("最大誤差:", error)
