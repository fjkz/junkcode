# It solves another problem: we can insert character any place, not front of the string.

from collections import deque
from string import ascii_lowercase

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        memo = {c: deque() for c in ascii_lowercase}
        for i, c in enumerate(s):
            memo[c].append(i)

        left_wing = []
        left = 0
        right = len(s) - 1
        while left < right:
            cl = s[left]
            cr = s[right]
            if cl == cr:
                left_wing.append(cl)
                left += 1
                right -= 1
                continue
            while memo[cr] and memo[cr][0] <= left:
                memo[cr].popleft()
            if memo[cr]:
                nearest_cr = memo[cr][0]
            else:
                nearest_cr = -1
            while memo[cl] and memo[cl][-1] >= right:
                memo[cl].pop()
            if memo[cl]:
                nearest_cl = memo[cl][-1]
            else:
                nearest_cl = len(s)
            if nearest_cr - left < - (nearest_cl - right):
                left_wing.append(cl)
                left += 1
            else:
                left_wing.append(cr)
                right -= 1

        left_str = "".join(left_wing)
        if left == right:
            return left_str + s[left] + left_str[::-1]
        return left_str + left_str[::-1]
