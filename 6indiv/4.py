import numpy as np

A = np.array([[2, 3, -1, 5], [3, -1, 2, -7], [4, 1, -3, 6], [1, -2, 4, -7]])
b = np.array([25, -21, 21, -19])

x = np.linalg.solve(A, b)
print("Solve=", x)

Ainv = np.linalg.inv(A)
x = Ainv.dot(b)
print("Обернена матриці=", x)

det = np.linalg.det(A)
B = b[:, None]
A1 = np.hstack((B, A[:, 1:]))
d1 = np.linalg.det(A1)
A2 = np.hstack((A[:, 0:1], B, A[:, 2:4]))
d2 = np.linalg.det(A2)
A3 = np.hstack((A[:, 0:2], B, A[:, 3:4]))
d3 = np.linalg.det(A3)
A4 = np.hstack((A[:, 0:3], B))
d4 = np.linalg.det(A4)
print("Допоміжні матриці")
print('A1=\n', A1, '\nA2=\n', A2, '\nA3=\n', A3, '\nA4=\n', A4)
x = np.array([d1, d2, d3, d4]) / det
print("Метод Крамера=", x)
