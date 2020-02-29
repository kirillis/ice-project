import Cage as Cg
import Materials
import numpy as np
from matplotlib import pyplot as plt


# plot and show graphs
def plotter(number, result):
    for b in range(number):
        plt.plot(result[:, b])
    plt.show()


n = 5500
first = Cg.Cage(5, Materials.water)
second = Cg.Cage(-30, Materials.ice)
third = Cg.Cage(5.01, Materials.water)
# first = Cg.Cage(3, Materials.water)
# second = Cg.Cage(-50, Materials.ice)
# third = Cg.Cage(2, Materials.water)
cells_l = [first, second, third]
number_of_cells = np.zeros((n, len(cells_l)))
for i in range(n):
    number_of_cells[i][0] = first.temperature
    number_of_cells[i][1] = second.temperature
    number_of_cells[i][2] = third.temperature
    first.interaction(second)
    second.interaction(first)
    third.interaction(second, first)
    third.change_temp()
    first.change_temp()
    second.change_temp()

plotter(len(cells_l), number_of_cells)
print(first.material.name, second.material.name, third.material.name)
print(number_of_cells[-1])
