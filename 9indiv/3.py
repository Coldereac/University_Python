import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, simplify, diff, lambdify, solve

x, y = symbols('x y')
F = 4 * x ** 2 + 24 * x * y + 11 * y ** 2 + 64 * x + 42 * y + 51
Fx = simplify(diff(F, x))
Fy = simplify(diff(F, y))
Fim = lambdify((x, y), F, 'numpy')
xl = np.linspace(-20, 20, 300)
yl = np.linspace(-20, 20, 300)
X, Y = np.meshgrid(xl, yl)
Z = Fim(X, Y)
fig, ax = plt.subplots(1, 1, figsize=(10, 10))
ax.contour(X, Y, Z, [0], colors='k', linewidths=2)

ax.axis('equal')

x_s = [5, 2.5, -0.5, -6, -7]
# Створюємо два масиви з 5 кольорами для дотичних і нормалей
colors = ["blue", "green", "purple", "orange", "red"]

for x0, col in zip(x_s, colors):
    yr = solve(F.subs(x, x0), y)
    y0 = yr[0]  # вібір першої точки, якщо розв’язків кілька
    print('y0=', y0)
    ax.scatter(x0, y0, s=100, c='r', linewidths=1)
    Fx0 = Fx.subs([(x, x0), (y, y0)])
    Fy0 = Fy.subs([(x, x0), (y, y0)])
    eqt = Fx0 * (x - x0) + Fy0 * (y - y0)
    eqn = Fx0 * (y - y0) - Fy0 * (x - x0)
    Eqt = lambdify((x, y), eqt, 'numpy')
    Eqn = lambdify((x, y), eqn, 'numpy')
    Zt = Eqt(X, Y)
    Zn = Eqn(X, Y)
    ax.contour(X, Y, Zt, [0], colors=col,
           linewidths=2, linestyles='dashed')
    ax.contour(X, Y, Zn, [0], colors=col,
           linewidths=2, linestyles='dashdot')

plt.show()
