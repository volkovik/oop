from itertools import chain


def draw_triangle(n: int, symbol: str) -> None:
    for i in chain(range(1, n), range(n - 2, 0, -1)):
        print(*([symbol] * i), sep='\t')


draw_triangle(5, '*')
