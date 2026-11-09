class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        n = len(numbers)
        a = 0
        b = n - 1
        while a < b:
            if numbers[a] + numbers[b] == target:
                return [a+1, b+1]
            elif target - numbers[b] < numbers[a]:
                b -= 1
            elif target - numbers[b] > numbers[a]:
                a += 1
