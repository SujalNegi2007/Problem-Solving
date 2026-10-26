# This one was easy as it took me just 3 mins to crack it and I thought of using Counter but then shifted to using normal dict.
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        temp = {}
        for num in nums:
            if num not in temp:
                temp[num] = 1
            else:
                temp[num] += 1
            if temp[num] > len(nums)/2:
                return num
