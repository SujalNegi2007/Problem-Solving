class Solution:
    def firstUniqChar(self, s: str) -> int:
        # Method - 1
        # seen = {}
        # for i in range(len(s)):
        #     if s[i] in seen:
        #         seen[s[i]] += 1
        #     else:
        #         seen[s[i]] = 1
        # for i in range(len(s)):
        #     if seen[s[i]] == 1:
        #         return i
        # return -1
        # Method - 2
        seen = {}
        for i in range(len(s)):
            seen[s[i]] = seen.get(s[i], 0) + 1
        for i in range(len(s)):
            if seen[s[i]] == 1:
                return i
        return -1
