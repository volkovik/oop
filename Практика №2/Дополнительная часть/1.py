from random import randint

guess_number = randint(1, 100)

print('Угадайте загаданное число')
amount_of_attempts = int(input('Введите количество попыток: '))

while amount_of_attempts > 0:

    user_number = int(input('\nВведите число: '))

    if user_number == guess_number:
        print('\nВы угадали загаданное число')
        break
    elif user_number > guess_number:
        print('Загаданное число меньше введенного', end='')
    else:
        print('Загаданное число больше введенного', end='')

    print(f' (осталось попыток: {amount_of_attempts - 1})')
    amount_of_attempts -= 1
else:
    print('Попытки закончились')
    print(f'Загаданное число: {guess_number}')
