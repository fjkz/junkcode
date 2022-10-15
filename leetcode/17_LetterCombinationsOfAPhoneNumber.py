from itertools import product

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
                   "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        letters = [mapping[d] for d in digits]
        # altough product([]) -> [], product() -> [()]
        if not letters:
            return []
        return ["".join(combination) for combination in product(*letters)]
