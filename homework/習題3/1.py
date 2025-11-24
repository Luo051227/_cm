import cmath

def root3(a, b, c, d):
    if a == 0:
        raise ValueError
    
    p = (3*a*c - b*b) / (3*a*a)
    q = (2*b*b*b - 9*a*b*c + 27*a*a*d) / (27*a*a*a)

    delta = (q/2)**2 + (p/3)**3

    A = -q/2 + cmath.sqrt(delta)
    B = -q/2 - cmath.sqrt(delta)

    C = cmath.exp(cmath.log(A)/3) if A != 0 else 0
    D = cmath.exp(cmath.log(B)/3) if B != 0 else 0

    omega = complex(-1/2,  (3**0.5)/2)
    omega2 = complex(-1/2, -(3**0.5)/2)

    x1 = C + D
    x2 = C*omega + D*omega2
    x3 = C*omega2 + D*omega

    shift = b / (3*a)
    x1 -= shift
    x2 -= shift
    x3 -= shift

    return x1, x2, x3


r = root3(1, 0, -3, 1)
print(r)
