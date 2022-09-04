def is_nabeatsu_number(num: int) -> bool:
    if num % 3 == 0:
        return True
    while num > 0:
        if num % 10 == 3:
            return True
        num //= 10
    return False

for i in range(1000000):
    if not is_nabeatsu_number(i):
        print(i)
