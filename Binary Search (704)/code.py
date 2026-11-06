class Solution:
    def search(self, nums: list[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        middle = int((start + end)/2)
        while start <= end:
            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                end = middle - 1
            elif nums[middle] < target:
                start = middle + 1
            middle = int((start + end)/2)
        return -1
