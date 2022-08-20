# Minimal wallet problem solver
#
# How mush we should pay for minimizing the number of coins?

from copy import copy

# Japanese yen coins
coin_kind = [1, 5, 10, 50, 100, 500]


def minimal_coin_set(value):
    # greedy algorithm
    ret = {}
    for coin in sorted(coin_kind, reverse=True):
        ret[coin] = value // coin
        value %= coin
    return ret


def coin_combinations(coin_set, min_value=0):
    kinds = [k for k in coin_set.keys()]
    comb = []
    counts = {k: 0 for k in kinds}
    while all([counts[k] <= coin_set[k] for k in kinds]):
        if sum([k * counts[k] for k in kinds]) >= min_value:
            comb.append(copy(counts))
        counts[kinds[0]] += 1
        for i, k in enumerate(kinds[:-1]):
            if counts[k] <= coin_set[k]:
                break
            counts[k] = 0
            counts[kinds[i + 1]] += 1
    return comb


def minimal_change_payment(price, wallet):
    if isinstance(wallet, int):
        wallet = minimal_coin_set(wallet)
    min_pay_set = None
    min_wallet = None

    options = coin_combinations(wallet, price)
    for pay in options:
        pay_value = sum([k * n for k, n in pay.items()])
        change = minimal_coin_set(pay_value - price)
        wallet_remain = {k: wallet[k] - pay[k] + change[k] for k in wallet.keys()}
        if (not min_wallet
            or (sum(wallet_remain.values()) < sum(min_wallet.values()))
            or (sum(wallet_remain.values()) == sum(min_wallet.values())
                and sum(pay.values()) < sum(min_pay_set.values()))):
            min_pay_set = pay
            min_wallet = wallet_remain
    return min_pay_set


if __name__ == "__main__":
    END = 49  # limit of terminal width
    print("  |", end="")
    for i in range(1, END):
        print("{:2d} ".format(i), end="")
    print("")
    print("=" * 3 * END)
    for price in range(1, END):
        print("{:2d}|".format(price), end="")
        for wallet in range(1, price):
            print("   ", end="")
        for wallet in range(price, END):
            pay = minimal_change_payment(price, wallet)
            pay_value = sum([k * n for k, n in pay.items()])
            print("{:2d} ".format(pay_value), end="")
        print("")
