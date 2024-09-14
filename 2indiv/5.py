from collections.abc import MutableSet
from math import trunc
from random import randint

N = 12
L = [randint(-10, 10) for i in range(N)]
print(L)
k = False
for i in range(len(L) - 2):
    if L[i] == L[i + 1]:
        k = True
        break
print('Сусідні однакові числа ', k)
