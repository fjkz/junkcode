class Solution:
    def scoreOfString(self, s: str) -> int:
        values = [ord(c) for c in s]
        answer = 0
        for i in range(0, len(s) - 1):
            answer += abs(values[i] - values[i+1])
        return answer
