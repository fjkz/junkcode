def checkPalindrome(word):
    n = len(word)
    if n % 2 == 0:
        return word[:n//2] == word[n-1: n//2-1: -1] 
    return word[:n//2] == word[n-1: n//2: -1] 

class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if checkPalindrome(word):
                return word
        return ''
