N, A, B = [int(s) for s in input().split()]
answer = sum(i for i in range(1, N+1) if A <= sum(int(d) for d in str(i)) <= B)
print(answer)
