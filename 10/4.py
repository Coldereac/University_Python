import matplotlib.pyplot as plt
from matplotlib.figure import figaspect
from sympy import symbols, integrate, And, solve, plot_implicit

x, y = symbols('x y')
Fun = x ** 2 + y ** 2 / 9
x0 = -1
x1 = 1
y0 = 0
sols = solve(Fun - 1, y)
print(sols)

y1 = sols[1]

mu = 35 * x ** 4 * y ** 3
m = integrate(mu, (y, y0, y1), (x, x0, x1))
print('Маса платівки=', m)

plot_implicit(And(Fun <= 1, y >= 0), depth=2)
fig = plt.gcf()
ax = fig.gca()
ax.axis('equal')
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 3)
