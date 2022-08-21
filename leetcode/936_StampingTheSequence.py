class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        N = len(target)
        s = [c for c in target]
        answer = []
        while any(s[i] is not None for i in range(N)):
            if len(answer) > 10 * N:
                return []
            for i in range(N - len(stamp) + 1):
                if (any(s[i + j] is not None for j in range(len(stamp))) and
                    all(s[i + j] is None or s[i + j] == c for j, c in enumerate(stamp))): 
                    answer.append(i)
                    for j in range(len(stamp)):
                        s[i + j] = None
                    break
            else:
                return []
        return reversed(answer)
