class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        seen = {}
        for num in nums:
            if num not in seen:
                seen[num] = 1
            else:
                seen[num] += 1
        temp = sorted(seen, key = seen.get)
        return temp[-k:]
