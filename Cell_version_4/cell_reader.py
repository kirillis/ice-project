import numpy as np


def matrix_reader(matrix_cells, num_iterations):
    m_shape = matrix_cells.shape
    if len(m_shape) == 2 and m_shape[0] != 1:
        res = np.zeros((m_shape[0], m_shape[1], num_iterations))
        for k in range(num_iterations):
            for i in range(m_shape[0]):
                res[i, :, k] = list_cell_reader(matrix_cells[i, :])
            for j in range(m_shape[1]):
                res[:, j, k] = list_cell_reader(matrix_cells[:, j])
            for l in range(m_shape[0]):
                for f in range(m_shape[1]):
                    matrix_cells[l][f].change_temp()
        return res


def list_cell_reader(cells):
    n = len(cells)
    result = np.zeros(n)
    # for k in range(iterations):
    for j in range(n):
        result[j] = cells[j].temperature
    for j in range(n):
        if j == 0:
            cells[j].interaction(cells[j + 1])
        elif j == n - 1:
            cells[j].interaction(cells[j - 1])
        else:
            cells[j].interaction(cells[j - 1], cells[j + 1])
        # for j in range(n):
        #     cells[j].change_temp()
    return result
