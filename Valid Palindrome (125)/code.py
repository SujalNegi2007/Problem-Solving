class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Method 1: This takes extra space as we build a new list just to check if it's palindrome or not.
        # result = []
        # for i in range(len(s)):
        #     if s[i].isalnum():
        #         result.append(s[i].lower())
        # return result == result[::-1]
        # ____________________________________________________________________________________________________________
        # Method 2: This is optimal with O(n) time, O(1) space.
        a = 0
        b = len(s) - 1
        while a < b:
            if not s[a].isalnum():
                a += 1
                continue
            elif not s[b].isalnum():
                b -= 1
                continue
            elif s[a].lower() != s[b].lower():
                return False
            a += 1
            b -= 1
        return True
