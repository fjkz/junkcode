class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original_color = image[sr][sc]
        found = set()
        def dfs(i, j):
            if (i, j) in found:
                return
            if image[i][j] != original_color:
                return
            found.add((i, j))
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni = i + di
                nj = j + dj
                if not (0 <= ni < len(image) and 0 <= nj < len(image[0])):
                    continue
                dfs(ni, nj)
        dfs(sr, sc)
        for i, j in found:
            image[i][j] = color
        return image
