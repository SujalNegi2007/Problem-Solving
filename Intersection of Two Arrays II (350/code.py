class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        result = []
        nums1.sort()
        nums2.sort()
        a = 0
        b = 0
        while a < len(nums1) and b < len(nums2):
            if nums1[a] == nums2[b]:
                result.append(nums1[a])
                a += 1
                b += 1
            elif nums1[a] > nums2[b]:
                b += 1
            else:
                a += 1
        return result
