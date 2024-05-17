from sys import stdin

user_data = [int(line.strip()) for line in stdin]


def a_function(numbers):
    return sum(filter(lambda n: -50 < n < 50, numbers))


def b_function(numbers):
    return [
        n ** 2 for n in numbers
        if n % 2 == 0 and -50 < n < 0
    ]


def c_function(numbers):
    numbers = [n for n in numbers if -50 < n < 50]
    return max(numbers) - min(numbers)


print(f'Сумма всех чисел: {a_function(user_data)}')
print(f'Квадраты отрицательных четных чисел: {b_function(user_data)}')
print(f'Разность макс. и мин. чисел: {c_function(user_data)}')
