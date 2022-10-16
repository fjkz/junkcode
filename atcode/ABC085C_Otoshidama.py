N, Y = [int(s) for s in input().split()]
if Y % 1000 != 0:
    print(-1, -1, -1)
    exit(1)
y = Y // 1000
n1 = 0
while (x := y - N - 9 * n1) >= 0:
    if x % 4 == 0:
        n2 = x // 4
        n3 = N - n1 - n2
        if n3 >= 0:
            assert 10000 * n1 + 5000 * n2 + 1000 * n3 == Y
            print(n1, n2, n3)
            break
    n1 += 1
else:
    print(-1, -1, -1)
    exit(1)
