from collections import Counter

class Solution:
    def minimumPushes(self, word: str) -> int:
        return sum((i // 8 + 1) * n for i, n in enumerate(sorted(Counter(word).values(), reverse=True)))
