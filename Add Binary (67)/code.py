#Made by Sujal.
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        temp1 = list(a)
        temp2 = list(b)
        num1, num2 = 0, 0
        for i in range(len(temp1)-1,-1,-1):
            if temp1[i] == "1":
                num1 += 2**(len(temp1) - 1 - i)
        for j in range(len(temp2)-1,-1,-1):
            if temp2[j] == "1":
                num2 += 2**(len(temp2) - 1 - j)
        num = num1 + num2
        ans = []
        if num == 0:
            return "0"
        while num > 0:
            if num % 2 == 1:
                ans.append("1")
                num = num//2
            else:
                ans.append("0")
                num = num//2
        ans = reversed(ans)
        return "".join(ans)
