def get_table_of_multiply(number):
    return [f'{number} * {n} = {n * number}' for n in range(1, 11)]


user_number = int(input('Введите число: '))
print('\n'.join(get_table_of_multiply(user_number)))
