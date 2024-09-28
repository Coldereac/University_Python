import math

const1_1 = ((2+5/8) - (2/3) * (2 + 5/14)) / (((3 + 1/2) + 4.375) / (19 + 8/9))
const1_2 = math.log(math.sin(1 / 2)) - (1 / 24) * (math.cos(10 * math.sqrt(2)) ** 2) / (math.sin(24*math.exp(3)))

def func1(a, b):
    z1 = math.fabs((a - b) * math.sqrt((a + b) / (a - b)) + a - b)
    z2 = math.fabs((a - b) * (math.sqrt((a + b) / (a - b)) - 1))
    return z1 * z2

def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)