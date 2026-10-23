class Solution:
    def isValid(self, s: str) -> bool:
        check = {"{":"}", "[":"]", "(":")"}
        temp = []
        for ch in s:
            if ch in check:
                temp.append(check[ch])
            else:
                if ch == temp[-1]:
                    temp.pop()
                elif not temp or ch != temp.pop():
                    return False
        return True if temp == [] else False
