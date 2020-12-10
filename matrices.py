import numpy as np
import datetime
import random


# def rref(matrix):
#     # get number of rows 'n' and columns 'm' of the matrix
#     m, n = matrix.shape
#
#     # determines if any rows are all zero and puts them at the bottom of the matrix
#     for i in range(m):
#         print(matrix[i, :], matrix[i, :] == 0, '\n', matrix)
#         if False not in (matrix[i, :] == 0):
#             print(i)
#             matrix[[m - 1, i]] = matrix[[i, m - 1]]
#             m -= 1
#
#     print(matrix)
#
#     # j = 0
#     # for row in range(m):
#     #     if j >= n:
#     #         return matrix
#     #
#     #     i = row
#     #     while matrix[i, j] == 0:
#     #         i += 1
#     #         if i == m:
#     #             i = row
#     #             j += 1
#     #             if j == n:
#     #                 return matrix
#
#     return matrix


def det(matrix):
    m, n = matrix.shape

    # check if matrix is square
    if m != n:
        return None

    # check if matrix is a 2 x 2
    if m == 2:
        return matrix[0, 0] * matrix[1, 1] - matrix[1, 0] * matrix[0, 1]

    # find the submatrices and then take their determinants
    det_total = 0
    for i in range(n):
        # removes the first row and specified column
        submat = np.delete(matrix, 0, 0)
        submat = np.delete(submat, i, 1)
        sub_det = det(submat)
        det_total += sub_det * matrix[0, i] * ((-1) ** i)

    return det_total


if __name__ == '__main__':
    big_matrix = np.array([[10, 3, 9, 7, 10, 9, 8, 9, 3, 3], [5, 10, 5, 4, 3, 4, 10, 7, 8, 7], [2, 9, 7, 2, 4, 10, 10, 9, 3, 8], [8, 4, 6, 1, 4, 3, 8, 10, 6, 4], [5, 4, 7, 7, 5, 8, 5, 9, 4, 7], [10, 10, 4, 8, 4, 3, 6, 6, 2, 2], [5, 5, 8, 7, 3, 7, 7, 8, 5, 9], [4, 9, 6, 9, 4, 4, 9, 6, 7, 9], [4, 2, 6, 10, 3, 1, 3, 3, 1, 6], [3, 3, 4, 5, 5, 10, 2, 8, 10, 1]])

    test_matrix = np.array([[1,4,3,4],[9,8,7,6],[5,4,3,2],[5,7,9,10]])

    start_time = datetime.datetime.now()
    print(det(big_matrix))
    print(datetime.datetime.now() - start_time)


