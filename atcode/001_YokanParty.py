N, L = [int(s) for s in input().split()]
K = int(input())
A = [int(s) for s in input().split()]

pieces = [A[0]] + [A[i] - A[i-1] for i in range(1, len(A))] + [L - A[-1]]

while len(pieces) > K + 1:
    mini = min(pieces)
    i_min = [i for i, n in enumerate(pieces) if n == mini]
    min_merged = L
    i_merge = None
    for i in i_min:
        if i > 0:
            merged = pieces[i - 1] + pieces[i]
            if merged < min_merged:
                min_merged = merged
                i_merge = i - 1
        if i < len(pieces) - 1:
            merged = pieces[i] + pieces[i + 1]
            if merged < min_merged:
                min_merged = merged
                i_merge = i
    pieces[i_merge] = min_merged
    del pieces[i_merge + 1]

print(min(pieces))
