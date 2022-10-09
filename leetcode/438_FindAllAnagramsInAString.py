from string import ascii_lowercase

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []

        chcnt_p = {ch: 0 for ch in ascii_lowercase}
        for ch in p:
            chcnt_p[ch] += 1

        chcnt_w =  {ch: 0 for ch in ascii_lowercase}
        for ch in s[:len(p)]:
            chcnt_w[ch] += 1

        answer = []
        if all(chcnt_w[ch] == chcnt_p[ch] for ch in ascii_lowercase):
            answer.append(0)

        for i1 in range(len(p), len(s)):
            i0 = i1 - len(p)
            c0 = s[i0]
            chcnt_w[c0] -= 1
            c1 = s[i1]
            chcnt_w[c1] += 1
            if all(chcnt_w[ch] == chcnt_p[ch] for ch in ascii_lowercase):
                 answer.append(i0 + 1)
        return answer
