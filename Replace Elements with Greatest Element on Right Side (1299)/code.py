class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:

        # Attempt-1
        # for i in range(len(arr)):
        #     maximum = -1
        #     if i+1 < len(arr):
        #         maximum = max(arr[i+1:])
        #     arr[i] = maximum
        # return arr
        #_______________________________________
        
        # Attempt-2
        # maximum = -1
        # i = len(arr) - 2
        # copy = arr[:]
        # while i > -1:
        #     curr = copy[i+1]
        #     maximum = max(maximum, curr)
        #     arr[i] = maximum
        #     i -= 1
        # arr[-1] = -1
        # return arr
        #_______________________________________
        
        #Attempt-3
        # maximum = -1
        # curr = arr[-1]
        # for i in range(len(arr)-1,-1,-1):
        #     maximum = max(maximum, curr)
        #     curr = arr[i]
        #     arr[i] = maximum
        # arr[-1] = -1
        # return arr
        #_______________________________________

        Attempt-4
        maximum = -1
        for i in range(len(arr)-1,-1,-1):
            arr[i], maximum = maximum, max(arr[i], maximum)
        return arr
        
