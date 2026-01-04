import numpy as np
from collections import defaultdict

def solve_ode_general(coefficients, tol=1e-6):
    roots = np.roots(coefficients)

    groups = []
    for r in roots:
        placed = False
        for g in groups:
            if abs(r - g[0]) < tol:
                g.append(r)
                placed = True
                break
        if not placed:
            groups.append([r])

    terms = []
    C = 1

    for g in groups:
        r = np.mean(g) # 代表根
        m = len(g)  # 重根階數

        if abs(r.imag) < tol:
            # 實根
            lam = r.real
            for k in range(m):
                if k == 0:
                    terms.append(f"C_{C}e^({lam:.1f}x)")
                else:
                    terms.append(f"C_{C}x^{k}e^({lam:.1f}x)")
                C += 1
        else:
            # 複數共軛根
            alpha = r.real
            beta = abs(r.imag)

            for k in range(m):
                if k == 0:
                    terms.append(f"C_{C}e^({alpha:.1f}x)cos({beta:.1f}x)")
                    C += 1
                    terms.append(f"C_{C}e^({alpha:.1f}x)sin({beta:.1f}x)")
                    C += 1
                else:
                    terms.append(f"C_{C}x^{k}e^({alpha:.1f}x)cos({beta:.1f}x)")
                    C += 1
                    terms.append(f"C_{C}x^{k}e^({alpha:.1f}x)sin({beta:.1f}x)")
                    C += 1

    return "y(x) = " + " + ".join(terms)

