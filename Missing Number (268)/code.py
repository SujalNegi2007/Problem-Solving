class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        # Method - 1
        # temp = set(nums)
        # for i in range(len(nums)+1):
        #     if i not in temp:
        #         return i
        # ___________________________________
        # Method - 2
        # nums.sort()
        # for i in range(len(nums)):
        #     if nums[i] != i:
        #         return i
        # return len(nums)
        # ___________________________________
        # Method - 3
        a = 0
        for i in range(len(nums)):
            a += i
        total = sum(nums)
        a += len(nums)
        return a - total
