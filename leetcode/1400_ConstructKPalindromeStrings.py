from collections import Counter

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False
        count = Counter(s)
        odd = [c for c, n in count.items() if n % 2 != 0]
        return len(odd) <= k
