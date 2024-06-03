import numpy as np

zeros_array = np.zeros((3, 4))
print("Массив, состоящий из нулей:")
print(zeros_array)

ones_array = np.ones((3, 4))
print("Массив, состоящий из единиц:")
print(ones_array)

user_values = [[n for n in range(i, i + 4)] for i in range(1, 13, 4)]
custom_array = np.array(user_values)
print("Массив, состоящий из значений, указанных пользователем:")
print(custom_array)
