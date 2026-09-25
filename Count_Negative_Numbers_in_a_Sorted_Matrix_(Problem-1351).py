#Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid.

class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        result = 0
        if len(grid) == 0:
            return 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] < 0:
                    result += 1
        return result
