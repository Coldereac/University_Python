import cmath
import math


def func1(x):
    return math.cbrt(x) + 2 * math.cbrt(x ** 2) - 3

def func2(x):
    return 3 * ((6 * (x - 4) ** 2) ** (1 / 3)) / (x ** 2 - 4 * x + 12)

def func3(x):
    return math.log(math.sin(1 / 2)) - ((1 / 24) * ((cmath.cos(12 * x) ** 2) / cmath.sin(24 * x)))

def func4(x):
    return 6 * math.exp(x - 1) - 3 * x - x ** 3

def func5(x):
    return 3 * ((6 * (x - 4) ** 2) ** (1 / 3)) / (x ** 2 - 4 * x + 12)

def func6(x):
    return 6 * math.exp(x - 1) - 3 * x - x ** 3

def func7(x):
    return (func5(x) + func6(x)) / 2