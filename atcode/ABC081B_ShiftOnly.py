N = int(input())
A = [int(a) for a in input().split()]
count = 0
while all(i % 2 == 0 for i in A):
    A = [i // 2 for i in A]
    count += 1
print(count)
