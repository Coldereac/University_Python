import math

s = 0
for n in range(1, 101):
    s = n**n / math.factorial(n)**2
print('Сума 100 членів= ', s, sep='')
