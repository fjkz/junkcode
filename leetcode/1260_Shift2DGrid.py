class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        M = len(grid)
        N = len(grid[0])
        arr = [grid[i][j] for i in range(M) for j in range(N)]
        k %= len(arr)
        arr2 = arr[-k:] + arr[:-k]
        return [[arr2[i + N * j] for i in range(N)] for j in range(M)]
