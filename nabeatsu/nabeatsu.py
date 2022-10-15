def is_nabeatsu_number(num: int) -> bool:
    return num % 3 == 0 or "3" in str(num)

for i in range(1000000):
    if not is_nabeatsu_number(i):
        print(i)
