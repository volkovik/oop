import numpy as np

array1 = np.random.randint(1, 10, size=(3, 3))
array2 = np.random.randint(1, 10, size=(3, 3))

print("Массив 1:")
print(array1)

print("Массив 2:")
print(array2)

multiplied_array = array1 * array2
print("Перемноженные элементы массивов:")
print(multiplied_array)

powered_array = np.power(array1, array2)
print("Массив 1, возведенный в степень, равную элементам массива 2:")
print(powered_array)
