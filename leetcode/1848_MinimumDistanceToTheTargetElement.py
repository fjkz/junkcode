from itertools import zip_longest

class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        for i, (l, r) in enumerate(zip_longest(nums[start::-1], nums[start:])):
            if l == target or r == target:
                return i
