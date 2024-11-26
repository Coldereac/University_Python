import numpy as np
import matplotlib.pyplot as plt

xp = np.array([0, 1, 2, 3, 4, 5, 6])
yp = np.array([4, 2, 1, 0, 1, 0, 4])

# Обчислення коефіцієнтів k і b
# методом найменших квадратів
n = len(xp)
k = (n * np.sum(xp * yp) - np.sum(xp) * np.sum(yp)) / (n * np.sum(xp ** 2) - (np.sum(xp)) ** 2)
b = (np.sum(yp) - k * np.sum(xp)) / n


def linear_func(x):
    return k * x + b

print(f"Рівняння знайденої прямої: y = {k:.2f}x + {b:.2f}")

x_line = np.linspace(min(xp) - 1, max(xp) + 1, 100)
y_line = linear_func(x_line)

plt.figure(figsize=(10, 6))
plt.scatter(xp, yp, color='red', label='Точки')
plt.plot(x_line, y_line, color='blue', label=f'Пряма: y = {k:.2f}x + {b:.2f}')
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.legend()
plt.grid()
plt.show()

