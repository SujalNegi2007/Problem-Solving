class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        # Method - 1
        # for i in range(len(nums)):
        #     nums[i] *= nums[i]
        # return sorted(nums)
        # -------------------------------------------------------
        # Method - 2
        n = len(nums)
        a = 0
        b = n - 1
        ans = [0] * n
        for i in range(n-1, -1, -1):
            if abs(nums[a]) > abs(nums[b]):
                ans[i] = nums[a]**2
                a += 1
            else:
                ans[i] = nums[b]**2
                b -= 1
        return ans
