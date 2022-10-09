from collections import defaultdict
from copy import copy

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        charcount = defaultdict(int)
        for c in chars:
            charcount[c] += 1

        def good(word):
            count = copy(charcount)
            for c in word:
                if c in count and count[c] > 0:
                    count[c] -= 1
                    continue
                return False
            return True  

        answer = 0
        for word in words:
            if good(word):
                answer += len(word)
        return answer
