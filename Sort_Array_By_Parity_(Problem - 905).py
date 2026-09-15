#Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

#Return any array that satisfies this condition.

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        a = [x for x in nums if x % 2 == 0]
        b = [y for y in nums if y % 2 == 1]
        for z in b:
            a.append(z)
        return a
