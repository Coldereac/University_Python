import numpy as np

x = np.array([-4, 2, 1])
A = np.array([[2, 1, 0], [3, 0, 4], [1, -1, 2]])
B = np.array([[0, 2, 3], [4, 1, 0], [2, -1, -2]])

y=2*(2*A+A.dot(B)).dot(x)
print('2*(2*A+A.B).x=',y)

z=(A.dot(B)-B.dot(A)).dot(x)
print('(A.B-B.A).x=',z)

k=np.linalg.inv(A).dot(x)
print('A^(-1).x=',k)

print('max(B)=',B.max())