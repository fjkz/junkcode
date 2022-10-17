from string import ascii_lowercase

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        letters = set(sentence)
        return all(a in letters for a in ascii_lowercase)
