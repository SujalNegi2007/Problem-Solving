class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        # Method - 1
        # n = len(strs)
        # ans = ""
        # a = set()
        # minimum = float('inf')
        # for i in range(n):
        #     minimum = min(minimum, len(strs[i]))
        # for j in range(minimum):
        #     for k in range(n):
        #         a.add(strs[k][j])
        #     if len(a) != 1:
        #         return ans
        #     ans = ans + a.pop()
        # return ans
        # __________________________________________________________
        # Method - 2
        # n = len(strs)
        # ans = ""
        # a = set()
        # minimum = float('inf')
        # for i in range(n):
        #     minimum = min(minimum, len(strs[i]))
        # for j in range(minimum):
        #     for k in range(n):
        #         a.add(strs[k][j])
        #         if len(a) != 1:
        #             return ans
        #     ans = ans + a.pop()
        # return ans
        # __________________________________________________________
        # Method - 3
        n = len(strs)
        ans = ""
        minimum = float('inf')
        for i in range(n):
            minimum = min(minimum, len(strs[i]))
        for j in range(minimum):
            for k in range(n):
                if strs[0][j] != strs[k][j]:
                    return ans
            ans = ans + strs[0][j]
        return ans
