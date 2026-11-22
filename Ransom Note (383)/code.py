class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Method - 1
        # temp = list(ransomNote)
        # for i in range(len(magazine)):
        #     if magazine[i] in temp:
        #         temp.remove(magazine[i])
        # return not temp
        # Method - 2
        # temp_magazine = {}
        # for i in range(len(magazine)):
        #     if magazine[i] in temp_magazine:
        #         temp_magazine[magazine[i]] += 1
        #     else:
        #         temp_magazine[magazine[i]] = 1
        # temp_ransomNote = {}
        # for i in range(len(ransomNote)):
        #     if ransomNote[i] in temp_ransomNote:
        #         temp_ransomNote[ransomNote[i]] += 1    
        #     else:
        #         temp_ransomNote[ransomNote[i]] = 1
        # for i in range(len(ransomNote)):
        #     try:
        #         if temp_magazine[ransomNote[i]] - temp_ransomNote[ransomNote[i]] < 0:
        #             return False
        #     except:
        #         return False
        # return True
        # Method - 3
        temp_magazine = {}
        for i in range(len(magazine)):
            if magazine[i] in temp_magazine:
                temp_magazine[magazine[i]] += 1
            else:
                temp_magazine[magazine[i]] = 1
        temp_ransomNote = {}
        for i in range(len(ransomNote)):
            if ransomNote[i] in temp_ransomNote:
                temp_ransomNote[ransomNote[i]] += 1    
            else:
                temp_ransomNote[ransomNote[i]] = 1
        a = set(ransomNote)
        b = list(a)
        for i in range(len(b)):
            try:
                if temp_magazine[b[i]] - temp_ransomNote[b[i]] < 0:
                    return False
            except:
                return False
        return True
