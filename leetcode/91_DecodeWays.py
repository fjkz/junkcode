class Solution:
    def numDecodings(self, s: str) -> int:
        code = [str(i) for i in range(1, 27)]
        N = len(s)
        dp = [0] * N

        if s[0] in code:
            dp[0] = 1

        if N >= 2:
            if s[0:2] in code:
                dp[1] += 1
            if s[1] in code:
                dp[1] += dp[0]

        for i in range(2, N):
            if s[i-1:i+1] in code:
                dp[i] += dp[i-2]
            if s[i] in code:
                dp[i] += dp[i-1]

        return dp[-1]
