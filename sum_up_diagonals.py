def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """

    # return (matrix[0][0] + matrix[1][1] + matrix[1][0] + matrix[0][1])

    # return matrix[0][0] + matrix[1][1] + matrix[2][2] + matrix[2][0] + matrix[1][1] + matrix[0][2]


    n = len(matrix)
    diagonal1 = 0
    diagonal2 = 0
    
    for i in range(0, n):
        diagonal1 += matrix[i][i]
        diagonal2 += matrix[n-i-1][i]
    return diagonal1 + diagonal2


