import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import *

plt.close('all')


def f(x):
    return np.arctan(np.sqrt(4 * x - 1))


x = np.linspace(1 / 4, 3, num=200)
y = f(x)
С = 0
yint = cumulative_trapezoid(y, x, initial=None) + С

x0 = 0.3  # Example point
i0 = np.where(x >= x0)[0][0]  # Index of x0
y0 = yint[i0]
dx = x[1] - x[0]
k = (yint[i0 + 1] - yint[i0]) / dx  # Slope of the tangent
x_tangent = np.linspace(x0 - 0.5, x0 + 0.5, 100)
y_tangent = y0 + k * (x_tangent - x0)

fig = plt.figure(figsize=(8, 8))
plt.plot(x_tangent, y_tangent, '--', label="Tangent at $x_0 = 2$", color="purple")
plt.scatter([x0], [y0], color="blue", label="$x_0=2$")
plt.plot(x[1:], yint, 'k-', linewidth=3, label='\u222Bf(x)dx')
plt.plot(x, y, 'r', linewidth=3, label='f(x)')
plt.legend(fontsize=12, loc='upper left')
plt.grid(True)
plt.show()
