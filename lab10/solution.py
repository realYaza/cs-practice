import numpy as np

def make_table(rows, columns):
    res = np.arange(0, rows*columns)
    res = np.reshape(res, rows, columns)
    return res.tolist()

def rectangle(matrix, row_start, row_stop, column_start, column_stop):
    matrix = np.asarray(matrix, dtype=float)
    return matrix[row_start:row_stop, column_start:column_stop].tolist()

def replace_rectangle(matrix, row_start, row_stop, column_start, column_stop, value):
    matrix = np.array(matrix, dtype=float)
    matrix[row_start:row_stop, column_start:column_stop] = value
    return matrix.tolist()

def matrix_vector_product(matrix, vector):
    matrix = np.asarray(matrix, dtype=float)
    vector = np.asarray(vector, dtype=float)
    return (matrix @ vector).tolist()

def matrix_multiply(left, right):
    left = np.asarray(left, dtype=float)
    right = np.asarray(right, dtype=float)
    return (left @ right).tolist()

def transpose_matrix(matrix):
    matrix = np.asarray(matrix, dtype=float)
    return matrix.T.tolist()

def solve_system(matrix, vector):
    matrix = np.asarray(matrix, dtype=float)
    vector = np.asarray(vector, dtype=float)
    x = np.linalg.solve(matrix, vector)
    return x.round(6).tolist()
