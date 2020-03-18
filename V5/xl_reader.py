import Cell as Cg
import Materials
import numpy as np
from cell_reader import matrix_reader as mr
from openpyxl import load_workbook


def starter(name_xl, range_xl, iteration_number, file_name):
    """
    Фунуция инициализации модели. Считывает имя файла Exel 2007-2019, в котором записаны температуры ячеек,
    диапазон данных в таблице и кол-во итераций. Возвращает матрицу cell_matrix с ячейками класса Cell, а так же
    3-х мерный массив, в котором записаны матрицы температур на каждой итерации
    """

    wb = load_workbook(filename=name_xl)
    wb_name = wb['Sheet1']

    sheet_cells = np.array(wb_name[range_xl])  # Чтение файла Exel
    temp_list = np.zeros_like(sheet_cells)  # Матрица температур

    for i in range(sheet_cells.shape[0]):
        for k in range(sheet_cells.shape[1]):
            temp_list[i][k] = sheet_cells[i][k].value  # Запись значений температур ячеек в матрицу

    cell_matrix = np.array([[None] * temp_list.shape[1]] * temp_list.shape[0])  # пустая матрица, в ней будут Cell
    # ____________ Заполнения матрицы ячейками, в зависимости от знака температур ______________________
    for i in range(sheet_cells.shape[0]):
        for k in range(sheet_cells.shape[1]):
            if temp_list[i][k] > 0:
                cell_matrix[i][k] = Cg.Cage(temp_list[i][k], Materials.water)
            elif temp_list[i][k] < 0 and temp_list[i][k] != -50:
                cell_matrix[i][k] = Cg.Cage(temp_list[i][k], Materials.ice)
            elif temp_list[i][k] == -50:
                cell_matrix[i][k] = Cg.Cage(temp_list[i][k], Materials.air)
    # __________________________________________________________________________________________________
    mr(cell_matrix, iteration_number, file_name)  # Рассчет модели, запись в файл
    # ___________ Вывод значений материала каждой ячейки после рассчета ________________________________
    for i in range(sheet_cells.shape[0]):
        for k in range(sheet_cells.shape[1]):
            if cell_matrix[i][k].material.name is "Ice":
                print('I', end=' ')
            elif cell_matrix[i][k].material.name is 'Air':
                print('A', end=' ')
            else:
                print('W', end=' ')
        print('\n', end='')
    for i in range(sheet_cells.shape[0]):
        for k in range(sheet_cells.shape[1]):
            print(cell_matrix[i][k].temperature, end=' ')
        print('\n')
    # __________________________________________________________________________________________________
    return 'Success'
