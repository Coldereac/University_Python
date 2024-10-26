import numpy as np
import matplotlib.pyplot as plt

plt.close('all')
A = np.array([2, -1, 2])
B = np.array([1, 2, -1])
C = np.array([3, 2, 1])
D = np.array([-4, 2, 5])
X, Y, Z = zip(A, B, C, A, D, B, C, D)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(X, Y, Z, linewidth=4, c='k')

AB = B - A
AC = C - A
AD = D - A

mp = np.array([AB, AC, AD])
V = np.abs(np.linalg.det(mp)) / 6
print("Об’єм тетраедра \tV=%8.5f" % V)

Nrm = np.cross(AB, AC)
S = np.linalg.norm(Nrm) / 2
print("Площа трикутника ABC\tS=%8.5f" % S)

# Вычисляем координаты точки пересечения медиан E
E = (A + B + C) / 3
print("Координати точки E:\t%8.2f %8.2f %8.2f" % (E[0], E[1], E[2]))
ax.scatter(*E, s=100, c='r')

xAE, yAE, zAE = zip(A, E)
ax.plot(xAE, yAE, zAE, linewidth=4, c='r')

xDE, yDE, zDE = zip(D, E)
ax.plot(xDE, yDE, zDE, linewidth=4, c='r')

plt.show()
