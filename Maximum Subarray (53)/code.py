# Only passed 202 cases as it reached time limit.
# class Solution:
#     def maxSubArray(self, nums: list[int]) -> int:
#         maximum = max(nums)
#         for i in range(len(nums)):
#             total = 0
#             for j in range(i,len(nums)):
#                 total += nums[j]
#                 maximum = max(maximum, total)
#         return maximum

# Finally Solved after using two max at one loop for the first time.
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        best_sum = nums[0]
        maximum = nums[0]
        for i in range(1, len(nums)):
            maximum = max(nums[i], maximum + nums[i])
            best_sum = max(best_sum, maximum)
        return best_sum
