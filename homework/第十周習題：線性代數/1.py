import numpy as np

def det(A):
    n = len(A)

    if n == 1:
        return A[0][0]

    if n == 2:
        return A[0][0]*A[1][1] -A[0][1]*A[1][0]

    result = 0
    for j in range(n):
        minor = [row[:j] + row[j+1:] for row in A[1:]]
        result += ((-1) ** j)* A[0][j]*det(minor)

    return result

A = [
    [1, 2, 3],
    [0, 4, 5],
    [1, 0, 6]
]

print(det(A))
