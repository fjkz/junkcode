WATER = "0"
LAND = "1"

def removeIsland(grid, i, j):
    m = len(grid)
    n = len(grid[0])
    if not 0 <= i < m or not 0 <= j < n:
        return
    if grid[i][j] == WATER:
        return
    grid[i][j] = WATER
    for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        removeIsland(grid, i + di, j + dj)

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        answer = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == WATER:
                    continue
                answer += 1
                removeIsland(grid, i, j)
        return answer
