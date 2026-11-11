import numpy as np


#задание 1
hours = np.arange(0, 22, 3)
line = np.array([0.0, 0.25, 0.5, 0.75, 1.0])
zeros = np.zeros(6, dtype=int)
unknown_table = np.full((2,3), -1)
identity = np.eye(3, dtype=int)

print(hours)
print(hours.shape)
print(hours.ndim)
print(hours.size)
print(hours.dtype)

#задание 2
print(hours[2])
print(hours[-1])
print(hours[2:6])
print(hours[1::2])
print(hours[::-1])

#задание 3
temperatures = np.array([
    [12, 14, 13, 15],
    [11, 13, 16, 17],
    [10, 12, 15, 18],
])

print(temperatures.shape)
print(temperatures.ndim)
print(temperatures.size)
print(temperatures[1, 2])
print(temperatures[0])
print(temperatures[:, -1])
print(temperatures[:2, 1:])
print(temperatures[:2, 1:3])

#задание 4
matrix = np.arange(1, 26).reshape(5, 5)
print(matrix[:4])
print(matrix[:4].shape)
print(matrix[-2:])
print(matrix[-2:].shape)
print(matrix[:, :2])
print(matrix[:, :2].shape)
print(matrix[1:4, 2:5])
print(matrix[1:4, 2:5].shape)
print(matrix[-2:, -2:])
print(matrix[-2:, -2:].shape)

#задание 5
vector = np.array([10, 20, 30, 40, 50])
vector[1:4] = 0

small_matrix = np.arange(1, 10).reshape(3, 3)
small_matrix[0, :] = -1
small_matrix[1:, 1:] = 9

changed_hours = hours.copy()
changed_hours[2:5] = 99
print(changed_hours)
