#!/usr/bin/python3
"""Rotates 2D matrix 90 degrees clockwise"""


def rotate_2d_matrix(matrix):
    """
    Employs nested loops to iterate through each element in the matrix.
    It exchanges the values of each element with those situated at the
    corresponding positions in the rotated matrix
    """

    n = len(matrix)
    for i in range(n // 2):
        for j in range(i, n - i - 1):
            temp = matrix[i][j]
            matrix[i][j] = matrix[n - j - 1][i]
            matrix[n - j - 1][i] = matrix[n - i - 1][n - j - 1]
            matrix[n - i - 1][n - j - 1] = matrix[j][n - i - 1]
            matrix[j][n - i - 1] = temp
