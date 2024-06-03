import numpy as np

array = np.array(list(range(1, 51, 10)))
print("Исходный массив:")
print(array)

array_plus_3 = array + 3
print("Массив после прибавления 3 к каждому элементу:")
print(array_plus_3)

array_minus_5 = array_plus_3 - 5
print("Массив после вычитания 5 из каждого элемента:")
print(array_minus_5)
