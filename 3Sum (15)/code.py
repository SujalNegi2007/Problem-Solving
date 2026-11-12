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
        a = 1
        b = n - 1
        for i in range(n):
            while a < b:
                if i == a or i == b:
                    break
                if nums[a] + nums[b] + nums[i] == 0:
                    temp = True
                    for j in range(len(result)):
                        if sorted([nums[a], nums[b], nums[i]]) == sorted(result[j]):
                            temp = False
                    if temp:
                        result.append([nums[a], nums[b], nums[i]])
                    a += 1
                    b -= 1
                elif nums[i] + nums[a] < -nums[b]:
                    a += 1
                elif nums[i] + nums[a] > -nums[b]:
                    b -= 1
            a = i + 2
            b = n - 1
        return result
