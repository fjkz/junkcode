from bisect import bisect_left

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i, n in enumerate(numbers[:-1]):
            m = target - n
            j = bisect_left(numbers, m, lo=i+1)
            if j < len(numbers) and numbers[j] == m:
                return [i+1, j+1]
