from collections import Counter

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        count = Counter(nums)
        longest = 0
        for n in count:
            if not n + 1 in count:
                continue
            longest = max(longest, count[n] + count[n + 1])
        return longest
