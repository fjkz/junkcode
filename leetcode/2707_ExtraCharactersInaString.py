class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        d = set(dictionary)
        dp = [None] * (len(s) + 1)
        dp[0] = 0
        for i in range(1, len(dp)):
            dp[i] = 51
            for j in range(i): 
                extra = 0 if s[j:i] in d else i - j
                dp[i] = min(dp[i], dp[j] + extra)
        return dp[-1]
