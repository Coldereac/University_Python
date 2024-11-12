import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, simplify, solve, lambdify

plt.close('all')

x, y, z, t = symbols('x y z t')
F = 3 * x - 2 * y - 4 * z - 8

xt = t + 1
yt = t * 0 - 1
zt = -t + 1

ff = F.subs([(x, xt), (y, yt), (z, zt)])
eq = simplify(ff)
[t0] = solve(eq, t)
print('t0 =', t0)

x0 = xt.subs(t, t0)
y0 = yt.subs(t, t0)
z0 = zt.subs(t, t0)
print('Координати точки М = (%4.2f,%4.2f,%4.2f)' % (x0, y0, z0))

[zz] = solve(F, z)  # вираження z через x,y
fz = lambdify((x, y), zz, 'numpy')
x = np.linspace(-5, 5, 61)
y = np.linspace(-5, 5, 61)
X, Y = np.meshgrid(x, y)
Z = fz(X, Y)
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, rstride=10, cstride=10, color='c', alpha=0.5)
ax.azim, ax.elev = 15, 15  # азимут і кутова висота точки спостереження

Xt = lambdify(t, xt, 'numpy')
Yt = lambdify(t, yt, 'numpy')
Zt = lambdify(t, zt, 'numpy')
ti = np.linspace(-2, 2, 24)
Xl = Xt(ti)
Yl = Yt(ti)
Zl = Zt(ti)
ax.plot(Xl, Yl, Zl, linewidth=3, c='m')

ax.scatter(x0, y0, z0, s=50, c='r')
N = np.array([3, -2, -4])  # вектор нормалі до площини P
n = N / np.linalg.norm(N)  # одиничний вектор нормалі до площини P
ax.quiver([x0], [y0], [z0], *(3 * -n), linewidth=2, color='b',
          arrow_length_ratio=0.25)

aL = np.array([1, 0, -1])
aL1 = np.cross(np.cross(aL, N), N)
aL1 = aL1 / np.linalg.norm(aL1)
aL2 = np.cross(aL, N)
aL2 = aL2 / np.linalg.norm(aL2)
t_vals = np.linspace(-2, 2, 50)
L1_x = x0 + t_vals * aL1[0]
L1_y = y0 + t_vals * aL1[1]
L1_z = z0 + t_vals * aL1[2]

L2_x = x0 + t_vals * aL2[0]
L2_y = y0 + t_vals * aL2[1]
L2_z = z0 + t_vals * aL2[2]

ax.plot(L1_x, L1_y, L1_z, color="r")

ax.plot(L2_x, L2_y, L2_z, color="r")

ax.set_aspect('equal')
plt.show()
