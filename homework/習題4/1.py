import numpy as np

def roots_with_numpy(c):
    coeffs = np.array(c[::-1], dtype=np.complex128)
    return np.roots(coeffs)

import cmath

def durand_kerner(c, maxiter=200, tol=1e-12):
    n = len(c)-1
    if n == 0:
        return []

    roots = [0.4 + 0.9*cmath.exp(2j*cmath.pi*k/n) for k in range(n)]
    def p(z):
        val = 0
        for coeff in reversed(c):
            val = val*z + coeff
        return val
    for _ in range(maxiter):
        converged = True
        new_roots = roots.copy()
        for i in range(n):
            prod = 1
            for j in range(n):
                if i != j:
                    prod *= (roots[i] - roots[j])
            if prod == 0:
                converged = False
                continue
            delta = p(roots[i]) / prod
            new_roots[i] = roots[i] - delta
            if abs(new_roots[i] - roots[i]) > tol:
                converged = False
        roots = new_roots
        if converged:
            break

    def p_and_dp(z):
        val = 0
        d = 0
        for coeff in reversed(c):
            d = d*z + val
            val = val*z + coeff
        return val, d
    polished = []
    for r in roots:
        z = r
        for _ in range(20):
            pv, dv = p_and_dp(z)
            if dv == 0: break
            z_new = z - pv/dv
            if abs(z_new - z) < 1e-14:
                z = z_new; break
            z = z_new
        polished.append(z)
    return polished


#https://chatgpt.com/share/6924395f-4c6c-8012-a627-50cd7d7d8aae
