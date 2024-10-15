import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

plt.close('all')

def f(x):
    return np.piecewise(x,
                        [x <= 1, np.logical_and(x > 1, x <= 2), np.logical_and(x > 2, x <= 4), x > 4],
                        [lambda t: 3 - t, lambda t: 2, lambda t: 2 - (2 - t) ** 2 / 2, lambda t: 0])

def F1(x, y):
    return f(np.sqrt(x ** 2 + y ** 2))

def F2(x, y):
    return f(np.abs(x))

x = np.linspace(-4, 4, 81)
z = f(np.abs(x))

fig = plt.figure(figsize=(12, 8))

axUpLeft = fig.add_subplot(221)
axUpLeft.plot(x, z, lw=3, c='k')
axUpLeft.set_title('2D Plot')

X2, Y2 = np.meshgrid(x, x)
Z2 = F2(X2, Y2)
axRight = fig.add_subplot(222, projection='3d')
axRight.plot_wireframe(X2, Y2, Z2, rstride=8, cstride=2, color='b')
axRight.set_title('3D Wireframe Plot')


X1, Y1 = np.meshgrid(x, x)
Z1 = F1(X1, Y1)
axDown = fig.add_subplot(223, projection='3d')
axDown.plot_surface(X1, Y1, Z1, rstride=1, cstride=1)
axDown.set_title('3D Surface Plot')

plt.show()
