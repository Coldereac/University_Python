import math
import sys

eps = 0.00001  # похибка обчислення кореня
dig = len(str(int(1 / eps)))  # кількість десяткових цифр


def F(x):
    y1 = math.cbrt(x) + 2 * math.cbrt(x ** 2)
    y2 = 3.0
    return y1 - y2



def half_div(fun, A, B, eps=0.00001):
    if A >= B:
        print('Потрібно, щоб було A<B', sep='')
        return None
    if fun(A) * fun(B) > 0:
        print('На відрізку [A,B] корінь повинен бути локалізований.', sep='')
        return None
    if fun(A) == 0: return A
    if fun(B) == 0: return B
    # початок алгоритму половинного ділення
    a = A
    fl = fun(a)
    b = B
    fr = fun(b)
    while b - a > eps:
        x = (a + b) / 2
        f = fun(x)
        if fl * f < 0:
            b = x
            fr = fun(b)
        elif fr * f < 0:
            a = x
            fl = fun(x)
        else:  # точно потрапили в корінь
            x = (a + b) / 2
            return x
    return x


A = float(input('A='))
B = float(input('B='))
x1 = half_div(F, A, B, eps)
if x1 is None:
    print("Розв'язок не знайдено.")
    sys.exit()
print('x1= ', round(x1, 5))
A = float(input('A='))
B = float(input('B='))
eps = 0.00001  # похибка обчислення кореня
dig = len(str(int(1 / eps)))
x2 = half_div(F, A, B, eps)
if x2 is None:
    print("Розв'язок не знайдено.")
    sys.exit()  # дострокове завершення програми
print('x2= ', round(x2, dig))
