class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        idigit = [i for i, d in enumerate(number) if d == digit]
        return str(max(int(number[:i] + number[i+1:]) for i in idigit))
