import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

def x_param(t):
    return np.exp(t) * (np.cos(t) + np.sin(t))

def y_param(t):
    return np.exp(t) * (np.cos(t) - np.sin(t))

t_values = np.linspace(np.pi/2, np.pi, 7)
x_values = x_param(t_values)
y_values = y_param(t_values)
x_values[-1] = x_values[0]
y_values[-1] = y_values[0]

spline_x = CubicSpline(t_values, x_values, bc_type='periodic')
spline_y = CubicSpline(t_values, y_values, bc_type='periodic')

t_fine = np.linspace(np.pi/2, np.pi, 500)
x_fine = spline_x(t_fine)
y_fine = spline_y(t_fine)

t_input = np.linspace(np.pi/2, np.pi, 500)
x_input = x_param(t_input)
y_input = y_param(t_input)

plt.figure(figsize=(10, 8))
plt.scatter(x_values, y_values, color='black', s=40, label = "Точки")
plt.plot(x_input, y_input, label="Вхідна крива", color="red")
plt.plot(x_fine, y_fine, label="Інтерполяційний сплайн", color="blue")
plt.legend()
plt.grid()
plt.axis("equal")
plt.show()
