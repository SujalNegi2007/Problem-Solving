# Method 1: Brute Force
# class Solution:
#     def maxArea(self, height: list[int]) -> int:
#         n = len(height)
#         maximum_volume = 0
#         for i in range(n):
#             for j in range(i + 1, n):
#                 if height[j] < height[i]:
#                     maximum_volume = max(maximum_volume,height[j]*(j - i))
#                 else:
#                     maximum_volume = max(maximum_volume,height[i]*(j - i))
#         return maximum_volume
# ____________________________________________________________________________________
# Method 2: Optimal
class Solution:
    def maxArea(self, height: list[int]) -> int:
        a = 0
        b = len(height) - 1
        maximum_volume = 0
        while a < b:
            if height[a] < height[b]:
                maximum_volume = max(maximum_volume, height[a] * (b - a))
                a += 1
            else:
                maximum_volume = max(maximum_volume, height[b] * (b - a))
                b -= 1
        return maximum_volume
