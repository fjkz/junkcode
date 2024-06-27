def solution(A, B, K):
    if A % K == 0:
        a = A // K
    else:
        a = A // K + 1
    b = B // K
    return b - a + 1
