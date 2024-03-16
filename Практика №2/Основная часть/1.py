numbers = [2, -3, -4, 5, 6, -7, -8]
print(f'Числа: {numbers}')

square_numbers = list(map(lambda n: n ** 2, numbers))
print(f'Квадрат чисел: {square_numbers}')

even_positive_numbers = list(filter(lambda n: n % 2 == 0 and n >= 0, numbers))
odd_negative_numbers = list(filter(lambda n: n % 2 == 1 and n < 0, numbers))
print(f'Четные положительные числа: {even_positive_numbers}')
print(f'Нечетные отрицательные числа: {odd_negative_numbers}')
