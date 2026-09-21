#Given a 2D integer array matrix, return the transpose of matrix.

#The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.

class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        rows, cols = len(matrix), len(matrix[0])
        # result = []
        # for c in range(cols):
        #     new_row = []
        #     for r in range(rows):
        #         new_row.append(matrix[r][c])
        #     result.append(new_row)
        # return result
        return [[matrix[r][c] for r in range(rows)] for c in range(cols)]
