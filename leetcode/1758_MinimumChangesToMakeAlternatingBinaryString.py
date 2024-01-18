class Solution:
    def minOperations(self, s: str) -> int:
        alt0 = ['0' if n % 2 else '1' for n in range(len(s))]
        alt1 = ['1' if n % 2 else '0' for n in range(len(s))]
        return min(sum(c != a for c, a in zip(s, alt)) for alt in [alt0, alt1])
