#You are given a 0-indexed array of distinct integers nums.

#There is an element in nums that has the lowest value and an element that has the highest value. We call them the minimum and maximum respectively. 
#Your goal is to remove both these elements from the array.

#A deletion is defined as either removing an element from the front of the array or removing an element from the back of the array.

#Return the minimum number of deletions it would take to remove both the minimum and maximum element from the array.

class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        a = []
        for i in range(len(nums)):
            if nums[i] == max(nums) or nums[i] == min(nums):
                a.append(i)
        b = sorted(a)
        if len(nums) >= 2:
            x = len(nums) - len(nums[b[0]+1:b[1]])
            y = len(nums) - len(nums[b[1]+1:])
            z = len(nums) - len(nums[:b[0]])
        else:
            x = 1
            y = 1
            z = 1
        return min(x,y,z)
