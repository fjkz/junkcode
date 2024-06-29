from collections import Counter

def solution(S):
    count = Counter(int(c) for c in S)

    wing = ""
    for n in range(9, 0, -1):
        m = count[n] // 2
        wing += str(n) * m
    if wing:
        wing += "0" * (count[0] // 2)
    
    center = ""
    for n in range(9, -1, -1):
        if count[n] % 2 >= 1:
            center = str(n)
            break

    if not wing and not center:
        return "0"
    return wing + center + wing[::-1]
