import Test_Cage as Cg
import Materials
import numpy as np
from matplotlib import pyplot as plt


# plot and show graphs
def plotter(number, result):
    for b in range(number):
        plt.plot(result[:, b])
    plt.show()


n = 1600
first = Cg.Cage(20, Materials.water)
second = Cg.Cage(-10, Materials.ice)
third = Cg.Cage(10, Materials.water)
# fourth = cg.Mew(-5, Materials.water)
cells_l = [first, second, third]
number_of_cells = np.zeros((n, 3))
for i in range(n):
    number_of_cells[i][0] = first.temperature
    number_of_cells[i][1] = second.temperature
    number_of_cells[i][2] = third.temperature
    first.interaction(second)
    second.interaction(first, third)
    third.interaction(second)
    first.change_temp()
    second.change_temp()
    third.change_temp()

plotter(len(cells_l), number_of_cells)
print(first.material.name, second.material.name, third.material.name)
