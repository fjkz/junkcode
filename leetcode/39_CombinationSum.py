from itertools import product

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = set(candidates)
        dp = [None] * 41
        dp[1] = set()
        for i in range(2, target + 1):
            dp[i] = set()
            if i in candidates:
                dp[i].add((i,))
            for j in range(1, i // 2 + 1):
                combination = {tuple(sorted(a + b)) for a, b in product(dp[j], dp[i-j])}
                dp[i].update(combination)
        return dp[target]
