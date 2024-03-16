a, b = int(input()), float(input())
print(f'{a=}, {b=}')

a, b = b, a
print(f'{a=}, {b=}')

print(f'a + b = {a + b}, a - b = {a - b}, a * b = {a * b}')
