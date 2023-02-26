class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        N = len(word1)
        M = len(word2)
        distance = [[None] * (M + 1) for i in range(N + 1)]

        for i in range(N + 1):
            distance[i][0] = i
        for j in range(1, M + 1):
            distance[0][j] = j

        for i in range(1, N + 1):
            for j in range(1, M + 1):
                if word1[i - 1] != word2[j - 1]:
                    replace = 1
                else:
                    replace = 0
                distance[i][j] = min(
                    distance[i-1][j] + 1,
                    distance[i][j-1] + 1,
                    distance[i-1][j-1] + replace
                )

        return distance[N][M]
