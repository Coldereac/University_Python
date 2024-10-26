import numpy as np
import matplotlib.pyplot as plt

plt.close('all')
A = np.array([-1, -2, 1])
B = np.array([-4, -2, 5])
C = np.array([-8, -2, 2])
AB = B - A
AC = C - A
D = A + (AB + AC)
print('Координати точки D:\t%8.2f %8.2f %8.2f' % (D[0], D[1], D[2]))

nrm = np.cross(AB, AC)
S = np.linalg.norm(nrm)
print('Площа паралелограма \tS=%8.5f' % S)

E = (D + B) / 2

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
X, Y, Z = zip(A, B, E, D, C, A)
ax.plot(X, Y, Z, linewidth=4, c='k')
ax.azim, ax.elev = 60, 15  # азимут і кутова висота точки спостереження
ax.scatter(X, Y, Z, s=100, c='r')
xAE, yAE, zAE = zip(A, E)
ax.plot(xAE, yAE, zAE, linewidth=4, c='k')

t = np.linspace(0, 1, 9)
p, q = np.meshgrid(t, t)
X = A[0] + p * AB[0] + q * AC[0]
Y = A[1] + p * AB[1] + q * AC[1]
Z = A[2] + p * AB[2] + q * AC[2]
ax.plot_surface(X, Y, Z, rstride=1, cstride=2, color='c', alpha=0.3)

ne = nrm / np.linalg.norm(nrm)  # одиничний вектор нормалі
ax.quiver(*E, *(1 * ne), linewidth=2, color='b', arrow_length_ratio=0.25)

plt.show()
