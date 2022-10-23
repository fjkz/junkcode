class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [[None] * (i + 1) for i in range(len(triangle))]
        dp[0] = triangle[0]
        for i in range(1, len(triangle)):
            for j in range(i+1):
                if j == 0:
                    dp[i][j] = dp[i-1][j] + triangle[i][j]
                elif j == i:
                    dp[i][j] = dp[i-1][j-1] + triangle[i][j]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j-1]) + triangle[i][j]
        return min(dp[-1])
