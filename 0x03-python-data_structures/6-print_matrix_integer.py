#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    for mat in matrix:
        if len(mat) == 0:
            print ()
        for number in range(len(mat)):
            print("{}".format(mat[number]), end="\n"
                  if number is len(mat) - 1
                  else " ")
