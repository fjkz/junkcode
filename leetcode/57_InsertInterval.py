from bisect import insort_left

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        insort(intervals, newInterval)
        merged = [intervals[0]]
        for start, end in intervals[1:]:
            last = merged[-1]
            if last[1] >= start:
                last[1] = max(last[1], end)
            else:
                merged.append([start, end])
        return merged
