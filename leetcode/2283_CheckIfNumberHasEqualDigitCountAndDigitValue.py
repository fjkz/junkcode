from collections import Counter

class Solution:
    def digitCount(self, num: str) -> bool:
        counter = Counter(num)
        return all(int(num[i]) == counter[str(i)] for i in range(len(num)))
