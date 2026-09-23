import math
import numpy as np

def backward_difference_table(y):
    y = np.asarray(y, dtype=float)
    n = len(y)
    table = np.zeros((n, n), dtype=float)
    table[:, 0] = y
    for j in range(1, n):
        for i in range(j, n):
            table[i, j] = table[i, j-1] - table[i-1, j-1]
    return table

def newton_backward(x, y, value):
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    if len(x) != len(y) or len(x) < 2:
        raise ValueError("x and y must have the same length (at least 2).")
    h = x[1] - x[0]
    if np.isclose(h, 0) or not np.allclose(np.diff(x), h):
        raise ValueError("Newton's backward difference requires equally spaced x values.")
    table = backward_difference_table(y)
    p = (value - x[-1]) / h
    result = table[-1, 0]
    term = 1.0
    for k in range(1, len(x)):
        term *= (p + k - 1) / k
        result += term * table[-1, k]
    return result, table, h, p

def print_difference_table(x, table):
    n = len(x)
    headers = ["x", "y"] + [f"∇^{j}y" for j in range(1, n)]
    print("\nBackward Difference Table")
    print("-" * 80)
    print(" | ".join(f"{h:>12}" for h in headers))
    print("-" * 80)
    for i in range(n):
        row = [f"{x[i]:.4f}", f"{table[i,0]:.4f}"]
        for j in range(1, n):
            row.append(f"{table[i,j]:.4f}" if j <= i else "")
        print(" | ".join(f"{item:>12}" for item in row))
    print("-" * 80)
