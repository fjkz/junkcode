class Solution:
    def minLength(self, s: str) -> int:
        if (i := s.find("AB")) >= 0:
            return self.minLength(s[:i] + s[i+2:])
        elif (j := s.find("CD")) >= 0:
            return self.minLength(s[:j] + s[j+2:])
        else:
            return len(s)
