class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        a = 1
        n = len(digits)
        if digits[0] == 9 and set(digits) == {9}:
            return [1] + [0]*n
        for i in range(n-1, -1, -1):
            if a == 1:
                digits[i] += a
                a -= 1
            if digits[i] < 10:
                break
            digits[i] = 0
            a = 1
        return digits
