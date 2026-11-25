class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Method - 1
        # return len(s.strip().split()[-1])
        # ________________________________________
        # Method - 2
        # ans = 0
        # for i in range(len(s)-1, -1, -1):
        #     if s[i] == " ":
        #         if ans != 0:
        #             return ans
        #         continue
        #     ans += 1
        # return ans
