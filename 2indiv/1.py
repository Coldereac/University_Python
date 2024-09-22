# %% Використання циклу for ... in range
import math
from math import sin, exp

print('\tВикористання циклу for ... in range')
print('\tx', '\t\t y', '\t\t y**2', '\texp(-y)')
print('\t-------------------------------')
for i in range(11):
    x = 1 + 0.1 * i
    y = 6 * math.exp(x - 1) - 3 * x - x ** 3
    print('\t', round(x, 2), '\t', round(y, 3), '\t',
          round(y ** 2, 3), '\t', round(exp(-y), 3))
# %% Використання циклу for ... in list
from math import sin, exp

print('\tВикористання циклу for ... in list')
print('\tx', '\t\t y', '\t\t y**2', '\texp(-y)')
print('\t-------------------------------')
for x in [1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0]:
    y = 6 * math.exp(x - 1) - 3 * x - x ** 3
    print('\t', round(x, 2), '\t', round(y, 3), '\t',
      round(y ** 2, 3), '\t', round(exp(-y), 3))
# %% Використання циклу while
from math import sin, exp

print('\tВикористання циклу while')
x = 1.0
print('\tx', '\t\t y', '\t\t y**2', '\texp(-y)')
print('\t-------------------------------')
while x < 2.1:
    y = 6 * math.exp(x - 1) - 3 * x - x ** 3
    print(' ', round(x, 2), '\t', round(y, 3), '\t',
          round(y ** 2, 3), '\t', round(exp(-y), 3))
    x = x + 0.1
