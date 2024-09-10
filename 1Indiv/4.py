import math

for x in range(10):
    y = 3 * ((6 * (x - 4) ** 2) ** (1 / 3)) / (x ** 2 - 4 * x + 12)
    print('x=', x, '\ty=', round(y, 5))
