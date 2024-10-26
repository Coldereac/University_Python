import numpy as np
import matplotlib.pyplot as plt

A = np.array([-2, -1, -1])
B = np.array([0, 3, 2])
C = np.array([3, 1, -4])

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
X, Y, Z = zip(A, B, C, A)
ax.plot(X, Y, Z)
ax.scatter(X, Y, Z, s=100, c='r')

d = np.array([B - A, C - A])
detx = np.linalg.det(d[:, 1:])
dety = np.linalg.det(d[:, [0, 2]])
detz = np.linalg.det(d[:, 0:-1])

x = np.linspace(-3, 4, 61)
y = np.linspace(-2, 4, 81)
X, Y = np.meshgrid(x, y)
Z = A[2] + 1 / detz * ((Y - A[1]) * dety - (X - A[0]) * detx)
ax.plot_surface(X, Y, Z, rstride=7, cstride=7, color='c', alpha=0.5)

a = np.linalg.norm(B - C)
b = np.linalg.norm(C - A)
c = np.linalg.norm(A - B)

# Semi-perimeter
s = (a + b + c) / 2

# Inradius (area divided by semi-perimeter)
R = np.sqrt((s - a) * (s - b) * (s - c) / s)

# Incenter coordinates
O = (a * A + b * B + c * C) / (a + b + c)

print("Координати центра кола:\t%8.2f%8.2f%8.2f" % (O[0], O[1], O[2]))
ax.scatter(*O, s=80, c='b')

t = np.linspace(0, 2 * np.pi, 100)

AB = B - A
AC = C - A

nv = np.cross(AB, AC)

basis_x = AB / np.linalg.norm(AB)
basis_y = np.cross(nv, basis_x)
basis_y /= np.linalg.norm(basis_y)

# Incircle points in plane coordinates
O_x = O + R * np.cos(t)[:, np.newaxis] * basis_x
O_y = R * np.sin(t)[:, np.newaxis] * basis_y
O_points = O_x + O_y

# Plot the incircle in the triangle plane
ax.plot(O_points[:, 0], O_points[:, 1], O_points[:, 2], color="purple", label="Incircle")
Nrm = nv / np.linalg.norm(nv)

ax.quiver(*O, *-Nrm, color='k', length=1.5, arrow_length_ratio=0.1, label="Normal vector")

max_range = np.ptp(np.array([A, B, C]), axis=0).max() / 2

mid_x = (A[0] + B[0] + C[0]) / 3

mid_y = (A[1] + B[1] + C[1]) / 3

mid_z = (A[2] + B[2] + C[2]) / 3

ax.set_xlim(mid_x - max_range, mid_x + max_range)

ax.set_ylim(mid_y - max_range, mid_y + max_range)

ax.set_zlim(mid_z - max_range, mid_z + max_range)

plt.show()
