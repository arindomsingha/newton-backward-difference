import numpy as np
import matplotlib.pyplot as plt
from newton_backward import newton_backward, print_difference_table

x = np.array([100, 150, 200, 250, 300, 350, 400], dtype=float)
y = np.array([10.63, 13.03, 15.04, 16.81, 18.42, 19.90, 21.27], dtype=float)
target = 410

result, table, h, p = newton_backward(x, y, target)

print("QUESTION 1")
print("Given data:")
print("x =", x)
print("y =", y)
print_difference_table(x, table)
print(f"h = {h}")
print(f"p = (x - xn) / h = ({target} - {x[-1]}) / {h} = {p:.4f}")
print(f"\nEstimated y({target}) = {result:.6f}")

grid = np.linspace(x[0], x[-1], 300)
curve = np.array([newton_backward(x, y, v)[0] for v in grid])
plt.figure(figsize=(8, 5))
plt.plot(grid, curve, label="Newton backward interpolation")
plt.scatter(x, y, label="Given data")
plt.scatter([target], [result], marker="x", s=80, label=f"Estimated value = {result:.4f}")
plt.xlabel("x"); plt.ylabel("y")
plt.title("Question 1: Newton's Backward Difference")
plt.grid(True, alpha=0.3); plt.legend(); plt.tight_layout()
plt.savefig("images/question1_plot.png", dpi=160)
plt.show()
