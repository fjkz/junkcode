from string import digits

class Solution:
    def secondHighest(self, s: str) -> int:
        dd = sorted(set(c for c in s if c in digits))
        if len(dd) < 2:
            return -1
        return dd[-2]
