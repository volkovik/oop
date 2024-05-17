first_matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
second_matrix = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]


def sum_matrix(m1, m2):
    return [[m1[i][j] + m2[i][j] for j in range(len(m1[i]))]
            for i in range(len(m1))]


print(*sum_matrix(first_matrix, second_matrix), sep='\n')
