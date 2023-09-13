#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square_matrix = [[number ** 2 for num in row] for row in matrix]
    return square_matrix
