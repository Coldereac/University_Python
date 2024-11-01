import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, lambdify, solve, limit, oo
import warnings

x, y = symbols('x y')
f = (4 * x ** 3 - 3 * x) / (4 * x ** 2 - 1)

a = limit(f / x, x, oo)
b = limit(f - a * x, x, oo)
fasm = a * x + b
print('Рівняння косої асимптоти: y =', fasm)

sols = solve(4 * x ** 2 - 1, x)
print('Корені знаменника:', sols)

# Побудова графіка
F = lambdify(x, f, "numpy")
X = np.linspace(-3, 7, 101)
warnings.filterwarnings('ignore')  # не виводити попередження
Y = F(X)
plt.plot(X, Y, 'b', linewidth=3)

Fasm = lambdify(x, fasm, "numpy")
Yasm = Fasm(X)
plt.plot(X, Yasm, linestyle='--', color='r')

for va in sols:
    plt.axvline(va, color='r', linestyle='--')

plt.axhline(color='k')
plt.axvline(color='k')
plt.grid(True)
plt.show()
