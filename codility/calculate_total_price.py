import sys
import math
from contextlib import redirect_stdout


def calculate_total_price(prices, discount):
    most_expensive = max(prices)
    return sum(prices) - math.ceil(discount * 0.01 * most_expensive)



# Ignore and do not change the code below
def main():
    # pylint: disable = C, W
    discount = int(input())
    n = int(input())
    prices = [int(i) for i in input().split()]
    with redirect_stdout(sys.stderr):
        price = calculate_total_price(prices, discount)
    print(price)


if __name__ == "__main__":
    main()
# Ignore and do not change the code above
