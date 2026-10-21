class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0 or len(s) == 0:
            return False
        plate = []
        pairs = {'[' : ']', '{' : '}', '(' : ')', '"':'"'}
        for ch in s:
            if ch in pairs:
                plate.append(ch)
            else:
                if len(plate) == 0 or pairs[plate[-1]] != ch:
                    return False
                plate.pop()
        return len(plate) == 0
