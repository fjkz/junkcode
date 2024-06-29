def solution(S):
    answer = 1
    curset = set()
    for c in S:
        if c in curset:
            answer += 1
            curset = set([c])
            continue
        curset.add(c)
    return answer
