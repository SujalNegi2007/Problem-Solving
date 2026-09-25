#Given an m x n matrix of distinct numbers, return all lucky numbers in the matrix in any order.

#A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.

class Solution:
    def luckyNumbers(self, matrix: list[list[int]]) -> list[int]:
        a = []
        result = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == min(matrix[i]):
                    for k in range(len(matrix)):
                        a.append(matrix[k][j])
                    if matrix[i][j] == max(a):
                        result.append(matrix[i][j])
                        return result
                    else:
                        a = []
        return []
