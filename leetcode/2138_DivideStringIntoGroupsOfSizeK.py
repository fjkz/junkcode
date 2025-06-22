class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        answer = []
        n = len(s)
        start = 0
        while (end := start + k) <= n:
            answer.append(s[start:end])
            start += k
        if start < n:
            n_fill = k - n % k
            answer.append(s[start:] + fill * n_fill)
        return answer

