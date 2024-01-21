class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        if len(nums) <= 2:
            return max(nums)
        dp = [None] * N
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, N):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        return dp[N-1]
