/* 
Rotate Matrix:
Rotate matrix 90 degrees in place (space complexity: O(1))
*/

// Example of matrix
// [[1,2,3],
// [4,5,6],
// [7,8,9]]

// PSEUDOCODE
// 1. TRANSPOSE MATRIX: swap matrix[i][j] with matrix[j][i]
// 2. FLIP HORIZONTALLY: swap matrix[i][j] with matrix[i][length - 1 - i]

const rotateMatrix = function (matrix) {
    // Return false if empty matrix or uneven matrix
    if (matrix.length == 0 || matrix.length !== matrix[0].length) return false;

    let n = matrix.length;

    // Step 1 TRANSPOSE MATRIX
    for (let i = 0; i < n; i++) {
        for (let j = i; j < n; j++) {
            let temp = matrix[i][j];
            matrix[i][j] = matrix[j][i];
            matrix[j][i] = temp;
        }
    }

    // Step 2 FLIP HORIZONTALLY
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < (n / 2); j++) {
            let temp = matrix[i][j];
            matrix[i][j] = matrix[i][n - 1 - j];
            matrix[i][n - 1 - j] = temp;
        }
    }

    return matrix;
}

// Test Cases
let matrix1 =
    [[1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]

let matrix2 =
    [[1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]]

let matrix3 =
    [[1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]]

console.log(rotateMatrix(matrix1), '[[7, 4, 1], [8, 5, 2], [9, 6, 3]]');
console.log(rotateMatrix(matrix2), '[[13, 9, 5, 1], [14, 10, 6, 2], [15, 11, 7, 3], [16, 12, 8, 4]]');
console.log(rotateMatrix(matrix3), 'false');
console.log(rotateMatrix([]), 'false');