import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

xmin = 0
xmax = 1
tmax = 2 * np.pi
nframes = 100

fig = plt.figure()
ax = plt.axes(xlim=(xmin, xmax), ylim=(-1, 1))
line, = ax.plot([], [], lw=3)
ttl = ax.text(3.0, 0.9, '')


def u(x, t):
    return 8 * x ** 3 * (x - 1) * np.sin(t)


def animate(i):
    x = np.linspace(xmin, xmax, 100)
    t = i * tmax / nframes  # момент часу по номеру i кадру
    y = u(x, t)
    ttl.set_text('t={:4.2f}'.format(t))
    line.set_data(x, y)
    return line, ttl


anim = FuncAnimation(fig, animate, frames=nframes, interval=80)
plt.show()
anim.save("7_3_anim.gif", writer='pillow')
