import numpy as np
import scipy.interpolate as si
import matplotlib.pyplot as plt
from numpy.polynomial.polynomial import Polynomial

xp = np.array([1, 2, 5, 6, 8, 9, 11])
yp = np.array([3, 1, 3, 5, 2, 4, 2])
li = si.lagrange(xp, yp)
print("Поліном: \n", li)
right_answ = Polynomial([-1049/42, 26251/432, -293773/6480, 76127/5184, -3989/1728, 901/5184, -911/181440])
print("Правильна відповідь: ", right_answ)

plt.figure(figsize=(8, 8))
plt.subplot(2, 1, 1)
plt.scatter(xp, yp, label="Точки")
plt.plot(xp, yp, label="Ламана")

x_vals = np.linspace(0, 12, 100)
y_vals = li(x_vals)
plt.plot(x_vals, y_vals, label="Поліном")
plt.grid(True)
plt.ylim(-10, 10)
plt.legend()
plt.show()
