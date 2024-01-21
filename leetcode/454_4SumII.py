from collections import Counter

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        count12 = Counter()
        for n1, n2 in product(nums1, nums2):
            n12 = n1 + n2
            count12[n12] += 1
        count123 = Counter()
        for (n12, c12), n3 in product(count12.items(), nums3):
            n123 = n12 + n3
            count123[n123] += c12
        return sum(count123[-n4] for n4 in nums4)
