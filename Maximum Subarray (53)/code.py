class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        maximum = max(nums)
        for i in range(len(nums)):
            total = 0
            for j in range(i,len(nums)):
                total += nums[j]
                maximum = max(maximum, total)
        return maximum
