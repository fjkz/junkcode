class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        if arrLen == 1:
            return 1
        N = min(501, arrLen)
        np0 = [0 for i in range(N)]
        np0[0] = 1
        np1 = [None for i in range(N)]

        M = 10**9 + 7

        for step in range(steps):
            np1[0] = (np0[0] + np0[1]) % M
            for i in range(1, N-1):
                np1[i] = (np0[i-1] + np0[i] + np0[i+1]) % M
            np1[N-1] = (np0[N-2] + np0[N-1]) % M
            np0, np1 = np1, np0
        return np0[0]
