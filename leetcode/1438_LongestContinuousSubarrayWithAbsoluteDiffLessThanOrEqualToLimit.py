from heapq import heappush, heappop

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        def cut_left(heap, left):
            while heap[0][1] < left:
                heappop(heap)

        max_length = 0
        max_heap = []
        min_heap = []
        left = 0
        for right, nr in enumerate(nums):
            heappush(max_heap, (- nr, right))
            heappush(min_heap, (+ nr, right))

            while - max_heap[0][0] - min_heap[0][0] > limit:
                left = min(max_heap[0][1], min_heap[0][1]) + 1
                cut_left(max_heap, left)
                cut_left(min_heap, left)

            max_length = max(max_length, right - left + 1)
        return max_length
