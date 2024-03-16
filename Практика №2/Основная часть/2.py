from sys import stdin

summary = 0

for line in stdin:
    line = line.rstrip()
    if line.lstrip('-').isnumeric():
        summary += int(line)
    else:
        print('Не является числом')

print(f'Сумма введенных чисел: {summary}')
