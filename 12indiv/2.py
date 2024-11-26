import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange

def f(x):
    return np.sin(x) * np.log(x**2 + 1) * 2**(-x)

x_nodes = np.linspace(-1, 1, 5)
y_nodes = f(x_nodes)

polynomial = lagrange(x_nodes, y_nodes)
print("Поліном:")
print(polynomial)

x = np.linspace(-2, 2, 500)
y = f(x)
y_poly = polynomial(x)

plt.figure(figsize=(10, 6))
plt.plot(x, y, label='f(x)', color='blue')
plt.plot(x, y_poly, label='Поліном', color='orange', linestyle='--')
plt.scatter(x_nodes, y_nodes, color='red', label='Вузли інтерполяції')
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.legend()
plt.grid()
plt.show()

