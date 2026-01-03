import numpy as np

def dft(fx, x, omega):
    dx = x[1] - x[0]
    F = []

    for w in omega:
        Fw = np.sum(fx * np.exp(-1j * w * x)) * dx
        F.append(Fw)

    return np.array(F)

def idft(Fw, omega, x):
    dw = omega[1] - omega[0]
    f = []

    for xi in x:
        fx = np.sum(Fw * np.exp(1j * omega * xi)) * dw / (2 * np.pi)
        f.append(fx)

    return np.array(f)

L = 10
N = 1000

x = np.linspace(-L, L, N)
omega = np.linspace(-L, L, N)

f = np.exp(-x**2)

F = dft(f, x, omega)

f_rec = idft(F, omega, x)

error = np.max(np.abs(f - f_rec.real))
print("最大誤差:", error)

