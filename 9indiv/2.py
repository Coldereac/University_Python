from cProfile import label

import numpy as np
import matplotlib.pyplot as plt
from numpy.ma.core import equal
from sympy import symbols, simplify, sqrt, diff, lambdify

x, y = symbols('x y')
fx = ((x ** 2 - 2) * sqrt(4 + x ** 2)) / (24 * x ** 3)
f1x = simplify(diff(fx, x))
f2x = simplify(diff(fx, x, x))
print("f'(x)=", f1x, '\nf"(x)=', f2x)

F0 = lambdify(x, fx, "numpy")
F1 = lambdify(x, f1x, "numpy")
F2 = lambdify(x, f2x, "numpy")

X = np.linspace(-5, 5, 100)
X = X[X != 0]
Y = F0(X)
X1 = np.linspace(-5, 5, 100)
X1 = X1[X1 != 0]
Y1 = F1(X1)
X2 = np.linspace(-5, 5, 100)
X2 = X2[X2 != 0]
Y2 = F2(X2)

fig, ax = plt.subplots(1, 1, figsize=(8, 8))
ax.plot(X, Y, 'b', linewidth=3, label='f(x)')
ax.plot(X1, Y1, 'r', linewidth=3, label="f'(x)")
ax.plot(X2, Y2, 'g', linewidth=3, label='f"(x)')
ax.grid(True)

x0 = 0.8
y0 = F0(x0)
ax.scatter(x0, y0, s=50, c='k')

k = F1(x0)
Xt = np.linspace(x0 - 1, x0 + 1, 100)
Yt = y0 + k * (Xt - x0)
ax.plot(Xt, Yt, '--k', linewidth=2, label='Дотична')

k_normal = -1 / F1(x0)
Xn = np.linspace(x0 - 1, x0, 100)
Yn = y0 + k_normal * (Xn - x0)
ax.plot(Xn, Yn, 'k', linewidth=2, label='Нормаль')

ax.legend(fontsize=12, loc='lower right')  # loc='upper center'
ax.axis('equal')

plt.xlim(-5, 5)
plt.ylim(-5, 5)

plt.show()
