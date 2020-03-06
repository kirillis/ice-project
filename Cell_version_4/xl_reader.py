import Cell as Cg
import Materials
import numpy as np
from matplotlib import pyplot as plt
from cell_reader import matrix_reader as mr
from openpyxl import load_workbook


# plot and show graphs
def plotter(number, result):
    for b in range(number):
        plt.plot(result[:, b])
    plt.show()


def starter(name_xl, range_xl, iteration_number):
    wb = load_workbook(filename=name_xl)
    smth = wb['Sheet1']
    sheet_cells = np.array(smth[range_xl])
    temp_list = np.zeros_like(sheet_cells)
    for i in range(sheet_cells.shape[0]):
        for k in range(sheet_cells.shape[1]):
            temp_list[i][k] = sheet_cells[i][k].value
    cell_matrix = np.array([[None] * temp_list.shape[1]] * temp_list.shape[0])
    for i in range(sheet_cells.shape[0]):
        for k in range(sheet_cells.shape[1]):
            if temp_list[i][k] > 0:
                cell_matrix[i][k] = Cg.Cage(temp_list[i][k], Materials.water)
            elif temp_list[i][k] < 0:
                cell_matrix[i][k] = Cg.Cage(temp_list[i][k], Materials.ice)
    n = iteration_number
    answer = mr(cell_matrix, n)
    for i in range(sheet_cells.shape[0]):
        for k in range(sheet_cells.shape[1]):
            print(cell_matrix[i][k].material.name, end=' ')
        print('\n', end='')
    return answer, cell_matrix
