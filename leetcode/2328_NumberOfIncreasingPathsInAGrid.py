class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        DIVISOR = 10**9 + 7
        N = len(grid)
        M = len(grid[0])
        memo = {}

        def countPathFrom(n, m):
            if (n, m) in memo:
                return memo[(n, m)]
            count = 1
            for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                na = n + i
                ma = m + j
                if not 0 <= na < N or not 0 <= ma < M:
                    continue
                if grid[na][ma] > grid[n][m]:
                    count += countPathFrom(na, ma)
            count %= DIVISOR
            memo[(n, m)] = count
            return count

        answer = 0
        for n in range(N):
            for m in range(M):
                answer += countPathFrom(n, m)
                answer %= DIVISOR
        return answer
