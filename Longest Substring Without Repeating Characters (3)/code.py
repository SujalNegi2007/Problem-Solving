class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # Attempt-1
        # temp = 0
        # maximum = 0
        # val = []
        # for i in range(len(s)):
        #     if s[i] not in val:
        #         val.append(s[i])
        #         temp += 1
        #         maximum = max(maximum, temp)
        #     else:
        #         val.append(s[i])
        #         for j in range(len(val)):
        #             if val[j] == s[i]:
        #                 while j+1 > 0:
        #                     val.pop(0)
        #                     j -= 1
        #                 temp = len(val)
        #                 maximum = max(maximum, temp)
        #                 break
        # return maximum
        #_______________________________________________
