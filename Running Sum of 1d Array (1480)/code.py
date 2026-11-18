class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        running_sum = 0
        for i in range(len(nums)):
            running_sum += nums[i]
            nums[i] = running_sum
        return nums
