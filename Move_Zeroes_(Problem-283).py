#Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

#Note that you must do this in-place without making a copy of the array.

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not bool(set(nums) - {0}):
            return
        write_idx = 0
        for read_idx in range(len(nums)):
            if nums[read_idx] != 0:
                nums[write_idx], nums[read_idx] = nums[read_idx], nums[write_idx]
                write_idx += 1
