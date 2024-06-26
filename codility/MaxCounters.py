def solution(N, A):
    base = 0
    max_val = 0
    counter = [0] * N
    for n in A:
        if n == N + 1:
            base = max_val
            continue
        counter[n - 1] = max(base, counter[n - 1]) + 1
        max_val = max(max_val, counter[n - 1])
    return [max(base, n) for n in counter]
