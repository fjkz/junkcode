from collections import Counter

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        count12 = Counter(n1 + n2 for n1, n2 in product(nums1, nums2))
        count34 = Counter(n3 + n4 for n3, n4 in product(nums3, nums4))
        return sum(c12 * count34[-n12] for n12, c12 in count12.items())
