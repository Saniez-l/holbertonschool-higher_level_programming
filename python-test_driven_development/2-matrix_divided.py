#!/usr/bin/python3

def matrix_divided(matrix, div):
    # check if matrix is list of list of int or float
    if not isinstance(matrix, list) or matrix == []:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for row in matrix:
        if not isinstance(row, list) or row == []:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        for elem in row:
            if not isinstance(elem, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    # check if all rows have same size
    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")
    # check if div is int or float
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    # check if div is 0
    if div == 0:
        raise ZeroDivisionError("division by zero")
    # make new matrix, not change the original
    new_matrix = []
    for i in range(len(matrix)):
        new_row = []
        for j in range(len(matrix[i])):
            # divide and round 2 decimal
            new_row.append(round(matrix[i][j] / div, 2))
        new_matrix.append(new_row)
    return new_matrix
