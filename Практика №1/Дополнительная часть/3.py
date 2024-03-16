year = int(input())

animal_years = ('Крысы, Быка, Тигра, Зайца, '
                'Дракона, Змеи, Лошади, Овцы, '
                'Обезьяны, Петуха, Собаки, Свиньи').split(', ')

index = year % 12 - 4 if year % 12 >= 4 else 11 - 3 - year % 12

print(f'Вы родились в год {animal_years[index]}')
