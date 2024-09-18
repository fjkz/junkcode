from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def cmp(a, b):
            return int(b + a) - int(a + b)
        answer =  "".join(sorted(map(str, nums), key=cmp_to_key(cmp)))
        if answer.startswith("0"):
            return "0"
        return answer
