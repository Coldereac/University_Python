import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange, CubicSpline
from numpy.polynomial.polynomial import Polynomial

xp = np.array([0, 1, 2, 3, 4])
yp = np.array([4, 2, 1, 0, 1])

# 1. Інтерполяційна ламана
plt.figure(figsize=(12, 8))
plt.plot(xp, yp, 'o-', label="Інтерполяційна ламана", color="blue")

# 2. Інтерполяційний поліном Лагранжа
lagrange_poly = lagrange(xp, yp)
x_fine = np.linspace(min(xp), max(xp), 500)
y_lagrange = lagrange_poly(x_fine)
plt.plot(x_fine, y_lagrange, label="Поліном Лагранжа", color="orange", linewidth=4)

print("Рівняння інтерполяційного полінома Лагранжа:")
print(lagrange_poly)

# 3. Інтерполяційний кубічний сплайн
lagrange_derivative = np.polyder(lagrange_poly)  # Перша похідна полінома Лагранжа
bc_type = ((1, lagrange_derivative(xp[0])), (1, lagrange_derivative(xp[-1])))
spline = CubicSpline(xp, yp, bc_type=bc_type)
y_spline = spline(x_fine)

print("\nПоліноміальні сегменти кубічного сплайну:")
for i in range(len(spline.c[0])):
    segment = Polynomial(spline.c[:, i][::-1])
    print(f"Сегмент {i}: {segment}")

plt.plot(x_fine, y_spline, label="Кубічний сплайн", color="green")

#4. Апроксимуюча пряма
n = len(xp)
k = (n * np.sum(xp * yp) - np.sum(xp) * np.sum(yp)) / (n * np.sum(xp ** 2) - (np.sum(xp)) ** 2)
b = (np.sum(yp) - k * np.sum(xp)) / n

x_fine = np.linspace(min(xp), max(xp), 500)
y_line = k * x_fine + b

print("\nРівняння апроксимуючої прямої (метод найменших квадратів):")
print(f"y = {k:.3f}x + {b:.3f}")

plt.plot(x_fine, y_line, label="Апроксимуюча пряма", linestyle="--", color="red")

plt.scatter(xp, yp, color="black", label="Точки")
plt.legend()
plt.grid()
plt.show()
