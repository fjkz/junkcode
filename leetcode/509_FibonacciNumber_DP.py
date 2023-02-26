class Solution:
    def fib(self, n: int) -> int:
        dp = [None] * max(2, n + 1)
        dp[0] = 0
        dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = dp[i-2] + dp[i-1]
        return dp[n]