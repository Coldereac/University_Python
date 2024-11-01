import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, simplify, diff, lambdify, sqrt, asin

x, y = symbols('x y')
zf = asin(sqrt(x**4+y**4)/sqrt(x**2+y**2))
zx = simplify(diff(zf, x))
zy = simplify(diff(zf, y))
print("dz/dx =", zx)
print("dz/dy =", zy)

x0 = 0.5
y0 = 0.5
z0 = zf.subs([(x, x0), (y, y0)])
print('Координати точки %5.2f %5.2f %5.2f' % (x0, y0, z0))

zx0 = zx.subs([(x, x0), (y, y0)])
zy0 = zy.subs([(x, x0), (y, y0)])
F = lambdify((x, y), zf, 'numpy')

xx = np.linspace(-1, 1, 50)
yy = np.linspace(-1, 1, 50)
X, Y = np.meshgrid(xx, yy)
Z = F(X, Y)
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(xlim=(-2, 2), ylim=(-2, 2), zlim=(-1, 3), projection='3d')
ax.plot_wireframe(X, Y, Z, rstride=1, cstride=1, linewidth=1)

P = np.array([x0, y0, z0], dtype='float')
ax.plot3D(*P, c='r', marker='o', ms=10)

n = np.array([zx0, zy0, -1], dtype='float')
ax.quiver(*P, *(-1.5 * n), linewidth=2, color='r',
          arrow_length_ratio=0.25)

t = np.linspace(-0.5, 1, 50)
xc = t
yc = 2 * t - 2 * x0 + y0  # для площини y=y0 буде yc=y0*np.ones(xc.shape)
zc = F(xc, yc)
ax.plot(xc, yc, zc, linewidth=3, c='k')

nc = np.array([1, 2, zx0 + zy0 * 2], dtype='float')
ax.quiver(*P, *nc * 0.5, linewidth=2, color='m', arrow_length_ratio=0.25)
ax.axis('equal')
plt.show()