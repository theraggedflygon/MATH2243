import numpy as np


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
        num = sub_det * matrix[0, i] * (-1 ** i)
        det_total += sub_det * matrix[0, i] * ((-1) ** i)

    return det_total


if __name__ == '__main__':
    test_matrix = np.array([[1, -3, -1, 3], [1, 0, 2, 0], [3, 4, -5, 1], [7, 8, 10, 6]]).astype(np.float64)
    tm2 = np.array([[1, 2], [3, 4]])
    tm3 = np.array([[1, 4, 5], [6, 7, 8], [9, 12, 4]])
    print(det(test_matrix))
