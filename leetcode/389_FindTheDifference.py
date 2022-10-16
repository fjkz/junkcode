from collections import Counter

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count_s = Counter(s)
        count_t = Counter(t)
        for c, n in count_t.items():
            if not c in count_s or count_s[c] < n:
                return c
