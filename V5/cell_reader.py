def max_temp(matrix_cells):
    sup = matrix_cells[0][0].temperature
    for i in range(matrix_cells.shape[0]):
        for k in range(matrix_cells.shape[1]):
            if sup < matrix_cells[i][k].temperature:
                sup = matrix_cells[i][k].temperature
            else:
                pass
    return sup


def matrix_reader(matrix_cells, num_iterations, file_name):
    """
    Функция реализует взаимодействие матрицы ячеек. Принимает на вход матрицу из объектов класса Cell. Возвращает 3-х
    мерный массив матриц температур в каждой итерации. Использует фуекцию list_cell_reader с закоменнченным кодом

    :param file_name:
    :param matrix_cells: матрица ячеек класса Cell
    :param num_iterations: кол-во итераций
    :return: 3-х мерный массив
    """

    m_shape = matrix_cells.shape  # Размер исходной матрицы
    if len(m_shape) == 2 and m_shape[0] != 1:  # нужно, так как взаимодейстиве строки отдельно строки не реализованно
        f = open(file_name, 'w')
        for i in range(len(m_shape)):
            f.write(str(m_shape[i]))
            f.write(' ')
        f.write(str(max_temp(matrix_cells)))
        f.write('\n')
        for l in range(m_shape[0]):
            for z in range(m_shape[1]):
                f.write(str(matrix_cells[l][z].temperature))
                f.write(' ')
        f.write('\n')
        for k in range(num_iterations):  # кол-во итераций
            if k % (num_iterations / 100) == 0:
                print('{} %'.format(round(k / num_iterations * 100, 2)))
            for i in range(m_shape[0]):  # Взаимодействие всех строк между собой и
                list_cell_reader(matrix_cells[i, :])
            for j in range(m_shape[1]):  # Взаимодействие всех столбцов между собой и
                list_cell_reader(matrix_cells[:, j])
            if k % 1 == 0:
                for l in range(m_shape[0]):
                    for z in range(m_shape[1]):
                        matrix_cells[l][z].change_temp()  # изменения температур всех ячеек
                        f.write(str(round(matrix_cells[l][z].temperature, 5)))
                        f.write(' ')
                f.write('\n')
        f.close()


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
