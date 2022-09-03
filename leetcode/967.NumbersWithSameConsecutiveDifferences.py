class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        answer = []
        
        def dfs(degits):
            if len(degits) == n:
                ans = sum(10**i * d for i, d in enumerate(reversed(degits)))
                answer.append(ans)
                return
            up = degits[-1] + k
            if up <= 9:
                dfs(degits + [up])
            if k == 0:
                # up == down
                return
            down = degits[-1] - k
            if down >= 0:
                dfs(degits + [down])

        for d in range(1, 10):
            dfs([d])

        return answer
