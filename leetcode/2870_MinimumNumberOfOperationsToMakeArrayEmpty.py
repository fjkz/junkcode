from collections import Counter

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = Counter(nums)

        def delete(n):
            m = n % 3
            if m == 0:
                return n // 3
            if m == 2:
                return n // 3 + 1
            if n >= 4:
                return 2 + (n - 4) // 3
            raise ValueError

        try:
            return sum(delete(n) for n in count.values())
        except ValueError:
            return -1

