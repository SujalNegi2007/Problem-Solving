class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        a = len(nums)
        b = len(set(nums))
        if a == b:
            return False
        return True
#_________________________________________
#This one is more faster as both solution take O(n) time but last one do this while checking so if first two elements are same then second one is faster.
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()
        for i in nums:
            if i in seen:
                return True
            seen.add(i) 
        return False
