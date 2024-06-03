import numpy as np

one_d_array = np.array([n for n in range(1, 6)])
two_d_array = np.array([[n for n in range(i, i + 3)] for i in range(1, 10, 3)])
three_d_array = np.array([[n for n in range(i, i + 2)] for i in range(1, 13, 2)])


print("Кол-во изм. 1-мерного массива:", one_d_array.ndim)
print("Кол-во изм. 2-мерного массива:", two_d_array.ndim)
print("Кол-во изм. 3-мерного массива:", three_d_array.ndim)

print("Форма 1-мерного массива:", one_d_array.shape)
print("Форма 2-мерного массива:", two_d_array.shape)
print("Форма 3-мерного массива:", three_d_array.shape)

print("Тип элементов 1-мерного массива:", one_d_array.dtype)
print("Тип элементов 2-мерного массива:", two_d_array.dtype)
print("Тип элементов 3-мерного массива:", three_d_array.dtype)
