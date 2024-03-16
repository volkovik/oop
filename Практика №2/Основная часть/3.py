length_of_list = int(input('Введите размер списка: '))
user_list = []
print('Вводите каждый элемент с новой строки.')
for _ in range(length_of_list):
    user_list.append(int(input()))

print(f'Ваш список: {user_list}')

sorted_list = sorted(user_list)
print(f'По возрастанию: {sorted_list}')

reversed_sorted_list = sorted(user_list, reverse=True)
print(f'По убыванию: {reversed_sorted_list}')

max_of_user_list = max(user_list)
print(f'Максимальный элемент: {max_of_user_list}')

min_of_user_list = min(user_list)
print(f'Минимальный элемент: {min_of_user_list}')
