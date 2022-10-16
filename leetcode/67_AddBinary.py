from itertools import zip_longest

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        answer = []
        carryover = "0"
        for b1, b2 in zip_longest(a[::-1],b[::-1], fillvalue='0'):
            c = (b1, b2, carryover).count("1")
            if c == 0:
                answer.append("0")
                carryover = "0"
            elif c == 1:
                answer.append("1")
                carryover = "0"
            elif c == 2:
                answer.append("0")
                carryover = "1"
            else: # 3
                answer.append("1")
                carryover = "1"
        if carryover == "1":
            answer.append("1")
        return "".join(answer[::-1])
