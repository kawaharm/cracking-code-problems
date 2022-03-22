# /*
# Rotate Matrix:
# Rotate matrix 90 degrees in place (space complexity: O(1))
# */

# // Example of matrix
# // [[1,2,3],
# // [4,5,6],
# // [7,8,9]]

# // PSEUDOCODE
# // 1. TRANSPOSE MATRIX: swap matrix[i][j] with matrix[j][i]
# // 2. FLIP HORIZONTALLY: swap matrix[i][j] with matrix[i][length - 1 - i]

import math


def rotate_matrix(matrix):
    # Return false if empty string or uneven matrix
    if len(matrix) == 0 or len(matrix) != len(matrix[0]):
        return False

    n = len(matrix)

    # Step 1 Transpose
    for i in range(n):
        for j in range(i, n):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp

    # Step 2 Flip Horizontal
    for i in range(n):
        for j in range(math.floor(n/2)):
            temp = matrix[i][j]
            matrix[i][j] = matrix[i][n-1-j]
            matrix[i][n-1-j] = temp

    return matrix


# // Test Cases
matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

matrix2 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

matrix3 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

print(rotate_matrix(matrix1), '[[7, 4, 1], [8, 5, 2], [9, 6, 3]]')
print(rotate_matrix(matrix2),
      '[[13, 9, 5, 1], [14, 10, 6, 2], [15, 11, 7, 3], [16, 12, 8, 4]]')
print(rotate_matrix(matrix3), 'False')
print(rotate_matrix([]), 'False')
