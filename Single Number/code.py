class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        from collections import Counter
        c = Counter(nums)
        return c.most_common()[-1][0]
