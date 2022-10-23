from collections import deque
from string import digits

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        answer = []
        q = deque([""])
        while q:
            w = q.pop()
            if len(w) == len(s):
                answer.append(w)
                continue
            ns = s[len(w)]
            if ns in digits:
                q.appendleft(w + ns)
                continue
            q.appendleft(w + ns.lower())
            q.appendleft(w + ns.upper())
        return answer
