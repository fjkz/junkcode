from collections import Counter

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        duplicated = [n for n, c in count.items() if c == 2][0]
        loss = [n for n in range(1, len(nums) + 1) if count[n] == 0][0]
        return [duplicated, loss]
