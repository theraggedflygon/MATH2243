import numpy as np


def rref(matrix):
    # get the shape of the matrix and set up counters
    m, n = matrix.shape
    i = 0
    j = 0

    # iterate through the matrix
    while i < m and j < n:
        # find the pivot and its index
        pivot = max(abs(matrix[i:m, j]))

        if pivot == 0:
            j += 1
            continue

        p_idx = abs(A[i:m, j]).tolist().index(pivot)
        p_idx += i

        i == 1 and print(pivot, p_idx)

        # swap rows i and p_idx
        matrix[[i, p_idx]] = matrix[[p_idx, i]]
        # divide the pivot row by pivot value
        matrix[i, :] /= matrix[i, j]
        # cancel out the i-th column in other rows using the pivot column
        for r in range(i + 1, m):
            matrix[r, :] -= (matrix[r, j] * matrix[i, :])

        for r in range(i):
            matrix[r, :] -= (matrix[r, j] * matrix[i, :])

        i += 1
        j += 1

    return matrix


if __name__ == '__main__':
    A = np.array([[2, 3, 1, 4], [3, 3, 4, 6], [1, 2, 2, 3]], dtype=float)
    print(rref(A))
