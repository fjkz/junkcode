class Solution:
    def trailingZeroes(self, n: int) -> int:
        a = 0
        for i in range(1, 10): # 10 is enough because 5 ** 6 = 15625
            d = n // (5 ** i)
            if d == 0:
                break
            a += d
        return a
