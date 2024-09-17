from collections import Counter

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        words1 = s1.split()
        words2 = s2.split()
        xor_words = set(words1) ^ set(words2)
        word_count = Counter(words1 + words2)
        return [w for w in xor_words if word_count[w] == 1]
