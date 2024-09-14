import math
from turtle import *

reset()

kx = 20  # x-axis scale
ky = 20  # y-axis scale


def f(x):
    return 6 * math.exp(x - 1) - 3 * x - x ** 3


color('red')
width(2)

x_min = -3
x_max = 4
y_max = 10

up()
goto(kx * x_min, 0)
down()
goto(kx * x_max, 0)

up()
goto(0, ky * y_max)
down()
goto(0, -ky * y_max)

color('blue')
width(3)

x = x_min
y = f(x)
dx = math.pi / 25

# Move to the initial point of the curve
up()
goto(kx * x, ky * y)
down()

# Draw the curve
while x <= x_max:
    y = f(x)
    goto(kx * x, ky * y)
    x += dx

done()
