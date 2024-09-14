import math
import numpy as np
import matplotlib.pyplot as plt


def f1(x):
    return 3 * ((6 * (x - 4) ** 2) ** (1 / 3)) / (x ** 2 - 4 * x + 12)


def f2(x):
    return 6 * math.exp(x - 1) - 3 * x - x ** 3


def f3(x):
    return (f1(x) + f2(x)) / 2


a = -2
b = 4


def f(x):
    if x < a:
        return f1(x) - f1(a)
    elif x <= b:
        return f2(x) - f2(a)
    else:
        return f3(x) - f3(b) + f2(b) - f2(a)


xl = -5  # лівий кінець відрізка зміни x
xe = 7 # правий кінець відрізка зміни x
for i in range(11):
    x = xl + i * (xe - xl) / 10
    print('\t', round(x, 4), '\t', round(f(x), 4))

x = np.linspace(xl, xe, 100)
y = np.array([f(t) for t in x])
plt.plot(x, y)
plt.show()
