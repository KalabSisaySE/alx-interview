#!/usr/bin/python3
"""the 0-rotate_2d_matrix module
defines the function `rotate_2d_matrix`
"""


def rotate_2d_matrix(matrix):
    """rotates the given `matrix` 90 degrees clockwise, in-place"""
    new_matrix = []
    for i in range(len(matrix)):
        temp = []
        for li in reversed(matrix):
            temp.append(li[i])
        new_matrix.append(temp)

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            matrix[i][j] = new_matrix[i][j]
