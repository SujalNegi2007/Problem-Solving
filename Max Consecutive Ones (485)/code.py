class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        #---------------------------------------
        # Attempt 1:
        # a = "0"
        # for num in nums:
        #     a = str(num) + a
        # return len(max(a.split("0")))
        #----------------------------------------
        # Attempt 2:
        # cons_ones = 0
        # a = set()
        # for i in range(len(nums)):
        #     if nums[i] == 1 and i == len(nums) - 1:
        #         cons_ones += 1
        #         a.add(cons_ones)
        #     elif nums[i] == 1:
        #         cons_ones += 1
        #     else:
        #         a.add(cons_ones)
        #         cons_ones = 0
        # return max(a)
        #----------------------------------------
        # Attempt 3:
        cons_ones = 0
        max_cons = 0
        for num in nums:
            if num == 1:
                cons_ones += 1
                max_cons = max(max_cons, cons_ones)
            else:
                cons_ones = 0
        return max_cons
