class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        N = len(palindrome)
        for i, char in enumerate(palindrome[:N//2]):
            if char == "a":
                continue
            return palindrome[:i] + 'a' + palindrome[i+1:]
        if N >= 2:
            return palindrome[:-1] + 'b'
        return ""
