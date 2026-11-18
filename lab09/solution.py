import numpy as np


def make_hours():
    return np.arange(0, 21, 3).tolist()

def vector_report(values):
    values = np.array(values, dtype = float)
    return {'third': values[2], 'last': values[-1], 'middle': values[2:6], 'every_second': values[::2], 'reversed': values[::-1]}

def change_vector(values):
    values = np.array(values)
    values[1:4] = 99
    values[1::2] = -1
    return values.tolist()
