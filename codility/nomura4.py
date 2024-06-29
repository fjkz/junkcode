def solution(S):
    S = S.lstrip('0')
    answer = 1
    for b in S[1:]:
        if b == "0":
            answer += 1
        else:
            answer += 2
    return answer
