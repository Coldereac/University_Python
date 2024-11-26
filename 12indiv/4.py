import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline
import sympy as sp

x = sp.symbols('x')
f_sym = (3 * sp.cbrt(6 * (x - 4) ** 2)) / (x ** 2 - 4 * x + 12)

df_sym = sp.diff(f_sym, x)
d2f_sym = sp.diff(df_sym, x)

f = sp.lambdify(x, f_sym, 'numpy')
df = sp.lambdify(x, df_sym, 'numpy')
d2f = sp.lambdify(x, d2f_sym, 'numpy')

x_points = np.linspace(5, 10, 6)
y_points = f(x_points)

natural_spline = CubicSpline(x_points, y_points, bc_type='natural')
clamped_spline = CubicSpline(x_points, y_points, bc_type='clamped')
first_derivatives_spline = CubicSpline(x_points, y_points,
                                       bc_type=((1, df(x_points[0])), (1, df(x_points[-1]))))
second_derivatives_spline = CubicSpline(x_points, y_points,
                                        bc_type=((2, d2f(x_points[0])), (2, d2f(x_points[-1]))))

x_fine = np.linspace(5, 10, 500)
y_true = f(x_fine)
y_natural = natural_spline(x_fine)
y_clamped = clamped_spline(x_fine)
y_first = first_derivatives_spline(x_fine)
y_second = second_derivatives_spline(x_fine)

fig = plt.figure(figsize=(12, 8))
fig.add_subplot(2, 1, 1)
plt.plot(x_fine, y_true, label='Входова функція f(x)', color='black', linewidth=1.5)
plt.scatter(x_points, y_points, color='red', label='Точки інтерполяції')
plt.plot(x_fine, y_natural, label='Природні умови', linestyle='--')
plt.plot(x_fine, y_clamped, label='Затиснені умови', linestyle='--')
plt.plot(x_fine, y_first, label='Задані похідні 1-го порядку', linestyle='--')
plt.plot(x_fine, y_second, label='Задані похідні 2-го порядку', linestyle='--')
plt.legend()
plt.grid()

fig.add_subplot(2, 1, 2)
plt.plot(x_fine, natural_spline(x_fine, 1), label='Природний сплайн (1-а похідна)', linestyle='--')
plt.plot(x_fine, clamped_spline(x_fine, 1), label='Затиснений сплайн (1-а похідна)', linestyle='--')
plt.plot(x_fine, first_derivatives_spline(x_fine, 1), label='1-а похідна зі значеннями', linestyle='--')
plt.plot(x_fine, second_derivatives_spline(x_fine, 1), label='2-а похідна зі значеннями', linestyle='--')
plt.plot(x_fine, natural_spline.antiderivative()(x_fine), label='Природний сплайн (первісна)', linestyle='--')
plt.plot(x_fine, clamped_spline.antiderivative()(x_fine), label='Затиснений сплайн (первісна)', linestyle='--')
plt.plot(x_fine, first_derivatives_spline.antiderivative()(x_fine), label='Первісна зі значеннями 1-ї похідної',
         linestyle='--')
plt.plot(x_fine, second_derivatives_spline.antiderivative()(x_fine), label='Первісна зі значеннями 2-ї похідної',
         linestyle='--')
plt.legend()
plt.grid()
plt.show()
