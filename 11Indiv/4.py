import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import dblquad, nquad
from sympy import symbols, sqrt, integrate

plt.close('all')

f = lambda y, x: 12 * x ** 2 * y ** 2 + 16 * x ** 3 * y ** 3
g = lambda x: -np.cbrt(x)
h = lambda x: x ** 3
I1 = dblquad(f, 0, 1, g, h)
print("I1 ={:5.3}".format(I1[0]))

xbnd = lambda: [0, 1]
ybnd = lambda x: [g(x), h(x)]
I2 = nquad(f, [ybnd, xbnd])
print("I2 ={:5.3}".format(I2[0]))

xh = np.linspace(-1, 2, num=100)
xg = np.linspace(0, 2, num=100)
yg = g(xg)
yh = h(xh)
fig = plt.figure(facecolor='white')
plt.plot(xg, yg, 'k-', xh, yh, 'b-', linewidth=4)

xr = np.linspace(0, 1, num=100)
yrg = g(xr)
yrh = h(xr)
plt.fill_between(xr, yrg, yrh, color='c')
plt.grid(True)

x_line = np.linspace(1, 1, 100)
x_line_y = np.linspace(-1, 1, 100)
plt.plot(x_line, x_line_y, 'k-', linewidth=4)

plt.show()
