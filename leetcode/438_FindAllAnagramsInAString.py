from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []

        chcnt_p = Counter(p)
        chcnt_w = Counter(s[:len(p)])

        answer = []
        if chcnt_w == chcnt_p:
            answer.append(0)

        for i1 in range(len(p), len(s)):
            i0 = i1 - len(p)
            c0 = s[i0]
            chcnt_w[c0] -= 1
            c1 = s[i1]
            chcnt_w[c1] += 1
            if chcnt_w == chcnt_p:
                 answer.append(i0 + 1)
        return answer
