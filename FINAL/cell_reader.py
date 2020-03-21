import matplotlib.pyplot as plt
import numpy as np


def max_temp(matrix_cells):
    sup = matrix_cells[0][0].temperature
    for i in range(matrix_cells.shape[0]):
        for k in range(matrix_cells.shape[1]):
            if sup < matrix_cells[i][k].temperature:
                sup = matrix_cells[i][k].temperature
            else:
                pass
    return sup


def matrix_reader(matrix_cells, num_iterations):
    """
    Функция реализует взаимодействие матрицы ячеек. Принимает на вход матрицу из объектов класса Cell. Возвращает 3-х
    мерный массив матриц температур в каждой итерации. Использует фуекцию list_cell_reader с закоменнченным кодом

    :param matrix_cells: матрица ячеек класса Cell
    :param num_iterations: кол-во итераций
    :return: 3-х мерный массив
    """

    m_shape = matrix_cells.shape  # Размер исходной матрицы
    to_plot = np.zeros(m_shape)
    for i in range(m_shape[0]):
        for j in range(m_shape[1]):
            to_plot[i][j] = matrix_cells[m_shape[0]-i-1][m_shape[1]-j-1].temperature
    fig, ax0 = plt.subplots(1, 1)
    im = ax0.pcolor(to_plot, vmax=20, vmin=-20, cmap='seismic')
    plt.axis('off')
    fig.colorbar(im, ax=ax0)
    name = 'C:\\Users\\bushanka\\Desktop\\Ans5(x100)\\pic' + str(0) + '.png'
    plt.savefig(name)
    plt.close()
    for k in range(num_iterations):  # кол-во итераций
        for i in range(m_shape[0]):  # Взаимодействие всех строк между собой и
            list_cell_reader(matrix_cells[i, :])
        for j in range(m_shape[1]):  # Взаимодействие всех столбцов между собой и
            list_cell_reader(matrix_cells[:, j])
        for l in range(m_shape[0]):
            for z in range(m_shape[1]):
                matrix_cells[l][z].change_temp()  # изменения температур всех ячеек
        if k % 100 == 0:
            print('{} %'.format(round(k / num_iterations * 100, 2)))
            name = 'C:\\Users\\bushanka\\Desktop\\Ans5(x100)\\pic' + str(k) + '.png'
            for m in range(m_shape[0]):
                for r in range(m_shape[1]):
                    to_plot[m][r] = matrix_cells[m_shape[0]-m-1][m_shape[1]-r-1].temperature
            fig, ax0 = plt.subplots(1, 1)
            im = ax0.pcolor(to_plot, vmax=20, vmin=-20, cmap='seismic')
            plt.axis('off')
            fig.colorbar(im, ax=ax0)
            plt.savefig(name)
            plt.close()


def list_cell_reader(cells):
    """
    Функция реализует взаимодействие строки ячеек между собой. Принимает на вход строку из ячеек. Не умеет менять
    температуру ячеек. Если убрать комментарии в коде, то сможет изменять температуры ячеек, но будет не пригода для
    матриц ячеек

    :param cells: Строка ячеек класса Cell
    :return: Матрицу температур ячеек после 1 итерации
    """

    n = len(cells)  # Длина ячеек
    # for k in range(iterations):
    for j in range(n):  # Взаимодействуем
        if j == 0:
            cells[j].interaction(cells[j + 1])  # Первая со второй
        elif j == n - 1:
            cells[j].interaction(cells[j - 1])  # Последняя с предпоследней
        else:
            cells[j].interaction(cells[j - 1], cells[j + 1])  # центральныое взаимодействие
        # for j in range(n):
        #     cells[j].change_temp()
