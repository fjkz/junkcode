from heapq import heapify, heappush, heappop

class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        heap = [- n for n in inventory]
        heapify(heap)
        answer = 0
        for i in range(orders):
            value = - heappop(heap)
            answer += value
            answer %= 10**9 + 7
            if value >= 1:
                heappush(heap, - value + 1)
        return answer
