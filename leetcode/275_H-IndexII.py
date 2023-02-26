class Solution:
    def hIndex(self, citations: List[int]) -> int:
        N = len(citations)
        for i, nc in enumerate(citations):
            if nc >= N - i:
                return N - i
        return 0
