import Cage as cg
import Materials
import numpy as np
from matplotlib import pyplot as plt


# plot and show graphs
def plotter(number, result):
    for b in range(number):
        plt.plot(result[:, b])
    plt.show()


n = 5000
first = cg.Mew(30, Materials.water) # 5 -40 10
second = cg.Mew(-10, Materials.ice)
third = cg.Mew(10, Materials.water)
# fourth = cg.Mew(-5, Materials.water)
cells_l = [first, second, third]
two_cells = np.zeros((n, 3))
for i in range(n):
    two_cells[i][0] = first.temperature
    two_cells[i][1] = second.temperature
    two_cells[i][2] = third.temperature
    # two_cells[i][3] = fourth.temperature
    cg.line_interaction(cells_l)

plotter(3, two_cells)
# print(two_cells)
print(first.material.name, second.material.name, third.material.name)
