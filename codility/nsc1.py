from collections import Counter

def solution(S):
    count = Counter(S)
    nb = count["B"]
    na = count["A"] // 3
    nn = count["N"] // 2
    return min(na, nb, nn)
