import cmath
import math

x = complex(input('x= '))
y = math.log(math.sin(1 / 2)) - ((1 / 24) * ((cmath.cos(12 * x) ** 2) / cmath.sin(24 * x)))
yr = complex(round(y.real, 4), round(y.imag, 4))
print('round y=', yr)
print('x+y=', x + y)
print('x*y=', x * y)
print('x/y=', x / y)

# x= 1+1j
