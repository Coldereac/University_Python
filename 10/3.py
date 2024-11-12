import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, lambdify, pprint, Function, Eq, exp, sin, dsolve, cos

x, y, C1, C2 = symbols('x y C1 C2')
u = Function('u')
eq = Eq(u(x).diff(x, x) - 4 * u(x).diff(x) + 8 * u(x), exp(x) * (-3 * sin(x) + 4 * cos(x)))
pprint(eq)
rez = dsolve(eq, u(x))
print("Загальний розв'язок u(x)=", rez.rhs)

y = rez.rhs.subs([(C1, 1), (C2, -1)])
print("Окремий розв'язок y(x)=", y)

F = lambdify(x, y, "numpy")
X = np.linspace(0, 40, 1000)
Y = F(X)
plt.figure(figsize=(8, 8))
plt.plot(X, Y, 'k', linewidth=3)
plt.grid(True)

plt.show()
