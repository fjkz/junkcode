# Time Limit Exceeded
from heapq import heappush, heappop
from copy import copy

class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        so = [ord(c) for c in s]
        heap = []
        for i, co in enumerate(so):
            heap_copy = copy(heap)
            while heap_copy:
                negative_len, i2 = heappop(heap_copy)
                if abs(so[i2] - co) > k:
                    continue
                heappush(heap, (negative_len - 1, i))
            else:
                heappush(heap, (-1, i))
        return - heap[0][0]
