A = int(input())
B = int(input())
C = int(input())
X = int(input())
coins = [(500, A), (100, B), (50, C)]
def backtrack(total, coins):
    if total == 0:
        return 1
    if not coins:
        return 0
    value, n = coins[0]
    count = 0
    for i in range(n + 1):
        if value * i > total:
            break
        count += backtrack(total - value * i, coins[1:])
    return count
print(backtrack(X, coins))
