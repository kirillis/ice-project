import numpy as np


def matrix_reader(matrix_cells, num_iterations):
    """
    Функция реализует взаимодействие матрицы ячеек. Принимает на вход матрицу из объектов класса Cell. Возвращает 3-х
    мерный массив матриц температур в каждой итерации. Использует фуекцию list_cell_reader с закоменнченным кодом

    :param matrix_cells: матрица ячеек класса Cell
    :param num_iterations: кол-во итераций
    :return: 3-х мерный массив
    """

    m_shape = matrix_cells.shape  # Размер исходной матрицы

    if len(m_shape) == 2 and m_shape[0] != 1:  # нужно, так как взаимодейстиве строки отдельно строки не реализованно
        res = np.zeros((m_shape[0], m_shape[1], num_iterations))  # 3-х мерный пустой массив
        for k in range(num_iterations):  # кол-во итераций
            for i in range(m_shape[0]):  # Взаимодействие всех строк между собой и
                list_cell_reader(matrix_cells[i, :])  # запись строки температур в матрицу
            for j in range(m_shape[1]):  # Взаимодействие всех столбцов между собой и
                res[:, j, k] = list_cell_reader(matrix_cells[:, j])  # запись столбцов температур в матрицу
            for l in range(m_shape[0]):
                for f in range(m_shape[1]):
                    matrix_cells[l][f].change_temp()  # изменения температур всех ячеек
        return res


def list_cell_reader(cells):
    """
    Функция реализует взаимодействие строки ячеек между собой. Принимает на вход строку из ячеек. Не умеет менять
    температуру ячеек. Если убрать комментарии в коде, то сможет изменять температуры ячеек, но будет не пригода для
    матриц ячеек

    :param cells: Строка ячеек класса Cell
    :return: Матрицу температур ячеек после 1 итерации
    """

    n = len(cells)  # Длина ячеек
    result = np.zeros(n)  # Матрица температур, пока там нули
    # for k in range(iterations):
    for j in range(n):  # Заполняем температурами
        result[j] = cells[j].temperature
    for j in range(n):  # Взаимодействуем
        if j == 0:
            cells[j].interaction(cells[j + 1])  # Первая со второй
        elif j == n - 1:
            cells[j].interaction(cells[j - 1])  # Последняя с предпоследней
        else:
            cells[j].interaction(cells[j - 1], cells[j + 1])  # центральныое взаимодействие
        # for j in range(n):
        #     cells[j].change_temp()
    return result
