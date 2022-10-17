from itertools import product

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def erase_island(i, j):
            if grid[i][j] == 0:
                return 0
            grid[i][j] = 0
            count = 1
            for di, dj in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
                ni = i + di
                nj = j + dj
                if not (0 <= ni < len(grid) and 0 <= nj < len(grid[0])):
                    continue
                count += erase_island(ni, nj)
            return count

        max_island = 0
        for i, j in product(range(len(grid)), range(len(grid[0]))):
            if grid[i][j] == 0:
                continue
            area = erase_island(i, j)
            max_island = max(max_island, area)
        return max_island
