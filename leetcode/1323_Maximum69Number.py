class Solution:
    def maximum69Number (self, num: int) -> int:
        dd = [ d for d in str(num) ]
        for i, d in enumerate(dd):
            if d == '6':
                dd[i] = '9'
                break
        return int(''.join(dd))
