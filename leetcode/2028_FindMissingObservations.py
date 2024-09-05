class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        sum_n = mean * (n + len(rolls)) - sum(rolls)
        base = sum_n // n
        remain = sum_n - base * n
        if base < 1 or base > 6 or (base == 6 and remain > 0):
            return []
        if base == 6:
            return [6] * n
        n6 = remain // (6 - base)
        fraction = remain % (6 - base)
        return [6] * n6 + [base + fraction] + [base] * (n - n6 - 1)
