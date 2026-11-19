class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        # Method - 1
        # ans = []
        # temp = set(nums)
        # for i in range(1, len(nums)):
        #     if i not in temp:
        #         ans.append(i)
        # return ans
        # ___________________________________________________________
        # Method - 2: using O(1) space complexity
        ans = []
        for i in range(len(nums)):
            position = abs(nums[i])-1
            nums[position] = -abs(nums[position])
        for i in range(len(nums)):
            if nums[i] > 0:
                ans.append(i+1)
        return ans
