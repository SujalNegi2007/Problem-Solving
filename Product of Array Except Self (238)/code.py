class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
#___________________________________________________________________________
        # Answer 1 With O(n^2) time complexity
        # answer = []
        # a = 1
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         a *= nums[j]
        #     for k in range(i):
        #         a *= nums[k]
        #     answer.append(a)
        #     a = 1
        # return answer
#___________________________________________________________________________
        # Answer 2 With O(n) Time Complexity
        temp = [1]
        right_multiplied = 1
        for j in range(len(nums)-1, 0,-1):
            right_multiplied *= nums[j]
            temp.append(right_multiplied)
        temp.reverse()

        answer = []
        left_multiplied = 1
        for i in range(len(nums)):
            if i != 0:
                left_multiplied *= nums[i-1]
            answer.append(left_multiplied*temp[i])

        return answer
