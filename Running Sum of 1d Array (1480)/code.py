class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        # Method 1
        # running_sum = 0
        # for i in range(len(nums)):
        #     running_sum += nums[i]
        #     nums[i] = running_sum
        # return nums
        # Method 2
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        return nums
