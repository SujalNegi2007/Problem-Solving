class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        # Attempt-1
        # nums_set = set(nums)
        # copy_set = set(nums)
        # max_ele = max(nums_set)
        # try:
        #     copy_set.remove(max_ele)
        #     copy_set.remove(max(copy_set))
        #     return max(copy_set)
        # except:
        #     return max_ele
        #--------------------------------------------------------------------

        # Attempt-2
        # first, second, third = float('-inf'), float('-inf'), float('-inf')
        # for num in nums:
        #     if num >= first:
        #         if num != first:
        #             third, second, first = second, first, num
        #     elif num >= second:
        #         if num != second:
        #             third, second = second, num
        #     elif num >= third:
        #         third = num
        # return third if third != float('-inf') else first
