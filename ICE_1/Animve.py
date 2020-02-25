import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use('seaborn-pastel')

lines = Smth.two_cells

fig = plt.figure()
ax = plt.axes(xlim=(-50, 5000), ylim=(-150, 50))
line, = ax.plot([], [], lw=3)


def init():
    line.set_data([], [])
    return line,


xdata, ydata = [], []


def animate(i):
    t = i

    # x, y данные на графике
    x = t

    # добавление новых точек в список точек осей x, y
    xdata.append(x)
    ydata.append(lines[i][2])
    line.set_data(xdata, ydata)
    return line,


anim = FuncAnimation(fig, animate, init_func=init,
                     frames=5000, interval=0.001, blit=True)
plt.show(anim)
# anim.save('C:\\Users\\bushanka\\Desktopsine\\wave.gif')
