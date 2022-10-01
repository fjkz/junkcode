class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        n = len(grid)
        face_back = sum(grid[i][j] != 0 for j in range(n) for i in range(n))
        side1 = sum(grid[0][j] for j in range(n))
        side2 = sum(grid[n-1][j] for j in range(n))
        side3 = sum(grid[i][0] for i in range(n))
        side4 = sum(grid[i][n-1] for i in range(n))
        mid1 = sum(abs(grid[i][j] - grid[i][j+1]) for j in range(n-1) for i in range(n))
        mid2 = sum(abs(grid[i][j] - grid[i+1][j]) for j in range(n) for i in range(n-1))
        return 2 * face_back + side1 + side2 + side3 + side4 + mid1 + mid2
