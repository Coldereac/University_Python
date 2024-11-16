import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
from sympy import symbols, simplify, lambdify, exp, cos, sin, diff, sqrt
from sympy.physics.units import length

plt.close('all')

t0 = 0
t1 = 3 * np.pi / 2

t = symbols('t')

x = exp(t) * (cos(t) + sin(t))
y = exp(t) * (cos(t) - sin(t))

dx_dt = diff(x, t)
dy_dt = diff(y, t)

arc_integrand = sqrt(dx_dt ** 2 + dy_dt ** 2)
arc_length_func = lambdify(t, arc_integrand, 'numpy')
arc_length, _ = quad(arc_length_func, t0, t1)
print('Довжина = {:6.4f}'.format(arc_length))

t_vals = np.linspace(-5, 5, 500)
x_vals = lambdify(t, x, 'numpy')(t_vals)
y_vals = lambdify(t, y, 'numpy')(t_vals)

length_vals = np.linspace(t0, t1, 500)
length_vals_x = lambdify(t, x, 'numpy')(length_vals)
length_vals_y = lambdify(t, y, 'numpy')(length_vals)

plt.figure(figsize=(8, 6))

plt.plot(x_vals, y_vals, label="Curve")
plt.plot(length_vals_x, length_vals_y, 'r-', linewidth=6, label="Length")
plt.legend()
plt.grid()
plt.show()
