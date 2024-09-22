from random import randint

L = set([randint(1, 9) for i in range(12)])
T = tuple(zip(L, L))
print(T)