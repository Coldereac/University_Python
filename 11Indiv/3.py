import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import cumulative_trapezoid

plt.close('all')


def f(x):
    return np.arctan(np.sqrt(4 * x - 1))


x = np.linspace(1 / 4, 3, num=200)
y = f(x)
C = 0
yint = cumulative_trapezoid(y, x, initial=0) + C

x0 = 0.3
i0 = np.where(x >= x0)[0][0]
y0 = yint[i0]
dx = x[1] - x[0]

k1 = (yint[i0 + 1] - yint[i0]) / dx
k2 = f(x0)
print("k1 = ", k1, "k2 = ", k2)

# Побудова дотичних
x_tangent = np.linspace(x0 - 0.5, x0 + 0.5, 100)
y_tangent_k1 = y0 + k1 * (x_tangent - x0)  # Дотична для k1
y_tangent_k2 = y0 + k2 * (x_tangent - x0)  # Дотична для k2


fig, axes = plt.subplots( figsize=(8, 12))

# Графік для k1
axes.plot(x_tangent, y_tangent_k1, '--', color="purple")
axes.scatter([x0], [y0], color="blue")
axes.plot(x_tangent, y_tangent_k2, '--', color="green")
axes.plot(x, yint, 'k-', linewidth=3)
axes.plot(x, y, 'r', linewidth=3)
axes.set_title("k_1")
axes.grid(True)
plt.show()
