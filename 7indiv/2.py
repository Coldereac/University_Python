import numpy as np
import matplotlib.pyplot as plt


def f1(x):
    return np.sin(x)


def f2(x):
    return np.exp(-(x ** 2))


def f3(x):
    return 1 / (1 + x ** 2)


a = -np.pi
b = np.pi


def f(x):
    # if(x < a):
    #     return f1(x) - f1(a)
    # elif(x <= b):
    #     return f2(x) - f2(a)
    # else:
    #     return f3(x) - f3(b) + f2(b) - f2(a)

    return np.piecewise(x, [x < a, np.logical_and(x > a, x <= b), x > b],
                        [lambda t: f1(t) - f1(a), lambda t: f2(t) - f2(a), lambda t: f3(t) - f3(b) + f2(b) - f2(a)])


def F(x, y):
    return x ** 2 + 2 * x * y + 10 * x - 10 * y + 1

x = np.linspace(-10, 10, 100)
y = f(x)
fig, axes = plt.subplots(1, 2)
fig.set_size_inches(7, 3)
axes[0].plot(x, y, lw=3, c='k')
axes[0].grid(True)
axes[0].set_xlabel('x')
axes[0].set_ylabel('y')
t = np.linspace(-15, 15, 100)
X, Y = np.meshgrid(t, t)
axes[1].set_xlim(-15,10)
axes[1].set_ylim(-3,15)
axes[1].contour(X,Y, F(X,Y),[0],linewidths=3,colors='red')
axes[1].set_xlabel('x')
axes[1].set_ylabel('y')
axes[1].grid(True)
plt.show()
