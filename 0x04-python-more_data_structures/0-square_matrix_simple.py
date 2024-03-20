#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    matrixResult = []
    for row in matrix:
        result = []
        for element in row:
            result.append(element ** 2)
        matrixResult.append(result)
    return matrixResult
