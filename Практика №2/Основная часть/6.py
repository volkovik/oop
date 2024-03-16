first_numbers = set([int(n) for n in input().split(' ')])
second_numbers = set([int(n) for n in input().split(' ')])

unique_numbers = list(first_numbers & second_numbers)
sorted_unique_numbers = sorted(unique_numbers)

print(f'Числа, которые находятся в обеих строчках: {sorted_unique_numbers}')
