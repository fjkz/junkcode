from math import sqrt, floor

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a = 0
        b = floor(sqrt(c))
        while a <= b:
            n = a * a + b * b
            if n == c:
                return True
            if n < c:
                a += 1
            else:
                b -= 1
        return False
