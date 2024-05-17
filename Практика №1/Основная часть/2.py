a = '485'
b = 'participate'
c = 'Needle In a Haystack'

print(a + b + c)

a = int(a)
print(f'Строка a теперь число: {a}')

symbol = input()
if symbol in b:
    print(f'Символ {symbol} был найден в строке.')
else:
    print(f'Символ {symbol} не найден в строке.')

c = c.upper()
print(c)
c = c.lower()
print(c)
