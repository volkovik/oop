number = int(input())

if number in range(1, 128):
    print(f'Число {number} входит в диапазон чисел')
else:
    print(f'Число {number} не входит в диапазон чисел')
