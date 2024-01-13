from collections import Counter

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count_s = Counter(s)
        count_t = Counter(t)
        char_kinds = set(s + t)
        up = 0
        #down = 0
        for ch in char_kinds:
            num_ch_s = count_s[ch]
            num_ch_t = count_t[ch]
            diff = num_ch_s - num_ch_t
            if diff > 0:
                up += diff
            #elif diff < 0:
            #    down += - diff
        #assert up == down
        return up
