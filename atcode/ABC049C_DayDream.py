def can_accept(s: str) -> bool:
    words = ["dream", "dreamer", "erase", "eraser"]
    stack = [0]
    while stack:
        i = stack.pop()
        if i == len(s):
            return True
        for w in words:
            if s[i:].startswith(w):
                stack.append(i + len(w))
    return False

S = input()
if can_accept(S):
    print("YES")
else:
    print("NO")
