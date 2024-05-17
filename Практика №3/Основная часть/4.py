a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


def function(matrix):
    new_matrix = []
    for i in range(len(matrix)):
        row = []
        for j in range(len(matrix[0])):
            row.append(matrix[j][i])
        new_matrix.append(row)

    return new_matrix

    return [[matrix[j][i] for i in range(len(matrix))] for i in range]


print(function(a))
