from math import log2, floor

class Solution:
    def countBits(self, n: int) -> List[int]:
        answer = [None] * (n + 1)
        answer[0] = 0
        for i in range(1, n + 1):
            r = 2 ** floor(log2(i))
            answer[i] = 1 + answer[i-r]
        return answer
