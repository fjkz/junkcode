class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        NY = len(mat)
        NX = len(mat[0])
        answer = [[None] * NX for _ in range(NY)]
        
        for x0 in range(- NY + 1, NX):
            diagonal_cells = []
            diagonal_nums = []
            for y in range(0, NY):
                x = x0 + y
                if 0 <= x < NX:
                    diagonal_cells.append((y, x))
                    diagonal_nums.append(mat[y][x])
            
            diagonal_nums.sort()
            
            for (j, i), n in zip(diagonal_cells, diagonal_nums):
                answer[j][i] = n
        return answer
