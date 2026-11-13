class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # result = []
        # n = len(nums)
        # for i in range(n):
        #     for j in range(i+1, n):
        #         for k in range(j+1, n):
        #             if nums[i] + nums[j] + nums[k] == 0:
        #                 temp = [nums[i], nums[j], nums[k]]
        #                 a = True
        #                 for l in range(len(result)):
        #                     if sorted(result[l]) == sorted(temp):
        #                         a = False
        #                 if a:
        #                     result.append(temp)
        # return result
        # ---------------------------------------------------------------------------------
        # Method -2
        result = []
        n = len(nums)
        nums.sort()
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            a = i+1
            b = n-1
            while a < b:
                if nums[a] + nums[b] + nums[i] == 0:
                    result.append([nums[i], nums[a], nums[b]])
                    a += 1
                    b -= 1
                    while a < b and nums[a] == nums[a-1]:
                        a += 1
                elif nums[i] + nums[a] < -nums[b]:
                    a += 1
                elif nums[i] + nums[a] > -nums[b]:
                    b -= 1
        return result
