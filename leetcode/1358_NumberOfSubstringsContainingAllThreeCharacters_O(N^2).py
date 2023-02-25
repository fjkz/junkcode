# O(N^2) solution
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        answer = 0
        N = len(s)
        for start in range(N-2):
            abc = {s[start], s[start+1]}
            for end in range(start + 3, N + 1):
                abc.add(s[end - 1])
                if len(abc) == 3:
                    answer += N - end + 1
                    break
        return answer
