class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        temp = {}
        n = len(nums)
        for i in range(n):
            if nums[i] in temp:
                if abs(i-temp[nums[i]]) <= k:
                    return True
            temp[nums[i]] = i
        return False
