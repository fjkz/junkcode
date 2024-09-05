from functools import reduce
from operator import or_

class Solution:
    def maximumXOR(self, nums: List[int]) -> int:
        return reduce(or_, nums)
