class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        n = len(nums)
        a = 0
        for i in range(n):
            if nums[i] != val:
                nums[a], nums[i] = nums[i], nums[a]
                a += 1
        return a
