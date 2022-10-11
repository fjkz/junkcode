# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:
from bisect import bisect_left

class Solution:
    def firstBadVersion(self, n: int) -> int:
        class dummy:
            def __len__(self):
                return n
            def __getitem__(self, i):
                return i + 1
        return bisect_left(dummy(), True, key=isBadVersion) + 1
