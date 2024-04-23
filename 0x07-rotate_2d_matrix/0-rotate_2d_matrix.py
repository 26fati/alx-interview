#!/usr/bin/python3
''' an n x n 2D matrix, rotate it 90 degrees clockwise.'''


def rotate_2d_matrix(matrix):
    '''
    an n x n 2D matrix, rotate it 90 degrees clockwise.
    '''
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in range(len(matrix)):
        matrix[i].reverse()
