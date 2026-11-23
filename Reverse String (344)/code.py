class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        for i in range(int(n/2)):
            s[i], s[n-1-i] = s[n-1-i], s[i]
