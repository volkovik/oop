number = int(input())

if number > 0:
    number += 100

    if number % 2 == 0:
        number *= 2

    print(number)
elif number < 0:
    number -= 100

    if number % 2 == 1:
        number **= 2

    print(number)
else:
    print('Число равно нулю')
