def score(grid):
    return sum(int("".join(str(n) for n in row), base=2) for row in grid)

def toggle(n):
    return 0 if n == 1 else 1

class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        for row in grid:
            if row[0] == 1:
                continue
            for i, n in enumerate(row):
                row[i] = toggle(n)
        m = len(grid)
        n = len(grid[0])
        for j in range(n):
            if sum(grid[i][j] for i in range(m)) > m // 2:
                continue
            for i in range(m):
                grid[i][j] = toggle(grid[i][j])

        return score(grid)
