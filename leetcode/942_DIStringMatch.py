class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        top = 0
        buttom = 0
        perm = [0]
        for label in s:
            if label == 'I':
                top += 1
                perm.append(top)
            else:
                buttom -= 1
                perm.append(buttom)
        return [val - buttom for val in perm]
