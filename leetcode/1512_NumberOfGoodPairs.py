from collections import Counter
from math import comb

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        return sum(comb(n, 2) for n in Counter(nums).values())
