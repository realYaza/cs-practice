import numpy as np


def reshape_rows(values, width):
    if len(values) % width != 0: # проверка по правилу лабы, мол если длина списка не делится на ширину нацело, то возвращаем []
        return []
    else:
        values = np.asarray(values)  # преобразовали список values в массив
        values = values.reshape(-1,width)  # пересобираем массив по заданным параметрам, width ширина каждой строки, -1 - кол-во строк,
        # которое питон сам посчитает
        return values.tolist()  # возвразаем массив, преображенный в список


def block(matrix, rows, columns):
    matrix = np.asarray(matrix, dtype=float) #преобразовываем в массив, dtype = какой тип данных
    return matrix[np.ix_(rows, columns)].tolist() #матрица[специальная индексация ix_(строки, столбцы)].

def column_means(matrix):
    if not matrix:
        return []
    else:
        matrix = np.asarray(matrix, dtype=float)
        return matrix.mean(axis=0).round(6).tolist() #встроенная ф-ия mean считает ср. знач, а параметр 0 даёт ей указание идти по столбцам
        #round округляет до 6 после запятой

def column_range(matrix, column):
    if not matrix:
        return 0.0
    else:
        matrix = np.asarray(matrix, dtype=float)
        col = matrix[:, column]  # срез matrix[строка(нашем случае вся, обозначаем :), столбец]
        return round(max(col) - min(col), 6)

print(column_range([[1, 2], [5, 7]], 1) )