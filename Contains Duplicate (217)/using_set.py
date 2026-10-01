class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        a = len(nums)
        b = len(set(nums))
        if a == b:
            return False
        return True
