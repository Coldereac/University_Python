def elem(n):
    return (-2/5)**n

alph = 0.01
n = 1
sgn = -1
a = sgn * elem(n)
s = 0.0
while abs(a) > alph:
    s += a
    n += 1
    sgn = -sgn
    a = sgn * elem(n)
print('Сума ряду=', round(s, 3), sep='')
