# this solution exceeded time limit
from collections import defaultdict

class Solution:
    def appealSum(self, s: str) -> int:
        setcount = defaultdict(lambda: 0)
        total = 0
        for ch in s:
            setcount[frozenset()] = 1
            new_setcount = defaultdict(lambda: 0)
            for chset, num in setcount.items():
                new_setcount[chset | {ch}] += num
            setcount = new_setcount
            total += sum(len(s) * n for s, n in setcount.items())
        return total
