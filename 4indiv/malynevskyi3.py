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


def func(L: list, filename: str):
    T = tuple(zip(L, L))
    file = open(filename, 'w')
    file.write(str(T))
    file.close()
