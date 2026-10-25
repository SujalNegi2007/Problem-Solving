# Got Stuck as what to do but looking at question for more than 30 mins gave me bit of idea. I was even able to look through my screen as that much time I spent solving this problem. God Bless My Eyes.
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        temp = {}
        for i in range(len(strs)):
            sorted_strs = "".join(sorted(strs[i]))
            if sorted_strs in temp:
                temp[sorted_strs].append(strs[i])
            else:
                temp[sorted_strs] = [strs[i]]
        ans = []
        for key in temp.keys():
            ans.append(temp[key])
        return ans
