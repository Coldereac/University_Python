from math import sin, cos, pi
import turtle

t = turtle.Turtle()
N = 13
k = 4
R = 100
X = [R * cos(k * 2 * pi / N * i) for i in range(N + 1)]
Y = [R * sin(k * 2 * pi / N * i) for i in range(N + 1)]
t.penup()
t.goto(X[0], Y[0])
t.pendown()
t.color('red')
t.begin_fill()
for i in range(N + 1):
    t.goto(X[i], Y[i])
t.end_fill()
turtle.mainloop()
#https://pythonsandbox.com/code/pythonsandbox_u110331_QUTD1822873CCVJYnBXNhLxD_v1.py