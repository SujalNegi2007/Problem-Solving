# Attempt-1
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)):
#             for j in range(len(nums)):
#                 if i != j:
#                     if nums[i] + nums[j] == target:
#                         return [i,j]
#____________________________________________________________________

# Attempt-2
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        viewed = {}
        for i in range(len(nums)):
            if target - nums[i] not in viewed.keys():
                viewed[nums[i]] = i
            else:
                return [i, viewed[target-nums[i]]]
