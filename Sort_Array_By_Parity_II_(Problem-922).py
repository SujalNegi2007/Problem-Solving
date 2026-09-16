#Given an array of integers nums, half of the integers in nums are odd, and the other half are even.

#Sort the array so that whenever nums[i] is odd, i is odd, and whenever nums[i] is even, i is even.

#Return any answer array that satisfies this condition.

class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even = [x for x in nums if x % 2 == 0]
        odd = [y for y in nums if y % 2 == 1]
        ans = []
        for i in range(len(nums)):
            if i % 2 == 0:
                a = int(i/2)
                ans.append(even[a])
            else:
                b = int((i-1)/2)
                ans.append(odd[b])
        return ans
