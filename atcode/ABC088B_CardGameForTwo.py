N = int(input())
a = [int(s) for s in input().split()]
a.sort(reverse=True)
alice = sum(score for i, score in enumerate(a) if i % 2 == 0)
bob = sum(score for i, score in enumerate(a) if i % 2 != 0)
print(alice - bob)
