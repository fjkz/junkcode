class Solution:
    def sumZero(self, n: int) -> List[int]:
        pairs = [ [i, -i] for i in range(1, n // 2 + 1) ]
        answer = sum(pairs, [])
        if n % 2 == 1:
            return [0] + answer
        return answer
