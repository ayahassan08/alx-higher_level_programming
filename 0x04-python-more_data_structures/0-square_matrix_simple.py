#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    matrixResult = []
    for row in matrix:
        result = []
        for number in row:
            result.append(number ** 2)
        matrixResult.append(result)
    return matrixResult
