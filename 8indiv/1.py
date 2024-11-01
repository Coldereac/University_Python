import numpy as np
import matplotlib.pyplot as plt


def anglegrad(a, b):  # кут між векторами a,b в градусах
    sp = np.dot(a, b)
    la = np.linalg.norm(a)
    lb = np.linalg.norm(b)
    alph = np.arccos(sp / la / lb) * 180 / np.pi
    return alph


plt.close('all')
A = np.array([-1, -2, 1])
B = np.array([-4, 2, 10])
C = np.array([-8, -2, 2])
X, Y, Z = zip(A, B, C, A)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(X, Y, Z, linewidth=4, c='k')
ax.azim, ax.elev = 45, 20  # азимут і кутова висота точки спостереження

AB = B - A
AC = C - A
BC = C - B
LAB, LAC, LBC = map(np.linalg.norm, [AB, AC, BC])
sL = 'Довжини сторін: \tAB={:.4f}\tAC={:.4f}\tBC={:.4f}'.format(LAB, LAC, LBC)
print(sL)

aA, aB, aC = map(anglegrad, [AB, -AB, AC], [AC, BC, BC])
sA = 'Кути трикутника:\tA={:.2f} \tB={:.2f} \tC={:.2f}'.format(aA, aB, aC)
print(sA)

S = np.linalg.norm(np.cross(AB, AC)) / 2
print('Площа трикутника \tS=%6.5f' % S)

BD = -AB + AC * -(-AB.dot(AC) / np.linalg.norm(AC) ** 2)
D = BD + B
xAE, yAE, zAE = zip(B, D)
ax.plot(xAE, yAE, zAE, linewidth=4, c='g')
ax.scatter([D[0]], [D[1]], [D[2]], s=100, c='r')

plt.show()
