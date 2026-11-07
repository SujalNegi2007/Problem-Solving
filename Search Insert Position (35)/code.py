class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        middle = int((start + end)/2)
        if target < nums[0]:
            return 0
        while start <= end:
            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                end = middle - 1
            elif nums[middle] < target:
                start = middle + 1
            try:
                if nums[middle] > target and target > nums[middle - 1]:
                    return middle
                middle = int((start + end)/2)
            except:
                middle = int((start + end)/2)
        return len(nums)
