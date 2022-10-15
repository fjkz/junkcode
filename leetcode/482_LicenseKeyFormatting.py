class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace("-", "").upper()
        answer = []
        for i, c in enumerate(reversed(s)):
            if i % k == 0 and i != 0:
                answer.append("-")
            answer.append(c)
        return "".join(reversed(answer))
