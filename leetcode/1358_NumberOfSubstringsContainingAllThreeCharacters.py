# O(NlogN) solution
import bisect

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        answer = 0
        indicies = dict()
        for a in 'abc':
            indicies[a] = [i for i, c in enumerate(s) if c == a]
        for begin in range(len(s)-2):
            first_index = dict()
            for a in 'abc':
                i = bisect.bisect_left(indicies[a], begin)
                if i == len(indicies[a]):
                    first_index[a] = len(s)
                else:
                    first_index[a] = indicies[a][i]
            end = max(first_index.values()) + 1
            answer += len(s) - end + 1
        return answer
