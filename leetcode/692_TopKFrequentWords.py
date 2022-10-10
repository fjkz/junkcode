from collections import Counter 
from heapq import heapify, heappop

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)
        heap = [(-t[1], t[0]) for t in count.items()]
        heapify(heap)
        return [heappop(heap)[1] for _ in range(k)]
