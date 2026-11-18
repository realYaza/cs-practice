import numpy as np


def make_hours():
    return np.arange(0, 22, 3).tolist()

def vector_report(values):
    values = np.array(values, dtype = float)
    return {'third': values[2], 'last': values[-1], 'middle': values[2:6].tolist(), 'every_second': values[::2].tolist(), 'reversed': values[::-1].tolist()}

def change_vector(values):
    values = np.array(values, dtype=float)
    values[1:4] = 99
    values[::2] = -1
    return values.tolist()

def cap_above(values, limit):
    values = np.array(values)
    values[values > limit] = limit #по условию в [] находим элементы, и заменяем их limit
    return values.tolist()

def celsius_to_fahrenheit(values):
    values = np.array(values, dtype= float)
    values = values * 9 / 5 + 32
    return values.tolist()

