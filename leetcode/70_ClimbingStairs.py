from math import comb

class Solution:
    def climbStairs(self, n: int) -> int:
        return sum(comb(n - n2, n2) for n2 in range(0, n // 2 + 1))
