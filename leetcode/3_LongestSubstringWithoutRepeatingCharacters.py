class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        working_set = set()
        working_start = 0
        for i, c in enumerate(s):
            if c in working_set:
                j = working_start
                while s[j] != c:
                    working_set.remove(s[j])
                    j += 1
                working_start = j + 1
                continue
            working_set.add(c)
            longest = max(longest, len(working_set))
        return longest
