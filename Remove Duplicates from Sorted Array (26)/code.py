# Used Two Pointers Here.
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        b = 0
        seen = set()
        for i in range(len(nums)):
            if nums[i] not in seen:
                seen.add(nums[i])
                nums[b] = nums[i]
                b += 1
        return len(seen)
