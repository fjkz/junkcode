N = int(input())
S = [int(c) for c in input()]
T = [int(c) for c in input()]

diff_i = [i for i in range(N) if S[i] != T[i]]
if len(diff_i) % 2 != 0:
    print(-1)
    exit()

answer = ["0"] * N

s1 = sum(S[i] == 1 for i in diff_i)
t1 = sum(T[i] == 1 for i in diff_i)
num1 = abs(s1 - t1) // 2

for i, j in enumerate(diff_i):
    if len(diff_i) - i <= num1:
        answer[j] = "1"
    else:
        answer[j] = "0"

print("".join(answer))
