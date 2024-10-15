
import numpy as np
import matplotlib.pyplot as plt

def f(x):
        return (3 * np.cbrt(6 * (x - 4) ** 2)) / (x ** 2 - 4 * x + 12)



x = np.linspace(-5, 10, 100)
y = f(x)
x1 = np.linspace(-5, 10, 15)
y1 = f(x1)

Z=np.vstack((x1,y1)).transpose()
print(Z)

plt.plot(x, y, 'r', x1, y1, 'bo-', linewidth=2)
plt.axhline(color='black', lw=3)
plt.axvline(color='black', lw=3)
plt.show()
