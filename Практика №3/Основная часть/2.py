N, M = int(input('Введите N: ')), int(input('Введите M: '))
X, Y = int(input('Введите X: ')), int(input('Введите Y: '))


def function(n, m, x, y):
    return n <= x and y <= m


if function(N, M, X, Y):
    print('Диапазон от x до y входят в диапазон от n до m')
else:
    print(f'Диапазон от x до y не входят в диапазон от n до m')
