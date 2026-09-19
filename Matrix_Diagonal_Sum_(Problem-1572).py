#Given a square matrix mat, return the sum of the matrix diagonals.

#Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal.

class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        a = len(mat[0])
        total_sum = 0
        for i in range(a):
            total_sum += mat[i][i]
            total_sum += mat[i][a-1-i]
            if (i, i) == (i, a-1-i):
                total_sum -= mat[i][a-1-i]
        return total_sum
