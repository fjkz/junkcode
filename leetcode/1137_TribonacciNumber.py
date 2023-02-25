class Solution:
    def tribonacci(self, n: int) -> int:
        T = [None] * max(3, n + 1)
        T[0] = 0
        T[1] = 1
        T[2] = 1
        for i in range(3, n + 1):
            T[i] = T[i-3] + T[i-2] + T[i-1]
        return T[n]
